import flet as ft
import random
import math


class ComplexNumbersModule:
    """Comprehensive Complex Numbers learning module"""
    
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
        """Display the main Complex Numbers page
        Args:
            page: Optional page reference. If not provided, uses self.page
        """
        if page is None:
            page = self.page
        self.page = page  # Update the page reference
            
        view = ft.View(
            "/complex_numbers",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: page.go_back()),
                    title=ft.Text("Complex Numbers"),
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
            title=ft.Text("Complex Numbers"),
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
                            "🔢 Complex Numbers",
                            size=32,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.BLUE_900,
                            text_align=ft.TextAlign.CENTER
                        ),
                        ft.Text(
                            "Explore the extended number system with real and imaginary parts",
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
                        ft.Text("• Understand complex number notation (a + bi)", size=14),
                        ft.Text("• Perform arithmetic operations with complex numbers", size=14),
                        ft.Text("• Convert between rectangular and polar forms", size=14),
                        ft.Text("• Calculate complex conjugates and modulus", size=14),
                        ft.Text("• Apply De Moivre's theorem", size=14),
                        ft.Text("• Solve equations with complex solutions", size=14),
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
                        ft.Text("🌟 Complex Numbers Overview", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                        ft.Text("Complex numbers extend the real number system to include solutions to equations like x² + 1 = 0. They consist of a real part and an imaginary part, written as a + bi where i is the imaginary unit (√(-1)).", size=14),
                        
                        ft.Divider(height=10),
                        
                        ft.Text("🔑 Key Concepts:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_800),
                        ft.Text("• Standard form: z = a + bi (a, b are real numbers)", size=14),
                        ft.Text("• Imaginary unit: i = √(-1), so i² = -1", size=14),
                        ft.Text("• Complex conjugate: z̄ = a - bi", size=14),
                        ft.Text("• Modulus (magnitude): |z| = √(a² + b²)", size=14),
                        ft.Text("• Polar form: z = r(cos θ + i sin θ)", size=14),
                        
                        ft.Divider(height=10),
                        
                        ft.Text("🌟 Applications:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_800),
                        ft.Text("• Electrical engineering (AC circuits)", size=14),
                        ft.Text("• Signal processing and Fourier transforms", size=14),
                        ft.Text("• Quantum mechanics", size=14),
                        ft.Text("• Computer graphics and fractals", size=14),
                        ft.Text("• Control systems engineering", size=14),
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
                        tooltip="Back to Complex Numbers"
                    ),
                    ft.Text(
                        "📚 Complex Numbers: Complete Guide",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLUE_900
                    )
                ], alignment=ft.MainAxisAlignment.START),
                
                ft.Divider(),
                
                # Content sections
                ft.Container(
                    ft.Column([
                        ft.Text("1. Introduction to Complex Numbers", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800),
                        ft.Text("Complex numbers were invented to solve equations that have no real solutions, like x² + 1 = 0.", size=14),
                        ft.Container(
                            ft.Column([
                                ft.Text("The imaginary unit: i = √(-1)", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("Therefore: i² = -1, i³ = -i, i⁴ = 1", size=14),
                                ft.Text("Standard form: z = a + bi", size=14),
                                ft.Text("where a = real part, b = imaginary part", size=14),
                                ft.Text("Examples:", size=14),
                                ft.Text("• 3 + 4i (a=3, b=4)", size=14),
                                ft.Text("• 2 - 5i (a=2, b=-5)", size=14),
                                ft.Text("• 7 (a=7, b=0, purely real)", size=14),
                                ft.Text("• 3i (a=0, b=3, purely imaginary)", size=14),
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
                        ft.Text("2. Arithmetic Operations", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_800),
                        ft.Text("Complex numbers can be added, subtracted, multiplied, and divided like algebraic expressions.", size=14),
                        ft.Container(
                            ft.Column([
                                ft.Text("Addition: (a+bi) + (c+di) = (a+c) + (b+d)i", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("Subtraction: (a+bi) - (c+di) = (a-c) + (b-d)i", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("Multiplication: (a+bi)(c+di) = (ac-bd) + (ad+bc)i", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("Division: (a+bi)/(c+di) = [(a+bi)(c-di)]/[c²+d²]", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("Example: (2+3i) + (1-2i) = 3+i", size=14),
                                ft.Text("Example: (2+3i)(1-2i) = 2-4i+3i-6i² = 2-i+6 = 8-i", size=14),
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
                        ft.Text("3. Complex Conjugate and Modulus", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_800),
                        ft.Text("The complex conjugate and modulus are important properties of complex numbers.", size=14),
                        ft.Container(
                            ft.Column([
                                ft.Text("Complex Conjugate: z̄ = a - bi", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("If z = 3 + 4i, then z̄ = 3 - 4i", size=14),
                                ft.Text("Properties: z + z̄ = 2a, z × z̄ = a² + b²", size=14),
                                ft.Text("Modulus (Magnitude): |z| = √(a² + b²)", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("If z = 3 + 4i, then |z| = √(3² + 4²) = √25 = 5", size=14),
                                ft.Text("Geometric interpretation: distance from origin", size=14),
                                ft.Text("Property: |z₁ × z₂| = |z₁| × |z₂|", size=14),
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
                        ft.Text("4. Polar Form", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_800),
                        ft.Text("Complex numbers can be represented in polar form using magnitude and angle.", size=14),
                        ft.Container(
                            ft.Column([
                                ft.Text("Polar form: z = r(cos θ + i sin θ) = re^(iθ)", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("where r = |z| = √(a² + b²)", size=14),
                                ft.Text("and θ = arg(z) = arctan(b/a)", size=14),
                                ft.Text("Conversion from rectangular to polar:", size=14),
                                ft.Text("r = √(a² + b²)", size=14),
                                ft.Text("θ = arctan(b/a) (adjust for quadrant)", size=14),
                                ft.Text("Conversion from polar to rectangular:", size=14),
                                ft.Text("a = r cos θ", size=14),
                                ft.Text("b = r sin θ", size=14),
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
                        ft.Text("5. De Moivre's Theorem", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.RED_800),
                        ft.Text("De Moivre's theorem simplifies powers and roots of complex numbers in polar form.", size=14),
                        ft.Container(
                            ft.Column([
                                ft.Text("De Moivre's Theorem:", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("[r(cos θ + i sin θ)]ⁿ = rⁿ(cos nθ + i sin nθ)", size=14),
                                ft.Text("For roots: z^(1/n) = r^(1/n)[cos(θ+2πk)/n + i sin(θ+2πk)/n]", size=14),
                                ft.Text("where k = 0, 1, 2, ..., n-1", size=14),
                                ft.Text("Applications:", size=14),
                                ft.Text("• Finding powers of complex numbers", size=14),
                                ft.Text("• Finding nth roots", size=14),
                                ft.Text("• Solving polynomial equations", size=14),
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
                        "Back to Complex Numbers",
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
                        tooltip="Back to Complex Numbers"
                    ),
                    ft.Text(
                        "💡 Complex Numbers: Worked Examples",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.ORANGE_900
                    )
                ], alignment=ft.MainAxisAlignment.START),
                
                ft.Divider(),
                
                # Example 1
                ft.Container(
                    ft.Column([
                        ft.Text("Example 1: Complex Number Addition", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800),
                        ft.Text("Problem: Add (3 + 2i) + (1 - 4i)", size=14),
                        ft.Text("Solution:", size=14, weight=ft.FontWeight.BOLD),
                        ft.Text("Step 1: Add the real parts", size=14),
                        ft.Text("3 + 1 = 4", size=14),
                        ft.Text("Step 2: Add the imaginary parts", size=14),
                        ft.Text("2i + (-4i) = -2i", size=14),
                        ft.Text("Step 3: Combine the results", size=14),
                        ft.Container(
                            ft.Text("Answer: 4 - 2i", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
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
                        ft.Text("Example 2: Complex Number Multiplication", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_800),
                        ft.Text("Problem: Multiply (2 + 3i)(1 - 2i)", size=14),
                        ft.Text("Solution:", size=14, weight=ft.FontWeight.BOLD),
                        ft.Text("Step 1: Use FOIL method", size=14),
                        ft.Text("First: 2 × 1 = 2", size=14),
                        ft.Text("Outer: 2 × (-2i) = -4i", size=14),
                        ft.Text("Inner: 3i × 1 = 3i", size=14),
                        ft.Text("Last: 3i × (-2i) = -6i²", size=14),
                        ft.Text("Step 2: Simplify using i² = -1", size=14),
                        ft.Text("-6i² = -6(-1) = 6", size=14),
                        ft.Text("Step 3: Combine like terms", size=14),
                        ft.Text("2 + (-4i) + 3i + 6 = 8 - i", size=14),
                        ft.Container(
                            ft.Text("Answer: 8 - i", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
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
                        ft.Text("Example 3: Finding Modulus and Conjugate", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_800),
                        ft.Text("Problem: Find the modulus and conjugate of z = 3 - 4i", size=14),
                        ft.Text("Solution:", size=14, weight=ft.FontWeight.BOLD),
                        ft.Text("Finding the conjugate:", size=14),
                        ft.Text("z̄ = 3 - (-4)i = 3 + 4i", size=14),
                        ft.Text("Finding the modulus:", size=14),
                        ft.Text("|z| = √(a² + b²)", size=14),
                        ft.Text("|z| = √(3² + (-4)²)", size=14),
                        ft.Text("|z| = √(9 + 16)", size=14),
                        ft.Text("|z| = √25 = 5", size=14),
                        ft.Container(
                            ft.Column([
                                ft.Text("Answer:", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("Conjugate: z̄ = 3 + 4i", size=14),
                                ft.Text("Modulus: |z| = 5", size=14),
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
                        ft.Text("Example 4: Converting to Polar Form", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.RED_800),
                        ft.Text("Problem: Convert z = 1 + i to polar form", size=14),
                        ft.Text("Solution:", size=14, weight=ft.FontWeight.BOLD),
                        ft.Text("Step 1: Find the modulus r", size=14),
                        ft.Text("r = √(1² + 1²) = √2", size=14),
                        ft.Text("Step 2: Find the argument θ", size=14),
                        ft.Text("θ = arctan(1/1) = arctan(1) = π/4", size=14),
                        ft.Text("(Since both parts are positive, z is in quadrant I)", size=14),
                        ft.Text("Step 3: Write in polar form", size=14),
                        ft.Text("z = r(cos θ + i sin θ)", size=14),
                        ft.Text("z = √2(cos π/4 + i sin π/4)", size=14),
                        ft.Container(
                            ft.Text("Answer: z = √2(cos π/4 + i sin π/4)", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
                            bgcolor=ft.Colors.GREEN_50,
                            padding=10,
                            border_radius=5,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        ft.Text("Or in exponential form: z = √2 e^(iπ/4)", size=14, style=ft.TextStyle(italic=True)),
                    ], spacing=8),
                    bgcolor=ft.Colors.WHITE,
                    border_radius=10,
                    padding=15,
                    margin=ft.margin.only(bottom=20)
                ),
                
                # Back button
                ft.Container(
                    ft.ElevatedButton(
                        "Back to Complex Numbers",
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
        """Generate quiz questions for complex numbers"""
        questions = [
            {
                "question": "What is i²?",
                "options": ["i", "-1", "1", "-i"],
                "correct": 1,
                "explanation": "By definition, i = √(-1), so i² = -1"
            },
            {
                "question": "What is (2 + 3i) + (1 - 2i)?",
                "options": ["3 + i", "3 - i", "1 + 5i", "3 + 5i"],
                "correct": 0,
                "explanation": "Add real parts: 2+1=3, add imaginary parts: 3i+(-2i)=i, so answer is 3+i"
            },
            {
                "question": "What is the conjugate of 4 - 5i?",
                "options": ["4 + 5i", "-4 + 5i", "-4 - 5i", "5 - 4i"],
                "correct": 0,
                "explanation": "The conjugate changes the sign of the imaginary part: 4 - 5i becomes 4 + 5i"
            },
            {
                "question": "What is |3 + 4i|?",
                "options": ["5", "7", "25", "√7"],
                "correct": 0,
                "explanation": "|3 + 4i| = √(3² + 4²) = √(9 + 16) = √25 = 5"
            },
            {
                "question": "What is i³?",
                "options": ["i", "-i", "1", "-1"],
                "correct": 1,
                "explanation": "i³ = i² × i = (-1) × i = -i"
            },
            {
                "question": "What is (1 + i)(1 - i)?",
                "options": ["2", "0", "2i", "1"],
                "correct": 0,
                "explanation": "(1+i)(1-i) = 1² - i² = 1 - (-1) = 1 + 1 = 2"
            },
            {
                "question": "In the complex plane, what does the real part represent?",
                "options": ["y-coordinate", "x-coordinate", "angle", "distance"],
                "correct": 1,
                "explanation": "In the complex plane, the real part is plotted on the x-axis (horizontal coordinate)"
            },
            {
                "question": "What is the polar form representation of i?",
                "options": ["1(cos π/2 + i sin π/2)", "1(cos 0 + i sin 0)", "1(cos π + i sin π)", "1(cos 3π/2 + i sin 3π/2)"],
                "correct": 0,
                "explanation": "i = 0 + 1i has r=1 and θ=π/2, so i = 1(cos π/2 + i sin π/2)"
            },
            {
                "question": "What is i⁴?",
                "options": ["-1", "i", "-i", "1"],
                "correct": 3,
                "explanation": "i⁴ = (i²)² = (-1)² = 1"
            },
            {
                "question": "Which equation has complex solutions?",
                "options": ["x² - 4 = 0", "x² + 1 = 0", "x² - 1 = 0", "x² - 9 = 0"],
                "correct": 1,
                "explanation": "x² + 1 = 0 gives x² = -1, so x = ±i (complex solutions)"
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
                        tooltip="Back to Complex Numbers"
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
            message = "Outstanding! You've mastered complex numbers!"
            color = ft.Colors.GREEN_600
        elif percentage >= 80:
            grade = "A"
            message = "Excellent work! You have a strong understanding of complex numbers."
            color = ft.Colors.GREEN_600
        elif percentage >= 70:
            grade = "B"
            message = "Good job! You understand most complex number concepts."
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
                            "Back to Complex Numbers",
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
            label="Ask me anything about complex numbers...",
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
                        tooltip="Back to Complex Numbers"
                    ),
                    ft.Text(
                        "🤖 AI Tutor - Complex Numbers Help",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.PURPLE_900
                    )
                ], alignment=ft.MainAxisAlignment.START),
                
                ft.Divider(),
                
                # Instructions
                ft.Container(
                    ft.Column([
                        ft.Text("💬 Ask me anything about complex numbers!", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_800),
                        ft.Text("I can help with:", size=14),
                        ft.Text("• Basic operations (addition, multiplication)", size=12),
                        ft.Text("• Complex conjugates and modulus", size=12),
                        ft.Text("• Polar and rectangular forms", size=12),
                        ft.Text("• Powers and roots using De Moivre's theorem", size=12),
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
                            "Basic Operations",
                            on_click=lambda e: self._quick_help("operations"),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.PURPLE_100)
                        ),
                        col={'xs': 6, 'sm': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            "Conjugate/Modulus",
                            on_click=lambda e: self._quick_help("properties"),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.PURPLE_100)
                        ),
                        col={'xs': 6, 'sm': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            "Polar Form",
                            on_click=lambda e: self._quick_help("polar"),
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
            "operations": "Complex number operations: Addition/subtraction (combine like terms), multiplication (use FOIL and i²=-1), division (multiply by conjugate). Example: (2+3i)+(1-2i) = 3+i",
            "properties": "Complex conjugate: change sign of imaginary part (3+4i → 3-4i). Modulus: |a+bi| = √(a²+b²), represents distance from origin. These are key for division and geometric interpretation.",
            "polar": "Polar form: z = r(cos θ + i sin θ) where r = |z| and θ = arg(z). Convert: r = √(a²+b²), θ = arctan(b/a). Useful for multiplication, powers, and roots.",
            "applications": "Complex numbers are essential in: electrical engineering (AC circuits), signal processing (Fourier transforms), quantum mechanics, computer graphics, and solving polynomial equations with no real roots."
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
        
        if "imaginary unit" in question_lower or "what is i" in question_lower:
            return "The imaginary unit i is defined as √(-1). Key properties: i² = -1, i³ = -i, i⁴ = 1, and the pattern repeats. It allows us to extend the real numbers to solve equations like x² + 1 = 0."
        
        elif "addition" in question_lower or "add" in question_lower:
            return "To add complex numbers, add the real parts and imaginary parts separately: (a+bi) + (c+di) = (a+c) + (b+d)i. Example: (3+2i) + (1-4i) = 4-2i. It's just like combining like terms in algebra!"
        
        elif "multiplication" in question_lower or "multiply" in question_lower:
            return "Multiply complex numbers using FOIL, then simplify using i² = -1: (a+bi)(c+di) = ac + adi + bci + bdi² = (ac-bd) + (ad+bc)i. Remember that i² = -1 is key to simplification."
        
        elif "conjugate" in question_lower:
            return "The complex conjugate of a+bi is a-bi (flip the sign of the imaginary part). It's useful for division and finding modulus. Key property: z × z̄ = |z|² (a real number)."
        
        elif "modulus" in question_lower or "magnitude" in question_lower:
            return "The modulus |a+bi| = √(a²+b²) represents the distance from the origin in the complex plane. It's like the length of a vector. For geometric problems and polar form, modulus is essential."
        
        elif "polar" in question_lower or "polar form" in question_lower:
            return "Polar form: z = r(cos θ + i sin θ) where r = |z| and θ = arg(z). To convert: r = √(a²+b²), θ = arctan(b/a). Polar form makes multiplication and powers much easier!"
        
        elif "division" in question_lower or "divide" in question_lower:
            return "To divide complex numbers, multiply numerator and denominator by the conjugate of the denominator: (a+bi)/(c+di) = (a+bi)(c-di)/[(c+di)(c-di)] = (a+bi)(c-di)/(c²+d²)."
        
        elif "de moivre" in question_lower:
            return "De Moivre's theorem: [r(cos θ + i sin θ)]ⁿ = rⁿ(cos nθ + i sin nθ). It makes finding powers and roots of complex numbers much easier when in polar form. Great for solving polynomial equations!"
        
        elif "complex plane" in question_lower:
            return "The complex plane plots complex numbers as points: real part on x-axis, imaginary part on y-axis. So 3+4i is at point (3,4). This geometric view helps visualize operations and relationships."
        
        else:
            return "Great question about complex numbers! I can help with the imaginary unit i, arithmetic operations, complex conjugates, modulus/magnitude, polar form, De Moivre's theorem, or any specific calculations. What would you like to explore?"


def complex_numbers_page(page: ft.Page):
    """Main entry point for Complex Numbers module"""
    module = ComplexNumbersModule(page)
    module.show_page()
