#! /bin/bash
sed -n '/tags:/,/categories:/p' *.md > test
sed '/^id/d' ./test | sed '/^date/d'  > test2
sort -n ./test2 | awk '{if($0!=line)print; line=$0}' > test3
./test.py
rm ./test ./test2 ./test3