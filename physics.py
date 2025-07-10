import flet as ft

def physics_page(page: ft.Page):
    page.title = "Physics - Student AI Assistance"
    page.scroll = ft.ScrollMode.AUTO
    
    # AppBar with back button
    page.appbar = ft.AppBar(
        leading=ft.IconButton(
            ft.Icons.ARROW_BACK,
            on_click=lambda e: page.go("/")
        ),
        title=ft.Text("Physics Lab"),
        bgcolor=ft.Colors.BLUE_700,
        center_title=True
    )
    
    # Main content
    content = ft.Container(
        ft.Column([
            ft.Text(
                "⚡ Physics Laboratory",
                size=28,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLUE_900,
                text_align=ft.TextAlign.CENTER
            ),
            ft.Text(
                "Master physics concepts, laws, and problem-solving with AI assistance!",
                size=16,
                color=ft.Colors.BLUE_700,
                text_align=ft.TextAlign.CENTER
            ),
            ft.Divider(height=30),
            
            # Physics topics
            ft.Text("Physics Topics:", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
            ft.Container(
                ft.Column([
                    ft.ListTile(
                        leading=ft.Icon(ft.Icons.SPEED, color=ft.Colors.BLUE_700),
                        title=ft.Text("Mechanics"),
                        subtitle=ft.Text("Motion, Forces, Energy, Momentum"),
                        trailing=ft.Icon(ft.Icons.ARROW_FORWARD_IOS)
                    ),
                    ft.ListTile(
                        leading=ft.Icon(ft.Icons.ELECTRIC_BOLT, color=ft.Colors.YELLOW_700),
                        title=ft.Text("Electricity & Magnetism"),
                        subtitle=ft.Text("Circuits, Current, Magnetic Fields"),
                        trailing=ft.Icon(ft.Icons.ARROW_FORWARD_IOS)
                    ),
                    ft.ListTile(
                        leading=ft.Icon(ft.Icons.WAVES, color=ft.Colors.PURPLE_700),
                        title=ft.Text("Waves & Sound"),
                        subtitle=ft.Text("Wave Properties, Sound, Light"),
                        trailing=ft.Icon(ft.Icons.ARROW_FORWARD_IOS)
                    ),
                    ft.ListTile(
                        leading=ft.Icon(ft.Icons.THERMOSTAT, color=ft.Colors.RED_700),
                        title=ft.Text("Heat & Temperature"),
                        subtitle=ft.Text("Thermodynamics, Heat Transfer"),
                        trailing=ft.Icon(ft.Icons.ARROW_FORWARD_IOS)
                    ),
                ]),
                bgcolor=ft.Colors.AMBER_50,
                border_radius=12,
                padding=10
            ),
            
            ft.Divider(height=20),
            
            # Interactive section
            ft.Text("Physics Problem:", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
            ft.TextField(
                label="Describe your physics problem or concept...",
                multiline=True,
                min_lines=3,
                max_lines=5,
                border_color=ft.Colors.BLUE_300
            ),
            ft.ElevatedButton(
                "Get Physics Help",
                icon=ft.Icons.ELECTRIC_BOLT,
                style=ft.ButtonStyle(
                    color=ft.Colors.WHITE,
                    bgcolor=ft.Colors.ORANGE_600,
                    shape=ft.RoundedRectangleBorder(radius=8)
                ),
                on_click=lambda e: page.show_snack_bar(
                    ft.SnackBar(content=ft.Text("AI Physics tutor feature coming soon!"))
                )
            )
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15),
        padding=30,
        expand=True
    )
    
    page.add(content)
