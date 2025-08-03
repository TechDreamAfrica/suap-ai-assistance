import flet as ft
import random
import math

class FractionsDecimalsModule:
    def __init__(self, page):
        self.page = page
        self.current_quiz_questions = []
        self.current_question_index = 0
        self.user_answers = []
        self.current_quiz_level = "basic"
        self.quiz_score = 0
        self.quiz_question_index = 0
        
        # Initialize learning content
        self.learning_content = {
            "fractions_basics": {
                "title": "Understanding Fractions",
                "content": [
                    "A fraction represents a part of a whole, written as a/b.",
                    "The numerator (top number) shows how many parts we have.",
                    "The denominator (bottom number) shows total parts in the whole.",
                    "Example: 3/4 means 3 parts out of 4 total parts.",
                    "Proper fractions: numerator < denominator (3/4).",
                    "Improper fractions: numerator ≥ denominator (5/3)."
                ]
            },
            "decimal_basics": {
                "title": "Understanding Decimals",
                "content": [
                    "Decimals are another way to represent parts of a whole.",
                    "The decimal point separates whole numbers from fractional parts.",
                    "Place values: tenths (0.1), hundredths (0.01), thousandths (0.001).",
                    "Example: 0.75 = 7 tenths + 5 hundredths = 75/100.",
                    "Decimals make calculations and comparisons easier.",
                    "Every fraction can be written as a decimal."
                ]
            },
            "conversions": {
                "title": "Converting Between Fractions and Decimals",
                "content": [
                    "To convert fraction to decimal: divide numerator by denominator.",
                    "Example: 3/4 = 3 ÷ 4 = 0.75.",
                    "To convert decimal to fraction: use place value.",
                    "Example: 0.25 = 25/100 = 1/4 (simplified).",
                    "Some fractions create repeating decimals (1/3 = 0.333...).",
                    "Always simplify fractions to lowest terms."
                ]
            },
            "operations": {
                "title": "Operations with Fractions and Decimals",
                "content": [
                    "Adding fractions: find common denominator, add numerators.",
                    "Example: 1/4 + 1/3 = 3/12 + 4/12 = 7/12.",
                    "Multiplying fractions: multiply numerators and denominators.",
                    "Example: 2/3 × 3/4 = 6/12 = 1/2.",
                    "Decimal operations follow same rules as whole numbers.",
                    "Keep track of decimal point placement in calculations."
                ]
            }
        }
        
    def show_quizzes(self):
        """Show the quiz selection page"""
        view = ft.View(
            "/fractions_decimals/quizzes",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.show_main_page(self.page)),
                    title=ft.Text("Fractions & Decimals Quizzes"),
                    bgcolor=ft.Colors.GREEN_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("📝 Choose Your Quiz Level", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_900),
                        ft.Text("Select the difficulty level that matches your skill", size=16, color=ft.Colors.GREEN_700),
                        
                        ft.ResponsiveRow([
                            ft.Container(
                                ft.Card(
                                    ft.Container(
                                        ft.Column([
                                            ft.Icon(ft.Icons.STAR_OUTLINE, size=40, color=ft.Colors.GREEN_600),
                                            ft.Text("Basic Level", size=18, weight=ft.FontWeight.BOLD),
                                            ft.Text("Basic Fractions & Decimals\nSimple Conversions", text_align=ft.TextAlign.CENTER),
                                            ft.Text("10 Questions", size=12, color=ft.Colors.GREEN_600),
                                            ft.ElevatedButton(
                                                "Start Basic Quiz",
                                                on_click=lambda e: self.start_quiz("basic"),
                                                style=ft.ButtonStyle(bgcolor=ft.Colors.GREEN_700, color=ft.Colors.WHITE)
                                            )
                                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
                                        padding=20
                                    )
                                ),
                                col={'xs': 12, 'sm': 6, 'md': 4}
                            ),
                            ft.Container(
                                ft.Card(
                                    ft.Container(
                                        ft.Column([
                                            ft.Icon(ft.Icons.STAR_HALF, size=40, color=ft.Colors.ORANGE_600),
                                            ft.Text("Intermediate", size=18, weight=ft.FontWeight.BOLD),
                                            ft.Text("Operations with Decimals\nFraction Arithmetic", text_align=ft.TextAlign.CENTER),
                                            ft.Text("10 Questions", size=12, color=ft.Colors.ORANGE_600),
                                            ft.ElevatedButton(
                                                "Start Intermediate",
                                                on_click=lambda e: self.start_quiz("intermediate"),
                                                style=ft.ButtonStyle(bgcolor=ft.Colors.ORANGE_700, color=ft.Colors.WHITE)
                                            )
                                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
                                        padding=20
                                    )
                                ),
                                col={'xs': 12, 'sm': 6, 'md': 4}
                            ),
                            ft.Container(
                                ft.Card(
                                    ft.Container(
                                        ft.Column([
                                            ft.Icon(ft.Icons.STAR, size=40, color=ft.Colors.PURPLE_600),
                                            ft.Text("Advanced", size=18, weight=ft.FontWeight.BOLD),
                                            ft.Text("Complex Operations\nWord Problems", text_align=ft.TextAlign.CENTER),
                                            ft.Text("10 Questions", size=12, color=ft.Colors.PURPLE_600),
                                            ft.ElevatedButton(
                                                "Start Advanced",
                                                on_click=lambda e: self.start_quiz("advanced"),
                                                style=ft.ButtonStyle(bgcolor=ft.Colors.PURPLE_700, color=ft.Colors.WHITE)
                                            )
                                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
                                        padding=20
                                    )
                                ),
                                col={'xs': 12, 'sm': 6, 'md': 4}
                            ),
                        ], spacing=20, run_spacing=20)
                    ], spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()
        
    def start_quiz(self, level):
        """Start a quiz at the specified level"""
        self.current_quiz_level = level
        self.quiz_score = 0
        self.quiz_question_index = 0
        
        # Shuffle questions for variety
        questions = self.quiz_questions[level].copy()
        random.shuffle(questions)
        self.current_quiz_questions = questions[:min(len(questions), 10)]
        
        self.show_quiz_question()
        
    def show_quiz_question(self):
        """Display the current quiz question"""
        if self.quiz_question_index >= len(self.current_quiz_questions):
            self.show_quiz_results()
            return
            
        question_data = self.current_quiz_questions[self.quiz_question_index]
        options = question_data["options"].copy()
        correct_answer = options[question_data["correct"]]
        
        # Shuffle options
        random.shuffle(options)
        new_correct_index = options.index(correct_answer)
        
        # Store shuffled state
        self.current_correct_index = new_correct_index
        self.current_shuffled_options = options.copy()
        
        view = ft.View(
            f"/fractions_decimals/quiz/{self.current_quiz_level}",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.show_quizzes()),
                    title=ft.Text(f"{self.current_quiz_level.title()} Quiz"),
                    bgcolor=ft.Colors.GREEN_700
                ),
                self.build_quiz_question_view(question_data, options)
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()
        
    def build_quiz_question_view(self, question_data, options):
        """Build the UI for a quiz question"""
        option_buttons = []
        for i, option in enumerate(options):
            option_buttons.append(
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Text(f"{chr(65+i)}. {option}", size=16),
                        on_click=lambda e, idx=i: self.answer_question(idx),
                        style=ft.ButtonStyle(
                            padding=ft.Padding(20, 15, 20, 15),
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        width=None,
                        expand=True
                    ),
                    col={'xs': 12, 'sm': 6},
                    margin=5
                )
            )
            
        return ft.Container(
            ft.Column([
                ft.Container(
                    ft.Column([
                        ft.Text(f"Question {self.quiz_question_index + 1} of {len(self.current_quiz_questions)}", 
                                size=16, color=ft.Colors.GREEN_700),
                        ft.ProgressBar(
                            value=(self.quiz_question_index) / len(self.current_quiz_questions),
                            color=ft.Colors.GREEN_700,
                            bgcolor=ft.Colors.GREEN_100
                        )
                    ], spacing=10),
                    padding=10,
                    bgcolor=ft.Colors.GREEN_50,
                    border_radius=10
                ),
                
                ft.Container(
                    ft.Column([
                        ft.Text("❓ Question:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
                        ft.Text(question_data["question"], size=18, weight=ft.FontWeight.BOLD),
                    ], spacing=10),
                    padding=20,
                    bgcolor=ft.Colors.BLUE_50,
                    border_radius=10,
                    border=ft.border.all(2, ft.Colors.BLUE_200)
                ),
                
                ft.Text("Choose your answer:", size=16, weight=ft.FontWeight.BOLD),
                ft.ResponsiveRow(option_buttons, spacing=10, run_spacing=10),
                
                ft.Row([
                    ft.Container(
                        ft.Text(f"Current Score: {self.quiz_score}/{self.quiz_question_index}", 
                               size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
                        padding=10,
                        bgcolor=ft.Colors.GREEN_50,
                        border_radius=5,
                        expand=True
                    )
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
            ], spacing=20),
            padding=20,
            expand=True
        )
        
    def answer_question(self, selected_index):
        """Handle when a user selects an answer"""
        is_correct = selected_index == self.current_correct_index
        if is_correct:
            self.quiz_score += 1
            
        self.show_answer_feedback(self.current_quiz_questions[self.quiz_question_index], selected_index, is_correct)
        
    def show_answer_feedback(self, question_data, selected_index, is_correct):
        """Show feedback after answering a question"""
        feedback_color = ft.Colors.GREEN_700 if is_correct else ft.Colors.RED_700
        feedback_icon = ft.Icons.CHECK_CIRCLE if is_correct else ft.Icons.CANCEL
        feedback_text = "Correct!" if is_correct else "Incorrect"
        
        correct_answer = question_data["options"][question_data["correct"]]
        user_selected = self.current_shuffled_options[selected_index]
        
        dialog = ft.AlertDialog(
            title=ft.Text(feedback_text, color=feedback_color, size=24, weight=ft.FontWeight.BOLD),
            content=ft.Column([
                ft.Icon(feedback_icon, size=50, color=feedback_color),
                ft.Text(f"Your answer: {user_selected}", size=16),
                ft.Text(f"Correct answer: {correct_answer}", size=16),
                ft.Divider(),
                ft.Text("Explanation:", size=16, weight=ft.FontWeight.BOLD),
                ft.Text(question_data["explanation"], size=14)
            ], spacing=10, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            actions=[
                ft.TextButton(
                    "Next Question",
                    on_click=lambda e: self.next_question(e)
                )
            ]
        )
        
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()
        
    def next_question(self, e):
        """Move to the next question after showing feedback"""
        self.page.dialog.open = False
        self.page.update()
        
        self.quiz_question_index += 1
        if self.quiz_question_index < len(self.current_quiz_questions):
            self.show_quiz_question()
        else:
            self.show_quiz_results()
            
    def show_quiz_results(self):
        """Show the final quiz results"""
        score_percentage = (self.quiz_score / len(self.current_quiz_questions)) * 100
        
        view = ft.View(
            "/fractions_decimals/quiz/results",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.show_main_page(self.page)),
                    title=ft.Text("Quiz Results"),
                    bgcolor=ft.Colors.BLUE_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Icon(
                            ft.Icons.EMOJI_EVENTS_ROUNDED if score_percentage >= 70 else ft.Icons.STAR,
                            size=80,
                            color=ft.Colors.AMBER_500
                        ),
                        ft.Text(
                            "Quiz Complete!",
                            size=32,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.BLUE_900
                        ),
                        ft.Text(
                            f"Your Score: {self.quiz_score}/{len(self.current_quiz_questions)}",
                            size=24,
                            color=ft.Colors.BLUE_700
                        ),
                        ft.Text(
                            f"{score_percentage:.1f}%",
                            size=48,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.GREEN_700 if score_percentage >= 70 else ft.Colors.RED_700
                        ),
                        ft.Text(
                            "Great job!" if score_percentage >= 70 else "Keep practicing!",
                            size=20,
                            color=ft.Colors.GREY_800
                        ),
                        ft.ElevatedButton(
                            "Try Another Quiz",
                            on_click=lambda e: self.show_quizzes(),
                            style=ft.ButtonStyle(
                                bgcolor=ft.Colors.BLUE_700,
                                color=ft.Colors.WHITE
                            )
                        )
                    ], 
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20
                    ),
                    padding=20,
                    alignment=ft.alignment.center
                )
            ]
        )
        
        self.page.views.clear()
        self.page.views.append(view)
        self.page.update()
        
        self.quiz_questions = {
            "basic": [
                {"question": "Convert 0.5 to a fraction", "options": ["1/2", "2/4", "5/10", "All of these"], "correct": 3, "explanation": "0.5 = 1/2 = 2/4 = 5/10. These are all equivalent fractions."},
                {"question": "What is 3/4 as a decimal?", "options": ["0.75", "0.70", "0.80", "0.65"], "correct": 0, "explanation": "3/4 = 0.75 because 3 ÷ 4 = 0.75"},
                {"question": "Which fraction is equal to 0.25?", "options": ["1/4", "2/5", "1/5", "3/10"], "correct": 0, "explanation": "0.25 = 1/4 because 25/100 simplifies to 1/4"}
            ],
            "intermediate": [
                {"question": "What is 2.5 + 1.75?", "options": ["4.25", "3.25", "4.00", "3.75"], "correct": 1, "explanation": "2.5 + 1.75 = 3.25. Line up decimal points and add."},
                {"question": "Convert 7/8 to a decimal", "options": ["0.875", "0.750", "0.800", "0.785"], "correct": 0, "explanation": "7/8 = 0.875 because 7 ÷ 8 = 0.875"},
                {"question": "What is 5/6 - 1/3?", "options": ["1/2", "2/3", "1/3", "1/6"], "correct": 0, "explanation": "5/6 - 1/3 = (5/6) - (2/6) = 3/6 = 1/2"}
            ],
            "advanced": [
                {"question": "What is 2.5 × 0.4?", "options": ["1.0", "0.8", "1.2", "1.5"], "correct": 0, "explanation": "2.5 × 0.4 = 1.0. Convert to 25/10 × 4/10 = 100/100 = 1"},
                {"question": "Convert 0.333... to a fraction", "options": ["1/3", "3/10", "1/4", "3/9"], "correct": 0, "explanation": "0.333... (repeating) = 1/3"},
                {"question": "What is 7/8 ÷ 1/4?", "options": ["3.5", "2.5", "4.5", "3.0"], "correct": 0, "explanation": "7/8 ÷ 1/4 = 7/8 × 4/1 = 28/8 = 3.5"}
            ]
        }
        self.quiz_score = 0
        self.quiz_difficulty = "basic"
        self.practice_test_questions = []
        self.practice_test_score = 0
        self.practice_test_answers = []
        
    def show_main_page(self, page=None):
        """Show the main fractions and decimals page
        Args:
            page: Optional page reference. If not provided, uses self.page
        """
        if page is None:
            page = self.page
            
        # Set up the main page view
        view = ft.View(
            "/fractions_decimals",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: page.go("/")),
                    title=ft.Text("Fractions & Decimals"),
                    bgcolor=ft.Colors.BLUE_700,
                    center_title=True
                ),
                self.create_main_view()
            ]
        )
        
        # Clear existing views and show main view
        page.views.clear()
        page.views.append(view)
        page.update()

    # Learning content is handled by show_learning_content(self, page) method below
        
        self.page.views.append(view)
        self.page.update()

    def create_topic_card(self, title, description, icon, color):
        return ft.Container(
            ft.Card(
                ft.Container(
                    ft.Column([
                        ft.Icon(icon, size=40, color=color[700]),
                        ft.Text(title, size=18, weight=ft.FontWeight.BOLD),
                        ft.Text(description, 
                               size=14, 
                               text_align=ft.TextAlign.CENTER,
                               color=ft.colors.GREY_700),
                        ft.ElevatedButton(
                            "Start Learning",
                            on_click=lambda e, t=title: self.show_topic_content(t),
                            style=ft.ButtonStyle(
                                bgcolor=color[700],
                                color=ft.colors.WHITE
                            )
                        )
                    ], 
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10),
                    padding=20
                )
            ),
            col={'xs': 12, 'sm': 6, 'md': 4}
        )
        
    def create_main_view(self):
        return ft.Container(
            ft.Column([
                ft.Text("🧮 Fractions & Decimals", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900, text_align=ft.TextAlign.CENTER),
                ft.Text("Master fractions, decimals, and their operations", size=16, color=ft.Colors.BLUE_700, text_align=ft.TextAlign.CENTER),
                ft.Divider(height=30),
                
                # Navigation buttons
                ft.ResponsiveRow([
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.QUIZ_OUTLINED, size=30, color=ft.Colors.GREEN_700),
                                ft.Text("Practice Quiz", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_quizzes(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.GREEN_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.SCHOOL_OUTLINED, size=30, color=ft.Colors.PURPLE_700),
                                ft.Text("Learn Topics", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_learning_content(self.page),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.PURPLE_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.FITNESS_CENTER, size=30, color=ft.Colors.ORANGE_700),
                                ft.Text("Practice Test", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_practice_test(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.ORANGE_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.CALCULATE_OUTLINED, size=30, color=ft.Colors.BLUE_700),
                                ft.Text("Calculator", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_calculator(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.BLUE_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                ], spacing=10, run_spacing=10),
                
                ft.Divider(height=20),
                
                # Learning overview
                ft.Container(
                    ft.Column([
                        ft.Text("📚 What You'll Learn", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800),
                        ft.Text("Master fractions and decimals with comprehensive lessons", size=14),
                        
                        ft.Text("🎯 Learning Topics:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
                        ft.Column([
                            ft.Text("📊 Understanding Fractions: Parts of a whole", size=14),
                            ft.Text("🔢 Converting Between Fractions & Decimals", size=14),
                            ft.Text("➕ Adding & Subtracting Fractions", size=14),
                            ft.Text("✖️ Multiplying Fractions", size=14),
                            ft.Text("➗ Dividing Fractions", size=14),
                            ft.Text("💯 Working with Decimals", size=14),
                            ft.Text("📝 Real-world Applications", size=14),
                        ], spacing=5),
                        
                        # Quick stats
                        ft.ResponsiveRow([
                            ft.Container(
                                ft.Column([
                                    ft.Icon(ft.Icons.QUIZ, size=25, color=ft.Colors.BLUE_700),
                                    ft.Text("40+", size=16, weight=ft.FontWeight.BOLD),
                                    ft.Text("Practice Questions", size=12)
                                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                                bgcolor=ft.Colors.BLUE_50,
                                border_radius=10,
                                padding=10,
                                col={'xs': 6, 'sm': 3}
                            ),
                            ft.Container(
                                ft.Column([
                                    ft.Icon(ft.Icons.SCHOOL, size=25, color=ft.Colors.GREEN_700),
                                    ft.Text("7", size=16, weight=ft.FontWeight.BOLD),
                                    ft.Text("Core Topics", size=12)
                                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                                bgcolor=ft.Colors.GREEN_50,
                                border_radius=10,
                                padding=10,
                                col={'xs': 6, 'sm': 3}
                            ),
                            ft.Container(
                                ft.Column([
                                    ft.Icon(ft.Icons.SPEED, size=25, color=ft.Colors.PURPLE_700),
                                    ft.Text("3", size=16, weight=ft.FontWeight.BOLD),
                                    ft.Text("Difficulty Levels", size=12)
                                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                                bgcolor=ft.Colors.PURPLE_50,
                                border_radius=10,
                                padding=10,
                                col={'xs': 6, 'sm': 3}
                            ),
                            ft.Container(
                                ft.Column([
                                    ft.Icon(ft.Icons.CALCULATE, size=25, color=ft.Colors.ORANGE_700),
                                    ft.Text("Built-in", size=16, weight=ft.FontWeight.BOLD),
                                    ft.Text("Calculator", size=12)
                                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                                bgcolor=ft.Colors.ORANGE_50,
                                border_radius=10,
                                padding=10,
                                col={'xs': 6, 'sm': 3}
                            ),
                        ], spacing=10, run_spacing=10)
                    ], spacing=15),
                    bgcolor=ft.Colors.BLUE_50,
                    border_radius=10,
                    padding=15,
                    border=ft.border.all(2, ft.Colors.BLUE_200)
                )
            ], spacing=20),
            padding=20,
            expand=True
        )

        # Learning content data
        self.learning_content = {
            "fractions_basics": {
                "title": "Understanding Fractions",
                "content": [
                    "A fraction represents a part of a whole, written as a/b.",
                    "The numerator (top number) shows how many parts we have.",
                    "The denominator (bottom number) shows total parts in the whole.",
                    "Example: 3/4 means 3 parts out of 4 total parts.",
                    "Proper fractions: numerator < denominator (3/4).",
                    "Improper fractions: numerator ≥ denominator (5/3)."
                ]
            },
            "decimal_basics": {
                "title": "Understanding Decimals",
                "content": [
                    "Decimals are another way to represent parts of a whole.",
                    "The decimal point separates whole numbers from fractional parts.",
                    "Place values: tenths (0.1), hundredths (0.01), thousandths (0.001).",
                    "Example: 0.75 = 7 tenths + 5 hundredths = 75/100.",
                    "Decimals make calculations and comparisons easier.",
                    "Every fraction can be written as a decimal."
                ]
            },
            "conversions": {
                "title": "Converting Between Fractions and Decimals",
                "content": [
                    "To convert fraction to decimal: divide numerator by denominator.",
                    "Example: 3/4 = 3 ÷ 4 = 0.75.",
                    "To convert decimal to fraction: use place value.",
                    "Example: 0.25 = 25/100 = 1/4 (simplified).",
                    "Some fractions create repeating decimals (1/3 = 0.333...).",
                    "Always simplify fractions to lowest terms."
                ]
            },
            "operations": {
                "title": "Operations with Fractions and Decimals",
                "content": [
                    "Adding fractions: find common denominator, add numerators.",
                    "Example: 1/4 + 1/3 = 3/12 + 4/12 = 7/12.",
                    "Multiplying fractions: multiply numerators and denominators.",
                    "Example: 2/3 × 3/4 = 6/12 = 1/2.",
                    "Decimal operations follow same rules as whole numbers.",
                    "Keep track of decimal point placement in calculations."
                ]
            }
        }

    def show_page(self):
        """Main entry point for the module"""
        self.fractions_decimals_page(self.page)
        
    def fractions_decimals_page(self, page: ft.Page):
        """Main Fractions & Decimals page"""
        page.title = "Fractions & Decimals - Mathematics Learning"
        page.scroll = ft.ScrollMode.AUTO
        page.clean()

        def go_back_to_main(e):
            page.go("/maths")

        # Main content with tabs
        def on_tab_change(e):
            selected_index = e.control.selected_index
            if selected_index == 0:
                self.show_learning_content(page)
            elif selected_index == 1:
                self.show_practice_quiz(page)
            elif selected_index == 2:
                self.show_ai_help(page)
            elif selected_index == 3:
                self.show_examples(page)

        # AppBar
        page.appbar = ft.AppBar(
            leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/")),
            title=ft.Text("Fractions & Decimals", color=ft.Colors.WHITE),
            bgcolor=ft.Colors.PURPLE_700,
            center_title=True
        )

        # Main container with tabs
        main_content = ft.Container(
            ft.Column([
                ft.Text(
                    "🔢 Fractions & Decimals",
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.PURPLE_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Text(
                    "Master fractions, decimals, and their conversions",
                    size=18,
                    color=ft.Colors.PURPLE_700,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Divider(height=20),
                
                ft.Tabs(
                    selected_index=0,
                    on_change=on_tab_change,
                    tabs=[
                        ft.Tab(text="📚 Learn", icon=ft.Icons.SCHOOL),
                        ft.Tab(text="📝 Quiz", icon=ft.Icons.QUIZ),
                        ft.Tab(text="🤖 AI Help", icon=ft.Icons.SMART_TOY),
                        ft.Tab(text="💡 Examples", icon=ft.Icons.LIGHTBULB)
                    ],
                    indicator_color=ft.Colors.PURPLE_700,
                    label_color=ft.Colors.PURPLE_900,
                    unselected_label_color=ft.Colors.PURPLE_400
                )
            ], spacing=20),
            padding=20,
            expand=True
        )
        
        page.add(main_content)
        # Show learning content by default
        self.show_learning_content(page)

    # Navigation helper methods
    def show_main_page(self, page=None):
        """Show the main fractions & decimals page"""
        if page is None:
            page = self.page
            
        # Set up the main page view
        view = ft.View(
            "/fractions_decimals",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: page.go("/")),
                    title=ft.Text("Fractions & Decimals"),
                    bgcolor=ft.Colors.BLUE_700,
                    center_title=True
                ),
                self.create_main_view()
            ]
        )
        
        # Clear existing views and show main view
        page.views.clear()
        page.views.append(view)
        page.update()

    def show_learning_content(self, page: ft.Page):
        """Show learning content with topics"""
        page.clean()
        
        # AppBar
        page.appbar = ft.AppBar(
            leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.show_main_page(self.page)),
            title=ft.Text("Fractions & Decimals - Learn", color=ft.Colors.WHITE),
            bgcolor=ft.Colors.PURPLE_700,
            center_title=True
        )

        # Create learning content cards
        content_cards = []
        for topic_key, topic_data in self.learning_content.items():
            content_list = []
            for item in topic_data["content"]:
                content_list.append(ft.Text(f"• {item}", size=14, color=ft.Colors.PURPLE_800))
            
            card = ft.Card(
                content=ft.Container(
                    ft.Column([
                        ft.Text(topic_data["title"], size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_900),
                        ft.Divider(height=10),
                        ft.Column(content_list, spacing=8)
                    ], spacing=10),
                    padding=20
                ),
                elevation=5,
                margin=ft.margin.only(bottom=15)
            )
            content_cards.append(card)

        # Main content
        content = ft.Container(
            ft.Column([
                ft.Text(
                    "🔢 Fractions & Decimals Learning",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.PURPLE_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Text(
                    "Learn to work with fractions, decimals, and conversions",
                    size=16,
                    color=ft.Colors.PURPLE_700,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Divider(height=20),
                
                ft.Column(content_cards, spacing=10, scroll=ft.ScrollMode.AUTO)
            ], spacing=20),
            padding=20,
            expand=True
        )
        
        page.add(content)

    def generate_quiz_questions(self, difficulty="basic"):
        """Generate quiz questions based on difficulty"""
        questions = []
        
        if difficulty == "basic":
            # Basic fractions and decimals questions
            questions.extend([
                {
                    "question": "What fraction is equivalent to 0.5?",
                    "options": ["1/3", "1/2", "2/3", "3/4"],
                    "correct": 1,
                    "explanation": "0.5 = 5/10 = 1/2 when simplified"
                },
                {
                    "question": "What is 1/4 + 1/4?",
                    "options": ["1/8", "2/8", "1/2", "2/4"],
                    "correct": 2,
                    "explanation": "1/4 + 1/4 = 2/4 = 1/2"
                },
                {
                    "question": "Convert 3/4 to a decimal:",
                    "options": ["0.25", "0.5", "0.75", "0.34"],
                    "correct": 2,
                    "explanation": "3/4 = 3 ÷ 4 = 0.75"
                },
                {
                    "question": "Which fraction is larger: 2/3 or 3/4?",
                    "options": ["2/3", "3/4", "They are equal", "Cannot tell"],
                    "correct": 1,
                    "explanation": "Convert to decimals: 2/3 ≈ 0.67, 3/4 = 0.75, so 3/4 is larger"
                },
                {
                    "question": "What is 0.25 as a fraction in simplest form?",
                    "options": ["25/100", "1/4", "2/8", "50/200"],
                    "correct": 1,
                    "explanation": "0.25 = 25/100 = 1/4 when simplified"
                }
            ])
        
        elif difficulty == "intermediate":
            questions.extend([
                {
                    "question": "What is 2/3 × 3/4?",
                    "options": ["6/12", "1/2", "5/7", "2/4"],
                    "correct": 1,
                    "explanation": "2/3 × 3/4 = 6/12 = 1/2"
                },
                {
                    "question": "Convert 5/8 to a decimal:",
                    "options": ["0.625", "0.58", "0.85", "0.68"],
                    "correct": 0,
                    "explanation": "5/8 = 5 ÷ 8 = 0.625"
                },
                {
                    "question": "What is 3.75 as a mixed number?",
                    "options": ["3 1/4", "3 3/4", "3 1/2", "3 2/3"],
                    "correct": 1,
                    "explanation": "3.75 = 3 + 0.75 = 3 + 3/4 = 3 3/4"
                },
                {
                    "question": "Simplify: 1/2 + 1/3",
                    "options": ["2/5", "5/6", "3/6", "1/6"],
                    "correct": 1,
                    "explanation": "1/2 + 1/3 = 3/6 + 2/6 = 5/6"
                }
            ])
        
        elif difficulty == "advanced":
            questions.extend([
                {
                    "question": "What is 2 1/3 ÷ 1/2?",
                    "options": ["4 2/3", "1 1/6", "7/3", "14/3"],
                    "correct": 0,
                    "explanation": "2 1/3 = 7/3; 7/3 ÷ 1/2 = 7/3 × 2/1 = 14/3 = 4 2/3"
                },
                {
                    "question": "What fraction is equivalent to the repeating decimal 0.333...?",
                    "options": ["1/3", "3/9", "33/100", "1/30"],
                    "correct": 0,
                    "explanation": "0.333... = 1/3 (the repeating decimal 0.3̄ equals one-third)"
                },
                {
                    "question": "Solve: 3/4 - 2/5",
                    "options": ["1/1", "7/20", "1/20", "15/20"],
                    "correct": 1,
                    "explanation": "3/4 - 2/5 = 15/20 - 8/20 = 7/20"
                }
            ])
        
        return random.sample(questions, min(5, len(questions)))

    def show_practice_quiz(self, page: ft.Page):
        """Show practice quiz options"""
        page.clean()
        
        # AppBar
        page.appbar = ft.AppBar(
            leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.go_back_to_fractions_main(page)),
            title=ft.Text("Fractions & Decimals - Quiz", color=ft.Colors.WHITE),
            bgcolor=ft.Colors.PURPLE_700,
            center_title=True
        )

        # Quiz difficulty selection
        def start_quiz(e):
            difficulty = e.control.data
            self.quiz_difficulty = difficulty
            self.current_quiz_questions = self.generate_quiz_questions(difficulty)
            self.current_question_index = 0
            self.user_answers = []
            self.quiz_score = 0
            self.show_quiz_question(page)

        content = ft.Container(
            ft.Column([
                ft.Text(
                    "📝 Practice Quiz",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.PURPLE_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Text(
                    "Test your knowledge of fractions and decimals",
                    size=16,
                    color=ft.Colors.PURPLE_700,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Divider(height=30),
                
                ft.Text("Select Difficulty Level:", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_900),
                
                ft.Column([
                    ft.ElevatedButton(
                        "📚 Basic Level",
                        data="basic",
                        on_click=start_quiz,
                        style=ft.ButtonStyle(
                            padding=20,
                            bgcolor=ft.Colors.GREEN_100,
                            color=ft.Colors.GREEN_900,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        width=300
                    ),
                    ft.ElevatedButton(
                        "🔢 Intermediate Level",
                        data="intermediate",
                        on_click=start_quiz,
                        style=ft.ButtonStyle(
                            padding=20,
                            bgcolor=ft.Colors.ORANGE_100,
                            color=ft.Colors.ORANGE_900,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        width=300
                    ),
                    ft.ElevatedButton(
                        "🏆 Advanced Level",
                        data="advanced",
                        on_click=start_quiz,
                        style=ft.ButtonStyle(
                            padding=20,
                            bgcolor=ft.Colors.RED_100,
                            color=ft.Colors.RED_900,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        width=300
                    )
                ], spacing=15, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            ], spacing=20, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=20,
            expand=True
        )
        
        page.add(content)

    def update_difficulty(self, difficulty):
        """Update quiz difficulty"""
        self.quiz_difficulty = difficulty

    def show_quiz_question(self, page: ft.Page):
        """Show current quiz question"""
        page.clean()
        
        if self.current_question_index >= len(self.current_quiz_questions):
            self.show_quiz_results(page)
            return

        question = self.current_quiz_questions[self.current_question_index]
        
        # AppBar
        page.appbar = ft.AppBar(
            leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.show_practice_quiz(page)),
            title=ft.Text(f"Question {self.current_question_index + 1}/{len(self.current_quiz_questions)}", color=ft.Colors.WHITE),
            bgcolor=ft.Colors.PURPLE_700,
            center_title=True
        )

        # Question content
        def answer_question(e):
            selected_option = e.control.data
            self.answer_question(page, selected_option)

        option_buttons = []
        for i, option in enumerate(question["options"]):
            option_buttons.append(
                ft.ElevatedButton(
                    f"{chr(65 + i)}. {option}",
                    data=i,
                    on_click=answer_question,
                    style=ft.ButtonStyle(
                        padding=15,
                        bgcolor=ft.Colors.PURPLE_50,
                        color=ft.Colors.PURPLE_900,
                        shape=ft.RoundedRectangleBorder(radius=10)
                    ),
                    width=400
                )
            )

        content = ft.Container(
            ft.Column([
                ft.Text(
                    f"Question {self.current_question_index + 1}",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.PURPLE_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Container(
                    ft.Text(
                        question["question"],
                        size=18,
                        text_align=ft.TextAlign.CENTER,
                        color=ft.Colors.PURPLE_800
                    ),
                    bgcolor=ft.Colors.PURPLE_50,
                    border_radius=10,
                    padding=20,
                    margin=ft.margin.only(top=20, bottom=20)
                ),
                ft.Column(option_buttons, spacing=10, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            ], spacing=20, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=20,
            expand=True
        )
        
        page.add(content)

    def answer_question(self, page: ft.Page, selected_option):
        """Process answer and show feedback"""
        question = self.current_quiz_questions[self.current_question_index]
        is_correct = selected_option == question["correct"]
        
        self.user_answers.append(selected_option)
        if is_correct:
            self.quiz_score += 1
            
        self.show_answer_feedback(page, is_correct, question)

    def show_answer_feedback(self, page: ft.Page, is_correct, question):
        """Show feedback for the answer"""
        page.clean()
        
        # AppBar
        page.appbar = ft.AppBar(
            title=ft.Text("Answer Feedback", color=ft.Colors.WHITE),
            bgcolor=ft.Colors.PURPLE_700,
            center_title=True,
            automatically_imply_leading=False
        )

        def next_question(e):
            self.current_question_index += 1
            self.show_quiz_question(page)

        feedback_color = ft.Colors.GREEN_700 if is_correct else ft.Colors.RED_700
        feedback_icon = ft.Icons.CHECK_CIRCLE if is_correct else ft.Icons.CANCEL
        feedback_text = "Correct!" if is_correct else "Incorrect!"

        content = ft.Container(
            ft.Column([
                ft.Icon(feedback_icon, size=60, color=feedback_color),
                ft.Text(
                    feedback_text,
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=feedback_color,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("Explanation:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_900),
                        ft.Text(question["explanation"], size=14, color=ft.Colors.PURPLE_800)
                    ], spacing=10),
                    bgcolor=ft.Colors.PURPLE_50,
                    border_radius=10,
                    padding=20,
                    margin=ft.margin.only(top=20, bottom=20)
                ),
                ft.ElevatedButton(
                    "Next Question" if self.current_question_index < len(self.current_quiz_questions) - 1 else "View Results",
                    on_click=next_question,
                    style=ft.ButtonStyle(
                        padding=20,
                        bgcolor=ft.Colors.PURPLE_700,
                        color=ft.Colors.WHITE,
                        shape=ft.RoundedRectangleBorder(radius=10)
                    )
                )
            ], spacing=20, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=20,
            expand=True
        )
        
        page.add(content)

    def show_quiz_results(self, page: ft.Page):
        """Show quiz results and score"""
        page.clean()
        
        # AppBar
        page.appbar = ft.AppBar(
            title=ft.Text("Quiz Results", color=ft.Colors.WHITE),
            bgcolor=ft.Colors.PURPLE_700,
            center_title=True,
            automatically_imply_leading=False
        )

        percentage = (self.quiz_score / len(self.current_quiz_questions)) * 100
        
        def retake_quiz(e):
            self.show_practice_quiz(page)

        def back_to_main(e):
            self.go_back_to_fractions_main(page)

        # Determine performance message
        if percentage >= 80:
            performance_msg = "Excellent work! 🎉"
            performance_color = ft.Colors.GREEN_700
        elif percentage >= 60:
            performance_msg = "Good job! 👍"
            performance_color = ft.Colors.PURPLE_700
        else:
            performance_msg = "Keep practicing! 💪"
            performance_color = ft.Colors.ORANGE_700

        content = ft.Container(
            ft.Column([
                ft.Text(
                    "Quiz Complete!",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.PURPLE_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Container(
                    ft.Column([
                        ft.Text(f"Your Score: {self.quiz_score}/{len(self.current_quiz_questions)}", size=24, weight=ft.FontWeight.BOLD),
                        ft.Text(f"Percentage: {percentage:.1f}%", size=20),
                        ft.Text(performance_msg, size=18, color=performance_color, weight=ft.FontWeight.BOLD)
                    ], spacing=10, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    bgcolor=ft.Colors.PURPLE_50,
                    border_radius=10,
                    padding=30,
                    margin=ft.margin.only(top=20, bottom=20)
                ),
                ft.Row([
                    ft.ElevatedButton(
                        "Retake Quiz",
                        on_click=retake_quiz,
                        style=ft.ButtonStyle(
                            padding=20,
                            bgcolor=ft.Colors.ORANGE_100,
                            color=ft.Colors.ORANGE_900,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        )
                    ),
                    ft.ElevatedButton(
                        "Back to Main",
                        on_click=back_to_main,
                        style=ft.ButtonStyle(
                            padding=20,
                            bgcolor=ft.Colors.PURPLE_100,
                            color=ft.Colors.PURPLE_900,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        )
                    )
                ], spacing=20, alignment=ft.MainAxisAlignment.CENTER)
            ], spacing=20, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=20,
            expand=True
        )
        
        page.add(content)

    def show_ai_help(self, page: ft.Page):
        """Show AI help for fractions and decimals"""
        page.clean()
        
        # AppBar
        page.appbar = ft.AppBar(
            leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.go_back_to_fractions_main(page)),
            title=ft.Text("Fractions & Decimals - AI Help", color=ft.Colors.WHITE),
            bgcolor=ft.Colors.PURPLE_700,
            center_title=True
        )

        # AI help topics
        def show_help_topic(e):
            topic = e.control.data
            self.show_specific_help(page, topic)

        help_topics = [
            ("fraction_basics", "🔢 Fraction Basics"),
            ("decimal_basics", "📏 Decimal Basics"),
            ("conversions", "🔄 Conversions"),
            ("adding_subtracting", "➕➖ Adding & Subtracting"),
            ("multiplying_dividing", "✖️➗ Multiplying & Dividing"),
            ("comparing", "⚖️ Comparing Fractions & Decimals")
        ]

        topic_buttons = []
        for topic_key, topic_title in help_topics:
            topic_buttons.append(
                ft.ElevatedButton(
                    topic_title,
                    data=topic_key,
                    on_click=show_help_topic,
                    style=ft.ButtonStyle(
                        padding=20,
                        bgcolor=ft.Colors.PURPLE_50,
                        color=ft.Colors.PURPLE_900,
                        shape=ft.RoundedRectangleBorder(radius=10)
                    ),
                    width=350
                )
            )

        content = ft.Container(
            ft.Column([
                ft.Text(
                    "🤖 AI Help - Fractions & Decimals",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.PURPLE_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Text(
                    "Get help with specific fractions and decimals topics",
                    size=16,
                    color=ft.Colors.PURPLE_700,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Divider(height=30),
                
                ft.Text("Choose a topic for detailed help:", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_900),
                
                ft.Column(topic_buttons, spacing=15, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            ], spacing=20, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=20,
            expand=True
        )
        
        page.add(content)

    def show_specific_help(self, page: ft.Page, topic_key):
        """Show specific help for a topic"""
        help_content = {
            "fraction_basics": {
                "title": "Fraction Basics",
                "content": [
                    "UNDERSTANDING FRACTIONS:",
                    "• Numerator = top number (parts we have)",
                    "• Denominator = bottom number (total parts)",
                    "• Example: 3/4 = 3 parts out of 4 total",
                    "",
                    "TYPES OF FRACTIONS:",
                    "• Proper: numerator < denominator (2/3)",
                    "• Improper: numerator ≥ denominator (5/3)",
                    "• Mixed number: whole + fraction (1 2/3)",
                    "",
                    "SIMPLIFYING FRACTIONS:",
                    "• Find the GCD of numerator and denominator",
                    "• Divide both by the GCD",
                    "• Example: 6/8 = 3/4 (divided by 2)"
                ]
            },
            "decimal_basics": {
                "title": "Decimal Basics",
                "content": [
                    "DECIMAL PLACE VALUES:",
                    "• Tenths place: 0.1 (one-tenth)",
                    "• Hundredths place: 0.01 (one-hundredth)",
                    "• Thousandths place: 0.001 (one-thousandth)",
                    "",
                    "READING DECIMALS:",
                    "• 0.5 = 'five tenths'",
                    "• 0.25 = 'twenty-five hundredths'",
                    "• 0.125 = 'one hundred twenty-five thousandths'",
                    "",
                    "COMPARING DECIMALS:",
                    "• Compare digit by digit from left to right",
                    "• 0.7 > 0.65 (7 tenths > 6 tenths)"
                ]
            },
            "conversions": {
                "title": "Converting Fractions & Decimals",
                "content": [
                    "FRACTION TO DECIMAL:",
                    "• Divide numerator by denominator",
                    "• 3/4 = 3 ÷ 4 = 0.75",
                    "• 1/3 = 1 ÷ 3 = 0.333... (repeating)",
                    "",
                    "DECIMAL TO FRACTION:",
                    "• Use place value to write fraction",
                    "• 0.25 = 25/100 = 1/4 (simplified)",
                    "• 0.5 = 5/10 = 1/2 (simplified)",
                    "",
                    "COMMON CONVERSIONS:",
                    "• 1/2 = 0.5, 1/4 = 0.25, 3/4 = 0.75",
                    "• 1/5 = 0.2, 1/10 = 0.1"
                ]
            },
            "adding_subtracting": {
                "title": "Adding & Subtracting",
                "content": [
                    "ADDING FRACTIONS:",
                    "• Same denominator: add numerators",
                    "• 1/4 + 2/4 = 3/4",
                    "• Different denominators: find common denominator",
                    "• 1/3 + 1/4 = 4/12 + 3/12 = 7/12",
                    "",
                    "SUBTRACTING FRACTIONS:",
                    "• Same denominator: subtract numerators",
                    "• 3/5 - 1/5 = 2/5",
                    "• Different denominators: find common denominator",
                    "",
                    "ADDING/SUBTRACTING DECIMALS:",
                    "• Line up decimal points",
                    "• Add/subtract as with whole numbers",
                    "• 2.5 + 1.25 = 3.75"
                ]
            },
            "multiplying_dividing": {
                "title": "Multiplying & Dividing",
                "content": [
                    "MULTIPLYING FRACTIONS:",
                    "• Multiply numerators together",
                    "• Multiply denominators together",
                    "• 2/3 × 3/4 = 6/12 = 1/2",
                    "",
                    "DIVIDING FRACTIONS:",
                    "• Multiply by the reciprocal (flip second fraction)",
                    "• 2/3 ÷ 1/4 = 2/3 × 4/1 = 8/3",
                    "",
                    "MULTIPLYING DECIMALS:",
                    "• Multiply as whole numbers",
                    "• Count decimal places in both numbers",
                    "• Place decimal point in answer",
                    "",
                    "DIVIDING DECIMALS:",
                    "• Move decimal point in divisor to make it whole",
                    "• Move decimal point same places in dividend"
                ]
            },
            "comparing": {
                "title": "Comparing Fractions & Decimals",
                "content": [
                    "COMPARING FRACTIONS:",
                    "• Same denominator: compare numerators",
                    "• Different denominators: find common denominator",
                    "• Cross multiply: a/b vs c/d → compare ad vs bc",
                    "",
                    "COMPARING DECIMALS:",
                    "• Compare digit by digit from left to right",
                    "• 0.7 > 0.65 (ignore trailing zeros)",
                    "",
                    "COMPARING FRACTIONS & DECIMALS:",
                    "• Convert to same form (both fractions or decimals)",
                    "• 1/2 = 0.5, so 1/2 = 0.5",
                    "• 3/4 = 0.75, so 3/4 > 0.7"
                ]
            }
        }

        topic_data = help_content.get(topic_key, {"title": "Topic", "content": ["Help content not available."]})
        
        page.clean()
        
        # AppBar
        page.appbar = ft.AppBar(
            leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.show_ai_help(page)),
            title=ft.Text(f"AI Help - {topic_data['title']}", color=ft.Colors.WHITE),
            bgcolor=ft.Colors.PURPLE_700,
            center_title=True
        )

        # Content
        content_items = []
        for item in topic_data["content"]:
            if item == "":
                content_items.append(ft.Divider(height=10))
            else:
                content_items.append(ft.Text(item, size=14, color=ft.Colors.PURPLE_800))

        content = ft.Container(
            ft.Column([
                ft.Text(
                    f"🤖 {topic_data['title']}",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.PURPLE_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Container(
                    ft.Column(content_items, spacing=8),
                    bgcolor=ft.Colors.PURPLE_50,
                    border_radius=10,
                    padding=20,
                    margin=ft.margin.only(top=20)
                )
            ], spacing=20),
            padding=20,
            expand=True
        )
        
        page.add(content)

    def show_examples(self, page: ft.Page):
        """Show worked examples"""
        page.clean()
        
        # AppBar
        page.appbar = ft.AppBar(
            leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.go_back_to_fractions_main(page)),
            title=ft.Text("Fractions & Decimals - Examples", color=ft.Colors.WHITE),
            bgcolor=ft.Colors.PURPLE_700,
            center_title=True
        )

        # Example problems
        examples = [
            {
                "title": "Converting Fraction to Decimal",
                "problem": "Convert 3/8 to a decimal",
                "solution": [
                    "To convert fraction to decimal, divide numerator by denominator",
                    "3 ÷ 8 = 0.375",
                    "Therefore, 3/8 = 0.375"
                ]
            },
            {
                "title": "Converting Decimal to Fraction",
                "problem": "Convert 0.6 to a fraction in simplest form",
                "solution": [
                    "0.6 = 6/10 (six tenths)",
                    "Simplify by dividing both numerator and denominator by their GCD",
                    "GCD of 6 and 10 is 2",
                    "6 ÷ 2 = 3, 10 ÷ 2 = 5",
                    "Therefore, 0.6 = 3/5"
                ]
            },
            {
                "title": "Adding Fractions",
                "problem": "Calculate 1/3 + 1/4",
                "solution": [
                    "Find common denominator: LCM of 3 and 4 is 12",
                    "Convert fractions: 1/3 = 4/12, 1/4 = 3/12",
                    "Add numerators: 4/12 + 3/12 = 7/12",
                    "Therefore, 1/3 + 1/4 = 7/12"
                ]
            },
            {
                "title": "Multiplying Fractions",
                "problem": "Calculate 2/3 × 4/5",
                "solution": [
                    "Multiply numerators: 2 × 4 = 8",
                    "Multiply denominators: 3 × 5 = 15",
                    "Result: 8/15",
                    "Check if it can be simplified (GCD of 8 and 15 is 1)",
                    "Therefore, 2/3 × 4/5 = 8/15"
                ]
            }
        ]

        example_cards = []
        for example in examples:
            solution_items = []
            for step in example["solution"]:
                solution_items.append(ft.Text(f"• {step}", size=13, color=ft.Colors.PURPLE_800))
            
            card = ft.Card(
                content=ft.Container(
                    ft.Column([
                        ft.Text(example["title"], size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_900),
                        ft.Text("Problem:", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_800),
                        ft.Text(example["problem"], size=14, color=ft.Colors.PURPLE_700),
                        ft.Text("Solution:", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_800),
                        ft.Column(solution_items, spacing=5)
                    ], spacing=10),
                    padding=15
                ),
                elevation=3,
                margin=ft.margin.only(bottom=15)
            )
            example_cards.append(card)

        content = ft.Container(
            ft.Column([
                ft.Text(
                    "💡 Worked Examples",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.PURPLE_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Text(
                    "Step-by-step solutions to common fractions and decimals problems",
                    size=16,
                    color=ft.Colors.PURPLE_700,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Divider(height=20),
                
                ft.Column(example_cards, spacing=10, scroll=ft.ScrollMode.AUTO)
            ], spacing=20),
            padding=20,
            expand=True
        )
        
        page.add(content)

def show_examples(page):
    """Show examples"""
    page.snack_bar = ft.SnackBar(
        content=ft.Text("Examples section coming soon! Explore worked examples and detailed explanations."),
        bgcolor=ft.Colors.ORANGE_100
    )
    page.snack_bar.open = True
    page.update()

def fractions_decimals_page(page: ft.Page):
    """Main entry point for Fractions and Decimals module"""
    module = FractionsDecimalsModule(page)
    module.show_main_page(page)
