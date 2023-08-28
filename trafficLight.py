
from time import sleep
from gpiozero import LED, Button
from signal import pause



red = LED(17)
yellow = LED(16)
green = LED(18)
button = Button(2)



def startProcess():
       #  while button.when_pressed == True and button.when_released == False:
    if (green.is_active == True):
        green.off()
        red.on()
        sleep(3)
        red.off()
        
        yellow.on()
        sleep(3)
        yellow.off()
        
        green.on()


    else:
         red.on()
         sleep(3)
         red.off()
         
         yellow.on()
         sleep(3)
         yellow.off()
         
         green.on()


button.when_pressed = startProcess
pause()      
        
        
        



# 
# while button.when_pressed == True:
#    led_1.on()
#    sleep(1)
#    led_2.off()
#    sleep(1)
#    led_3.off()
#    sleep(1)
#    
#    led_1.off()
#    sleep(1)
#    led_2.on()
#    sleep(1)
#    led_3.off()
#    sleep(1)
#    
#    led_1.off()
#    sleep(1)
#    led_2.off()
#    sleep(1)
#    led_3.on()
#    sleep(1)
   
   
   
    
   
    
    
    
