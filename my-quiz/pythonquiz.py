# Python Quiz Game  
import random 
import time 
import sys
from colorama import Fore, Style, init
init()

# Animation Function

def console_loading_animation(duration_seconds=3):
    animation_frames = [Fore.CYAN + "|", "/", "-", "\\" + Style.RESET_ALL]
    start_time = time.time() 
    frame_index = 0

    while time.time() - start_time < duration_seconds:
        sys.stdout.write("\r" + animation_frames[frame_index % len(animation_frames)] + Fore.YELLOW + " Loading..." + Style.RESET_ALL)
        sys.stdout.flush()
        frame_index += 1
        time.sleep(0.1) # Adjust To Change Animation Speed

    sys.stdout.write("\r" + " " * 20 + "\r") # Clear The Animation Line
    sys.stdout.flush()
    
# Questions 
questions = ("""What is the output of the following code? - valueOne = 5 ** 2 
                                            valueTwo = 5 ** 3
                                            print(valueOne)            
                                            print(valueTwo)""",              #1
             """What is the output of print("Python" * 2 + "is fun")?""",  #2 
             """What is the output of the following code? - for x in range(0.5, 5.5, 0.5):  
                                                print(x)""",            #3
             "Which of the following data types is mutable in Python?",   #4
           """What is the purpose of "self" in a Python class method?""",     #5 
             "Which of the following is not a valid variable name in Python?", #6   
           """What is the output of the following code? - str = "pynative" 
                                            print(str[1:3])""",       #7
           """How do you add an element at the end of a "List" in Python?""",  #8
           """What will be the output of print(3 * "Abc")?""",         #9
           """What is the purpose of the 'if__name__=="__main__":' block?""",   #10
            """What is the output of the following code? - var = "James Bond"
                                            print(var[2::-1])""",     #11
             "What is the output print(bool(0))?",        #12
             """Can we use the “else” block for a "for loop"? 
                              example: for i in range(1, 5):
                                           print(i)
                                       else:
                                           print("this is else block statement")""",   #13
             """What is the output of the following code? - sampleSet = {"Jodi", "Eric", "Garry"}
                                                          sampleSet.add(1, "Vicki")
                                                          print(sampleSet)""",    #14
             """How do you remove an item from a dictionary with a specific key "key_name"?""",
             """What is the output of the following code? - my_list[1, 2, 3, 4]
                                            print(my_list[2])""",   #15
             "How do you get the current working directory in Python?",       #16
             "Which operator has the higher precedence in the following list?",   #17
           """What is the output of the following code? - print("Python" + "Quiz")""",  #18
             """What is the output of the following code? - def calculate (num1, num2=4):
                                                res = num1 * num2
                                                print(res)

                                                calculate(5, 6)""")  #19 

options = (("A.10|15", "B.Error:Invalid Input", "C.25|125", "D.valueOne|valueTwo"), #1
           ("A.Python is funPython", "B.Error", "C.PythonPython is fun", "D.PythonPythonis fun"), #2
           ("A.Error:Program Executes", "B.[0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]", #3
            "C.[0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5]", "D.0.5, 5.5, 0.5"),  #4
           ("A.list", "B.tuple", "C.str", "D.int"),  #5
           ("A.it refers to the class itself", "B.it refers to the instance of the class", "C.it is a reserved keyword for static methods", "D.it is a placeholder for any argument"), #6
           ("A._my_variable", "B.myVariable", "C.2myvariable", "D.my_variable2"), #7
           ("A.py ", "B.yn ", "C.pyn", "D.yna"), #8
           ("A.list.add(element)", "B.list.insert(element)", "C.list.append(element)", "D.list.extend(element)"), #9
           ("A.AbcAbcAbc", "B.Error", "C.3Abc", "D.Abc3"), #10
           ("A.it defines a global variable", "B.it marks the beginning of class definition", "C.it ensures that the code inside this block only runs when the script is executed directly", "D.it is used for multi-threading"), #11
           ("A.Jam", "B.dno", "C.maJ", "D.dnoB semaJ"),  #12
           ("A.True", "B.False", "C.None", "D.Error"),  #13
           ("A for Yes", "B for No"),   #14
           ("A.{'Vicki','Jodi','Garry','Eric'}", "B.{'Jodi','Vicki','Garry','Eric'}", "C.The program executed with error", "D.'Jodi','Vicki','Garry','Eric',"), #15
           ("A.del my_dict[key_name]", "B.my_dict.remove(key_name)", "C.my_dict.delete(key_name)", "D.my_dict.pop_key(key_name)"),  #16
           ("A.1", "B.2", "C.3", "D.4"),   #16
           ("A.os.cwd()", "B.os.get_current_directory()", "C.os.getcwd()", "D.os.current_dir()"), #17
           ("A.%(Modulus)", "B.&(BitWise AND)", "C.>(Comparison)", "D.**(Exponent)"),   #18
           ("A.Python Quiz", "B.PythonQuiz", "C.Python+Quiz", "D.Error"),  #19
           ("A.20", "B.The program executed with errors", "C.30")) #20

print() 
print(Fore.YELLOW + "Welcome To My Beginner's Python Quiz!" + Style.RESET_ALL)
print() 
print(Fore.YELLOW + "GOOD LUCK!" + Style.RESET_ALL)
input(Fore.YELLOW + "\nPress Enter To Continue...\n" + Style.RESET_ALL)
print() 

if __name__ == "__main__":
    print(Fore.CYAN + "Starting Quiz..." + Style.RESET_ALL)
    console_loading_animation(duration_seconds=3) # Run Animation For Specified Time

answers = ("C", "D", "A", "A", "B", "C", "D", "C", "A", "C", "C", "B", "A", "B", "D", "C", "C", "D", "B", "C") 

# Define and Zip
quiz_data = list(zip(questions, options, answers))

# Randomize Zipped Data
random.shuffle(quiz_data)

# Unzip 
questions, options, answers = zip(*quiz_data)
guesses = [] 
score = 0 
question_num = 0     
# Main Loop For Quiz
for question in questions:
    print(Fore.BLUE + "----------------------" + Style.RESET_ALL)
    print(Fore.YELLOW + question + Style.RESET_ALL)
    print() 
    
    for option in options[question_num]:
        print(Fore.CYAN + option + Style.RESET_ALL)     

    guess = input(Fore.YELLOW + "Enter (A, B, C, D): " + Style.RESET_ALL).upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print(Fore.GREEN + "CORRECT" + Style.RESET_ALL)
    else:
        print(Fore.RED + "INCORRECT" + Style.RESET_ALL)    
        print(Fore.RED + f"{answers[question_num]} is the correct answer" + Style.RESET_ALL)  
    question_num += 1 

if __name__ == "__main__":
    print(Fore.CYAN + "Calculating Results..." + Style.RESET_ALL)
    console_loading_animation(duration_seconds=3)

print(Fore.YELLOW + "----------------------" + Style.RESET_ALL)
print(Fore.YELLOW + "       RESULTS        " + Style.RESET_ALL)
print(Fore.YELLOW + "----------------------" + Style.RESET_ALL)

print()

print(Fore.CYAN + "guesses: " + Style.RESET_ALL, end="")

for guess in guesses:
    print(Fore.YELLOW + guess + Style.RESET_ALL, end=" ")
print()

score = int(score / len(questions) * 100)
print(Fore.CYAN + "Your score is: " + Fore.GREEN + f"{score}%" + Style.RESET_ALL) 

