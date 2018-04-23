""" in name picker2 I will add a leftover file2 wich is a leftover file
I will load it as leftoverlist = file2.readlines().
next I will edit the pick_out function to see if the leftover list is empty or not
if it is empty it will reasign leftover with all of class list.
in the first case leftver should be empty.

then I will add a new fuction wich will write the contents of leftover to file2
and call that function when x is chosen

must take the list and write each line to the file.

"""





import os, random
from datetime import datetime

 

file1 = open('class_1_pin_eng.txt',encoding='utf-8', mode='r')
file2 = open('class_1_leftover.txt',encoding='utf-8', mode='r') 
#global classlist
#global leftover

classlist = file1.readlines()
leftover = file2.readlines() 
file1.close()
file2.close() 


def check_leftover():   #checks if leftover is empty
    global leftover
    if len(leftover)<1:
        leftover = list(classlist) #if empty assigns it the contents of class list
        print("I have refilled..") # but you cannot do leftover = classlist as 
#this would not copy the list but assign two variable s to the same lsit
# you must use built in list function new_list = list(old_list)       
#if the program books a totaly empty list it will still read as having one
#element as it is the Utf-8 marker
#so in that case chosing c will give no name


def write_leftover_file():
    file2 = open('class_1_leftover.txt',encoding='utf-8', mode='w')
    for item in leftover:
        file2.write(item)
    file2.close()


def print_list():
    print("%"*30)
    for item in classlist:
        print(item)
    print("Total:",len(classlist))    

def print_rating():
    num = 0
    with open('class_1_rating.txt',encoding='utf-8', mode='r')as file3:
        for line in file3:
            print(line)
            num+=1 #must use a iteratable var as file not loaded as string
        print("Total:",num)

def print_left():
    print("%"*30)
    for item in leftover:
        print(item)
    print("Total:",len(leftover))

def pick_out():
    
    check_leftover()  #check to see if leftover is empty    
    
    choi = random.choice(leftover) #gets random choice form leftover
    #leftover.remove(choi)  #removers from leftover
    print("%"*20, "PICK","%"*20,"\n")
    print(choi)
    print("%"*46)
    rate_stu_save(choi)


def rate_stu_save(student):
    rating = ""
    myrate =" "
    while myrate not in "QqEePpOo": 
        myrate =input("Enter\n Q = Low\n E = Middle\n P = High\n O = don't save\n: ")
        

    if myrate == "o":
        print("The student hasn't been removed")
        return
    elif myrate == "q":
        rating = " a Poor response"
    elif myrate == "e":
        rating = " a Standard response"
    elif myrate == "p":
        rating = " an Exceptional response"

    leftover.remove(student)  #removers from leftover list
    student = student[:-1]  #removes the line return \n from student so it saves nicely
    stamptime = str(datetime.now())
    stu_rating = "{} gave {} on {}\n".format(student,rating,stamptime)
    print(stu_rating)
    with open('class_1_rating.txt',encoding='utf-8', mode='a+')as file3:
        file3.write(stu_rating)
               
            
        



       


work = True
#print("leftover:",leftover, len(leftover))
#print("class list;",classlist, len(classlist))
while work == True:

    mychoice = input("Enter\n C = CHOOSE\n P = Print Class\n L = Print Leftover\n R = Print Rating\n X = Save/Quit\n: ")
    if mychoice not in "CcPpXxLlRr":
        print("Not a choice")
    elif mychoice == "c":
        pick_out()
        
    elif mychoice == "p":
        print_list()
    elif mychoice == "l":
        print_left()
    elif mychoice == "r":
        print_rating()
    elif mychoice == "x":
        write_leftover_file()
        work = False

        



        
