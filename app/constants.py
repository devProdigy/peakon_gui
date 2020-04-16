import json
from os import path

APP_FONT_NAME = "Verdana"
LARGE_FONT = (APP_FONT_NAME, 14)
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 400

json_data_file = "app_text.json"
json_data_file_path = path.join("app", json_data_file)

if not path.exists(json_data_file_path):
    json_data_file_path = json_data_file

with open(json_data_file_path) as json_file:
    data = json.load(json_file)

# Welcome screen
GREETINGS = data["GREETINGS"]

# Questions screen
SCORE_BTNS_AMOUNT = 10
QUESTIONS = data["QUESTIONS"]
QUESTIONS_AMOUNT = len(QUESTIONS)
QUESTIONS_COUNTER = "QUESTION {}/" + str(QUESTIONS_AMOUNT)
