
import json 
with open("C:/Users/cplei/Documents/GitHub/Python-repo/introduction_to_python/Python/Project Hints/students/json/data/quiz.json") as json_file:
    json_data = json.load(json_file)

    quiz= {
        "One": {
            "question": "Our goal at She Codes is to get x women in tech by y.",
            "options": [
                "x=50000, y=2030",
                "x=50000, y=2025",
                "x=100000, y=2025",
                "x=100000, y=2030"
            ],
            "answer": "x=100000, y=2025"
        },
        "Two": {
            "question": "What percentage of tech roles in Australia are currently held by women?",
            "options": [
                "29%",
                "23%",
                "14%",
                "32%"
            ],
            "answer": "29%"
        },
        "Three": {
            "question": "Which is the tutorial we DON'T have on our website?",
            "options": [
                "HTML/CSS",
                "Python",
                "Django",
                "Hardware"
            ],
            "answer": "Hardware"
        },
        "Four": {
            "question": "What kind of food is always served at She Codes events?",
            "options": [
                "Brownies",
                "Sandwiches",
                "Cupcakes",
                "Chocolate"
            ],
            "answer": "Cupcakes"
        }
    }


for question, option in quiz.items():
    print(question, option)