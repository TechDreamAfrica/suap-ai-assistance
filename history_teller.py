import flet as ft

def history_page(page: ft.Page):
    page.title = "History Teller - Student AI Assistance"
    page.scroll = ft.ScrollMode.AUTO
    
    # AppBar with back button
    page.appbar = ft.AppBar(
        leading=ft.IconButton(
            ft.Icons.ARROW_BACK,
            on_click=lambda e: page.go("/")
        ),
        title=ft.Text("History Teller"),
        bgcolor=ft.Colors.BLUE_700,
        center_title=True
    )
    
    # Main content
    content = ft.Container(
        ft.Column([
            ft.Text(
                "📚 History Discovery Portal",
                size=28,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLUE_900,
                text_align=ft.TextAlign.CENTER
            ),
            ft.Text(
                "Explore African and world history with interactive AI storytelling!",
                size=16,
                color=ft.Colors.BLUE_700,
                text_align=ft.TextAlign.CENTER
            ),
            ft.Divider(height=30),
            
            # History topics
            ft.Text("Historical Periods & Regions:", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
            ft.Container(
                ft.Column([
                    ft.ListTile(
                        leading=ft.Icon(ft.Icons.ACCOUNT_BALANCE, color=ft.Colors.BROWN_700),
                        title=ft.Text("Ancient Civilizations"),
                        subtitle=ft.Text("Egypt, Greece, Rome, Mesopotamia"),
                        trailing=ft.Icon(ft.Icons.ARROW_FORWARD_IOS)
                    ),
                    ft.ListTile(
                        leading=ft.Icon(ft.Icons.TERRAIN, color=ft.Colors.GREEN_700),
                        title=ft.Text("African History"),
                        subtitle=ft.Text("Kingdoms, Empires, Colonial Period"),
                        trailing=ft.Icon(ft.Icons.ARROW_FORWARD_IOS)
                    ),
                    ft.ListTile(
                        leading=ft.Icon(ft.Icons.CASTLE, color=ft.Colors.PURPLE_700),
                        title=ft.Text("Medieval Period"),
                        subtitle=ft.Text("Middle Ages, Feudalism, Crusades"),
                        trailing=ft.Icon(ft.Icons.ARROW_FORWARD_IOS)
                    ),
                    ft.ListTile(
                        leading=ft.Icon(ft.Icons.FACTORY, color=ft.Colors.ORANGE_700),
                        title=ft.Text("Modern History"),
                        subtitle=ft.Text("Industrial Revolution, World Wars"),
                        trailing=ft.Icon(ft.Icons.ARROW_FORWARD_IOS)
                    ),
                ]),
                bgcolor=ft.Colors.AMBER_50,
                border_radius=12,
                padding=10
            ),
            
            ft.Divider(height=20),
            
            # Interactive section
            ft.Text("Ask About History:", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
            ft.TextField(
                label="What historical topic interests you?",
                multiline=True,
                min_lines=3,
                max_lines=5,
                border_color=ft.Colors.BLUE_300
            ),
            ft.ElevatedButton(
                "Get Historical Insights",
                icon=ft.Icons.HISTORY_EDU,
                style=ft.ButtonStyle(
                    color=ft.Colors.WHITE,
                    bgcolor=ft.Colors.BROWN_600,
                    shape=ft.RoundedRectangleBorder(radius=8)
                ),
                on_click=lambda e: page.show_snack_bar(
                    ft.SnackBar(content=ft.Text("AI History tutor feature coming soon!"))
                )
            )
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15),
        padding=30,
        expand=True
    )
    
    page.add(content)
