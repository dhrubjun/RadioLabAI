import threading
import tkinter as tk
from tkinter import ttk

from radiolab_ai.app.conversation import get_response
from radiolab_ai.llm.ollama_client import LLMError


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

    conversation_display = tk.Text(
        conversation_area,
        wrap="word",
    )
    conversation_display.insert(
        "end",
        "Ask a question about SDR or GNU Radio.",
    )
    conversation_display.config(state="disabled")

    conversation_scrollbar = ttk.Scrollbar(
        conversation_area,
        orient="vertical",
        command=conversation_display.yview,
    )

    conversation_display.configure(
        yscrollcommand=conversation_scrollbar.set,
    )

    conversation_display.pack(
        side="left",
        fill="both",
        expand=True,
    )

    conversation_scrollbar.pack(
        side="right",
        fill="y",
    )

    input_area = ttk.Frame(main_area)
    input_area.grid(row=1, column=0, sticky="ew", pady=(12, 0))

    def submit_from_keyboard(event):
        if event.state & 0x0001:
            return

        submit_message()
        return "break"

    question_input = tk.Text(input_area, height=3, wrap="word")
    question_input.pack(side="left", fill="x", expand=True)
    question_input.bind("<Return>", submit_from_keyboard)

    has_messages = False

    def generate_response_in_background(message: str):
        try:
            response = get_response(message)
        except LLMError:
            response = (
                "RadioLab AI could not reach the local model. "
                "Please make sure Ollama is running and the configured model is installed."
            )

        window.after(0, display_response, response)

    def display_response(response: str):
        conversation_display.config(state="normal")
        conversation_display.insert("end", f"RadioLab AI\n{response}\n\n")
        conversation_display.see("end")
        conversation_display.config(state="disabled")

    def submit_message():
        nonlocal has_messages

        message = question_input.get("1.0", "end").strip()

        if not message:
            return

        if not has_messages:
            conversation_display.config(state="normal")
            conversation_display.delete("1.0", "end")
            conversation_display.config(state="disabled")
            has_messages = True

        conversation_display.config(state="normal")
        conversation_display.insert("end", f"You\n{message}\n\n")
        conversation_display.see("end")
        conversation_display.config(state="disabled")

        question_input.delete("1.0", "end")

        worker = threading.Thread(
            target=generate_response_in_background,
            args=(message,),
            daemon=True,
        )
        worker.start()

    send_button = ttk.Button(
        input_area,
        text="Send",
        command=submit_message,
    )
    send_button.pack(side="left", padx=(8, 0))

    return window