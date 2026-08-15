import tkinter as tk
from tkinter import ttk


def create_main_window() -> tk.Tk:
    window = tk.Tk()
    window.title("RadioLab AI")
    window.geometry("1100x700")

    window.columnconfigure(0, weight=0)
    window.columnconfigure(1, weight=1)
    window.rowconfigure(0, weight=1)

    sidebar = ttk.Frame(window, padding=12)
    sidebar.grid(row=0, column=0, sticky="ns")
    sidebar.rowconfigure(3, weight=1)

    app_title = ttk.Label(sidebar, text="RadioLab AI")
    app_title.grid(row=0, column=0, sticky="w", pady=(0, 12))

    new_chat_button = ttk.Button(sidebar, text="+ New Chat")
    new_chat_button.grid(row=1, column=0, sticky="ew")

    recent_label = ttk.Label(sidebar, text="Recent Conversations")
    recent_label.grid(row=2, column=0, sticky="w", pady=(20, 8))

    recent_area = ttk.Frame(sidebar)
    recent_area.grid(row=3, column=0, sticky="nsew")

    settings_button = ttk.Button(sidebar, text="Settings")
    settings_button.grid(row=4, column=0, sticky="ew", pady=(8, 0))

    about_button = ttk.Button(sidebar, text="About")
    about_button.grid(row=5, column=0, sticky="ew", pady=(8, 0))

    main_area = ttk.Frame(window, padding=12)
    main_area.grid(row=0, column=1, sticky="nsew")

    main_area.columnconfigure(0, weight=1)
    main_area.rowconfigure(0, weight=1)

    conversation_area = ttk.Frame(main_area)
    conversation_area.grid(row=0, column=0, sticky="nsew")

    empty_state = ttk.Label(
        conversation_area,
        text="Ask a question about SDR or GNU Radio.",
    )
    empty_state.pack(expand=True)

    input_area = ttk.Frame(main_area)
    input_area.grid(row=1, column=0, sticky="ew", pady=(12, 0))

    question_input = tk.Text(input_area, height=3, wrap="word")
    question_input.pack(side="left", fill="x", expand=True)

    send_button = ttk.Button(input_area, text="Send")
    send_button.pack(side="left", padx=(8, 0))

    return window