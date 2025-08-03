import flet as ft
import random
import math


class NumberTheoryModule:
    """Comprehensive Number Theory learning module"""
    
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
        """Show the main number theory page
        Args:
            page: Optional page reference. If not provided, uses self.page
        """
        if page is None:
            page = self.page
        self.page = page  # Update the page reference
            
        view = ft.View(
            "/number_theory",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: page.go_back()),
                    title=ft.Text("Number Theory"),
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
            title=ft.Text("Number Theory"),
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
                            "🔢 Number Theory",
                            size=32,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.BLUE_900,
                            text_align=ft.TextAlign.CENTER
                        ),
                        ft.Text(
                            "Explore the fascinating world of integers and their properties",
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
                        ft.Text("• Understand prime numbers and factorization", size=14),
                        ft.Text("• Learn about divisibility rules", size=14),
                        ft.Text("• Master GCD and LCM calculations", size=14),
                        ft.Text("• Explore modular arithmetic", size=14),
                        ft.Text("• Study Fibonacci sequences", size=14),
                        ft.Text("• Apply number theory in cryptography", size=14),
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
                        ft.Text("🧮 Number Theory Overview", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                        ft.Text("Number theory is the study of integers and their properties. It's one of the oldest branches of mathematics and has applications in modern cryptography, computer science, and digital security.", size=14),
                        
                        ft.Divider(height=10),
                        
                        ft.Text("🔑 Key Concepts:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_800),
                        ft.Text("• Prime numbers: numbers divisible only by 1 and themselves", size=14),
                        ft.Text("• Composite numbers: numbers with more than two factors", size=14),
                        ft.Text("• Greatest Common Divisor (GCD)", size=14),
                        ft.Text("• Least Common Multiple (LCM)", size=14),
                        ft.Text("• Modular arithmetic and congruences", size=14),
                        
                        ft.Divider(height=10),
                        
                        ft.Text("🌟 Applications:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_800),
                        ft.Text("• Cryptography and data security", size=14),
                        ft.Text("• Computer algorithms", size=14),
                        ft.Text("• Error-correcting codes", size=14),
                        ft.Text("• Random number generation", size=14),
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
                        tooltip="Back to Number Theory"
                    ),
                    ft.Text(
                        "📚 Number Theory: Complete Guide",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLUE_900
                    )
                ], alignment=ft.MainAxisAlignment.START),
                
                ft.Divider(),
                
                # Content sections
                ft.Container(
                    ft.Column([
                        ft.Text("1. Prime Numbers", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800),
                        ft.Text("A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.", size=14),
                        ft.Text("Examples: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29...", size=14),
                        ft.Container(
                            ft.Column([
                                ft.Text("Key Properties:", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("• 2 is the only even prime number", size=14),
                                ft.Text("• There are infinitely many prime numbers", size=14),
                                ft.Text("• Every integer > 1 is either prime or composite", size=14),
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
                        ft.Text("2. Prime Factorization", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_800),
                        ft.Text("Every integer greater than 1 can be expressed as a unique product of prime numbers.", size=14),
                        ft.Text("This is called the Fundamental Theorem of Arithmetic.", size=14),
                        ft.Container(
                            ft.Column([
                                ft.Text("Example: 60 = 2² × 3 × 5", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("Steps:", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("60 ÷ 2 = 30", size=14),
                                ft.Text("30 ÷ 2 = 15", size=14),
                                ft.Text("15 ÷ 3 = 5", size=14),
                                ft.Text("5 ÷ 5 = 1", size=14),
                                ft.Text("So 60 = 2² × 3 × 5", size=14),
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
                        ft.Text("3. GCD and LCM", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_800),
                        ft.Text("Greatest Common Divisor (GCD): The largest positive integer that divides both numbers.", size=14),
                        ft.Text("Least Common Multiple (LCM): The smallest positive integer that is divisible by both numbers.", size=14),
                        ft.Container(
                            ft.Column([
                                ft.Text("Euclidean Algorithm for GCD:", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("GCD(48, 18):", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("48 = 18 × 2 + 12", size=14),
                                ft.Text("18 = 12 × 1 + 6", size=14),
                                ft.Text("12 = 6 × 2 + 0", size=14),
                                ft.Text("GCD(48, 18) = 6", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("LCM(48, 18) = (48 × 18) ÷ 6 = 144", size=14),
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
                        ft.Text("4. Modular Arithmetic", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_800),
                        ft.Text("Modular arithmetic deals with remainders after division.", size=14),
                        ft.Text("We write a ≡ b (mod n) if a and b have the same remainder when divided by n.", size=14),
                        ft.Container(
                            ft.Column([
                                ft.Text("Examples:", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("17 ≡ 2 (mod 5) because 17 = 5×3 + 2", size=14),
                                ft.Text("23 ≡ 2 (mod 5) because 23 = 5×4 + 3", size=14),
                                ft.Text("Clock arithmetic: 15:00 + 10 hours = 1:00 (mod 12)", size=14),
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
                        ft.Text("5. Divisibility Rules", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.RED_800),
                        ft.Text("Quick ways to check if a number is divisible by another without performing division:", size=14),
                        ft.Column([
                            ft.Text("• Divisible by 2: Last digit is even (0, 2, 4, 6, 8)", size=14),
                            ft.Text("• Divisible by 3: Sum of digits is divisible by 3", size=14),
                            ft.Text("• Divisible by 5: Last digit is 0 or 5", size=14),
                            ft.Text("• Divisible by 9: Sum of digits is divisible by 9", size=14),
                            ft.Text("• Divisible by 10: Last digit is 0", size=14),
                            ft.Text("• Divisible by 11: Alternating sum of digits is divisible by 11", size=14),
                        ], spacing=5),
                    ], spacing=8),
                    bgcolor=ft.Colors.WHITE,
                    border_radius=10,
                    padding=15,
                    margin=ft.margin.only(bottom=15)
                ),
                
                # Back button
                ft.Container(
                    ft.ElevatedButton(
                        "Back to Number Theory",
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
                        tooltip="Back to Number Theory"
                    ),
                    ft.Text(
                        "💡 Number Theory: Worked Examples",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.ORANGE_900
                    )
                ], alignment=ft.MainAxisAlignment.START),
                
                ft.Divider(),
                
                # Example 1
                ft.Container(
                    ft.Column([
                        ft.Text("Example 1: Finding Prime Factorization", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800),
                        ft.Text("Problem: Find the prime factorization of 84.", size=14),
                        ft.Text("Solution:", size=14, weight=ft.FontWeight.BOLD),
                        ft.Text("Step 1: Start with the smallest prime (2)", size=14),
                        ft.Text("84 ÷ 2 = 42", size=14),
                        ft.Text("42 ÷ 2 = 21", size=14),
                        ft.Text("Step 2: 21 is odd, try next prime (3)", size=14),
                        ft.Text("21 ÷ 3 = 7", size=14),
                        ft.Text("Step 3: 7 is prime", size=14),
                        ft.Container(
                            ft.Text("Answer: 84 = 2² × 3 × 7", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
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
                        ft.Text("Example 2: Using Euclidean Algorithm", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_800),
                        ft.Text("Problem: Find GCD(252, 105) using the Euclidean algorithm.", size=14),
                        ft.Text("Solution:", size=14, weight=ft.FontWeight.BOLD),
                        ft.Text("Step 1: 252 = 105 × 2 + 42", size=14),
                        ft.Text("Step 2: 105 = 42 × 2 + 21", size=14),
                        ft.Text("Step 3: 42 = 21 × 2 + 0", size=14),
                        ft.Text("When remainder is 0, the last non-zero remainder is the GCD.", size=14),
                        ft.Container(
                            ft.Text("Answer: GCD(252, 105) = 21", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
                            bgcolor=ft.Colors.GREEN_50,
                            padding=10,
                            border_radius=5,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        ft.Text("Bonus: LCM(252, 105) = (252 × 105) ÷ 21 = 1260", size=14, style=ft.TextStyle(italic=True)),
                    ], spacing=8),
                    bgcolor=ft.Colors.WHITE,
                    border_radius=10,
                    padding=15,
                    margin=ft.margin.only(bottom=20)
                ),
                
                # Example 3
                ft.Container(
                    ft.Column([
                        ft.Text("Example 3: Checking Divisibility", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_800),
                        ft.Text("Problem: Is 5,367 divisible by 3 and 9?", size=14),
                        ft.Text("Solution:", size=14, weight=ft.FontWeight.BOLD),
                        ft.Text("Step 1: Find sum of digits", size=14),
                        ft.Text("5 + 3 + 6 + 7 = 21", size=14),
                        ft.Text("Step 2: Check divisibility by 3", size=14),
                        ft.Text("21 ÷ 3 = 7, so 21 is divisible by 3", size=14),
                        ft.Text("Therefore, 5,367 is divisible by 3", size=14),
                        ft.Text("Step 3: Check divisibility by 9", size=14),
                        ft.Text("21 ÷ 9 = 2 remainder 3, so 21 is NOT divisible by 9", size=14),
                        ft.Text("Therefore, 5,367 is NOT divisible by 9", size=14),
                        ft.Container(
                            ft.Column([
                                ft.Text("Answer:", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("Divisible by 3: YES", size=14, color=ft.Colors.GREEN_700),
                                ft.Text("Divisible by 9: NO", size=14, color=ft.Colors.RED_700),
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
                        ft.Text("Example 4: Modular Arithmetic Application", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.RED_800),
                        ft.Text("Problem: What day of the week will it be 100 days from today if today is Wednesday?", size=14),
                        ft.Text("Solution:", size=14, weight=ft.FontWeight.BOLD),
                        ft.Text("Step 1: Assign numbers to days", size=14),
                        ft.Text("Sunday=0, Monday=1, Tuesday=2, Wednesday=3, Thursday=4, Friday=5, Saturday=6", size=14),
                        ft.Text("Step 2: Today is Wednesday = 3", size=14),
                        ft.Text("Step 3: Calculate (3 + 100) mod 7", size=14),
                        ft.Text("103 ÷ 7 = 14 remainder 5", size=14),
                        ft.Text("So 103 ≡ 5 (mod 7)", size=14),
                        ft.Container(
                            ft.Text("Answer: Friday (day 5)", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
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
                
                # Back button
                ft.Container(
                    ft.ElevatedButton(
                        "Back to Number Theory",
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
        """Generate quiz questions for number theory"""
        questions = [
            {
                "question": "Which of the following is a prime number?",
                "options": ["21", "27", "29", "33"],
                "correct": 2,
                "explanation": "29 is prime because it's only divisible by 1 and 29. The others have additional factors."
            },
            {
                "question": "What is the prime factorization of 36?",
                "options": ["2² × 3²", "2³ × 3", "2 × 3³", "6²"],
                "correct": 0,
                "explanation": "36 = 4 × 9 = 2² × 3²"
            },
            {
                "question": "What is GCD(48, 18)?",
                "options": ["3", "6", "9", "12"],
                "correct": 1,
                "explanation": "Using Euclidean algorithm: 48 = 18×2 + 12, 18 = 12×1 + 6, 12 = 6×2 + 0. GCD = 6"
            },
            {
                "question": "What is LCM(12, 18)?",
                "options": ["36", "54", "72", "216"],
                "correct": 0,
                "explanation": "LCM(12,18) = (12×18)÷GCD(12,18) = 216÷6 = 36"
            },
            {
                "question": "Is 87 divisible by 3?",
                "options": ["Yes", "No", "Cannot determine", "Only if it's even"],
                "correct": 0,
                "explanation": "Sum of digits: 8+7=15. Since 15 is divisible by 3, so is 87."
            },
            {
                "question": "What is 23 mod 7?",
                "options": ["2", "3", "4", "5"],
                "correct": 0,
                "explanation": "23 ÷ 7 = 3 remainder 2, so 23 ≡ 2 (mod 7)"
            },
            {
                "question": "How many prime numbers are there less than 20?",
                "options": ["7", "8", "9", "10"],
                "correct": 1,
                "explanation": "Primes less than 20: 2, 3, 5, 7, 11, 13, 17, 19. That's 8 primes."
            },
            {
                "question": "Which number is NOT divisible by 9?",
                "options": ["144", "207", "351", "423"],
                "correct": 3,
                "explanation": "Sum of digits for 423: 4+2+3=9, which IS divisible by 9. Check others: 144(9), 207(9), 351(9). All are divisible by 9."
            },
            {
                "question": "What is the smallest composite number?",
                "options": ["2", "4", "6", "8"],
                "correct": 1,
                "explanation": "4 is the smallest composite number (4 = 2×2). 2 is prime, not composite."
            },
            {
                "question": "If today is Monday, what day will it be in 50 days?",
                "options": ["Monday", "Tuesday", "Wednesday", "Thursday"],
                "correct": 2,
                "explanation": "50 mod 7 = 1 (since 50 = 7×7 + 1). Monday + 1 day = Tuesday. Wait, let me recalculate: 50 ÷ 7 = 7 remainder 1, so it's Tuesday."
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
                        tooltip="Back to Number Theory"
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
            message = "Outstanding! You've mastered number theory concepts!"
            color = ft.Colors.GREEN_600
        elif percentage >= 80:
            grade = "A"
            message = "Excellent work! You have a strong understanding of number theory."
            color = ft.Colors.GREEN_600
        elif percentage >= 70:
            grade = "B"
            message = "Good job! You understand most number theory concepts."
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
                            "Back to Number Theory",
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
            label="Ask me anything about number theory...",
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
                        tooltip="Back to Number Theory"
                    ),
                    ft.Text(
                        "🤖 AI Tutor - Number Theory Help",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.PURPLE_900
                    )
                ], alignment=ft.MainAxisAlignment.START),
                
                ft.Divider(),
                
                # Instructions
                ft.Container(
                    ft.Column([
                        ft.Text("💬 Ask me anything about number theory!", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_800),
                        ft.Text("I can help with:", size=14),
                        ft.Text("• Prime numbers and factorization", size=12),
                        ft.Text("• GCD and LCM calculations", size=12),
                        ft.Text("• Modular arithmetic", size=12),
                        ft.Text("• Divisibility rules", size=12),
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
                            "Prime Numbers",
                            on_click=lambda e: self._quick_help("primes"),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.PURPLE_100)
                        ),
                        col={'xs': 6, 'sm': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            "GCD/LCM",
                            on_click=lambda e: self._quick_help("gcd"),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.PURPLE_100)
                        ),
                        col={'xs': 6, 'sm': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            "Modular Math",
                            on_click=lambda e: self._quick_help("modular"),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.PURPLE_100)
                        ),
                        col={'xs': 6, 'sm': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            "Divisibility",
                            on_click=lambda e: self._quick_help("divisibility"),
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
            "primes": "Prime numbers are integers greater than 1 that have exactly two positive divisors: 1 and themselves. Examples: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29... The number 2 is the only even prime.",
            "gcd": "GCD (Greatest Common Divisor) is the largest number that divides both numbers. Use the Euclidean algorithm: repeatedly divide and take remainders until you get 0. LCM = (a×b)÷GCD(a,b).",
            "modular": "Modular arithmetic deals with remainders. a ≡ b (mod n) means a and b have the same remainder when divided by n. It's like clock arithmetic - useful in cryptography and computer science.",
            "divisibility": "Quick divisibility rules: By 2 (last digit even), by 3 (sum of digits divisible by 3), by 5 (ends in 0 or 5), by 9 (sum of digits divisible by 9), by 11 (alternating sum divisible by 11)."
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
        
        if "prime" in question_lower:
            return "Prime numbers are fundamental building blocks in number theory. A prime has exactly two factors: 1 and itself. To check if a number is prime, test divisibility by all primes up to its square root. Would you like me to help check a specific number?"
        
        elif "gcd" in question_lower or "greatest common divisor" in question_lower:
            return "To find GCD, use the Euclidean algorithm: divide the larger by smaller, then replace the larger with the remainder. Repeat until remainder is 0. The last non-zero remainder is the GCD. Want me to show an example?"
        
        elif "lcm" in question_lower or "least common multiple" in question_lower:
            return "LCM can be found using: LCM(a,b) = (a × b) ÷ GCD(a,b). Or find prime factorizations and take the highest power of each prime factor. Which method would you like me to demonstrate?"
        
        elif "modular" in question_lower or "mod" in question_lower:
            return "Modular arithmetic is 'clock math'. When we say a ≡ b (mod n), it means a and b have the same remainder when divided by n. For example, 17 ≡ 3 (mod 7) because both have remainder 3. What would you like to practice?"
        
        elif "divisible" in question_lower or "divisibility" in question_lower:
            return "Divisibility rules help check factors quickly. For 3: sum of digits divisible by 3. For 9: sum of digits divisible by 9. For 11: alternating sum divisible by 11. Which rule would you like me to explain further?"
        
        elif "factor" in question_lower:
            return "Prime factorization breaks a number into prime factors. Start with smallest primes (2,3,5,7...) and divide repeatedly. Every integer > 1 has a unique prime factorization. Want to factor a specific number together?"
        
        elif "composite" in question_lower:
            return "Composite numbers have more than two factors. They can be written as products of smaller positive integers. Examples: 4=2×2, 6=2×3, 8=2×4, 9=3×3. The smallest composite number is 4."
        
        else:
            return "That's an interesting question about number theory! I can help with prime numbers, factorization, GCD/LCM, modular arithmetic, or divisibility rules. What specific concept would you like to explore?"


def number_theory_page(page: ft.Page):
    """Main entry point for Number Theory module"""
    module = NumberTheoryModule(page)
    module.show_page()
