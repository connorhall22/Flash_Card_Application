import time
import json


#Helper Functions
##########################################################
def strip_questions(data,lst):
    questions= {}
    for i in data[lst]:
        words = i.split(":")
        question = words[0]
        answer = words[1]
        answer = answer.strip()
        answer = answer.lower()
        questions[question] = answer
    return questions
    

def get_answer(x):
    ans = input(f"{x}: ")
    ans = ans.strip()
    ans = ans.lower()
    return ans

##########################################################
#Json File
def read_json(filename = "cards.json"):
    with open(filename) as file:
        file_data = json.load(file)
        questions = read_list(file_data)
        file.close()
        return questions

def write_json(new_data, name, filename = "cards.json"):
    with open(filename,"r+") as file:
        file_data=json.load(file)
        file_data.update({name:new_data})
        file.seek(0)
        json.dump(file_data, file, indent = 4)
        file.close()
        return strip_questions(file_data,name)

##########################################################

def setup():

    new_list = input("Would you like to use an already existing list(Y/N)")

    if new_list == "Y":
        read_questions = read_json()
        return read_questions
    else:
        new_questions = []
        name = input("What would you like the name of this set to be? ")
        while True:
            question = input("Please enter the questions and answers in the following format (Question : Answer). Leave blank if finished.")
            if question == "":
                break
            new_questions.append(question)
        write_questions = write_json(new_questions,name)
        return write_questions
      
    
def read_list(data):  
    print("Sets Avaiable:")
    for i in data:
        print(i)
    while True:
        lst = input("Please input what list you would like to study, spelled exactly as it is seen above.") 
        try:
            if data[lst]:
                break
        except:
            print("Invalid input.")

    questions = strip_questions(data,lst)
    print(f"{lst} loaded in successfully.")
    return questions


def flash_cards(dictionary):
    wrong_answers = {}
    for i in dictionary.keys():
        ans = get_answer(i)

        if ans == "skip":
            continue
        if ans == "exit":
            quit()
        
        if ans != dictionary[i]:
            print(f"Wrong, the correct answer was {dictionary[i]}")
            wrong_answers[i] = dictionary[i]
            time.sleep(.5)

        else:
            print("Correct.")
            time.sleep(.5)
    if wrong_answers:
        print("Time to go back through the answers that were missed")
        flash_cards(wrong_answers)
    
    again = input("Finished you got all answers correct. Would you like to go again?(Y/N)")
    return again
           
def main():
    questions = setup()
    print("Let us begin...")
    ans = flash_cards(questions)
    while True:
        if ans == "Y":
            ans = flash_cards(questions)
        else:
            print("All Done")
            break


if __name__ == "__main__":
    main()



