from tkinter import ttk

from constants import APP_FONT_NAME, SCORE_BTNS_AMOUNT

BUTTON_STYLE_TYPE = "TButton"
BUTTONS_STYLE_NAME = f"common.{BUTTON_STYLE_TYPE}"


def apply_button_style():
    buttons_style = ttk.Style()
    buttons_style.configure(BUTTONS_STYLE_NAME, font=(APP_FONT_NAME, 16,  "bold"))


def apply_score_button_style(index) -> str:
    buttons_style = ttk.Style()
    style_name = f"{index}.{BUTTON_STYLE_TYPE}"
    buttons_style.configure(style_name, font=(APP_FONT_NAME, 16, "bold"))
    buttons_style.map(
        style_name,
        foreground=[('active', 'blue')],
        background=[('pressed', '!disabled', 'black'), ('active', 'white')]
    )
    return style_name


def clear_score_buttons_styles():
    for i in range(1, SCORE_BTNS_AMOUNT + 1):
        apply_score_button_style(i)


def apply_disabled_status(index):
    style = ttk.Style()
    style_name = f"{index}.{BUTTON_STYLE_TYPE}"
    style.map(
        style_name,
        foreground=[("!disabled", "red")],
    )
