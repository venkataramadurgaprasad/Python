#!/usr/bin/env python3

import sys
import os
import re

old_name=sys.argv[1]
new_name=sys.argv[2]
location=sys.argv[3]
path=os.path.join(os.path.expanduser("~"),location)

os.chdir(path)
list_files=os.listdir(path)
actual_files={}

for i in list_files:
  if old_name in  i:
    x=re.sub(old_name,new_name,i)
    actual_files[i]=x

for old,new in actual_files.items():
  os.rename(old,new)
