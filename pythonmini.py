import tkinter as tk
import random


# ============================================================
# QUIZ DATA
# ============================================================

QUIZ_DATA = {
    "Python": [
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["function", "def", "define", "fun"],
            "answer": "def"
        },
        {
            "question": "Which data type stores multiple values in an ordered collection?",
            "options": ["Integer", "List", "Boolean", "Float"],
            "answer": "List"
        },
        {
            "question": "Which symbol starts a single-line comment?",
            "options": ["//", "#", "/*", "--"],
            "answer": "#"
        },
        {
            "question": "Which function displays output in Python?",
            "options": ["show()", "display()", "print()", "output()"],
            "answer": "print()"
        },
        {
            "question": "Which keyword is used to create a class?",
            "options": ["object", "class", "struct", "create"],
            "answer": "class"
        },
        {
            "question": "Which method adds an item to the end of a list?",
            "options": ["add()", "insert()", "append()", "push()"],
            "answer": "append()"
        },
        {
            "question": "Which operator is used for exponentiation?",
            "options": ["^", "//", "**", "%%"],
            "answer": "**"
        },
        {
            "question": "Which function returns the length of a list?",
            "options": ["size()", "count()", "length()", "len()"],
            "answer": "len()"
        }
    ],

    "Programming": [
        {
            "question": "What does CPU stand for?",
            "options": [
                "Central Processing Unit",
                "Computer Personal Unit",
                "Central Program Utility",
                "Computer Processing Utility"
            ],
            "answer": "Central Processing Unit"
        },
        {
            "question": "Which language is mainly used for webpage structure?",
            "options": ["Python", "HTML", "SQL", "C++"],
            "answer": "HTML"
        },
        {
            "question": "Which language is commonly used to style webpages?",
            "options": ["CSS", "Python", "SQL", "Java"],
            "answer": "CSS"
        },
        {
            "question": "Which language is commonly used to query databases?",
            "options": ["HTML", "SQL", "CSS", "XML"],
            "answer": "SQL"
        },
        {
            "question": "What does RAM stand for?",
            "options": [
                "Random Access Memory",
                "Read Access Memory",
                "Rapid Access Module",
                "Random Application Memory"
            ],
            "answer": "Random Access Memory"
        },
        {
            "question": "What is a bug in programming?",
            "options": [
                "A programming error",
                "A computer screen",
                "A programming language",
                "A hardware component"
            ],
            "answer": "A programming error"
        }
    ],

    "General Knowledge": [
        {
            "question": "What is the capital of India?",
            "options": ["Mumbai", "New Delhi", "Kolkata", "Chennai"],
            "answer": "New Delhi"
        },
        {
            "question": "Which is the largest planet in our solar system?",
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "answer": "Jupiter"
        },
        {
            "question": "How many days are there in a week?",
            "options": ["5", "6", "7", "8"],
            "answer": "7"
        },
        {
            "question": "Which ocean is the largest?",
            "options": [
                "Atlantic Ocean",
                "Indian Ocean",
                "Arctic Ocean",
                "Pacific Ocean"
            ],
            "answer": "Pacific Ocean"
        },
        {
            "question": "How many continents are there?",
            "options": ["5", "6", "7", "8"],
            "answer": "7"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Venus", "Mars", "Mercury", "Neptune"],
            "answer": "Mars"
        }
    ]
}


# ============================================================
# COLORS
# ============================================================

BG = "#0F172A"
CARD = "#1E293B"
CARD_LIGHT = "#263449"

PRIMARY = "#6366F1"
PRIMARY_HOVER = "#818CF8"

WHITE = "#FFFFFF"
TEXT = "#E2E8F0"
MUTED = "#94A3B8"

GREEN = "#22C55E"
RED = "#EF4444"
YELLOW = "#F59E0B"

BORDER = "#334155"


# ============================================================
# QUIZ APPLICATION
# ============================================================

class QuizApplication:

    def __init__(self, root):

        self.root = root

        self.root.title("QuizMaster")
        self.root.geometry("1000x700")
        self.root.resizable(False, False)
        self.root.configure(bg=BG)

        # ---------------- VARIABLES ----------------

        self.category = None
        self.questions = []
        self.current = 0
        self.score = 0

        self.selected = tk.StringVar()

        self.time_left = 15
        self.timer_id = None

        self.answered = False

        # Start application
        self.show_home()

    # ========================================================
    # CLEAR WINDOW
    # ========================================================

    def clear(self):

        if self.timer_id:

            self.root.after_cancel(self.timer_id)
            self.timer_id = None

        for widget in self.root.winfo_children():
            widget.destroy()

    # ========================================================
    # HOME SCREEN
    # ========================================================

    def show_home(self):

        self.clear()

        # ---------------- HEADER ----------------

        header = tk.Frame(
            self.root,
            bg=BG
        )

        header.pack(
            fill="x",
            padx=60,
            pady=30
        )

        logo = tk.Label(
            header,
            text="◆ QUIZMASTER",
            font=("Segoe UI", 18, "bold"),
            bg=BG,
            fg=WHITE
        )

        logo.pack(side="left")

        tagline = tk.Label(
            header,
            text="Test • Learn • Improve",
            font=("Segoe UI", 11),
            bg=BG,
            fg=MUTED
        )

        tagline.pack(side="right")

        # ---------------- HERO ----------------

        hero = tk.Frame(
            self.root,
            bg=BG
        )

        hero.pack(
            pady=(20, 25)
        )

        title = tk.Label(
            hero,
            text="Challenge Your Mind",
            font=("Segoe UI", 34, "bold"),
            bg=BG,
            fg=WHITE
        )

        title.pack()

        subtitle = tk.Label(
            hero,
            text="Choose a category and see how much you know.",
            font=("Segoe UI", 13),
            bg=BG,
            fg=MUTED
        )

        subtitle.pack(pady=10)

        # ---------------- CATEGORY AREA ----------------

        category_frame = tk.Frame(
            self.root,
            bg=BG
        )

        category_frame.pack(
            pady=20
        )

        categories = [
            ("🐍", "Python", "Programming & Python"),
            ("💻", "Programming", "Coding fundamentals"),
            ("🌎", "General Knowledge", "World & everyday facts")
        ]

        for icon, name, description in categories:

            self.create_category_card(
                category_frame,
                icon,
                name,
                description
            )

        # ---------------- FOOTER ----------------

        footer = tk.Label(
            self.root,
            text="8 questions  •  15 seconds per question  •  Instant results",
            font=("Segoe UI", 10),
            bg=BG,
            fg=MUTED
        )

        footer.pack(
            pady=30
        )

    # ========================================================
    # CATEGORY CARD
    # ========================================================

    def create_category_card(
        self,
        parent,
        icon,
        name,
        description
    ):

        card = tk.Frame(
            parent,
            bg=CARD,
            width=270,
            height=190,
            highlightbackground=BORDER,
            highlightthickness=1
        )

        card.pack(
            side="left",
            padx=12
        )

        card.pack_propagate(False)

        icon_label = tk.Label(
            card,
            text=icon,
            font=("Segoe UI Emoji", 35),
            bg=CARD,
            fg=WHITE
        )

        icon_label.pack(
            pady=(20, 5)
        )

        name_label = tk.Label(
            card,
            text=name,
            font=("Segoe UI", 15, "bold"),
            bg=CARD,
            fg=WHITE
        )

        name_label.pack()

        description_label = tk.Label(
            card,
            text=description,
            font=("Segoe UI", 9),
            bg=CARD,
            fg=MUTED
        )

        description_label.pack(
            pady=5
        )

        start_button = tk.Button(
            card,
            text="START QUIZ  →",
            command=lambda: self.start_quiz(name),
            font=("Segoe UI", 10, "bold"),
            bg=PRIMARY,
            fg=WHITE,
            activebackground=PRIMARY_HOVER,
            activeforeground=WHITE,
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=7
        )

        start_button.pack(
            pady=8
        )

    # ========================================================
    # START QUIZ
    # ========================================================

    def start_quiz(self, category):

        self.category = category

        self.questions = QUIZ_DATA[category].copy()

        random.shuffle(self.questions)

        self.current = 0
        self.score = 0

        self.selected.set("")

        self.show_quiz()

    # ========================================================
    # QUIZ SCREEN
    # ========================================================

    def show_quiz(self):

        self.clear()

        # ---------------- TOP BAR ----------------

        top = tk.Frame(
            self.root,
            bg=BG
        )

        top.pack(
            fill="x",
            padx=60,
            pady=25
        )

        logo = tk.Label(
            top,
            text="QUIZMASTER",
            font=("Segoe UI", 16, "bold"),
            bg=BG,
            fg=WHITE
        )

        logo.pack(side="left")

        self.score_label = tk.Label(
            top,
            text="Score: 0",
            font=("Segoe UI", 12, "bold"),
            bg=BG,
            fg=YELLOW
        )

        self.score_label.pack(side="right")

        # ---------------- PROGRESS ----------------

        progress_info = tk.Frame(
            self.root,
            bg=BG
        )

        progress_info.pack(
            fill="x",
            padx=60
        )

        self.question_counter = tk.Label(
            progress_info,
            text="",
            font=("Segoe UI", 11, "bold"),
            bg=BG,
            fg=MUTED
        )

        self.question_counter.pack(
            side="left"
        )

        self.timer_label = tk.Label(
            progress_info,
            text="15",
            font=("Segoe UI", 15, "bold"),
            bg=BG,
            fg=GREEN
        )

        self.timer_label.pack(
            side="right"
        )

        # Progress bar background
        self.progress_bg = tk.Frame(
            self.root,
            bg="#334155",
            height=8
        )

        self.progress_bg.pack(
            fill="x",
            padx=60,
            pady=(8, 30)
        )

        self.progress_fill = tk.Frame(
            self.progress_bg,
            bg=PRIMARY,
            height=8
        )

        # ---------------- QUESTION CARD ----------------

        question_card = tk.Frame(
            self.root,
            bg=CARD,
            height=160
        )

        question_card.pack(
            fill="x",
            padx=60
        )

        question_card.pack_propagate(False)

        self.question_label = tk.Label(
            question_card,
            text="",
            font=("Segoe UI", 21, "bold"),
            bg=CARD,
            fg=WHITE,
            wraplength=780,
            justify="center"
        )

        self.question_label.pack(
            expand=True
        )

        # ---------------- OPTIONS ----------------

        self.options_frame = tk.Frame(
            self.root,
            bg=BG
        )

        self.options_frame.pack(
            fill="x",
            padx=60,
            pady=25
        )

        self.option_buttons = []

        for i in range(4):

            button = tk.Radiobutton(
                self.options_frame,
                text="",
                variable=self.selected,
                value="",
                command=self.option_selected,
                font=("Segoe UI", 12, "bold"),
                bg=CARD,
                fg=TEXT,
                activebackground=CARD_LIGHT,
                activeforeground=WHITE,
                selectcolor=PRIMARY,
                anchor="w",
                padx=20,
                pady=13,
                relief="flat",
                bd=0,
                cursor="hand2"
            )

            button.grid(
                row=i // 2,
                column=i % 2,
                sticky="ew",
                padx=6,
                pady=6
            )

            self.option_buttons.append(button)

        self.options_frame.columnconfigure(
            0,
            weight=1
        )

        self.options_frame.columnconfigure(
            1,
            weight=1
        )

        # ---------------- NEXT BUTTON ----------------

        self.next_button = tk.Button(
            self.root,
            text="SUBMIT ANSWER",
            command=self.submit_answer,
            font=("Segoe UI", 12, "bold"),
            bg=PRIMARY,
            fg=WHITE,
            activebackground=PRIMARY_HOVER,
            activeforeground=WHITE,
            relief="flat",
            cursor="hand2",
            padx=45,
            pady=12
        )

        self.next_button.pack(
            pady=5
        )

        self.load_question()

    # ========================================================
    # LOAD QUESTION
    # ========================================================

    def load_question(self):

        self.answered = False

        self.selected.set("")

        question = self.questions[self.current]

        self.question_counter.config(
            text=f"QUESTION {self.current + 1} / {len(self.questions)}"
        )

        self.score_label.config(
            text=f"Score: {self.score}"
        )

        self.question_label.config(
            text=question["question"]
        )

        # Progress
        percentage = (
            self.current / len(self.questions)
        )

        self.progress_fill.place(
            x=0,
            y=0,
            relwidth=percentage,
            relheight=1
        )

        # Options
        for i, option in enumerate(question["options"]):

            self.option_buttons[i].config(
                text=option,
                value=option,
                state="normal",
                bg=CARD,
                fg=TEXT
            )

        self.next_button.config(
            text="SUBMIT ANSWER",
            state="normal"
        )

        self.start_timer()

    # ========================================================
    # OPTION SELECTED
    # ========================================================

    def option_selected(self):

        if self.answered:
            return

        selected = self.selected.get()

        for button in self.option_buttons:

            if button.cget("value") == selected:

                button.config(
                    bg="#312E81"
                )

            else:

                button.config(
                    bg=CARD
                )

    # ========================================================
    # TIMER
    # ========================================================

    def start_timer(self):

        if self.timer_id:

            self.root.after_cancel(
                self.timer_id
            )

        self.time_left = 15

        self.update_timer()

    def update_timer(self):

        self.timer_label.config(
            text=f"⏱ {self.time_left}s"
        )

        if self.time_left <= 5:

            self.timer_label.config(
                fg=RED
            )

        else:

            self.timer_label.config(
                fg=GREEN
            )

        if self.time_left > 0 and not self.answered:

            self.time_left -= 1

            self.timer_id = self.root.after(
                1000,
                self.update_timer
            )

        elif self.time_left == 0:

            self.time_up()

    # ========================================================
    # TIME UP
    # ========================================================

    def time_up(self):

        if self.answered:
            return

        self.answered = True

        correct = self.questions[
            self.current
        ]["answer"]

        for button in self.option_buttons:

            button.config(
                state="disabled"
            )

            if button.cget("value") == correct:

                button.config(
                    bg="#14532D",
                    fg=WHITE
                )

        self.next_button.config(
            text="NEXT QUESTION  →"
        )

        self.next_button.config(
            command=self.next_question
        )

    # ========================================================
    # SUBMIT
    # ========================================================

    def submit_answer(self):

        if self.answered:
            return

        selected = self.selected.get()

        if not selected:

            self.show_message(
                "Please select an answer first."
            )

            return

        self.answered = True

        if self.timer_id:

            self.root.after_cancel(
                self.timer_id
            )

            self.timer_id = None

        correct = self.questions[
            self.current
        ]["answer"]

        if selected == correct:

            self.score += 1

            self.show_feedback(
                True,
                correct
            )

        else:

            self.show_feedback(
                False,
                correct
            )

        for button in self.option_buttons:

            button.config(
                state="disabled"
            )

            if button.cget("value") == correct:

                button.config(
                    bg="#14532D",
                    fg=WHITE
                )

            elif button.cget("value") == selected:

                button.config(
                    bg="#7F1D1D",
                    fg=WHITE
                )

        self.next_button.config(
            text="NEXT QUESTION  →",
            command=self.next_question
        )

    # ========================================================
    # FEEDBACK
    # ========================================================

    def show_feedback(self, correct, answer):

        if correct:

            self.next_button.config(
                bg=GREEN,
                text="CORRECT!  →"
            )

        else:

            self.next_button.config(
                bg=RED,
                text="WRONG!  →"
            )

    # ========================================================
    # NEXT QUESTION
    # ========================================================

    def next_question(self):

        self.current += 1

        if self.current >= len(self.questions):

            self.show_results()

        else:

            self.next_button.config(
                bg=PRIMARY,
                command=self.submit_answer
            )

            self.load_question()

    # ========================================================
    # MESSAGE
    # ========================================================

    def show_message(self, message):

        popup = tk.Toplevel(self.root)

        popup.title("QuizMaster")

        popup.geometry("400x180")

        popup.configure(
            bg=CARD
        )

        popup.resizable(
            False,
            False
        )

        tk.Label(
            popup,
            text="⚠",
            font=("Segoe UI", 30),
            bg=CARD,
            fg=YELLOW
        ).pack(
            pady=(20, 5)
        )

        tk.Label(
            popup,
            text=message,
            font=("Segoe UI", 12),
            bg=CARD,
            fg=WHITE
        ).pack(
            pady=5
        )

        tk.Button(
            popup,
            text="OK",
            command=popup.destroy,
            bg=PRIMARY,
            fg=WHITE,
            relief="flat",
            padx=25,
            pady=7,
            cursor="hand2"
        ).pack(
            pady=10
        )

    # ========================================================
    # RESULTS
    # ========================================================

    def show_results(self):

        self.clear()

        percentage = (
            self.score / len(self.questions)
        ) * 100

        # Main card
        card = tk.Frame(
            self.root,
            bg=CARD,
            width=650,
            height=520
        )

        card.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        card.pack_propagate(False)

        tk.Label(
            card,
            text="QUIZ COMPLETE",
            font=("Segoe UI", 28, "bold"),
            bg=CARD,
            fg=WHITE
        ).pack(
            pady=(55, 10)
        )

        tk.Label(
            card,
            text="Your final score",
            font=("Segoe UI", 12),
            bg=CARD,
            fg=MUTED
        ).pack()

        tk.Label(
            card,
            text=f"{self.score} / {len(self.questions)}",
            font=("Segoe UI", 55, "bold"),
            bg=CARD,
            fg=PRIMARY_HOVER
        ).pack(
            pady=5
        )

        tk.Label(
            card,
            text=f"{percentage:.0f}%",
            font=("Segoe UI", 22, "bold"),
            bg=CARD,
            fg=GREEN if percentage >= 50 else RED
        ).pack()

        if percentage >= 80:

            message = "Outstanding! You're a quiz master! 🏆"

        elif percentage >= 60:

            message = "Great job! Keep learning! 🎉"

        elif percentage >= 40:

            message = "Good effort! Keep practicing! 💪"

        else:

            message = "Don't give up. Try again! 📚"

        tk.Label(
            card,
            text=message,
            font=("Segoe UI", 13),
            bg=CARD,
            fg=MUTED
        ).pack(
            pady=15
        )

        # Play again
        tk.Button(
            card,
            text="🔄  PLAY AGAIN",
            command=lambda: self.start_quiz(self.category),
            font=("Segoe UI", 12, "bold"),
            bg=PRIMARY,
            fg=WHITE,
            activebackground=PRIMARY_HOVER,
            relief="flat",
            cursor="hand2",
            padx=35,
            pady=12
        ).pack(
            pady=7
        )

        # Home
        tk.Button(
            card,
            text="←  MAIN MENU",
            command=self.show_home,
            font=("Segoe UI", 11),
            bg=CARD_LIGHT,
            fg=TEXT,
            activebackground="#334155",
            relief="flat",
            cursor="hand2",
            padx=30,
            pady=10
        ).pack(
            pady=5
        )


# ============================================================
# RUN APPLICATION
# ============================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = QuizApplication(root)

    root.mainloop()
