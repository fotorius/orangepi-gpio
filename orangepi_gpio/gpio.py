import subprocess

# Pin modes
OUTPUT = 'out'
INPUT = 'in'

# Pin status
HIGH = '1'
LOW = '0'

def init(pin,mode):
    """
    Initialize pin.
    """
    f = open('/sys/class/gpio/export','w')
    f.write(str(pin))
    try:
        f.close()
    except IOError:
        pass
    
    f = open('/sys/class/gpio/gpio%d/direction'%int(pin),'w')
    f.write(mode)
    try:
        f.close()
    except IOError:
        pass
    

def set(pin,status):
    """
    Set pin status.
    """
    f = open('/sys/class/gpio/gpio%d/value'%int(pin),'w')
    f.write(status)
    f.close()
    
