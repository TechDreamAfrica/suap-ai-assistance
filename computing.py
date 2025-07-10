import flet as ft

def computing_page(page: ft.Page):
    page.title = "Computing - Student AI Assistance"
    page.scroll = ft.ScrollMode.AUTO
    
    # AppBar with back button
    page.appbar = ft.AppBar(
        leading=ft.IconButton(
            ft.Icons.ARROW_BACK,
            on_click=lambda e: page.go("/")
        ),
        title=ft.Text("Computing Hub"),
        bgcolor=ft.Colors.BLUE_700,
        center_title=True
    )
    
    # Main content
    content = ft.Container(
        ft.Column([
            ft.Text(
                "💻 Computing & ICT Center",
                size=28,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLUE_900,
                text_align=ft.TextAlign.CENTER
            ),
            ft.Text(
                "Learn ICT skills, programming, and digital literacy with AI guidance!",
                size=16,
                color=ft.Colors.BLUE_700,
                text_align=ft.TextAlign.CENTER
            ),
            ft.Divider(height=30),
            
            # Computing topics
            ft.Text("Available Topics:", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
            
            # Digital Basics Section
            ft.Text("💻 Digital Basics", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
            ft.ResponsiveRow([
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.COMPUTER, size=30, color=ft.Colors.BLUE_700),
                            ft.Text("Computer Fundamentals", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Hardware, Software, OS", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.BLUE_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: page.show_snack_bar(ft.SnackBar(content=ft.Text("Computer Fundamentals module coming soon!")))
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.APPS, size=30, color=ft.Colors.GREEN_700),
                            ft.Text("Digital Applications", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Word, Excel, PowerPoint", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.GREEN_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: page.show_snack_bar(ft.SnackBar(content=ft.Text("Digital Applications module coming soon!")))
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.KEYBOARD, size=30, color=ft.Colors.ORANGE_700),
                            ft.Text("Digital Literacy", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Typing, File Management", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.ORANGE_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: page.show_snack_bar(ft.SnackBar(content=ft.Text("Digital Literacy module coming soon!")))
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
            ], spacing=10, run_spacing=10),
            
            # Programming Section
            ft.Text("🐍 Programming & Development", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
            ft.ResponsiveRow([
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.CODE, size=30, color=ft.Colors.PURPLE_700),
                            ft.Text("Python Programming", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Basics, Data Structures", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.PURPLE_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: page.show_snack_bar(ft.SnackBar(content=ft.Text("Python Programming module coming soon!")))
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.WEB, size=30, color=ft.Colors.TEAL_700),
                            ft.Text("Web Development", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("HTML, CSS, JavaScript", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.TEAL_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: page.show_snack_bar(ft.SnackBar(content=ft.Text("Web Development module coming soon!")))
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.EXTENSION, size=30, color=ft.Colors.INDIGO_700),
                            ft.Text("Scratch Programming", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Visual Coding, Logic", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.INDIGO_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: page.show_snack_bar(ft.SnackBar(content=ft.Text("Scratch Programming module coming soon!")))
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
            ], spacing=10, run_spacing=10),
            
            # Advanced Topics Section
            ft.Text("🚀 Advanced Computing", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.RED_700),
            ft.ResponsiveRow([
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.CLOUD, size=30, color=ft.Colors.PINK_700),
                            ft.Text("Internet & Networks", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Web Safety, Cloud Computing", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.PINK_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: page.show_snack_bar(ft.SnackBar(content=ft.Text("Internet & Networks module coming soon!")))
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.STORAGE, size=30, color=ft.Colors.CYAN_700),
                            ft.Text("Databases", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("SQL, Data Management", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.CYAN_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: page.show_snack_bar(ft.SnackBar(content=ft.Text("Databases module coming soon!")))
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.SECURITY, size=30, color=ft.Colors.LIME_700),
                            ft.Text("Cybersecurity", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Digital Safety, Privacy", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.LIME_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: page.show_snack_bar(ft.SnackBar(content=ft.Text("Cybersecurity module coming soon!")))
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.SMART_TOY, size=30, color=ft.Colors.DEEP_PURPLE_700),
                            ft.Text("Artificial Intelligence", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Machine Learning Basics", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.DEEP_PURPLE_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: page.show_snack_bar(ft.SnackBar(content=ft.Text("Artificial Intelligence module coming soon!")))
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.PHONE_ANDROID, size=30, color=ft.Colors.BROWN_700),
                            ft.Text("Mobile App Development", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("App Design, Development", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.BROWN_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: page.show_snack_bar(ft.SnackBar(content=ft.Text("Mobile App Development module coming soon!")))
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.GAMEPAD, size=30, color=ft.Colors.DEEP_ORANGE_700),
                            ft.Text("Game Development", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Game Design, Programming", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.DEEP_ORANGE_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: page.show_snack_bar(ft.SnackBar(content=ft.Text("Game Development module coming soon!")))
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
            ], spacing=10, run_spacing=10),
            
            ft.Divider(height=20),
            
            # Interactive section
            ft.Text("🤖 AI Computing Assistant", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
            ft.Container(
                ft.Column([
                    ft.TextField(
                        label="Ask your computing question...",
                        hint_text="e.g., How do I create a website? or Explain what a database is",
                        multiline=True,
                        min_lines=3,
                        max_lines=5,
                        border_color=ft.Colors.BLUE_300,
                        expand=True
                    ),
                    ft.Row([
                        ft.ElevatedButton(
                            "Get Computing Help",
                            icon=ft.Icons.COMPUTER,
                            style=ft.ButtonStyle(
                                color=ft.Colors.WHITE,
                                bgcolor=ft.Colors.GREEN_600,
                                shape=ft.RoundedRectangleBorder(radius=8)
                            ),
                            on_click=lambda e: page.show_snack_bar(
                                ft.SnackBar(content=ft.Text("AI Computing tutor coming soon!"))
                            ),
                            expand=True
                        ),
                        ft.ElevatedButton(
                            "Code Practice",
                            icon=ft.Icons.CODE,
                            style=ft.ButtonStyle(
                                color=ft.Colors.WHITE,
                                bgcolor=ft.Colors.PURPLE_600,
                                shape=ft.RoundedRectangleBorder(radius=8)
                            ),
                            on_click=lambda e: page.show_snack_bar(
                                ft.SnackBar(content=ft.Text("Interactive coding exercises coming soon!"))
                            ),
                            expand=True
                        ),
                    ], spacing=10),
                    ft.Row([
                        ft.ElevatedButton(
                            "Project Ideas",
                            icon=ft.Icons.LIGHTBULB,
                            style=ft.ButtonStyle(
                                color=ft.Colors.WHITE,
                                bgcolor=ft.Colors.ORANGE_600,
                                shape=ft.RoundedRectangleBorder(radius=8)
                            ),
                            on_click=lambda e: page.show_snack_bar(
                                ft.SnackBar(content=ft.Text("Computing project ideas coming soon!"))
                            ),
                            expand=True
                        ),
                        ft.ElevatedButton(
                            "Tech Quiz",
                            icon=ft.Icons.QUIZ_OUTLINED,
                            style=ft.ButtonStyle(
                                color=ft.Colors.WHITE,
                                bgcolor=ft.Colors.BLUE_600,
                                shape=ft.RoundedRectangleBorder(radius=8)
                            ),
                            on_click=lambda e: page.show_snack_bar(
                                ft.SnackBar(content=ft.Text("Technology knowledge tests coming soon!"))
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
