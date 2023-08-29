import requests
from gpiozero import LED, Button
from signal import pause

led = LED(17)
button = Button(2)
url = "https://maker.ifttt.com/trigger/button_pressed/json/with/key/emIUu4JtDzBTg5kilS4sKYLe8xWXjO-pKDCaPwWFgWB"
# button.when_pressed = led.on
# button.when_released = led.off

from subprocess import call

def print_thing():
    print("button pressed")
    
def send_request(url):
    print("Hello")
    r = requests.get(url)
    if r.status_code == "200":
        return led.on
while True:   
    if button.is_pressed:
       
        send_request(url)
    
#  
# button.when_pressed = send_request()
      
pause()


