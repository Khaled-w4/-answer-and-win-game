print("[Hello.This game has been programmed by a beginner. We apologize for any errors and in the future it will be developed!]")
points = 0

while points >= 0:
    print("Welcome to the [answer and win] game")
    a1 = input(" Please enter your name : ")
    print("%"*50)
    print("The first question is [1 + 3 equals ?]")
    print("Options [4] [2] [19]")                         
    q1 = (input("Please choose the correct answer:"))
    if q1 == '4'  :
        print("Excellent correct answer ")
        points += 10 
        print("=" * 30)
        print(f"[You now have {points} points]") 
        print("=" * 30)


    else :
        print("- The answer is wrong -")
        print("[Good luck with the next questions]")


    print("%"*50)
    print("The second question is [ What is the capital of the Kingdom of Saudi Arabia ?] ")
    print(" options  [[1]-Riyadh] [[2]-Washington] [[3]-Dubai]")
    q2 = (input("Please choose the correct answer : ")).strip().capitalize()
    if q2 == 'Riyadh' :
        print("Excellent correct answer ")
        points += 10 
        print("=" * 30)
        print(f"[You now have {points} points]") 
        print("=" * 30)


    else :
        print("- The answer is wrong -")
        print("[Good luck with the next questions]")


    print("%"*50)     
    print("The third question is [who invented the lamp ?] ")
    print(" options  [[1]-Thomas Edison], [[2]-Nikola Tesla], [[3]-Einstein]")
    q3 = (input("Please choose the correct answer :"))
    if q3 == "Thomas Edison"  :
        print("Excellent correct answer ")
        points += 10 
        print("=" * 30)
        print(f"[You now have {points} points]") 
        print("=" * 30)



    else :
        print("- The answer is wrong -")
        print("[Good luck with the next questions]")



    print("%"*50)
    print("the fourth question is [How many colors of the spectrum ?] ")
    print(" options  [[1]-12], [[2]-4], [[3]-7]")
    q4 =  (input("Please choose the correct answer :"))
    if q4 == '7' :
        print("Excellent correct answer ")
        points += 10 
        print("=" * 30)
        print(f"[You now have {points} points]") 
        print("=" * 30)



    else :
        print("- The answer is wrong -")
        print("[Good luck with the next questions]")

    
    print("%"*50)
    print("The fifth question is [When was the Kingdom of Saudi Arabia established?] ")
    print(" options  [[1]-1919], [[2]-1455 ], [[3]-1355]")
    q5 =  (input("Please choose the correct answer :"))
    if q5 == '1355'  :
        print("Excellent correct answer ")
        points += 10 
        print("=" * 30)
        print(f"[You now have {points} points]") 
        print("=" * 30)


    else :
        print("- The answer is wrong -")
        print("[Good luck with the next questions]")


    print("%"*50)
    print("The sixth question is [How many states in America?] ")
    print(" options  [[1]-38], [[2]-48], [[3]-50]")
    q6 =  (input("Please choose the correct answer :"))
    if q6 == '50' :
        print("Excellent correct answer ")
        points += 10 
        print("=" * 30)
        print(f"[You now have {points} points]") 
        print("=" * 30)


    else :
        print("- The answer is wrong -")
        print("[Good luck with the next questions]")



    print("%"*50)
    print("The Seven question is [How many countries are in Asia??] ")
    print(" options  [[1]-98], [[2]-58], [[3]-48]")
    q7 =  (input("Please choose the correct answer :"))
    if q7 == '48'  :
        print("Excellent correct answer ")
        points += 10 
        print("=" * 30)
        print(f"[You now have {points} points]") 
        print("=" * 30)


    else :
        print("- The answer is wrong -")
        print("[Good luck with the next questions]")



    print("%"*50)
    print("The eighth question is [When did the second world war start?] ")
    print(" options  [[1]-1928], [[2]-1939 ], [[3]-1945]")
    q8 =  (input("Please choose the correct answer :"))
    if q8 == '1939'  :
        print("Excellent correct answer ")
        points += 10 
        print("=" * 30)
        print(f"[You now have {points} points]") 
        print("=" * 30)

    else :
        print("- The answer is wrong -")
        print("[Good luck with the next questions]")




    print("%"*50)
    print("The ninth question is [What is the tallest tower in the world?] ")
    print(" options  [[1]-World Trade Center], [[2]-Makkah clock tower], [[3]-Burj Khalifa]")
    q9 = (input("Please choose the correct answer :"))
    if q9 == "Burj Khalifa":
        print("Excellent correct answer ")
        points += 10 
        print("=" * 30)
        print(f"[You now have {points} points]") 
        print("=" * 30)

    else :
        print("- The answer is wrong -")
        print("[Good luck with the next questions]")


    
    print("%"*50)
    print("The last question is [How tall is the tallest tower in the world ?] ")
    print(" options  [[1]-1200], [[2]-828], [[3]-939]")
    q10 =  (input("Please choose the correct answer :"))
    if q10 == '828'  :
        print("Excellent correct answer ")
        points += 10 
        print("=" * 30)
        print(f"[You now have {points} points]") 
        print("=" * 30)


    else :
        print("- The answer is wrong -")
        print("[Good luck with the next questions]")


    print(f"Hello [{a1}] You have [{points}] points . ")

    
    if points >= 90 :
        print("Your appreciation is [Excellent]")

    elif points >= 70 :
        print("Your appreciation is [very good]")

    elif points >= 50 :
        print("Your appreciation is [good]")

    elif points >= 40 :
        print("Your appreciation is [Bad]")

    elif points >= 30 :
        print("Your appreciation is [very Bad]")
    
    elif points >= 20 or 10 or 0 :
        print("Your appreciation is [very bad please play again]")

    

    break


     


    
  

  
    