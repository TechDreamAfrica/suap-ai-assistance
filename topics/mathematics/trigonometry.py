import flet as ft
import random
import math

class TrigonometryModule:
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
        """Show the main trigonometry page
        Args:
            page: Optional page reference. If not provided, uses self.page
        """
        if page is None:
            page = self.page
        self.page = page  # Update the page reference
            
        view = ft.View(
            "/trigonometry",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: page.go_back()),
                    title=ft.Text("Trigonometry"),
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
            "basic_ratios": {
                "title": "Basic Trigonometric Ratios",
                "content": [
                    "Trigonometry studies relationships between angles and sides of triangles.",
                    "Three basic ratios: sine (sin), cosine (cos), and tangent (tan).",
                    "sin θ = opposite / hypotenuse",
                    "cos θ = adjacent / hypotenuse",
                    "tan θ = opposite / adjacent",
                    "Remember: SOH-CAH-TOA"
                ]
            },
            "special_angles": {
                "title": "Special Angles",
                "content": [
                    "Common angles: 30°, 45°, 60°, 90°",
                    "sin 30° = 1/2, cos 30° = √3/2, tan 30° = 1/√3",
                    "sin 45° = √2/2, cos 45° = √2/2, tan 45° = 1",
                    "sin 60° = √3/2, cos 60° = 1/2, tan 60° = √3",
                    "sin 90° = 1, cos 90° = 0, tan 90° = undefined"
                ]
            },
            "unit_circle": {
                "title": "Unit Circle",
                "content": [
                    "Circle with radius 1 centered at origin",
                    "Angle measured from positive x-axis",
                    "cos θ = x-coordinate, sin θ = y-coordinate",
                    "Angles can be in degrees or radians",
                    "π radians = 180°, so 1 radian ≈ 57.3°"
                ]
            },
            "identities": {
                "title": "Trigonometric Identities",
                "content": [
                    "Pythagorean identity: sin²θ + cos²θ = 1",
                    "Reciprocal identities:",
                    "csc θ = 1/sin θ (cosecant)",
                    "sec θ = 1/cos θ (secant)",
                    "cot θ = 1/tan θ (cotangent)",
                    "tan θ = sin θ / cos θ"
                ]
            }
        }

        
    def trigonometry_page(self, page: ft.Page):
        """Main Trigonometry learning page"""
        page.title = "Trigonometry - Mathematics Learning"
        page.scroll = ft.ScrollMode.AUTO
        page.clean()
        
        # Navigation helper functions
        def go_back_to_main(e):
            page.go("/maths")
        
        # AppBar with back button
        page.appbar = ft.AppBar(
            leading=ft.IconButton(
                ft.Icons.ARROW_BACK,
                on_click=go_back_to_main
            ),
            title=ft.Text("Trigonometry"),
            bgcolor=ft.Colors.PURPLE_700,
            center_title=True
        )
        
        # Main content
        content = ft.Container(
            ft.Column([
                ft.Text(
                    "� Trigonometry",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.PURPLE_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Text(
                    "Master the relationships between angles and sides in triangles",
                    size=16,
                    color=ft.Colors.PURPLE_700,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Divider(height=30),
                
                # Learning sections
                ft.Container(
                    ft.Column([
                        ft.Text("🎯 Learning Objectives", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_900),
                        ft.Text("• Understand trigonometric ratios (sin, cos, tan)", size=14),
                        ft.Text("• Work with special angles and the unit circle", size=14),
                        ft.Text("• Apply trigonometric identities", size=14),
                        ft.Text("• Solve triangles using trigonometry", size=14),
                        ft.Text("• Use trigonometry in real-world applications", size=14),
                    ], spacing=10),
                    bgcolor=ft.Colors.PURPLE_50,
                    border_radius=10,
                    padding=20,
                    margin=ft.margin.only(bottom=20)
                ),
                
                # Action buttons
                ft.ResponsiveRow([
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.BOOK, size=30, color=ft.Colors.PURPLE_700),
                                ft.Text("Learn", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            style=ft.ButtonStyle(
                                padding=20,
                                bgcolor=ft.Colors.PURPLE_50,
                                shape=ft.RoundedRectangleBorder(radius=10)
                            ),
                            on_click=lambda e: self.show_learning_content(page)
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.QUIZ, size=30, color=ft.Colors.PURPLE_700),
                                ft.Text("Practice Quiz", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            style=ft.ButtonStyle(
                                padding=20,
                                bgcolor=ft.Colors.PURPLE_50,
                                shape=ft.RoundedRectangleBorder(radius=10)
                            ),
                            on_click=lambda e: self.show_practice_quiz(page)
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.HELP_OUTLINE, size=30, color=ft.Colors.PURPLE_700),
                                ft.Text("AI Help", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            style=ft.ButtonStyle(
                                padding=20,
                                bgcolor=ft.Colors.PURPLE_50,
                                shape=ft.RoundedRectangleBorder(radius=10)
                            ),
                            on_click=lambda e: self.show_ai_help(page)
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.LIGHTBULB_OUTLINE, size=30, color=ft.Colors.PURPLE_700),
                                ft.Text("Examples", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            style=ft.ButtonStyle(
                                padding=20,
                                bgcolor=ft.Colors.PURPLE_50,
                                shape=ft.RoundedRectangleBorder(radius=10)
                            ),
                            on_click=lambda e: self.show_examples(page)
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                ], spacing=15, run_spacing=15),
                
                ft.Divider(height=20),
                
                # Content area
                ft.Container(
                    ft.Column([
                        ft.Text("Welcome to Trigonometry Learning!", size=18, weight=ft.FontWeight.BOLD),
                        ft.Text("This is where you'll learn about trigonometry concepts. Click the buttons above to get started with learning content, practice quizzes, AI help, or see examples.", size=14),
                        ft.Text("✨ Features:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_900),
                        ft.Text("• Interactive learning for trigonometry", size=14),
                        ft.Text("• Step-by-step problem solving", size=14),
                        ft.Text("• Practice exercises with feedback", size=14),
                        ft.Text("• Helpful examples and explanations", size=14),
                    ], spacing=10),
                    bgcolor=ft.Colors.GREY_50,
                    border_radius=10,
                    padding=20
                )
            ], spacing=20),
            padding=20,
            expand=True
        )
        
        page.add(content)

        
    def go_back_to_main(self, page: ft.Page):
        """Navigate back to main maths page"""
        page.go("/maths")
        
    def go_back_to_trigonometry_main(self, page: ft.Page):
        """Navigate back to trigonometry main page"""
        self.trigonometry_page(page)
        
    def show_learning_content(self, page: ft.Page):
        """Display comprehensive learning content"""
        page.clean()
        
        # AppBar with back button
        page.appbar = ft.AppBar(
            leading=ft.IconButton(
                ft.Icons.ARROW_BACK,
                on_click=lambda e: self.go_back_to_trigonometry_main(page)
            ),
            title=ft.Text("Trigonometry Learning Content"),
            bgcolor=ft.Colors.PURPLE_700,
            center_title=True
        )
        
        # Create tabs for different topics
        tabs = []
        for topic_key, topic_data in self.learning_content.items():
            content_items = []
            for i, content_point in enumerate(topic_data["content"]):
                content_items.append(
                    ft.Container(
                        ft.Text(content_point, size=14),
                        bgcolor=ft.Colors.PURPLE_50 if i % 2 == 0 else ft.Colors.WHITE,
                        padding=15,
                        border_radius=8,
                        margin=ft.margin.only(bottom=10)
                    )
                )
                
            tabs.append(
                ft.Tab(
                    text=topic_data["title"],
                    content=ft.Container(
                        ft.Column(content_items, spacing=10, scroll=ft.ScrollMode.AUTO),
                        padding=20
                    )
                )
            )
        
        content = ft.Container(
            ft.Column([
                ft.Text(
                    "📐 Trigonometry Learning Content",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.PURPLE_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Divider(height=20),
                ft.Container(
                    ft.Tabs(
                        selected_index=0,
                        animation_duration=300,
                        tabs=tabs,
                        expand=1
                    ),
                    expand=True
                )
            ], spacing=20),
            padding=20,
            expand=True
        )
        
        page.add(content)
        
    def generate_quiz_questions(self, difficulty="basic"):
        """Generate quiz questions based on difficulty level"""
        questions = []
        
        if difficulty == "basic":
            questions = [
                {
                    "question": "What is sin(30°)?",
                    "options": ["1/2", "√2/2", "√3/2", "1"],
                    "correct": 0,
                    "explanation": "sin(30°) = 1/2. This is one of the special angle values."
                },
                {
                    "question": "What is cos(45°)?",
                    "options": ["1/2", "√2/2", "√3/2", "1"],
                    "correct": 1,
                    "explanation": "cos(45°) = √2/2. In a 45-45-90 triangle, both legs are equal."
                },
                {
                    "question": "What is tan(60°)?",
                    "options": ["1", "√3", "1/√3", "√2"],
                    "correct": 1,
                    "explanation": "tan(60°) = √3. This comes from the 30-60-90 triangle ratios."
                },
                {
                    "question": "In SOH-CAH-TOA, what does 'SOH' represent?",
                    "options": ["sin = opposite/hypotenuse", "sin = adjacent/hypotenuse", "cos = opposite/hypotenuse", "tan = opposite/hypotenuse"],
                    "correct": 0,
                    "explanation": "'SOH' means Sin = Opposite/Hypotenuse"
                },
                {
                    "question": "What is the Pythagorean identity?",
                    "options": ["sin²θ + cos²θ = 1", "sin²θ - cos²θ = 1", "tan²θ + 1 = sec²θ", "sin θ + cos θ = 1"],
                    "correct": 0,
                    "explanation": "The fundamental Pythagorean identity is sin²θ + cos²θ = 1"
                }
            ]
        elif difficulty == "intermediate":
            questions = [
                {
                    "question": "If sin θ = 3/5 and θ is in the first quadrant, what is cos θ?",
                    "options": ["4/5", "3/4", "5/4", "4/3"],
                    "correct": 0,
                    "explanation": "Using sin²θ + cos²θ = 1: (3/5)² + cos²θ = 1, so cos²θ = 16/25, thus cos θ = 4/5"
                },
                {
                    "question": "What is the period of sin(x)?",
                    "options": ["π", "2π", "π/2", "4π"],
                    "correct": 1,
                    "explanation": "The sine function has a period of 2π, meaning sin(x + 2π) = sin(x)"
                },
                {
                    "question": "If cos θ = -1/2, what are the possible values of θ in [0, 2π]?",
                    "options": ["π/3, 5π/3", "2π/3, 4π/3", "π/6, 11π/6", "π/4, 7π/4"],
                    "correct": 1,
                    "explanation": "cos θ = -1/2 occurs at θ = 2π/3 and θ = 4π/3 in the interval [0, 2π]"
                },
                {
                    "question": "What is sec(θ) equal to?",
                    "options": ["sin θ", "1/sin θ", "1/cos θ", "cos θ"],
                    "correct": 2,
                    "explanation": "Secant is the reciprocal of cosine: sec θ = 1/cos θ"
                },
                {
                    "question": "In which quadrants is tangent positive?",
                    "options": ["I and II", "I and III", "II and IV", "I and IV"],
                    "correct": 1,
                    "explanation": "Tangent is positive when sin and cos have the same sign, which occurs in quadrants I and III"
                }
            ]
        
        return random.sample(questions, min(len(questions), 5))
        
    def show_practice_quiz(self, page: ft.Page):
        """Display practice quiz with multiple choice questions"""
        page.clean()
        
        # AppBar with back button
        page.appbar = ft.AppBar(
            leading=ft.IconButton(
                ft.Icons.ARROW_BACK,
                on_click=lambda e: self.go_back_to_trigonometry_main(page)
            ),
            title=ft.Text("Trigonometry Practice Quiz"),
            bgcolor=ft.Colors.PURPLE_700,
            center_title=True
        )
        
        # Difficulty selection
        difficulty_dropdown = ft.Dropdown(
            width=200,
            options=[
                ft.dropdown.Option("basic", "Basic"),
                ft.dropdown.Option("intermediate", "Intermediate"),
            ],
            value="basic",
            on_change=lambda e: self.update_difficulty(e.control.value)
        )
        
        def start_quiz(e):
            self.current_quiz_questions = self.generate_quiz_questions(self.quiz_difficulty)
            self.current_question_index = 0
            self.user_answers = []
            self.quiz_score = 0
            self.show_quiz_question(page)
            
        content = ft.Container(
            ft.Column([
                ft.Text(
                    "🧠 Practice Quiz",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.PURPLE_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Text(
                    "Test your trigonometry knowledge with interactive questions",
                    size=16,
                    color=ft.Colors.PURPLE_700,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Divider(height=30),
                
                ft.Container(
                    ft.Column([
                        ft.Text("Select Difficulty:", size=16, weight=ft.FontWeight.BOLD),
                        difficulty_dropdown,
                        ft.ElevatedButton(
                            "Start Quiz",
                            icon=ft.Icons.PLAY_ARROW,
                            style=ft.ButtonStyle(
                                bgcolor=ft.Colors.PURPLE_600,
                                color=ft.Colors.WHITE,
                                padding=20
                            ),
                            on_click=start_quiz
                        )
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20),
                    bgcolor=ft.Colors.PURPLE_50,
                    border_radius=10,
                    padding=30,
                    alignment=ft.alignment.center
                )
            ], spacing=20, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=20,
            expand=True
        )
        
        page.add(content)
        
    def update_difficulty(self, difficulty):
        """Update quiz difficulty"""
        self.quiz_difficulty = difficulty
        
    def show_quiz_question(self, page: ft.Page):
        """Display current quiz question"""
        if self.current_question_index >= len(self.current_quiz_questions):
            self.show_quiz_results(page)
            return
            
        page.clean()
        
        # AppBar with back button
        page.appbar = ft.AppBar(
            leading=ft.IconButton(
                ft.Icons.ARROW_BACK,
                on_click=lambda e: self.show_practice_quiz(page)
            ),
            title=ft.Text(f"Question {self.current_question_index + 1}/{len(self.current_quiz_questions)}"),
            bgcolor=ft.Colors.PURPLE_700,
            center_title=True
        )
        
        current_question = self.current_quiz_questions[self.current_question_index]
        
        # Create option buttons
        option_buttons = []
        for i, option in enumerate(current_question["options"]):
            option_buttons.append(
                ft.ElevatedButton(
                    option,
                    style=ft.ButtonStyle(
                        bgcolor=ft.Colors.PURPLE_50,
                        padding=15,
                        shape=ft.RoundedRectangleBorder(radius=10)
                    ),
                    width=200,
                    on_click=lambda e, idx=i: self.answer_question(page, idx)
                )
            )
        
        content = ft.Container(
            ft.Column([
                ft.Text(
                    f"Question {self.current_question_index + 1}",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.PURPLE_900
                ),
                ft.Container(
                    ft.Text(
                        current_question["question"],
                        size=16,
                        text_align=ft.TextAlign.CENTER
                    ),
                    bgcolor=ft.Colors.PURPLE_50,
                    border_radius=10,
                    padding=20,
                    margin=ft.margin.only(bottom=30)
                ),
                ft.Text("Choose your answer:", size=14, weight=ft.FontWeight.BOLD),
                ft.Column(option_buttons, spacing=15, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            ], spacing=20, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=20,
            expand=True
        )
        
        page.add(content)
        
    def answer_question(self, page: ft.Page, selected_option):
        """Process quiz answer and show feedback"""
        current_question = self.current_quiz_questions[self.current_question_index]
        is_correct = selected_option == current_question["correct"]
        
        if is_correct:
            self.quiz_score += 1
            
        self.user_answers.append(selected_option)
        self.show_answer_feedback(page, is_correct, current_question)
        
    def show_answer_feedback(self, page: ft.Page, is_correct, question):
        """Show feedback for the answered question"""
        page.clean()
        
        # AppBar with back button
        page.appbar = ft.AppBar(
            leading=ft.IconButton(
                ft.Icons.ARROW_BACK,
                on_click=lambda e: self.show_practice_quiz(page)
            ),
            title=ft.Text("Answer Feedback"),
            bgcolor=ft.Colors.PURPLE_700,
            center_title=True
        )
        
        feedback_color = ft.Colors.GREEN if is_correct else ft.Colors.RED
        feedback_icon = ft.Icons.CHECK_CIRCLE if is_correct else ft.Icons.CANCEL
        feedback_text = "Correct!" if is_correct else "Incorrect"
        
        def next_question(e):
            self.current_question_index += 1
            self.show_quiz_question(page)
            
        content = ft.Container(
            ft.Column([
                ft.Icon(feedback_icon, size=60, color=feedback_color),
                ft.Text(
                    feedback_text,
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    color=feedback_color,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("Explanation:", size=16, weight=ft.FontWeight.BOLD),
                        ft.Text(question["explanation"], size=14),
                        ft.Text(f"Correct answer: {question['options'][question['correct']]}", 
                               size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN)
                    ], spacing=10),
                    bgcolor=ft.Colors.GREY_50,
                    border_radius=10,
                    padding=20,
                    margin=ft.margin.only(top=20, bottom=30)
                ),
                ft.ElevatedButton(
                    "Next Question" if self.current_question_index < len(self.current_quiz_questions) - 1 else "View Results",
                    icon=ft.Icons.ARROW_FORWARD,
                    style=ft.ButtonStyle(
                        bgcolor=ft.Colors.PURPLE_600,
                        color=ft.Colors.WHITE,
                        padding=20
                    ),
                    on_click=next_question
                )
            ], spacing=20, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=20,
            expand=True
        )
        
        page.add(content)
        
    def show_quiz_results(self, page: ft.Page):
        """Display quiz results and performance summary"""
        page.clean()
        
        # AppBar with back button
        page.appbar = ft.AppBar(
            leading=ft.IconButton(
                ft.Icons.ARROW_BACK,
                on_click=lambda e: self.go_back_to_trigonometry_main(page)
            ),
            title=ft.Text("Quiz Results"),
            bgcolor=ft.Colors.PURPLE_700,
            center_title=True
        )
        
        total_questions = len(self.current_quiz_questions)
        percentage = (self.quiz_score / total_questions) * 100
        
        # Performance feedback
        if percentage >= 80:
            performance_text = "Excellent work! 🌟"
            performance_color = ft.Colors.GREEN
        elif percentage >= 60:
            performance_text = "Good job! 👍"
            performance_color = ft.Colors.BLUE
        else:
            performance_text = "Keep practicing! 💪"
            performance_color = ft.Colors.ORANGE
            
        def retake_quiz(e):
            self.show_practice_quiz(page)
            
        content = ft.Container(
            ft.Column([
                ft.Text(
                    "🏆 Quiz Complete!",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.PURPLE_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Container(
                    ft.Column([
                        ft.Text(f"Score: {self.quiz_score}/{total_questions}", size=24, weight=ft.FontWeight.BOLD),
                        ft.Text(f"Percentage: {percentage:.1f}%", size=20),
                        ft.Text(performance_text, size=18, color=performance_color, weight=ft.FontWeight.BOLD)
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
                    bgcolor=ft.Colors.PURPLE_50,
                    border_radius=10,
                    padding=30,
                    margin=ft.margin.only(bottom=30)
                ),
                
                # Action buttons
                ft.Row([
                    ft.ElevatedButton(
                        "Retake Quiz",
                        icon=ft.Icons.REFRESH,
                        style=ft.ButtonStyle(
                            bgcolor=ft.Colors.PURPLE_600,
                            color=ft.Colors.WHITE,
                            padding=20
                        ),
                        on_click=retake_quiz
                    ),
                    ft.ElevatedButton(
                        "Back to Main",
                        icon=ft.Icons.HOME,
                        style=ft.ButtonStyle(
                            bgcolor=ft.Colors.GREY_600,
                            color=ft.Colors.WHITE,
                            padding=20
                        ),
                        on_click=lambda e: self.go_back_to_trigonometry_main(page)
                    )
                ], alignment=ft.MainAxisAlignment.CENTER, spacing=20)
            ], spacing=20, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=20,
            expand=True
        )
        
        page.add(content)
        
    def show_ai_help(self, page: ft.Page):
        """Display AI help interface"""
        page.clean()
        
        # AppBar with back button
        page.appbar = ft.AppBar(
            leading=ft.IconButton(
                ft.Icons.ARROW_BACK,
                on_click=lambda e: self.go_back_to_trigonometry_main(page)
            ),
            title=ft.Text("AI Help - Trigonometry"),
            bgcolor=ft.Colors.PURPLE_700,
            center_title=True
        )
        
        # Help topics
        help_topics = [
            {
                "title": "📐 Basic Trig Ratios",
                "description": "Learn about sine, cosine, and tangent ratios",
                "icon": ft.Icons.FUNCTIONS
            },
            {
                "title": "🔄 Special Angles",
                "description": "Master the common angles: 30°, 45°, 60°, 90°",
                "icon": ft.Icons.ROTATE_RIGHT
            },
            {
                "title": "⭕ Unit Circle",
                "description": "Understand the unit circle and angle measurement",
                "icon": ft.Icons.CIRCLE_OUTLINED
            },
            {
                "title": "🧮 Trig Identities",
                "description": "Learn and apply trigonometric identities",
                "icon": ft.Icons.CALCULATE
            }
        ]
        
        help_cards = []
        for topic in help_topics:
            help_cards.append(
                ft.Container(
                    ft.ListTile(
                        leading=ft.Icon(topic["icon"], size=30, color=ft.Colors.PURPLE_700),
                        title=ft.Text(topic["title"], weight=ft.FontWeight.BOLD),
                        subtitle=ft.Text(topic["description"]),
                        on_click=lambda e, t=topic["title"]: self.show_specific_help(page, t)
                    ),
                    bgcolor=ft.Colors.PURPLE_50,
                    border_radius=10,
                    margin=ft.margin.only(bottom=10)
                )
            )
        
        content = ft.Container(
            ft.Column([
                ft.Text(
                    "🤖 AI Trigonometry Helper",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.PURPLE_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Text(
                    "Get personalized help with trigonometry concepts and problems",
                    size=16,
                    color=ft.Colors.PURPLE_700,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Divider(height=30),
                
                ft.Column(help_cards, spacing=10),
                
                ft.Container(
                    ft.Column([
                        ft.Text("💡 Quick Tips:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_900),
                        ft.Text("• Remember SOH-CAH-TOA for basic ratios", size=14),
                        ft.Text("• Practice with special angles first", size=14),
                        ft.Text("• Use the unit circle for reference", size=14),
                        ft.Text("• Check your calculator mode (degrees/radians)", size=14),
                    ], spacing=8),
                    bgcolor=ft.Colors.ORANGE_50,
                    border_radius=10,
                    padding=20,
                    margin=ft.margin.only(top=20)
                )
            ], spacing=20),
            padding=20,
            expand=True,
            scroll=ft.ScrollMode.AUTO
        )
        
        page.add(content)
        
    def show_specific_help(self, page: ft.Page, topic_title):
        """Show specific help content for a topic"""
        page.snack_bar = ft.SnackBar(
            content=ft.Text(f"Detailed help for '{topic_title}' coming soon! This will include step-by-step tutorials and interactive examples."),
            bgcolor=ft.Colors.PURPLE_100
        )
        page.snack_bar.open = True
        page.update()
        
    def show_examples(self, page: ft.Page):
        """Display worked examples"""
        page.clean()
        
        # AppBar with back button
        page.appbar = ft.AppBar(
            leading=ft.IconButton(
                ft.Icons.ARROW_BACK,
                on_click=lambda e: self.go_back_to_trigonometry_main(page)
            ),
            title=ft.Text("Trigonometry Examples"),
            bgcolor=ft.Colors.PURPLE_700,
            center_title=True
        )
        
        examples = [
            {
                "title": "Finding Missing Side Using Sine",
                "problem": "In a right triangle, if the hypotenuse is 10 and one angle is 30°, find the opposite side.",
                "solution": [
                    "Given: Hypotenuse = 10, Angle = 30°",
                    "We need: Opposite side",
                    "Formula: sin θ = opposite/hypotenuse",
                    "Calculation: sin 30° = opposite/10",
                    "Since sin 30° = 1/2: 1/2 = opposite/10",
                    "Therefore: opposite = 10 × 1/2 = 5",
                    "Answer: The opposite side is 5 units"
                ]
            },
            {
                "title": "Using Cosine to Find Adjacent Side",
                "problem": "In a right triangle with hypotenuse 8 and angle 60°, find the adjacent side.",
                "solution": [
                    "Given: Hypotenuse = 8, Angle = 60°",
                    "We need: Adjacent side",
                    "Formula: cos θ = adjacent/hypotenuse",
                    "Calculation: cos 60° = adjacent/8",
                    "Since cos 60° = 1/2: 1/2 = adjacent/8",
                    "Therefore: adjacent = 8 × 1/2 = 4",
                    "Answer: The adjacent side is 4 units"
                ]
            },
            {
                "title": "Finding Angle Using Inverse Trig",
                "problem": "In a right triangle, if opposite = 3 and adjacent = 4, find the angle θ.",
                "solution": [
                    "Given: Opposite = 3, Adjacent = 4",
                    "We need: Angle θ",
                    "Formula: tan θ = opposite/adjacent",
                    "Calculation: tan θ = 3/4 = 0.75",
                    "To find θ: θ = arctan(0.75)",
                    "Using calculator: θ ≈ 36.87°",
                    "Answer: The angle is approximately 36.87°"
                ]
            }
        ]
        
        example_cards = []
        for i, example in enumerate(examples):
            solution_steps = []
            for step in example["solution"]:
                solution_steps.append(ft.Text(step, size=12))
                
            example_cards.append(
                ft.Container(
                    ft.Column([
                        ft.Text(f"Example {i+1}: {example['title']}", 
                               size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_900),
                        ft.Container(
                            ft.Text(example["problem"], size=14, style=ft.TextStyle(italic=True)),
                            bgcolor=ft.Colors.PURPLE_50,
                            padding=15,
                            border_radius=8,
                            margin=ft.margin.only(top=10, bottom=10)
                        ),
                        ft.Text("Solution:", size=14, weight=ft.FontWeight.BOLD),
                        ft.Column(solution_steps, spacing=5)
                    ], spacing=10),
                    bgcolor=ft.Colors.GREY_50,
                    border_radius=10,
                    padding=20,
                    margin=ft.margin.only(bottom=20)
                )
            )
        
        content = ft.Container(
            ft.Column([
                ft.Text(
                    "📝 Worked Examples",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.PURPLE_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Text(
                    "Step-by-step solutions to common trigonometry problems",
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


def trigonometry_page(page: ft.Page):
    """Main entry point for Trigonometry module"""
    module = TrigonometryModule()
    module.show_main_page(page)
