import flet as ft
import random
import math

def get_fractions_ai_help(query, topic="fractions_decimals"):
    """AI help for Fractions and Decimals concepts"""
    try:
        responses = {
            "fraction": "A fraction represents part of a whole. The numerator (top) shows parts you have, denominator (bottom) shows total parts. Example: 3/4 means 3 parts out of 4 total parts.",
            "decimal": "Decimals show parts of a whole using place values. The decimal point separates whole numbers from fractional parts. 0.75 = 7 tenths + 5 hundredths.",
            "convert": "To convert fraction to decimal, divide numerator by denominator (3/4 = 3÷4 = 0.75). To convert decimal to fraction, use place value (0.25 = 25/100 = 1/4).",
            "add": "To add fractions: find common denominator, then add numerators. Example: 1/4 + 1/3 = 3/12 + 4/12 = 7/12.",
            "subtract": "To subtract fractions: find common denominator, then subtract numerators. Example: 3/4 - 1/2 = 3/4 - 2/4 = 1/4.",
            "multiply": "To multiply fractions: multiply numerators together and denominators together. Example: 2/3 × 3/4 = 6/12 = 1/2.",
            "divide": "To divide fractions: multiply by the reciprocal (flip the second fraction). Example: 1/2 ÷ 1/4 = 1/2 × 4/1 = 4/2 = 2.",
            "compare": "To compare fractions: convert to same denominator or to decimals. Example: 2/3 = 0.667, 3/4 = 0.75, so 3/4 > 2/3.",
            "simplify": "To simplify fractions: divide numerator and denominator by their greatest common divisor. Example: 6/8 = 3/4 (both divided by 2).",
        }
        
        query_lower = query.lower()
        for key, response in responses.items():
            if key in query_lower:
                return f"🤖 Fractions & Decimals Helper: {response}"
        
        return f"🤖 Fractions & Decimals Helper: I can help with fractions, decimals, converting between them, and operations (add, subtract, multiply, divide). Ask me about any specific topic!"
    except Exception:
        return f"🤖 Fractions & Decimals Helper: I'm here to help with fractions and decimals! Ask about specific operations or concepts."

class FractionsDecimalsModule:
    def __init__(self, page):
        self.page = page
        self.current_quiz_questions = []
        self.current_question_index = 0
        self.user_answers = []
        self.current_quiz_level = "basic"
        self.quiz_score = 0
        self.quiz_question_index = 0
        self.current_correct_index = 0
        self.current_shuffled_options = []
        
        # Initialize comprehensive quiz questions
        self.quiz_questions = {
            "basic": [
                {"question": "Convert 0.5 to a fraction", "options": ["1/2", "2/4", "5/10", "All of these"], "correct": 3, "explanation": "0.5 = 1/2 = 2/4 = 5/10. These are all equivalent fractions."},
                {"question": "What is 3/4 as a decimal?", "options": ["0.75", "0.70", "0.80", "0.65"], "correct": 0, "explanation": "3/4 = 0.75 because 3 ÷ 4 = 0.75"},
                {"question": "Which fraction is equal to 0.25?", "options": ["1/4", "2/5", "1/5", "3/10"], "correct": 0, "explanation": "0.25 = 1/4 because 25/100 simplifies to 1/4"},
                {"question": "What is 1/2 + 1/4?", "options": ["2/6", "3/4", "1/6", "2/4"], "correct": 1, "explanation": "1/2 + 1/4 = 2/4 + 1/4 = 3/4"},
                {"question": "Which is larger: 0.3 or 1/4?", "options": ["0.3", "1/4", "They are equal", "Cannot tell"], "correct": 0, "explanation": "0.3 = 3/10 = 0.3, and 1/4 = 0.25, so 0.3 > 1/4"},
                {"question": "What is 0.1 as a fraction?", "options": ["1/10", "1/100", "10/1", "1/1"], "correct": 0, "explanation": "0.1 = 1/10 (one tenth)"},
                {"question": "Simplify 4/8", "options": ["1/2", "2/4", "8/16", "4/8"], "correct": 0, "explanation": "4/8 = 1/2 when we divide both numerator and denominator by 4"},
                {"question": "What is 1/3 as a decimal (rounded to 2 places)?", "options": ["0.33", "0.30", "0.34", "0.333"], "correct": 0, "explanation": "1/3 = 0.333... which rounds to 0.33"},
                {"question": "What is 0.75 + 0.25?", "options": ["1.0", "0.10", "1.25", "0.50"], "correct": 0, "explanation": "0.75 + 0.25 = 1.0 (add the decimal parts: 75 + 25 = 100 hundredths = 1)"},
                {"question": "Which fraction equals 0.6?", "options": ["6/10", "3/5", "Both A and B", "None"], "correct": 2, "explanation": "0.6 = 6/10 = 3/5 (both are equivalent when simplified)"}
            ],
            "intermediate": [
                {"question": "What is 2.5 + 1.75?", "options": ["3.25", "4.25", "4.00", "3.75"], "correct": 0, "explanation": "2.5 + 1.75 = 4.25. Line up decimal points and add."},
                {"question": "Convert 7/8 to a decimal", "options": ["0.875", "0.750", "0.800", "0.785"], "correct": 0, "explanation": "7/8 = 0.875 because 7 ÷ 8 = 0.875"},
                {"question": "What is 5/6 - 1/3?", "options": ["1/2", "2/3", "1/3", "1/6"], "correct": 0, "explanation": "5/6 - 1/3 = 5/6 - 2/6 = 3/6 = 1/2"},
                {"question": "What is 2/3 × 3/4?", "options": ["6/12", "1/2", "5/7", "2/4"], "correct": 1, "explanation": "2/3 × 3/4 = 6/12 = 1/2"},
                {"question": "Convert 5/8 to a decimal:", "options": ["0.625", "0.58", "0.85", "0.68"], "correct": 0, "explanation": "5/8 = 5 ÷ 8 = 0.625"},
                {"question": "What is 3.75 as a mixed number?", "options": ["3 1/4", "3 3/4", "3 1/2", "3 2/3"], "correct": 1, "explanation": "3.75 = 3 + 0.75 = 3 + 3/4 = 3 3/4"},
                {"question": "Simplify: 1/2 + 1/3", "options": ["2/5", "5/6", "3/6", "1/6"], "correct": 1, "explanation": "1/2 + 1/3 = 3/6 + 2/6 = 5/6"},
                {"question": "What is 4.2 - 1.75?", "options": ["2.45", "2.55", "3.45", "2.35"], "correct": 0, "explanation": "4.2 - 1.75 = 4.20 - 1.75 = 2.45"},
                {"question": "Convert 1.25 to a fraction", "options": ["5/4", "25/100", "1 1/4", "All correct"], "correct": 3, "explanation": "1.25 = 125/100 = 5/4 = 1 1/4. All are correct representations."},
                {"question": "What is 3/5 ÷ 2/3?", "options": ["9/10", "6/15", "1/2", "2/5"], "correct": 0, "explanation": "3/5 ÷ 2/3 = 3/5 × 3/2 = 9/10"}
            ],
            "advanced": [
                {"question": "What is 2 1/3 ÷ 1/2?", "options": ["4 2/3", "1 1/6", "7/3", "14/3"], "correct": 0, "explanation": "2 1/3 = 7/3; 7/3 ÷ 1/2 = 7/3 × 2/1 = 14/3 = 4 2/3"},
                {"question": "What fraction is equivalent to the repeating decimal 0.333...?", "options": ["1/3", "3/9", "33/100", "1/30"], "correct": 0, "explanation": "0.333... = 1/3 (the repeating decimal 0.3̄ equals one-third)"},
                {"question": "Solve: 3/4 - 2/5", "options": ["1/1", "7/20", "1/20", "15/20"], "correct": 1, "explanation": "3/4 - 2/5 = 15/20 - 8/20 = 7/20"},
                {"question": "What is 2.5 × 0.4?", "options": ["1.0", "0.8", "1.2", "1.5"], "correct": 0, "explanation": "2.5 × 0.4 = 1.0. Convert to 25/10 × 4/10 = 100/100 = 1"},
                {"question": "Convert 0.375 to a fraction in simplest form", "options": ["3/8", "375/1000", "15/40", "6/16"], "correct": 0, "explanation": "0.375 = 375/1000 = 3/8 when simplified"},
                {"question": "What is (1/2 + 1/4) × 2/3?", "options": ["1/2", "3/8", "5/12", "1/3"], "correct": 0, "explanation": "(1/2 + 1/4) × 2/3 = 3/4 × 2/3 = 6/12 = 1/2"},
                {"question": "Express 0.8̄ (0.888...) as a fraction", "options": ["8/9", "4/5", "8/10", "80/100"], "correct": 0, "explanation": "0.8̄ = 8/9 (let x = 0.888..., then 10x = 8.888..., so 9x = 8, x = 8/9)"},
                {"question": "What is 1.6 ÷ 0.4?", "options": ["4", "0.4", "6.4", "16"], "correct": 0, "explanation": "1.6 ÷ 0.4 = 16 ÷ 4 = 4 (multiply both by 10 to remove decimals)"},
                {"question": "Find the decimal equivalent of 5/12", "options": ["0.417", "0.425", "0.512", "0.42"], "correct": 0, "explanation": "5/12 = 5 ÷ 12 = 0.41666... ≈ 0.417"},
                {"question": "What is 2 3/8 - 1 5/6?", "options": ["13/24", "7/12", "1/2", "11/24"], "correct": 0, "explanation": "2 3/8 - 1 5/6 = 19/8 - 11/6 = 57/24 - 44/24 = 13/24"}
            ]
        }
        
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

    def create_main_view(self):
        return ft.Container(
            ft.Column([
                ft.Text("🔢 Fractions & Decimals", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_900, text_align=ft.TextAlign.CENTER),
                ft.Text("Master fractions, decimals, and their operations", size=16, color=ft.Colors.PURPLE_700, text_align=ft.TextAlign.CENTER),
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
                            on_click=lambda e: self.show_learning_content(),
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
                        
                        ft.Text("🎯 Learning Topics:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_700),
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
                                    ft.Text("30+", size=16, weight=ft.FontWeight.BOLD),
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
                                    ft.Text("4", size=16, weight=ft.FontWeight.BOLD),
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
                    bgcolor=ft.Colors.PURPLE_50,
                    border_radius=10,
                    padding=15,
                    border=ft.border.all(2, ft.Colors.PURPLE_200)
                )
            ], spacing=20),
            padding=20,
            expand=True
        )

    def show_main_page(self, page=None):
        """Show the main fractions and decimals page"""
        if page is None:
            page = self.page
            
        view = ft.View(
            "/fractions_decimals",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: page.go("/")),
                    title=ft.Text("Fractions & Decimals"),
                    bgcolor=ft.Colors.PURPLE_700,
                    center_title=True
                ),
                self.create_main_view()
            ]
        )
        
        page.views.clear()
        page.views.append(view)
        page.update()

    def show_quizzes(self):
        """Show the quiz selection page"""
        def go_back(e):
            if len(self.page.views) > 1:
                self.page.views.pop()
                self.page.update()
            else:
                self.show_main_page()
        
        view = ft.View(
            "/fractions_decimals/quizzes",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=go_back),
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
        
        def go_back(e):
            if len(self.page.views) > 1:
                self.page.views.pop()
                self.page.update()
            else:
                self.show_quizzes()
        
        view = ft.View(
            f"/fractions_decimals/quiz/{self.current_quiz_level}",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=go_back),
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
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Row([
                                ft.Icon(ft.Icons.LIGHTBULB_OUTLINE, color=ft.Colors.AMBER_700),
                                ft.Text("Get Hint", size=14)
                            ], spacing=5),
                            on_click=lambda e: self.show_quiz_ai_help(question_data["question"]),
                            style=ft.ButtonStyle(
                                bgcolor=ft.Colors.AMBER_50,
                                color=ft.Colors.AMBER_900
                            )
                        ),
                        padding=5
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
        
        if score_percentage >= 90:
            grade = "A+"
            grade_color = ft.Colors.GREEN_700
            message = "Outstanding! You've mastered this level!"
        elif score_percentage >= 80:
            grade = "A"
            grade_color = ft.Colors.GREEN_600
            message = "Excellent work! You have strong understanding!"
        elif score_percentage >= 70:
            grade = "B"
            grade_color = ft.Colors.BLUE_600
            message = "Good job! Keep practicing to improve!"
        elif score_percentage >= 60:
            grade = "C"
            grade_color = ft.Colors.ORANGE_600
            message = "You're getting there! Review the topics!"
        else:
            grade = "F"
            grade_color = ft.Colors.RED_600
            message = "Keep practicing! Review the learning materials!"
        
        def go_back_from_results(e):
            if len(self.page.views) > 1:
                self.page.views.pop()
                self.page.update()
            else:
                self.show_quizzes()
        
        view = ft.View(
            "/fractions_decimals/quiz/results",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=go_back_from_results),
                    title=ft.Text("Quiz Results"),
                    bgcolor=grade_color
                ),
                ft.Container(
                    ft.Column([
                        ft.Container(
                            ft.Column([
                                ft.Icon(ft.Icons.EMOJI_EVENTS, size=60, color=grade_color),
                                ft.Text("Quiz Complete!", size=28, weight=ft.FontWeight.BOLD, color=grade_color),
                                ft.Text(f"Grade: {grade}", size=24, weight=ft.FontWeight.BOLD),
                                ft.Text(f"Score: {self.quiz_score}/{len(self.current_quiz_questions)} ({score_percentage:.1f}%)", size=20),
                                ft.Text(message, size=16, text_align=ft.TextAlign.CENTER, color=ft.Colors.GREY_700)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
                            padding=30,
                            bgcolor=ft.Colors.GREY_50,
                            border_radius=15
                        ),
                        
                        ft.ResponsiveRow([
                            ft.Container(
                                ft.ElevatedButton(
                                    "Try Again",
                                    on_click=lambda e: self.start_quiz(self.current_quiz_level),
                                    style=ft.ButtonStyle(bgcolor=ft.Colors.BLUE_700, color=ft.Colors.WHITE, padding=15)
                                ),
                                col={'xs': 12, 'sm': 6, 'md': 4}
                            ),
                            ft.Container(
                                ft.ElevatedButton(
                                    "Different Level",
                                    on_click=lambda e: self.show_quizzes(),
                                    style=ft.ButtonStyle(bgcolor=ft.Colors.GREEN_700, color=ft.Colors.WHITE, padding=15)
                                ),
                                col={'xs': 12, 'sm': 6, 'md': 4}
                            ),
                            ft.Container(
                                ft.ElevatedButton(
                                    "Back to Main",
                                    on_click=lambda e: self.show_main_page(),
                                    style=ft.ButtonStyle(bgcolor=ft.Colors.PURPLE_700, color=ft.Colors.WHITE, padding=15)
                                ),
                                col={'xs': 12, 'sm': 6, 'md': 4}
                            ),
                        ], spacing=10, run_spacing=10)
                    ], spacing=30),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def show_quiz_ai_help(self, question):
        """Show AI help dialog for quiz questions"""
        # Extract operation type from question to provide targeted help
        operation_type = ""
        if "convert" in question.lower():
            operation_type = "convert"
        elif "add" in question.lower() or "+" in question:
            operation_type = "add"
        elif "subtract" in question.lower() or "-" in question:
            operation_type = "subtract"
        elif "multiply" in question.lower() or "×" in question:
            operation_type = "multiply"
        elif "divide" in question.lower() or "÷" in question:
            operation_type = "divide"
        elif "compare" in question.lower() or "larger" in question.lower():
            operation_type = "compare"
        else:
            operation_type = "fraction"

        dialog = ft.AlertDialog(
            title=ft.Text("🤖 Fractions & Decimals Helper", size=20, weight=ft.FontWeight.BOLD),
            content=ft.Container(
                ft.Column([
                    ft.Container(
                        ft.Column([
                            ft.Text("📝 Question:", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_700),
                            ft.Text(question, size=14),
                        ], spacing=5),
                        bgcolor=ft.Colors.PURPLE_50,
                        padding=10,
                        border_radius=5
                    ),
                    
                    ft.Divider(),
                    
                    ft.Container(
                        ft.Column([
                            ft.Text("💡 Hint:", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
                            ft.Text(
                                get_fractions_ai_help(f"{operation_type} hint for {question}"),
                                size=14
                            ),
                        ], spacing=5),
                        bgcolor=ft.Colors.GREEN_50,
                        padding=10,
                        border_radius=5
                    ),
                ], spacing=10, scroll=ft.ScrollMode.AUTO),
                height=300,
                width=500,
            ),
            actions=[
                ft.TextButton(
                    "Close",
                    on_click=lambda e: self.close_dialog(),
                    style=ft.ButtonStyle(color=ft.Colors.PURPLE_700)
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()
    
    def close_dialog(self):
        """Close the current dialog"""
        if self.page.dialog:
            self.page.dialog.open = False
            self.page.update()

    def show_learning_content(self):
        """Show learning content with comprehensive topics"""
        def go_back(e):
            if len(self.page.views) > 1:
                self.page.views.pop()
                self.page.update()
            else:
                self.show_main_page()
        
        view = ft.View(
            "/fractions_decimals/learn",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=go_back),
                    title=ft.Text("Learn Fractions & Decimals"),
                    bgcolor=ft.Colors.PURPLE_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("📚 Fractions & Decimals Learning Guide", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_900),
                        ft.Text("Master fractions, decimals, and their operations", size=16, color=ft.Colors.PURPLE_700),
                        
                        # Fractions Section
                        ft.Container(
                            ft.Column([
                                ft.Text("📊 Understanding Fractions", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
                                ft.Text("Fractions represent parts of a whole.", size=14),
                                
                                ft.Text("🎯 Key Concepts:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_600),
                                ft.Column([
                                    ft.Text("• Numerator (top): parts we have", size=14),
                                    ft.Text("• Denominator (bottom): total parts", size=14),
                                    ft.Text("• Example: 3/4 = 3 parts out of 4 total", size=14),
                                    ft.Text("• Proper fractions: numerator < denominator", size=14),
                                    ft.Text("• Improper fractions: numerator ≥ denominator", size=14),
                                ], spacing=5),
                            ], spacing=10),
                            bgcolor=ft.Colors.GREEN_50,
                            padding=15,
                            border_radius=10,
                            border=ft.border.all(2, ft.Colors.GREEN_200)
                        ),
                        
                        # Decimals Section
                        ft.Container(
                            ft.Column([
                                ft.Text("💯 Understanding Decimals", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
                                ft.Text("Decimals are another way to show parts of a whole.", size=14),
                                
                                ft.Text("🎯 Place Values:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_600),
                                ft.Column([
                                    ft.Text("• Tenths: 0.1 (one tenth)", size=14),
                                    ft.Text("• Hundredths: 0.01 (one hundredth)", size=14),
                                    ft.Text("• Thousandths: 0.001 (one thousandth)", size=14),
                                    ft.Text("• Example: 0.75 = 7 tenths + 5 hundredths", size=14),
                                ], spacing=5),
                            ], spacing=10),
                            bgcolor=ft.Colors.BLUE_50,
                            padding=15,
                            border_radius=10,
                            border=ft.border.all(2, ft.Colors.BLUE_200)
                        ),
                        
                        # Conversions Section
                        ft.Container(
                            ft.Column([
                                ft.Text("🔄 Converting Between Fractions & Decimals", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_700),
                                
                                ft.Text("📝 Fraction to Decimal:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_600),
                                ft.Column([
                                    ft.Text("• Divide numerator by denominator", size=14),
                                    ft.Text("• Example: 3/4 = 3 ÷ 4 = 0.75", size=14),
                                ], spacing=5),
                                
                                ft.Text("📝 Decimal to Fraction:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_600),
                                ft.Column([
                                    ft.Text("• Use place value to write fraction", size=14),
                                    ft.Text("• Example: 0.25 = 25/100 = 1/4", size=14),
                                    ft.Text("• Always simplify to lowest terms", size=14),
                                ], spacing=5),
                            ], spacing=10),
                            bgcolor=ft.Colors.ORANGE_50,
                            padding=15,
                            border_radius=10,
                            border=ft.border.all(2, ft.Colors.ORANGE_200)
                        ),
                        
                        # Operations Section
                        ft.Container(
                            ft.Column([
                                ft.Text("✖️➗ Operations with Fractions", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_700),
                                
                                ft.Text("➕ Adding Fractions:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_600),
                                ft.Text("• Same denominator: add numerators (1/4 + 2/4 = 3/4)", size=14),
                                ft.Text("• Different denominators: find common denominator first", size=14),
                                
                                ft.Text("✖️ Multiplying Fractions:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_600),
                                ft.Text("• Multiply numerators and denominators (2/3 × 3/4 = 6/12 = 1/2)", size=14),
                                
                                ft.Text("➗ Dividing Fractions:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_600),
                                ft.Text("• Multiply by the reciprocal (1/2 ÷ 1/4 = 1/2 × 4/1 = 2)", size=14),
                            ], spacing=10),
                            bgcolor=ft.Colors.PURPLE_50,
                            padding=15,
                            border_radius=10,
                            border=ft.border.all(2, ft.Colors.PURPLE_200)
                        ),
                    ], spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def show_practice_test(self):
        """Show comprehensive practice test"""
        def go_back(e):
            if len(self.page.views) > 1:
                self.page.views.pop()
                self.page.update()
            else:
                self.show_main_page()
        
        # Mix questions from all levels for comprehensive test
        all_questions = []
        for level in self.quiz_questions:
            all_questions.extend(self.quiz_questions[level][:5])  # 5 from each level
        
        random.shuffle(all_questions)
        self.current_quiz_questions = all_questions[:15]  # 15-question practice test
        self.current_quiz_level = "practice_test"
        self.quiz_score = 0
        self.quiz_question_index = 0
        
        view = ft.View(
            "/fractions_decimals/practice_test",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=go_back),
                    title=ft.Text("Practice Test"),
                    bgcolor=ft.Colors.ORANGE_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("🎯 Fractions & Decimals Practice Test", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_900),
                        ft.Text("A comprehensive test covering all fractions and decimals concepts", size=16, color=ft.Colors.ORANGE_700),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("📋 Test Information:", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_700),
                                ft.Text("• 15 questions covering all difficulty levels", size=14),
                                ft.Text("• Mix of basic, intermediate, and advanced problems", size=14),
                                ft.Text("• Fractions, decimals, and conversions", size=14),
                                ft.Text("• Operations: adding, subtracting, multiplying, dividing", size=14),
                                ft.Text("• Take your time and work carefully", size=14),
                                
                                ft.Text("🏆 Scoring:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_700),
                                ft.Text("• 90-100%: Excellent mastery", size=14),
                                ft.Text("• 80-89%: Good understanding", size=14),
                                ft.Text("• 70-79%: Needs some practice", size=14),
                                ft.Text("• Below 70%: Review fundamentals", size=14),
                            ], spacing=10),
                            padding=20,
                            bgcolor=ft.Colors.ORANGE_50,
                            border_radius=10,
                            border=ft.border.all(2, ft.Colors.ORANGE_200)
                        ),
                        
                        ft.ElevatedButton(
                            "Start Practice Test",
                            on_click=lambda e: self.show_quiz_question(),
                            style=ft.ButtonStyle(
                                bgcolor=ft.Colors.ORANGE_700,
                                color=ft.Colors.WHITE,
                                padding=ft.Padding(30, 15, 30, 15)
                            )
                        )
                    ], spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def show_calculator(self):
        """Show fractions and decimals calculator with proper grid layout"""
        def go_back(e):
            if len(self.page.views) > 1:
                self.page.views.pop()
                self.page.update()
            else:
                self.show_main_page()
        
        # Calculator state
        display = ft.TextField(
            value="0",
            text_align=ft.TextAlign.RIGHT,
            read_only=True,
            text_style=ft.TextStyle(size=28, weight=ft.FontWeight.BOLD),
            bgcolor=ft.Colors.GREY_900,
            color=ft.Colors.WHITE,
            border_color=ft.Colors.GREY_700,
            height=80,
            content_padding=ft.Padding(15, 10, 15, 10)
        )
        
        result_display = ft.Text(
            value="",
            size=18,
            color=ft.Colors.BLUE_700,
            text_align=ft.TextAlign.RIGHT,
            weight=ft.FontWeight.BOLD
        )
        
        # Calculator functions
        def clear_display(e):
            display.value = "0"
            result_display.value = ""
            self.page.update()
        
        def append_to_display(text):
            if display.value == "0" and text not in [".", "+", "-", "×", "÷"]:
                display.value = text
            else:
                display.value += text
            self.page.update()
        
        def calculate_result(e):
            try:
                expression = display.value
                
                # Handle fraction to decimal conversion
                if "/" in expression and all(op not in expression for op in ["+", "-", "×", "÷"]):
                    parts = expression.split("/")
                    if len(parts) == 2:
                        num = float(parts[0])
                        den = float(parts[1])
                        if den != 0:
                            result = num / den
                            result_display.value = f"= {result:.6g} = {self.decimal_to_fraction(result)}"
                        else:
                            result_display.value = "Error: Cannot divide by zero"
                
                # Handle decimal arithmetic
                else:
                    expression = expression.replace("×", "*").replace("÷", "/")
                    result = eval(expression)
                    result_display.value = f"= {result:.6g}"
                    
                    if isinstance(result, (int, float)) and result == round(result, 6):
                        frac = self.decimal_to_fraction(result)
                        if frac != str(result):
                            result_display.value += f" = {frac}"
                
                self.page.update()
                
            except Exception:
                result_display.value = "Error in calculation"
                self.page.update()
        
        def decimal_to_fraction_convert(e):
            try:
                decimal_val = float(display.value)
                fraction = self.decimal_to_fraction(decimal_val)
                result_display.value = f"= {fraction}"
                self.page.update()
            except:
                result_display.value = "Error: Enter a valid decimal"
                self.page.update()
        
        def fraction_to_decimal_convert(e):
            try:
                if "/" in display.value:
                    parts = display.value.split("/")
                    if len(parts) == 2:
                        num = float(parts[0])
                        den = float(parts[1])
                        if den != 0:
                            decimal = num / den
                            result_display.value = f"= {decimal:.6g}"
                        else:
                            result_display.value = "Error: Cannot divide by zero"
                    else:
                        result_display.value = "Error: Enter fraction as a/b"
                else:
                    result_display.value = "Error: Enter a fraction (a/b)"
                self.page.update()
            except:
                result_display.value = "Error: Invalid fraction"
                self.page.update()
        
        # Create calculator button with consistent styling
        def create_calc_button(text, on_click_func, color=ft.Colors.WHITE, bg_color=ft.Colors.GREY_300, text_color=ft.Colors.BLACK, width=70, height=60):
            return ft.Container(
                ft.ElevatedButton(
                    text,
                    on_click=on_click_func,
                    style=ft.ButtonStyle(
                        bgcolor=bg_color,
                        color=text_color,
                        shape=ft.RoundedRectangleBorder(radius=8),
                        padding=ft.Padding(0, 0, 0, 0),
                        text_style=ft.TextStyle(size=20, weight=ft.FontWeight.BOLD)
                    ),
                    width=width,
                    height=height
                ),
                padding=2
            )
        
        # Calculator grid layout (traditional calculator style)
        calculator_grid = ft.Container(
            ft.Column([
                # Row 1: Clear, Backspace, Parentheses, Division
                ft.Row([
                    create_calc_button("C", clear_display, bg_color=ft.Colors.RED_400, text_color=ft.Colors.WHITE),
                    create_calc_button("⌫", lambda e: self.backspace_display(display), bg_color=ft.Colors.ORANGE_400, text_color=ft.Colors.WHITE),
                    create_calc_button("(", lambda e: append_to_display("("), bg_color=ft.Colors.BLUE_300),
                    create_calc_button(")", lambda e: append_to_display(")"), bg_color=ft.Colors.BLUE_300),
                    create_calc_button("÷", lambda e: append_to_display("÷"), bg_color=ft.Colors.BLUE_500, text_color=ft.Colors.WHITE),
                ], alignment=ft.MainAxisAlignment.CENTER, spacing=5),
                
                # Row 2: 7, 8, 9, Multiply
                ft.Row([
                    create_calc_button("7", lambda e: append_to_display("7")),
                    create_calc_button("8", lambda e: append_to_display("8")),
                    create_calc_button("9", lambda e: append_to_display("9")),
                    create_calc_button("/", lambda e: append_to_display("/"), bg_color=ft.Colors.GREEN_400, text_color=ft.Colors.WHITE),
                    create_calc_button("×", lambda e: append_to_display("×"), bg_color=ft.Colors.BLUE_500, text_color=ft.Colors.WHITE),
                ], alignment=ft.MainAxisAlignment.CENTER, spacing=5),
                
                # Row 3: 4, 5, 6, Subtract
                ft.Row([
                    create_calc_button("4", lambda e: append_to_display("4")),
                    create_calc_button("5", lambda e: append_to_display("5")),
                    create_calc_button("6", lambda e: append_to_display("6")),
                    create_calc_button(".", lambda e: append_to_display("."), bg_color=ft.Colors.GREY_400),
                    create_calc_button("-", lambda e: append_to_display("-"), bg_color=ft.Colors.BLUE_500, text_color=ft.Colors.WHITE),
                ], alignment=ft.MainAxisAlignment.CENTER, spacing=5),
                
                # Row 4: 1, 2, 3, Add
                ft.Row([
                    create_calc_button("1", lambda e: append_to_display("1")),
                    create_calc_button("2", lambda e: append_to_display("2")),
                    create_calc_button("3", lambda e: append_to_display("3")),
                    create_calc_button("0", lambda e: append_to_display("0")),
                    create_calc_button("+", lambda e: append_to_display("+"), bg_color=ft.Colors.BLUE_500, text_color=ft.Colors.WHITE),
                ], alignment=ft.MainAxisAlignment.CENTER, spacing=5),
                
                # Row 5: Equals button (spans multiple columns)
                ft.Row([
                    ft.Container(
                        ft.ElevatedButton(
                            "=",
                            on_click=calculate_result,
                            style=ft.ButtonStyle(
                                bgcolor=ft.Colors.GREEN_600,
                                color=ft.Colors.WHITE,
                                shape=ft.RoundedRectangleBorder(radius=8),
                                text_style=ft.TextStyle(size=24, weight=ft.FontWeight.BOLD)
                            ),
                            width=360,  # Spans full width
                            height=60
                        ),
                        padding=2
                    )
                ], alignment=ft.MainAxisAlignment.CENTER, spacing=5),
            ], spacing=8),
            bgcolor=ft.Colors.GREY_800,
            padding=15,
            border_radius=15,
            border=ft.border.all(3, ft.Colors.GREY_600),
            width=400,
            alignment=ft.alignment.center
        )
        
        view = ft.View(
            "/fractions_decimals/calculator",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=go_back),
                    title=ft.Text("Fractions & Decimals Calculator"),
                    bgcolor=ft.Colors.BLUE_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("🧮 Fractions & Decimals Calculator", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900, text_align=ft.TextAlign.CENTER),
                        
                        # Display section
                        ft.Container(
                            ft.Column([
                                display,
                                ft.Container(
                                    result_display,
                                    padding=ft.Padding(10, 5, 10, 5),
                                    height=30
                                )
                            ], spacing=5),
                            padding=15,
                            bgcolor=ft.Colors.GREY_100,
                            border_radius=10,
                            border=ft.border.all(2, ft.Colors.GREY_400),
                            width=400
                        ),
                        
                        # Calculator grid
                        calculator_grid,
                        
                        # Conversion buttons
                        ft.Container(
                            ft.Column([
                                ft.Text("Quick Conversions:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_700, text_align=ft.TextAlign.CENTER),
                                ft.Row([
                                    ft.ElevatedButton(
                                        "Fraction → Decimal",
                                        on_click=fraction_to_decimal_convert,
                                        style=ft.ButtonStyle(
                                            bgcolor=ft.Colors.GREEN_700, 
                                            color=ft.Colors.WHITE,
                                            padding=ft.Padding(20, 10, 20, 10)
                                        ),
                                        width=175
                                    ),
                                    ft.ElevatedButton(
                                        "Decimal → Fraction",
                                        on_click=decimal_to_fraction_convert,
                                        style=ft.ButtonStyle(
                                            bgcolor=ft.Colors.PURPLE_700, 
                                            color=ft.Colors.WHITE,
                                            padding=ft.Padding(20, 10, 20, 10)
                                        ),
                                        width=175
                                    ),
                                ], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
                            ], spacing=10),
                            width=400
                        ),
                        
                        # Usage instructions
                        ft.Container(
                            ft.Column([
                                ft.Text("📖 How to Use:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
                                ft.Text("• Enter fractions using / (e.g., 3/4)", size=14),
                                ft.Text("• Use decimal point for decimals (e.g., 0.75)", size=14),
                                ft.Text("• Use conversion buttons for quick conversions", size=14),
                                ft.Text("• Press = for calculations", size=14),
                                ft.Text("• C clears everything, ⌫ removes last character", size=14),
                            ], spacing=5),
                            bgcolor=ft.Colors.BLUE_50,
                            padding=15,
                            border_radius=10,
                            width=400
                        )
                    ], spacing=20, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def backspace_display(self, display):
        """Remove last character from display"""
        if len(display.value) > 1:
            display.value = display.value[:-1]
        else:
            display.value = "0"
        self.page.update()

    def decimal_to_fraction(self, decimal_val):
        """Convert decimal to fraction string"""
        try:
            if decimal_val == int(decimal_val):
                return str(int(decimal_val))
            
            # Handle common decimals
            decimal_str = str(decimal_val)
            if '.' in decimal_str:
                decimal_places = len(decimal_str.split('.')[1])
                denominator = 10 ** decimal_places
                numerator = int(decimal_val * denominator)
                
                # Simplify fraction
                def gcd(a, b):
                    while b:
                        a, b = b, a % b
                    return a
                
                common_divisor = gcd(numerator, denominator)
                numerator //= common_divisor
                denominator //= common_divisor
                
                if denominator == 1:
                    return str(numerator)
                else:
                    return f"{numerator}/{denominator}"
            
            return str(decimal_val)
        except:
            return str(decimal_val)

def fractions_decimals_page(page: ft.Page):
    """Main entry point for Fractions and Decimals module"""
    page.title = "Fractions & Decimals - Mathematics Learning"
    page.scroll = ft.ScrollMode.AUTO
    page.clean()
    
    # Create module instance
    module = FractionsDecimalsModule(page)
    
    # AppBar with back button
    page.appbar = ft.AppBar(
        leading=ft.IconButton(
            ft.Icons.ARROW_BACK,
            on_click=lambda e: page.go("/maths")
        ),
        title=ft.Text("Fractions & Decimals"),
        bgcolor=ft.Colors.PURPLE_700,
        center_title=True
    )
    
    # Add main view
    page.add(module.create_main_view())