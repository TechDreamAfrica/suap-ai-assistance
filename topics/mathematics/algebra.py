import flet as ft
import random
import math

class AlgebraModule:
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
        """Show the main algebra page
        Args:
            page: Optional page reference. If not provided, uses self.page
        """
        if page is None:
            page = self.page
        self.page = page  # Update the page reference
            
        view = ft.View(
            "/algebra",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: page.go_back()),
                    title=ft.Text("Algebra"),
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
            "variables": {
                "title": "Variables and Expressions",
                "content": [
                    "A variable is a letter that represents an unknown number.",
                    "Common variables are x, y, n, and a. Example: x + 5",
                    "An algebraic expression combines numbers and variables using operations.",
                    "Terms are parts of an expression separated by + or - signs.",
                    "Like terms have the same variable part (3x and 5x are like terms).",
                    "To simplify expressions, combine like terms: 3x + 5x = 8x"
                ]
            },
            "equations": {
                "title": "Solving Linear Equations",
                "content": [
                    "An equation states that two expressions are equal.",
                    "To solve an equation, isolate the variable on one side.",
                    "What you do to one side, you must do to the other side.",
                    "Addition/Subtraction: x + 3 = 7 → x = 7 - 3 → x = 4",
                    "Multiplication/Division: 3x = 12 → x = 12 ÷ 3 → x = 4",
                    "Check your answer by substituting back into the original equation."
                ]
            },
            "inequalities": {
                "title": "Inequalities",
                "content": [
                    "Inequalities compare two expressions using <, >, ≤, or ≥.",
                    "Solve inequalities the same way as equations.",
                    "When multiplying or dividing by a negative number, flip the inequality sign.",
                    "x + 2 > 5 → x > 3 means x can be any number greater than 3.",
                    "Graph solutions on a number line using open or closed circles.",
                    "Compound inequalities involve 'and' or 'or' conditions."
                ]
            },
            "functions": {
                "title": "Functions and Graphing",
                "content": [
                    "A function is a rule that assigns each input exactly one output.",
                    "Function notation: f(x) = 2x + 1 means 'f of x equals 2x plus 1'.",
                    "The domain is all possible input values (x-values).",
                    "The range is all possible output values (y-values).",
                    "Linear functions have the form y = mx + b, where m is slope and b is y-intercept.",
                    "Slope = rise/run = (y₂ - y₁)/(x₂ - x₁)"
                ]
            }
        }
        
    def algebra_page(self, page: ft.Page):
        """Main Algebra learning page"""
        page.title = "Algebra - Mathematics Learning"
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
            title=ft.Text("Algebra"),
            bgcolor=ft.Colors.RED_700,
            center_title=True
        )
        
        # Main content
        content = ft.Container(
            ft.Column([
                ft.Text(
                    "� Algebra",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.RED_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Text(
                    "Master variables, equations, and mathematical relationships",
                    size=16,
                    color=ft.Colors.RED_700,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Divider(height=30),
                
                # Learning sections
                ft.Container(
                    ft.Column([
                        ft.Text("🎯 Learning Objectives", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.RED_900),
                        ft.Text("• Understand variables and algebraic expressions", size=14),
                        ft.Text("• Solve linear equations and inequalities", size=14),
                        ft.Text("• Work with functions and their graphs", size=14),
                        ft.Text("• Apply algebraic thinking to problem solving", size=14),
                        ft.Text("• Build foundation for advanced mathematics", size=14),
                    ], spacing=10),
                    bgcolor=ft.Colors.RED_50,
                    border_radius=10,
                    padding=20,
                    margin=ft.margin.only(bottom=20)
                ),
                
                # Action buttons
                ft.ResponsiveRow([
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.BOOK, size=30, color=ft.Colors.RED_700),
                                ft.Text("Learn", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            style=ft.ButtonStyle(
                                padding=20,
                                bgcolor=ft.Colors.RED_50,
                                shape=ft.RoundedRectangleBorder(radius=10)
                            ),
                            on_click=lambda e: self.show_learning_content(page)
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.QUIZ, size=30, color=ft.Colors.RED_700),
                                ft.Text("Practice Quiz", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            style=ft.ButtonStyle(
                                padding=20,
                                bgcolor=ft.Colors.RED_50,
                                shape=ft.RoundedRectangleBorder(radius=10)
                            ),
                            on_click=lambda e: self.show_practice_quiz(page)
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.HELP_OUTLINE, size=30, color=ft.Colors.RED_700),
                                ft.Text("AI Help", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            style=ft.ButtonStyle(
                                padding=20,
                                bgcolor=ft.Colors.RED_50,
                                shape=ft.RoundedRectangleBorder(radius=10)
                            ),
                            on_click=lambda e: self.show_ai_help(page)
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.LIGHTBULB_OUTLINE, size=30, color=ft.Colors.RED_700),
                                ft.Text("Examples", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            style=ft.ButtonStyle(
                                padding=20,
                                bgcolor=ft.Colors.RED_50,
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
                        ft.Text("Welcome to Algebra Learning!", size=18, weight=ft.FontWeight.BOLD),
                        ft.Text("This is where you'll learn about algebra concepts. Click the buttons above to get started with learning content, practice quizzes, AI help, or see examples.", size=14),
                        ft.Text("✨ Features:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.RED_900),
                        ft.Text("• Interactive learning for algebra", size=14),
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
        
    def go_back_to_algebra_main(self, page: ft.Page):
        """Navigate back to algebra main page"""
        self.algebra_page(page)
        
    def show_learning_content(self, page: ft.Page):
        """Display comprehensive learning content"""
        page.clean()
        
        # AppBar with back button
        page.appbar = ft.AppBar(
            leading=ft.IconButton(
                ft.Icons.ARROW_BACK,
                on_click=lambda e: self.go_back_to_algebra_main(page)
            ),
            title=ft.Text("Algebra Learning Content"),
            bgcolor=ft.Colors.RED_700,
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
                        bgcolor=ft.Colors.RED_50 if i % 2 == 0 else ft.Colors.WHITE,
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
                    "🔢 Algebra Learning Content",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.RED_900,
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
                    "question": "If x + 3 = 7, what is x?",
                    "options": ["4", "3", "10", "7"],
                    "correct": 0,
                    "explanation": "x + 3 = 7. Subtract 3 from both sides: x = 7 - 3 = 4"
                },
                {
                    "question": "Simplify: 3x + 2x",
                    "options": ["5x", "6x", "5x²", "6"],
                    "correct": 0,
                    "explanation": "3x + 2x = (3 + 2)x = 5x. Combine like terms."
                },
                {
                    "question": "If 2y = 10, what is y?",
                    "options": ["5", "20", "12", "8"],
                    "correct": 0,
                    "explanation": "2y = 10. Divide both sides by 2: y = 10 ÷ 2 = 5"
                },
                {
                    "question": "What is the coefficient of x in 7x + 3?",
                    "options": ["7", "3", "x", "10"],
                    "correct": 0,
                    "explanation": "The coefficient is the number multiplying the variable. In 7x, the coefficient is 7."
                },
                {
                    "question": "Evaluate 2x + 1 when x = 3",
                    "options": ["7", "6", "5", "8"],
                    "correct": 0,
                    "explanation": "Substitute x = 3: 2(3) + 1 = 6 + 1 = 7"
                }
            ]
        elif difficulty == "intermediate":
            questions = [
                {
                    "question": "Solve: 3x - 4 = 11",
                    "options": ["5", "15", "7", "3"],
                    "correct": 0,
                    "explanation": "3x - 4 = 11. Add 4: 3x = 15. Divide by 3: x = 5"
                },
                {
                    "question": "If 2x + 3y = 12 and x = 3, what is y?",
                    "options": ["2", "3", "6", "1"],
                    "correct": 0,
                    "explanation": "2(3) + 3y = 12 → 6 + 3y = 12 → 3y = 6 → y = 2"
                },
                {
                    "question": "Solve the inequality: x + 5 > 8",
                    "options": ["x > 3", "x < 3", "x > 13", "x < 13"],
                    "correct": 0,
                    "explanation": "x + 5 > 8. Subtract 5 from both sides: x > 3"
                },
                {
                    "question": "What is the slope of the line y = 2x + 3?",
                    "options": ["2", "3", "2x", "5"],
                    "correct": 0,
                    "explanation": "In y = mx + b form, m is the slope. Here m = 2."
                },
                {
                    "question": "Factor: x² + 5x + 6",
                    "options": ["(x + 2)(x + 3)", "(x + 1)(x + 6)", "(x + 5)(x + 1)", "(x - 2)(x - 3)"],
                    "correct": 0,
                    "explanation": "Find two numbers that multiply to 6 and add to 5: 2 and 3. So (x + 2)(x + 3)."
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
                on_click=lambda e: self.go_back_to_algebra_main(page)
            ),
            title=ft.Text("Algebra Practice Quiz"),
            bgcolor=ft.Colors.RED_700,
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
                    color=ft.Colors.RED_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Text(
                    "Test your algebra knowledge with interactive questions",
                    size=16,
                    color=ft.Colors.RED_700,
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
                                bgcolor=ft.Colors.RED_600,
                                color=ft.Colors.WHITE,
                                padding=20
                            ),
                            on_click=start_quiz
                        )
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20),
                    bgcolor=ft.Colors.RED_50,
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
            bgcolor=ft.Colors.RED_700,
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
                        bgcolor=ft.Colors.RED_50,
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
                    color=ft.Colors.RED_900
                ),
                ft.Container(
                    ft.Text(
                        current_question["question"],
                        size=16,
                        text_align=ft.TextAlign.CENTER
                    ),
                    bgcolor=ft.Colors.RED_50,
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
            bgcolor=ft.Colors.RED_700,
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
                        bgcolor=ft.Colors.RED_600,
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
                on_click=lambda e: self.go_back_to_algebra_main(page)
            ),
            title=ft.Text("Quiz Results"),
            bgcolor=ft.Colors.RED_700,
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
                    color=ft.Colors.RED_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Container(
                    ft.Column([
                        ft.Text(f"Score: {self.quiz_score}/{total_questions}", size=24, weight=ft.FontWeight.BOLD),
                        ft.Text(f"Percentage: {percentage:.1f}%", size=20),
                        ft.Text(performance_text, size=18, color=performance_color, weight=ft.FontWeight.BOLD)
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
                    bgcolor=ft.Colors.RED_50,
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
                            bgcolor=ft.Colors.RED_600,
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
                        on_click=lambda e: self.go_back_to_algebra_main(page)
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
                on_click=lambda e: self.go_back_to_algebra_main(page)
            ),
            title=ft.Text("AI Help - Algebra"),
            bgcolor=ft.Colors.RED_700,
            center_title=True
        )
        
        # Help topics
        help_topics = [
            {
                "title": "🔢 Variables & Expressions",
                "description": "Learn about variables, terms, and algebraic expressions",
                "icon": ft.Icons.FUNCTIONS
            },
            {
                "title": "⚖️ Solving Equations",
                "description": "Master techniques for solving linear equations",
                "icon": ft.Icons.BALANCE
            },
            {
                "title": "📊 Inequalities",
                "description": "Understand and solve inequality problems",
                "icon": ft.Icons.COMPARE_ARROWS
            },
            {
                "title": "📈 Functions & Graphs",
                "description": "Explore functions and their graphical representations",
                "icon": ft.Icons.SHOW_CHART
            }
        ]
        
        help_cards = []
        for topic in help_topics:
            help_cards.append(
                ft.Container(
                    ft.ListTile(
                        leading=ft.Icon(topic["icon"], size=30, color=ft.Colors.RED_700),
                        title=ft.Text(topic["title"], weight=ft.FontWeight.BOLD),
                        subtitle=ft.Text(topic["description"]),
                        on_click=lambda e, t=topic["title"]: self.show_specific_help(page, t)
                    ),
                    bgcolor=ft.Colors.RED_50,
                    border_radius=10,
                    margin=ft.margin.only(bottom=10)
                )
            )
        
        content = ft.Container(
            ft.Column([
                ft.Text(
                    "🤖 AI Algebra Helper",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.RED_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Text(
                    "Get personalized help with algebra concepts and problems",
                    size=16,
                    color=ft.Colors.RED_700,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Divider(height=30),
                
                ft.Column(help_cards, spacing=10),
                
                ft.Container(
                    ft.Column([
                        ft.Text("💡 Quick Tips:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.RED_900),
                        ft.Text("• Always do the same operation to both sides of an equation", size=14),
                        ft.Text("• Combine like terms to simplify expressions", size=14),
                        ft.Text("• Check your answers by substituting back", size=14),
                        ft.Text("• Draw diagrams for word problems", size=14),
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
            bgcolor=ft.Colors.RED_100
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
                on_click=lambda e: self.go_back_to_algebra_main(page)
            ),
            title=ft.Text("Algebra Examples"),
            bgcolor=ft.Colors.RED_700,
            center_title=True
        )
        
        examples = [
            {
                "title": "Solving a Linear Equation",
                "problem": "Solve: 3x + 5 = 14",
                "solution": [
                    "Given: 3x + 5 = 14",
                    "Step 1: Subtract 5 from both sides",
                    "3x + 5 - 5 = 14 - 5",
                    "3x = 9",
                    "Step 2: Divide both sides by 3",
                    "x = 9 ÷ 3 = 3",
                    "Check: 3(3) + 5 = 9 + 5 = 14 ✓"
                ]
            },
            {
                "title": "Simplifying Expressions",
                "problem": "Simplify: 4x + 2y + 3x - y",
                "solution": [
                    "Given: 4x + 2y + 3x - y",
                    "Step 1: Group like terms",
                    "(4x + 3x) + (2y - y)",
                    "Step 2: Combine coefficients",
                    "7x + 1y",
                    "Step 3: Write final answer",
                    "Answer: 7x + y"
                ]
            },
            {
                "title": "Solving an Inequality",
                "problem": "Solve: 2x - 3 < 7",
                "solution": [
                    "Given: 2x - 3 < 7",
                    "Step 1: Add 3 to both sides",
                    "2x - 3 + 3 < 7 + 3",
                    "2x < 10",
                    "Step 2: Divide both sides by 2",
                    "x < 5",
                    "Answer: x can be any number less than 5"
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
                               size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.RED_900),
                        ft.Container(
                            ft.Text(example["problem"], size=14, style=ft.TextStyle(italic=True)),
                            bgcolor=ft.Colors.RED_50,
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
                    color=ft.Colors.RED_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Text(
                    "Step-by-step solutions to common algebra problems",
                    size=16,
                    color=ft.Colors.RED_700,
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


def algebra_page(page: ft.Page):
    """Main entry point for Algebra module"""
    module = AlgebraModule()
    module.show_main_page(page)
