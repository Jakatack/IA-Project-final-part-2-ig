'''
Jack Gross
February 24, 2021
This is the "Post Oak Grade Getter" Application
Tool for use by students to gather information about their classes quickly and efficiently
The overall goal of this application is to make it so easy for students to know how they are doing in all of their classes that they find it difficult to fall behind
'''


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import tkinter as tk
from functools import partial

global username
global password
global classcounter

classcounter = 0

BIGWIDTH = 15
BIGHEIGHT = 10
BIGYES = '#2B5945'
BIGNO = '#fff7fe'

color = [BIGNO, BIGNO, BIGNO, BIGNO, BIGNO, BIGNO, BIGNO, BIGNO, BIGNO, BIGNO, BIGNO, BIGNO, BIGNO, BIGNO]

#Assigning link and name for every class to a variable
bio = 'https://postoakschool.learning.powerschool.com/janetott/biology2020-21/sbg_student_detail'
bioN = 'Biology'
chem = 'https://postoakschool.learning.powerschool.com/hannahmayhew/chem-122020-21/sbg_student_detail'
chemN = 'Chemistry'
compSci = 'https://postoakschool.learning.powerschool.com/mikeberadino/computersciencegrade_12/sbg_student_detail'
compSciN = 'Computer Science'
econ = 'https://postoakschool.learning.powerschool.com/jamesquillin/ehc2020-21/sbg_student_detail'
econN = 'Economics'
film = 'https://postoakschool.learning.powerschool.com/kimharrison/film2021/sbg_student_detail'
filmN = 'Film'
gphc = 'https://postoakschool.learning.powerschool.com/davidroddy/gphc2020-2021/sbg_student_detail'
gphcN = 'GPHC'
lit = 'https://postoakschool.learning.powerschool.com/kimharrison/languageandliterature/sbg_student_detail'
litN = 'Literature'
music = 'https://postoakschool.learning.powerschool.com/maxwelllowery/1112music2020-2021/sbg_student_detail'
musicN = 'Music'
mathjacobs = 'https://postoakschool.learning.powerschool.com/mattjacobs/mathapplications2020-21/sbg_student_detail'
mathjacobsN = 'Math Jacobs'
math = 'https://postoakschool.learning.powerschool.com/jeremygrisbee/upperlevelmathematics2020/sbg_student_detail'
mathN = 'Math Analysis'
spanish = 'https://postoakschool.learning.powerschool.com/andreanovak/espaol1112/sbg_student_detail'
spanishN = 'Spanish 11-12'
theatre = 'https://postoakschool.learning.powerschool.com/dana.bowman/upperleveltheatre2020-2021/sbg_student_detail'
theatreN = 'Theatre'
tok = 'https://postoakschool.learning.powerschool.com/casiecobos/theoryofknowledge20202021/sbg_student_detail'
tokN = 'Theory of Knowledge'
VisArt = 'https://postoakschool.learning.powerschool.com/emilysloan/ulvisualartsseniors2020-21/sbg_student_detail'
VisArtN = 'Visual Art'

#classes & their colloquial names put into arrays
allClasses = [bio, chem, compSci, econ, film, gphc, lit, music, mathjacobs, math, spanish, theatre, tok, VisArt]
allNames = [bioN, chemN, compSciN, econN, filmN, gphcN, litN, musicN, mathjacobsN, mathN, spanishN, theatreN, tokN, VisArtN]

#empty array created for user selected classes
selectedclasses = ["", "", "", "", "", "", "", "", ""]
selectedNames = ["", "", "", "", "", "", "", "", ""]

window = tk.Tk()
greeting = tk.Label(text="Hello, and welcome, you are an estemed beta tester, wow ")

greeting.pack()

frame = tk.Frame(master=window, width=100000, height=1000)
frame.pack()


def classgatherer(chosenOne):
    global classcounter
    selectedclasses[classcounter] = allClasses[chosenOne]
    selectedNames[classcounter] = allNames[chosenOne]

    print(allNames[chosenOne])
    print(allClasses[chosenOne])

    print(classcounter)
    classcounter += 1
    Buttons[chosenOne].configure(bg="#2B5945") #makes
    if classcounter == 8:
        print("finish!")


#buttons for all classes
BioButton = tk.Button(master=frame, command=partial(classgatherer, 0), text="Bio", bg=color[0], width=BIGWIDTH, height=BIGHEIGHT)
BioButton.grid(row=1, column=4)

ChemButton = tk.Button(master=frame, command=partial(classgatherer, 1), text="Chem", bg=color[1], width=BIGWIDTH, height=BIGHEIGHT)
ChemButton.grid(row=1, column=5)

ComputerScienceButton = tk.Button(master=frame, command=partial(classgatherer, 2), text="Computer Science", bg=color[2], width=BIGWIDTH, height=BIGHEIGHT)
ComputerScienceButton.grid(row=1, column=6)

EconButton = tk.Button(master=frame, command=partial(classgatherer, 3), text="Econ", bg=color[3], width=BIGWIDTH, height=BIGHEIGHT)
EconButton.grid(row=1, column=7)

FilmButton = tk.Button(master=frame, command=partial(classgatherer, 4), text="Film", bg=color[4], width=BIGWIDTH, height=BIGHEIGHT)
FilmButton.grid(row=1, column=8)

GPHCButton = tk.Button(master=frame, command=partial(classgatherer, 5), text="GPHC", bg=color[5], width=BIGWIDTH, height=BIGHEIGHT)
GPHCButton.grid(row=1, column=9)

LitButton = tk.Button(master=frame, command=partial(classgatherer, 6), text="Lit", bg=color[6], width=BIGWIDTH, height=BIGHEIGHT)
LitButton.grid(row=1, column=10)

MusicButton = tk.Button(master=frame, command=partial(classgatherer, 7), text="Music", bg=color[7], width=BIGWIDTH, height=BIGHEIGHT)
MusicButton.grid(row=1, column=11)

MathJacobsButton = tk.Button(master=frame, command=partial(classgatherer, 8), text="Math Jacobs", bg=color[8], width=BIGWIDTH, height=BIGHEIGHT)
MathJacobsButton.grid(row=1, column=12)

MathButton = tk.Button(master=frame, command=partial(classgatherer, 9), text="Math", bg=color[9], width=BIGWIDTH, height=BIGHEIGHT)
MathButton.grid(row=1, column=13)

SpanishButton = tk.Button(master=frame, command=partial(classgatherer, 10), text="Spanish", bg=color[10], width=BIGWIDTH, height=BIGHEIGHT)
SpanishButton.grid(row=1, column=14)

TheatreButton = tk.Button(master=frame, command=partial(classgatherer, 11), text="Theatre", bg=color[11], width=BIGWIDTH, height=BIGHEIGHT)
TheatreButton.grid(row=1, column=15)

TOKButton = tk.Button(master=frame, command=partial(classgatherer, 12), text="TOK", bg=color[12], width=BIGWIDTH, height=BIGHEIGHT)
TOKButton.grid(row=1, column=16)

VisualArtButton = tk.Button(master=frame, command=partial(classgatherer, 13), text="Visual Art", bg=color[13], width=BIGWIDTH, height=BIGHEIGHT)
VisualArtButton.grid(row=1, column =17)


Buttons = [BioButton, ChemButton, ComputerScienceButton, EconButton, FilmButton, GPHCButton, LitButton, MusicButton, MathJacobsButton, MathButton, SpanishButton, TheatreButton, TOKButton, VisualArtButton]

window.mainloop()


class1 = selectedclasses[0]
class1n = selectedNames[0]

class2 = selectedclasses[1]
class2n = selectedNames[1]

class3 = selectedclasses[2]
class3n = selectedNames[2]

class4 = selectedclasses[3]
class4n = selectedNames[3]

class5 = selectedclasses[4]
class5n = selectedNames[4]

class6 = selectedclasses[5]
class6n = selectedNames[5]

class7 = selectedclasses[6]
class7n = selectedNames[6]

class8 = selectedclasses[7]
class8n = selectedNames[7]

def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

    global username
    global password
    username = e1.get()
    password = e2.get()

    print(username)
    print(password)


master = tk.Tk()
tk.Label(master, text="First & Last name").grid(row=0)
tk.Label(master, text="Google acc password").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e1.insert(10, "JohnDoe")
e2.insert(10, "Password")

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=tk.W, pady=4)
tk.Button(master, text='Submit', command=master.quit).grid(row=3, column=1, sticky=tk.W, pady=4)

master.mainloop()


PATH = "C:\Program Files\JetBrains\PyCharm Community Edition 2020.2.2\chromedriver.exe"
driver = webdriver.Chrome(PATH)

def login():
    driver.get('https://postoakschool.learning.powerschool.com/do/account/login')
    print(driver.title)

    time.sleep(3)
    search = driver.find_element_by_id('login').send_keys(username)
    search = driver.find_element_by_id('password').send_keys(password + Keys.ENTER)

    time.sleep(3)
    search = driver.find_element_by_id('identifierId').send_keys(username + '@stu.postoakschool.org'+ Keys.ENTER)

    time.sleep(5)

    search = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password + Keys.ENTER)

login()


def waitForGrades(link):
    CurrentClass=""
    driver.get(link)
    loopnums=0
    fullloop=0
    while CurrentClass == "":
        CurrentClass = driver.find_element_by_id('sbg_overall_grade_span').text
        time.sleep(0.1)
        loopnums+=1
        if loopnums == 50:
            driver.get(link)
            loopnums = 0
            fullloop+=1
            if fullloop == 3:
                print("Error, please try again")
                break
    return CurrentClass

def scrape():

    mygrade=waitForGrades(class1)
    print(mygrade + ' In ' + class1n)

    mygrade=waitForGrades(class2)
    print(mygrade + ' In ' + class2n)

    mygrade=waitForGrades(class3)
    print(mygrade + ' In ' + class3n)

    mygrade = waitForGrades(class4)
    print(mygrade + ' In ' + class4n)

    mygrade = waitForGrades(class5)
    print(mygrade + ' In ' + class5n)

    mygrade = waitForGrades(class6)
    print(mygrade + ' In '+ class6n)

    mygrade = waitForGrades(class7)
    print(mygrade + ' In ' + class7n)

scrape()