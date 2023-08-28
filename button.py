from gpiozero import LED, Button
from signal import pause

led = LED(17)
button = Button(2)

button.when_pressed = led.on
button.when_released = led.off

from subprocess import call

def print_thing():
    print("reset")
    

 = print_thing
led_3.off()
   
pause()


