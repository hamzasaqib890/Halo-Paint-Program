#Hamza Saqib Paint Project
from pygame import * #all graphics programs will need this
from tkinter import * #import all the other modules
from tkinter import filedialog
from math import *
from random import *
root = Tk()
root.withdraw()
init()
    #r   g b
RED = (255,0,0) #tuple - a list that can not be changed!
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)

size=(1250, 770) #screen resolution
screen=display.set_mode(size)#creating a 800x600 window

arialFont = font.SysFont("Impact", 16) #Using the Impact font at two differnt sizes
arialFontBig = font.SysFont("Impact", 23)

display.set_caption("Halo Paint Program") #caption for the program

#------------------------making all the rectangles for the tool icons------------------------------
pencilRect = Rect(33, 78, 55, 55)
eraserRect = Rect(105, 78, 55, 55)
markerRect = Rect(177, 78, 55, 55)
sprayRect = Rect(249, 78, 55, 55)
fillRect = Rect(321, 78, 55, 55)
lineRect = Rect(33, 150, 55, 55)
rectRect = Rect(105, 150, 55, 55)
circleRect = Rect(177, 150, 55, 55)
freeRect = Rect(249, 150, 55, 55)
saveRect = Rect(1200, 700, 50, 20)
palRect = Rect(286, 222, 55, 55)
col0Rect = Rect(347, 227, 23, 23)
col1Rect = Rect(347, 252, 23, 23)
infoBar = Rect(480, 13, 730, 34)
foregroundRect = Rect(1082, 562, 128, 72)
backgroundRect = Rect(1082, 665, 128, 72)
canvasClearRect = Rect(1010, 674, 55, 55)
canvasFillRect = Rect(938, 674, 55, 55)
backgroundReset = Rect(866, 674, 55, 55)
stampRect = Rect(424, 665, 128, 72)
fileRect = Rect(8, 13, 100, 34)
saveRect = Rect(8, 47, 100, 34)
loadRect = Rect(8, 81, 100, 34)
editRect = Rect(108, 13, 100, 34)
undoRect = Rect(108, 47, 100, 34)
redoRect = Rect(108, 81, 100, 34)
sizeRect = Rect(315, 294, 67, 250)
smallRect = Rect(321, 328, 55, 55)
mediumRect = Rect(321, 400, 55, 55)
largeRect = Rect(321, 472, 55, 55)
fillOptionsRect = Rect(315, 561, 67, 178)
unfilledRect = Rect(321, 595, 55, 55)
filledRect = Rect(321, 667, 55, 55)
#making the surface that will be used to draw shapes on. after it is made it is filled completely tranparent (explained later on)
canvasShapes = Surface((816, 459), SRCALPHA)
canvasShapes.fill((0, 0, 0, 0))
#this is the foreground layer for the canvas. it is completely tranparent
canvas = Surface((816, 459), SRCALPHA)
canvas.fill((0,0,0,0))
canvasRect=Rect(0, 0, 816, 459)
#the second canvas layer (background) is created
canvasBackground = Surface((816, 459))
draw.rect(canvasBackground, WHITE, canvasRect)

#load ALL images
backgroundImg = image.load("images/background.jpg")
backgroundImg = transform.scale(backgroundImg,(1350,760))
palette = image.load("images/colour_palette.png")
#loading images for icons for tools and also resizing them
pencilIcon = image.load("images/pencilpic.jpg")
pencilIcon = transform.scale(pencilIcon, (45, 45))
eraserIcon = image.load("images/eraserpic.jpg")
eraserIcon = transform.scale(eraserIcon, (45, 45))
markerIcon = image.load("images/markerpic.jpg")
markerIcon = transform.scale(markerIcon, (45, 45))
sprayIcon = image.load("images/spraypic.png")
sprayIcon = transform.scale(sprayIcon, (51, 51))
fillIcon = image.load("images/fillpic.jpg")
fillIcon = transform.scale(fillIcon, (45, 45))
lineIcon = image.load("images/linepic.jpg")
lineIcon = transform.scale(lineIcon, (45, 45))
rectIcon = image.load("images/rectpic.png")
rectIcon = transform.scale(rectIcon, (30, 30))
circleIcon = image.load("images/circlepic.png")
circleIcon = transform.scale(circleIcon, (40, 40))
freeIcon = image.load("images/freepic.png")
freeIcon = transform.scale(freeIcon, (45, 45))
palIcon = image.load("images/colpaletteicon.png")
palIcon = transform.scale(palIcon, (45, 45))
clearIcon = image.load("images/clearpic.png")
clearIcon = transform.scale(clearIcon, (45, 45))
arrowIcon = image.load("images/arrowIcon.png")
arrowIcon = transform.scale(arrowIcon, (50, 50))
rArrow = transform.rotate(arrowIcon, 270)
lArrow = transform.rotate(arrowIcon, 90)

#loading the backgrounds using a loop and storing them in a list. another list is created to store the icons for the backgrounds
backgroundNames = ["wallpaper0.jpg", "wallpaper1.jpg", "wallpaper2.jpg", "wallpaper3.jpg"]
backgrounds = []
backgroundsIcon = []
for background in backgroundNames:
    wp = image.load("images//" + background)
    wp = transform.scale(wp, (816, 459))
    backgrounds.append(wp)
    wp = transform.scale(wp, (128, 72))
    backgroundsIcon.append(wp)

stamps = []#stamps are all loaded in and stored in a list

stamp0 = image.load("images/stamp0.png")
stamps.append(stamp0)

stamp1 = image.load("images/stamp1.png")
stamps.append(stamp1)

stamp2 = image.load("images/stamp2.png")
stamps.append(stamp2)

stamp3 = image.load("images/stamp3.png")
stamps.append(stamp3)

stamp4 = image.load("images/stamp4.png")
stamps.append(stamp4)

stamp5 = image.load("images/stamp5.png")
stamps.append(stamp5)

stamp6 = image.load("images/stamp6.png")
stamps.append(stamp6)

stamp7 = image.load("images/stamp7.png")
stamps.append(stamp7)

stamp8 = image.load("images/stamp8.png")
stamps.append(stamp8)

stamp9 = image.load("images/stamp9.png")
stamps.append(stamp9)

stamp10 = image.load("images/stamp10.png")
stamps.append(stamp10)

stampsIcon = []
#all the icons for the stamps are then made by resizeing them and storing in a list
for stamp in stamps:
    stampx = stamp.get_width()
    stampy = stamp.get_height()
    stampsIcon.append(transform.scale(stamp, (int(stampx * 72 / stampy), 72)))

running = True #boolean variable
screen.blit(backgroundImg, (-100, 10)) #blitting canvases (background anf foreground)
screen.blit(canvasBackground, (409, 70))
screen.blit(canvas, (409, 70))
whiteCanvas = canvasBackground.copy()
backgrounds.append(whiteCanvas)
whiteCanvasIcon = transform.scale(whiteCanvas, (128, 72))
backgroundsIcon.append(whiteCanvasIcon) #default icon for background is created
draw.rect(screen, WHITE, foregroundRect)
tool = "none" #default tool
colours = [BLACK, WHITE] #default colours
fill = 2 #default for fill meaning shapes will be unfilled by default
col = 0 #default colour selection
selecting = "none"
runningTool = "none"
omx, omy = 300, 300
myClock = time.Clock()
shift = False #this variable checks if the user is presing the shift key
samePos = 0 #used for spray paint
size = "medium" #default size for tools
background = 4 #default background (white)
freePoints = [] #used for the free shape tool
undo = [whiteCanvas] #used for undo/redo
redo = []
currentSurface = canvas #declares which canvas surface the user is on (background or foreground)
draw.rect(screen, WHITE, (409, 70, 816, 459))
screen.blit(transform.scale(canvasBackground.copy(), (128, 72)), (1082,  665))
stampPage = 0 #default stamp pages and size
stampSize = 0
flip = 1 #used to indicate whether or not to flip stamp, default is obviously no

while running:
    leftClick = False #all four of these variables are declared false at the star of the main loop
    rightClick = False
    scrollUp = False
    scrollDown = False

    mx, my = mouse.get_pos()
    cmx, cmy = mx - 409, my - 70 #cmx, cmy is the mouse position on the canvas itself
    comx, comy = omx - 409, omy - 70 #this is the mouse position on the canvas last time the loop ran
    mb = mouse.get_pressed()

    if (mx, my) == (omx, omy): #used for spray tool to check how long the user has been at the same postiono for
        samePos += 1
    else:
        samePos = 0
        
    for evt in event.get():
        if evt.type == QUIT:
            running = False
        if evt.type == MOUSEBUTTONDOWN:
            if evt.button == 1:
                leftClick = True
                leftClickPos = mx, my
                if Rect(409, 70, 816, 459).collidepoint(mx, my):
                    sx, sy = evt.pos
                    csx, csy = sx - 409, sy - 70
            if evt.button == 3:
                rightClick = True
            elif evt.button == 4: scrollUp = True
            elif evt.button == 5: scrollDown = True
        if evt.type == MOUSEBUTTONUP:
            if evt.button == 1 and runningTool != "free" and Rect(409, 70, 816, 459).collidepoint(leftClickPos):
                if currentSurface == canvas:
                    undo.insert(0, canvas.copy())#used for undo/redo. everytime the user releases mouse it takes screen copy and adds it to the "undo" list
                    redo = []
                    draw.rect(screen, WHITE, foregroundRect)
                    screen.blit(transform.scale(canvas.copy(), (128, 72)), (1082,  562)) #this line and next two lines check which canvas surface user is drawing on and picture to show on the icon
                else:
                    screen.blit(transform.scale(canvasBackground.copy(), (128, 72)), (1082,  665))
        if evt.type == KEYDOWN:
            if evt.key == K_LSHIFT or evt.key == K_RSHIFT:
                shift = True #checking for left or right shift
        if evt.type == KEYUP:
            if evt.key == K_LSHIFT or evt.key == K_RSHIFT:
                shift = False

    draw.rect(screen, (150, 150, 145), (0, 0, 1250, 60)) #drawing all the stuff on the top of the screen. (file, edit, info bar etc.)
    draw.rect(screen, (240, 240, 235), infoBar)
    draw.rect(screen, (65, 50, 45), infoBar, 2)
    draw.rect(screen, (240, 240, 235), fileRect)
    draw.rect(screen, (65, 50, 45), fileRect, 2)
    draw.rect(screen, (240, 240, 235), editRect)
    draw.rect(screen, (65, 50, 45), editRect, 2)
    screen.blit(arialFont.render("File", True, BLACK), (20, 22))
    screen.blit(arialFont.render("Edit", True, BLACK), (120, 22))
    screen.blit(arialFont.render(tool, True, BLACK), (490, 20))

    #--------------------------------------------drawing the rectangles and image icons for the tools--------------------------------------------------
    if tool == "pencil":
        draw.rect(screen, RED, pencilRect, 2)
    else: draw.rect(screen, (100, 110, 80), pencilRect, 2)
    screen.blit(pencilIcon, (38, 83))
        
    if tool == "eraser":
        draw.rect(screen, RED, eraserRect, 2)
    else: draw.rect(screen, (100, 110, 80), eraserRect, 2)
    screen.blit(eraserIcon, (110, 83))

    if tool == "line":
        draw.rect(screen, RED, lineRect, 2)
    else: draw.rect(screen, (100, 110, 80), lineRect, 2)
    screen.blit(lineIcon, (38, 155))

    if tool == "rect":
        draw.rect(screen, RED, rectRect, 2)
    else: draw.rect(screen, (100, 110, 80), rectRect, 2)
    screen.blit(rectIcon, (117, 162))

    if tool == "circle":
        draw.rect(screen, RED, circleRect, 2)
    else: draw.rect(screen, (100, 110, 80), circleRect, 2)
    screen.blit(circleIcon, (185, 158))
    
    if tool == "spray":
        draw.rect(screen, RED, sprayRect, 2)
    else: draw.rect(screen, (100, 110, 80), sprayRect, 2)
    screen.blit(sprayIcon, (251, 80))
    
    if tool == "free":
        draw.rect(screen, RED, freeRect, 2)
    else: draw.rect(screen, (100, 110, 80), freeRect, 2)
    screen.blit(freeIcon, (255, 155))

    if tool == "fill":
        draw.rect(screen, RED, fillRect, 2)
    else: draw.rect(screen, (100, 110, 80), fillRect, 2)
    screen.blit(fillIcon, (326, 83))

    if tool == "marker":
        draw.rect(screen, RED, markerRect, 2)
    else: draw.rect(screen, (100, 110, 80), markerRect, 2)
    screen.blit(markerIcon, (182, 83))

    if selecting != "stamp":
        draw.rect(screen, (100, 110, 80), stampRect, 2)
        screen.blit(arialFontBig.render("Stamps", True, BLACK), (453, 685))
    
    if selecting != "background" and currentSurface != canvasBackground: draw.rect(screen, (100, 110, 80), backgroundRect, 2)

    if currentSurface == canvas:
        draw.rect(screen, RED, foregroundRect, 2)
    else:
        draw.rect(screen, (100, 110, 80), foregroundRect, 2)
        draw.rect(screen, RED, backgroundRect, 2)
    
    if selecting != "colour": draw.rect(screen, (100, 110, 80), palRect, 2)

    screen.blit(palIcon, (293, 225))

    draw.rect(screen, colours[0], col0Rect)
    draw.rect(screen, colours[1], col1Rect)
    
    if col == 0:
        draw.rect(screen, RED, col0Rect, 1)
    else: draw.rect(screen, (100, 110, 80), col0Rect, 1)

    if col == 1:
        draw.rect(screen, RED, col1Rect, 1)
    else: draw.rect(screen, (100, 110, 80), col1Rect, 1)
    
    if selecting != "colour":
        draw.rect(screen, (240, 240, 235), sizeRect)
        screen.blit(arialFont.render("Size", True, BLACK), (335, 300))
        screen.blit(arialFont.render("Small", True, BLACK), (332, 345))
        screen.blit(arialFont.render("Medium", True, BLACK), (323, 417))
        screen.blit(arialFont.render("Large", True, BLACK), (332, 490))

        if tool == "marker" or tool == "eraser" or tool == "spray":
            if size == "small":
                draw.rect(screen, RED, smallRect, 2)
            else: draw.rect(screen, (100, 110, 80), smallRect, 2)

            if size == "medium":
                draw.rect(screen, RED, mediumRect, 2)
            else: draw.rect(screen, (100, 110, 80), mediumRect, 2)

            if size == "large":
                draw.rect(screen, RED, largeRect, 2)
            else: draw.rect(screen, (100, 110, 80), largeRect, 2)

        else:
            draw.rect(screen, (150, 150, 150), smallRect, 2) 
            draw.rect(screen, (150, 150, 150), mediumRect, 2)
            draw.rect(screen, (150, 150, 150), largeRect, 2)

    draw.rect(screen, (240, 240, 235), fillOptionsRect)
    screen.blit(arialFont.render("Filled", True, BLACK), (331, 568))
    screen.blit(arialFont.render("No", True, BLACK), (340, 611))
    screen.blit(arialFont.render("Yes", True, BLACK), (337, 683))

    if tool == "rect" or tool == "circle" or tool == "free":
        if fill == 2:
            draw.rect(screen, RED, unfilledRect, 2)
        else: draw.rect(screen, (100, 110, 80), unfilledRect, 2)

        if fill == 0:
            draw.rect(screen, RED, filledRect, 2)
        else: draw.rect(screen, (100, 110, 80), filledRect, 2)

    else:
        draw.rect(screen, (150, 150, 150), unfilledRect, 2)
        draw.rect(screen, (150, 150, 150), filledRect, 2)

    #-----------------------------selecting the tool and tool options------------------------------------------------
    if selecting == "none":
        if pencilRect.collidepoint(mx, my):
            if leftClick and runningTool == "none":
                tool = "pencil"
            draw.rect(screen, RED, pencilRect, 2)

        if eraserRect.collidepoint(mx, my):
            if leftClick and runningTool == "none":
                tool = "eraser"
            elif rightClick and runningTool == "none":
                tool = "eraser"
                preEraser = screen.copy()
                draw.rect(screen, BLACK, eraserOptionsRect)
                selectingEraser = True
            draw.rect(screen, RED, eraserRect, 2)

        if lineRect.collidepoint(mx, my):
            if leftClick and runningTool == "none":
                tool = "line"
            draw.rect(screen, RED, lineRect, 2)

        if rectRect.collidepoint(mx, my):
            if leftClick and runningTool == "none":
                tool = "rect"
            draw.rect(screen, RED, rectRect, 2)

        if circleRect.collidepoint(mx, my):
            if leftClick and runningTool == "none":
                tool = "circle"
            draw.rect(screen, RED, circleRect, 2)

        if sprayRect.collidepoint(mx, my):
            if leftClick and runningTool == "none":
                tool = "spray"
            draw.rect(screen, RED, sprayRect, 2)

        if freeRect.collidepoint(mx, my):
            if leftClick and runningTool == "none":
                tool = "free"
            draw.rect(screen, RED, freeRect, 2)

        if fillRect.collidepoint(mx, my):
            if leftClick and runningTool == "none":
                tool = "fill"
            draw.rect(screen, RED, fillRect, 2)

        if markerRect.collidepoint(mx, my):
            if leftClick and runningTool == "none":
                tool = "marker"
            draw.rect(screen, RED, markerRect, 2)

        if tool == "marker" or tool == "eraser" or tool == "spray":
            if selecting != "colour":
                if smallRect.collidepoint(mx, my):
                    if leftClick and runningTool == "none":
                        size = "small"
                    draw.rect(screen, RED, smallRect, 2)
                if mediumRect.collidepoint(mx, my):
                    if leftClick and runningTool == "none":
                        size = "medium"
                    draw.rect(screen, RED, mediumRect, 2)
                if largeRect.collidepoint(mx, my):
                    if leftClick and runningTool == "none":
                        size = "large"
                    draw.rect(screen, RED, largeRect, 2)
                    
        if tool == "rect" or tool == "circle" or tool == "free":
            if unfilledRect.collidepoint(mx, my):
                if leftClick and runningTool == "none":
                    fill = 2
                draw.rect(screen, RED, unfilledRect, 2)
            if filledRect.collidepoint(mx, my):
                if leftClick and runningTool == "none":
                    fill = 0
                draw.rect(screen, RED, filledRect, 2)

    #----------------------------------------------selecting stamps------------------------------------------
    if stampRect.collidepoint(mx, my) and selecting != "stamp":
        if selecting != "file" and selecting != "edit":
            preStamp = screen.copy()
            selecting = "stamp"
            for i in range(0, 648, 12): #animation for the rectangle to slide out and show the stamps
                draw.rect(screen, (65, 50, 45), (424, 665, i, 72))
                draw.rect(screen, RED, stampRect, 2)
                screen.blit(arialFontBig.render("Stamps", True, BLACK), (453, 685))
                time.Clock().tick(600)
                display.flip()
            screen.blit(lArrow, (555, 676))#blits the arrow icons for the stamp pages and also blits the stamp icons
            screen.blit(stampsIcon[0], (610, 665))
            screen.blit(stampsIcon[1], (652, 665))
            screen.blit(stampsIcon[2], (720, 665))
            screen.blit(stampsIcon[3], (820, 665))
            screen.blit(stampsIcon[4], (880, 665))
            screen.blit(rArrow, (1010, 676))
            
    if selecting == "stamp" and Rect(424, 665, 648, 72).collidepoint(mx ,my) and leftClick:
        if Rect(1010, 676, 50, 50).collidepoint(mx, my) and stampPage != 2: #checking if user is switching pages for the stamp
            stampPage += 1
        elif Rect(555, 676, 50, 50).collidepoint(mx, my) and stampPage != 0:
            stampPage -= 1
        if Rect(1010, 676, 50, 50).collidepoint(mx, my) or Rect(555, 676, 50, 50).collidepoint(mx, my):#blits stamp images depending on which page the user is on
            if stampPage == 0:
                draw.rect(screen, (65, 50, 45), (424, 665, 636, 72))
                screen.blit(arialFontBig.render("Stamps", True, BLACK), (453, 685))
                draw.rect(screen, RED, stampRect, 2)
                screen.blit(lArrow, (555, 676))
                screen.blit(stampsIcon[0], (610, 665))
                screen.blit(stampsIcon[1], (652, 665))
                screen.blit(stampsIcon[2], (720, 665))
                screen.blit(stampsIcon[3], (820, 665))
                screen.blit(stampsIcon[4], (880, 665))
                screen.blit(rArrow, (1010, 676))
            if stampPage == 1:
                draw.rect(screen, (65, 50, 45), (424, 665, 636, 72))
                screen.blit(arialFontBig.render("Stamps", True, BLACK), (453, 685))
                draw.rect(screen, RED, stampRect, 2)
                screen.blit(lArrow, (555, 676))
                screen.blit(stampsIcon[5], (620, 665))
                screen.blit(stampsIcon[6], (740, 665))
                screen.blit(stampsIcon[7], (855, 665))
                screen.blit(rArrow, (1010, 676))
            if stampPage == 2:
                draw.rect(screen, (65, 50, 45), (424, 665, 636, 72))
                screen.blit(arialFontBig.render("Stamps", True, BLACK), (453, 685))
                draw.rect(screen, RED, stampRect, 2)
                screen.blit(lArrow, (555, 676))
                screen.blit(stampsIcon[8], (605, 665))
                screen.blit(stampsIcon[9], (745, 665))
                screen.blit(stampsIcon[10], (875, 665))
                screen.blit(rArrow, (1010, 676))
        else:
            if currentSurface == canvas:
                preSurface = "canvas"
                preTool = canvas.copy()
            else:
                preSurface = "canvasBackground"
                preTool = canvasBackground.copy()

            if stampPage == 0:
                if Rect(610, 665, 30, 72).collidepoint(mx, my):#checking if the user is selecting and going to use any of the stamps
                    runningTool = "stamp"
                    stamp = transform.scale(stamp0, (107, 250))
                    stampNum = 0
                elif Rect(652, 665, 63, 72).collidepoint(mx, my):
                    runningTool = "stamp"
                    stamp = transform.scale(stamp1, (214, 245))
                    stampNum = 1
                elif Rect(720, 665, 96, 72).collidepoint(mx, my):
                    runningTool = "stamp"
                    stamp = transform.scale(stamp2, (200, 150))
                    stampNum = 2
                elif Rect(820, 665, 58, 72).collidepoint(mx, my):
                    runningTool = "stamp"
                    stamp = transform.scale(stamp3, (322, 400))
                    stampNum = 3
                elif Rect(880, 665, 127, 72).collidepoint(mx, my):
                    runningTool = "stamp"
                    stamp = transform.scale(stamp4, (441, 250))
                    stampNum = 4
            elif stampPage == 1:
                if Rect(620, 665, 110, 72).collidepoint(mx, my):
                    runningTool = "stamp"
                    stamp = transform.scale(stamp5, (458, 300))
                    stampNum = 5
                elif Rect(740, 665, 127, 72).collidepoint(mx, my):
                    runningTool = "stamp"
                    stamp = transform.scale(stamp6, (617, 350))
                    stampNum = 6
                elif Rect(855, 665, 141, 72).collidepoint(mx, my):
                    runningTool = "stamp"
                    stamp = transform.scale(stamp7, (685, 350))
                    stampNum = 7
            elif stampPage == 2:
                if Rect(605, 665, 137, 72).collidepoint(mx, my):
                    runningTool = "stamp"
                    stamp = transform.scale(stamp8, (523, 275))
                    stampNum = 8
                elif Rect(745, 665, 127, 72).collidepoint(mx, my):
                    runningTool = "stamp"
                    stamp = transform.scale(stamp9, (617, 350))
                    stampNum = 9
                elif Rect(875, 665, 127, 72).collidepoint(mx, my):
                    runningTool = "stamp"
                    stamp = transform.scale(stamp10, (530, 300))
                    stampNum = 10
                
            
    if not Rect(424, 665, 648, 72).collidepoint(mx, my) and selecting == "stamp": #checks if user is still selecting stamp even if the mouse isnt hovering over the stamp icon
        selecting = "none"
        stampPage = 0 #sets stamp page back to the default (0)
        for i in range(648, 0, -12): #closing animation, similiar to the opening one
            screen.blit(preStamp, (0, 0))
            draw.rect(screen, (65, 50, 45), (424, 665, i, 72))
            draw.rect(screen, RED, stampRect, 2)
            screen.blit(arialFontBig.render("Stamps", True, BLACK), (453, 685))
            time.Clock().tick(600)
            display.flip()
        screen.blit(preStamp, (0, 0))

    #---------------------------------------------------------selecting background--------------------------------------------------------------
    if backgroundRect.collidepoint(mx, my) and leftClick: #user can choose which surface to draw on background canvas or the fore ground
        currentSurface = canvasBackground
    elif foregroundRect.collidepoint(mx, my):
        draw.rect(screen, RED, foregroundRect, 2)
        if leftClick:
            currentSurface = canvas#changes currentCanvas depending on which one the user clicks on
    if backgroundRect.collidepoint(mx, my) and selecting != "background":
        if selecting != "file" and selecting != "edit":
            preBackground = screen.copy()
            preBackCanvas = transform.scale(canvasBackground.copy(), (128, 72))
            selecting = "background"
            for i in range(0, 657, 12): #opening animation for the background selection pane
                draw.rect(screen, (65, 50, 45), (1210-i, 665, i, 72))
                screen.blit(preBackCanvas,(1082, 665))
                draw.rect(screen, RED, backgroundRect, 2)
                time.Clock().tick(600)
                display.flip()
            screen.blit(backgroundsIcon[0], (557, 665)) #blits the four background icons
            screen.blit(backgroundsIcon[1], (688, 665))
            screen.blit(backgroundsIcon[2], (819, 665))
            screen.blit(backgroundsIcon[3], (950, 665))
            wpselect = screen.copy()
        
    if selecting == "background":
        if background == 0:
            draw.rect(screen, RED, (557, 665, 128, 72), 2) #gives user feedback by displaying which background they have selected by highlighting in red
        elif background == 1:
            draw.rect(screen, RED, (688, 665, 128, 72), 2)
        elif background == 2:
            draw.rect(screen, RED, (819, 665, 128, 72), 2)
        elif background == 3:
            draw.rect(screen, RED, (950, 665, 128, 72), 2)
        draw.rect(screen, RED, backgroundRect, 2)

    if selecting == "background" and leftClick: #allows user to select one of the four backgrounds and blits on the canvas
        if Rect(557, 665, 128, 72).collidepoint(mx, my):
            background = 0 #changes the background variable to a number between 0 and 3
            screen.blit(wpselect, (0, 0))
            canvasBackground.blit(backgrounds[0], (0, 0)) #blits the background on the background canvas
            screen.blit(backgroundsIcon[0],(1082, 665)) #blits the icon
        elif Rect(688, 665, 128, 72).collidepoint(mx, my):
            background = 1
            screen.blit(wpselect, (0, 0))
            canvasBackground.blit(backgrounds[1], (0, 0))
            screen.blit(backgroundsIcon[1],(1082, 665))
        elif Rect(819, 665, 128, 72).collidepoint(mx, my):
            background = 2
            screen.blit(wpselect, (0, 0))
            canvasBackground.blit(backgrounds[2], (0, 0))
            screen.blit(backgroundsIcon[2],(1082, 665))
        elif Rect(950, 665, 128, 72).collidepoint(mx, my):
            background = 3
            screen.blit(wpselect, (0, 0))
            canvasBackground.blit(backgrounds[3], (0, 0))
            screen.blit(backgroundsIcon[3],(1082, 665))
                   
    if not Rect(554, 665, 657, 72).collidepoint(mx, my) and selecting == "background":
        selecting = "none"
        preBackCanvas = transform.scale(canvasBackground.copy(), (128, 72))
        for i in range(657, 0, -12): #closing animation
            screen.blit(preBackground, (0, 0))
            screen.blit(canvasBackground, (409, 70))
            draw.rect(screen, (65, 50, 45), (1210-i, 665, i, 72))
            screen.blit(preBackCanvas,(1082, 665))
            draw.rect(screen, RED, backgroundRect, 2)
            screen.blit(canvas, (409, 70))
            time.Clock().tick(600)
            display.flip()
        screen.blit(preBackground, (0, 0))
        screen.blit(preBackCanvas,(1082, 665))
        screen.blit(canvas, (409, 70))

    if selecting != "background" and selecting != "stamp":
        draw.rect(screen, WHITE, canvasClearRect)
        draw.rect(screen, colours[col], canvasFillRect)
        screen.blit(clearIcon, (1015, 680)) #garbage can icons
        screen.blit(clearIcon, (943, 680))
        if canvasClearRect.collidepoint(mx, my): #allows the user to clear the background canvas and make it completely white
            if leftClick and runningTool == "none":
                background = 4
                draw.rect(canvasBackground, WHITE, (0, 0, 816, 459))
                backgroundsIcon[4] = whiteCanvasIcon
                screen.blit(backgroundsIcon[4], (1082,  665))
            draw.rect(screen, RED, canvasClearRect, 2)
        else: draw.rect(screen, (100, 110, 80), canvasClearRect, 2)

        if canvasFillRect.collidepoint(mx, my): #allows the user to clear the background canvas and make it the colours that the user has selected
            if leftClick and runningTool == "none":
                background = 4
                draw.rect(canvasBackground, colours[col], (0, 0, 816, 459))
                colourCanvas = canvasBackground.copy()
                backgroundsIcon[4] = transform.scale(colourCanvas, (128, 72))
                screen.blit(backgroundsIcon[4], (1082,  665))
            draw.rect(screen, RED, canvasFillRect, 2)
        else: draw.rect(screen, (100, 110, 80), canvasFillRect, 2)
        
    #----------------------------------------------------------using the tool-------------------------------------------------------------
    if Rect(409, 70, 816, 459).collidepoint(mx, my):
        canvas.set_clip(canvasRect) #sets the clip to the canvas so user cant draw outside

        if runningTool == "stamp": #first tool is the stamp
            if mb[0] == 1: #allows user to scroll up and down to change the size of the stamp
                if scrollUp:
                    stampx = stamp.get_width()
                    stampy = stamp.get_height()
                    stamp = transform.scale(stamps[stampNum], (int(stampx * 1.1), int(stamps[stampNum].get_height() * int(stampx * 1.1) / stamps[stampNum].get_width()))) #important to keep the same aspect ratio of the stamp
                    if flip == -1: #checks if the user wants the stamp flipped or not
                        stamp = transform.flip(stamp, True, False)
                elif scrollDown:
                    stampx = stamp.get_width()
                    stampy = stamp.get_height()
                    if stampx > 30 or stampy > 30:
                        stamp = transform.scale(stamps[stampNum], (int(stampx / 1.1), int(stamps[stampNum].get_height() * int(stampx / 1.1) / stamps[stampNum].get_width())))
                    if flip == -1:
                        stamp = transform.flip(stamp, True, False)
                if rightClick:
                    flip *= -1 #multiplies the flip variable by -1 because u can keep multiplying by -1 to alternate between -1 and 1
                    stamp = transform.flip(stamp, True, False)
                if preSurface == "canvas": #checking which surface the user is drawing on
                    canvas = preTool.copy()
                    currentSurface = canvas
                else:
                    canvasBackground = preTool.copy()
                    currentSurface = canvasBackground
                stampx = stamp.get_width()#finds the stamps width and height
                stampy = stamp.get_height()
                currentSurface.blit(stamp, (cmx - stampx / 2, cmy - stampy / 2)) #blits the stamp at the middle of the cursor
            else:
                runningTool = "none"
                if currentSurface == canvas:
                    undo.insert(0, canvas.copy()) #if the user does use a stamp, it adds a screen copy to the undo list
                    redo = []
                    screen.blit(transform.scale(canvas.copy(), (127, 72)), (1082, 562))
                else:
                    screen.blit(transform.scale(canvasBackground.copy(), (127, 72)), (1082, 665))
                flip = 1 #sets the flip back to default (which is 1)
            
        elif tool == "pencil" and mb[0] == 1 and abs(mx - omx) < 250 and abs(my - omy) < 250: #very simple pencil tool
            draw.line(currentSurface, colours[col], (comx, comy), (cmx, cmy))

        elif tool == "eraser" and mb[0] == 1: #eraser tool
            dx = cmx - comx
            dy = cmy - comy
            dist = int(hypot(dx, dy))#all of this is to fill the empty gaps between the eraser

            for i in range(1, dist+1):
                eraserX = int(comx + i * dx / dist)  #horizontal move(run)
                eraserY = int(comy + i * dy / dist)  #vertical move (rise)

                if currentSurface == canvas:
                    if size == "small": #three sizes(small medium lare)
                        draw.rect(currentSurface, (0, 0, 0, 0), (eraserX - 10, eraserY - 10, 20, 20))#if user is erasing on foreground, thenit draws transparent squares
                    elif size == "medium":
                        draw.rect(currentSurface, (0, 0, 0, 0), (eraserX - 20, eraserY - 20, 40, 40))
                    elif size == "large":
                        draw.rect(currentSurface, (0, 0, 0, 0), (eraserX - 40, eraserY - 40, 80, 80))
                else:
                    if size == "small":
                        draw.rect(currentSurface, WHITE, (eraserX - 10, eraserY - 10, 20, 20))#if user is drawing on background then it draws white squares
                    elif size == "medium":
                        draw.rect(currentSurface, WHITE, (eraserX - 20, eraserY - 20, 40, 40))
                    elif size == "large":
                        draw.rect(currentSurface, WHITE, (eraserX - 40, eraserY - 40, 80, 80))

        elif tool == "line": #simple line tool
            if leftClick:
                if currentSurface == canvas:
                    preSurface = "canvas"
                    preTool = canvas.copy()
                else:
                    preSurface = "canvasBackground"
                    preTool = canvasBackground.copy()
                runningTool = "line"
            elif runningTool == "line":
                if preSurface == "canvas":
                    canvas = preTool.copy()
                    currentSurface = canvas
                else:
                    canvasBackground = preTool.copy()
                    currentSurface = canvasBackground
                draw.line(currentSurface, colours[col], (csx, csy), (cmx, cmy), 2) #draws a line on the currentSurface from the orignal clicking location to cmx, cmy
                if mb[0] == 0: runningTool = "none"

        elif tool == "rect": #rectangle tool
            if leftClick:
                if currentSurface == canvas:
                    preSurface = "canvas"
                    preTool = canvas.copy()
                else:
                    preSurface = "canvasBackground"
                    preTool = canvasBackground.copy()
                rectWidth = 2 #default width
                rectx = 0
                recty = 0
                runningTool = "rect"

            elif runningTool == "rect":
                if rectx / 2 < rectWidth or recty / 2 < rectWidth: #checks if the width is bigger than the rectangle and if it is then it sets it back to the right size
                    if rectx > recty:
                        rectWidth = recty/2 + 1
                    else:
                        rectWidth = rectx/2 + 1
                            
                if scrollUp:
                    if rectx / 2 > rectWidth + 5 and recty / 2 > rectWidth + 5: #allows user to change the width of the rectangle by scrolling
                        rectWidth += 5
                    else:
                        if rectx > recty:
                            rectWidth = rectx/2
                        else:
                            rectWidth = recty/2
                elif scrollDown:
                    if rectWidth - 5 > 1:
                        rectWidth -= 5
                    else:
                        rectWidth = 2

                if preSurface == "canvas":
                    canvas = preTool.copy()
                    currentSurface = canvas
                else:
                    canvasBackground = preTool.copy()
                    currentSurface = canvasBackground

                rectx = abs(mx - sx)
                recty = abs(my - sy)

                if fill == 0: #either rectangle is filled, so width is 0
                    if not shift: #if user isnt holding shift then it draws a normal rectangle
                        if mx > sx and my > sy:
                            draw.rect(currentSurface, colours[col], (csx, csy, rectx, recty), fill)
                        elif mx < sx and my < sy:
                            draw.rect(currentSurface, colours[col], (cmx, cmy, rectx, recty), fill)
                        elif mx > sx and my < sy:
                            draw.rect(currentSurface, colours[col], (csx, cmy, rectx, recty), fill)
                        elif mx < sx and my > sy:
                            draw.rect(currentSurface, colours[col], (cmx, csy, rectx, recty), fill)

                    if shift: #if user holding shift then it draws a square by getting the shorter length for the x and y and using that as the side length
                        if rectx <= recty:
                            rectxy = rectx
                        else: rectxy = recty

                        if mx > sx and my > sy:
                            draw.rect(currentSurface, colours[col], (csx, csy, rectxy, rectxy), fill)
                        elif mx < sx and my < sy:
                            draw.rect(currentSurface, colours[col], (csx - rectxy, csy - rectxy, rectxy, rectxy), fill)
                        elif mx > sx and my < sy:
                            draw.rect(currentSurface, colours[col], (csx, csy - rectxy, rectxy, rectxy), fill)
                        elif mx < sx and my > sy:
                            draw.rect(currentSurface, colours[col], (csx - rectxy, csy, rectxy, rectxy), fill)
                else:
                    canvasShapes.fill((0, 0, 0, 0)) #if user wants an unfilled rectangle then i use a more complicated technique to allow the user to chage the thckness without making it look strange
                    if not shift:
                            if mx > sx and my > sy:
                                draw.rect(canvasShapes, colours[col], (csx, csy, rectx, recty), 0) #draws a filled rectangle on a seperate surface
                                draw.rect(canvasShapes, (0, 0, 0, 0), (csx + rectWidth, csy + rectWidth, rectx - 2 * rectWidth, recty - 2 * rectWidth), 0) #draws a transparent rectangle inside of it to make it looked unfilled
                            elif mx < sx and my < sy:
                                draw.rect(canvasShapes, colours[col], (cmx, cmy, rectx, recty), 0)
                                draw.rect(canvasShapes, (0, 0, 0, 0), (cmx + rectWidth, cmy + rectWidth, rectx - 2 * rectWidth, recty - 2 * rectWidth), 0)
                            elif mx > sx and my < sy:
                                draw.rect(canvasShapes, colours[col], (csx, cmy, rectx, recty), 0)
                                draw.rect(canvasShapes, (0, 0, 0, 0), (csx + rectWidth, cmy + rectWidth, rectx - 2 * rectWidth, recty - 2 * rectWidth), 0)
                            elif mx < sx and my > sy:
                                draw.rect(canvasShapes, colours[col], (cmx, csy, rectx, recty), 0)
                                draw.rect(canvasShapes, (0, 0, 0, 0), (cmx + rectWidth, csy + rectWidth, rectx - 2 * rectWidth, recty - 2 * rectWidth), 0)

                    if shift:
                        if rectx <= recty:
                            rectxy = rectx
                        else: rectxy = recty
                        
                        if mx > sx and my > sy:
                            draw.rect(canvasShapes, colours[col], (csx, csy, rectxy, rectxy), 0)
                            draw.rect(canvasShapes, (0, 0, 0, 0), (csx + rectWidth, csy + rectWidth, rectxy - 2 * rectWidth, rectxy - 2 * rectWidth), 0)
                        elif mx < sx and my < sy:
                            draw.rect(canvasShapes, colours[col], (csx - rectxy, csy - rectxy, rectxy, rectxy), 0)
                            draw.rect(canvasShapes, (0, 0, 0, 0), (csx - rectxy + rectWidth, csy - rectxy + rectWidth, rectxy - 2 * rectWidth, rectxy - 2 * rectWidth), 0)
                        elif mx > sx and my < sy:
                            draw.rect(canvasShapes, colours[col], (csx, csy - rectxy, rectxy, rectxy), 0)
                            draw.rect(canvasShapes, (0, 0, 0, 0), (csx + rectWidth, csy - rectxy + rectWidth, rectxy - 2 * rectWidth, rectxy - 2 * rectWidth), 0)
                        elif mx < sx and my > sy:
                            draw.rect(canvasShapes, colours[col], (csx - rectxy, csy, rectxy, rectxy), 0)
                            draw.rect(canvasShapes, (0, 0, 0, 0), (csx - rectxy + rectWidth, csy + rectWidth, rectxy - 2 * rectWidth, rectxy - 2 * rectWidth), 0)
                
                if mb[0] == 0:
                    if preSurface == "canvas":
                        canvas.blit(canvasShapes, (0, 0))#blits the canvasShapes surface on the respective surface (background or foreground)
                        screen.blit(transform.scale(canvas.copy(), (127, 72)), (1082, 562))
                        undo[0] = canvas.copy() #adds to the undo list
                    else:
                        canvasBackground.blit(canvasShapes, (0, 0))
                        screen.blit(transform.scale(canvasBackground.copy(), (127, 72)), (1082, 665))
                    canvasShapes.fill((0, 0, 0, 0))
                    runningTool = "none"

        elif tool == "circle": #ellipse tool is exact same as recatngle so i will not explain it
            if runningTool == "circle":
                if scrollUp:
                    if circlex / 2 > circleWidth + 5 and circley / 2 > circleWidth + 5:
                        circleWidth += 5
                    else:
                        if circlex > circley:
                            circleWidth = circlex/2
                        else:
                            circleWidth = circley/2
                elif scrollDown:
                    if circleWidth - 5 > 1:
                        circleWidth -= 5
                    else:
                        circleWidth = 2

            if leftClick and runningTool == "none":
                if currentSurface == canvas:
                    preSurface = "canvas"
                    preTool = canvas.copy()
                else:
                    preSurface = "canvasBackground"
                    preTool = canvasBackground.copy()
                    
                runningTool = "circle"
                circleWidth = 2

            elif runningTool == "circle":                    
                circlex = abs(mx - sx)
                circley = abs(my - sy)

                if fill == 0:
                    if preSurface == "canvas":
                        canvas = preTool.copy()
                        currentSurface = canvas
                    else:
                        canvasBackground = preTool.copy()
                        currentSurface = canvasBackground

                    try:
                        if not shift:
                            if mx > sx and my > sy:
                                draw.ellipse(currentSurface, colours[col], (csx, csy, circlex, circley), fill)
                            elif mx < sx and my < sy:
                                draw.ellipse(currentSurface, colours[col], (cmx, cmy, circlex, circley), fill)
                            elif mx > sx and my < sy:
                                draw.ellipse(currentSurface, colours[col], (csx, cmy, circlex, circley), fill)
                            elif mx < sx and my > sy:
                                draw.ellipse(currentSurface, colours[col], (cmx, csy, circlex, circley), fill)  

                        if shift:
                            if circlex <= circley:
                                circlexy = circlex
                            else: circlexy = circley
                            
                            if mx > sx and my > sy:
                                draw.ellipse(currentSurface, colours[col], (csx, csy, circlexy, circlexy), fill)
                            elif mx < sx and my < sy:
                                draw.ellipse(currentSurface, colours[col], (csx - circlexy, csy - circlexy, circlexy, circlexy), fill)
                            elif mx > sx and my < sy:
                                draw.ellipse(currentSurface, colours[col], (csx, csy - circlexy, circlexy, circlexy), fill)
                            elif mx < sx and my > sy:
                                draw.ellipse(currentSurface, colours[col], (csx - circlexy, csy, circlexy, circlexy), fill)
                    except:
                        pass

                else:
                    canvasShapes.fill((0, 0, 0, 0))
                    try:
                        if not shift:
                            if mx > sx and my > sy:
                                draw.ellipse(canvasShapes, colours[col], (csx, csy, circlex, circley), 0)
                                draw.ellipse(canvasShapes, (0, 0, 0, 0), (csx + circleWidth, csy + circleWidth, circlex - 2 * circleWidth, circley - 2 * circleWidth), 0)
                            elif mx < sx and my < sy:
                                draw.ellipse(canvasShapes, colours[col], (cmx, cmy, circlex, circley), 0)
                                draw.ellipse(canvasShapes, (0, 0, 0, 0), (cmx + circleWidth, cmy + circleWidth, circlex - 2 * circleWidth, circley - 2 * circleWidth), 0)
                            elif mx > sx and my < sy:
                                draw.ellipse(canvasShapes, colours[col], (csx, cmy, circlex, circley), 0)
                                draw.ellipse(canvasShapes, (0, 0, 0, 0), (csx + circleWidth, cmy + circleWidth, circlex - 2 * circleWidth, circley - 2 * circleWidth), 0)
                            elif mx < sx and my > sy:
                                draw.ellipse(canvasShapes, colours[col], (cmx, csy, circlex, circley), 0)
                                draw.ellipse(canvasShapes, (0, 0, 0, 0), (cmx + circleWidth, csy + circleWidth, circlex - 2 * circleWidth, circley - 2 * circleWidth), 0)

                        if shift:
                            if circlex <= circley:
                                circlexy = circlex
                            else: circlexy = circley
                            
                            if mx > sx and my > sy:
                                draw.ellipse(canvasShapes, colours[col], (csx, csy, circlexy, circlexy), 0)
                                draw.ellipse(canvasShapes, (0, 0, 0, 0), (csx + circleWidth, csy + circleWidth, circlexy - 2 * circleWidth, circlexy - 2 * circleWidth), 0)
                            elif mx < sx and my < sy:
                                draw.ellipse(canvasShapes, colours[col], (csx - circlexy, csy - circlexy, circlexy, circlexy), 0)
                                draw.ellipse(canvasShapes, (0, 0, 0, 0), (csx - circlexy + circleWidth, csy - circlexy + circleWidth, circlexy - 2 * circleWidth, circlexy - 2 * circleWidth), 0)
                            elif mx > sx and my < sy:
                                draw.ellipse(canvasShapes, colours[col], (csx, csy - circlexy, circlexy, circlexy), 0)
                                draw.ellipse(canvasShapes, (0, 0, 0, 0), (csx + circleWidth, csy - circlexy + circleWidth, circlexy - 2 * circleWidth, circlexy - 2 * circleWidth), 0)
                            elif mx < sx and my > sy:
                                draw.ellipse(canvasShapes, colours[col], (csx - circlexy, csy, circlexy, circlexy), 0)
                                draw.ellipse(canvasShapes, (0, 0, 0, 0), (csx - circlexy + circleWidth, csy + circleWidth, circlexy - 2 * circleWidth, circlexy - 2 * circleWidth), 0)
                    except:
                        pass
                    
                if mb[0] == 0:
                    if preSurface == "canvas":
                        canvas.blit(canvasShapes, (0, 0))
                        screen.blit(transform.scale(canvas.copy(), (127, 72)), (1082, 562))
                        undo[0] = canvas.copy()
                    else:
                        canvasBackground.blit(canvasShapes, (0, 0))
                        screen.blit(transform.scale(canvasBackground.copy(), (127, 72)), (1082, 665))
                    canvasShapes.fill((0, 0, 0, 0))
                    runningTool = "none"

        elif tool == "spray" and mb[0] == 1: #spray tool uses the random module
            if samePos < 30: 
                if size == "small":
                    for i in range(4): #picks random points within a circle and sets them as a specific colour
                        sprayx = randint(-5, 5)
                        sprayy = randint(-5, 5)
                        if hypot(sprayx, sprayy) <= 5:
                            currentSurface.set_at((cmx + sprayx, cmy + sprayy), colours[col])
                elif size == "medium": #different sizes for the tool
                    for i in range(15):
                        sprayx = randint(-10, 10)
                        sprayy = randint(-10, 10)
                        if hypot(sprayx, sprayy) <= 10:
                            currentSurface.set_at((cmx + sprayx, cmy + sprayy), colours[col])
                elif size == "large":
                    for i in range(35):
                        sprayx = randint(-20, 20)
                        sprayy = randint(-20, 20)
                        if hypot(sprayx, sprayy) <= 20:
                            currentSurface.set_at((cmx + sprayx, cmy + sprayy), colours[col])
                            
            else: #if user has been in the same position for long time then it makes the spray less dense
                if size == "small":
                    sprayx = randint(-5, 5)
                    sprayy = randint(-5, 5)
                    if hypot(sprayx, sprayy) <= 5:
                        currentSurface.set_at((cmx + sprayx, cmy + sprayy), colours[col])
                elif size == "medium":
                    sprayx = randint(-10, 10)
                    sprayy = randint(-10, 10)
                    if hypot(sprayx, sprayy) <= 10:
                        currentSurface.set_at((cmx + sprayx, cmy + sprayy), colours[col])
                elif size == "large":
                    for i in range(10):
                        sprayx = randint(-20, 20)
                        sprayy = randint(-20, 20)
                        if hypot(sprayx, sprayy) <= 20:
                            currentSurface.set_at((cmx + sprayx, cmy + sprayy), colours[col])

        elif tool == "free": #free form tool, allowa user to click on random points and joins them after user right clicks (option for filled or unfilled)
            if runningTool == "none" and leftClick:
                if currentSurface == canvas:
                    preSurface = "canvas"
                    preTool = canvas.copy()
                else:
                    preSurface = "canvasBackground"
                    preTool = canvasBackground.copy()
                    
                runningTool = "free"
                freePoints += [(cmx, cmy)]

            if runningTool == "free" and leftClick:
                freePoints += [(cmx, cmy)] #when user left click it appends point to a list
                if len(freePoints) != 2:
                    draw.line(currentSurface, colours[col], freePoints[-1], freePoints[-2], 2)
                freeTool = currentSurface.copy()

            if runningTool == "free" and len(freePoints) != 1:
                if preSurface == "canvas":
                    canvas = freeTool.copy()
                    currentSurface = canvas
                else:
                    canvasBackground = freeTool.copy()
                    currentSurface = canvasBackground
                    
                draw.line(currentSurface, colours[col], freePoints[-1], (cmx, cmy), 2)

            if runningTool == "free" and rightClick and freePoints != []:
                freePoints += [(cmx, cmy)] #when user finally right clicks it adds the final point to the list
                runningTool = "none"
                if preSurface == "canvas":
                    canvas = preTool.copy()
                    currentSurface = canvas
                else:
                    canvasBackground = preTool.copy()
                    currentSurface = canvasBackground
                draw.polygon(currentSurface, colours[col], freePoints, fill) #draws the shape
                if currentSurface == canvas:
                        screen.blit(transform.scale(canvas.copy(), (127, 72)), (1082, 562))
                        undo.insert(0, canvas.copy()) #adds to the undo list
                        redo = []
                else:
                    screen.blit(transform.scale(canvasBackground.copy(), (127, 72)), (1082, 665))
                freePoints = []

        elif tool == "fill" and leftClick: #flood fill bucket tool
            canvasPixelArray = PixelArray(currentSurface) #created pixel array of the canvas the user wants to fill
            colStart = currentSurface.get_at((cmx, cmy)) #gets the colour at the point where the user clicked
            fillQueue = [(cmx, cmy)] #adds point to fillQueue list
            
            if colStart != colours[col]: #runs loop as long as starting colour is deiffernt as desired colour
                while fillQueue != []: #runs loop until fillQueue list is empty
                    for i in fillQueue:
                        xFill = i[0]
                        yFill = i[1]
                        if canvasRect.collidepoint(xFill - 1, yFill) and canvasPixelArray[xFill - 1, yFill] == currentSurface.map_rgb((colStart)): #checks the four pixels around the each pixel and fills them if neccesary
                            canvasPixelArray[xFill - 1, yFill] = colours[col]
                            fillQueue.append((xFill - 1, yFill))
                        if canvasRect.collidepoint(xFill + 1, yFill) and canvasPixelArray[xFill + 1, yFill] == currentSurface.map_rgb((colStart)):
                            canvasPixelArray[xFill + 1, yFill] = colours[col]
                            fillQueue.append((xFill + 1, yFill))
                        if canvasRect.collidepoint(xFill, yFill - 1) and canvasPixelArray[xFill, yFill - 1] == currentSurface.map_rgb((colStart)):
                            canvasPixelArray[xFill, yFill - 1] = colours[col]
                            fillQueue.append((xFill, yFill - 1))
                        if canvasRect.collidepoint(xFill, yFill + 1) and canvasPixelArray[xFill, yFill + 1] == currentSurface.map_rgb((colStart)):
                            canvasPixelArray[xFill, yFill + 1] = colours[col]
                            fillQueue.append((xFill, yFill + 1))
                        
                        fillQueue = fillQueue[1:] #deletes the point from the list
            del canvasPixelArray #deletes the pixel array to unlock the surface after it has finished
 
        elif tool == "marker" and mb[0] == 1: #marker tool exact same as eraser so no explanation needed
            dx = cmx - comx
            dy = cmy - comy
            dist = int(hypot(dx**2, dy**2))

            for i in range(1, dist + 1):
                dotX = int(comx + i * dx / dist)
                dotY = int(comy + i * dy / dist)
                if size == "small":
                    draw.circle(currentSurface, colours[col], (dotX, dotY), 5)
                elif size == "medium":
                    draw.circle(currentSurface, colours[col], (dotX, dotY), 10)
                elif size == "large":
                    draw.circle(currentSurface, colours[col], (dotX, dotY), 20)

        canvas.set_clip(None) #sets the clip back to none

    #---------------------------------------------------------selecting colour-------------------------------------------------------------------
    if palRect.collidepoint(mx, my) and selecting != "colour" and runningTool == "none":
        prePal = screen.copy()
        selecting = "colour"
        for i in range(0, 265, 12): #opening animation for the palette
            draw.rect(screen, (65, 50, 45), (341 - i, 222, i, i))
            time.Clock().tick(600)
            display.flip()
        screen.blit(palette, (91, 222)) #blits the image for the palette

    if selecting == "colour" and Rect(81, 222, 265, 265).collidepoint(mx ,my) and leftClick:
        colours[col] = screen.get_at((mx, my)) #if the user clicks then it gets the colour at that position
        
    if not Rect(81, 222, 265, 265).collidepoint(mx, my) and selecting == "colour":
        selecting = "none"
        for i in range(265, 0, -12): #closing animation for the palette
            screen.blit(prePal, (0, 0))
            draw.rect(screen, (65, 50, 45), (341 - i, 222, i, i))
            time.Clock().tick(600)
            display.flip()
        screen.blit(prePal, (0, 0))

    if col0Rect.collidepoint(mx, my) and leftClick: #allows user to change from primary to secondary colours
        col = 0

    elif col1Rect.collidepoint(mx, my) and leftClick:
        col = 1

    #-------------------------------------------------------------edit (undo/redo)---------------------------------------------------------------
    if editRect.collidepoint(mx, my) and leftClick and selecting == "none": #checks if user clicks the edit button
        selecting = "edit"
        preEditSelect = screen.copy()

    elif selecting == "edit":
        draw.rect(screen, (255, 255, 255), undoRect) #draws the undo and redo buttons and writes them out
        draw.rect(screen, (0, 0, 0), undoRect, 1)
        screen.blit(arialFont.render("Undo", True, BLACK), (120, 55))
        draw.rect(screen, (255, 255, 255), redoRect)
        draw.rect(screen, (0, 0, 0), redoRect, 1)
        screen.blit(arialFont.render("Redo", True, BLACK), (120, 90))
        
        if undoRect.collidepoint(mx, my) and leftClick: #checks if user clicks undo
                try:
                    canvas = undo[1].copy() #instead of blitting the picture I set the canvas as a deep copy. this is neccesary since the surface is transparent and in blitting then u can see through
                    currentSurface = canvas #program acts wierd if this isnt done since the above line changes the currentSurface
                    redo.insert(0, undo[0]) #moves the image from the undo list to the redo and next line deletes from the undo list
                    del undo[0]
                    screen.blit(whiteCanvas, (1082,  562)) #blit
                    screen.blit(transform.scale(canvas, (128, 72)), (1082,  562))
                except:
                    pass
        elif redoRect.collidepoint(mx, my) and leftClick:
            try:
                canvas = redo[0].copy() #redo is very similiar to undo so no need for explanatation
                currentSurface = canvas
                undo.insert(0, redo[0])
                del redo[0]
                screen.blit(whiteCanvas, (1082,  562))
                screen.blit(transform.scale(canvas, (128, 72)), (1082,  562))
            except:
                pass
        if leftClick:
            selecting = "none" # closes the edit menu
            screen.blit(preEditSelect, (0, 0))

    #------------------------------------------------------------file (save/load)----------------------------------------------------------------------
    elif fileRect.collidepoint(mx, my) and leftClick and selecting == "none": #opens the file menu
        selecting = "file"
        preFileSelect = screen.copy()

    elif selecting == "file":
        draw.rect(screen, (255, 255, 255), saveRect) #blits the savea and open buttons
        draw.rect(screen, (0, 0, 0), saveRect, 1)
        screen.blit(arialFont.render("Save", True, BLACK), (20, 55))
        draw.rect(screen, (255, 255, 255), loadRect)
        draw.rect(screen, (0, 0, 0), loadRect, 1)
        screen.blit(arialFont.render("Load", True, BLACK), (20, 90))
        
        if saveRect.collidepoint(mx, my) and leftClick:
            try:
                fname = filedialog.asksaveasfilename(defaultextension = ".png") # asks user where they want to save it
                image.save(canvas, fname) #saves it at the location user specifies
            except:
                pass #the try, except: pass is necessary incase user doesnt select anything to prevent program fom crashing

        elif loadRect.collidepoint(mx, my) and leftClick:
            try:
                fname=filedialog.askopenfilename(filetypes=[("Images","*.png;*.jpg;*.jpeg;*.bmp")]) #user specifies path for image
                loadImg = image.load(fname) #image is opened and blit onto the canvas
                canvas.blit(loadImg, (0, 0))
            except:
                pass #this is neccesary again for the same reason as above

        if leftClick:
            selecting = "none" #closes the file menu
            screen.blit(preFileSelect, (0, 0))

    screen.blit(canvasBackground, (409, 70)) #blits the background first onto the screen
    if currentSurface == canvasBackground:
        screen.blit(canvasShapes, (409, 70)) #checks if the shapes are drawn onto background and if es then blits this first, otherwise it gets blit after the foreground canvas
    screen.blit(canvas, (409, 70)) #foreground canvas is blit
    if currentSurface == canvas:
        screen.blit(canvasShapes, (409, 70))
    
    omx, omy = mx, my #used for some tools (ex: pencil tool)
    display.flip()
    #everything we "draw" is actually copied
                #to a place in RAM
            #display.flip copies that to the actual screen
            
quit() #closing the pygame window
