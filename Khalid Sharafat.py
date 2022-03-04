import opc, time, math                                                                                                                                                                                                              #opc Library.
from time import sleep                                                                                                                                                                                                              #position for HI.
import colorsys                                                                                                                                                                                                                        #position for HI.
                                                                                                                                                                                                                     #position for HI.

client = opc.Client('localhost:7890')                                                                                                                                                                                           #position for HI.
leds = [(0,0,0)]*360                                                                                                                                                                                                                  #position for HI.
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
HI = [29,30,33,34,36,37,38,39,40,41,89,90,93,94,96,97,98,                                                                                                                                                          #Position for HI.
      99,100,101,149,150,151,152,153,154,158,159,209,210,
      211,212,213,214,218,219,269,270,273,274,276,277,278,
    279,280,281,329,330,333,334,336,337,338,339,340,341]
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
one_two_three = [0,1,2,62,122,182,242,300,301,302,303,304,                                                                                                                                                     #Position for 123.
                          6,7,8,68,128,186,187,188,246,306,307,308,
                     10,11,12,72,130,131,132,192,252,310,311,312]
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
ready = [16, 17, 18, 19, 20, 76, 80, 136, 137, 138, 139, 140,                                                                                                                                                         #Position for READ.
            196, 198, 256, 260, 22, 23, 24, 25, 26, 82, 142, 143,
            144, 145, 146, 202, 262, 263, 264, 265, 266, 28, 29,
            30, 31, 32, 88, 92, 148, 149, 150, 151, 152, 208, 212,
            268, 272, 34, 35, 36, 37, 94, 98, 154, 158, 214, 218,
            274, 275, 276, 277, 40, 44, 101, 103, 162, 222, 282]
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
steady = [12, 13, 14, 15, 16, 72, 132, 133, 134, 135, 136, 196,                                                                                                                                                  #Position for STEADY.
               252, 253, 254, 255, 256, 18, 19, 20, 21, 22, 80, 140,
               200, 260, 24, 25, 26, 27, 28, 84, 144, 145, 146, 147,
             148, 204, 264, 265, 266, 267, 268, 30, 31, 32, 33, 34,
              90, 94, 150, 151, 152, 153, 154, 210, 214, 270, 274,
              36, 37, 38, 39, 96, 100, 156, 160, 216, 220, 276, 277,
              278, 279, 42, 46, 103, 105, 164, 224, 284]
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
go = [26, 27, 28, 29, 30, 86, 146, 149, 150, 206, 210,                                                                                                                                                               #Position for GO.
       266, 267, 268, 269, 270, 32, 33, 34, 35, 36, 92,
       96, 152, 156, 212, 216, 272, 273, 274, 275, 276]
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
car = [63,64,65,124,125,126,184,185,186,242,244,62,                                                                                                                                                                #Position for HI.
         120,121,122,123,183,180,181,182,]
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
snake = [0,1,2]                                                                                                                                                                                                                        #Position for the snake.
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def say(colour, time, text):                                                                                                                                                                                                         # what the fuctontion does
    for i in text:
        leds [i] = colour                                                                                                                                                                                                                #tuns on the specifys the LEDs.
        client.put_pixels(leds)
        sleep(time)

while True:
    choice = input ("What animation would you like to see?\n1.HI\n2.Moving Numbers123\n3.READY,STEADY,GO\n4.Moving car\n5.Snake\n6.Random color\n7.Gun\n")         #string prints option on the screen. 

    if choice == '1':
        print ('whats your name')                                                                                                                                                                                                   #Prints whats your name. Asks for a Nmae.
        myname = input ()                                                                                                                                                                                                           # input your name.
        print ('HI,' + myname)                                                                                                                                                                                                       #prints Hi + the inpued name.
        for i in HI:
            leds [i] = (255,165,0)                                          #tuens off the specifyed LEDs.
            client.put_pixels(leds)
            sleep(0.03)
            
    elif choice == '2':
        n = 12
        while n < 60:
            leds = [(0,0,0)]*360                                    #Background color
            for x in one_two_three:
                leds[x] = (255,0,0)
                client.put_pixels(leds)
            for x in enumerate(one_two_three):
                one_two_three[x[0]] = x[1]+1
            time.sleep(0.3)
            n+=1
        leds = [(0,0,0)]*360
    elif choice == '3':
        n =0
        while n < 1:
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
    elif choice =='6':
            s = 1.0                                                                                                                                                                                                                                      ##maximum colour
            v = 1.0                                                                                                                                                                                                                                      ##maximum brightness

            for hue in range(360):
                rgb_fractional = colorsys.hsv_to_rgb(hue/360.0, s, v)                                                                                                                                                                #colorsys returns floats between 0 and 1
                print(rgb_fractional)
                r_float = rgb_fractional[0]                                                                                                                                                                                                       #extract said floating point numbers
                g_float = rgb_fractional[1]
                b_float = rgb_fractional[2]

                rgb = (r_float*255, g_float*255, b_float*255)                                                                                                                                                                             #make new tuple with corrected values
                print(rgb)
                leds[hue] = rgb
                client.put_pixels(leds)                                                                                                                                                                                                            #send out

                sleep(0.03)
    elif choice =='7':
        led = 0
        while led<60:
            for led in range (60):
                leds = [(0,20,255)]*360#

                leds[59-led] = (255,0,0)
                leds[54] = (255,0,0)
                leds[55] = (255,0,0)
                leds[56] = (255,0,0)
                leds[57] = (255,0,0)
                leds[58] = (255,0,0)
                leds[59] = (255,0,0)
                leds[116] = (255,0,0)
                leds[117] = (255,0,0)
                leds[118] = (255,0,0)
                leds[119] = (255,0,0)
                leds[178] = (255,0,0)
                leds[179] = (255,0,0)
                leds[238] = (255,0,0)
                leds[239] = (255,0,0)
                leds[298] = (255,0,0)
                leds[299] = (255,0,0)



                client.put_pixels(leds)
                time.sleep(0.1)
        break
                
    else:
            print("Option not recognised")
