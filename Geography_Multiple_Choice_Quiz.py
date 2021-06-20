#Quiz
import time


class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

print("Welcome to the Geography quiz")
time.sleep(1)


question_prompts = [
     "What is the capital of Peru?\n(A) Lima\n(B) La Paz\n(C) Montevideo\n(D) Quito",
     "What African country has the largest population?\n(A) South Africa\n(B) Nigeria\n(C) Egypt\n(D) Kenya",
     "What US state is furthest west?\n(A) Michigan\n(B) Ohio\n(C) Kentucky\n(D) Alabama",
     "What London Underground line is represented as yellow on the tube map?\n(A) Hammersmith & City\n(B) District\n(C) Circle\n(D) Victoria",
     "What is the currency of Czech Republic\n(A) Koruna\n(B) Forint\n(C) Euro\n(D) Zloty",
     "What is the most visited country in East Asia?\n(A) Thailand\n(B) Japan\n(C) Malaysia\n(D) China",
     "Constantinople and Byzantium are former names of which major city?\n(A) Istanbul\n(B) Athens\n(C) Ankara\n(D) Beirut",
     "What country has the longest coastline in the world?\n(A) Russia\n(B) Canada\n(C) Australia\n(D) Greenland",
     "The Strait of Gibraltar separates the Iberian Peninsular from which African country?\n(A) Libya\n(B) Algeria\n(C) Morocco\n(D) Tunisia",
     "Which of these is not a state of India?\n(A) Rajasthan\n(B) Goa\n(C) Assam\n(D) New Delhi"
]

questions = [
     Question(question_prompts[0], "a"),
     Question(question_prompts[1], "b"),
     Question(question_prompts[2], "c"),
     Question(question_prompts[3], "c"),
     Question(question_prompts[4], "a"),
     Question(question_prompts[5], "d"),
     Question(question_prompts[6], "a"),
     Question(question_prompts[7], "b"),
     Question(question_prompts[8], "c"),
     Question(question_prompts[9], "d"),
]

def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt).lower()
          if answer == question.answer:
               score += 1
     print("You got", score, "out of", len(questions))
     if score in range(0, 5):
         print("Do you even know which way is up?!")
     elif score in range(5, 8):
         print("You know some stuff, but I know you can do better!")
     else:
         print("Congrats, you are way en fuego!")

run_quiz(questions)







