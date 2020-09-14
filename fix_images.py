#!/usr/bin/env python3
from PIL import Image
import os, sys
size = (128, 128)
new_path = '/opt/icons/'
for image in os.listdir():
  img = os.path.splitext(image)[0]
  try:
    with Image.open(image).convert('RGB') as im:
      im.thumbnail(size)
      im.rotate(270)
      im.save(new_path+img,"jpeg")
  except OSError:
    pass
