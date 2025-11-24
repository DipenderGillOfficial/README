# Study Grind Boss Planner

A simple, straightforward command-line application to help you keep track of your study tasks without the bloat. It's written in plain Python and saves everything to a single, easy-to-read file.

## Features

* **View Tasks:** See your whole to-do list with clear status checks (`[ ]` or `[DONE]`).
* **Add Tasks:** Quickly throw in the next topic you need to conquer.
* **Mark Complete:** Celebrate your wins by marking tasks as done! 🎉
* **Trash Tasks:** Delete tasks you've decided aren't important anymore (or just finished).
* **Persistent Storage:** All your data is automatically saved to a file called `tasks.txt` every time you exit.

---

## How to Run It

1.  **Prerequisites:** You need **Python 3** installed on your computer.
2.  **Save the Code:** Save the provided Python script as a file named `planner.py` (or whatever you like).
3.  **Run from Terminal:** Open your terminal or command prompt, navigate to the folder where you saved the file, and run:

    ```bash
    python planner.py
    ```

4.  **Start Grinding!** Follow the on-screen menu to manage your study goals.

---

## Data Storage

This app uses the built-in `json` library to save your data.

* **File Name:** `tasks.txt`
* **What's in it?** It stores a list of dictionaries. For example:

    ```json
    [
        {
            "name": "Review Calculus Ch 3",
            "is_done": true
        },
        {
            "name": "Write 500 words for English paper",
            "is_done": false
        }
    ]
    ```

You can technically open and edit `tasks.txt` yourself, but it's safer to use the app!

---

## Known Quirks (aka The Code's Personality)

Since this app was written quickly, there are a few things that make it unique:

1.  **Menu Inefficiency:** In the main loop, it checks every single menu option using separate `if` statements instead of using the faster `elif`. It works, but it's a bit extra!
2.  **Casual Error Handling:** Error messages are usually generic or a bit snarky ("Come on, you need to enter a NUMBER. Not letters.").
3.  **Variable Names:** Sometimes the variables change names for no good reason (`tasks_data` becomes `all_my_tasks`). Consistency is overrated, right?

Enjoy crushing your study list!# README
