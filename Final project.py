#CSC2280 final project
#Where should you study today? FSC Edition!!

#To do:
#fix end screen - descriptions need to show, pictures need to show - line 232
#add: Can change answer once clicked
#possible add: new fonts


#Set up graphics window
from graphics import *
win = GraphWin("Where should you study? FSC Edition!", 600, 400)


#initialize different study areas
rinker = 0
tutus = 0
library = 0
yourdorm = 0


#Initialize buttons
abutton = Rectangle(Point(75, 115), Point(90, 130))
bbutton = Rectangle(Point(75, 135), Point(90, 150))
cbutton = Rectangle(Point(75, 155), Point(90, 170))
dbutton = Rectangle(Point(75, 175), Point(90, 190))

abutton.setFill("light gray")
bbutton.setFill("light gray")
cbutton.setFill("light gray")
dbutton.setFill("light gray")


#make list of questions
questions = ["What noise can you handle while studying?",
             "What materials will you need?",
             "Are you studying with anyone else?",
             "Will you be hungry?",
             "How much time do you need to be studying?",
             "Are you easily distracted?",
             "How do you like to sit when you study?",
             "Where will you be before studying?",
             "Do you like to study all at once or a little at a time?",
             "What time of day will you be studying?",
             "When you study, are you tempted to fall asleep?",
             "What kind of clothes will you be in while studying?"]

#make question numbers
numofq = ["Question 1", "Question 2", "Question 3", "Question 4",
          "Question 5", "Question 6", "Question 7", "Question 8",
          "Question 9", "Question 10", "Question 11", "Question 12"]

#make list of options
#library
A = ["A. None.",
     "A. I need my laptop, notebooks, and dry erase markers",
     "A. Nope! Just me, but I could call over a study group",
     "A. I mean not starving, but I like to snack while studying",
     "A. I have a test tomorrow, so I'll keep going until I get it",
     "A. Y.E.S.!! I can't focus if anything is happening around me",
     "A. I need to sit upright at a desk",
     "A. I'll be in class",
     "A. All at once, no question",
     "A. In between classes",
     "A. Nah, I'm pretty awake",
     "A. Whatever I wore to class"]
#rinker
B = ["B. I like having some background noise, but not a lot",
     "B. I just need computer access",
     "B. Yeah, but just a small group project",
     "B. I will DEFINITELY need to eat",
     "B. Probably an hour or two",
     "B. Not really, but I do goof off if I have the chance",
     "B. I like being in a wheely chair",
     "B. I'll be at the caf",
     "B. I like to spread it over time",
     "B. Probably after dinner",
     "B. Only if I'm in a comfy place",
     "B. Sweats/leggings and a t-shirt"]
#tutus
C = ["C. I need background noise",
     "C. Probably just my laptop and a charger.",
     "C. Yes! We're studying a lot of diagrams and",
     "C. Yeah I'll want to have something small",
     "C. Not too long",
     "C. Nope, when I'm in the zone nothing can touch me",
     "C. I like to sit at a table with a lot of space",
     "C. I will be waiting for a class that starts later",
     "C. I need to pull an allnighter usually",
     "C. Late at night",
     "C. I do! I usually need some sort of caffeine",
     "C. Something cute, just in case I run into people"]
#yourdorm
D = ["D. Only is its my own music",
     "D. Literally every piece of school supplies I own",
     "D. Nope, its just me.",
     "D. Yeah, but the campus doesn't have a lot of options I like",
     "D. Its just a quick assignment",
     "D. Not really, but people being around me can distract me",
     "D. I like to sprawl out and sometimes even lay down",
     "D. I'll be in my residence hall",
     "D. Overtime, the assignment isn't due for awhile",
     "D. Gurl I have NO idea.  ¯\\_(ツ)_/¯",
     "D. Nope! I can control my sleep really well",
     "D. Pajamas for sureeeeee"]


#create title screen
title = Text(Point(300, 20), "Welcome to the FSC study place quiz!")
title.setSize(25)
title.setStyle("bold")
title.setTextColor("red")
title.draw(win)

instructions = Text(Point(300, 150), "This quiz is meant to assist you in finding your perfect study area \non the Florida Southern College campus.\n\nFor each question, answer by choosing an 'A', 'B', 'C' or 'D' when prompted. \n\nReady? Click the button to get started!")
instructions.draw(win)

startbutton = Rectangle(Point(250, 250), Point(350, 300))
startbutton.draw(win)

startlabel = Text(Point(300,275), "Start!")
startlabel.draw(win)

mocslogo = Image(Point(500,310),"C:\\Users\\Admin\\Documents\\CSC 2280\\Final project\\logo.png")
mocslogo.draw(win)


#start questions
#initialize objects for while loop
qnum = Text(Point(300, 60), numofq)
qnum.setStyle("bold")
qnum.setSize(20)
question = Text(Point(300,90), questions)
question.setStyle("bold italic")
opta = Text(Point(300,120), A)
optb = Text(Point(300,140), B)
optc = Text(Point(300,160), C)
optd = Text(Point(300,180), D)
opta.setSize(11)
optb.setSize(11)
optc.setSize(11)
optd.setSize(11)
i = 0

while True:

    #change from start screen to actual quiz
    pt = win.getMouse()
    if pt:
        x = pt.getX()
        y = pt.getY()

        #Begin quiz
        if x >= 250 and x <=350 and y >= 250 and y <= 350:
            instructions.setText("Click the box next to the option that most applies to you, \nthen click next!")
            instructions.move(0,200)
            instructions.setStyle("bold")
            startlabel.setText("Next")
            title.setText("Where will you study today?")
            mocslogo.undraw()
            
            #go through questions
            if i == 0:
                
                question.setText(questions[i])
                question.draw(win)
                
                opta.setText(A[i])
                opta.draw(win)
                optb.setText(B[i])
                optb.draw(win)
                optc.setText(C[i])
                optc.draw(win)
                optd.setText(D[i])
                optd.draw(win)

                abutton.draw(win)
                bbutton.draw(win)
                cbutton.draw(win)
                dbutton.draw(win)
                
                
                qnum.setText(numofq[i])
                qnum.draw(win)

                hasstarted = True

                #start recording results
                pt2 = win.getMouse()
                while True:
                    x = pt2.getX()
                    y = pt2.getY()

                    #check which button was clicked
                    #a button clicked
                    if hasstarted and x >= 75 and x <= 90 and y >= 115 and y <= 130:
                        library += 1
                        abutton.setFill("green")
                        break

                        
                    #b button clicked
                    elif hasstarted and x >= 75 and x <= 90 and y >= 135 and y <= 150:
                        rinker += 1
                        bbutton.setFill("green")
                        break


                    #c button clicked
                    elif hasstarted and x >= 75 and x <= 90 and y >= 155 and y <= 170:
                        tutus += 1
                        cbutton.setFill("green")
                        break


                    #d button clicked
                    elif hasstarted and x >= 75 and x <= 90 and y >= 175 and y <= 190:
                        yourdorm += 1
                        dbutton.setFill("green")
                        break
                        
                    #if misclick 
                    else:
                        instructions.setText("Sorry, you didn't click in the right place, \nplease try again!")
                        pt2 = win.getMouse()
                        x = pt2.getX()
                        y = pt2.getY()
            #No more questions!!!
            elif i >= len(numofq):
                
                question.undraw()
                
                opta.undraw()
                optb.undraw()
                optc.undraw()
                optd.undraw()

                abutton.undraw()
                bbutton.undraw()
                cbutton.undraw()
                dbutton.undraw()
            
                qnum.undraw()

                startlabel.setText("Finish!")
                startlabel.setStyle("italic")

                #give user results
                if rinker > tutus and rinker > library and rinker > yourdorm:
                    title.setText("You should study at Rinker!")
                    instructions.setText("Rinker is the perfect place for you to study! \
                                        You enjoy the quiet aspects of the library, but don't like how crowded it can be. \
                                        \nRinker is a place full of hidden study places we don't always think of. \
                                        \nTheres computer access, tech help when needed, and printing options! \
                                        \nIt has a very convinent location next to the caf and the dorms, \
                                        \nso being hungry or meeting with a group is a piece of cake! \
                                        \nSo now you know where to go, so get studying!")
                    instructions.setTexColor("blue")
                    rinkerpic1 = Image(Point(500, 310), "C:\\Users\\Admin\\Documents\\CSC 2280\\Final project\\rinker.jpg")
                    pt4 = win.getMouse()
                    x = pt4.getX()
                    y = pt4.getY()
                    if x >= 250 and x <=350 and y >= 250 and y <= 350:
                        win.close()
                        
                elif tutus > rinker and tutus > library and tutus > yourdorm:
                    title.setText("You should study at Tutu's!")
                    instructions.setText("Tutu's is the perfect place for you to study! \
                                        \nYou enjoy having a lot of conveniences around you, plus who doesn't \
                                        \nlove a cup of coffee while studying? You're not easily distracted, so being \
                                        \naround people and noise doesn't bother you. It could be that \
                                        \nyou're working on a group project, or you just like having all \
                                        \nof your materials sprawled out on a table. The community study spaces \
                                        \nare great for group projects or study sessions, and the windows double as \
                                        \nhuge wipe boards! \nSo now you know where to go, so get studying!")
                    tutuspic1 = Image(Point(500,310), "C:\\Users\\Admin\\Documents\\CSC 2280\\Final project\\tutus2.jpg")
                    pt4 = win.getMouse()
                    x = pt4.getX()
                    y = pt4.getY()
                    if x >= 250 and x <=350 and y >= 250 and y <= 350:
                        win.close()
                        
                elif library > tutus and library > rinker and library > yourdorm:
                    title.setText("You should study at the library!")
                    instructions.setText("The library is the perfect place for you to study! \
                                        \nLike a lot of students, you need a distraction free zone while you're studying. \
                                        \nThe cubbies in the library are the perfect place to study for a hard test, \
                                        \nbecause it is far from distractions. It helps that you are mostly on campus \
                                        \nall day anyway. The library has a convenient location near Tutu's, \
                                        \nwithout the busy environment. So now you know where to go, so get studying!")
                    librarypic1 = Image(Point(500,310), "C:\\Users\\Admin\\Documents\\CSC 2280\\Final project\\library.jpg")
                    pt4 = win.getMouse()
                    x = pt4.getX()
                    y = pt4.getY()
                    if x >= 250 and x <=350 and y >= 250 and y <= 350:
                        win.close()
                        
                elif yourdorm > tutus and yourdorm > rinker and yourdorm > library:
                    title.setText("You should study at your OWN dorm!")
                    instructions.setText("Your dorm is the perfect place for you to study. \
                                        \nEvery once in a while, people just need to have a chill study time. \
                                        \nThis is the most comfortable place you can be, because you \
                                        \ncan be in pajamas, laying down, and eating snack food too!\
                                        \nBecause you tend to need everything, (like EVERYTHING) in \
                                        \nyour desk, this is the easiest place for you to be. \
                                        \nSo now you know where to go, so get studying!")
                    dormpic1 = Image(Point(500,310), "C:\\Users\\Admin\\Documents\\CSC 2280\\Final project\\dorms.jpg")
                    pt4 = win.getMouse()
                    x = pt4.getX()
                    y = pt4.getY()
                    if x >= 250 and x <=350 and y >= 250 and y <= 350:
                        win.close()
                else:
                    #if there is a tie
                    title.setText("You should study your department's lounge today!")
                    instructions.setText("A lot of the things you need out of a study place are \
                                        \na mixed sort of needs. One of the great parts of being \
                                        \nin a student lounge is the ability to have a study group with \
                                        \nstudents just like you! They will be able to help you \
                                        \nwith your classes, because they'll be in the same ones! \
                                        \nIf you don't know where your department's lounge is, \
                                        \nbe sure to talk to your professors! \
                                        \nSo now you know where to go, so get studying!")
                    tiepic = Image(Point(500,310), "C:\\Users\\Admin\\Documents\\CSC 2280\\Final project\\tie2.jpg")
                    pt4 = win.getMouse()
                    x = pt4.getX()
                    y = pt4.getY()
                    if x >= 250 and x <=350 and y >= 250 and y <= 350:
                        win.close()

            #Run through the questions   
            else:
                abutton.setFill("light gray")
                bbutton.setFill("light gray")
                cbutton.setFill("light gray")
                dbutton.setFill("light gray")
                
                question.setText(questions[i])
                
                opta.setText(A[i])
                optb.setText(B[i])
                optc.setText(C[i])
                optd.setText(D[i])
                
                qnum.setText(numofq[i])

                pt3 = win.getMouse()
                while True:
                    x = pt3.getX()
                    y = pt3.getY()

                    #check which button was clicked
                    #a button clicked
                    if hasstarted and x >= 75 and x <= 90 and y >= 115 and y <= 130:
                        library += 1
                        abutton.setFill("green")
                        break


                    #b button clicked
                    elif hasstarted and x >= 75 and x <= 90 and y >= 135 and y <= 150:
                        rinker += 1
                        bbutton.setFill("green")
                        break


                    #c button clicked
                    elif hasstarted and x >= 75 and x <= 90 and y >= 155 and y <= 170:
                        tutus += 1
                        cbutton.setFill("green")
                        break


                    #d button clicked
                    elif hasstarted and x >= 75 and x <= 90 and y >= 175 and y <= 190:
                        yourdorm += 1
                        dbutton.setFill("green")
                        break

                    #if misclick 
                    else:
                        instructions.setText("Sorry, you didn't click in the right place, \nplease try again!")
                        pt3 = win.getMouse()
                        x = pt3.getX()
                        y = pt3.getY()
                        
            #go to the next question in the cycle     
            i += 1







