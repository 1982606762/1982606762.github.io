---
title: swift学习
date: 2021-12-03 20:50:14
tags:
categories: swift
---

udemy [iOS & Swift - The Complete iOS App Development Bootcamp](https://www.udemy.com/course/ios-13-app-development-bootcamp/) 学习笔记

<!--more-->

# 使用xcode

在view中使用上方的加号可以添加元素，点击元素在右侧可以修改属性

使用assistant分屏左侧view右侧controller的时候点control并将元素拖到右边可以创建链接，按钮需要放到最下边并使用UIButton

![image-20211203214120296](https://gitee.com/Squirrel_01/img/raw/master/img/image-20211203214120296.png)

> control+I自动格式化
>
> cmd+shift+B分析代码

## 在storyboard中修改按钮圆角

![image-20211206191909648](https://gitee.com/Squirrel_01/img/raw/master/img/image-20211206191909648.png)

在这里新增`` layer.cornerRadius`` 即可

## 可视化选择UIColor和Img

Xcode13之后变成了``#colorLiteral()`` 和 ``#imgLiteral()`` 来快速选择

Xcode13之前可以使用 ``color literal``来自动补全

## 使用自带图形SFSymbol

点imageview，右边image下拉菜单找或者输入名字

## Dark Mode

将颜色设置成label或者Systemcolor就可以随系统变化

自定义颜色：

1. 在Assets.xcassets里左下角点加号新增一个color set，然后分别自定义各个颜色

自定义图片：

![image-20211220185034330](https://gitee.com/Squirrel_01/img/raw/master/img/image-20211220185034330.png)



## 分割线和自定义快捷输入

分割线是``//MARK: - ``

选中函数右键，create code snippet可以新建快捷输入	

# Swift基础

用var声明变量，用let声明常量。

获取随机数：
Int.random(in:begin...end)
Int.random(in:begin..<end)不包含end
Float.random(in:begin...end)获取浮点随机数

arr.shuffle()可以将数组打乱顺序

字符串可以直接用加号连接

## for循环建议使用

```swift
for _ in 0..<6{
  
}
```

也支持

```swift
let titleText = "⚡️FlashChat"
for letter in titleText{
    print(letter)
}
```





## if语句

```swift
if a == 1{
  xxx
}else{
  xxx
}
```

## switch语句

```swift
let num = Int.random(in: 0...100)
switch num {
case 1:
    print(1)
case 2:
    print(2)
default:
    print("hello!")
}

```

## Swift range

> a...b closed Range  [a,b]
>
> a..<b half open Range  [a,b)
>
> ...b One sided Range [1,b]

## Dictionary

```swift
let dic = [:]
let dic : [String:Int] = ["aaa":123]
```

## Optional

一个变量如果可能是nil就是一个optional变量，如果用到某个变量，他有可能是nil，并且是nil的时候会崩溃，就需要使用optional变量

> string   普通string
> String? optional string

```swift
var name : string? = nil
```

## Structure

包含property 和method¡

```swift
struct MyStructure{
  let name : String
  var p : [String]
  init(name:String,p:[String]){
    self.name = name
    self.p = p
}
  func hello(){
    print("hello")
  }
}
var s1 = MyStructure()
print(s1.name)


func exercise() {

    struct User{
        let name : String
        var email : String?
        var followers : Int
        var isActive : Bool
        func logStatus(){
            if self.isActive {
                print("\(self.name) is working hard")
            } else {
                print("\(self.name) has left the earth")
            }
        }
    }
    // Define the User struct here


    // Initialise a User struct here
    var riuser = User(name: "Richard", email: nil, followers: 0, isActive: false)
    riuser.logStatus()


    // Diagnostic code - do not change this code
    print("\nDiagnostic code (i.e., Challenge Hint):")
    var musk = User(name: "Elon", email: "elon@tesla.com", followers: 2001, isActive: true)
    musk.logStatus()
    print("Contacting \(musk.name) on \(musk.email!) ...")
    print("\(musk.name) has \(musk.followers) followers")
    // sometime later
    musk.isActive = false
    musk.logStatus()
    
}

```

## External parameter 

一个函数的参数可以有一个外部名字和一个内部名字，在设置了之后，使用函数就可以用外部名字传参，函数内再使用内部名字。或者直接不使用外部名字，使用函数时就不需要写参数名

```swift
//with external parameter
func test(answer parameter:String){
  print(parameter)
}

test(answer:"Hello")

//without external parameter
func test2(_ parameter:String,_ para2:Int){
    print(parameter)
    print(para2)
}

test2("Hello",123)
```

## Function

```swift
func isOdd(_ n:Int)-> Bool{
    if n%2 == 1{
        return true
    }else{
        return false
    }
}

```

## Mutable(可变性)

Swift中用var创建的变量都是mutable，用let创建的都是immutable。在修改immutable变量时需要打碎再重建

在struct内部修改struct变量值的时候需要给方法添加mutating属性

使用SwiftUI的时候可以给变量加@State属性来修复

## 保留小数位数

从Double转到String时可使用`` String("$.2f",num)``来保留两位小数

从Int转到String，不足两位前面补0：``String("%02d,num")`` 



## 类和继承

类的定义方式和结构体类似

继承：`` class A : B{}``

重载函数： ``override func a(){}``

使用父类的函数：``super.funca()``

 ![image-20211210111025022](https://gitee.com/Squirrel_01/img/raw/master/img/image-20211210111025022.png)

NSObject(NextObject)

## Struct和Class区别

使用A=B的时候Class是浅拷贝，struct是深拷贝

struct使用值传递，class使用reference传递

apple建议一开始使用struct，有需要时再变成class



## Optional进阶用法

1. 强制unwrap a = optional!

2. ```swift
   if optional != nil{
     print(safe!)
   }else{
     
   }
   ```

3. optional binding : 

   ```swift
   if let safe = optional{
     print(safe)
   }else{
     
   }
   ```

4. Default:
   `` optional ?? defaltvalue``

5. Optional chaining
   `` optional?.prop`` 

## 自动页面位置

横屏时自动修正位置：

可以通过添加位置约束和对齐的方式

> - 位置约束：距离最近的元素上下左右具体多少像素
> - 对齐：水平轴或者垂直轴居中
> - 也可以两者一起使用

添加位置约束：

选择需要修改的view，选中需要修改的元素，右下角添加约束

![image-20211204153117825](https://gitee.com/Squirrel_01/img/raw/master/img/image-20211204153117825.png)

把虚线点成实线后add。现在横屏后可能会局限在safe area中，就需要点constraint，具体修改四个方位的safe area改成superview即可

添加居中：

![image-20211204155250623](https://gitee.com/Squirrel_01/img/raw/master/img/image-20211204155250623.png)

两个一起使用可以制作出如图label效果，垂直轴居中并且离上边元素30px

居中时会让元素大小发生变化，可以使用constrain来设置大小

### 用view控制位置

对复杂元素定位时可以使用view，就是div的用处。选中需要在一起的元素点击这里可以放进一个view。

![image-20211204160340654](https://gitee.com/Squirrel_01/img/raw/master/img/image-20211204160340654.png)

Stackview可以把多个view堆叠。将多个view添加到一个stackview后可以调整边距，元素距离等。

> Bug:Stack view 的Alignment设置成vertical时会使按钮无法使用，需要设置成Fill

## 播放声音

在遇到新模块的时候去google，模板：dosth+language+stackoverflow

```swift
import AVFoundation
var player: AVAudioPlayer?
func playSound(name: String) {
        guard let url = Bundle.main.url(forResource: name, withExtension: "mp3") else { return }
        
        do {
            try AVAudioSession.sharedInstance().setCategory(.playback, mode: .default)
            try AVAudioSession.sharedInstance().setActive(true)
            
            player = try AVAudioPlayer(contentsOf: url, fileTypeHint: AVFileType.mp3.rawValue)
            
            guard let player = player else { return }
            
            player.play()
            
        } catch let error {
            print(error.localizedDescription)
        }
}

```

## 使用progressViewer

```swift
progressViewer.setProgress(0.0,animated: true)
```

## 定时器

```swift
var timer = Timer?
func startTimer(time:Int) {
        timer?.invalidate()
        timer = nil
        counter = time
        timer = Timer.scheduledTimer(timeInterval: 1.0, target: self, selector: #selector(updateCounter), userInfo: nil, repeats: true)
    }
@objc func updateCounter() {
        if counter > 0 {
            progressViewer.setProgress(Float(times[hard]!-counter)/Float(times[hard]!), animated: true)
            counter -= 1
        }else{
            playSound(name: "alarm_sound")
            progressViewer.setProgress(1.0, animated: true)
            DispatchQueue.main.asyncAfter(deadline: .now() + 3) {
                self.progressViewer.setProgress(0.0, animated: true)
            }
            if let timer = self.timer {
                timer.invalidate()
                self.timer = nil
            }
        }
    }
```

## 设计模式

设计模式就是针对某一种问题的一个经过验证的解决方案

有很多设计模式

### MVC

Model-view-controller

![image-20211206165603374](https://gitee.com/Squirrel_01/img/raw/master/img/image-20211206165603374.png)

### Delegate

常用delegate：

Decodable：用于表明这个struct可以转化成json

Identifiable：必须自己有一个叫做id的东西，可以使用computed propoty代替。用处可以简便的遍历这个类的元素

![image-20211228193140941](https://gitee.com/Squirrel_01/img/raw/master/img/image-20211228193140941.png)

## 使用代码新建view

```swift
class secondViewController: UIViewController {
    var bmi =  "0.0"
    override func viewDidLoad() {
        super.viewDidLoad()
        
        view.backgroundColor = .red
        let label = UILabel()
        label.text = bmi
        label.frame = CGRect(x: 0, y: 0, width: 100, height: 50)
        label.backgroundColor = .green
        view.addSubview(label)
    }
}

```

## 切换显示view

```swift
        let vc2 = secondViewController()
        vc2.bmi = String(format: "%.2f", bmi1)
        self.present(vc2, animated: true, completion: nil)
```

## 创建segue

![image-20211211172952388](https://gitee.com/Squirrel_01/img/raw/master/img/image-20211211172952388.png)

在controller上或者view上边的小点上按住control拖到下边的viewcontroller

还可以直接按住cintrol从Aview里的某一个按钮上拖到另一个view

segue可以定义页面切换的动画，不同segue的区别：https://help.apple.com/xcode/mac/8.0/#/dev564169bb1

若要用segue从Acontroller切换到Bcontroller：

> 需要在Acontroller中定义prepare函数来传输一些B必要的变量
>
> A中使用``self.performSegue``切换.第一个是在storyboard设置的名称，第二个是self或别的类
>
> B中使用 ``dismiss`` 来回去

![image-20220123215120967](https://gitee.com/Squirrel_01/img/raw/master/img/image-20220123215120967.png)

## protocol用法

protocol类似一种认证，其实就是虚类

内部类似虚类，只能定义函数名

用的时候需要定义函数

```swift
struct airplane: canfly{
  func fly(){
    print("fly")
  }
}
```



## 使用api获得天气数据

在openweather注册账号，使用current来获取数据，还可以自定义一些显示特征

## 使用swift进行url链接

1. 生成url
2. 创建URLSession
3. 给UrlSession一个任务
4. 运行任务

## 用函数作为参数，匿名函数

函数作参数传入：

```swift
func calculate(n1:Int,n2:Int,operation:(Int,Int)->Int)->Int{
  return operation(n1,n2)
}
func plus(n1:Int,n2:Int)->Int{
  return n1+n2
}
calculate(n1: 2, n2: 3, operation: plus(n1:n2:))

```

匿名函数：

```swift
	{
    (no1:Int,no2:Int)->Int in
    	return no1+no2
  }
//编译器可以预判你要输出一些东西
calculate(n1:2,n2:3,operation:{(no1,no2) in 
                              no1+no2})
//$0代表第一个变量
calculate(n1:2,n2:3,operation:{$0+$1})
calculate(n1:2,n2:3){$1+$2}
```

## Map函数

``array.map(func1)``

```swift
let newarray = array.map{"\($0)"}
array.map({(n1)in
    n1+1})
```



## Computed property

```swift
var prop:String{
  return "qwwe"
}
```

## DispatchQueue

在需要长时间进行的任务（如从网上寻找东西）的时候系统会让他在后台执行，因为如果让用户等的话就会看起来像是卡住了。但是如果在任务中需要更新前台的显示就需要修改更新的代码

把更新部分的代码用sync包裹起来

```swift
DispatchQueue.main.sync {
            temperatureLabel.text = weather.temperatureString
            conditionImageView.image = UIImage(systemName: weather.conditionName)
        }
```

## extension用法

用于扩展某个类，新增函数

1. 扩展内建类

   ```swift
   extension Double{
       func round(to:Int) -> Double {
           let q = pow(10, Double(to))
           var n = self
           n=n*q
           n.round()
           n = n/q
           return n
       }
       
   }
   var double = 3.14159
   double.round(to:3)
   ```

2. 扩展protocol

   如果某个protocol里的函数需要一个默认值可以使用extension来添加

3. 简化代码。

   如果一个类有很多继承关系，可以把每个继承写成一个扩展，扩展内部写和这个继承相关的函数

## 使用cocoapods

cocoapods类似前端的npm，是一个Swift的包管理器

1. ``sudo gem install cocoapods``安装
2. cd到项目目录，使用pod init生成podfile
3. 修改podfile，添加需要的模块
4. `` pod install``
5. 打开新生成的App.xcworkspace进行操作

删除操作：

1. 在podfile中删除模块
2. 使用pod install

相关链接：[cocoapods官网](https://cocoapods.org/)

## Constant文件

用来记录一些项目中的常量

在根文件夹新建Constants.swift，里边新增一个Constants struct。里边的成员使用static修饰

![](https://img.zhaoxuanlang.cn/image-20220130205457742.png)

let是instance变量，static let是type变量。type变量依赖于type，instance变量依赖于instance

建议struct叫做K，比较短

## UITableView

搜索tableview，同时新增一个table cell。这个cell必须要设置一个identifier

也可以直接搜索UItableviewcontroller，这样的话所有所需的关联都会自动添加。（推荐）

### 使用

在controller中首先需要有数据源的数组

然后添加两个函数，一个是有numberOfRowsInSection，返回数据源的成员个数，获得table的行数

另一个是有cellForRowAt，返回的是一个cell。这个函数内先定义一个cell，这里要用到之前的那个identifier，然后可以设置它的文本，最好返回这个cell。

![image-20220213113516497](https://img.zhaoxuanlang.cn/image-20220213113516497.png)

### 添加点击事件

需要用到delegate方法来呼叫delegate。

添加有didSelectRowAt的tableView方法，里边可以先写个print来获得点击的位置。点击后有灰色的效果，如果想取消灰色效果就需要加tableView.deselectRow方法。

可以通过添加accessoryType来添加尾部元素如checkmark。

```swift
override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
//        print(ItemArray[indexPath.row])
        
        if (tableView.cellForRow(at: indexPath)?.accessoryType == .checkmark){
            tableView.cellForRow(at: indexPath)?.accessoryType = .none
        }else{
            tableView.cellForRow(at: indexPath)?.accessoryType = .checkmark
        }
        tableView.deselectRow(at: indexPath, animated: true)
    }
```

### 重新加载

```swift
self.tableview.reloadData()
```







# as标签的使用

```swift
If i is int{
  
}//可以用来辨别i变量的属性
```

as!用于强制类型转换，可以转化成子类，但是有可能在运行时报错

as?用于有可能能转化

```swift
if let a as? b{
	a.bfunc()
}else{
  
}
```

as是把类转化成父类（不常用）

## Navigation bar

### 生成

点击第一个view，editor-embedin-navigation controller就可以添加进navigation stack

### 颜色设置

点左侧Navigation Bar，右侧的设置中Translucent可以让它颜色和下边相同

Tint是返回文字的颜色

### 自定义显示和隐藏

在要隐藏的view controller中添加

```swift
override func viewWillAppear(xxx){
  super.viewxxxx
  navigationController?.isNavigationBarHidden = true
}
override func viewWillDisappear(xxx){
  super.viewxxxx
  xxx = false
}
```

### 在bar中添加button

搜索barbutton添加，可以直接选择systemItem为一些预设样式

## View Controller 生命周期

![image-20220201211336874](https://img.zhaoxuanlang.cn/image-20220201211336874.png)

## SwiftUI使用

SwiftUI可以实时预览，还能直接向画面上添加组件

### 创建

在创建项目时选择使用SwiftUI

### 添加自定义字体

把文件放进项目后在info里新增一条Fonts provided by application,值填字体的全称，包括扩展名。

### 图片

更改大小需要加resizable，然后可以用aspectRatio来自适应。padding类似于前端的margin。

### Extract Subview实现组件复用

cmd+左键点某一个组件，选择Extract Subview就可以分离出来，然后可以进行改名。

分离出来之后在总view中新建变量，调用的时候传入变量后就可以复用。

还可以新建一个SwiftUI文件，把这个复制进去作为单独的文件用。

![](https://img.zhaoxuanlang.cn/image-20220207123719045.png)

## UIAlert

### 定义

需要定义一个alert和一个action。alert是对话框本地，action是添加到alert对象上的选项。

alert可以添加TextField文本输入框

## 本地存储

![](https://img.zhaoxuanlang.cn/%E6%88%AA%E5%B1%8F2022-02-16%20%E4%B8%8B%E5%8D%881.53.27.png)

### Userdefault

把所有数据以key-value的形式存在一个plist里



首先需要定义一个``var defaults = UserDefaults.standard``

存储：``self.defaults.set(xxxxx,forKey:"keyxxx")``

读取取决于存入的类型：

```swift
defaults.array(forKey:"keyxxx")
defaults.float()
defaults.object()
defaults.dictionary()
```

不建议存储大量数据，每次读取都会读所有的plist

### NSdecoder

自定义plist的存储位置，可以分开多个plist存放不同数据



首先需要定义plist：

``  **let** dataFilePath = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first?.appendingPathComponent("items.plist")``

读取与写入：

```swift
func saveitems() {
        let encoder = PropertyListEncoder()
        do{
            let data = try encoder.encode(ItemArray)
            try data.write(to: dataFilePath!)
        }catch{
            print("Error saving!")
        }
        tableView.reloadData()
    }
    
    func loadItem() {
        if let data = try? Data(contentsOf: dataFilePath!){
            let decoder = PropertyListDecoder()
            do{
                ItemArray = try decoder.decode([Item].self, from: data)
            }catch{
                print(error)
            }
        }
    }
```



## Singleton

全局只能有一个

在class里定义一个static类型变量




