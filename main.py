import requests
import html
import random

API_URL = "https://opentdb.com/api.php?amount=10&category=9&type=multiple"

def get_questions():
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()

        #check if questions are available
        if data['response_code'] == 0 and data['results']:
            return data["results"]
    return None

def run_quiz():
    questions = get_questions()
    if not questions:
        print("Failed to fetch questions")
        return
    score = 0
    print("Welcome to the GK Education Quiz!")

    #Loop through each questions
    for i, q in enumerate(questions, 1):
        question = html.unescape(q['question'])
        correct = html.unescape(q["correct_answer"])
        incorrects = [html.unescape(a) for a in q["incorrect_answers"]]

        options = incorrects + [correct]

        random.shuffle(options)

        print(f"question {i}: {question}")

        for idx, option in enumerate(options, 1):
            print(f" {idx}. {option}")

        while True:
            choice = int(input("\n Your answer(1-4): "))
            if 1 <= choice <= 4:
                break

        if options[choice - 1] == correct:
            print("correct! \n")
            score += 1
        else:
            print("wrong! Correct answer is:", correct)

    print(f"Final Score: {score}/{len(questions)}")


run_quiz()