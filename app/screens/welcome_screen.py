import tkinter as tk
from tkinter import ttk

from constants import GREETINGS, LARGE_FONT, SCREEN_HEIGHT, SCREEN_WIDTH
from db.database import db_instance
from screens.questions_screen import QuestionsScreen
from styles import BUTTONS_STYLE_NAME, apply_button_style


class WelcomeScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        apply_button_style()

        part_label = tk.Label(self, text=GREETINGS, font=LARGE_FONT, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        part_label.config(anchor=tk.CENTER)
        part_label.pack(fill="both")

        to_quiz_btn = ttk.Button(
            self,
            text="Go to the quiz =>",
            width=12,
            style=BUTTONS_STYLE_NAME,
            command=lambda: self.start_quiz(controller),
        )
        to_quiz_btn.pack(before=part_label, pady=20, side=tk.BOTTOM)

    @staticmethod
    def start_quiz(controller):
        db_instance.clear_db()
        controller.show_frame(QuestionsScreen)
