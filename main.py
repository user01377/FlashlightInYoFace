from ppadb.client import Client as AdbClient
from PIL import Image
from PIL import ImageStat
import pyautogui
import time

client = AdbClient(host="127.0.0.1", port=5037) # Default is "127.0.0.1" and 5037
devices = client.devices()
#checks if device is connected to PC properly
if len(devices) == 0:
    print('No devices')
    quit()

device = devices[0]
print(f'Connected to {device}')

#returns avg value of pixels in a png
def brightness( im_file ):
   im = Image.open(im_file).convert('L')
   stat = ImageStat.Stat(im)
   return(round(stat.mean[0],0))
   #255 brighest, 0 darkest

while True:
   pyautogui.screenshot("downloads/currentState.png")
   im_file = "downloads/currentState.png"
   time.sleep(0.25)
   if brightness(im_file) >= 130:
      device.shell("input touchscreen tap 667 1502")
   elif brightness(im_file) not range(45,71):
      device.shell("input touchscreen tap 667 1502")
   elif brightness(im_file) #notin range(45,71)
      device.shell("input touchscreen tap 667 1502")
   elif brightness(im_file) < 130:
      brightness(im_file) >= 130:
   print("program has ran")
