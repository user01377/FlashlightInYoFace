from PIL import Image
from PIL import ImageStat
import pyautogui
import time

#returns avg value of pixels in a png
def brightness( im_file ):
   im = Image.open(im_file).convert('L')
   stat = ImageStat.Stat(im)
   return(round(stat.mean[0],0))
   #255 brighest, 0 darkest

while True:
   pyautogui.screenshot("downloads/test.png")
   im_file = "downloads/test.png"
   time.sleep(0.25)
   if brightness(im_file) >= 130:
      #turn on flash
   elif brightness(im_file) in range(45,71):
      #turn on flash
   print("program has ran")
