
APP_FONT_NAME = "Verdana"
LARGE_FONT = (APP_FONT_NAME, 14)
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 400

# TODO read from the config file
# Welcome screen
GREETINGS = """
Hi!

Employee satisfaction is vital for us. 
We use this quiz to collect the feedback on:
 - what is working in the organization well; 
 - and what requires improvements. 

It will take you about 10 minutes to fill the survey in.
We appreciate your honesty and openness.
"""

# Questions screen
SCORE_BTNS_AMOUNT = 10
QUESTIONS = [
    "How likely is it you would recommend ___ as a place to work?",
    "At work, I have the opportunity to do what I do best every day.",
    "I can have well-informed and constructive conversations with my manager about pay.",
    "The atmosphere in my team is friendly and easy-going.",
    "I find my workload manageable.",
    "My job enables me to learn and develop new skills.",
    "My manager cares about my opinions.",
    "Our organization does a good job of communicating the goals and strategies set by senior leadership.",
]
QUESTIONS_AMOUNT = len(QUESTIONS)
QUESTIONS_COUNTER = "QUESTION {}/" + str(QUESTIONS_AMOUNT)
