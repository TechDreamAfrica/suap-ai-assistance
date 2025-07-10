import flet as ft
from maths_tutor import maths_tutor_page
from science import science_page
from history_teller import history_page
from english import english_page
from computing import computing_page
from physics import physics_page
from social_studies import social_studies_page
from chemistry_module import chemistry_page
from biology_module import biology_page
from geography_module import geography_page
from literature_module import literature_page
from art_design_module import art_design_page

# Import mathematics topic pages
from topics.mathematics.basic_arithmetic import basic_arithmetic_page
from topics.mathematics.fractions_decimals import fractions_decimals_page
from topics.mathematics.number_patterns import number_patterns_page
from topics.mathematics.algebra import algebra_page
from topics.mathematics.geometry import geometry_page
from topics.mathematics.trigonometry import trigonometry_page
from topics.mathematics.quadratic_equations import quadratic_equations_page
from topics.mathematics.statistics_probability import statistics_probability_page
from topics.mathematics.linear_functions import linear_functions_page
from topics.mathematics.calculus import calculus_page
from topics.mathematics.matrices import matrices_page
from topics.mathematics.complex_numbers import complex_numbers_page
from topics.mathematics.differential_equations import differential_equations_page
from topics.mathematics.vector_calculus import vector_calculus_page
from topics.mathematics.number_theory import number_theory_page

# Import other subject topic pages
from topics.english.grammar import grammar_page
from topics.english.vocabulary import vocabulary_page
from topics.english.reading_comprehension import reading_comprehension_page
from topics.social_studies.civics import civics_page
from topics.social_studies.economics import economics_page
from topics.social_studies.culture import culture_page
from topics.computing.programming_basics import programming_basics_page
from topics.computing.digital_literacy import digital_literacy_page
from topics.computing.web_design import web_design_page
from topics.history.ancient_civilizations import ancient_civilizations_page
from topics.history.world_wars import world_wars_page
from topics.history.african_history import african_history_page
from topics.geography.physical_geography import physical_geography_page
from topics.geography.human_geography import human_geography_page
from topics.geography.world_regions import world_regions_page
from topics.literature.poetry import poetry_page
from topics.literature.drama import drama_page
from topics.literature.african_literature import african_literature_page
from topics.art_design.visual_arts import visual_arts_page
from topics.art_design.design_principles import design_principles_page
from topics.art_design.digital_art import digital_art_page

def main(page: ft.Page):
    page.title = "Sua Pa Student AI Assistance"
    page.scroll = ft.ScrollMode.AUTO

    def route_change(route):
        page.controls.clear()
        
        # Route handling
        if page.route == "/maths":
            maths_tutor_page(page)
        elif page.route == "/science":
            science_page(page)
        elif page.route == "/history":
            history_page(page)
        elif page.route == "/english":
            english_page(page)
        elif page.route == "/computing":
            computing_page(page)
        elif page.route == "/physics":
            physics_page(page)
        elif page.route == "/social_studies":
            social_studies_page(page)
        elif page.route == "/chemistry":
            chemistry_page(page)
        elif page.route == "/biology":
            biology_page(page)
        elif page.route == "/geography":
            geography_page(page)
        elif page.route == "/literature":
            literature_page(page)
        elif page.route == "/art_design":
            art_design_page(page)
        # Mathematics topic routes
        elif page.route == "/basic-arithmetic":
            basic_arithmetic_page(page)
        elif page.route == "/fractions-decimals":
            fractions_decimals_page(page)
        elif page.route == "/number-patterns":
            number_patterns_page(page)
        elif page.route == "/algebra":
            algebra_page(page)
        elif page.route == "/geometry":
            geometry_page(page)
        elif page.route == "/trigonometry":
            trigonometry_page(page)
        elif page.route == "/quadratic-equations":
            quadratic_equations_page(page)
        elif page.route == "/statistics-probability":
            statistics_probability_page(page)
        elif page.route == "/linear-functions":
            linear_functions_page(page)
        elif page.route == "/calculus":
            calculus_page(page)
        elif page.route == "/matrices":
            matrices_page(page)
        elif page.route == "/complex-numbers":
            complex_numbers_page(page)
        elif page.route == "/differential-equations":
            differential_equations_page(page)
        elif page.route == "/vector-calculus":
            vector_calculus_page(page)
        elif page.route == "/number-theory":
            number_theory_page(page)
        # English topic routes
        elif page.route == "/grammar":
            grammar_page(page)
        elif page.route == "/vocabulary":
            vocabulary_page(page)
        elif page.route == "/reading-comprehension":
            reading_comprehension_page(page)
        # Social Studies topic routes
        elif page.route == "/civics":
            civics_page(page)
        elif page.route == "/economics":
            economics_page(page)
        elif page.route == "/culture":
            culture_page(page)
        # Computing topic routes
        elif page.route == "/programming-basics":
            programming_basics_page(page)
        elif page.route == "/digital-literacy":
            digital_literacy_page(page)
        elif page.route == "/web-design":
            web_design_page(page)
        # History topic routes
        elif page.route == "/ancient-civilizations":
            ancient_civilizations_page(page)
        elif page.route == "/world-wars":
            world_wars_page(page)
        elif page.route == "/african-history":
            african_history_page(page)
        # Geography topic routes
        elif page.route == "/physical-geography":
            physical_geography_page(page)
        elif page.route == "/human-geography":
            human_geography_page(page)
        elif page.route == "/world-regions":
            world_regions_page(page)
        # Literature topic routes
        elif page.route == "/poetry":
            poetry_page(page)
        elif page.route == "/drama":
            drama_page(page)
        elif page.route == "/african-literature":
            african_literature_page(page)
        # Art & Design topic routes
        elif page.route == "/visual-arts":
            visual_arts_page(page)
        elif page.route == "/design-principles":
            design_principles_page(page)
        elif page.route == "/digital-art":
            digital_art_page(page)
        else:
            # Home page
            home_page(page)
        
        page.update()

    def home_page(page: ft.Page):
        # Banner
        banner = ft.Banner(
            bgcolor=ft.Colors.AMBER_200,
            leading=ft.Icon(ft.Icons.SCHOOL_OUTLINED, size=140, color=ft.Colors.BLUE_900),
            content=ft.Text("Welcome to the Student AI Assistance App!", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
            actions=[ft.TextButton("OK", on_click=lambda e: setattr(page.banner, 'open', False))]
        )

        # AppBar
        app_bar = ft.AppBar(
            title=ft.Text("Student AI Assistance"),
            bgcolor=ft.Colors.BLUE_700,
            center_title=True
        )

        # Welcome Banner with Help and Instructions
        welcome_banner = ft.Container(
            content=ft.Column([
                ft.Text(
                    "Welcome to Sua Pa AI Learning Companion!", 
                    size=24, 
                    weight=ft.FontWeight.BOLD, 
                    color=ft.Colors.BLUE_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Text(
                    "Choose any subject below to start your personalized learning journey with AI assistance.",
                    size=16,
                    color=ft.Colors.BLUE_700,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Row([
                    ft.ElevatedButton(
                        "Help",
                        icon=ft.Icons.HELP,
                        style=ft.ButtonStyle(
                            color=ft.Colors.WHITE,
                            bgcolor=ft.Colors.BLUE_600,
                            shape=ft.RoundedRectangleBorder(radius=8)
                        ),
                        on_click=lambda e: page.show_snack_bar(
                            ft.SnackBar(content=ft.Text("Click on any subject to get AI-powered assistance and tutoring!"))
                        )
                    ),
                    ft.ElevatedButton(
                        "Instructions",
                        icon=ft.Icons.INFO_OUTLINE,
                        style=ft.ButtonStyle(
                            color=ft.Colors.WHITE,
                            bgcolor=ft.Colors.GREEN_600,
                            shape=ft.RoundedRectangleBorder(radius=8)
                        ),
                        on_click=lambda e: page.show_snack_bar(
                            ft.SnackBar(content=ft.Text("1. Select a subject 2. Ask questions 3. Get instant AI help and explanations!"))
                        )
                    )
                ], alignment=ft.MainAxisAlignment.CENTER, spacing=15)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15),
            bgcolor=ft.Colors.AMBER_50,
            padding=25,
            border_radius=12,
            border=ft.border.all(2, ft.Colors.AMBER_300),
            margin=ft.margin.only(bottom=20)
        )

        # Button helper function
        def button(title, icon, description, route):
            return ft.ElevatedButton(
                content=ft.Row([
                    ft.Icon(icon, size=40, color=ft.Colors.BLUE_700),
                    ft.Column([
                        ft.Text(title, size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                        ft.Text(description, size=14, color=ft.Colors.BLUE_900, text_align=ft.TextAlign.LEFT, overflow=ft.TextOverflow.VISIBLE)
                    ], spacing=5, expand=True)
                ], alignment=ft.MainAxisAlignment.START, vertical_alignment=ft.CrossAxisAlignment.CENTER),
                style=ft.ButtonStyle(
                    padding=20,
                    bgcolor=ft.Colors.AMBER_100,
                    shape=ft.RoundedRectangleBorder(radius=12)
                ),
                expand=True,
                on_click=lambda e: page.go(route)
            )

        # Responsive layout
        grid = ft.ResponsiveRow([
            ft.Container(button("Maths Tutor", ft.Icons.FUNCTIONS, "Practice math problems, get step-by-step solutions, and quizzes.", "/maths"), col={'xs':12, 'sm':6, 'md':4}),
            ft.Container(button("Science", ft.Icons.SCIENCE, "Explore science concepts, experiments, and Q&A.", "/science"), col={'xs':12, 'sm':6, 'md':4}),
            ft.Container(button("History Teller", ft.Icons.MAPS_HOME_WORK, "Learn about African and world history interactively.", "/history"), col={'xs':12, 'sm':6, 'md':4}),
            ft.Container(button("English", ft.Icons.LANGUAGE, "Improve your vocabulary, grammar, and comprehension.", "/english"), col={'xs':12, 'sm':6, 'md':4}),
            ft.Container(button("Social Studies", ft.Icons.PEOPLE, "Understand society, culture, and civic education.", "/social_studies"), col={'xs':12, 'sm':6, 'md':4}),
            ft.Container(button("Computing", ft.Icons.COMPUTER, "Learn ICT, coding, and digital skills.", "/computing"), col={'xs':12, 'sm':6, 'md':4}),
            ft.Container(button("Physics", ft.Icons.ELECTRIC_BOLT, "Master physics concepts, laws, and problem-solving techniques.", "/physics"), col={'xs':12, 'sm':6, 'md':4}),
            ft.Container(button("Chemistry", ft.Icons.SCIENCE_OUTLINED, "Explore chemical reactions, formulas, and laboratory experiments.", "/chemistry"), col={'xs':12, 'sm':6, 'md':4}),
            ft.Container(button("Biology", ft.Icons.PETS, "Discover life sciences, anatomy, ecology, and biological processes.", "/biology"), col={'xs':12, 'sm':6, 'md':4}),
            ft.Container(button("Geography", ft.Icons.PUBLIC, "Learn about world geography, maps, climate, and natural resources.", "/geography"), col={'xs':12, 'sm':6, 'md':4}),
            ft.Container(button("Literature", ft.Icons.MENU_BOOK, "Analyze literary works, poetry, and creative writing techniques.", "/literature"), col={'xs':12, 'sm':6, 'md':4}),
            ft.Container(button("Art & Design", ft.Icons.PALETTE, "Explore visual arts, design principles, and creative expression.", "/art_design"), col={'xs':12, 'sm':6, 'md':4}),
        ], spacing=20, run_spacing=20, alignment=ft.MainAxisAlignment.CENTER)

        # Main layout
        page.banner = banner
        page.banner.open = True
        page.appbar = app_bar
        
        # Create scrollable content area
        content_area = ft.Container(
            ft.Column([
                welcome_banner,
                grid
            ], spacing=0),
            alignment=ft.alignment.center,
            padding=30,
            expand=True
        )
        
        # Set fixed footer at bottom
        page.bottom_appbar = ft.BottomAppBar(
            bgcolor=ft.Colors.BLUE_700,
            content=ft.Container(
                ft.Text("© 2025 Sua Pa Student AI Assistance | Powered by Tech Dream Africa", 
                       size=14, 
                       color=ft.Colors.WHITE,
                       text_align=ft.TextAlign.CENTER),
                padding=10,
                alignment=ft.alignment.center
            )
        )
        
        page.add(content_area)

    # Set up routing
    page.on_route_change = route_change
    page.go("/")  # Navigate to home page

if __name__ == "__main__":
    ft.app(target=main)
