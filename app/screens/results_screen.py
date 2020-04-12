import tkinter as tk
from tkinter import ttk

from db.database import db_instance
from styles import BUTTONS_STYLE_NAME, apply_button_style


class ResultsScreen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        apply_button_style()

        self.results_list = tk.Listbox(self, height=18, width=70, border=1)
        self.results_list.grid(row=0, column=0, columnspan=3, rowspan=26, pady=20, padx=20)
        # Create scrollbar
        scrollbar = tk.Scrollbar(self)
        scrollbar.grid(row=0, column=3)
        # Set scroll to listbox
        self.results_list.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=self.results_list.yview)

        quit_btn = ttk.Button(
            self,
            text="Close app",
            style=BUTTONS_STYLE_NAME,
            command=self.quit_app,
        )
        quit_btn.grid(row=26, column=0, columnspan=1, pady=5)

        next_question_btn = ttk.Button(
            self,
            text="Show results",
            style=BUTTONS_STYLE_NAME,
            command=self.populate_results,
        )
        next_question_btn.grid(row=26, column=2, columnspan=3, pady=5)

    def populate_results(self):
        self.results_list.delete(0, tk.END)
        for row in db_instance.fetch():
            record = f"{row[0]}. '{row[1]}': score - {row[2]}, comment - '{row[3]}'."
            self.results_list.insert(tk.END, record)

    def quit_app(self):
        self.quit()
