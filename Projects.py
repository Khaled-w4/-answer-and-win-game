from termcolor import colored
import time
import os
time.sleep(4)
print(colored("created by khaled_waleed ",'yellow'))
print(colored("twitter ==> @Khaled_4w <== ",'blue'))
time.sleep(3)
print("[Hello.This game has been programmed by a beginner. We apologize for any errors and in the future it will be developed!]")
points = 0

while points >= 0:
    print(colored("Welcome to the [answer and win] game",'green'))
    a1 = input(colored(" Please enter your name : ",'blue'))
    print("%"*50)
    time.sleep(3)
    print(colored("The first question is [1 + 3 equals ?]",'yellow'))
    print("Options [4] [2] [19]")                         
    q1 = (input("Please choose the correct answer:"))
    if q1 == '4'  :
        print(colored("Excellent correct answer ",'green'))
        points += 10 
        print("=" * 30)
        print(colored(f"[You now have {points} points]",'blue')) 
        print("=" * 30)


    else :
        print(colored("- The answer is wrong -",'red'))
        print("[Good luck with the next questions]")

    print("%"*50)
    time.sleep(3)
    print(colored("The second question is [ What is the capital of the Kingdom of Saudi Arabia ?] ",'yellow'))
    print(" options  [[1]-Riyadh] [[2]-Washington] [[3]-Dubai]")
    q2 = (input("Please choose the correct answer : ")).strip().capitalize()
    if q2 == 'Riyadh' or q2=='1':
        print(colored("Excellent correct answer ",'green'))
        points += 10 
        print("=" * 30)
        print(colored(f"[You now have {points} points]",'blue')) 
        print("=" * 30)


    else :
        print(colored("- The answer is wrong -",'red'))
        print("[Good luck with the next questions]")


    print("%"*50)   
    time.sleep(3)  
    print(colored("The third question is [who invented the lamp ?] ",'yellow'))
    print(" options  [[1]-Thomas Edison], [[2]-Nikola Tesla], [[3]-Einstein]")
    q3 = (input("Please choose the correct answer :"))
    if q3 == "Thomas Edison" or q3=="1" :
        print(colored("Excellent correct answer ",'green'))
        points += 10 
        print("=" * 30)
        print(colored(f"[You now have {points} points]",'blue')) 
        print("=" * 30)



    else :
        print(colored("- The answer is wrong -",'red'))
        print("[Good luck with the next questions]")



    print("%"*50)
    time.sleep(3)
    print(colored("the fourth question is [How many colors of the spectrum ?] ",'yellow'))
    print(" options  [[1]-12], [[2]-4], [[3]-7]")
    q4 =  (input("Please choose the correct answer :"))
    if q4 == '7' or q4=='3':
        print(colored("Excellent correct answer ",'green'))
        points += 10 
        print("=" * 30)
        print(colored(f"[You now have {points} points]",'blue')) 
        print("=" * 30)



    else :
        print(colored("- The answer is wrong -",'red'))
        print("[Good luck with the next questions]")

    
    print("%"*50)
    time.sleep(3)
    print(colored("The fifth question is [When was the Kingdom of Saudi Arabia established?] ",'yellow'))
    print(" options  [[1]-1919], [[2]-1455 ], [[3]-1355]")
    q5 =  (input("Please choose the correct answer :"))
    if q5 == '1355' or q5=="3" :
        print(colored("Excellent correct answer ",'green'))
        points += 10 
        print("=" * 30)
        print(colored(f"[You now have {points} points]",'blue')) 
        print("=" * 30)


    else :
        print(colored("- The answer is wrong -",'red'))
        print("[Good luck with the next questions]")


    print("%"*50)
    time.sleep(3)
    print(colored("The sixth question is [How many states in America?] ",'yellow'))
    print(" options  [[1]-38], [[2]-48], [[3]-50]")
    q6 =  (input("Please choose the correct answer :"))
    if q6 == '50' or q6=="3":
        print(colored("Excellent correct answer ",'green'))
        points += 10 
        print("=" * 30)
        print(colored(f"[You now have {points} points]",'blue')) 
        print("=" * 30)


    else :
        print(colored("- The answer is wrong -",'red'))
        print("[Good luck with the next questions]")

    print("%"*50)
    time.sleep(5)
    print(colored("The Seven question is [How many countries are in Asia??] ",'yellow'))
    print(" options  [[1]-98], [[2]-58], [[3]-48]")
    q7 =  (input("Please choose the correct answer :"))
    if q7 == '48'  or "3":
        print(colored("Excellent correct answer ",'green'))
        points += 10 
        print("=" * 30)
        print(colored(f"[You now have {points} points]",'blue')) 
        print("=" * 30)


    else :
        print(colored("- The answer is wrong -",'red'))
        print("[Good luck with the next questions]")



    print("%"*50)
    time.sleep(3)
    print(colored("The eighth question is [When did the second world war start?] ",'yellow'))
    print(" options  [[1]-1928], [[2]-1939 ], [[3]-1945]")
    q8 =  (input("Please choose the correct answer :"))
    if q8 == '1939'  or q8=="2":
        print(colored("Excellent correct answer ",'green'))
        points += 10 
        print("=" * 30)
        print(colored(f"[You now have {points} points]",'blue')) 
        print("=" * 30)

    else :
        print(colored("- The answer is wrong -",'red'))
        print("[Good luck with the next questions]")




    print("%"*50)
    time.sleep(3)
    print(colored("The ninth question is [What is the tallest tower in the world?] ",'yellow'))
    print(" options  [[1]-World Trade Center], [[2]-Makkah clock tower], [[3]-Burj Khalifa]")
    q9 = (input("Please choose the correct answer :"))
    if q9 == "Burj Khalifa" or q9=="3":
        print(colored("Excellent correct answer ",'green'))
        points += 10 
        print("=" * 30)
        print(colored(f"[You now have {points} points]",'blue')) 
        print("=" * 30)

    else :
        print(colored("- The answer is wrong -",'red'))
        print("[Good luck with the next questions]")


    
    print("%"*50)
    time.sleep(3)
    print(colored("The last question is [How tall is the tallest tower in the world ?] ",'yellow'))
    print(" options  [[1]-1200], [[2]-828], [[3]-939]")
    q10 =  (input("Please choose the correct answer :"))
    if q10 == '828' or q10=="2" :
        print(colored("Excellent correct answer ",'green'))
        points += 10 
        print("=" * 30)
        print(colored(f"[You now have {points} points]",'blue')) 
        print("=" * 30)


    else :
        print(colored("- The answer is wrong -",'red'))
        print("[Good luck with the next questions]")


    print(f"Hello [{a1}] You have [{points}] points . ")

    
    if points >= 90 :
        print(colored("Your appreciation is [Excellent]",'green'))

    elif points >= 70 :
        print(colored("Your appreciation is [very good]",'yellow'))

    elif points >= 50 :
        print(colored("Your appreciation is [good]",'blue'))

    elif points >= 40 :
        print(colored("Your appreciation is [Bad]"))

    elif points >= 30 :
        print(colored("Your appreciation is [very Bad]",'red'))
    
    elif points >= 20 or 10 or 0 :
        print(colored("Your appreciation is [very bad please play again]",'red'))

    

    break
