import flet as ft
import random
import math


class LinearFunctionsModule:
    """Comprehensive Linear Functions learning module"""
    
    def __init__(self, page: ft.Page):
        self.page = page
        self.current_question = 0
        self.score = 0
        self.quiz_questions = self._generate_quiz_questions()
        self.selected_answer = None
        
    def show_page(self):
        """Main entry point for the module"""
        self.show_main_page()
        
    def show_main_page(self, page=None):
        """Show the main linear functions page
        Args:
            page: Optional page reference. If not provided, uses self.page
        """
        if page is None:
            page = self.page
        self.page = page  # Update the page reference
            
        view = ft.View(
            "/linear_functions",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: page.go_back()),
                    title=ft.Text("Linear Functions"),
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
        
        # AppBar with navigation
        self.page.appbar = ft.AppBar(
            leading=ft.IconButton(
                ft.Icons.ARROW_BACK,
                on_click=lambda e: self.page.go("/maths"),
                tooltip="Back to Mathematics"
            ),
            title=ft.Text("Linear Functions"),
            bgcolor=ft.Colors.BLUE_700,
            center_title=True
        )
        
        # Main content
        content = ft.Container(
            ft.Column([
                # Header
                ft.Container(
                    ft.Column([
                        ft.Text(
                            "📈 Linear Functions",
                            size=32,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.BLUE_900,
                            text_align=ft.TextAlign.CENTER
                        ),
                        ft.Text(
                            "Master linear equations, slopes, and graphing",
                            size=16,
                            color=ft.Colors.BLUE_700,
                            text_align=ft.TextAlign.CENTER
                        ),
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    bgcolor=ft.Colors.BLUE_50,
                    border_radius=15,
                    padding=20,
                    margin=ft.margin.only(bottom=20)
                ),
                
                # Learning objectives
                ft.Container(
                    ft.Column([
                        ft.Text("🎯 Learning Objectives", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                        ft.Text("• Understand slope-intercept form (y = mx + b)", size=14),
                        ft.Text("• Calculate slope from two points", size=14),
                        ft.Text("• Graph linear functions", size=14),
                        ft.Text("• Find x and y intercepts", size=14),
                        ft.Text("• Solve linear equations", size=14),
                        ft.Text("• Apply linear functions to real-world problems", size=14),
                    ], spacing=8),
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
                                ft.Icon(ft.Icons.SCHOOL, size=30, color=ft.Colors.BLUE_700),
                                ft.Text("Learn Concepts", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            style=ft.ButtonStyle(
                                padding=20,
                                bgcolor=ft.Colors.BLUE_50,
                                shape=ft.RoundedRectangleBorder(radius=10)
                            ),
                            on_click=lambda e: self.show_learning_content()
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
                            on_click=lambda e: self.show_quiz()
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.LIGHTBULB_OUTLINE, size=30, color=ft.Colors.ORANGE_700),
                                ft.Text("Examples", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            style=ft.ButtonStyle(
                                padding=20,
                                bgcolor=ft.Colors.ORANGE_50,
                                shape=ft.RoundedRectangleBorder(radius=10)
                            ),
                            on_click=lambda e: self.show_examples()
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
                            on_click=lambda e: self.show_ai_help()
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                ], spacing=15, run_spacing=15),
                
                ft.Divider(height=20),
                
                # Overview content
                ft.Container(
                    ft.Column([
                        ft.Text("📊 Linear Functions Overview", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                        ft.Text("Linear functions represent relationships where the change between variables is constant. They form straight lines when graphed and are fundamental to understanding algebraic relationships.", size=14),
                        
                        ft.Divider(height=10),
                        
                        ft.Text("🔑 Key Concepts:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_800),
                        ft.Text("• Slope-intercept form: y = mx + b", size=14),
                        ft.Text("• Slope (m): rate of change", size=14),
                        ft.Text("• Y-intercept (b): where line crosses y-axis", size=14),
                        ft.Text("• X-intercept: where line crosses x-axis", size=14),
                        
                        ft.Divider(height=10),
                        
                        ft.Text("🌟 Why Learn Linear Functions?", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_800),
                        ft.Text("• Model real-world relationships (speed, cost, growth)", size=14),
                        ft.Text("• Foundation for more advanced mathematics", size=14),
                        ft.Text("• Used in business, science, and engineering", size=14),
                        ft.Text("• Essential for data analysis and statistics", size=14),
                    ], spacing=10),
                    bgcolor=ft.Colors.GREY_50,
                    border_radius=10,
                    padding=20
                )
            ], spacing=20),
            padding=20,
            expand=True
        )
        
        self.page.add(content)
        self.page.update()
    
    def show_learning_content(self):
        """Display comprehensive learning content"""
        self.page.clean()
        
        content = ft.Container(
            ft.Column([
                # Header
                ft.Row([
                    ft.IconButton(
                        ft.Icons.ARROW_BACK,
                        on_click=lambda e: self.show_page(),
                        tooltip="Back to Linear Functions"
                    ),
                    ft.Text(
                        "📚 Linear Functions: Complete Guide",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLUE_900
                    )
                ], alignment=ft.MainAxisAlignment.START),
                
                ft.Divider(),
                
                # Content sections
                ft.Container(
                    ft.Column([
                        ft.Text("1. Understanding Linear Functions", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800),
                        ft.Text("A linear function is a mathematical relationship where one variable changes at a constant rate with respect to another variable. The general form is:", size=14),
                        ft.Container(
                            ft.Text("y = mx + b", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
                            bgcolor=ft.Colors.BLUE_50,
                            padding=10,
                            border_radius=5,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        ft.Text("Where:", size=14, weight=ft.FontWeight.BOLD),
                        ft.Text("• m = slope (rate of change)", size=14),
                        ft.Text("• b = y-intercept (value when x = 0)", size=14),
                        ft.Text("• x = independent variable", size=14),
                        ft.Text("• y = dependent variable", size=14),
                    ], spacing=8),
                    bgcolor=ft.Colors.WHITE,
                    border_radius=10,
                    padding=15,
                    margin=ft.margin.only(bottom=15)
                ),
                
                ft.Container(
                    ft.Column([
                        ft.Text("2. Understanding Slope", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_800),
                        ft.Text("Slope measures how steep a line is and the direction it goes. It's calculated as:", size=14),
                        ft.Container(
                            ft.Text("slope = (y₂ - y₁) / (x₂ - x₁)", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
                            bgcolor=ft.Colors.GREEN_50,
                            padding=10,
                            border_radius=5,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        ft.Text("Types of slopes:", size=14, weight=ft.FontWeight.BOLD),
                        ft.Text("• Positive slope: line goes up from left to right", size=14),
                        ft.Text("• Negative slope: line goes down from left to right", size=14),
                        ft.Text("• Zero slope: horizontal line", size=14),
                        ft.Text("• Undefined slope: vertical line", size=14),
                    ], spacing=8),
                    bgcolor=ft.Colors.WHITE,
                    border_radius=10,
                    padding=15,
                    margin=ft.margin.only(bottom=15)
                ),
                
                ft.Container(
                    ft.Column([
                        ft.Text("3. Finding Intercepts", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_800),
                        ft.Text("Y-intercept: The point where the line crosses the y-axis (when x = 0)", size=14),
                        ft.Text("To find: substitute x = 0 into the equation", size=14),
                        ft.Text("X-intercept: The point where the line crosses the x-axis (when y = 0)", size=14),
                        ft.Text("To find: substitute y = 0 and solve for x", size=14),
                        ft.Container(
                            ft.Column([
                                ft.Text("Example: y = 2x + 4", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("Y-intercept: (0, 4)", size=14),
                                ft.Text("X-intercept: 0 = 2x + 4, so x = -2, giving (-2, 0)", size=14),
                            ], spacing=5),
                            bgcolor=ft.Colors.ORANGE_50,
                            padding=10,
                            border_radius=5,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                    ], spacing=8),
                    bgcolor=ft.Colors.WHITE,
                    border_radius=10,
                    padding=15,
                    margin=ft.margin.only(bottom=15)
                ),
                
                ft.Container(
                    ft.Column([
                        ft.Text("4. Different Forms of Linear Equations", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_800),
                        ft.Text("• Slope-intercept form: y = mx + b", size=14),
                        ft.Text("• Point-slope form: y - y₁ = m(x - x₁)", size=14),
                        ft.Text("• Standard form: Ax + By = C", size=14),
                        ft.Text("Each form is useful for different situations and makes certain calculations easier.", size=14),
                    ], spacing=8),
                    bgcolor=ft.Colors.WHITE,
                    border_radius=10,
                    padding=15,
                    margin=ft.margin.only(bottom=15)
                ),
                
                # Back button
                ft.Container(
                    ft.ElevatedButton(
                        "Back to Linear Functions",
                        icon=ft.Icons.ARROW_BACK,
                        on_click=lambda e: self.show_page(),
                        style=ft.ButtonStyle(
                            bgcolor=ft.Colors.BLUE_700,
                            color=ft.Colors.WHITE,
                            padding=20
                        )
                    ),
                    alignment=ft.alignment.center,
                    margin=ft.margin.only(top=20)
                )
            ], spacing=15, scroll=ft.ScrollMode.AUTO),
            padding=20,
            expand=True
        )
        
        self.page.add(content)
        self.page.update()
    
    def show_examples(self):
        """Display worked examples"""
        self.page.clean()
        
        content = ft.Container(
            ft.Column([
                # Header
                ft.Row([
                    ft.IconButton(
                        ft.Icons.ARROW_BACK,
                        on_click=lambda e: self.show_page(),
                        tooltip="Back to Linear Functions"
                    ),
                    ft.Text(
                        "💡 Linear Functions: Worked Examples",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.ORANGE_900
                    )
                ], alignment=ft.MainAxisAlignment.START),
                
                ft.Divider(),
                
                # Example 1
                ft.Container(
                    ft.Column([
                        ft.Text("Example 1: Finding Slope from Two Points", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800),
                        ft.Text("Problem: Find the slope of the line passing through points (2, 3) and (6, 11).", size=14),
                        ft.Text("Solution:", size=14, weight=ft.FontWeight.BOLD),
                        ft.Text("Step 1: Identify the coordinates", size=14),
                        ft.Text("Point 1: (x₁, y₁) = (2, 3)", size=14),
                        ft.Text("Point 2: (x₂, y₂) = (6, 11)", size=14),
                        ft.Text("Step 2: Apply the slope formula", size=14),
                        ft.Text("m = (y₂ - y₁) / (x₂ - x₁)", size=14),
                        ft.Text("m = (11 - 3) / (6 - 2)", size=14),
                        ft.Text("m = 8 / 4 = 2", size=14),
                        ft.Container(
                            ft.Text("Answer: The slope is 2", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
                            bgcolor=ft.Colors.GREEN_50,
                            padding=10,
                            border_radius=5,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                    ], spacing=8),
                    bgcolor=ft.Colors.WHITE,
                    border_radius=10,
                    padding=15,
                    margin=ft.margin.only(bottom=20)
                ),
                
                # Example 2
                ft.Container(
                    ft.Column([
                        ft.Text("Example 2: Writing Equation in Slope-Intercept Form", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_800),
                        ft.Text("Problem: Write the equation of a line with slope 3 and y-intercept -2.", size=14),
                        ft.Text("Solution:", size=14, weight=ft.FontWeight.BOLD),
                        ft.Text("Step 1: Identify given information", size=14),
                        ft.Text("Slope (m) = 3", size=14),
                        ft.Text("Y-intercept (b) = -2", size=14),
                        ft.Text("Step 2: Use slope-intercept form", size=14),
                        ft.Text("y = mx + b", size=14),
                        ft.Text("Step 3: Substitute values", size=14),
                        ft.Text("y = 3x + (-2)", size=14),
                        ft.Container(
                            ft.Text("Answer: y = 3x - 2", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
                            bgcolor=ft.Colors.GREEN_50,
                            padding=10,
                            border_radius=5,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                    ], spacing=8),
                    bgcolor=ft.Colors.WHITE,
                    border_radius=10,
                    padding=15,
                    margin=ft.margin.only(bottom=20)
                ),
                
                # Example 3
                ft.Container(
                    ft.Column([
                        ft.Text("Example 3: Finding Intercepts", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_800),
                        ft.Text("Problem: Find the x and y intercepts of y = -2x + 8.", size=14),
                        ft.Text("Solution:", size=14, weight=ft.FontWeight.BOLD),
                        ft.Text("Finding y-intercept (when x = 0):", size=14),
                        ft.Text("y = -2(0) + 8 = 8", size=14),
                        ft.Text("Y-intercept: (0, 8)", size=14),
                        ft.Text("Finding x-intercept (when y = 0):", size=14),
                        ft.Text("0 = -2x + 8", size=14),
                        ft.Text("2x = 8", size=14),
                        ft.Text("x = 4", size=14),
                        ft.Text("X-intercept: (4, 0)", size=14),
                        ft.Container(
                            ft.Column([
                                ft.Text("Answer:", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("Y-intercept: (0, 8)", size=14),
                                ft.Text("X-intercept: (4, 0)", size=14),
                            ], spacing=5),
                            bgcolor=ft.Colors.GREEN_50,
                            padding=10,
                            border_radius=5,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                    ], spacing=8),
                    bgcolor=ft.Colors.WHITE,
                    border_radius=10,
                    padding=15,
                    margin=ft.margin.only(bottom=20)
                ),
                
                # Real-world example
                ft.Container(
                    ft.Column([
                        ft.Text("Example 4: Real-World Application", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.RED_800),
                        ft.Text("Problem: A car rental company charges $30 per day plus $0.25 per mile. Write a linear function for the total cost.", size=14),
                        ft.Text("Solution:", size=14, weight=ft.FontWeight.BOLD),
                        ft.Text("Step 1: Identify variables", size=14),
                        ft.Text("Let x = number of miles driven", size=14),
                        ft.Text("Let y = total cost", size=14),
                        ft.Text("Step 2: Identify the linear components", size=14),
                        ft.Text("Fixed cost (y-intercept): $30", size=14),
                        ft.Text("Rate of change (slope): $0.25 per mile", size=14),
                        ft.Text("Step 3: Write the equation", size=14),
                        ft.Container(
                            ft.Text("Answer: y = 0.25x + 30", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
                            bgcolor=ft.Colors.GREEN_50,
                            padding=10,
                            border_radius=5,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        ft.Text("This means the cost is $30 plus $0.25 for each mile driven.", size=14, style=ft.TextStyle(italic=True)),
                    ], spacing=8),
                    bgcolor=ft.Colors.WHITE,
                    border_radius=10,
                    padding=15,
                    margin=ft.margin.only(bottom=20)
                ),
                
                # Back button
                ft.Container(
                    ft.ElevatedButton(
                        "Back to Linear Functions",
                        icon=ft.Icons.ARROW_BACK,
                        on_click=lambda e: self.show_page(),
                        style=ft.ButtonStyle(
                            bgcolor=ft.Colors.ORANGE_700,
                            color=ft.Colors.WHITE,
                            padding=20
                        )
                    ),
                    alignment=ft.alignment.center,
                    margin=ft.margin.only(top=20)
                )
            ], spacing=15, scroll=ft.ScrollMode.AUTO),
            padding=20,
            expand=True
        )
        
        self.page.add(content)
        self.page.update()
    
    def _generate_quiz_questions(self):
        """Generate quiz questions for linear functions"""
        questions = [
            {
                "question": "What is the slope of the line passing through points (1, 2) and (5, 10)?",
                "options": ["2", "3", "4", "8"],
                "correct": 0,
                "explanation": "Slope = (10-2)/(5-1) = 8/4 = 2"
            },
            {
                "question": "What is the y-intercept of the equation y = 3x - 7?",
                "options": ["3", "-7", "7", "0"],
                "correct": 1,
                "explanation": "In y = mx + b form, b is the y-intercept, so b = -7"
            },
            {
                "question": "Which equation represents a line with slope -2 and y-intercept 5?",
                "options": ["y = -2x + 5", "y = 5x - 2", "y = 2x + 5", "y = -5x + 2"],
                "correct": 0,
                "explanation": "Using y = mx + b with m = -2 and b = 5 gives y = -2x + 5"
            },
            {
                "question": "What is the x-intercept of y = 4x - 12?",
                "options": ["4", "-12", "3", "-3"],
                "correct": 2,
                "explanation": "Set y = 0: 0 = 4x - 12, so 4x = 12, x = 3"
            },
            {
                "question": "A line has slope 0. What type of line is this?",
                "options": ["Vertical", "Horizontal", "Diagonal up", "Diagonal down"],
                "correct": 1,
                "explanation": "A slope of 0 means no change in y, creating a horizontal line"
            },
            {
                "question": "What is the slope of a vertical line?",
                "options": ["0", "1", "-1", "Undefined"],
                "correct": 3,
                "explanation": "Vertical lines have undefined slope because the denominator (change in x) is 0"
            },
            {
                "question": "If a line passes through (0, 3) and (2, 7), what is its equation?",
                "options": ["y = 2x + 3", "y = 3x + 2", "y = x + 3", "y = 4x + 3"],
                "correct": 0,
                "explanation": "Slope = (7-3)/(2-0) = 2, y-intercept = 3, so y = 2x + 3"
            },
            {
                "question": "Which point lies on the line y = -3x + 1?",
                "options": ["(1, -2)", "(2, -5)", "(0, 1)", "All of the above"],
                "correct": 3,
                "explanation": "Check each: (1,-2): -2 = -3(1)+1 ✓, (2,-5): -5 = -3(2)+1 ✓, (0,1): 1 = -3(0)+1 ✓"
            },
            {
                "question": "What is the slope-intercept form of the equation 2x + y = 6?",
                "options": ["y = 2x + 6", "y = -2x + 6", "y = 2x - 6", "y = x + 3"],
                "correct": 1,
                "explanation": "Solve for y: y = -2x + 6"
            },
            {
                "question": "A line with positive slope and negative y-intercept passes through which quadrants?",
                "options": ["I, II, III", "I, III, IV", "II, III, IV", "I, II, IV"],
                "correct": 1,
                "explanation": "Positive slope goes up from left to right, negative y-intercept starts below x-axis, passing through quadrants I, III, IV"
            }
        ]
        
        return random.sample(questions, len(questions))
    
    def show_quiz(self):
        """Display quiz interface"""
        self.current_question = 0
        self.score = 0
        self.selected_answer = None
        self._display_question()
    
    def _display_question(self):
        """Display current quiz question"""
        self.page.clean()
        
        if self.current_question >= len(self.quiz_questions):
            self._show_quiz_results()
            return
        
        question_data = self.quiz_questions[self.current_question]
        progress = (self.current_question + 1) / len(self.quiz_questions)
        
        content = ft.Container(
            ft.Column([
                # Header
                ft.Row([
                    ft.IconButton(
                        ft.Icons.ARROW_BACK,
                        on_click=lambda e: self.show_page(),
                        tooltip="Back to Linear Functions"
                    ),
                    ft.Text(
                        f"Quiz Question {self.current_question + 1} of {len(self.quiz_questions)}",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.GREEN_900
                    )
                ], alignment=ft.MainAxisAlignment.START),
                
                # Progress bar
                ft.Container(
                    ft.ProgressBar(value=progress, bgcolor=ft.Colors.GREEN_100, color=ft.Colors.GREEN_600),
                    margin=ft.margin.only(bottom=20)
                ),
                
                # Question
                ft.Container(
                    ft.Column([
                        ft.Text(
                            question_data["question"],
                            size=18,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.BLUE_900
                        ),
                    ]),
                    bgcolor=ft.Colors.BLUE_50,
                    border_radius=10,
                    padding=20,
                    margin=ft.margin.only(bottom=20)
                ),
                
                # Answer options
                ft.Column([
                    ft.RadioGroup(
                        content=ft.Column([
                            ft.Radio(value=i, label=option, label_style=ft.TextStyle(size=16))
                            for i, option in enumerate(question_data["options"])
                        ], spacing=10),
                        on_change=self._on_answer_selected
                    )
                ], spacing=10),
                
                # Submit button
                ft.Container(
                    ft.ElevatedButton(
                        "Submit Answer",
                        icon=ft.Icons.CHECK,
                        on_click=lambda e: self._submit_answer(),
                        disabled=True,
                        style=ft.ButtonStyle(
                            bgcolor=ft.Colors.GREEN_600,
                            color=ft.Colors.WHITE,
                            padding=15
                        )
                    ),
                    alignment=ft.alignment.center,
                    margin=ft.margin.only(top=20)
                ),
                
                # Score display
                ft.Container(
                    ft.Text(
                        f"Current Score: {self.score}/{self.current_question}",
                        size=16,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.PURPLE_700,
                        text_align=ft.TextAlign.CENTER
                    ),
                    alignment=ft.alignment.center,
                    margin=ft.margin.only(top=10)
                )
            ], spacing=15),
            padding=20,
            expand=True
        )
        
        self.page.add(content)
        self.page.update()
    
    def _on_answer_selected(self, e):
        """Handle answer selection"""
        self.selected_answer = int(e.control.value)
        # Enable submit button
        for control in self.page.controls:
            if hasattr(control, 'content'):
                self._enable_submit_button(control.content)
        self.page.update()
    
    def _enable_submit_button(self, control):
        """Recursively find and enable submit button"""
        if hasattr(control, 'controls'):
            for child in control.controls:
                if isinstance(child, ft.ElevatedButton) and hasattr(child, 'text') and child.text == "Submit Answer":
                    child.disabled = False
                    return
                elif hasattr(child, 'content'):
                    self._enable_submit_button(child.content)
                elif hasattr(child, 'controls'):
                    self._enable_submit_button(child)
    
    def _submit_answer(self):
        """Submit the selected answer"""
        if self.selected_answer is None:
            return
        
        question_data = self.quiz_questions[self.current_question]
        is_correct = self.selected_answer == question_data["correct"]
        
        if is_correct:
            self.score += 1
        
        self._show_answer_feedback(is_correct, question_data["explanation"])
    
    def _show_answer_feedback(self, is_correct, explanation):
        """Show feedback for the submitted answer"""
        self.page.clean()
        
        feedback_color = ft.Colors.GREEN_600 if is_correct else ft.Colors.RED_600
        feedback_icon = ft.Icons.CHECK_CIRCLE if is_correct else ft.Icons.CANCEL
        feedback_text = "Correct!" if is_correct else "Incorrect"
        
        content = ft.Container(
            ft.Column([
                ft.Container(
                    ft.Column([
                        ft.Icon(feedback_icon, size=60, color=feedback_color),
                        ft.Text(
                            feedback_text,
                            size=24,
                            weight=ft.FontWeight.BOLD,
                            color=feedback_color,
                            text_align=ft.TextAlign.CENTER
                        )
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    alignment=ft.alignment.center,
                    margin=ft.margin.only(bottom=20)
                ),
                
                ft.Container(
                    ft.Column([
                        ft.Text("Explanation:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                        ft.Text(explanation, size=14, color=ft.Colors.BLUE_800),
                    ], spacing=10),
                    bgcolor=ft.Colors.BLUE_50,
                    border_radius=10,
                    padding=20,
                    margin=ft.margin.only(bottom=20)
                ),
                
                ft.Container(
                    ft.ElevatedButton(
                        "Next Question" if self.current_question < len(self.quiz_questions) - 1 else "Show Results",
                        icon=ft.Icons.ARROW_FORWARD,
                        on_click=lambda e: self._next_question(),
                        style=ft.ButtonStyle(
                            bgcolor=ft.Colors.BLUE_600,
                            color=ft.Colors.WHITE,
                            padding=15
                        )
                    ),
                    alignment=ft.alignment.center
                )
            ], spacing=15),
            padding=20,
            expand=True
        )
        
        self.page.add(content)
        self.page.update()
    
    def _next_question(self):
        """Move to next question"""
        self.current_question += 1
        self.selected_answer = None
        self._display_question()
    
    def _show_quiz_results(self):
        """Show final quiz results"""
        self.page.clean()
        
        percentage = (self.score / len(self.quiz_questions)) * 100
        
        if percentage >= 90:
            grade = "A+"
            message = "Outstanding! You've mastered linear functions!"
            color = ft.Colors.GREEN_600
        elif percentage >= 80:
            grade = "A"
            message = "Excellent work! You have a strong understanding of linear functions."
            color = ft.Colors.GREEN_600
        elif percentage >= 70:
            grade = "B"
            message = "Good job! You understand most linear function concepts."
            color = ft.Colors.BLUE_600
        elif percentage >= 60:
            grade = "C"
            message = "Fair work. Review the examples and try again."
            color = ft.Colors.ORANGE_600
        else:
            grade = "F"
            message = "Keep practicing! Review the learning content and examples."
            color = ft.Colors.RED_600
        
        content = ft.Container(
            ft.Column([
                ft.Text(
                    "🎉 Quiz Complete!",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.PURPLE_900,
                    text_align=ft.TextAlign.CENTER
                ),
                
                ft.Container(
                    ft.Column([
                        ft.Text(f"Your Score: {self.score}/{len(self.quiz_questions)}", size=24, weight=ft.FontWeight.BOLD),
                        ft.Text(f"Percentage: {percentage:.1f}%", size=20),
                        ft.Text(f"Grade: {grade}", size=20, weight=ft.FontWeight.BOLD, color=color),
                        ft.Text(message, size=16, text_align=ft.TextAlign.CENTER),
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
                    bgcolor=ft.Colors.PURPLE_50,
                    border_radius=15,
                    padding=30,
                    margin=ft.margin.only(bottom=30)
                ),
                
                ft.ResponsiveRow([
                    ft.Container(
                        ft.ElevatedButton(
                            "Retake Quiz",
                            icon=ft.Icons.REFRESH,
                            on_click=lambda e: self.show_quiz(),
                            style=ft.ButtonStyle(
                                bgcolor=ft.Colors.BLUE_600,
                                color=ft.Colors.WHITE,
                                padding=15
                            )
                        ),
                        col={'xs': 12, 'sm': 6}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            "Back to Linear Functions",
                            icon=ft.Icons.ARROW_BACK,
                            on_click=lambda e: self.show_page(),
                            style=ft.ButtonStyle(
                                bgcolor=ft.Colors.GREEN_600,
                                color=ft.Colors.WHITE,
                                padding=15
                            )
                        ),
                        col={'xs': 12, 'sm': 6}
                    ),
                ], spacing=15)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20),
            padding=20,
            expand=True
        )
        
        self.page.add(content)
        self.page.update()
    
    def show_ai_help(self):
        """Display AI help interface"""
        self.page.clean()
        
        # Create text field for user input
        user_input = ft.TextField(
            label="Ask me anything about linear functions...",
            multiline=True,
            min_lines=3,
            max_lines=5,
            border_radius=10,
            bgcolor=ft.Colors.WHITE
        )
        
        # Chat messages container
        chat_messages = ft.Column([], spacing=10, scroll=ft.ScrollMode.AUTO, height=300)
        
        def send_message(e):
            user_question = user_input.value.strip()
            if not user_question:
                return
            
            # Add user message
            chat_messages.controls.append(
                ft.Container(
                    ft.Text(f"You: {user_question}", size=14, color=ft.Colors.BLUE_900),
                    bgcolor=ft.Colors.BLUE_50,
                    border_radius=10,
                    padding=10,
                    alignment=ft.alignment.center_right
                )
            )
            
            # Generate AI response
            ai_response = self._generate_ai_response(user_question)
            chat_messages.controls.append(
                ft.Container(
                    ft.Text(f"AI Tutor: {ai_response}", size=14, color=ft.Colors.GREEN_900),
                    bgcolor=ft.Colors.GREEN_50,
                    border_radius=10,
                    padding=10,
                    alignment=ft.alignment.center_left
                )
            )
            
            user_input.value = ""
            self.page.update()
        
        content = ft.Container(
            ft.Column([
                # Header
                ft.Row([
                    ft.IconButton(
                        ft.Icons.ARROW_BACK,
                        on_click=lambda e: self.show_page(),
                        tooltip="Back to Linear Functions"
                    ),
                    ft.Text(
                        "🤖 AI Tutor - Linear Functions Help",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.PURPLE_900
                    )
                ], alignment=ft.MainAxisAlignment.START),
                
                ft.Divider(),
                
                # Instructions
                ft.Container(
                    ft.Column([
                        ft.Text("💬 Ask me anything about linear functions!", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_800),
                        ft.Text("I can help with:", size=14),
                        ft.Text("• Understanding slope and y-intercept", size=12),
                        ft.Text("• Solving specific problems step-by-step", size=12),
                        ft.Text("• Explaining concepts in different ways", size=12),
                        ft.Text("• Providing additional practice problems", size=12),
                    ], spacing=5),
                    bgcolor=ft.Colors.PURPLE_50,
                    border_radius=10,
                    padding=15,
                    margin=ft.margin.only(bottom=20)
                ),
                
                # Chat area
                ft.Container(
                    chat_messages,
                    bgcolor=ft.Colors.GREY_50,
                    border_radius=10,
                    padding=10,
                    margin=ft.margin.only(bottom=20)
                ),
                
                # Input area
                ft.Row([
                    ft.Container(user_input, expand=True),
                    ft.IconButton(
                        ft.Icons.SEND,
                        icon_color=ft.Colors.PURPLE_700,
                        on_click=send_message,
                        tooltip="Send message"
                    )
                ], spacing=10),
                
                # Quick help buttons
                ft.Text("Quick Help:", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_800),
                ft.ResponsiveRow([
                    ft.Container(
                        ft.ElevatedButton(
                            "Explain Slope",
                            on_click=lambda e: self._quick_help("slope"),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.PURPLE_100)
                        ),
                        col={'xs': 6, 'sm': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            "Y-Intercept Help",
                            on_click=lambda e: self._quick_help("y-intercept"),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.PURPLE_100)
                        ),
                        col={'xs': 6, 'sm': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            "Graphing Help",
                            on_click=lambda e: self._quick_help("graphing"),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.PURPLE_100)
                        ),
                        col={'xs': 6, 'sm': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            "Practice Problem",
                            on_click=lambda e: self._quick_help("practice"),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.PURPLE_100)
                        ),
                        col={'xs': 6, 'sm': 3}
                    ),
                ], spacing=10)
            ], spacing=15),
            padding=20,
            expand=True
        )
        
        self.page.add(content)
        self.page.update()
    
    def _quick_help(self, topic):
        """Handle quick help buttons"""
        responses = {
            "slope": "Slope measures how steep a line is. It's calculated as 'rise over run' or (y₂-y₁)/(x₂-x₁). A positive slope goes up from left to right, negative slope goes down.",
            "y-intercept": "The y-intercept is where the line crosses the y-axis. In y = mx + b, the y-intercept is 'b'. It's the value of y when x = 0.",
            "graphing": "To graph a linear function: 1) Find the y-intercept (plot the point where the line crosses the y-axis), 2) Use the slope to find another point, 3) Draw a straight line through both points.",
            "practice": "Here's a practice problem: Find the equation of a line passing through (2, 5) and (4, 11). First find the slope: m = (11-5)/(4-2) = 6/2 = 3. Then use point-slope form: y - 5 = 3(x - 2), which simplifies to y = 3x - 1."
        }
        
        # Add the response to chat
        chat_messages = None
        for control in self.page.controls:
            if hasattr(control, 'content'):
                chat_messages = self._find_chat_messages(control.content)
                if chat_messages:
                    break
        
        if chat_messages:
            chat_messages.controls.append(
                ft.Container(
                    ft.Text(f"AI Tutor: {responses[topic]}", size=14, color=ft.Colors.GREEN_900),
                    bgcolor=ft.Colors.GREEN_50,
                    border_radius=10,
                    padding=10,
                    alignment=ft.alignment.center_left
                )
            )
            self.page.update()
    
    def _find_chat_messages(self, control):
        """Recursively find chat messages container"""
        if hasattr(control, 'controls'):
            for child in control.controls:
                if isinstance(child, ft.Column) and hasattr(child, 'height') and child.height == 300:
                    return child
                elif hasattr(child, 'content'):
                    result = self._find_chat_messages(child.content)
                    if result:
                        return result
                elif hasattr(child, 'controls'):
                    result = self._find_chat_messages(child)
                    if result:
                        return result
        return None
    
    def _generate_ai_response(self, question):
        """Generate AI tutor response based on question"""
        question_lower = question.lower()
        
        if "slope" in question_lower:
            return "Slope is the rate of change in a linear function. It tells us how much y changes for each unit change in x. The formula is (y₂-y₁)/(x₂-x₁). Would you like me to work through a specific example?"
        
        elif "intercept" in question_lower:
            if "y" in question_lower:
                return "The y-intercept is where the line crosses the y-axis (when x = 0). In the equation y = mx + b, the y-intercept is 'b'. To find it from a graph, look where the line crosses the vertical axis."
            elif "x" in question_lower:
                return "The x-intercept is where the line crosses the x-axis (when y = 0). To find it, set y = 0 in your equation and solve for x. For example, in y = 2x - 6, set 0 = 2x - 6, so x = 3."
            else:
                return "Intercepts are where the line crosses the axes. Y-intercept: crosses y-axis (x=0). X-intercept: crosses x-axis (y=0). Both are important for graphing and understanding the function."
        
        elif "graph" in question_lower:
            return "To graph a linear function: 1) Find the y-intercept and plot it, 2) Use the slope to find a second point (rise/run from the first point), 3) Draw a straight line through both points. The slope tells you the direction and steepness."
        
        elif "equation" in question_lower:
            return "Linear equations can be written in different forms: Slope-intercept (y = mx + b), Point-slope (y - y₁ = m(x - x₁)), or Standard form (Ax + By = C). Each form is useful for different situations."
        
        elif "example" in question_lower or "practice" in question_lower:
            examples = [
                "Find the slope between (1, 3) and (5, 11): m = (11-3)/(5-1) = 8/4 = 2",
                "Write the equation of a line with slope 2 and y-intercept -3: y = 2x - 3",
                "Find the x-intercept of y = 3x - 9: Set y = 0, so 0 = 3x - 9, x = 3"
            ]
            return f"Here's an example: {random.choice(examples)}. Would you like me to explain any step in detail?"
        
        elif "help" in question_lower or "don't understand" in question_lower:
            return "I'm here to help! Linear functions represent straight-line relationships. The key parts are slope (how steep) and intercepts (where it crosses axes). What specific part would you like me to explain further?"
        
        else:
            return "That's a great question about linear functions! Could you be more specific about what you'd like to know? I can help with slopes, intercepts, graphing, equations, or work through specific problems with you."


def linear_functions_page(page: ft.Page):
    """Main entry point for Linear Functions module"""
    module = LinearFunctionsModule(page)
    module.show_page()
