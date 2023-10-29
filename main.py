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

flashlightIsOn = False

#constanly runs code, probably could ask if user wanted to stop code
while True:
   #screenshots user's screen, saves that file to a variable
   pyautogui.screenshot("downloads/currentState.png")
   im_file = "downloads/currentState.png"
   
   if brightness(im_file) >= 130 or brightness(im_file) in range(45,71) and flashlightIsOn == False:
      device.shell("input touchscreen tap 667 1502")
      flashlightIsOn = True
   elif flashlightIsOn == True and brightness(im_file) <= 129 and brightness(im_file) not in range(45,71):
      device.shell("input touchscreen tap 667 1502")
      flashlightIsOn = False
   

#while brightness >= 130, keep light on
#if it dips below 130, turn off light

#while brightness in range(45,71), turn on flashlight
#if it is NOT in this range, turn off flashlight
