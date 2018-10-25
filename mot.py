import RPi.GPIO as GPIO 
import time
import os
GPIO.setmode(GPIO.BCM)

pirPin=6
GPIO.setup(pirPin,GPIO.IN)
counter=1
time.sleep(4)
a=1

while counter<=4:

    
    if GPIO.input(pirPin):
        print("Motion Detected")
      
        os.system("fswebcam -F 4 --fps 20 -r 800*600 /home/pi/vvv/"+str(a)+".jpg")
        print(" pic taken")
        time.sleep(1)
        counter = counter + 1
        a=a+1 
print("Testing")
exit()


