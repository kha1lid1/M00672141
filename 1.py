import opc
from time import sleep
import colorsys

client = opc.Client('localhost:7890')
leds = [(25,0,0)]*360

print ('whats your name')
myname = input ()
print ('HI,' + myname)


HI = [29,30,33,34,36,37,38,39,40,41,89,90,93,94,96,97,98,
      99,100,101,149,150,151,152,153,154,158,159,209,210,
      211,212,213,214,218,219,269,270,273,274,276,277,278,
      279,280,281,329,330,333,334,336,337,338,339,340,341]
for i in HI:
    leds [i] = (255,0,0)
    client.put_pixels(leds)
    sleep(0.003)
    
