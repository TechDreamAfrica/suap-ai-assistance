import flet as ft
import random
import math


class VectorCalculusModule:
    """Comprehensive Vector Calculus learning module"""
    
    def __init__(self, page=None):
        self.page = page
        self.current_question = 0
        self.score = 0
        self.quiz_questions = self._generate_quiz_questions()
        self.selected_answer = None
        
    def show_page(self):
        """Main entry point for the module"""
        self.show_main_page()
        
    def show_main_page(self, page=None):
        """Show the main vector calculus page
        Args:
            page: Optional page reference. If not provided, uses self.page
        """
        if page is None:
            page = self.page
        self.page = page  # Update the page reference
            
        view = ft.View(
            "/vector_calculus",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: page.go_back()),
                    title=ft.Text("Vector Calculus"),
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
            title=ft.Text("Vector Calculus"),
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
                            "🧮 Vector Calculus",
                            size=32,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.BLUE_900,
                            text_align=ft.TextAlign.CENTER
                        ),
                        ft.Text(
                            "Explore multivariable calculus with vectors and fields",
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
                        ft.Text("• Understand vector fields and their properties", size=14),
                        ft.Text("• Calculate gradient, divergence, and curl", size=14),
                        ft.Text("• Master line and surface integrals", size=14),
                        ft.Text("• Apply Green's, Stokes', and Divergence theorems", size=14),
                        ft.Text("• Work with parametric curves and surfaces", size=14),
                        ft.Text("• Solve real-world physics and engineering problems", size=14),
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
                        ft.Text("🌟 Vector Calculus Overview", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                        ft.Text("Vector calculus extends calculus to multivariable functions and vector fields. It provides tools for analyzing how vector quantities change in space and is fundamental to physics, engineering, and computer graphics.", size=14),
                        
                        ft.Divider(height=10),
                        
                        ft.Text("🔑 Key Operations:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_800),
                        ft.Text("• Gradient (∇f): Direction of steepest increase", size=14),
                        ft.Text("• Divergence (∇·F): Measure of source/sink strength", size=14),
                        ft.Text("• Curl (∇×F): Measure of rotation or circulation", size=14),
                        ft.Text("• Line integrals: Work done along a path", size=14),
                        ft.Text("• Surface integrals: Flux through a surface", size=14),
                        
                        ft.Divider(height=10),
                        
                        ft.Text("🌟 Major Theorems:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_800),
                        ft.Text("• Green's Theorem: Relates line and double integrals", size=14),
                        ft.Text("• Stokes' Theorem: Relates curl and circulation", size=14),
                        ft.Text("• Divergence Theorem: Relates flux and volume integrals", size=14),
                        
                        ft.Divider(height=10),
                        
                        ft.Text("🚀 Applications:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_800),
                        ft.Text("• Electromagnetic field theory", size=14),
                        ft.Text("• Fluid dynamics and flow analysis", size=14),
                        ft.Text("• Computer graphics and 3D modeling", size=14),
                        ft.Text("• Heat transfer and diffusion", size=14),
                        ft.Text("• Optimization and machine learning", size=14),
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
                        tooltip="Back to Vector Calculus"
                    ),
                    ft.Text(
                        "📚 Vector Calculus: Complete Guide",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLUE_900
                    )
                ], alignment=ft.MainAxisAlignment.START),
                
                ft.Divider(),
                
                # Content sections
                ft.Container(
                    ft.Column([
                        ft.Text("1. Vector Fields", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800),
                        ft.Text("A vector field assigns a vector to each point in space, representing quantities like velocity, force, or electric field.", size=14),
                        ft.Container(
                            ft.Column([
                                ft.Text("Vector Field Notation:", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("2D: F(x,y) = P(x,y)î + Q(x,y)ĵ", size=14),
                                ft.Text("3D: F(x,y,z) = P(x,y,z)î + Q(x,y,z)ĵ + R(x,y,z)k̂", size=14),
                                ft.Text("Examples:", size=14),
                                ft.Text("• Gravitational field: F = -GMm/r²", size=14),
                                ft.Text("• Velocity field: v(x,y) = -yî + xĵ (rotation)", size=14),
                                ft.Text("• Electric field: E = q/(4πε₀r²) r̂", size=14),
                                ft.Text("Conservative field: F = ∇φ (gradient of scalar potential)", size=14),
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
                        ft.Text("2. Gradient, Divergence, and Curl", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_800),
                        ft.Text("Three fundamental operations that analyze different aspects of vector fields.", size=14),
                        ft.Container(
                            ft.Column([
                                ft.Text("Gradient (∇f):", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("∇f = (∂f/∂x)î + (∂f/∂y)ĵ + (∂f/∂z)k̂", size=14),
                                ft.Text("Points in direction of steepest increase", size=14),
                                ft.Text("Magnitude = rate of steepest increase", size=14),
                                ft.Text("Divergence (∇·F):", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("∇·F = ∂P/∂x + ∂Q/∂y + ∂R/∂z", size=14),
                                ft.Text("Measures sources (+) and sinks (-)", size=14),
                                ft.Text("Curl (∇×F):", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("∇×F = |î  ĵ  k̂|", size=14),
                                ft.Text("      |∂/∂x ∂/∂y ∂/∂z|", size=14),
                                ft.Text("      |P  Q  R|", size=14),
                                ft.Text("Measures rotation and circulation", size=14),
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
                        ft.Text("3. Line Integrals", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_800),
                        ft.Text("Integrals along curves, used to calculate work done by force fields and circulation.", size=14),
                        ft.Container(
                            ft.Column([
                                ft.Text("Line Integral of Scalar Field:", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("∫_C f ds = ∫_a^b f(r(t))|r'(t)| dt", size=14),
                                ft.Text("Line Integral of Vector Field:", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("∫_C F·dr = ∫_a^b F(r(t))·r'(t) dt", size=14),
                                ft.Text("Physical interpretation: Work done", size=14),
                                ft.Text("Green's Theorem:", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("∮_C P dx + Q dy = ∫∫_D (∂Q/∂x - ∂P/∂y) dA", size=14),
                                ft.Text("Relates line integral to double integral", size=14),
                                ft.Text("Conservative fields: ∮_C F·dr = 0 for closed curves", size=14),
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
                        ft.Text("4. Surface Integrals", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_800),
                        ft.Text("Integrals over surfaces, used to calculate flux and mass distribution.", size=14),
                        ft.Container(
                            ft.Column([
                                ft.Text("Surface Integral of Scalar Field:", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("∫∫_S f dS = ∫∫_D f(r(u,v))|r_u × r_v| dudv", size=14),
                                ft.Text("Surface Integral of Vector Field (Flux):", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("∫∫_S F·n̂ dS = ∫∫_S F·(r_u × r_v) dudv", size=14),
                                ft.Text("Measures flow through surface", size=14),
                                ft.Text("Stokes' Theorem:", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("∮_C F·dr = ∫∫_S (∇×F)·n̂ dS", size=14),
                                ft.Text("Relates circulation to curl", size=14),
                                ft.Text("Divergence Theorem (Gauss's Theorem):", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("∫∫_S F·n̂ dS = ∫∫∫_V ∇·F dV", size=14),
                                ft.Text("Relates flux to divergence", size=14),
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
                        ft.Text("5. Applications in Physics and Engineering", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.RED_800),
                        ft.Text("Vector calculus provides the mathematical foundation for many physical phenomena.", size=14),
                        ft.Container(
                            ft.Column([
                                ft.Text("Maxwell's Equations (Electromagnetism):", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("∇·E = ρ/ε₀ (Gauss's law)", size=14),
                                ft.Text("∇·B = 0 (No magnetic monopoles)", size=14),
                                ft.Text("∇×E = -∂B/∂t (Faraday's law)", size=14),
                                ft.Text("∇×B = μ₀J + μ₀ε₀∂E/∂t (Ampère's law)", size=14),
                                ft.Text("Fluid Dynamics:", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("Continuity equation: ∂ρ/∂t + ∇·(ρv) = 0", size=14),
                                ft.Text("Heat Equation: ∂T/∂t = α∇²T", size=14),
                                ft.Text("Wave Equation: ∂²u/∂t² = c²∇²u", size=14),
                                ft.Text("Computer Graphics: Normal vectors, lighting, surface rendering", size=14),
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
                        "Back to Vector Calculus",
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
                        tooltip="Back to Vector Calculus"
                    ),
                    ft.Text(
                        "💡 Vector Calculus: Worked Examples",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.ORANGE_900
                    )
                ], alignment=ft.MainAxisAlignment.START),
                
                ft.Divider(),
                
                # Example 1
                ft.Container(
                    ft.Column([
                        ft.Text("Example 1: Computing Gradient", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800),
                        ft.Text("Problem: Find the gradient of f(x,y,z) = x²y + yz²", size=14),
                        ft.Text("Solution:", size=14, weight=ft.FontWeight.BOLD),
                        ft.Text("Step 1: Find partial derivatives", size=14),
                        ft.Text("∂f/∂x = 2xy", size=14),
                        ft.Text("∂f/∂y = x² + z²", size=14),
                        ft.Text("∂f/∂z = 2yz", size=14),
                        ft.Text("Step 2: Write as vector", size=14),
                        ft.Container(
                            ft.Text("Answer: ∇f = (2xy)î + (x² + z²)ĵ + (2yz)k̂", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
                            bgcolor=ft.Colors.GREEN_50,
                            padding=10,
                            border_radius=5,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        ft.Text("At point (1,2,3): ∇f = 4î + 10ĵ + 12k̂", size=14, style=ft.TextStyle(italic=True)),
                    ], spacing=8),
                    bgcolor=ft.Colors.WHITE,
                    border_radius=10,
                    padding=15,
                    margin=ft.margin.only(bottom=20)
                ),
                
                # Example 2
                ft.Container(
                    ft.Column([
                        ft.Text("Example 2: Computing Divergence", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_800),
                        ft.Text("Problem: Find the divergence of F = (x²y)î + (xy²)ĵ + (z³)k̂", size=14),
                        ft.Text("Solution:", size=14, weight=ft.FontWeight.BOLD),
                        ft.Text("Step 1: Apply divergence formula", size=14),
                        ft.Text("∇·F = ∂P/∂x + ∂Q/∂y + ∂R/∂z", size=14),
                        ft.Text("Step 2: Calculate each partial derivative", size=14),
                        ft.Text("∂(x²y)/∂x = 2xy", size=14),
                        ft.Text("∂(xy²)/∂y = 2xy", size=14),
                        ft.Text("∂(z³)/∂z = 3z²", size=14),
                        ft.Text("Step 3: Sum the results", size=14),
                        ft.Container(
                            ft.Text("Answer: ∇·F = 2xy + 2xy + 3z² = 4xy + 3z²", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
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
                        ft.Text("Example 3: Line Integral", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_800),
                        ft.Text("Problem: Evaluate ∫_C F·dr where F = (y)î + (x)ĵ and C is the line from (0,0) to (1,1)", size=14),
                        ft.Text("Solution:", size=14, weight=ft.FontWeight.BOLD),
                        ft.Text("Step 1: Parameterize the curve", size=14),
                        ft.Text("r(t) = tî + tĵ, 0 ≤ t ≤ 1", size=14),
                        ft.Text("r'(t) = î + ĵ", size=14),
                        ft.Text("Step 2: Express F along the curve", size=14),
                        ft.Text("F(r(t)) = tî + tĵ", size=14),
                        ft.Text("Step 3: Calculate the dot product", size=14),
                        ft.Text("F(r(t))·r'(t) = (tî + tĵ)·(î + ĵ) = t + t = 2t", size=14),
                        ft.Text("Step 4: Integrate", size=14),
                        ft.Text("∫₀¹ 2t dt = [t²]₀¹ = 1", size=14),
                        ft.Container(
                            ft.Text("Answer: ∫_C F·dr = 1", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
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
                        ft.Text("Example 4: Green's Theorem Application", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.RED_800),
                        ft.Text("Problem: Use Green's theorem to evaluate ∮_C (x²)dx + (xy)dy around unit circle", size=14),
                        ft.Text("Solution:", size=14, weight=ft.FontWeight.BOLD),
                        ft.Text("Step 1: Identify P and Q", size=14),
                        ft.Text("P(x,y) = x², Q(x,y) = xy", size=14),
                        ft.Text("Step 2: Calculate partial derivatives", size=14),
                        ft.Text("∂Q/∂x = y, ∂P/∂y = 0", size=14),
                        ft.Text("Step 3: Apply Green's theorem", size=14),
                        ft.Text("∮_C P dx + Q dy = ∫∫_D (∂Q/∂x - ∂P/∂y) dA", size=14),
                        ft.Text("= ∫∫_D (y - 0) dA = ∫∫_D y dA", size=14),
                        ft.Text("Step 4: Evaluate double integral over unit disk", size=14),
                        ft.Text("Using polar coordinates: x = r cos θ, y = r sin θ", size=14),
                        ft.Text("∫₀²π ∫₀¹ (r sin θ)r dr dθ = ∫₀²π sin θ [r³/3]₀¹ dθ", size=14),
                        ft.Text("= (1/3)∫₀²π sin θ dθ = (1/3)[-cos θ]₀²π = 0", size=14),
                        ft.Container(
                            ft.Text("Answer: ∮_C (x²)dx + (xy)dy = 0", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
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
                        "Back to Vector Calculus",
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
        """Generate quiz questions for vector calculus"""
        questions = [
            {
                "question": "What does the gradient ∇f represent?",
                "options": ["Vector pointing in direction of steepest decrease", "Vector pointing in direction of steepest increase", "Scalar representing rate of change", "Curl of the vector field"],
                "correct": 1,
                "explanation": "The gradient points in the direction of steepest increase of the scalar function f."
            },
            {
                "question": "What is the divergence of F = xî + yĵ + zk̂?",
                "options": ["0", "1", "3", "x + y + z"],
                "correct": 2,
                "explanation": "∇·F = ∂x/∂x + ∂y/∂y + ∂z/∂z = 1 + 1 + 1 = 3"
            },
            {
                "question": "In Green's theorem, what does ∮_C P dx + Q dy equal?",
                "options": ["∫∫_D (∂P/∂x - ∂Q/∂y) dA", "∫∫_D (∂Q/∂x - ∂P/∂y) dA", "∫∫_D P dA", "∫∫_D Q dA"],
                "correct": 1,
                "explanation": "Green's theorem states: ∮_C P dx + Q dy = ∫∫_D (∂Q/∂x - ∂P/∂y) dA"
            },
            {
                "question": "What does positive divergence indicate in a vector field?",
                "options": ["Rotation", "Source", "Sink", "Conservative field"],
                "correct": 1,
                "explanation": "Positive divergence indicates a source - vectors are flowing outward from that point."
            },
            {
                "question": "Which theorem relates flux through a closed surface to divergence?",
                "options": ["Green's theorem", "Stokes' theorem", "Divergence theorem", "Fundamental theorem"],
                "correct": 2,
                "explanation": "The Divergence theorem (Gauss's theorem) relates flux through a closed surface to the divergence in the volume."
            },
            {
                "question": "What is the curl of a conservative vector field?",
                "options": ["Maximum", "Minimum", "Zero", "Undefined"],
                "correct": 2,
                "explanation": "Conservative vector fields have zero curl everywhere: ∇×F = 0"
            },
            {
                "question": "A line integral ∫_C F·dr represents:",
                "options": ["Area under curve", "Work done by force field", "Length of curve", "Volume"],
                "correct": 1,
                "explanation": "The line integral ∫_C F·dr represents the work done by the force field F along the curve C."
            },
            {
                "question": "What is the gradient of f(x,y) = x² + y²?",
                "options": ["2x + 2y", "(2x, 2y)", "4xy", "2(x + y)"],
                "correct": 1,
                "explanation": "∇f = (∂f/∂x, ∂f/∂y) = (2x, 2y)"
            },
            {
                "question": "Stokes' theorem relates:",
                "options": ["Line integral to surface integral", "Surface integral to volume integral", "Double integral to triple integral", "Gradient to divergence"],
                "correct": 0,
                "explanation": "Stokes' theorem relates the circulation (line integral) around a closed curve to the curl through the surface it bounds."
            },
            {
                "question": "In 2D, what is the curl of F = P î + Q ĵ?",
                "options": ["∂P/∂x + ∂Q/∂y", "∂Q/∂x - ∂P/∂y", "∂P/∂y - ∂Q/∂x", "∂P/∂x - ∂Q/∂y"],
                "correct": 1,
                "explanation": "In 2D, curl F = ∂Q/∂x - ∂P/∂y (the k-component of the 3D curl)"
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
                        tooltip="Back to Vector Calculus"
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
            message = "Outstanding! You've mastered vector calculus!"
            color = ft.Colors.GREEN_600
        elif percentage >= 80:
            grade = "A"
            message = "Excellent work! You have a strong understanding of vector calculus."
            color = ft.Colors.GREEN_600
        elif percentage >= 70:
            grade = "B"
            message = "Good job! You understand most vector calculus concepts."
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
                            "Back to Vector Calculus",
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
            label="Ask me anything about vector calculus...",
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
                        tooltip="Back to Vector Calculus"
                    ),
                    ft.Text(
                        "🤖 AI Tutor - Vector Calculus Help",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.PURPLE_900
                    )
                ], alignment=ft.MainAxisAlignment.START),
                
                ft.Divider(),
                
                # Instructions
                ft.Container(
                    ft.Column([
                        ft.Text("💬 Ask me anything about vector calculus!", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_800),
                        ft.Text("I can help with:", size=14),
                        ft.Text("• Gradient, divergence, and curl calculations", size=12),
                        ft.Text("• Line and surface integrals", size=12),
                        ft.Text("• Green's, Stokes', and Divergence theorems", size=12),
                        ft.Text("• Vector field analysis and applications", size=12),
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
                            "Gradient/Div/Curl",
                            on_click=lambda e: self._quick_help("operations"),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.PURPLE_100)
                        ),
                        col={'xs': 6, 'sm': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            "Line Integrals",
                            on_click=lambda e: self._quick_help("line_integrals"),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.PURPLE_100)
                        ),
                        col={'xs': 6, 'sm': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            "Major Theorems",
                            on_click=lambda e: self._quick_help("theorems"),
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
            "operations": "Key operations: Gradient ∇f (steepest increase direction), Divergence ∇·F (source/sink measure), Curl ∇×F (rotation measure). For calculations: ∇f = (∂f/∂x, ∂f/∂y, ∂f/∂z), ∇·F = ∂P/∂x + ∂Q/∂y + ∂R/∂z, ∇×F uses determinant formula.",
            "line_integrals": "Line integrals: ∫_C f ds (scalar field), ∫_C F·dr (vector field, represents work). Parameterize curve r(t), then ∫_a^b F(r(t))·r'(t) dt. Conservative fields have path independence and ∮_C F·dr = 0 for closed curves.",
            "theorems": "Major theorems connect different integrals: Green's (line ↔ double), Stokes' (circulation ↔ curl), Divergence (flux ↔ divergence). They transform complex line/surface integrals into easier volume integrals or vice versa.",
            "applications": "Vector calculus powers physics: Maxwell's equations (electromagnetism), fluid dynamics (continuity, Navier-Stokes), heat equation, wave equation. Also used in computer graphics, optimization, and machine learning for gradients and vector fields."
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
        
        if "gradient" in question_lower:
            return "The gradient ∇f = (∂f/∂x, ∂f/∂y, ∂f/∂z) points in the direction of steepest increase of scalar function f. Its magnitude gives the rate of steepest increase. It's always perpendicular to level curves/surfaces."
        
        elif "divergence" in question_lower:
            return "Divergence ∇·F = ∂P/∂x + ∂Q/∂y + ∂R/∂z measures how much vector field F spreads out or converges at a point. Positive = source (outflow), negative = sink (inflow), zero = incompressible flow."
        
        elif "curl" in question_lower:
            return "Curl ∇×F measures rotation in vector field F. In 2D: ∇×F = ∂Q/∂x - ∂P/∂y. In 3D, use determinant with i,j,k. Zero curl = conservative field. Points in direction of rotation axis by right-hand rule."
        
        elif "line integral" in question_lower:
            return "Line integrals: ∫_C f ds (along curve) or ∫_C F·dr (work by force field). Parameterize curve r(t), then integrate. For work: ∫_a^b F(r(t))·r'(t) dt. Conservative fields give path independence."
        
        elif "surface integral" in question_lower:
            return "Surface integrals calculate flux: ∫∫_S F·n̂ dS. Parameterize surface r(u,v), find normal n̂ = r_u × r_v, then integrate F·(r_u × r_v) over parameter domain. Measures flow through surface."
        
        elif "green" in question_lower or "green's" in question_lower:
            return "Green's theorem: ∮_C P dx + Q dy = ∫∫_D (∂Q/∂x - ∂P/∂y) dA. Converts line integral around closed curve to double integral over enclosed region. Useful when line integral is complex but region integral is simple."
        
        elif "stokes" in question_lower:
            return "Stokes' theorem: ∮_C F·dr = ∫∫_S (∇×F)·n̂ dS. Relates circulation around boundary curve to curl through surface. 3D generalization of Green's theorem. Very useful in electromagnetic theory."
        
        elif "divergence theorem" in question_lower or "gauss" in question_lower:
            return "Divergence theorem: ∫∫_S F·n̂ dS = ∫∫∫_V ∇·F dV. Relates flux through closed surface to divergence throughout volume. Essential for deriving conservation laws and Maxwell's equations."
        
        elif "conservative" in question_lower:
            return "Conservative vector fields: F = ∇φ for some scalar potential φ. Properties: zero curl (∇×F = 0), path independence, ∮_C F·dr = 0 for closed curves. Work depends only on endpoints, not path taken."
        
        elif "flux" in question_lower:
            return "Flux measures flow through surface: ∫∫_S F·n̂ dS. F is vector field (like velocity), n̂ is unit normal to surface. Positive flux = flow outward, negative = inward. Key concept in fluid dynamics and electromagnetism."
        
        else:
            return "Great question about vector calculus! I can help with gradient, divergence, curl calculations, line/surface integrals, major theorems (Green's, Stokes', Divergence), conservative fields, or any specific problems. What would you like to explore?"


def vector_calculus_page(page: ft.Page):
    """Main entry point for Vector Calculus module"""
    module = VectorCalculusModule(page)
    module.show_page()
