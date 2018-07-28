# OrangePi GPIO

A _VERY_ early developmet module for handling gpio on the OrangePi using Python.

Example:
```python
# Import stuff
import gpio
from time import sleep

# Choose the pin to blink
pin = 7

# Initialize
gpio.init(pin,gpio.OUTPUT)
status = True

# Loop forever
while True:
    if status:
        gpio.set(pin,gpio.HIGH)
    else:
        gpio.set(pin,gpio.LOW)
    status = !status
    sleep(1)

```
