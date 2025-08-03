import flet as ft
import random
import math

class GeometryModule:
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
        """Show the main geometry page
        Args:
            page: Optional page reference. If not provided, uses self.page
        """
        if page is None:
            page = self.page
        self.page = page  # Update the page reference
            
        view = ft.View(
            "/geometry",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: page.go_back()),
                    title=ft.Text("Geometry"),
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
            "basic_shapes": {
                "title": "Basic Shapes",
                "content": [
                    "Geometry studies shapes, sizes, positions, angles, and dimensions of objects.",
                    "Basic 2D shapes include circles, triangles, squares, rectangles, and polygons.",
                    "Each shape has unique properties and formulas for area and perimeter.",
                ]
            },
            "triangles": {
                "title": "Triangles",
                "content": [
                    "A triangle has three sides and three angles that sum to 180°.",
                    "Types: Equilateral (all sides equal), Isosceles (two sides equal), Scalene (all sides different).",
                    "Area = (1/2) × base × height",
                    "Perimeter = sum of all three sides"
                ]
            },
            "circles": {
                "title": "Circles",
                "content": [
                    "A circle is a set of points equidistant from a center point.",
                    "Radius (r): distance from center to edge",
                    "Diameter (d): distance across circle through center, d = 2r",
                    "Circumference = 2πr or πd",
                    "Area = πr²"
                ]
            },
            "rectangles": {
                "title": "Rectangles and Squares",
                "content": [
                    "Rectangle: four sides with opposite sides equal and four right angles",
                    "Square: special rectangle with all sides equal",
                    "Rectangle Area = length × width",
                    "Rectangle Perimeter = 2(length + width)",
                    "Square Area = side²",
                    "Square Perimeter = 4 × side"
                ]
            }
        }
        
    def geometry_page(self, page: ft.Page):
        """Main Geometry learning page"""
        page.title = "Geometry - Mathematics Learning"
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
            title=ft.Text("Geometry"),
            bgcolor=ft.Colors.BLUE_700,
            center_title=True
        )
        
        # Main content
        content = ft.Container(
            ft.Column([
                ft.Text(
                    "� Geometry",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Text(
                    "Master the fundamentals of shapes, angles, and spatial relationships",
                    size=16,
                    color=ft.Colors.BLUE_700,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Divider(height=30),
                
                # Learning sections
                ft.Container(
                    ft.Column([
                        ft.Text("🎯 Learning Objectives", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                        ft.Text("• Understand basic geometric shapes and properties", size=14),
                        ft.Text("• Calculate areas and perimeters of different shapes", size=14),
                        ft.Text("• Work with angles and their relationships", size=14),
                        ft.Text("• Apply geometric principles to real-world problems", size=14),
                        ft.Text("• Develop spatial visualization skills", size=14),
                    ], spacing=10),
                    bgcolor=ft.Colors.BLUE_50,
                    border_radius=10,
                padding=20,
                margin=ft.margin.only(bottom=20)
            ),
            
            # Action buttons
            ft.ResponsiveRow([
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.BOOK, size=30, color=ft.Colors.BLUE_700),
                            ft.Text("Learn", size=14, weight=ft.FontWeight.BOLD)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=20,
                            bgcolor=ft.Colors.BLUE_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: self.show_learning_content(page)
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 3}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.QUIZ, size=30, color=ft.Colors.BLUE_700),
                            ft.Text("Practice Quiz", size=14, weight=ft.FontWeight.BOLD)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=20,
                            bgcolor=ft.Colors.BLUE_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: self.show_practice_quiz(page)
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 3}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.QUIZ, size=30, color=ft.Colors.BLUE_700),
                            ft.Text("Practice Quiz", size=14, weight=ft.FontWeight.BOLD)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=20,
                            bgcolor=ft.Colors.BLUE_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: self.show_practice_quiz(page)
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.HELP_OUTLINE, size=30, color=ft.Colors.BLUE_700),
                            ft.Text("AI Help", size=14, weight=ft.FontWeight.BOLD)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=20,
                            bgcolor=ft.Colors.BLUE_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: self.show_ai_help(page)
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 3}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.LIGHTBULB_OUTLINE, size=30, color=ft.Colors.BLUE_700),
                            ft.Text("Examples", size=14, weight=ft.FontWeight.BOLD)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=20,
                            bgcolor=ft.Colors.BLUE_50,
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
                    ft.Text(f"Welcome to Geometry Learning!", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text(f"This is where you'll learn about Geometry concepts. Click the buttons above to get started with practice quizzes, help, or see examples.", size=14),
                    ft.Text("✨ Features:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                    ft.Text(f"• Interactive learning for Geometry", size=14),
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
        
    def go_back_to_geometry_main(self, page: ft.Page):
        """Navigate back to geometry main page"""
        self.geometry_page(page)
        
    def show_learning_content(self, page: ft.Page):
        """Display comprehensive learning content"""
        page.clean()
        
        # AppBar with back button
        page.appbar = ft.AppBar(
            leading=ft.IconButton(
                ft.Icons.ARROW_BACK,
                on_click=lambda e: self.go_back_to_geometry_main(page)
            ),
            title=ft.Text("Geometry Learning Content"),
            bgcolor=ft.Colors.BLUE_700,
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
                        bgcolor=ft.Colors.BLUE_50 if i % 2 == 0 else ft.Colors.WHITE,
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
                    "📐 Geometry Learning Content",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE_900,
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
                    "question": "What is the area of a rectangle with length 8 and width 5?",
                    "options": ["40", "26", "13", "32"],
                    "correct": 0,
                    "explanation": "Area of rectangle = length × width = 8 × 5 = 40"
                },
                {
                    "question": "How many degrees are in the sum of angles in a triangle?",
                    "options": ["90°", "180°", "270°", "360°"],
                    "correct": 1,
                    "explanation": "The sum of angles in any triangle is always 180°"
                },
                {
                    "question": "What is the perimeter of a square with side length 7?",
                    "options": ["14", "21", "28", "49"],
                    "correct": 2,
                    "explanation": "Perimeter of square = 4 × side = 4 × 7 = 28"
                },
                {
                    "question": "What is the circumference of a circle with radius 3? (Use π ≈ 3.14)",
                    "options": ["9.42", "18.84", "28.26", "6.28"],
                    "correct": 1,
                    "explanation": "Circumference = 2πr = 2 × 3.14 × 3 = 18.84"
                },
                {
                    "question": "What type of triangle has all sides equal?",
                    "options": ["Scalene", "Isosceles", "Equilateral", "Right"],
                    "correct": 2,
                    "explanation": "An equilateral triangle has all three sides equal in length"
                }
            ]
        elif difficulty == "intermediate":
            questions = [
                {
                    "question": "What is the area of a triangle with base 12 and height 8?",
                    "options": ["48", "96", "20", "32"],
                    "correct": 0,
                    "explanation": "Area of triangle = (1/2) × base × height = (1/2) × 12 × 8 = 48"
                },
                {
                    "question": "What is the area of a circle with radius 5? (Use π ≈ 3.14)",
                    "options": ["31.4", "78.5", "15.7", "157"],
                    "correct": 1,
                    "explanation": "Area of circle = πr² = 3.14 × 5² = 3.14 × 25 = 78.5"
                },
                {
                    "question": "In a right triangle, if one angle is 30°, what is the third angle?",
                    "options": ["60°", "90°", "120°", "150°"],
                    "correct": 0,
                    "explanation": "Sum of angles = 180°. We have 90° + 30° + x = 180°, so x = 60°"
                },
                {
                    "question": "What is the diagonal of a rectangle with length 9 and width 12?",
                    "options": ["15", "21", "18", "27"],
                    "correct": 0,
                    "explanation": "Using Pythagorean theorem: d² = 9² + 12² = 81 + 144 = 225, so d = 15"
                },
                {
                    "question": "What is the area of a parallelogram with base 10 and height 6?",
                    "options": ["30", "60", "16", "32"],
                    "correct": 1,
                    "explanation": "Area of parallelogram = base × height = 10 × 6 = 60"
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
                on_click=lambda e: self.go_back_to_geometry_main(page)
            ),
            title=ft.Text("Geometry Practice Quiz"),
            bgcolor=ft.Colors.BLUE_700,
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
                    color=ft.Colors.BLUE_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Text(
                    "Test your geometry knowledge with interactive questions",
                    size=16,
                    color=ft.Colors.BLUE_700,
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
                                bgcolor=ft.Colors.BLUE_600,
                                color=ft.Colors.WHITE,
                                padding=20
                            ),
                            on_click=start_quiz
                        )
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20),
                    bgcolor=ft.Colors.BLUE_50,
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
            bgcolor=ft.Colors.BLUE_700,
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
                        bgcolor=ft.Colors.BLUE_50,
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
                    color=ft.Colors.BLUE_900
                ),
                ft.Container(
                    ft.Text(
                        current_question["question"],
                        size=16,
                        text_align=ft.TextAlign.CENTER
                    ),
                    bgcolor=ft.Colors.BLUE_50,
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
            bgcolor=ft.Colors.BLUE_700,
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
                        bgcolor=ft.Colors.BLUE_600,
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
                on_click=lambda e: self.go_back_to_geometry_main(page)
            ),
            title=ft.Text("Quiz Results"),
            bgcolor=ft.Colors.BLUE_700,
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
                    color=ft.Colors.BLUE_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Container(
                    ft.Column([
                        ft.Text(f"Score: {self.quiz_score}/{total_questions}", size=24, weight=ft.FontWeight.BOLD),
                        ft.Text(f"Percentage: {percentage:.1f}%", size=20),
                        ft.Text(performance_text, size=18, color=performance_color, weight=ft.FontWeight.BOLD)
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
                    bgcolor=ft.Colors.BLUE_50,
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
                            bgcolor=ft.Colors.BLUE_600,
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
                        on_click=lambda e: self.go_back_to_geometry_main(page)
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
                on_click=lambda e: self.go_back_to_geometry_main(page)
            ),
            title=ft.Text("AI Help - Geometry"),
            bgcolor=ft.Colors.BLUE_700,
            center_title=True
        )
        
        # Help topics
        help_topics = [
            {
                "title": "📐 Basic Shapes",
                "description": "Learn about circles, triangles, rectangles, and their properties",
                "icon": ft.Icons.CIRCLE_OUTLINED
            },
            {
                "title": "📏 Area & Perimeter",
                "description": "Calculate areas and perimeters of different geometric shapes",
                "icon": ft.Icons.SQUARE_FOOT
            },
            {
                "title": "📐 Angles",
                "description": "Understand angle relationships and calculations",
                "icon": ft.Icons.ROTATE_RIGHT
            },
            {
                "title": "🧮 Problem Solving",
                "description": "Step-by-step help with geometry word problems",
                "icon": ft.Icons.LIGHTBULB_OUTLINE
            }
        ]
        
        help_cards = []
        for topic in help_topics:
            help_cards.append(
                ft.Container(
                    ft.ListTile(
                        leading=ft.Icon(topic["icon"], size=30, color=ft.Colors.BLUE_700),
                        title=ft.Text(topic["title"], weight=ft.FontWeight.BOLD),
                        subtitle=ft.Text(topic["description"]),
                        on_click=lambda e, t=topic["title"]: self.show_specific_help(page, t)
                    ),
                    bgcolor=ft.Colors.BLUE_50,
                    border_radius=10,
                    margin=ft.margin.only(bottom=10)
                )
            )
        
        content = ft.Container(
            ft.Column([
                ft.Text(
                    "🤖 AI Geometry Helper",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Text(
                    "Get personalized help with geometry concepts and problems",
                    size=16,
                    color=ft.Colors.BLUE_700,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Divider(height=30),
                
                ft.Column(help_cards, spacing=10),
                
                ft.Container(
                    ft.Column([
                        ft.Text("💡 Quick Tips:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                        ft.Text("• Draw diagrams to visualize problems", size=14),
                        ft.Text("• Label all known measurements", size=14),
                        ft.Text("• Choose the right formula for the shape", size=14),
                        ft.Text("• Double-check your calculations", size=14),
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
            bgcolor=ft.Colors.BLUE_100
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
                on_click=lambda e: self.go_back_to_geometry_main(page)
            ),
            title=ft.Text("Geometry Examples"),
            bgcolor=ft.Colors.BLUE_700,
            center_title=True
        )
        
        examples = [
            {
                "title": "Rectangle Area Calculation",
                "problem": "Find the area of a rectangle with length 12 cm and width 8 cm.",
                "solution": [
                    "Given: Length = 12 cm, Width = 8 cm",
                    "Formula: Area = Length × Width",
                    "Calculation: Area = 12 × 8 = 96 cm²",
                    "Answer: The area is 96 cm²"
                ]
            },
            {
                "title": "Circle Circumference",
                "problem": "Find the circumference of a circle with radius 5 cm. (Use π = 3.14)",
                "solution": [
                    "Given: Radius = 5 cm, π = 3.14",
                    "Formula: Circumference = 2πr",
                    "Calculation: C = 2 × 3.14 × 5 = 31.4 cm",
                    "Answer: The circumference is 31.4 cm"
                ]
            },
            {
                "title": "Triangle Area",
                "problem": "Find the area of a triangle with base 10 cm and height 6 cm.",
                "solution": [
                    "Given: Base = 10 cm, Height = 6 cm",
                    "Formula: Area = (1/2) × Base × Height",
                    "Calculation: Area = (1/2) × 10 × 6 = 30 cm²",
                    "Answer: The area is 30 cm²"
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
                               size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                        ft.Container(
                            ft.Text(example["problem"], size=14, style=ft.TextStyle(italic=True)),
                            bgcolor=ft.Colors.BLUE_50,
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
                    color=ft.Colors.BLUE_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Text(
                    "Step-by-step solutions to common geometry problems",
                    size=16,
                    color=ft.Colors.BLUE_700,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Divider(height=20),
                
                ft.Column(example_cards, spacing=10, scroll=ft.ScrollMode.AUTO)
            ], spacing=20),
            padding=20,
            expand=True
        )
        
        page.add(content)


def geometry_page(page: ft.Page):
    """Main entry point for Geometry module"""
    module = GeometryModule()
    module.show_main_page(page)
