---
title: DADIU_Proj
date: 2023-10-18 11:11:27
tags: unity
categories: Unity
---

Problems and Learnings during the DADIU project.

<!--more-->

The game is called "I inherited a castle" and this is the [link](https://dadiu.itch.io/i-inherited-a-castle).

# Make an interactive object

### Add a trigger Area so when players step on it they can interact with some game objects

### add the object to interact

### Make a script to do the interact

 use "onTriggerEnter" to check if a player is in the area, and use an "inputAction" to bind an input method, then define an interact function to define what will be triggered after the input starts, and also need to bind that onenable. The code are as follows:

The "require component" means it needs to have a collider component on this object.

"ontriggerenter" needs two objects both have a collider and one of them is a trigger. If it's set to trigger then it cannot collide any more.

To add an event in inspector we need to use "UnityEvent" and to run it we need to use `event?.Invoke()`.

```c#
using System;
using UnityEngine;
using UnityEngine.Events;
using UnityEngine.InputSystem;

namespace LivingMansion._Scripts.Interact
{
    [RequireComponent(typeof(Collider))]
    public class InteractTrigger : MonoBehaviour
    {
        [SerializeField] private InputAction action = new();
        public UnityEvent interactEvent;
        private bool canInteract = false;

        private void OnEnable()
        {
            action.Enable();
            action.started += Interact;
        }

        private void OnDisable()
        {
            action.Disable();
            action.started -= Interact;
        }
        
        private void Interact( InputAction.CallbackContext context)
        {
            
            if (canInteract)
            {
                interactEvent?.Invoke();
            }
        }
        

        private void OnTriggerEnter(Collider other)
        {
            canInteract = true;
        }

        private void OnTriggerExit(Collider other)
        {
            canInteract = false;
        }
    }
}

```

### Add interactive UI

Add a canvas with a text on it, and deactivate it. And write another script that on trigger enter invoke an event to activate the canvas.

# Open a door slowly

### Add a door object

In order to make it rotate from one side of the door we need to add a door hinge which is an empty parent to the actual door. make the parent to be on the side of the door and apply the opendoor script on it.

Here I use a slerp to do the rotation and it's based on the "isOpen" variable.

```csharp
using UnityEngine;

public class OpenDoor : MonoBehaviour
{
    public float openAngle = 90f; 
    public float openSpeed = 2f;

    private bool isOpen = false;
    private Quaternion initialRotation;
    private Quaternion targetRotation;
    private bool finishRotation = true;
    private void Start()
    {
        // Store the initial rotation of the door.
        initialRotation = transform.rotation;
        targetRotation = Quaternion.Euler(transform.eulerAngles + new Vector3(0, openAngle, 0));
    }

    private void FixedUpdate()
    {
        finishRotation = false;
        // Rotate the door towards the target rotation.
        transform.rotation = Quaternion.Slerp(transform.rotation, 
            isOpen ? targetRotation : initialRotation, Time.fixedDeltaTime * openSpeed);
        finishRotation = true;
        
    }

    public void ToggleDoor()
    {
        if (finishRotation)
        {
            isOpen = !isOpen;
        }
    }
}

```

# Implement wwise sound into the project

It needs to have an AKBank component in the scene to manage the sound, also it needs to have an AkGameobj to calculate the distance from player to the object. Then to play a sound you need a script which receive a wwise event using `public AK.Wwise.Event sound;` and then trigger the sound with `sound.Post(gameObject);`.

### Implement sound effects to footsteps of the player

To make it sounds differently on different surfaces, we need to have a script to do the switch like follows:
```c#
using UnityEngine;


namespace LivingMansion._Scripts.Footsteps
{
    public class FootstepsMaterialSwitcher : MonoBehaviour
    {
        private RaycastHit hit;
        private string currentMaterial;
        private string previousMaterial = "Default";
        private void FixedUpdate()
        {
            if (Physics.Raycast(transform.position,-transform.up, out RaycastHit hit,2f))
            {
                
                if (hit.collider.TryGetComponent(out FootstepsMaterialSound sound))
                {
                    currentMaterial = sound.materialName;
                    if(currentMaterial != previousMaterial)
                    {
                        Debug.Log("Material: " + currentMaterial);
                        previousMaterial = currentMaterial;
                        AkSoundEngine.SetSwitch("Material", currentMaterial, gameObject);
                    }
                    
                }
            }
        }
       

    }
}
```

Here FootstepMaterialSound is a class which have a string called materialName. It uses raycasting to detect the surface under the player and send a switch to wwise engine whenever the material changes.

# Implement timed interaction object

Effect:  after interacting with an object(like press e) a series of different events will be triggered and each of them can have a wait time, which will make it wait for x seconds to invoke.

Implement:

```c#
using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Events;
using UnityEngine.InputSystem;

[Serializable]
class CustomAction
{
    public string actionName;
    public int waitTime;
    public UnityEvent action;
}
public class TimedInteractionObject : MonoBehaviour
{
    [SerializeField] private InputAction action = new();
    [SerializeField] private CustomAction[] customActions;
    private int runningCoroutineCount = 0;
    private void OnEnable()
    {
        action.Enable();
        action.started += Interact;
    }
    
    private void OnDisable()
    {
        action.Disable();
        action.started -= Interact;
    }
    
    private void Interact(InputAction.CallbackContext ctx)
    {
        if (runningCoroutineCount != 0)
        {
            Debug.Log("Already running coroutines: "+runningCoroutineCount);
            return;
        }
            
        foreach (var customAction in customActions)
        {
            StartCoroutine(InteractWithWaitTimeCoroutine(customAction));
        }
    }
    
    private IEnumerator InteractWithWaitTimeCoroutine(CustomAction customAction)
    {
        runningCoroutineCount++;
        yield return new WaitForSeconds(customAction.waitTime);
        customAction.action?.Invoke();
        runningCoroutineCount--;
    }
}

```

In this code, I defined a class "CustomAction" to store actions the designer may need to add, which contains a string, wait time and the action needed. Then Use InputAction to let them define the action needed to trigger. On enable it will listen to the action and then do the Interact function.

The interact function needs the parameter to receive the action activity, and then for each action, it will create a new coroutine to wait for some seconds and run the action.

To prevent the player from interacting multiple times while the actions are running, I use a variable to count the running coroutines, when it begins it +=1, and when it's done it will subtract 1.

# Implement puzzle-winning manager

Effect: In the game, there are different puzzles to be solved. I want to implement a manager that checks conditions to be met and then triggers some events.

Implement:

```c# 
using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[Serializable]
public class RotationData
{
    public string ConditionName;
    public GameObject RoomSectionGameObject;
    public RotationObject PaintingGameObject;
    public Vector3 DesiredRotationForRoomSection;


    public RotationData(GameObject obj, Vector3 angles)
    {
        RoomSectionGameObject = obj;
        DesiredRotationForRoomSection = angles;
    }
}

[Serializable]
public class SerializableEvent
{
    public string eventName;
    public UnityEngine.Events.UnityEvent unityEvent;
}

public class PuzzleWinningManager : MonoBehaviour
{
    [HideInInspector]
    public string comment;

    public string puzzleName;

    [SerializeField]
    private List<RotationData> ConditionsToBeMet;

    [SerializeField]
    private List<SerializableEvent> ActionsWhenPuzzleIsSolved = new List<SerializableEvent>();


    public void AreAllRotationsEqual()
    {
        StartCoroutine(CheckRotations());
    }

    private IEnumerator CheckRotations()
    {
        // This could be checked only once in Awake or in AreAllRotationsEqual
        CheckThatAllImportantFieldsAreFilled();

        bool allCorrect = true;
        foreach (var rotationData in ConditionsToBeMet)
        {
            // rotationData.PaintingGameObject.GetComponent<RotationPainting>() could be fetched 
            bool isRotating = rotationData.PaintingGameObject.GetComponent<RotationObject>().rotating;
            if (isRotating)
            {
                float waitTime = 10.0f; //max waiting time is 10s
                float timer = 0.0f;

                while (isRotating && timer < waitTime)
                {
                    // Doesn't need to be checked every frame necessarily 
                    // https://docs.unity3d.com/ScriptReference/WaitForSeconds.html
                    yield return null;
                    timer += Time.deltaTime;
                    isRotating = rotationData.PaintingGameObject.GetComponent<RotationObject>().rotating;
                }

                if (isRotating)
                {
                    Debug.Log("Rotation took too long.");
                    yield break; 
                }
            }

            // Check if the angle is correct
            Quaternion currentRotation = rotationData.RoomSectionGameObject.transform.rotation;
            Vector3 currentRotationAngles = currentRotation.eulerAngles;

            if (currentRotationAngles != rotationData.DesiredRotationForRoomSection)
            {
                Debug.Log(rotationData.RoomSectionGameObject.name + " Section should be " + rotationData.DesiredRotationForRoomSection + " and it's currently " + currentRotationAngles);
                allCorrect = false;
            }
            else
            {
                Debug.Log(rotationData.RoomSectionGameObject.name + " is correct");
            }
        }
        if (allCorrect)
        {
            //All the conditions are met and run the actions
            Debug.Log("The Puzzle: '" + puzzleName + "' is Correct!");
            foreach (var eventAction in ActionsWhenPuzzleIsSolved)
            {
                eventAction.unityEvent.Invoke();
            }
        }
        
        
    }

    private void CheckThatAllImportantFieldsAreFilled()
    {
        string fieldNameBeingChecked;

        foreach (var rotationData in ConditionsToBeMet)
        {
            if (rotationData.PaintingGameObject == null)
            {
                fieldNameBeingChecked = "Painting GameObject";
                Debug.LogWarning("ERROR: You have not attached a: " + fieldNameBeingChecked.Color("yellow") + " for the Condition: " + rotationData.ConditionName.Color("yellow"));

            }

            if (rotationData.RoomSectionGameObject == null) 
            {
                fieldNameBeingChecked = "Room Section GameObject";
                Debug.LogWarning("ERROR: You have not attached a: " + fieldNameBeingChecked.Color("yellow") + " for the Condition: " + rotationData.ConditionName.Color("yellow"));
            }
        }
    }
}

public static class StringExtension
{
    // This is an extension method so we can modify strings in the editor (fx in the debug console).
    // The first parameter takes the "this" modifier
    // and specifies the type for which the method is defined.
    
    public static string Bold(this string str) => "<b>" + str + "</b>";
    public static string Color(this string str, string clr) => string.Format("<color={0}>{1}</color>", clr, str);
    public static string Italic(this string str) => "<i>" + str + "</i>";
    public static string Size(this string str, int size) => string.Format("<size={0}>{1}</size>", size, str);
}
```

Here I first defined two different classes for designers to fill in, they can change the name and actions they want. Then in the main class, I make a function to check are all the conditions are met. It's a coroutine because the event will last for some time. For each rotation, it will wait for max 10 seconds, and then check if the rotating angle is correct. If all is correct it will invoke the actions one by one.

Also, there's a function to check if all important fields are filled so that if not it will give a debug log about the error.

# Implement timeline feature

Need a trigger, a director and a camera

## Trigger

only add a trigger script. In this script add a `public PlayableDirector timelineDirector` and use the on-trigger enter function, if the other object is a player then use `timelineDirector.Play()` and then deactivate the object.

## Director

The director game object needs two components, one is "Playable Director" to make the timeline work and the other one is "Signal Receiver" to disable player input while doing the timeline.

### Make a playable timeline

First, create a timeline file, and open it. Inside add a new cinemachine track. Then add a virtual cinemachine camera in the scene, and place it in some place. Then drag the new camera in the track, set the ease in and ease out duration and it's done

### Add signal receiver

create two new signals and assign them to the timeline at the correct time, and then set them with reactions to enable and disable player input.

# Implement in-game menu

## Switch between fullscreen and windowed

Use `Screen.fullScreenMode` . Set this property to one of the values in FullScreenMode to change the display mode of your application.

> fullScreenWindow: 
>
> All platforms. Sets your application window to the full-screen native display resolution, covering the whole screen. This full-screen mode is also known as 'borderless full screen'. Unity renders your application at the resolution set by a script, or the native display resolution if no resolution is set, and scales your application to fill the window. Unity adds black bars ('letterboxing') to the rendered output to match the display aspect ratio, to prevent content stretching. The operating system's overlay UI, such as input method editor (IME) window, displays on top of the full-screen window.
>
> ExclusiveFullScreen:
>
> Windows platforms only. Sets your application so it has sole full-screen use of a display. Unlike FullScreenMode.FullScreenWindow, this mode changes the operating system resolution of the display to match the application's chosen resolution. On platforms other than Windows, this mode falls back to FullScreenMode.FullScreenWindow.
>
> Windowed:
>
> Desktop platforms only. Sets your application to a standard, movable window that's not full screen. The size of the window depends on your application's resolution.

# Implement footstep sound on different surfaces

First need to attach either a tag or an enum type to all the surfaces to show the material of the surface.

Then use raycasting to detect what kind of material you are stepping on. In the following code, I use a variable to track current material and then when the ray cast detects the material change it will send a signal to the wwise engine to change the footstep sound.

As the model of the character has a centre at its feet, sometimes the ray cast may start below the surface, so I need to add an offset to the source point of the ray cast.

The hard point for this task is to first ray cast correctly when the gravity of the player changes, which means the player will no longer walk on the ground but instead walk on the wall or even on the ceiling. In this case, the ray cast needs to have the offset based on the current gravity. I 

Then

```c#
using System;
using LivingMansion._Scripts.Player;
using UnityEngine;

namespace LivingMansion._Scripts.Footsteps
{
    public class FootstepsMaterialSwitcher : MonoBehaviour
    {
        private string previousMaterial = "";
        public AK.Wwise.Event MyEvent;
        private Player.Player player;

        
        private void Start()
        {
            //Set default as Wood
            AkSoundEngine.SetSwitch("Material", "Wood", gameObject);
            previousMaterial = "Wood";
            player = FindObjectOfType<Player.Player>();
        }

        public void PlayFootstepSound()
        {
            MyEvent.Post(gameObject);
        }

        private void FixedUpdate()
        {
            //based on the current gravity direction, raycast downwards to find the material
            //need to add an offset
            Vector3 offest = -player.customCharacter.Gravity.normalized;
            Vector3 newpos = transform.position + offest;
            RaycastHit[] hits = Physics.RaycastAll(newpos, -transform.up, 10f);
            System.Array.Sort(hits, (x, y) => x.distance.CompareTo(y.distance));
            // Debug.DrawRay(newpos, -transform.up * 10f, Color.red, 1f);

            foreach (RaycastHit hit in hits)
            {
                if (hit.collider != null && hit.collider.TryGetComponent(out FootstepsMaterialSound sound))
                {
                    string currentMaterial = sound.materialName.ToString();
                    // Debug.Log(currentMaterial);   
                    if (currentMaterial != previousMaterial)
                    {
                        Debug.Log("Material: " + currentMaterial);
                        previousMaterial = currentMaterial;
                        AkSoundEngine.SetSwitch("Material", currentMaterial, gameObject);
                    }
                    // Only consider the first encountered material
                    break;
                }
            }
        }
    }
}
```

# Make cube appear and disappear effect

First, make a appear script, this needs to be done using a coroutine to prevent block main game.

Then do it in a separate function to be called somewere.

```
private IEnumerator ScaleDownAndDeactivate(GameObject obj, GameObject connectedSoundObject)
{
    CubeDisappearSound.Post(gameObject);
    connectedSoundObject.SetActive(false);
    Vector3 originalScale = obj.transform.localScale;
    float currentTime = 0;

    while (currentTime < 0.7f)
    {
        // Scale down the object over time
        obj.transform.localScale = Vector3.Lerp(originalScale, Vector3.zero, currentTime / 0.7f);
        currentTime += Time.deltaTime;
        yield return null;
    }

    // Deactivate the object
    obj.SetActive(false);
}
```

```csharp
public void MakeCubeDisappear()
        {
            GameObject obj = gameObject.transform.GetChild(3).gameObject;
            GameObject connectedSoundObject = gameObject.transform.GetChild(1).gameObject;
            StartCoroutine(ScaleDownAndDeactivate(obj, connectedSoundObject));
        }
```

