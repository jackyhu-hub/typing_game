import tkinter as tk
import random

words = {
    "Normal": ["apple", "banana", "mango", "keyboard", "window"],
    "Hard": ["binary search", "linked list", "cloud storage"],
    "Nightmare": [
        "Practice makes perfect.",
        "Accuracy is more important than speed."
    ]
}

rounds = 5
current_round = 0
correct_count = 0
time_left = 10
selected_mode = "Normal"

current_answer = ""
timer_running = False

root = tk.Tk()
root.title("Speed Typing Challenge")
root.geometry("600x400")

def set_mode(mode):
    global selected_mode
    selected_mode = mode

def start_game():
    global rounds, current_round, correct_count
    text = round_entry.get()

    if text.isdigit() and int(text) > 0:
        rounds = int(text)
    else:
        rounds = 5

    current_round = 0
    correct_count = 0
    result_label.config(text="")
    start_btn.config(state="disabled")

    next_round()

def next_round():
    global current_round, time_left, timer_running, current_answer

    if current_round >= rounds:
        end_game()
        return

    current_round += 1

    if selected_mode == "Nightmare":
        time_left = 15
    else:
        time_left = 10

    timer_running = True

    current_answer = random.choice(words[selected_mode])
    word_label.config(text=current_answer)

    input_entry.delete(0, tk.END)
    input_entry.focus()

    update_timer()

def update_timer():
    global time_left, timer_running

    if not timer_running:
        return

    timer_label.config(text=f"Time: {time_left:.1f}s")

    if time_left <= 0:
        timer_running = False
        result_label.config(text=f"Time's up! 正確答案: {current_answer}")
        root.after(1000, next_round)
        return

    time_left -= 0.1
    root.after(100, update_timer)

def check_answer(event=None):
    global timer_running, correct_count

    if not timer_running:
        return

    user_input = input_entry.get().strip()

    if user_input == current_answer:
        correct_count += 1
        result_label.config(text="正確!")
    else:
        result_label.config(text=f"錯誤! 正確答案: {current_answer}")

    timer_running = False
    root.after(500, next_round)

def end_game():
    word_label.config(text="Game Over")

    score_percent = int(correct_count / rounds * 100)

    timer_label.config(
        text=f"Final Score: {correct_count}/{rounds} ({score_percent}%)"
    )

    result_label.config(text="")
    start_btn.config(state="normal")

tk.Label(root, text="Rounds:").pack()

round_entry = tk.Entry(root, width=5, justify="center")
round_entry.insert(0, "5")
round_entry.pack()

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Normal", width=10,
          command=lambda: set_mode("Normal")).grid(row=0, column=0, padx=5)

tk.Button(btn_frame, text="Hard", width=10,
          command=lambda: set_mode("Hard")).grid(row=0, column=1, padx=5)

tk.Button(btn_frame, text="Nightmare", width=10,
          command=lambda: set_mode("Nightmare")).grid(row=0, column=2, padx=5)

start_btn = tk.Button(root, text="Start Game", width=15, command=start_game)
start_btn.pack(pady=10)

word_label = tk.Label(root, text="", font=("Arial", 24))
word_label.pack(pady=10)

timer_label = tk.Label(root, text="Time: --", font=("Arial", 14))
timer_label.pack()

input_entry = tk.Entry(root, font=("Arial", 16), justify="center")
input_entry.pack(pady=10)

input_entry.bind("<Return>", check_answer)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack()

root.mainloop()
