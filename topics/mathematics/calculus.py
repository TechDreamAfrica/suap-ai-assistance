import flet as ft
import random
import math

class CalculusModule:
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
        """Show the main calculus page
        Args:
            page: Optional page reference. If not provided, uses self.page
        """
        if page is None:
            page = self.page
        self.page = page  # Update the page reference
            
        view = ft.View(
            "/calculus",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: page.go_back()),
                    title=ft.Text("Calculus"),
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
            "limits": {
                "title": "Limits",
                "content": [
                    "A limit describes the value a function approaches as input approaches some value.",
                    "Notation: lim(x→a) f(x) = L means f(x) approaches L as x approaches a",
                    "Limits can exist even when the function is undefined at that point",
                    "Key limit laws: lim(f + g) = lim f + lim g, lim(fg) = (lim f)(lim g)",
                    "Special limits: lim(x→0) sin(x)/x = 1, lim(x→∞) (1 + 1/x)^x = e"
                ]
            },
            "derivatives": {
                "title": "Derivatives", 
                "content": [
                    "The derivative measures the rate of change of a function",
                    "Definition: f'(x) = lim(h→0) [f(x+h) - f(x)]/h",
                    "Geometric interpretation: slope of tangent line at a point",
                    "Power rule: d/dx(x^n) = nx^(n-1)",
                    "Product rule: d/dx(fg) = f'g + fg'",
                    "Chain rule: d/dx[f(g(x))] = f'(g(x)) · g'(x)"
                ]
            },
            "integrals": {
                "title": "Integrals",
                "content": [
                    "Integration is the reverse process of differentiation",
                    "Definite integral: ∫[a to b] f(x)dx represents area under curve",
                    "Indefinite integral: ∫f(x)dx = F(x) + C where F'(x) = f(x)",
                    "Fundamental Theorem: ∫[a to b] f(x)dx = F(b) - F(a)",
                    "Basic integrals: ∫x^n dx = x^(n+1)/(n+1) + C (n ≠ -1)",
                    "∫1/x dx = ln|x| + C, ∫e^x dx = e^x + C"
                ]
            },
            "applications": {
                "title": "Applications",
                "content": [
                    "Derivatives help find maximum and minimum values",
                    "Critical points occur where f'(x) = 0 or f'(x) is undefined",
                    "Second derivative test: f''(x) > 0 means concave up, f''(x) < 0 means concave down",
                    "Integrals calculate area, volume, and accumulation",
                    "Related rates problems use chain rule with implicit differentiation",
                    "Optimization problems use derivatives to find extrema"
                ]
            }
        }
        
    def calculus_page(self, page: ft.Page):
        """Main Calculus learning page"""
        page.title = "Calculus - Mathematics Learning"
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
            title=ft.Text("Calculus"),
            bgcolor=ft.Colors.GREEN_700,
            center_title=True
        )
        
        # Main content
        content = ft.Container(
            ft.Column([
                ft.Text(
                    "∫ Calculus",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.GREEN_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Text(
                    "Master the mathematics of change and motion",
                    size=16,
                    color=ft.Colors.GREEN_700,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Divider(height=30),
                
                # Learning sections
                ft.Container(
                    ft.Column([
                        ft.Text("🎯 Learning Objectives", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_900),
                        ft.Text("• Understand limits and continuity", size=14),
                        ft.Text("• Master derivatives and differentiation rules", size=14),
                        ft.Text("• Learn integration techniques and applications", size=14),
                        ft.Text("• Apply calculus to solve real-world problems", size=14),
                        ft.Text("• Develop analytical thinking skills", size=14),
                    ], spacing=10),
                    bgcolor=ft.Colors.GREEN_50,
                    border_radius=10,
                    padding=20,
                    margin=ft.margin.only(bottom=20)
                ),
                
                # Action buttons
                ft.ResponsiveRow([
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.BOOK, size=30, color=ft.Colors.GREEN_700),
                                ft.Text("Learn", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            style=ft.ButtonStyle(
                                padding=20,
                                bgcolor=ft.Colors.GREEN_50,
                                shape=ft.RoundedRectangleBorder(radius=10)
                            ),
                            on_click=lambda e: self.show_learning_content(page)
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.QUIZ, size=30, color=ft.Colors.GREEN_700),
                                ft.Text("Practice Quiz", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            style=ft.ButtonStyle(
                                padding=20,
                                bgcolor=ft.Colors.GREEN_50,
                                shape=ft.RoundedRectangleBorder(radius=10)
                            ),
                            on_click=lambda e: self.show_practice_quiz(page)
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.HELP_OUTLINE, size=30, color=ft.Colors.GREEN_700),
                                ft.Text("AI Help", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            style=ft.ButtonStyle(
                                padding=20,
                                bgcolor=ft.Colors.GREEN_50,
                                shape=ft.RoundedRectangleBorder(radius=10)
                            ),
                            on_click=lambda e: self.show_ai_help(page)
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.LIGHTBULB_OUTLINE, size=30, color=ft.Colors.GREEN_700),
                                ft.Text("Examples", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            style=ft.ButtonStyle(
                                padding=20,
                                bgcolor=ft.Colors.GREEN_50,
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
                        ft.Text("Welcome to Calculus Learning!", size=18, weight=ft.FontWeight.BOLD),
                        ft.Text("This is where you'll learn about calculus concepts. Click the buttons above to get started with learning content, practice quizzes, AI help, or see examples.", size=14),
                        ft.Text("✨ Features:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_900),
                        ft.Text("• Interactive learning for calculus", size=14),
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
        
    def go_back_to_calculus_main(self, page: ft.Page):
        """Navigate back to calculus main page"""
        self.calculus_page(page)
        
    def show_learning_content(self, page: ft.Page):
        """Display comprehensive learning content"""
        page.clean()
        
        # AppBar with back button
        page.appbar = ft.AppBar(
            leading=ft.IconButton(
                ft.Icons.ARROW_BACK,
                on_click=lambda e: self.go_back_to_calculus_main(page)
            ),
            title=ft.Text("Calculus Learning Content"),
            bgcolor=ft.Colors.GREEN_700,
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
                        bgcolor=ft.Colors.GREEN_50 if i % 2 == 0 else ft.Colors.WHITE,
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
                    "∫ Calculus Learning Content",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.GREEN_900,
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
                    "question": "What is the derivative of x²?",
                    "options": ["x", "2x", "x²", "2"],
                    "correct": 1,
                    "explanation": "Using the power rule: d/dx(x²) = 2x^(2-1) = 2x"
                },
                {
                    "question": "What is ∫x dx?",
                    "options": ["x²/2 + C", "x² + C", "1 + C", "x + C"],
                    "correct": 0,
                    "explanation": "∫x dx = x^(1+1)/(1+1) + C = x²/2 + C"
                },
                {
                    "question": "What is lim(x→0) sin(x)/x?",
                    "options": ["0", "1", "∞", "undefined"],
                    "correct": 1,
                    "explanation": "This is a standard limit: lim(x→0) sin(x)/x = 1"
                },
                {
                    "question": "What is the derivative of e^x?",
                    "options": ["e^x", "xe^x", "e^x/x", "1"],
                    "correct": 0,
                    "explanation": "The derivative of e^x is itself: d/dx(e^x) = e^x"
                },
                {
                    "question": "If f(x) = x³, what is f'(2)?",
                    "options": ["6", "8", "12", "3"],
                    "correct": 2,
                    "explanation": "f'(x) = 3x², so f'(2) = 3(2)² = 3(4) = 12"
                }
            ]
        elif difficulty == "intermediate":
            questions = [
                {
                    "question": "What is the derivative of ln(x²)?",
                    "options": ["1/x", "2/x", "2x", "x/2"],
                    "correct": 1,
                    "explanation": "Using chain rule: d/dx[ln(x²)] = (1/x²) · 2x = 2/x"
                },
                {
                    "question": "What is ∫x·e^x dx?",
                    "options": ["e^x + C", "x·e^x + C", "(x-1)e^x + C", "x²e^x/2 + C"],
                    "correct": 2,
                    "explanation": "Using integration by parts: ∫x·e^x dx = x·e^x - ∫e^x dx = x·e^x - e^x + C = (x-1)e^x + C"
                },
                {
                    "question": "If f(x) = x² + 3x - 2, where does f'(x) = 0?",
                    "options": ["x = -3/2", "x = 3/2", "x = -2", "x = 2"],
                    "correct": 0,
                    "explanation": "f'(x) = 2x + 3 = 0, so x = -3/2"
                },
                {
                    "question": "What is lim(x→∞) (1 + 1/x)^x?",
                    "options": ["1", "e", "∞", "0"],
                    "correct": 1,
                    "explanation": "This is the definition of e: lim(x→∞) (1 + 1/x)^x = e ≈ 2.718"
                },
                {
                    "question": "What is the second derivative of sin(x)?",
                    "options": ["cos(x)", "-cos(x)", "sin(x)", "-sin(x)"],
                    "correct": 3,
                    "explanation": "d/dx[sin(x)] = cos(x), and d/dx[cos(x)] = -sin(x)"
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
                on_click=lambda e: self.go_back_to_calculus_main(page)
            ),
            title=ft.Text("Calculus Practice Quiz"),
            bgcolor=ft.Colors.GREEN_700,
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
                    color=ft.Colors.GREEN_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Text(
                    "Test your calculus knowledge with interactive questions",
                    size=16,
                    color=ft.Colors.GREEN_700,
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
                                bgcolor=ft.Colors.GREEN_600,
                                color=ft.Colors.WHITE,
                                padding=20
                            ),
                            on_click=start_quiz
                        )
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20),
                    bgcolor=ft.Colors.GREEN_50,
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
            bgcolor=ft.Colors.GREEN_700,
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
                        bgcolor=ft.Colors.GREEN_50,
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
                    color=ft.Colors.GREEN_900
                ),
                ft.Container(
                    ft.Text(
                        current_question["question"],
                        size=16,
                        text_align=ft.TextAlign.CENTER
                    ),
                    bgcolor=ft.Colors.GREEN_50,
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
            bgcolor=ft.Colors.GREEN_700,
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
                        bgcolor=ft.Colors.GREEN_600,
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
                on_click=lambda e: self.go_back_to_calculus_main(page)
            ),
            title=ft.Text("Quiz Results"),
            bgcolor=ft.Colors.GREEN_700,
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
                    color=ft.Colors.GREEN_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Container(
                    ft.Column([
                        ft.Text(f"Score: {self.quiz_score}/{total_questions}", size=24, weight=ft.FontWeight.BOLD),
                        ft.Text(f"Percentage: {percentage:.1f}%", size=20),
                        ft.Text(performance_text, size=18, color=performance_color, weight=ft.FontWeight.BOLD)
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
                    bgcolor=ft.Colors.GREEN_50,
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
                            bgcolor=ft.Colors.GREEN_600,
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
                        on_click=lambda e: self.go_back_to_calculus_main(page)
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
                on_click=lambda e: self.go_back_to_calculus_main(page)
            ),
            title=ft.Text("AI Help - Calculus"),
            bgcolor=ft.Colors.GREEN_700,
            center_title=True
        )
        
        # Help topics
        help_topics = [
            {
                "title": "📈 Limits & Continuity",
                "description": "Understanding limits and continuous functions",
                "icon": ft.Icons.TRENDING_UP
            },
            {
                "title": "📉 Derivatives",
                "description": "Learn differentiation rules and applications",
                "icon": ft.Icons.SHOW_CHART
            },
            {
                "title": "∫ Integration",
                "description": "Master integration techniques and applications",
                "icon": ft.Icons.AREA_CHART
            },
            {
                "title": "🎯 Applications",
                "description": "Real-world calculus problem solving",
                "icon": ft.Icons.TARGET
            }
        ]
        
        help_cards = []
        for topic in help_topics:
            help_cards.append(
                ft.Container(
                    ft.ListTile(
                        leading=ft.Icon(topic["icon"], size=30, color=ft.Colors.GREEN_700),
                        title=ft.Text(topic["title"], weight=ft.FontWeight.BOLD),
                        subtitle=ft.Text(topic["description"]),
                        on_click=lambda e, t=topic["title"]: self.show_specific_help(page, t)
                    ),
                    bgcolor=ft.Colors.GREEN_50,
                    border_radius=10,
                    margin=ft.margin.only(bottom=10)
                )
            )
        
        content = ft.Container(
            ft.Column([
                ft.Text(
                    "🤖 AI Calculus Helper",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.GREEN_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Text(
                    "Get personalized help with calculus concepts and problems",
                    size=16,
                    color=ft.Colors.GREEN_700,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Divider(height=30),
                
                ft.Column(help_cards, spacing=10),
                
                ft.Container(
                    ft.Column([
                        ft.Text("💡 Quick Tips:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_900),
                        ft.Text("• Start with limits before derivatives", size=14),
                        ft.Text("• Practice basic rules before complex problems", size=14),
                        ft.Text("• Use graphing to visualize concepts", size=14),
                        ft.Text("• Check your work by differentiating integrals", size=14),
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
            bgcolor=ft.Colors.GREEN_100
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
                on_click=lambda e: self.go_back_to_calculus_main(page)
            ),
            title=ft.Text("Calculus Examples"),
            bgcolor=ft.Colors.GREEN_700,
            center_title=True
        )
        
        examples = [
            {
                "title": "Finding Derivative Using Power Rule",
                "problem": "Find the derivative of f(x) = 3x⁴ - 2x² + 5x - 1",
                "solution": [
                    "Given: f(x) = 3x⁴ - 2x² + 5x - 1",
                    "Apply power rule to each term:",
                    "d/dx(3x⁴) = 3 · 4x³ = 12x³",
                    "d/dx(-2x²) = -2 · 2x = -4x",
                    "d/dx(5x) = 5 · 1 = 5",
                    "d/dx(-1) = 0 (constant rule)",
                    "Answer: f'(x) = 12x³ - 4x + 5"
                ]
            },
            {
                "title": "Evaluating a Definite Integral",
                "problem": "Evaluate ∫[0 to 2] (x² + 1) dx",
                "solution": [
                    "Given: ∫[0 to 2] (x² + 1) dx",
                    "Find antiderivative: ∫(x² + 1) dx = x³/3 + x + C",
                    "Apply Fundamental Theorem:",
                    "= [x³/3 + x]₀²",
                    "= (2³/3 + 2) - (0³/3 + 0)",
                    "= (8/3 + 2) - 0 = 8/3 + 6/3 = 14/3",
                    "Answer: 14/3 ≈ 4.67"
                ]
            },
            {
                "title": "Finding Critical Points",
                "problem": "Find critical points of f(x) = x³ - 6x² + 9x + 1",
                "solution": [
                    "Given: f(x) = x³ - 6x² + 9x + 1",
                    "Find derivative: f'(x) = 3x² - 12x + 9",
                    "Set f'(x) = 0: 3x² - 12x + 9 = 0",
                    "Divide by 3: x² - 4x + 3 = 0",
                    "Factor: (x - 1)(x - 3) = 0",
                    "Solve: x = 1 or x = 3",
                    "Answer: Critical points at x = 1 and x = 3"
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
                               size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_900),
                        ft.Container(
                            ft.Text(example["problem"], size=14, style=ft.TextStyle(italic=True)),
                            bgcolor=ft.Colors.GREEN_50,
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
                    color=ft.Colors.GREEN_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Text(
                    "Step-by-step solutions to common calculus problems",
                    size=16,
                    color=ft.Colors.GREEN_700,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Divider(height=20),
                
                ft.Column(example_cards, spacing=10, scroll=ft.ScrollMode.AUTO)
            ], spacing=20),
            padding=20,
            expand=True
        )
        
        page.add(content)


def calculus_page(page: ft.Page):
    """Main entry point for Calculus module"""
    module = CalculusModule()
    module.show_main_page(page)
