import json

APP_FONT_NAME = "Verdana"
LARGE_FONT = (APP_FONT_NAME, 14)
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 400

with open("app_text.json") as json_file:
    data = json.load(json_file)

# Welcome screen
GREETINGS = data["GREETINGS"]

# Questions screen
SCORE_BTNS_AMOUNT = 10
QUESTIONS = data["QUESTIONS"]
QUESTIONS_AMOUNT = len(QUESTIONS)
QUESTIONS_COUNTER = "QUESTION {}/" + str(QUESTIONS_AMOUNT)
