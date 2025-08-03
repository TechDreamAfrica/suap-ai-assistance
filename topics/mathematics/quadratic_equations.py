import flet as ft
import random
import math

class QuadraticEquationsModule:
    def __init__(self, page=None):
        self.page = page
        self.current_quiz_questions = []
        self.current_question_index = 0
        self.user_answers = []
        self.quiz_score = 0
        self.quiz_difficulty = "basic"
        self.practice_test_questions = []
        self.practice_test_score = 0
        self.practice_test_answers = []
        
    def show_page(self):
        """Main entry point for the module"""
        self.show_main_page()
        
    def show_main_page(self, page=None):
        """Show the main quadratic equations page
        Args:
            page: Optional page reference. If not provided, uses self.page
        """
        if page is None:
            page = self.page
        self.page = page  # Update the page reference
            
        view = ft.View(
            "/quadratic_equations",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: page.go_back()),
                    title=ft.Text("Quadratic Equations"),
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
        
        # Learning content data
        self.learning_content = {
            "quadratic_form": {
                "title": "Standard Form of Quadratic Equations",
                "content": [
                    "A quadratic equation has the form ax² + bx + c = 0.",
                    "Where a, b, and c are constants and a ≠ 0.",
                    "The highest power of the variable is 2 (squared term).",
                    "Examples: x² - 5x + 6 = 0, 2x² + 3x - 1 = 0.",
                    "The graph of a quadratic function is a parabola.",
                    "Quadratics can have 0, 1, or 2 real solutions."
                ]
            },
            "solving_methods": {
                "title": "Methods for Solving Quadratic Equations",
                "content": [
                    "Factoring: Express as (x + p)(x + q) = 0, then x = -p or x = -q.",
                    "Quadratic Formula: x = (-b ± √(b² - 4ac)) / (2a).",
                    "Completing the Square: Rewrite in the form (x + h)² = k.",
                    "Graphing: Find where the parabola crosses the x-axis.",
                    "Square Root Method: For equations like (x + h)² = k.",
                    "Choose the method based on the form of the equation."
                ]
            },
            "discriminant": {
                "title": "The Discriminant and Nature of Roots",
                "content": [
                    "The discriminant is b² - 4ac from the quadratic formula.",
                    "If b² - 4ac > 0: Two distinct real roots.",
                    "If b² - 4ac = 0: One repeated real root.",
                    "If b² - 4ac < 0: No real roots (two complex roots).",
                    "The discriminant tells us about solutions before solving.",
                    "Helps determine the best solving method to use."
                ]
            },
            "applications": {
                "title": "Applications of Quadratic Equations",
                "content": [
                    "Projectile motion: Height = -16t² + v₀t + h₀.",
                    "Area problems: Finding dimensions when area is known.",
                    "Profit maximization in business applications.",
                    "Physics: Acceleration, velocity, and position relationships.",
                    "Optimization problems: Finding maximum or minimum values.",
                    "Real-world modeling with parabolic relationships."
                ]
            }
        }

    def quadratic_equations_page(self, page: ft.Page):
        """Main Quadratic Equations page"""
        page.title = "Quadratic Equations - Mathematics Learning"
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
            leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=go_back_to_main),
            title=ft.Text("Quadratic Equations", color=ft.Colors.WHITE),
            bgcolor=ft.Colors.ORANGE_700,
            center_title=True
        )

        # Main container with tabs
        main_content = ft.Container(
            ft.Column([
                ft.Text(
                    "📐 Quadratic Equations",
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.ORANGE_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Text(
                    "Master quadratic equations and their applications",
                    size=18,
                    color=ft.Colors.ORANGE_700,
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
                    indicator_color=ft.Colors.ORANGE_700,
                    label_color=ft.Colors.ORANGE_900,
                    unselected_label_color=ft.Colors.ORANGE_400
                )
            ], spacing=20),
            padding=20,
            expand=True
        )
        
        page.add(main_content)
        # Show learning content by default
        self.show_learning_content(page)

    # Navigation helper methods
    def go_back_to_main(self, page: ft.Page):
        page.go("/maths")

    def go_back_to_quadratic_main(self, page: ft.Page):
        self.quadratic_equations_page(page)

    def show_learning_content(self, page: ft.Page):
        """Show learning content with topics"""
        page.clean()
        
        # AppBar
        page.appbar = ft.AppBar(
            leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.go_back_to_quadratic_main(page)),
            title=ft.Text("Quadratic Equations - Learn", color=ft.Colors.WHITE),
            bgcolor=ft.Colors.ORANGE_700,
            center_title=True
        )

        # Create learning content cards
        content_cards = []
        for topic_key, topic_data in self.learning_content.items():
            content_list = []
            for item in topic_data["content"]:
                content_list.append(ft.Text(f"• {item}", size=14, color=ft.Colors.ORANGE_800))
            
            card = ft.Card(
                content=ft.Container(
                    ft.Column([
                        ft.Text(topic_data["title"], size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_900),
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
                    "📐 Quadratic Equations Learning",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.ORANGE_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Text(
                    "Learn to solve and apply quadratic equations",
                    size=16,
                    color=ft.Colors.ORANGE_700,
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
            # Basic quadratic equations questions
            questions.extend([
                {
                    "question": "What is the standard form of a quadratic equation?",
                    "options": ["ax + b = 0", "ax² + bx + c = 0", "ax³ + bx² + c = 0", "ax² + b = 0"],
                    "correct": 1,
                    "explanation": "The standard form of a quadratic equation is ax² + bx + c = 0, where a ≠ 0"
                },
                {
                    "question": "Solve x² - 4 = 0",
                    "options": ["x = ±2", "x = ±4", "x = 2", "x = 4"],
                    "correct": 0,
                    "explanation": "x² - 4 = 0 → x² = 4 → x = ±√4 = ±2"
                },
                {
                    "question": "Factor x² + 5x + 6",
                    "options": ["(x + 2)(x + 3)", "(x + 1)(x + 6)", "(x - 2)(x - 3)", "(x + 5)(x + 1)"],
                    "correct": 0,
                    "explanation": "x² + 5x + 6 = (x + 2)(x + 3) because 2 + 3 = 5 and 2 × 3 = 6"
                },
                {
                    "question": "What is the discriminant of x² + 2x + 1 = 0?",
                    "options": ["0", "4", "8", "-4"],
                    "correct": 0,
                    "explanation": "Discriminant = b² - 4ac = 2² - 4(1)(1) = 4 - 4 = 0"
                },
                {
                    "question": "How many real solutions does x² + 2x + 5 = 0 have?",
                    "options": ["0", "1", "2", "3"],
                    "correct": 0,
                    "explanation": "Discriminant = 2² - 4(1)(5) = 4 - 20 = -16 < 0, so no real solutions"
                }
            ])
        
        elif difficulty == "intermediate":
            questions.extend([
                {
                    "question": "Solve x² - 6x + 9 = 0 by factoring",
                    "options": ["x = 3", "x = ±3", "x = 3, x = -3", "x = 6"],
                    "correct": 0,
                    "explanation": "x² - 6x + 9 = (x - 3)² = 0, so x = 3 (repeated root)"
                },
                {
                    "question": "Use the quadratic formula to solve x² + 4x + 1 = 0",
                    "options": ["x = -2 ± √3", "x = -2 ± √5", "x = 2 ± √3", "x = -4 ± √3"],
                    "correct": 0,
                    "explanation": "x = (-4 ± √(16-4))/2 = (-4 ± √12)/2 = (-4 ± 2√3)/2 = -2 ± √3"
                },
                {
                    "question": "Complete the square for x² + 8x + 7 = 0",
                    "options": ["(x + 4)² = 9", "(x + 4)² = 16", "(x + 8)² = 57", "(x + 4)² = 23"],
                    "correct": 0,
                    "explanation": "x² + 8x + 7 = 0 → x² + 8x = -7 → x² + 8x + 16 = -7 + 16 → (x + 4)² = 9"
                },
                {
                    "question": "Find the vertex of y = x² - 4x + 3",
                    "options": ["(2, -1)", "(2, 1)", "(-2, -1)", "(4, 3)"],
                    "correct": 0,
                    "explanation": "Vertex x = -b/2a = -(-4)/2(1) = 2; y = 2² - 4(2) + 3 = -1; Vertex: (2, -1)"
                }
            ])
        
        elif difficulty == "advanced":
            questions.extend([
                {
                    "question": "Solve 2x² - 5x - 3 = 0",
                    "options": ["x = 3, x = -1/2", "x = -3, x = 1/2", "x = 3, x = 1/2", "x = -3, x = -1/2"],
                    "correct": 0,
                    "explanation": "Using quadratic formula: x = (5 ± √(25+24))/4 = (5 ± 7)/4 = 3 or -1/2"
                },
                {
                    "question": "Find k so that x² + kx + 9 = 0 has exactly one solution",
                    "options": ["k = ±6", "k = ±3", "k = ±9", "k = ±12"],
                    "correct": 0,
                    "explanation": "For one solution, discriminant = 0: k² - 4(1)(9) = 0 → k² = 36 → k = ±6"
                },
                {
                    "question": "A ball is thrown upward. Its height is h(t) = -16t² + 64t + 80. When does it hit the ground?",
                    "options": ["t = 5 seconds", "t = 4 seconds", "t = 6 seconds", "t = 3 seconds"],
                    "correct": 0,
                    "explanation": "Set h(t) = 0: -16t² + 64t + 80 = 0 → t² - 4t - 5 = 0 → (t-5)(t+1) = 0 → t = 5 (positive)"
                }
            ])
        
        return random.sample(questions, min(5, len(questions)))

    def show_practice_quiz(self, page: ft.Page):
        """Show practice quiz options"""
        page.clean()
        
        # AppBar
        page.appbar = ft.AppBar(
            leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.go_back_to_quadratic_main(page)),
            title=ft.Text("Quadratic Equations - Quiz", color=ft.Colors.WHITE),
            bgcolor=ft.Colors.ORANGE_700,
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
                    color=ft.Colors.ORANGE_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Text(
                    "Test your knowledge of quadratic equations",
                    size=16,
                    color=ft.Colors.ORANGE_700,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Divider(height=30),
                
                ft.Text("Select Difficulty Level:", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_900),
                
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
                        "📐 Intermediate Level",
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
            bgcolor=ft.Colors.ORANGE_700,
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
                        bgcolor=ft.Colors.ORANGE_50,
                        color=ft.Colors.ORANGE_900,
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
                    color=ft.Colors.ORANGE_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Container(
                    ft.Text(
                        question["question"],
                        size=18,
                        text_align=ft.TextAlign.CENTER,
                        color=ft.Colors.ORANGE_800
                    ),
                    bgcolor=ft.Colors.ORANGE_50,
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
            bgcolor=ft.Colors.ORANGE_700,
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
                        ft.Text("Explanation:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_900),
                        ft.Text(question["explanation"], size=14, color=ft.Colors.ORANGE_800)
                    ], spacing=10),
                    bgcolor=ft.Colors.ORANGE_50,
                    border_radius=10,
                    padding=20,
                    margin=ft.margin.only(top=20, bottom=20)
                ),
                ft.ElevatedButton(
                    "Next Question" if self.current_question_index < len(self.current_quiz_questions) - 1 else "View Results",
                    on_click=next_question,
                    style=ft.ButtonStyle(
                        padding=20,
                        bgcolor=ft.Colors.ORANGE_700,
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
            bgcolor=ft.Colors.ORANGE_700,
            center_title=True,
            automatically_imply_leading=False
        )

        percentage = (self.quiz_score / len(self.current_quiz_questions)) * 100
        
        def retake_quiz(e):
            self.show_practice_quiz(page)

        def back_to_main(e):
            self.go_back_to_quadratic_main(page)

        # Determine performance message
        if percentage >= 80:
            performance_msg = "Excellent work! 🎉"
            performance_color = ft.Colors.GREEN_700
        elif percentage >= 60:
            performance_msg = "Good job! 👍"
            performance_color = ft.Colors.ORANGE_700
        else:
            performance_msg = "Keep practicing! 💪"
            performance_color = ft.Colors.RED_700

        content = ft.Container(
            ft.Column([
                ft.Text(
                    "Quiz Complete!",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.ORANGE_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Container(
                    ft.Column([
                        ft.Text(f"Your Score: {self.quiz_score}/{len(self.current_quiz_questions)}", size=24, weight=ft.FontWeight.BOLD),
                        ft.Text(f"Percentage: {percentage:.1f}%", size=20),
                        ft.Text(performance_msg, size=18, color=performance_color, weight=ft.FontWeight.BOLD)
                    ], spacing=10, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    bgcolor=ft.Colors.ORANGE_50,
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
                            bgcolor=ft.Colors.ORANGE_100,
                            color=ft.Colors.ORANGE_900,
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
        """Show AI help for quadratic equations"""
        page.clean()
        
        # AppBar
        page.appbar = ft.AppBar(
            leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.go_back_to_quadratic_main(page)),
            title=ft.Text("Quadratic Equations - AI Help", color=ft.Colors.WHITE),
            bgcolor=ft.Colors.ORANGE_700,
            center_title=True
        )

        # AI help topics
        def show_help_topic(e):
            topic = e.control.data
            self.show_specific_help(page, topic)

        help_topics = [
            ("standard_form", "📐 Standard Form"),
            ("factoring", "🔧 Factoring Method"),
            ("quadratic_formula", "📊 Quadratic Formula"),
            ("completing_square", "⬜ Completing the Square"),
            ("discriminant", "🔍 Discriminant"),
            ("applications", "🌍 Real-World Applications")
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
                        bgcolor=ft.Colors.ORANGE_50,
                        color=ft.Colors.ORANGE_900,
                        shape=ft.RoundedRectangleBorder(radius=10)
                    ),
                    width=350
                )
            )

        content = ft.Container(
            ft.Column([
                ft.Text(
                    "🤖 AI Help - Quadratic Equations",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.ORANGE_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Text(
                    "Get help with specific quadratic equation topics",
                    size=16,
                    color=ft.Colors.ORANGE_700,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Divider(height=30),
                
                ft.Text("Choose a topic for detailed help:", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_900),
                
                ft.Column(topic_buttons, spacing=15, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            ], spacing=20, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=20,
            expand=True
        )
        
        page.add(content)

    def show_specific_help(self, page: ft.Page, topic_key):
        """Show specific help for a topic"""
        help_content = {
            "standard_form": {
                "title": "Standard Form",
                "content": [
                    "QUADRATIC EQUATION STANDARD FORM:",
                    "• ax² + bx + c = 0",
                    "• a, b, c are constants (a ≠ 0)",
                    "• The highest power is 2 (quadratic term)",
                    "",
                    "EXAMPLES:",
                    "• x² - 5x + 6 = 0 (a=1, b=-5, c=6)",
                    "• 2x² + 3x - 1 = 0 (a=2, b=3, c=-1)",
                    "• x² - 4 = 0 (a=1, b=0, c=-4)",
                    "",
                    "GRAPH:",
                    "• The graph is always a parabola",
                    "• Opens up if a > 0, down if a < 0"
                ]
            },
            "factoring": {
                "title": "Factoring Method",
                "content": [
                    "FACTORING STEPS:",
                    "• Find two numbers that multiply to give ac",
                    "• And add to give b",
                    "• Rewrite the middle term using these numbers",
                    "• Factor by grouping",
                    "",
                    "EXAMPLE: x² + 5x + 6 = 0",
                    "• Need two numbers: product = 6, sum = 5",
                    "• Numbers are 2 and 3 (2×3=6, 2+3=5)",
                    "• Factor: (x + 2)(x + 3) = 0",
                    "• Solutions: x = -2 or x = -3",
                    "",
                    "WHEN TO USE:",
                    "• When the quadratic factors nicely",
                    "• Usually when coefficients are small integers"
                ]
            },
            "quadratic_formula": {
                "title": "Quadratic Formula",
                "content": [
                    "THE QUADRATIC FORMULA:",
                    "• x = (-b ± √(b² - 4ac)) / (2a)",
                    "• Works for ANY quadratic equation",
                    "• Substitute values of a, b, c from ax² + bx + c = 0",
                    "",
                    "EXAMPLE: 2x² + 3x - 1 = 0",
                    "• a = 2, b = 3, c = -1",
                    "• x = (-3 ± √(9 - 4(2)(-1))) / (2(2))",
                    "• x = (-3 ± √(9 + 8)) / 4",
                    "• x = (-3 ± √17) / 4",
                    "",
                    "WHEN TO USE:",
                    "• When factoring is difficult or impossible",
                    "• Always gives exact answers"
                ]
            },
            "completing_square": {
                "title": "Completing the Square",
                "content": [
                    "COMPLETING THE SQUARE STEPS:",
                    "• Move constant to right side",
                    "• Take half of b coefficient, then square it",
                    "• Add this to both sides",
                    "• Factor left side as perfect square",
                    "",
                    "EXAMPLE: x² + 6x + 5 = 0",
                    "• x² + 6x = -5",
                    "• Half of 6 is 3, squared is 9",
                    "• x² + 6x + 9 = -5 + 9",
                    "• (x + 3)² = 4",
                    "• x + 3 = ±2, so x = -3 ± 2",
                    "",
                    "WHEN TO USE:",
                    "• To find vertex form of parabola",
                    "• When you need exact form with radicals"
                ]
            },
            "discriminant": {
                "title": "Discriminant",
                "content": [
                    "THE DISCRIMINANT:",
                    "• Discriminant = b² - 4ac",
                    "• Tells us about the nature of solutions",
                    "• From the quadratic formula",
                    "",
                    "INTERPRETING THE DISCRIMINANT:",
                    "• If b² - 4ac > 0: Two distinct real roots",
                    "• If b² - 4ac = 0: One repeated real root",
                    "• If b² - 4ac < 0: No real roots (complex roots)",
                    "",
                    "EXAMPLE: x² + 2x + 5 = 0",
                    "• a = 1, b = 2, c = 5",
                    "• Discriminant = 2² - 4(1)(5) = 4 - 20 = -16",
                    "• Since -16 < 0, no real solutions",
                    "",
                    "USES:",
                    "• Determine number of solutions before solving",
                    "• Choose the best solving method"
                ]
            },
            "applications": {
                "title": "Real-World Applications",
                "content": [
                    "PROJECTILE MOTION:",
                    "• Height: h(t) = -16t² + v₀t + h₀",
                    "• Find when object hits ground (h = 0)",
                    "• Find maximum height (vertex)",
                    "",
                    "AREA PROBLEMS:",
                    "• Given area, find dimensions",
                    "• Example: Rectangle area = length × width",
                    "• Often leads to quadratic equations",
                    "",
                    "BUSINESS APPLICATIONS:",
                    "• Profit = Revenue - Cost",
                    "• Revenue = price × quantity",
                    "• Find price for maximum profit",
                    "",
                    "PHYSICS:",
                    "• Acceleration problems",
                    "• Distance, velocity, time relationships",
                    "• Energy conservation problems"
                ]
            }
        }

        topic_data = help_content.get(topic_key, {"title": "Topic", "content": ["Help content not available."]})
        
        page.clean()
        
        # AppBar
        page.appbar = ft.AppBar(
            leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.show_ai_help(page)),
            title=ft.Text(f"AI Help - {topic_data['title']}", color=ft.Colors.WHITE),
            bgcolor=ft.Colors.ORANGE_700,
            center_title=True
        )

        # Content
        content_items = []
        for item in topic_data["content"]:
            if item == "":
                content_items.append(ft.Divider(height=10))
            else:
                content_items.append(ft.Text(item, size=14, color=ft.Colors.ORANGE_800))

        content = ft.Container(
            ft.Column([
                ft.Text(
                    f"🤖 {topic_data['title']}",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.ORANGE_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Container(
                    ft.Column(content_items, spacing=8),
                    bgcolor=ft.Colors.ORANGE_50,
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
            leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.go_back_to_quadratic_main(page)),
            title=ft.Text("Quadratic Equations - Examples", color=ft.Colors.WHITE),
            bgcolor=ft.Colors.ORANGE_700,
            center_title=True
        )

        # Example problems
        examples = [
            {
                "title": "Solving by Factoring",
                "problem": "Solve x² + 7x + 12 = 0",
                "solution": [
                    "Find two numbers that multiply to 12 and add to 7",
                    "The numbers are 3 and 4 (3×4=12, 3+4=7)",
                    "Factor: (x + 3)(x + 4) = 0",
                    "Set each factor equal to zero:",
                    "x + 3 = 0 → x = -3",
                    "x + 4 = 0 → x = -4",
                    "Solutions: x = -3, x = -4"
                ]
            },
            {
                "title": "Using the Quadratic Formula",
                "problem": "Solve 2x² - 3x - 2 = 0",
                "solution": [
                    "Identify: a = 2, b = -3, c = -2",
                    "Apply quadratic formula: x = (-b ± √(b² - 4ac)) / (2a)",
                    "x = (-(-3) ± √((-3)² - 4(2)(-2))) / (2(2))",
                    "x = (3 ± √(9 + 16)) / 4",
                    "x = (3 ± √25) / 4",
                    "x = (3 ± 5) / 4",
                    "Solutions: x = 8/4 = 2 or x = -2/4 = -1/2"
                ]
            },
            {
                "title": "Projectile Motion Problem",
                "problem": "A ball is thrown upward with initial velocity 48 ft/s from a height of 32 ft. When will it hit the ground?",
                "solution": [
                    "Use the height equation: h(t) = -16t² + 48t + 32",
                    "Set h(t) = 0 (when it hits the ground):",
                    "-16t² + 48t + 32 = 0",
                    "Divide by -16: t² - 3t - 2 = 0",
                    "Use quadratic formula: t = (3 ± √(9 + 8)) / 2",
                    "t = (3 ± √17) / 2",
                    "t ≈ (3 + 4.12) / 2 ≈ 3.56 seconds (take positive value)",
                    "The ball hits the ground after approximately 3.56 seconds"
                ]
            },
            {
                "title": "Completing the Square",
                "problem": "Solve x² + 4x - 1 = 0 by completing the square",
                "solution": [
                    "Move constant to right side: x² + 4x = 1",
                    "Take half of coefficient of x: 4/2 = 2",
                    "Square it: 2² = 4",
                    "Add to both sides: x² + 4x + 4 = 1 + 4",
                    "Factor left side: (x + 2)² = 5",
                    "Take square root: x + 2 = ±√5",
                    "Solve for x: x = -2 ± √5",
                    "Solutions: x = -2 + √5 or x = -2 - √5"
                ]
            }
        ]

        example_cards = []
        for example in examples:
            solution_items = []
            for step in example["solution"]:
                solution_items.append(ft.Text(f"• {step}", size=13, color=ft.Colors.ORANGE_800))
            
            card = ft.Card(
                content=ft.Container(
                    ft.Column([
                        ft.Text(example["title"], size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_900),
                        ft.Text("Problem:", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_800),
                        ft.Text(example["problem"], size=14, color=ft.Colors.ORANGE_700),
                        ft.Text("Solution:", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_800),
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
                    color=ft.Colors.ORANGE_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Text(
                    "Step-by-step solutions to common quadratic equation problems",
                    size=16,
                    color=ft.Colors.ORANGE_700,
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


def quadratic_equations_page(page: ft.Page):
    """Main entry point for Quadratic Equations module"""
    module = QuadraticEquationsModule()
    module.show_main_page(page)
