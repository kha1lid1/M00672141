import opc, time, math
from time import sleep
import colorsys

client = opc.Client('localhost:7890')
leds = [(0,0,0)]*360

HI = [29,30,33,34,36,37,38,39,40,41,89,90,93,94,96,97,98,
      99,100,101,149,150,151,152,153,154,158,159,209,210,
      211,212,213,214,218,219,269,270,273,274,276,277,278,
    279,280,281,329,330,333,334,336,337,338,339,340,341]

one_two_three = [0,1,2,62,122,182,242,300,301,302,303,304,
                          6,7,8,68,128,186,187,188,246,306,307,308,
                     10,11,12,72,130,131,132,192,252,310,311,312]

ready = [16, 17, 18, 19, 20, 76, 80, 136, 137, 138, 139, 140,
            196, 198, 256, 260, 22, 23, 24, 25, 26, 82, 142, 143,
            144, 145, 146, 202, 262, 263, 264, 265, 266, 28, 29,
            30, 31, 32, 88, 92, 148, 149, 150, 151, 152, 208, 212,
            268, 272, 34, 35, 36, 37, 94, 98, 154, 158, 214, 218,
            274, 275, 276, 277, 40, 44, 101, 103, 162, 222, 282]

steady = [12, 13, 14, 15, 16, 72, 132, 133, 134, 135, 136, 196,
               252, 253, 254, 255, 256, 18, 19, 20, 21, 22, 80, 140,
               200, 260, 24, 25, 26, 27, 28, 84, 144, 145, 146, 147,
             148, 204, 264, 265, 266, 267, 268, 30, 31, 32, 33, 34,
              90, 94, 150, 151, 152, 153, 154, 210, 214, 270, 274,
              36, 37, 38, 39, 96, 100, 156, 160, 216, 220, 276, 277,
              278, 279, 42, 46, 103, 105, 164, 224, 284]

go = [26, 27, 28, 29, 30, 86, 146, 149, 150, 206, 210,
       266, 267, 268, 269, 270, 32, 33, 34, 35, 36, 92,
       96, 152, 156, 212, 216, 272, 273, 274, 275, 276]

car = [120,121,122,180,181,182]

snake = [0,1,2]

def say(colour, time, text): what the fuctontion does
    for i in text:
        leds [i] = colour                                            #tuns on the specifys the LEDs.
        client.put_pixels(leds)
        sleep(time)


while True:
    choice = input ("What animation would you like to see?\n1.HI\n2.Moving Numbers123\n3.READY,STEADY,GO\n4.Moving car\n5.Snake\n")

    if choice == '1':
        print ('whats your name')              #Prints whats your name. Asks for a Nmae.
        myname = input ()                     # input your name.
        print ('HI,' + myname)                  #prints Hi + the inpued name.
        say((0,128,0),0.03,HI)
        say((255,255,255), 0.0003, HI)
        say((255,165,0), 0.0003, HI)    # call say fun

        numLEDs = 360
        t = 0
        n = 0

        while n < 100:
            t += 1
            brightness = int(min(1, 1.25 + math.sin(t)) * 255)
            frame = [ (brightness, brightness, brightness) ] * numLEDs
            client.put_pixels(frame)
            time.sleep(0.05)
            n += 1
            
    elif choice == '2':
        n = 12
        while n < 60:
            leds = [(0,0,0)]*360
            for x in one_two_three:
                leds[x] = (255,255,255)
                client.put_pixels(leds)
            for x in enumerate(one_two_three):
                one_two_three[x[0]] = x[1]+1
            time.sleep(0.3)
            n+=1
        leds = [(0,0,0)]*360
    elif choice == '3':
        n =0
        while n < 3:
            for x in range(3):
                say((255,0,0),0,ready)
                time.sleep(0.5)
                leds = [(0,0,0)]*360
                client.put_pixels(leds)
                time.sleep(0.2)
            for x in range(3):
                say((0,255,0),0,steady)
                time.sleep(0.5)
                leds = [(0,0,0)]*360
                client.put_pixels(leds)
                time.sleep(0.2)
            for x in range(3):
                say((0,0,255),0,go)
                time.sleep(0.5)
                leds = [(0,0,0)]*360
                client.put_pixels(leds)
                time.sleep(0.2)
            n += 1
    elif choice == '4':
        n = 3
        while n < 60:
            leds = [(0,0,0)]*360
            for x in car:
                leds[x] = (255,255,255)
                client.put_pixels(leds)
            for x in enumerate(car):
                car[x[0]] = x[1]+1
            input('press enter to continue')
            n+=1
    elif choice == '5':
        n = 2
        while n < 360:
            leds = [(0,0,0)]*360
            for x in snake:
                leds[x] = (255,255,255)
                client.put_pixels(leds)
            for x in enumerate(snake):
                snake[x[0]] = x[1]+1
            time.sleep(0.1)
            n+=1
    else:
            print("Option not recognised")
