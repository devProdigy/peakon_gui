import tkinter as tk
from tkinter import messagebox, ttk

from constants import (
    LARGE_FONT,
    QUESTIONS,
    QUESTIONS_AMOUNT,
    QUESTIONS_COUNTER,
    SCORE_BTNS_AMOUNT,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)
from db.database import db_instance
from screens.results_screen import ResultsScreen
from styles import (
    BUTTONS_STYLE_NAME,
    apply_button_style,
    apply_disabled_status,
    apply_score_button_style,
    clear_score_buttons_styles,
)

X_PADDING = 20


class QuestionsScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.current_question_index = 0
        self.current_question = QUESTIONS[self.current_question_index]
        self.current_clicked_btn_index = None  # index

        self.question_counter = tk.StringVar(value=QUESTIONS_COUNTER.format(self.current_question_index + 1))
        self.question_text = tk.StringVar(value=self.current_question)

        apply_button_style()

        # QUESTION -/-
        question_counter_label = tk.Label(
            self, textvariable=self.question_counter, font=LARGE_FONT, padx=X_PADDING, pady=20
        )
        question_counter_label.config(anchor=tk.CENTER)
        question_counter_label.grid(row=0, column=0, columnspan=SCORE_BTNS_AMOUNT, rowspan=1)

        # Question itself
        question_label = tk.Label(
            self, textvariable=self.question_text, font=LARGE_FONT, wraplength=SCREEN_WIDTH - 50, padx=X_PADDING
        )
        question_label.config(anchor=tk.CENTER)
        question_label.grid(row=1, column=0, columnspan=SCORE_BTNS_AMOUNT)

        self.grid_rowconfigure(2, minsize=30)

        # Choose score
        choose_label = tk.Label(self, text="Choose score:", font=LARGE_FONT, padx=X_PADDING)
        choose_label.config(anchor=tk.CENTER)
        # choose_label.pack(fill="x")
        choose_label.grid(row=3, column=0, columnspan=SCORE_BTNS_AMOUNT)

        # Score buttons
        for i in range(1, SCORE_BTNS_AMOUNT + 1):
            score_btn = ttk.Button(self, text=f"{i}", style=apply_score_button_style(i), width=2)
            score_btn.configure(command=lambda index=i: self.handle_score_button(index))
            score_btn.grid(row=4, column=i - 1)

        # Score tips
        bad_label = tk.Label(self, text="Not at all", font=LARGE_FONT, padx=X_PADDING)
        bad_label.config(anchor=tk.W)
        bad_label.grid(row=6, column=0, columnspan=2)

        good_label = tk.Label(self, text="Absolutely", font=LARGE_FONT, padx=X_PADDING)
        good_label.config(anchor=tk.W)
        good_label.grid(row=6, column=SCORE_BTNS_AMOUNT - 2, columnspan=2)

        self.grid_rowconfigure(7, minsize=20)

        # Comment
        comment_label = tk.Label(self, text="Comment (optional):", font=LARGE_FONT, padx=X_PADDING)
        comment_label.grid(row=8, column=0, columnspan=3)

        self.comment_text = tk.StringVar()
        comment_entry = tk.Entry(self, textvariable=self.comment_text, width=70, justify=tk.LEFT)
        comment_entry.grid(row=9, column=0, columnspan=10, ipady=10)

        next_question_btn = ttk.Button(
            self, text="Nex question", width=12, style=BUTTONS_STYLE_NAME, command=self.next_question,
        )
        next_question_btn.grid(row=10, column=7, columnspan=3, pady=30)

    def next_question(self):
        # check if any of the score buttons were clicked
        if self.current_clicked_btn_index is None:
            messagebox.showerror("Missing score", "Please, choose the score button first.")
            return

        # save result of the question
        self.add_item()

        if self.current_question_index >= QUESTIONS_AMOUNT - 1:
            self.controller.show_frame(ResultsScreen)
            return

        self.current_question_index += 1
        self.current_question = QUESTIONS[self.current_question_index]
        self.question_text.set(self.current_question)
        self.question_counter.set(QUESTIONS_COUNTER.format(self.current_question_index + 1))

        # clear data
        self.current_clicked_btn_index = None
        self.comment_text.set("")
        clear_score_buttons_styles()

    def add_item(self):
        question = self.current_question
        score = self.current_clicked_btn_index
        comment = self.comment_text.get()

        db_instance.insert(question=question, score=score, comment=comment)

    @staticmethod
    def popup_msg(msg: str, title: str):
        popup = tk.Tk()
        popup.geometry(f"{int(SCREEN_WIDTH/2)}x{int(SCREEN_HEIGHT/2)}")
        popup.wm_title(title)
        label = ttk.Label(popup, text=msg, font=LARGE_FONT, width=40, padding=40)
        label.pack(side="top", fill="both", pady=10)
        dismiss_btn = ttk.Button(popup, text="Dismiss", command=popup.destroy)
        dismiss_btn.pack()
        popup.mainloop()

    def handle_score_button(self, index: int):
        # clear all button styles
        clear_score_buttons_styles()

        # apply new style to the clicked button
        apply_disabled_status(index)

        # remember the values of the clicked button
        self.current_clicked_btn_index = index
