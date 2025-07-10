import flet as ft

def maths_tutor_page(page: ft.Page):
    page.title = "Maths Tutor - Student AI Assistance"
    page.scroll = ft.ScrollMode.AUTO
    
    # AppBar with back button
    page.appbar = ft.AppBar(
        leading=ft.IconButton(
            ft.Icons.ARROW_BACK,
            on_click=lambda e: page.go("/")
        ),
        title=ft.Text("Maths Tutor"),
        bgcolor=ft.Colors.BLUE_700,
        center_title=True
    )
    
    # Main content
    content = ft.Container(
        ft.Column([
            ft.Text(
                "🧮 Maths Tutor AI Assistant",
                size=28,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLUE_900,
                text_align=ft.TextAlign.CENTER
            ),
            ft.Text(
                "Get help with math problems, step-by-step solutions, and practice quizzes!",
                size=16,
                color=ft.Colors.BLUE_700,
                text_align=ft.TextAlign.CENTER
            ),
            ft.Divider(height=30),
            
            # Math topics
            ft.Text("Available Topics:", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
            
            # Basic Math Section
            ft.Text("📚 Basic Mathematics", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
            ft.ResponsiveRow([
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.CALCULATE, size=30, color=ft.Colors.BLUE_700),
                            ft.Text("Basic Arithmetic", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Add, Subtract, Multiply, Divide", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.BLUE_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: page.go("/basic-arithmetic")
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.PERCENT, size=30, color=ft.Colors.GREEN_700),
                            ft.Text("Fractions & Decimals", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Converting, Comparing", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.GREEN_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: page.go("/fractions-decimals")
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.TIMELINE, size=30, color=ft.Colors.ORANGE_700),
                            ft.Text("Number Patterns", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Sequences, Series", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.ORANGE_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: page.go("/number-patterns")
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
            ], spacing=10, run_spacing=10),
            
            # Intermediate Math Section
            ft.Text("🎯 Intermediate Mathematics", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
            ft.ResponsiveRow([
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.FUNCTIONS, size=30, color=ft.Colors.PURPLE_700),
                            ft.Text("Algebra", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Equations, Variables", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.PURPLE_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: page.go("/algebra")
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.SQUARE_FOOT, size=30, color=ft.Colors.TEAL_700),
                            ft.Text("Geometry", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Shapes, Areas, Angles", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.TEAL_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: page.go("/geometry")
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.SQUARE, size=30, color=ft.Colors.INDIGO_700),
                            ft.Text("Quadratic Equations", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Factoring, Solving", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.INDIGO_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: page.go("/quadratic-equations")
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.SHOW_CHART, size=30, color=ft.Colors.PINK_700),
                            ft.Text("Trigonometry", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Sin, Cos, Tan", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.PINK_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: page.go("/trigonometry")
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.ANALYTICS, size=30, color=ft.Colors.CYAN_700),
                            ft.Text("Statistics & Probability", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Data Analysis, Graphs", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.CYAN_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: page.go("/statistics-probability")
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.TRENDING_UP, size=30, color=ft.Colors.LIME_700),
                            ft.Text("Linear Functions", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Slope, Graphing", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.LIME_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: page.go("/linear-functions")
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
            ], spacing=10, run_spacing=10),
            
            # Advanced Math Section
            ft.Text("🚀 Advanced Mathematics", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.RED_700),
            ft.ResponsiveRow([
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.FUNCTIONS, size=30, color=ft.Colors.DEEP_PURPLE_700),
                            ft.Text("Calculus", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Derivatives, Integrals", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.DEEP_PURPLE_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: page.go("/calculus")
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.GRID_3X3, size=30, color=ft.Colors.BROWN_700),
                            ft.Text("Matrices", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Operations, Determinants", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.BROWN_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: page.go("/matrices")
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.WAVES, size=30, color=ft.Colors.DEEP_ORANGE_700),
                            ft.Text("Complex Numbers", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Imaginary, Operations", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.DEEP_ORANGE_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: page.go("/complex-numbers")
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.SCATTER_PLOT, size=30, color=ft.Colors.BLUE_GREY_700),
                            ft.Text("Differential Equations", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("ODEs, PDEs", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.BLUE_GREY_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: page.go("/differential-equations")
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.AUTO_GRAPH, size=30, color=ft.Colors.AMBER_700),
                            ft.Text("Vector Calculus", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Gradients, Divergence", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.AMBER_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: page.go("/vector-calculus")
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.POLYLINE, size=30, color=ft.Colors.RED_700),
                            ft.Text("Number Theory", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Primes, Modular Arithmetic", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.RED_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: page.go("/number-theory")
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
            ], spacing=10, run_spacing=10),
            
            ft.Divider(height=20),
            
            # Interactive section
            ft.Text("🤖 AI Math Assistant", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
            ft.Container(
                ft.Column([
                    ft.TextField(
                        label="Type your math problem here...",
                        hint_text="e.g., Solve 2x + 5 = 15, or Find the area of a circle with radius 7",
                        multiline=True,
                        min_lines=3,
                        max_lines=5,
                        border_color=ft.Colors.BLUE_300,
                        expand=True
                    ),
                    ft.Row([
                        ft.ElevatedButton(
                            "Get AI Help",
                            icon=ft.Icons.PSYCHOLOGY,
                            style=ft.ButtonStyle(
                                color=ft.Colors.WHITE,
                                bgcolor=ft.Colors.BLUE_600,
                                shape=ft.RoundedRectangleBorder(radius=8)
                            ),
                            on_click=lambda e: page.show_snack_bar(
                                ft.SnackBar(content=ft.Text("AI Math tutor will provide step-by-step solutions soon!"))
                            ),
                            expand=True
                        ),
                        ft.ElevatedButton(
                            "Practice Quiz",
                            icon=ft.Icons.QUIZ_OUTLINED,
                            style=ft.ButtonStyle(
                                color=ft.Colors.WHITE,
                                bgcolor=ft.Colors.GREEN_600,
                                shape=ft.RoundedRectangleBorder(radius=8)
                            ),
                            on_click=lambda e: page.show_snack_bar(
                                ft.SnackBar(content=ft.Text("Interactive math quizzes coming soon!"))
                            ),
                            expand=True
                        ),
                    ], spacing=10),
                    ft.Row([
                        ft.ElevatedButton(
                            "Step-by-Step Solution",
                            icon=ft.Icons.LIST_ALT,
                            style=ft.ButtonStyle(
                                color=ft.Colors.WHITE,
                                bgcolor=ft.Colors.ORANGE_600,
                                shape=ft.RoundedRectangleBorder(radius=8)
                            ),
                            on_click=lambda e: page.show_snack_bar(
                                ft.SnackBar(content=ft.Text("Detailed explanations feature coming soon!"))
                            ),
                            expand=True
                        ),
                        ft.ElevatedButton(
                            "Graph It",
                            icon=ft.Icons.TIMELINE,
                            style=ft.ButtonStyle(
                                color=ft.Colors.WHITE,
                                bgcolor=ft.Colors.PURPLE_600,
                                shape=ft.RoundedRectangleBorder(radius=8)
                            ),
                            on_click=lambda e: page.show_snack_bar(
                                ft.SnackBar(content=ft.Text("Mathematical graphing tool coming soon!"))
                            ),
                            expand=True
                        ),
                    ], spacing=10)
                ], spacing=15),
                bgcolor=ft.Colors.GREY_50,
                border_radius=12,
                padding=20,
                border=ft.border.all(2, ft.Colors.BLUE_200)
            )
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15),
        padding=30,
        expand=True
    )
    
    page.add(content)
