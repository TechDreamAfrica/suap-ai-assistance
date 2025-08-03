import flet as ft
import random
import math


class DifferentialEquationsModule:
    """Comprehensive Differential Equations learning module"""
    
    def __init__(self, page=None):
        self.page = page
        self.current_question = 0
        self.score = 0
        self.quiz_questions = self._generate_quiz_questions()
        self.selected_answer = None
        
    def show_main_page(self, page=None):
        """Show the main differential equations page
        Args:
            page: Optional page reference. If not provided, uses self.page
        """
        if page is None:
            page = self.page
        self.page = page  # Update the page reference
            
        view = ft.View(
            "/differential_equations",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: page.go_back()),
                    title=ft.Text("Differential Equations"),
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
            title=ft.Text("Differential Equations"),
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
                            "📈 Differential Equations",
                            size=32,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.BLUE_900,
                            text_align=ft.TextAlign.CENTER
                        ),
                        ft.Text(
                            "Master the mathematics of change and rates",
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
                        ft.Text("• Understand first and second-order differential equations", size=14),
                        ft.Text("• Master separation of variables technique", size=14),
                        ft.Text("• Solve linear differential equations", size=14),
                        ft.Text("• Apply initial value problems and boundary conditions", size=14),
                        ft.Text("• Use Laplace transforms for solving DEs", size=14),
                        ft.Text("• Model real-world phenomena with differential equations", size=14),
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
                        ft.Text("🌟 Differential Equations Overview", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                        ft.Text("Differential equations are mathematical equations that relate functions with their derivatives. They describe how quantities change and are fundamental to modeling dynamic systems in science and engineering.", size=14),
                        
                        ft.Divider(height=10),
                        
                        ft.Text("🔑 Key Types:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_800),
                        ft.Text("• Ordinary DEs (ODEs): Functions of one variable", size=14),
                        ft.Text("• Partial DEs (PDEs): Functions of multiple variables", size=14),
                        ft.Text("• Linear vs Nonlinear equations", size=14),
                        ft.Text("• First-order: dy/dx = f(x,y)", size=14),
                        ft.Text("• Second-order: d²y/dx² + p(x)dy/dx + q(x)y = g(x)", size=14),
                        
                        ft.Divider(height=10),
                        
                        ft.Text("🌟 Applications:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_800),
                        ft.Text("• Population growth and decay models", size=14),
                        ft.Text("• Motion and mechanics (Newton's laws)", size=14),
                        ft.Text("• Heat conduction and diffusion", size=14),
                        ft.Text("• Electrical circuits and oscillations", size=14),
                        ft.Text("• Economics and finance modeling", size=14),
                        ft.Text("• Chemical reaction rates", size=14),
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
                        tooltip="Back to Differential Equations"
                    ),
                    ft.Text(
                        "📚 Differential Equations: Complete Guide",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLUE_900
                    )
                ], alignment=ft.MainAxisAlignment.START),
                
                ft.Divider(),
                
                # Content sections
                ft.Container(
                    ft.Column([
                        ft.Text("1. Introduction to Differential Equations", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800),
                        ft.Text("A differential equation is an equation involving an unknown function and its derivatives.", size=14),
                        ft.Container(
                            ft.Column([
                                ft.Text("Order: The highest derivative in the equation", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("First-order: dy/dx = 2x (only first derivative)", size=14),
                                ft.Text("Second-order: d²y/dx² + 3dy/dx + 2y = 0", size=14),
                                ft.Text("Linear: No products or powers of y and its derivatives", size=14),
                                ft.Text("Linear example: dy/dx + 2y = x", size=14),
                                ft.Text("Nonlinear example: dy/dx = y²", size=14),
                                ft.Text("Solution: A function y(x) that satisfies the equation", size=14),
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
                        ft.Text("2. Separation of Variables", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_800),
                        ft.Text("A method for solving first-order DEs by separating variables on different sides.", size=14),
                        ft.Container(
                            ft.Column([
                                ft.Text("Method for dy/dx = f(x)g(y):", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("1. Rewrite as dy/g(y) = f(x)dx", size=14),
                                ft.Text("2. Integrate both sides", size=14),
                                ft.Text("3. ∫ dy/g(y) = ∫ f(x)dx + C", size=14),
                                ft.Text("Example: dy/dx = xy", size=14),
                                ft.Text("Solution: dy/y = x dx", size=14),
                                ft.Text("Integrating: ln|y| = x²/2 + C", size=14),
                                ft.Text("General solution: y = Ae^(x²/2)", size=14),
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
                        ft.Text("3. Linear First-Order Equations", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_800),
                        ft.Text("Standard form: dy/dx + p(x)y = q(x), solved using integrating factors.", size=14),
                        ft.Container(
                            ft.Column([
                                ft.Text("Integrating Factor Method:", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("1. Write in standard form: dy/dx + p(x)y = q(x)", size=14),
                                ft.Text("2. Find integrating factor: μ(x) = e^∫p(x)dx", size=14),
                                ft.Text("3. Multiply equation by μ(x)", size=14),
                                ft.Text("4. Left side becomes d/dx[μ(x)y]", size=14),
                                ft.Text("5. Integrate: μ(x)y = ∫μ(x)q(x)dx + C", size=14),
                                ft.Text("6. Solve for y", size=14),
                                ft.Text("Example: dy/dx + 2y = 4x", size=14),
                                ft.Text("μ(x) = e^∫2dx = e^2x", size=14),
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
                        ft.Text("4. Second-Order Linear Equations", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_800),
                        ft.Text("Form: ay'' + by' + cy = 0 (homogeneous) or ay'' + by' + cy = f(x) (non-homogeneous).", size=14),
                        ft.Container(
                            ft.Column([
                                ft.Text("Characteristic Equation Method:", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("For ay'' + by' + cy = 0:", size=14),
                                ft.Text("1. Substitute y = e^rx to get ar² + br + c = 0", size=14),
                                ft.Text("2. Solve quadratic for roots r₁, r₂", size=14),
                                ft.Text("3. Real distinct roots: y = c₁e^r₁x + c₂e^r₂x", size=14),
                                ft.Text("4. Real repeated root: y = (c₁ + c₂x)e^rx", size=14),
                                ft.Text("5. Complex roots r = α ± βi:", size=14),
                                ft.Text("   y = e^αx(c₁cos(βx) + c₂sin(βx))", size=14),
                                ft.Text("Example: y'' - 3y' + 2y = 0", size=14),
                                ft.Text("Characteristic: r² - 3r + 2 = 0", size=14),
                                ft.Text("Roots: r = 1, 2; Solution: y = c₁e^x + c₂e^2x", size=14),
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
                        ft.Text("5. Applications and Modeling", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.RED_800),
                        ft.Text("Differential equations model real-world phenomena involving rates of change.", size=14),
                        ft.Container(
                            ft.Column([
                                ft.Text("Common Models:", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("Population Growth: dp/dt = kp (exponential)", size=14),
                                ft.Text("Logistic Growth: dp/dt = kp(1 - p/M)", size=14),
                                ft.Text("Newton's Cooling: dT/dt = -k(T - T_env)", size=14),
                                ft.Text("Free Fall: d²y/dt² = -g", size=14),
                                ft.Text("Simple Harmonic Motion: d²x/dt² + ω²x = 0", size=14),
                                ft.Text("RC Circuit: RC(dq/dt) + q = V₀", size=14),
                                ft.Text("Compound Interest: dA/dt = rA", size=14),
                                ft.Text("Chemical Reactions: dc/dt = -kc^n", size=14),
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
                        "Back to Differential Equations",
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
                        tooltip="Back to Differential Equations"
                    ),
                    ft.Text(
                        "💡 Differential Equations: Worked Examples",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.ORANGE_900
                    )
                ], alignment=ft.MainAxisAlignment.START),
                
                ft.Divider(),
                
                # Example 1
                ft.Container(
                    ft.Column([
                        ft.Text("Example 1: Separation of Variables", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800),
                        ft.Text("Problem: Solve dy/dx = 3xy with initial condition y(0) = 2", size=14),
                        ft.Text("Solution:", size=14, weight=ft.FontWeight.BOLD),
                        ft.Text("Step 1: Separate variables", size=14),
                        ft.Text("dy/y = 3x dx", size=14),
                        ft.Text("Step 2: Integrate both sides", size=14),
                        ft.Text("∫ dy/y = ∫ 3x dx", size=14),
                        ft.Text("ln|y| = (3/2)x² + C", size=14),
                        ft.Text("Step 3: Solve for y", size=14),
                        ft.Text("y = Ae^((3/2)x²)", size=14),
                        ft.Text("Step 4: Apply initial condition y(0) = 2", size=14),
                        ft.Text("2 = Ae^0 = A, so A = 2", size=14),
                        ft.Container(
                            ft.Text("Answer: y = 2e^((3/2)x²)", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
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
                        ft.Text("Example 2: Linear First-Order with Integrating Factor", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_800),
                        ft.Text("Problem: Solve dy/dx + 2y = 6e^(-x)", size=14),
                        ft.Text("Solution:", size=14, weight=ft.FontWeight.BOLD),
                        ft.Text("Step 1: Identify p(x) = 2, q(x) = 6e^(-x)", size=14),
                        ft.Text("Step 2: Find integrating factor", size=14),
                        ft.Text("μ(x) = e^∫2dx = e^2x", size=14),
                        ft.Text("Step 3: Multiply equation by μ(x)", size=14),
                        ft.Text("e^2x(dy/dx) + 2e^2x·y = 6e^2x·e^(-x)", size=14),
                        ft.Text("d/dx[e^2x·y] = 6e^x", size=14),
                        ft.Text("Step 4: Integrate both sides", size=14),
                        ft.Text("e^2x·y = 6e^x + C", size=14),
                        ft.Text("Step 5: Solve for y", size=14),
                        ft.Container(
                            ft.Text("Answer: y = 6e^(-x) + Ce^(-2x)", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
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
                        ft.Text("Example 3: Second-Order Homogeneous", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_800),
                        ft.Text("Problem: Solve y'' - 5y' + 6y = 0", size=14),
                        ft.Text("Solution:", size=14, weight=ft.FontWeight.BOLD),
                        ft.Text("Step 1: Write characteristic equation", size=14),
                        ft.Text("r² - 5r + 6 = 0", size=14),
                        ft.Text("Step 2: Factor or use quadratic formula", size=14),
                        ft.Text("(r - 2)(r - 3) = 0", size=14),
                        ft.Text("r₁ = 2, r₂ = 3", size=14),
                        ft.Text("Step 3: Write general solution", size=14),
                        ft.Text("Since roots are real and distinct:", size=14),
                        ft.Container(
                            ft.Text("Answer: y = c₁e^(2x) + c₂e^(3x)", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
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
                        ft.Text("Example 4: Population Growth Model", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.RED_800),
                        ft.Text("Problem: A population grows at a rate proportional to its size. If P(0) = 1000 and P(2) = 1500, find P(t).", size=14),
                        ft.Text("Solution:", size=14, weight=ft.FontWeight.BOLD),
                        ft.Text("Step 1: Set up the DE", size=14),
                        ft.Text("dP/dt = kP (k is growth constant)", size=14),
                        ft.Text("Step 2: Solve by separation", size=14),
                        ft.Text("dP/P = k dt", size=14),
                        ft.Text("ln|P| = kt + C", size=14),
                        ft.Text("P = Ae^(kt)", size=14),
                        ft.Text("Step 3: Apply initial condition P(0) = 1000", size=14),
                        ft.Text("1000 = Ae^0 = A, so A = 1000", size=14),
                        ft.Text("P(t) = 1000e^(kt)", size=14),
                        ft.Text("Step 4: Use P(2) = 1500 to find k", size=14),
                        ft.Text("1500 = 1000e^(2k)", size=14),
                        ft.Text("1.5 = e^(2k)", size=14),
                        ft.Text("ln(1.5) = 2k", size=14),
                        ft.Text("k = ln(1.5)/2 ≈ 0.203", size=14),
                        ft.Container(
                            ft.Text("Answer: P(t) = 1000e^(0.203t)", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
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
                        "Back to Differential Equations",
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
        """Generate quiz questions for differential equations"""
        questions = [
            {
                "question": "What is the order of the differential equation y'' + 3y' - 2y = 0?",
                "options": ["First order", "Second order", "Third order", "Zero order"],
                "correct": 1,
                "explanation": "The order is determined by the highest derivative. Here y'' is the highest, so it's second order."
            },
            {
                "question": "Which method is used to solve dy/dx = 2xy?",
                "options": ["Integrating factor", "Separation of variables", "Characteristic equation", "Laplace transform"],
                "correct": 1,
                "explanation": "Since variables can be separated (dy/y = 2x dx), separation of variables is the appropriate method."
            },
            {
                "question": "What is the general solution to dy/dx = 3y?",
                "options": ["y = 3x + C", "y = Ce^(3x)", "y = 3e^x + C", "y = Ce^x"],
                "correct": 1,
                "explanation": "Separating variables: dy/y = 3 dx, integrating gives ln|y| = 3x + C, so y = Ce^(3x)"
            },
            {
                "question": "For ay'' + by' + cy = 0, if the characteristic equation has roots r = 2, 2, what's the solution?",
                "options": ["y = c₁e^(2x) + c₂e^(2x)", "y = (c₁ + c₂x)e^(2x)", "y = c₁e^(2x) + c₂xe^x", "y = c₁ + c₂e^(2x)"],
                "correct": 1,
                "explanation": "For repeated real roots r, the solution is y = (c₁ + c₂x)e^(rx)"
            },
            {
                "question": "Which differential equation models exponential population growth?",
                "options": ["dP/dt = k", "dP/dt = kP", "dP/dt = k/P", "dP/dt = kP²"],
                "correct": 1,
                "explanation": "Exponential growth means the rate of change is proportional to the current population: dP/dt = kP"
            },
            {
                "question": "What is the integrating factor for dy/dx + 2y = x?",
                "options": ["e^(2x)", "2x", "e^x", "x²"],
                "correct": 0,
                "explanation": "The integrating factor is μ(x) = e^∫p(x)dx = e^∫2dx = e^(2x)"
            },
            {
                "question": "Which type of differential equation is dy/dx + y² = x?",
                "options": ["Linear", "Nonlinear", "Separable", "Homogeneous"],
                "correct": 1,
                "explanation": "The presence of y² makes this nonlinear (the unknown function appears to a power other than 1)"
            },
            {
                "question": "What does the initial condition y(0) = 5 specify?",
                "options": ["The derivative at x=0", "The value of y when x=0", "The slope at x=5", "The maximum value"],
                "correct": 1,
                "explanation": "y(0) = 5 means when x = 0, the function y has the value 5"
            },
            {
                "question": "For the DE y'' + 4y = 0, what type of roots does the characteristic equation have?",
                "options": ["Real and distinct", "Real and repeated", "Complex conjugates", "One real root"],
                "correct": 2,
                "explanation": "r² + 4 = 0 gives r² = -4, so r = ±2i (complex conjugates)"
            },
            {
                "question": "Which model represents Newton's law of cooling?",
                "options": ["dT/dt = -k", "dT/dt = -kT", "dT/dt = -k(T - Tₑₙᵥ)", "dT/dt = kT²"],
                "correct": 2,
                "explanation": "Newton's law states that cooling rate is proportional to temperature difference: dT/dt = -k(T - Tₑₙᵥ)"
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
                        tooltip="Back to Differential Equations"
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
            message = "Outstanding! You've mastered differential equations!"
            color = ft.Colors.GREEN_600
        elif percentage >= 80:
            grade = "A"
            message = "Excellent work! You have a strong understanding of differential equations."
            color = ft.Colors.GREEN_600
        elif percentage >= 70:
            grade = "B"
            message = "Good job! You understand most differential equation concepts."
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
                            "Back to Differential Equations",
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
            label="Ask me anything about differential equations...",
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
                        tooltip="Back to Differential Equations"
                    ),
                    ft.Text(
                        "🤖 AI Tutor - Differential Equations Help",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.PURPLE_900
                    )
                ], alignment=ft.MainAxisAlignment.START),
                
                ft.Divider(),
                
                # Instructions
                ft.Container(
                    ft.Column([
                        ft.Text("💬 Ask me anything about differential equations!", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_800),
                        ft.Text("I can help with:", size=14),
                        ft.Text("• Solution methods (separation, integrating factor)", size=12),
                        ft.Text("• Second-order equations and characteristic equations", size=12),
                        ft.Text("• Applications and modeling", size=12),
                        ft.Text("• Initial and boundary value problems", size=12),
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
                            "Solution Methods",
                            on_click=lambda e: self._quick_help("methods"),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.PURPLE_100)
                        ),
                        col={'xs': 6, 'sm': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            "Second-Order",
                            on_click=lambda e: self._quick_help("second_order"),
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
                    ft.Container(
                        ft.ElevatedButton(
                            "Initial Conditions",
                            on_click=lambda e: self._quick_help("initial"),
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
            "methods": "Key solution methods: 1) Separation of variables for dy/dx = f(x)g(y), 2) Integrating factor μ(x) = e^∫p(x)dx for linear first-order, 3) Characteristic equation for second-order linear equations. Choose based on equation type!",
            "second_order": "For ay'' + by' + cy = 0: Find characteristic equation ar² + br + c = 0. Real distinct roots → y = c₁e^r₁x + c₂e^r₂x. Repeated root → y = (c₁ + c₂x)e^rx. Complex roots r = α ± βi → y = e^αx(c₁cos βx + c₂sin βx).",
            "applications": "Common models: Population growth (dP/dt = kP), Newton's cooling (dT/dt = -k(T-Tₑₙᵥ)), radioactive decay, simple harmonic motion (d²x/dt² + ω²x = 0), RC circuits. Identify the physical relationship to set up the DE.",
            "initial": "Initial conditions like y(0) = a specify function value at a point. Use these after finding general solution to determine constants. For second-order, need two conditions like y(0) = a and y'(0) = b to find both constants c₁ and c₂."
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
        
        if "order" in question_lower:
            return "The order of a differential equation is the highest derivative present. First-order has dy/dx, second-order has d²y/dx², etc. Order determines solution method and number of arbitrary constants in general solution."
        
        elif "separation" in question_lower or "separable" in question_lower:
            return "Separation of variables works for dy/dx = f(x)g(y). Rewrite as dy/g(y) = f(x)dx, then integrate both sides: ∫dy/g(y) = ∫f(x)dx + C. This gives an implicit solution you can solve for y."
        
        elif "integrating factor" in question_lower:
            return "For linear first-order dy/dx + p(x)y = q(x), the integrating factor is μ(x) = e^∫p(x)dx. Multiply the entire equation by μ(x) to make the left side become d/dx[μ(x)y], then integrate."
        
        elif "characteristic" in question_lower:
            return "For second-order ay'' + by' + cy = 0, substitute y = e^rx to get characteristic equation ar² + br + c = 0. Solutions depend on discriminant: real distinct roots, repeated root, or complex conjugates each give different solution forms."
        
        elif "linear" in question_lower:
            return "Linear DEs have no products or powers of y and its derivatives. First-order linear: dy/dx + p(x)y = q(x) (use integrating factor). Second-order linear: ay'' + by' + cy = f(x) (use characteristic equation for homogeneous part)."
        
        elif "initial" in question_lower or "boundary" in question_lower:
            return "Initial/boundary conditions specify values of y and/or its derivatives at particular points. Use these after finding the general solution to determine the arbitrary constants. Second-order equations need two conditions."
        
        elif "population" in question_lower or "growth" in question_lower:
            return "Population growth models: dP/dt = kP (exponential), dP/dt = kP(1-P/M) (logistic with carrying capacity M). The rate of change is proportional to current population (and available capacity for logistic)."
        
        elif "cooling" in question_lower or "newton" in question_lower:
            return "Newton's law of cooling: dT/dt = -k(T - Tₑₙᵥ). The rate of temperature change is proportional to the temperature difference with the environment. Solution: T(t) = Tₑₙᵥ + (T₀ - Tₑₙᵥ)e^(-kt)."
        
        elif "homogeneous" in question_lower:
            return "Homogeneous DE: all terms involve y or its derivatives (no standalone functions of x). For linear second-order ay'' + by' + cy = 0, solve using characteristic equation. General solution has arbitrary constants."
        
        else:
            return "Great question about differential equations! I can help with solution methods (separation of variables, integrating factors), second-order equations, applications, or any specific problems. What would you like to explore?"


def differential_equations_page(page: ft.Page):
    """Main entry point for Differential Equations module"""
    module = DifferentialEquationsModule(page)
    module.show_page()
