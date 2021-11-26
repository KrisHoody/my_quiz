"""
 Import json library
"""
import json
score = 0
name = ""
print("Welcome to movie quiz.")

"""
User can put only letter if enters his name.
If name dont't contain letters user program stops and asks user for another try.
"""
while True:
    your_name = input("Enter your name, please: ")
    if your_name.isalpha():
        print("Welcome," + your_name)   
        print("You will be presented with 20 Questions.")
        print("Enter your choice to get the points. Good luck!")
        break
    else:
         print("Only letters, please")

   
"""
Questions are printed without answers.
"""

def questions(all_questions):
    global score 
    print(all_questions["Question"])
    print("1", all_questions["1"])
    print("2", all_questions["2"])
    print("3", all_questions["3"])
    print("4", all_questions["4"])

    """
    User answer.
    """

    guest_answer = int(input('Your answer:\n'))

    """
    Ask user to put only number beetween 1 and four.
    If number is smaller or greater is asked to choose beetween 1 and 4.
    """

    while guest_answer > 4 or guest_answer <= 0:
        print("Please choose between 1 and 4")
        guest_answer = int(input("Please try again: "))
    else:
        return guest_answer

    """
    Checks if user answer is right, and if yes user earns a point.
    If not right answer is displayed.
    """

    if guest_answer == all_questions["right_answer"]:
        score += 1
        print("Great! You've earned a point. You've got:", score, "points")
        print("-----------------")
    else:
        print("Sorry, this is wrong answer")
        print("The right answer is", all_questions["right_answer"])
        print("-----------------")



""" 
Open json file with questions in another file.
"""

with open("quiz_main.json") as que_s:
    all_questions = json.load(que_s)

    """
    Loop to ask for question
    """

    for i in range(0, len(all_questions)):
        questions(all_questions[i])
"""
Program prints number of points.
"""
print("This is the end of quiz. You've got", score, "points.")