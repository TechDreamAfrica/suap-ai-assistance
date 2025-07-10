import flet as ft

def world_wars_page(page: ft.Page):
    """World Wars learning page"""
    page.title = f"World Wars - History Learning"
    page.scroll = ft.ScrollMode.AUTO
    
    # Clear page content first
    page.clean()
    
    # AppBar with back button
    page.appbar = ft.AppBar(
        leading=ft.IconButton(
            ft.Icons.ARROW_BACK,
            on_click=lambda e: page.go("/history")
        ),
        title=ft.Text("World Wars"),
        bgcolor=ft.Colors.BROWN_700,
        center_title=True
    )
    
    # Main content
    content = ft.Container(
        ft.Column([
            ft.Text(
                f"📚 World Wars",
                size=28,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BROWN_900,
                text_align=ft.TextAlign.CENTER
            ),
            ft.Text(
                f"Learn about World Wars concepts and practice problems",
                size=16,
                color=ft.Colors.BROWN_700,
                text_align=ft.TextAlign.CENTER
            ),
            ft.Divider(height=30),
            
            # Learning sections
            ft.Container(
                ft.Column([
                    ft.Text("🎯 Learning Objectives", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BROWN_900),
                    ft.Text(f"• Master fundamental World Wars concepts", size=14),
                    ft.Text(f"• Practice solving World Wars problems", size=14),
                    ft.Text(f"• Apply World Wars in real-world scenarios", size=14),
                    ft.Text(f"• Build confidence in World Wars skills", size=14),
                ], spacing=10),
                bgcolor=ft.Colors.BROWN_50,
                border_radius=10,
                padding=20,
                margin=ft.margin.only(bottom=20)
            ),
            
            # Action buttons
            ft.ResponsiveRow([
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.QUIZ, size=30, color=ft.Colors.BROWN_700),
                            ft.Text("Practice Quiz", size=14, weight=ft.FontWeight.BOLD)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=20,
                            bgcolor=ft.Colors.BROWN_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: show_practice_quiz(page)
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.HELP_OUTLINE, size=30, color=ft.Colors.BROWN_700),
                            ft.Text("Get Help", size=14, weight=ft.FontWeight.BOLD)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=20,
                            bgcolor=ft.Colors.BROWN_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: show_help(page)
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.LIGHTBULB_OUTLINE, size=30, color=ft.Colors.BROWN_700),
                            ft.Text("Examples", size=14, weight=ft.FontWeight.BOLD)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=20,
                            bgcolor=ft.Colors.BROWN_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: show_examples(page)
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
            ], spacing=15, run_spacing=15),
            
            ft.Divider(height=20),
            
            # Content area
            ft.Container(
                ft.Column([
                    ft.Text(f"Welcome to World Wars Learning!", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text(f"This is where you'll learn about World Wars concepts. Click the buttons above to get started with practice quizzes, help, or see examples.", size=14),
                    ft.Text("✨ Features:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BROWN_900),
                    ft.Text(f"• Interactive learning for World Wars", size=14),
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

def show_practice_quiz(page):
    """Show practice quiz"""
    page.snack_bar = ft.SnackBar(
        content=ft.Text("Practice quiz coming soon! This feature will include interactive questions and instant feedback."),
        bgcolor=ft.Colors.GREEN_100
    )
    page.snack_bar.open = True
    page.update()

def show_help(page):
    """Show help information"""
    page.snack_bar = ft.SnackBar(
        content=ft.Text("Help section coming soon! Get personalized assistance and step-by-step guidance."),
        bgcolor=ft.Colors.BLUE_100
    )
    page.snack_bar.open = True
    page.update()

def show_examples(page):
    """Show examples"""
    page.snack_bar = ft.SnackBar(
        content=ft.Text("Examples section coming soon! Explore worked examples and detailed explanations."),
        bgcolor=ft.Colors.ORANGE_100
    )
    page.snack_bar.open = True
    page.update()
