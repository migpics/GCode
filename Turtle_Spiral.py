import turtle

turtle.screensize(400,800)


turtle.shape("turtle")



myNewCoords=[]

##Draw Pancake Griddle
turtle.fill(True)
turtle.forward(460)
turtle.left(90)
turtle.forward(260)
turtle.left(90)
turtle.forward(460)
turtle.left(90)
turtle.forward(260)
turtle.fill(False)

##Move pen to Start Point
turtle.penup()
turtle.setposition(200,150)
turtle.pendown()


def drawPancake():
        turtle.pencolor("white")
        turtle.pensize(3)
        for i in range(1,20):
            turtle.left(245)

    
            for i in range(1,15):
                turtle.forward(i)
                turtle.left(2*i)
                myNewCoords.append('G00 X'+ str(round(turtle.xcor(),2))+' Y'+str(round(turtle.ycor(),2)))	    
	    

def writeGCode():

    newFile = raw_input('Enter the name of the GCodeFile')

    GCodefile = open(newFile+'.Gcode', 'w+')
    GCodefile.write('G21; sets units to millimeters \n')
    GCodefile.write('M107;  Turns extruder off \n')
    GCodefile.write('G28;  Home all axes \n')
    GCodefile.write('G1 F9600;  Sets the speed of Pancakebot \n')
    GCodefile.write('M107; \n')
    
    for i in myNewCoords:
        GCodefile.write(i+';')
        GCodefile.write('\n')

    GCodefile.write('M107;  Turns extruder off \n')
    GCodefile.write('G28 X0 Y0;  Home all axes \n')
    GCodefile.write('M84; Disable motors \n')


    GCodefile.close();


drawPancake()

myConfirmation = raw_input('Do you want to save the GCode File?  Enter Yes or No ')

if myConfirmation == 'Yes':
        writeGCode()
else:
            print "Thanks!  You are done!"
         
    
