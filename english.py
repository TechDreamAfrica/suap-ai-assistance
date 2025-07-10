import flet as ft

def english_page(page: ft.Page):
    page.title = "English - Student AI Assistance"
    page.scroll = ft.ScrollMode.AUTO
    
    # AppBar with back button
    page.appbar = ft.AppBar(
        leading=ft.IconButton(
            ft.Icons.ARROW_BACK,
            on_click=lambda e: page.go("/")
        ),
        title=ft.Text("English Learning"),
        bgcolor=ft.Colors.BLUE_700,
        center_title=True
    )
    
    # Main content
    content = ft.Container(
        ft.Column([
            ft.Text(
                "📖 English Language Center",
                size=28,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLUE_900,
                text_align=ft.TextAlign.CENTER
            ),
            ft.Text(
                "Improve your vocabulary, grammar, reading comprehension and writing skills!",
                size=16,
                color=ft.Colors.BLUE_700,
                text_align=ft.TextAlign.CENTER
            ),
            ft.Divider(height=30),
            
            # English topics
            ft.Text("Available Topics:", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
            
            # Foundation Skills Section
            ft.Text("📚 Foundation Skills", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
            ft.ResponsiveRow([
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.SPELLCHECK, size=30, color=ft.Colors.BLUE_700),
                            ft.Text("Grammar & Syntax", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Tenses, Parts of Speech", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.BLUE_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: page.go("/grammar")
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.LIBRARY_BOOKS, size=30, color=ft.Colors.GREEN_700),
                            ft.Text("Vocabulary Building", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Word Formation, Context", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.GREEN_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: page.go("/vocabulary")
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.RECORD_VOICE_OVER, size=30, color=ft.Colors.ORANGE_700),
                            ft.Text("Pronunciation", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Speaking, Phonetics", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.ORANGE_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: page.show_snack_bar(ft.SnackBar(content=ft.Text("Pronunciation module coming soon!")))
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
            ], spacing=10, run_spacing=10),
            
            # Reading & Comprehension Section
            ft.Text("📖 Reading & Comprehension", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
            ft.ResponsiveRow([
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.CHROME_READER_MODE, size=30, color=ft.Colors.PURPLE_700),
                            ft.Text("Reading Skills", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Comprehension, Analysis", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.PURPLE_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: page.go("/reading-comprehension")
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.MENU_BOOK, size=30, color=ft.Colors.TEAL_700),
                            ft.Text("Literature Analysis", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Poetry, Prose, Themes", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.TEAL_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: page.show_snack_bar(ft.SnackBar(content=ft.Text("Literature Analysis module coming soon!")))
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.SEARCH, size=30, color=ft.Colors.INDIGO_700),
                            ft.Text("Critical Thinking", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Inference, Evaluation", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.INDIGO_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: page.show_snack_bar(ft.SnackBar(content=ft.Text("Critical Thinking module coming soon!")))
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
            ], spacing=10, run_spacing=10),
            
            # Writing & Expression Section
            ft.Text("✍️ Writing & Expression", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.RED_700),
            ft.ResponsiveRow([
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.EDIT, size=30, color=ft.Colors.PINK_700),
                            ft.Text("Essay Writing", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Structure, Arguments", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.PINK_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: page.show_snack_bar(ft.SnackBar(content=ft.Text("Essay Writing module coming soon!")))
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.CREATE, size=30, color=ft.Colors.CYAN_700),
                            ft.Text("Creative Writing", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Stories, Poetry, Dialogue", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.CYAN_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: page.show_snack_bar(ft.SnackBar(content=ft.Text("Creative Writing module coming soon!")))
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.ASSIGNMENT, size=30, color=ft.Colors.LIME_700),
                            ft.Text("Academic Writing", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Reports, Research", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.LIME_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: page.show_snack_bar(ft.SnackBar(content=ft.Text("Academic Writing module coming soon!")))
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.FORMAT_QUOTE, size=30, color=ft.Colors.DEEP_PURPLE_700),
                            ft.Text("Language Devices", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Metaphors, Imagery", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.DEEP_PURPLE_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: page.show_snack_bar(ft.SnackBar(content=ft.Text("Language Devices module coming soon!")))
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.TRANSLATE, size=30, color=ft.Colors.BROWN_700),
                            ft.Text("Language Varieties", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Dialects, Registers", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.BROWN_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: page.show_snack_bar(ft.SnackBar(content=ft.Text("Language Varieties module coming soon!")))
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.CHAT, size=30, color=ft.Colors.DEEP_ORANGE_700),
                            ft.Text("Communication Skills", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Speaking, Listening", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.DEEP_ORANGE_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: page.show_snack_bar(ft.SnackBar(content=ft.Text("Communication Skills module coming soon!")))
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
            ], spacing=10, run_spacing=10),
            
            ft.Divider(height=20),
            
            # Interactive section
            ft.Text("🤖 AI English Assistant", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
            ft.Container(
                ft.Column([
                    ft.TextField(
                        label="Practice your English here...",
                        hint_text="e.g., Check my grammar, help with essay structure, or explain a literary device",
                        multiline=True,
                        min_lines=3,
                        max_lines=5,
                        border_color=ft.Colors.BLUE_300,
                        expand=True
                    ),
                    ft.Row([
                        ft.ElevatedButton(
                            "Grammar Check",
                            icon=ft.Icons.SPELLCHECK,
                            style=ft.ButtonStyle(
                                color=ft.Colors.WHITE,
                                bgcolor=ft.Colors.BLUE_600,
                                shape=ft.RoundedRectangleBorder(radius=8)
                            ),
                            on_click=lambda e: page.show_snack_bar(
                                ft.SnackBar(content=ft.Text("AI Grammar checker coming soon!"))
                            ),
                            expand=True
                        ),
                        ft.ElevatedButton(
                            "Vocabulary Help",
                            icon=ft.Icons.LIBRARY_BOOKS,
                            style=ft.ButtonStyle(
                                color=ft.Colors.WHITE,
                                bgcolor=ft.Colors.GREEN_600,
                                shape=ft.RoundedRectangleBorder(radius=8)
                            ),
                            on_click=lambda e: page.show_snack_bar(
                                ft.SnackBar(content=ft.Text("Vocabulary assistant coming soon!"))
                            ),
                            expand=True
                        ),
                    ], spacing=10),
                    ft.Row([
                        ft.ElevatedButton(
                            "Writing Assistant",
                            icon=ft.Icons.EDIT,
                            style=ft.ButtonStyle(
                                color=ft.Colors.WHITE,
                                bgcolor=ft.Colors.ORANGE_600,
                                shape=ft.RoundedRectangleBorder(radius=8)
                            ),
                            on_click=lambda e: page.show_snack_bar(
                                ft.SnackBar(content=ft.Text("AI Writing assistant coming soon!"))
                            ),
                            expand=True
                        ),
                        ft.ElevatedButton(
                            "Reading Practice",
                            icon=ft.Icons.CHROME_READER_MODE,
                            style=ft.ButtonStyle(
                                color=ft.Colors.WHITE,
                                bgcolor=ft.Colors.PURPLE_600,
                                shape=ft.RoundedRectangleBorder(radius=8)
                            ),
                            on_click=lambda e: page.show_snack_bar(
                                ft.SnackBar(content=ft.Text("Interactive reading exercises coming soon!"))
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
