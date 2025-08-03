import flet as ft
import random
import math


class NumberPatternsModule:
    """Comprehensive Number Patterns learning module"""
    
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
        """Show the main number patterns page
        Args:
            page: Optional page reference. If not provided, uses self.page
        """
        if page is None:
            page = self.page
        self.page = page  # Update the page reference
            
        view = ft.View(
            "/number_patterns",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: page.go_back()),
                    title=ft.Text("Number Patterns"),
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
            title=ft.Text("Number Patterns"),
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
                            "🔢 Number Patterns",
                            size=32,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.BLUE_900,
                            text_align=ft.TextAlign.CENTER
                        ),
                        ft.Text(
                            "Discover sequences, progressions, and mathematical patterns",
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
                        ft.Text("• Identify arithmetic and geometric sequences", size=14),
                        ft.Text("• Calculate terms using formulas", size=14),
                        ft.Text("• Understand Fibonacci sequences", size=14),
                        ft.Text("• Explore Pascal's triangle", size=14),
                        ft.Text("• Study square and triangular numbers", size=14),
                        ft.Text("• Apply patterns in problem solving", size=14),
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
                        ft.Text("🎭 Number Patterns Overview", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                        ft.Text("Number patterns are sequences that follow specific rules or formulas. They appear everywhere in mathematics, nature, art, and science, helping us understand relationships and predict future values.", size=14),
                        
                        ft.Divider(height=10),
                        
                        ft.Text("🔑 Key Types:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_800),
                        ft.Text("• Arithmetic sequences (constant difference)", size=14),
                        ft.Text("• Geometric sequences (constant ratio)", size=14),
                        ft.Text("• Fibonacci sequence (sum of previous two)", size=14),
                        ft.Text("• Square numbers (1, 4, 9, 16, 25...)", size=14),
                        ft.Text("• Triangular numbers (1, 3, 6, 10, 15...)", size=14),
                        
                        ft.Divider(height=10),
                        
                        ft.Text("🌟 Applications:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_800),
                        ft.Text("• Predicting growth patterns", size=14),
                        ft.Text("• Financial calculations (compound interest)", size=14),
                        ft.Text("• Computer algorithms", size=14),
                        ft.Text("• Art and design patterns", size=14),
                        ft.Text("• Natural phenomena (spiral shells, flowers)", size=14),
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
                        tooltip="Back to Number Patterns"
                    ),
                    ft.Text(
                        "📚 Number Patterns: Complete Guide",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLUE_900
                    )
                ], alignment=ft.MainAxisAlignment.START),
                
                ft.Divider(),
                
                # Content sections
                ft.Container(
                    ft.Column([
                        ft.Text("1. Arithmetic Sequences", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800),
                        ft.Text("An arithmetic sequence has a constant difference between consecutive terms.", size=14),
                        ft.Container(
                            ft.Column([
                                ft.Text("General Form: aₙ = a₁ + (n-1)d", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("Where:", size=14),
                                ft.Text("• a₁ = first term", size=14),
                                ft.Text("• d = common difference", size=14),
                                ft.Text("• n = term number", size=14),
                                ft.Text("Example: 2, 5, 8, 11, 14, ...", size=14),
                                ft.Text("First term a₁ = 2, common difference d = 3", size=14),
                                ft.Text("5th term: a₅ = 2 + (5-1)×3 = 2 + 12 = 14", size=14),
                            ], spacing=5),
                            bgcolor=ft.Colors.BLUE_50,
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
                        ft.Text("2. Geometric Sequences", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_800),
                        ft.Text("A geometric sequence has a constant ratio between consecutive terms.", size=14),
                        ft.Container(
                            ft.Column([
                                ft.Text("General Form: aₙ = a₁ × r^(n-1)", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("Where:", size=14),
                                ft.Text("• a₁ = first term", size=14),
                                ft.Text("• r = common ratio", size=14),
                                ft.Text("• n = term number", size=14),
                                ft.Text("Example: 3, 6, 12, 24, 48, ...", size=14),
                                ft.Text("First term a₁ = 3, common ratio r = 2", size=14),
                                ft.Text("5th term: a₅ = 3 × 2^(5-1) = 3 × 16 = 48", size=14),
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
                    margin=ft.margin.only(bottom=15)
                ),
                
                ft.Container(
                    ft.Column([
                        ft.Text("3. Fibonacci Sequence", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_800),
                        ft.Text("Each term is the sum of the two preceding terms.", size=14),
                        ft.Container(
                            ft.Column([
                                ft.Text("Rule: F(n) = F(n-1) + F(n-2)", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("Starting with F(1) = 1, F(2) = 1", size=14),
                                ft.Text("Sequence: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...", size=14),
                                ft.Text("F(3) = F(2) + F(1) = 1 + 1 = 2", size=14),
                                ft.Text("F(4) = F(3) + F(2) = 2 + 1 = 3", size=14),
                                ft.Text("F(5) = F(4) + F(3) = 3 + 2 = 5", size=14),
                                ft.Text("Golden Ratio: F(n+1)/F(n) approaches φ ≈ 1.618", size=14),
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
                        ft.Text("4. Square Numbers", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_800),
                        ft.Text("Numbers that result from multiplying an integer by itself.", size=14),
                        ft.Container(
                            ft.Column([
                                ft.Text("Formula: n² where n is a positive integer", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("Sequence: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, ...", size=14),
                                ft.Text("Pattern in differences:", size=14),
                                ft.Text("4-1=3, 9-4=5, 16-9=7, 25-16=9, ...", size=14),
                                ft.Text("The differences form: 3, 5, 7, 9, ... (odd numbers)", size=14),
                                ft.Text("Geometric interpretation: area of squares", size=14),
                            ], spacing=5),
                            bgcolor=ft.Colors.PURPLE_50,
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
                        ft.Text("5. Triangular Numbers", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.RED_800),
                        ft.Text("Numbers that can form triangular patterns of dots.", size=14),
                        ft.Container(
                            ft.Column([
                                ft.Text("Formula: Tₙ = n(n+1)/2", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("Sequence: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...", size=14),
                                ft.Text("T₁ = 1×2/2 = 1", size=14),
                                ft.Text("T₂ = 2×3/2 = 3", size=14),
                                ft.Text("T₃ = 3×4/2 = 6", size=14),
                                ft.Text("T₄ = 4×5/2 = 10", size=14),
                                ft.Text("Also: sum of first n natural numbers", size=14),
                            ], spacing=5),
                            bgcolor=ft.Colors.RED_50,
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
                
                # Back button
                ft.Container(
                    ft.ElevatedButton(
                        "Back to Number Patterns",
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
                        tooltip="Back to Number Patterns"
                    ),
                    ft.Text(
                        "💡 Number Patterns: Worked Examples",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.ORANGE_900
                    )
                ], alignment=ft.MainAxisAlignment.START),
                
                ft.Divider(),
                
                # Example 1
                ft.Container(
                    ft.Column([
                        ft.Text("Example 1: Arithmetic Sequence", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800),
                        ft.Text("Problem: Find the 15th term of the sequence 7, 11, 15, 19, ...", size=14),
                        ft.Text("Solution:", size=14, weight=ft.FontWeight.BOLD),
                        ft.Text("Step 1: Identify the pattern", size=14),
                        ft.Text("First term a₁ = 7", size=14),
                        ft.Text("Common difference d = 11 - 7 = 4", size=14),
                        ft.Text("Step 2: Use the formula aₙ = a₁ + (n-1)d", size=14),
                        ft.Text("a₁₅ = 7 + (15-1)×4", size=14),
                        ft.Text("a₁₅ = 7 + 14×4", size=14),
                        ft.Text("a₁₅ = 7 + 56 = 63", size=14),
                        ft.Container(
                            ft.Text("Answer: The 15th term is 63", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
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
                        ft.Text("Example 2: Geometric Sequence", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_800),
                        ft.Text("Problem: In the sequence 2, 6, 18, 54, ..., find the 8th term.", size=14),
                        ft.Text("Solution:", size=14, weight=ft.FontWeight.BOLD),
                        ft.Text("Step 1: Identify the pattern", size=14),
                        ft.Text("First term a₁ = 2", size=14),
                        ft.Text("Common ratio r = 6 ÷ 2 = 3", size=14),
                        ft.Text("Step 2: Use the formula aₙ = a₁ × r^(n-1)", size=14),
                        ft.Text("a₈ = 2 × 3^(8-1)", size=14),
                        ft.Text("a₈ = 2 × 3⁷", size=14),
                        ft.Text("a₈ = 2 × 2187 = 4374", size=14),
                        ft.Container(
                            ft.Text("Answer: The 8th term is 4374", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
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
                        ft.Text("Example 3: Identifying Pattern Type", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_800),
                        ft.Text("Problem: What type of sequence is 1, 4, 7, 10, 13, ...?", size=14),
                        ft.Text("Solution:", size=14, weight=ft.FontWeight.BOLD),
                        ft.Text("Step 1: Check differences between consecutive terms", size=14),
                        ft.Text("4 - 1 = 3", size=14),
                        ft.Text("7 - 4 = 3", size=14),
                        ft.Text("10 - 7 = 3", size=14),
                        ft.Text("13 - 10 = 3", size=14),
                        ft.Text("Step 2: Constant difference = 3", size=14),
                        ft.Container(
                            ft.Column([
                                ft.Text("Answer: Arithmetic sequence", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
                                ft.Text("Formula: aₙ = 1 + (n-1)×3 = 3n - 2", size=14),
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
                
                # Example 4
                ft.Container(
                    ft.Column([
                        ft.Text("Example 4: Triangular Numbers Application", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.RED_800),
                        ft.Text("Problem: How many handshakes occur when 10 people each shake hands with every other person exactly once?", size=14),
                        ft.Text("Solution:", size=14, weight=ft.FontWeight.BOLD),
                        ft.Text("Step 1: This is a combination problem", size=14),
                        ft.Text("We need to choose 2 people from 10 people", size=14),
                        ft.Text("Step 2: Use triangular numbers", size=14),
                        ft.Text("With n people, handshakes = Tₙ₋₁ = (n-1)n/2", size=14),
                        ft.Text("Wait, that's not right. Let me recalculate:", size=14),
                        ft.Text("With n people, handshakes = n(n-1)/2", size=14),
                        ft.Text("For 10 people: 10×9/2 = 45", size=14),
                        ft.Container(
                            ft.Text("Answer: 45 handshakes", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
                            bgcolor=ft.Colors.GREEN_50,
                            padding=10,
                            border_radius=5,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        ft.Text("This follows the 9th triangular number: T₉ = 9×10/2 = 45", size=14, style=ft.TextStyle(italic=True)),
                    ], spacing=8),
                    bgcolor=ft.Colors.WHITE,
                    border_radius=10,
                    padding=15,
                    margin=ft.margin.only(bottom=20)
                ),
                
                # Back button
                ft.Container(
                    ft.ElevatedButton(
                        "Back to Number Patterns",
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
        """Generate quiz questions for number patterns"""
        questions = [
            {
                "question": "What is the next term in the arithmetic sequence: 5, 9, 13, 17, ...?",
                "options": ["20", "21", "22", "23"],
                "correct": 1,
                "explanation": "Common difference is 4, so next term is 17 + 4 = 21"
            },
            {
                "question": "In the geometric sequence 3, 12, 48, 192, ..., what is the common ratio?",
                "options": ["3", "4", "9", "12"],
                "correct": 1,
                "explanation": "12 ÷ 3 = 4, and 48 ÷ 12 = 4, so the common ratio is 4"
            },
            {
                "question": "What is the 6th term in the Fibonacci sequence?",
                "options": ["5", "8", "13", "21"],
                "correct": 1,
                "explanation": "Fibonacci: 1, 1, 2, 3, 5, 8, ... The 6th term is 8"
            },
            {
                "question": "Which formula represents the nth triangular number?",
                "options": ["n²", "n(n+1)/2", "2ⁿ", "n(n-1)/2"],
                "correct": 1,
                "explanation": "The nth triangular number is given by Tₙ = n(n+1)/2"
            },
            {
                "question": "What is the 5th square number?",
                "options": ["20", "25", "30", "35"],
                "correct": 1,
                "explanation": "The 5th square number is 5² = 25"
            },
            {
                "question": "In the sequence 2, 5, 11, 23, 47, ..., what is the pattern?",
                "options": ["Add 3, then 6, then 12, ...", "Multiply by 2, then add 1", "Double previous and add 1", "Fibonacci-like addition"],
                "correct": 2,
                "explanation": "Each term is double the previous term plus 1: 2→5 (2×2+1), 5→11 (5×2+1), 11→23 (11×2+1)"
            },
            {
                "question": "What type of sequence is 1, 1/2, 1/4, 1/8, ...?",
                "options": ["Arithmetic", "Geometric", "Fibonacci", "Triangular"],
                "correct": 1,
                "explanation": "Each term is multiplied by 1/2, making it a geometric sequence with ratio 1/2"
            },
            {
                "question": "The sum of the first n natural numbers equals which triangular number?",
                "options": ["Tₙ₋₁", "Tₙ", "Tₙ₊₁", "T₂ₙ"],
                "correct": 1,
                "explanation": "The sum 1+2+3+...+n equals the nth triangular number Tₙ = n(n+1)/2"
            },
            {
                "question": "What is the 10th term of the sequence 3, 7, 11, 15, ...?",
                "options": ["35", "37", "39", "41"],
                "correct": 2,
                "explanation": "Arithmetic sequence: a₁=3, d=4. a₁₀ = 3 + (10-1)×4 = 3 + 36 = 39"
            },
            {
                "question": "In Pascal's triangle, what number appears in the 3rd position of the 5th row?",
                "options": ["6", "8", "10", "12"],
                "correct": 2,
                "explanation": "Row 5 (counting from 0): 1, 5, 10, 10, 5, 1. The 3rd position (counting from 0) is 10"
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
                        tooltip="Back to Number Patterns"
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
            message = "Outstanding! You've mastered number patterns!"
            color = ft.Colors.GREEN_600
        elif percentage >= 80:
            grade = "A"
            message = "Excellent work! You have a strong understanding of patterns."
            color = ft.Colors.GREEN_600
        elif percentage >= 70:
            grade = "B"
            message = "Good job! You understand most pattern concepts."
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
                            "Back to Number Patterns",
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
            label="Ask me anything about number patterns...",
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
                        tooltip="Back to Number Patterns"
                    ),
                    ft.Text(
                        "🤖 AI Tutor - Number Patterns Help",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.PURPLE_900
                    )
                ], alignment=ft.MainAxisAlignment.START),
                
                ft.Divider(),
                
                # Instructions
                ft.Container(
                    ft.Column([
                        ft.Text("💬 Ask me anything about number patterns!", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_800),
                        ft.Text("I can help with:", size=14),
                        ft.Text("• Arithmetic and geometric sequences", size=12),
                        ft.Text("• Fibonacci and other special sequences", size=12),
                        ft.Text("• Finding pattern formulas", size=12),
                        ft.Text("• Real-world pattern applications", size=12),
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
                            "Arithmetic",
                            on_click=lambda e: self._quick_help("arithmetic"),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.PURPLE_100)
                        ),
                        col={'xs': 6, 'sm': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            "Geometric",
                            on_click=lambda e: self._quick_help("geometric"),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.PURPLE_100)
                        ),
                        col={'xs': 6, 'sm': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            "Fibonacci",
                            on_click=lambda e: self._quick_help("fibonacci"),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.PURPLE_100)
                        ),
                        col={'xs': 6, 'sm': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            "Applications",
                            on_click=lambda e: self._quick_help("applications"),
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
            "arithmetic": "Arithmetic sequences have a constant difference between terms. Formula: aₙ = a₁ + (n-1)d. Example: 2, 5, 8, 11... (difference = 3). To find any term, use the formula with the first term and common difference.",
            "geometric": "Geometric sequences have a constant ratio between terms. Formula: aₙ = a₁ × r^(n-1). Example: 3, 6, 12, 24... (ratio = 2). Each term is multiplied by the same number to get the next term.",
            "fibonacci": "Fibonacci sequence: each term is the sum of the two previous terms. Starts 1, 1, 2, 3, 5, 8, 13, 21... Formula: F(n) = F(n-1) + F(n-2). Appears in nature: flower petals, spiral shells, tree branches.",
            "applications": "Number patterns appear everywhere! Arithmetic: saving money regularly. Geometric: population growth, compound interest. Fibonacci: nature patterns, art proportions. Patterns help predict trends, optimize algorithms, and model real-world phenomena."
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
        
        if "arithmetic" in question_lower:
            return "Arithmetic sequences have a constant difference between consecutive terms. The formula is aₙ = a₁ + (n-1)d where a₁ is the first term and d is the common difference. Would you like me to help with a specific arithmetic sequence?"
        
        elif "geometric" in question_lower:
            return "Geometric sequences have a constant ratio between consecutive terms. The formula is aₙ = a₁ × r^(n-1) where a₁ is the first term and r is the common ratio. Each term is found by multiplying the previous term by r."
        
        elif "fibonacci" in question_lower:
            return "The Fibonacci sequence starts with 1, 1 and each subsequent term is the sum of the two previous terms: 1, 1, 2, 3, 5, 8, 13, 21... It appears in nature and has the golden ratio property. What would you like to know about it?"
        
        elif "formula" in question_lower or "equation" in question_lower:
            return "Different patterns have different formulas: Arithmetic (aₙ = a₁ + (n-1)d), Geometric (aₙ = a₁ × r^(n-1)), Triangular (Tₙ = n(n+1)/2), Square (Sₙ = n²). Which type are you working with?"
        
        elif "difference" in question_lower:
            return "For arithmetic sequences, find the common difference by subtracting consecutive terms. For geometric sequences, find the common ratio by dividing consecutive terms. This helps identify the pattern type and formula."
        
        elif "next term" in question_lower or "find term" in question_lower:
            return "To find the next term, first identify the pattern type. Check if differences are constant (arithmetic) or ratios are constant (geometric), then apply the appropriate rule. What sequence are you working with?"
        
        elif "triangular" in question_lower:
            return "Triangular numbers represent dots arranged in triangular patterns: 1, 3, 6, 10, 15... The formula is Tₙ = n(n+1)/2. They also represent the sum of the first n natural numbers."
        
        elif "square" in question_lower:
            return "Square numbers are perfect squares: 1, 4, 9, 16, 25... The formula is Sₙ = n². The differences between consecutive square numbers are consecutive odd numbers: 3, 5, 7, 9..."
        
        else:
            return "Great question about number patterns! I can help with arithmetic sequences, geometric sequences, Fibonacci numbers, triangular numbers, square numbers, and their formulas. What specific pattern or concept would you like to explore?"


def number_patterns_page(page: ft.Page):
    """Main entry point for Number Patterns module"""
    module = NumberPatternsModule(page)
    module.show_page()
