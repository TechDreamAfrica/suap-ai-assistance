import flet as ft

# Import science modules
try:
    from topics.science.scientific_method import scientific_method_page
except ImportError:
    scientific_method_page = None

try:
    from topics.science.measurement_units import measurement_units_page
except ImportError:
    measurement_units_page = None

try:
    from topics.science.biology import biology_page
except ImportError:
    biology_page = None

try:
    from topics.science.classification import classification_page
except ImportError:
    classification_page = None

try:
    from topics.science.physics import physics_page
except ImportError:
    physics_page = None

try:
    from topics.science.chemistry import chemistry_page
except ImportError:
    chemistry_page = None

try:
    from topics.science.ecology import ecology_page
except ImportError:
    ecology_page = None

try:
    from topics.science.genetics import genetics_page
except ImportError:
    genetics_page = None

try:
    from topics.science.earth_science import earth_science_page
except ImportError:
    earth_science_page = None

def show_coming_soon(page, message):
    page.snack_bar = ft.SnackBar(content=ft.Text(message))
    page.snack_bar.open = True
    page.update()

def science_page(page: ft.Page):
    page.title = "Science - Student AI Assistance"
    page.scroll = ft.ScrollMode.AUTO
    
    # AppBar with back button
    page.appbar = ft.AppBar(
        leading=ft.IconButton(
            ft.Icons.ARROW_BACK,
            on_click=lambda e: page.go("/")
        ),
        title=ft.Text("Science Hub"),
        bgcolor=ft.Colors.BLUE_700,
        center_title=True
    )
    
    # Main content
    content = ft.Container(
        ft.Column([
            ft.Text(
                "🔬 Science Discovery Center",
                size=28,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLUE_900,
                text_align=ft.TextAlign.CENTER
            ),
            ft.Text(
                "Explore science concepts, conduct virtual experiments, and get AI-powered explanations!",
                size=16,
                color=ft.Colors.BLUE_700,
                text_align=ft.TextAlign.CENTER
            ),
            ft.Divider(height=30),
            
            # Science topics
            ft.Text("Available Topics:", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
            
            # Basic Science Section
            ft.Text("🔬 Basic Science Concepts", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
            ft.ResponsiveRow([
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.SCIENCE, size=30, color=ft.Colors.BLUE_700),
                            ft.Text("Scientific Method", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Observation, Hypothesis, Testing", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.BLUE_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: scientific_method_page(page) if scientific_method_page else show_coming_soon(page, "Scientific Method module loading...")
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.STRAIGHTEN, size=30, color=ft.Colors.GREEN_700),
                            ft.Text("Measurement & Units", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Metric System, Conversions", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.GREEN_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: measurement_units_page(page) if measurement_units_page else show_coming_soon(page, "Measurement & Units module loading...")
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.ACCOUNT_TREE, size=30, color=ft.Colors.ORANGE_700),
                            ft.Text("Classification", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Organizing, Categorizing", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.ORANGE_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: classification_page(page) if classification_page else show_coming_soon(page, "Classification module loading...")
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
            ], spacing=10, run_spacing=10),
            
            # Physical Sciences Section
            ft.Text("⚡ Physical Sciences", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
            ft.ResponsiveRow([
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.ELECTRIC_BOLT, size=30, color=ft.Colors.PURPLE_700),
                            ft.Text("Physics", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Motion, Forces, Energy", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.PURPLE_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: physics_page(page) if physics_page else show_coming_soon(page, "Physics module loading...")
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.SCIENCE_OUTLINED, size=30, color=ft.Colors.TEAL_700),
                            ft.Text("Chemistry", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Elements, Compounds, Reactions", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.TEAL_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: chemistry_page(page) if chemistry_page else show_coming_soon(page, "Chemistry module loading...")
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.PUBLIC, size=30, color=ft.Colors.INDIGO_700),
                            ft.Text("Earth Science", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Geology, Weather, Space", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.INDIGO_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: earth_science_page(page) if earth_science_page else show_coming_soon(page, "Earth Science module loading...")
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
            ], spacing=10, run_spacing=10),
            
            # Life Sciences Section
            ft.Text("🌱 Life Sciences", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.RED_700),
            ft.ResponsiveRow([
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.PETS, size=30, color=ft.Colors.PINK_700),
                            ft.Text("Biology", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Living Organisms, Cells", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.PINK_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: biology_page(page) if biology_page else show_coming_soon(page, "Biology module loading...")
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.FOREST, size=30, color=ft.Colors.CYAN_700),
                            ft.Text("Ecology", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Ecosystems, Environment", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.CYAN_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: ecology_page(page) if ecology_page else show_coming_soon(page, "Ecology module loading...")
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.BIOTECH, size=30, color=ft.Colors.LIME_700),
                            ft.Text("Genetics", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("DNA, Heredity, Evolution", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.LIME_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: genetics_page(page) if genetics_page else show_coming_soon(page, "Genetics module loading...")
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.HEALING, size=30, color=ft.Colors.DEEP_PURPLE_700),
                            ft.Text("Human Body", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Anatomy, Physiology", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.DEEP_PURPLE_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: show_coming_soon(page, "Human Body module coming soon!")
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.WATER_DROP, size=30, color=ft.Colors.BROWN_700),
                            ft.Text("Biochemistry", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Molecules of Life", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.BROWN_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: show_coming_soon(page, "Biochemistry module coming soon!")
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Icon(ft.Icons.PRECISION_MANUFACTURING, size=30, color=ft.Colors.DEEP_ORANGE_700),
                            ft.Text("Laboratory Skills", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Text("Equipment, Safety, Methods", size=12, text_align=ft.TextAlign.CENTER)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.DEEP_ORANGE_50,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=lambda e: show_coming_soon(page, "Laboratory Skills module coming soon!")
                    ),
                    col={'xs': 12, 'sm': 6, 'md': 4}
                ),
            ], spacing=10, run_spacing=10),
            
            ft.Divider(height=20),
            
            # Interactive section
            ft.Text("🤖 AI Science Assistant", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
            ft.Container(
                ft.Column([
                    ft.TextField(
                        label="Ask your science question here...",
                        hint_text="e.g., How does photosynthesis work? or Explain the water cycle",
                        multiline=True,
                        min_lines=3,
                        max_lines=5,
                        border_color=ft.Colors.BLUE_300,
                        expand=True
                    ),
                    ft.Row([
                        ft.ElevatedButton(
                            "Get Science Help",
                            icon=ft.Icons.SCIENCE,
                            style=ft.ButtonStyle(
                                color=ft.Colors.WHITE,
                                bgcolor=ft.Colors.GREEN_600,
                                shape=ft.RoundedRectangleBorder(radius=8)
                            ),
                            on_click=lambda e: show_coming_soon(page, "AI Science tutor will provide detailed explanations soon!"),
                            expand=True
                        ),
                        ft.ElevatedButton(
                            "Virtual Experiment",
                            icon=ft.Icons.PRECISION_MANUFACTURING,
                            style=ft.ButtonStyle(
                                color=ft.Colors.WHITE,
                                bgcolor=ft.Colors.ORANGE_600,
                                shape=ft.RoundedRectangleBorder(radius=8)
                            ),
                            on_click=lambda e: show_coming_soon(page, "Virtual lab experiments coming soon!"),
                            expand=True
                        ),
                    ], spacing=10),
                    ft.Row([
                        ft.ElevatedButton(
                            "Study Guide",
                            icon=ft.Icons.MENU_BOOK,
                            style=ft.ButtonStyle(
                                color=ft.Colors.WHITE,
                                bgcolor=ft.Colors.PURPLE_600,
                                shape=ft.RoundedRectangleBorder(radius=8)
                            ),
                            on_click=lambda e: (
                                setattr(page, 'snack_bar', ft.SnackBar(content=ft.Text("Interactive study guides coming soon!"))),
                                setattr(page.snack_bar, 'open', True),
                                page.update()
                            )[2],
                            expand=True
                        ),
                        ft.ElevatedButton(
                            "Science Quiz",
                            icon=ft.Icons.QUIZ_OUTLINED,
                            style=ft.ButtonStyle(
                                color=ft.Colors.WHITE,
                                bgcolor=ft.Colors.BLUE_600,
                                shape=ft.RoundedRectangleBorder(radius=8)
                            ),
                            on_click=lambda e: (
                                setattr(page, 'snack_bar', ft.SnackBar(content=ft.Text("Science knowledge tests coming soon!"))),
                                setattr(page.snack_bar, 'open', True),
                                page.update()
                            )[2],
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
