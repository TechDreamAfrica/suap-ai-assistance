import flet as ft
import random

def get_ai_help(query, topic="geography"):
    """AI help response for Geography"""
    try:
        responses = {
            "continents": "There are 7 continents: Asia (largest), Africa, North America, South America, Antarctica, Europe, and Australia/Oceania. Each has unique physical features, climates, and cultures. Continents are separated by oceans and have different time zones.",
            "climate": "Climate is the long-term weather pattern of a region. It's determined by latitude, altitude, distance from water, and ocean currents. Climate zones include tropical (hot, wet), temperate (moderate), and polar (cold). Climate change affects global weather patterns.",
            "maps": "Maps represent Earth's surface on a flat plane. Types include political (countries/borders), physical (landforms), climate, and thematic maps. Map elements include scale, legend, compass rose, and coordinates (latitude/longitude).",
            "mountains": "Mountains form through tectonic plate movement, volcanic activity, or erosion. Major ranges include Himalayas (highest), Andes (longest), Rocky Mountains, and Alps. Mountains affect climate, creating rain shadows and different ecosystems at various elevations.",
            "rivers": "Rivers are flowing water bodies that shape landscapes through erosion and deposition. Major rivers include Nile (longest), Amazon (largest volume), Mississippi, and Ganges. Rivers provide water, transportation, fertile soil, and hydroelectric power.",
            "oceans": "Earth has 5 oceans: Pacific (largest), Atlantic, Indian, Southern, and Arctic (smallest). Oceans regulate climate, provide food and resources, and enable global trade. Ocean currents distribute heat and affect weather patterns worldwide.",
            "population": "Population geography studies where people live and why. Most people live in urban areas near water sources, in moderate climates, and on flat land. Population density varies greatly between countries and regions due to resources and environment.",
            "resources": "Natural resources include renewable (water, wind, solar) and non-renewable (oil, coal, minerals). Distribution is uneven globally, leading to trade and sometimes conflict. Sustainable use is important for future generations."
        }
        
        query_lower = query.lower()
        for key, response in responses.items():
            if key in query_lower:
                return f"🤖 AI Helper: {response}"
        
        return "🤖 AI Helper: Geography studies Earth's features and how humans interact with the environment. Ask about continents, climate, maps, mountains, rivers, oceans, population, or resources for specific help!"
    except Exception:
        return "🤖 AI Helper: I'm here to help with geography concepts! Try asking about continents, climate, maps, or natural features."

class GeographyModule:
    def __init__(self, page):
        self.page = page
        self.current_quiz_level = "basic"
        self.quiz_score = 0
        self.quiz_question_index = 0
        
        # Quiz questions
        self.quiz_questions = {
            "basic": [
                {
                    "question": "How many continents are there?",
                    "options": ["5", "6", "7", "8"],
                    "correct": 2,
                    "explanation": "There are 7 continents: Asia, Africa, North America, South America, Antarctica, Europe, and Australia/Oceania."
                },
                {
                    "question": "Which is the largest ocean?",
                    "options": ["Atlantic", "Pacific", "Indian", "Arctic"],
                    "correct": 1,
                    "explanation": "The Pacific Ocean is the largest ocean, covering about one-third of Earth's surface."
                },
                {
                    "question": "What determines climate?",
                    "options": ["Only temperature", "Only rainfall", "Latitude and other factors", "Only seasons"],
                    "correct": 2,
                    "explanation": "Climate is determined by latitude, altitude, distance from water bodies, ocean currents, and other geographic factors."
                }
            ],
            "intermediate": [
                {
                    "question": "What is the longest river in the world?",
                    "options": ["Amazon", "Nile", "Mississippi", "Yangtze"],
                    "correct": 1,
                    "explanation": "The Nile River in Africa is the longest river in the world at about 6,650 kilometers."
                },
                {
                    "question": "Which mountain range contains the highest peak?",
                    "options": ["Andes", "Rocky Mountains", "Himalayas", "Alps"],
                    "correct": 2,
                    "explanation": "The Himalayas contain Mount Everest, the world's highest peak at 8,849 meters above sea level."
                },
                {
                    "question": "What causes seasons?",
                    "options": ["Distance from sun", "Earth's tilt", "Ocean currents", "Atmospheric pressure"],
                    "correct": 1,
                    "explanation": "Seasons are caused by Earth's 23.5-degree tilt as it orbits the sun, affecting how sunlight hits different regions."
                }
            ]
        }

    def create_main_view(self):
        return ft.Container(
            ft.Column([
                ft.Text("🌍 Geography", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.INDIGO_900, text_align=ft.TextAlign.CENTER),
                ft.Text("Learn about world geography, maps, climate, and natural resources", size=16, color=ft.Colors.INDIGO_700, text_align=ft.TextAlign.CENTER),
                ft.Divider(height=30),
                
                # Navigation buttons
                ft.ResponsiveRow([
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.HELP, size=30, color=ft.Colors.BLUE_700),
                                ft.Text("AI Help", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_ai_help(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.BLUE_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.QUIZ_OUTLINED, size=30, color=ft.Colors.GREEN_700),
                                ft.Text("Quizzes", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_quizzes(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.GREEN_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.SCHOOL_OUTLINED, size=30, color=ft.Colors.PURPLE_700),
                                ft.Text("Learn", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_explanations(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.PURPLE_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.MAP, size=30, color=ft.Colors.ORANGE_700),
                                ft.Text("Maps", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_maps(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.ORANGE_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                ], spacing=10, run_spacing=10),
                
                ft.Divider(height=20),
                
                # Quick overview
                ft.Container(
                    ft.Column([
                        ft.Text("📚 Geography Overview", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.INDIGO_800),
                        ft.Text("Geography is the study of Earth's features and how humans interact with the environment.", size=14),
                        ft.Text("🗺️ Key Topics:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.INDIGO_700),
                        ft.Column([
                            ft.Text("• Physical Geography (landforms, climate)", size=14),
                            ft.Text("• Human Geography (population, cities)", size=14),
                            ft.Text("• Maps and Navigation", size=14),
                            ft.Text("• Natural Resources and Environment", size=14),
                        ], spacing=5)
                    ], spacing=10),
                    bgcolor=ft.Colors.INDIGO_50,
                    border_radius=10,
                    padding=15,
                    border=ft.border.all(2, ft.Colors.INDIGO_200)
                )
            ], spacing=20),
            padding=20,
            expand=True
        )

    def show_ai_help(self):
        self.page.views.clear()
        
        query_field = ft.TextField(
            label="Ask about geography...",
            hint_text="e.g., What causes different climates?",
            multiline=True,
            min_lines=3,
            expand=True
        )
        
        response_text = ft.Text("", size=14, selectable=True)
        
        def handle_query(e):
            if query_field.value:
                response = get_ai_help(query_field.value)
                response_text.value = response
                self.page.update()
        
        view = ft.View(
            "/geography/ai_help",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/geography")),
                    title=ft.Text("AI Geography Help"),
                    bgcolor=ft.Colors.INDIGO_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("🤖 AI Geography Assistant", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.INDIGO_900),
                        query_field,
                        ft.ElevatedButton(
                            "Get Help",
                            on_click=handle_query,
                            style=ft.ButtonStyle(bgcolor=ft.Colors.INDIGO_600, color=ft.Colors.WHITE)
                        ),
                        ft.Container(response_text, bgcolor=ft.Colors.GREY_100, border_radius=10, padding=15, expand=True)
                    ], spacing=15),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def show_quizzes(self):
        self.page.views.clear()
        
        view = ft.View(
            "/geography/quizzes",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/geography")),
                    title=ft.Text("Geography Quizzes"),
                    bgcolor=ft.Colors.INDIGO_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("📝 Choose Quiz Level", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.INDIGO_900),
                        
                        ft.ResponsiveRow([
                            ft.Container(
                                ft.ElevatedButton(
                                    content=ft.Column([
                                        ft.Icon(ft.Icons.LOOKS_ONE, size=30, color=ft.Colors.GREEN_700),
                                        ft.Text("Basic", size=16, weight=ft.FontWeight.BOLD),
                                        ft.Text("Continents & oceans", size=12)
                                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                                    on_click=lambda e: self.start_quiz("basic"),
                                    style=ft.ButtonStyle(padding=20, bgcolor=ft.Colors.GREEN_50, shape=ft.RoundedRectangleBorder(radius=10))
                                ),
                                col={'xs': 12, 'sm': 6}
                            ),
                            ft.Container(
                                ft.ElevatedButton(
                                    content=ft.Column([
                                        ft.Icon(ft.Icons.LOOKS_TWO, size=30, color=ft.Colors.ORANGE_700),
                                        ft.Text("Intermediate", size=16, weight=ft.FontWeight.BOLD),
                                        ft.Text("Physical features", size=12)
                                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                                    on_click=lambda e: self.start_quiz("intermediate"),
                                    style=ft.ButtonStyle(padding=20, bgcolor=ft.Colors.ORANGE_50, shape=ft.RoundedRectangleBorder(radius=10))
                                ),
                                col={'xs': 12, 'sm': 6}
                            ),
                        ], spacing=15)
                    ], spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def start_quiz(self, level):
        self.current_quiz_level = level
        self.quiz_score = 0
        self.quiz_question_index = 0
        self.show_quiz_question()

    def show_quiz_question(self):
        questions = self.quiz_questions[self.current_quiz_level]
        if self.quiz_question_index >= len(questions):
            self.show_quiz_results()
            return
        
        question = questions[self.quiz_question_index]
        
        option_buttons = []
        for i, option in enumerate(question["options"]):
            option_buttons.append(
                ft.ElevatedButton(
                    option,
                    on_click=lambda e, idx=i: self.answer_question(idx),
                    style=ft.ButtonStyle(
                        padding=15,
                        bgcolor=ft.Colors.BLUE_50,
                        shape=ft.RoundedRectangleBorder(radius=8)
                    ),
                    expand=True
                )
            )
        
        self.page.views.clear()
        view = ft.View(
            "/geography/quiz_question",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/geography/quizzes")),
                    title=ft.Text(f"Quiz - Question {self.quiz_question_index + 1}"),
                    bgcolor=ft.Colors.INDIGO_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text(f"Question {self.quiz_question_index + 1} of {len(questions)}", size=16, color=ft.Colors.GREY_600),
                        ft.Text(question["question"], size=18, weight=ft.FontWeight.BOLD),
                        ft.Text("Choose the correct answer:", size=14, color=ft.Colors.GREY_700),
                        ft.Column(option_buttons, spacing=10)
                    ], spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def answer_question(self, selected_index):
        questions = self.quiz_questions[self.current_quiz_level]
        question = questions[self.quiz_question_index]
        
        is_correct = selected_index == question["correct"]
        if is_correct:
            self.quiz_score += 1
        
        # Show explanation
        self.page.views.clear()
        view = ft.View(
            "/geography/quiz_explanation",
            [
                ft.AppBar(
                    title=ft.Text("Answer Explanation"),
                    bgcolor=ft.Colors.INDIGO_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Icon(
                            ft.Icons.CHECK_CIRCLE if is_correct else ft.Icons.CANCEL,
                            size=60,
                            color=ft.Colors.GREEN if is_correct else ft.Colors.RED
                        ),
                        ft.Text(
                            "Correct!" if is_correct else "Incorrect!",
                            size=24,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.GREEN if is_correct else ft.Colors.RED
                        ),
                        ft.Text(f"Correct answer: {question['options'][question['correct']]}", size=16),
                        ft.Container(
                            ft.Text(question["explanation"], size=14),
                            bgcolor=ft.Colors.BLUE_50,
                            border_radius=10,
                            padding=15
                        ),
                        ft.ElevatedButton(
                            "Next Question",
                            on_click=lambda e: self.next_question(),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.INDIGO_600, color=ft.Colors.WHITE)
                        )
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def next_question(self):
        self.quiz_question_index += 1
        self.show_quiz_question()

    def show_quiz_results(self):
        total_questions = len(self.quiz_questions[self.current_quiz_level])
        percentage = (self.quiz_score / total_questions) * 100
        
        if percentage >= 80:
            message = "Excellent work! 🎉"
            color = ft.Colors.GREEN
        elif percentage >= 60:
            message = "Good job! 👍"
            color = ft.Colors.ORANGE
        else:
            message = "Keep studying! 📚"
            color = ft.Colors.RED
        
        self.page.views.clear()
        view = ft.View(
            "/geography/quiz_results",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/geography")),
                    title=ft.Text("Quiz Results"),
                    bgcolor=ft.Colors.INDIGO_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("Quiz Complete!", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.INDIGO_900),
                        ft.Text(f"Score: {self.quiz_score}/{total_questions} ({percentage:.0f}%)", size=20),
                        ft.Text(message, size=18, color=color, weight=ft.FontWeight.BOLD),
                        ft.ElevatedButton(
                            "Try Again",
                            on_click=lambda e: self.start_quiz(self.current_quiz_level),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.INDIGO_600, color=ft.Colors.WHITE)
                        ),
                        ft.ElevatedButton(
                            "Back to Geography",
                            on_click=lambda e: self.page.go("/geography")
                        )
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def show_explanations(self):
        self.page.views.clear()
        
        explanations = [
            {
                "title": "🌍 Physical Geography",
                "content": "Physical geography studies Earth's natural features:\n\n• **Landforms**: Mountains, valleys, plains, plateaus\n• **Water Bodies**: Oceans, seas, rivers, lakes\n• **Climate**: Temperature and precipitation patterns\n• **Weather**: Short-term atmospheric conditions\n\n**Processes**: Erosion, weathering, plate tectonics shape Earth's surface over time"
            },
            {
                "title": "👥 Human Geography",
                "content": "Human geography studies how people interact with Earth:\n\n• **Population**: Where people live and why\n• **Cities**: Urban development and planning\n• **Culture**: Languages, religions, customs\n• **Economics**: Trade, resources, development\n\n**Migration**: People move for jobs, safety, or better opportunities"
            },
            {
                "title": "🗺️ Maps and Navigation",
                "content": "Maps help us understand and navigate our world:\n\n• **Types**: Political, physical, climate, topographic\n• **Elements**: Scale, legend, compass rose, coordinates\n• **Projection**: How 3D Earth is shown on 2D maps\n• **GPS**: Global Positioning System for navigation\n\n**Coordinates**: Latitude (north-south) and longitude (east-west) lines"
            },
            {
                "title": "🌿 Environment and Resources",
                "content": "Geography examines human-environment relationships:\n\n• **Natural Resources**: Renewable and non-renewable\n• **Conservation**: Protecting environments for the future\n• **Climate Change**: Global warming and its effects\n• **Sustainability**: Meeting needs without harming future generations\n\n**Ecosystem Services**: Nature provides clean air, water, and food"
            }
        ]
        
        explanation_cards = []
        for explanation in explanations:
            card = ft.ExpansionTile(
                title=ft.Text(explanation["title"], size=16, weight=ft.FontWeight.BOLD),
                subtitle=ft.Text("Tap to expand"),
                controls=[
                    ft.Container(
                        ft.Text(explanation["content"], size=14),
                        padding=15,
                        bgcolor=ft.Colors.INDIGO_50,
                        border_radius=8
                    )
                ]
            )
            explanation_cards.append(card)
        
        view = ft.View(
            "/geography/explanations",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/geography")),
                    title=ft.Text("Geography Concepts"),
                    bgcolor=ft.Colors.INDIGO_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("📚 Learn Geography", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.INDIGO_900),
                        ft.Text("Explore the fundamental concepts of geography", size=16, color=ft.Colors.INDIGO_700),
                        ft.Column(explanation_cards, spacing=5)
                    ], spacing=15),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def show_maps(self):
        self.page.views.clear()
        
        map_activities = [
            {
                "title": "🗺️ World Map Quiz",
                "description": "Test your knowledge of countries and capitals",
                "action": "Start Quiz"
            },
            {
                "title": "🏔️ Physical Features",
                "description": "Learn about mountains, rivers, and landforms",
                "action": "Explore"
            },
            {
                "title": "🌡️ Climate Zones",
                "description": "Understand different climate regions",
                "action": "Learn More"
            },
            {
                "title": "📍 Coordinate Practice",
                "description": "Practice using latitude and longitude",
                "action": "Practice"
            }
        ]
        
        activity_cards = []
        for activity in map_activities:
            card = ft.Container(
                ft.Column([
                    ft.Text(activity["title"], size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.INDIGO_900),
                    ft.Text(activity["description"], size=14, color=ft.Colors.INDIGO_700),
                    ft.ElevatedButton(
                        activity["action"],
                        on_click=lambda e, title=activity["title"]: self.start_map_activity(title),
                        style=ft.ButtonStyle(bgcolor=ft.Colors.INDIGO_600, color=ft.Colors.WHITE)
                    )
                ], spacing=10),
                bgcolor=ft.Colors.INDIGO_50,
                border_radius=10,
                padding=15,
                border=ft.border.all(1, ft.Colors.INDIGO_200)
            )
            activity_cards.append(card)
        
        view = ft.View(
            "/geography/maps",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/geography")),
                    title=ft.Text("Map Activities"),
                    bgcolor=ft.Colors.INDIGO_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("🗺️ Interactive Maps", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.INDIGO_900),
                        ft.Text("Explore the world through interactive activities", size=16, color=ft.Colors.INDIGO_700),
                        ft.Column(activity_cards, spacing=15)
                    ], spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def start_map_activity(self, activity_title):
        self.page.show_snack_bar(
            ft.SnackBar(content=ft.Text(f"Map activity '{activity_title}' will be available soon!"))
        )

def geography_page(page: ft.Page):
    page.title = "Geography - Student AI Assistance"
    page.scroll = ft.ScrollMode.AUTO
    
    # Clear page content first
    page.clean()
    
    page.appbar = ft.AppBar(
        leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: page.go("/")),
        title=ft.Text("Geography"),
        bgcolor=ft.Colors.INDIGO_700,
        center_title=True
    )
    
    module = GeographyModule(page)
    page.add(module.create_main_view())
