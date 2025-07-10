import flet as ft
import random

def get_ai_help(query, topic="social_studies"):
    """AI help response for Social Studies"""
    try:
        responses = {
            "government": "Government is the system by which a country is organized and ruled. It includes institutions like the executive (president/prime minister), legislative (parliament), and judicial (courts). Democratic governments are elected by the people, while autocratic ones are not.",
            "democracy": "Democracy is a system of government where power comes from the people. Citizens elect their leaders and have rights like freedom of speech, assembly, and voting. It includes principles like majority rule, minority rights, and separation of powers.",
            "citizenship": "Citizenship involves rights and responsibilities. Rights include voting, freedom of expression, and equal treatment. Responsibilities include following laws, paying taxes, and participating in community life. Good citizens are informed and engaged.",
            "culture": "Culture includes beliefs, customs, arts, and ways of life shared by a group of people. It encompasses language, religion, food, music, and traditions. Culture shapes identity and helps communities maintain their heritage.",
            "economics": "Economics studies how societies use resources to meet needs and wants. It includes concepts like supply and demand, production, consumption, and trade. Economic systems can be market-based, command-based, or mixed.",
            "geography": "Geography studies the Earth's physical features and human activities. It includes physical geography (landforms, climate, water) and human geography (population, cities, culture). Geography helps us understand our world.",
            "history": "History is the study of past events and how they shape the present. It helps us understand how societies developed, learn from mistakes, and appreciate our heritage. Historical thinking involves analyzing sources and understanding cause and effect.",
            "society": "Society is a group of people living together in an organized community. It includes social institutions (family, school, church), social roles, and relationships. Societies have norms, values, and ways of organizing themselves."
        }
        
        query_lower = query.lower()
        for key, response in responses.items():
            if key in query_lower:
                return f"🤖 AI Helper: {response}"
        
        return "🤖 AI Helper: Social Studies explores how people live together in communities. Ask about government, democracy, citizenship, culture, economics, or society for specific help!"
    except Exception:
        return "🤖 AI Helper: I'm here to help with social studies concepts! Try asking about government, democracy, citizenship, or culture."

class SocialStudiesModule:
    def __init__(self, page):
        self.page = page
        self.current_quiz_level = "basic"
        self.quiz_score = 0
        self.quiz_question_index = 0
        
        # Quiz questions
        self.quiz_questions = {
            "basic": [
                {
                    "question": "What is democracy?",
                    "options": ["Rule by one person", "Rule by the people", "Rule by the wealthy", "Rule by the military"],
                    "correct": 1,
                    "explanation": "Democracy comes from Greek words meaning 'rule by the people.' In a democracy, citizens elect their leaders and have a say in government decisions."
                },
                {
                    "question": "What is a citizen's most important responsibility?",
                    "options": ["Paying taxes", "Voting", "Following laws", "All of the above"],
                    "correct": 3,
                    "explanation": "Citizens have multiple responsibilities including paying taxes, voting, and following laws. All are important for a functioning society."
                },
                {
                    "question": "Which branch of government makes laws?",
                    "options": ["Executive", "Legislative", "Judicial", "Administrative"],
                    "correct": 1,
                    "explanation": "The legislative branch (like Congress or Parliament) makes laws. The executive enforces them, and the judicial interprets them."
                }
            ],
            "intermediate": [
                {
                    "question": "What is the separation of powers?",
                    "options": ["Dividing government into branches", "Separating rich and poor", "Dividing land", "Separating countries"],
                    "correct": 0,
                    "explanation": "Separation of powers divides government into three branches (executive, legislative, judicial) to prevent any one branch from becoming too powerful."
                },
                {
                    "question": "What is culture?",
                    "options": ["Only food and music", "Shared beliefs and customs", "Government rules", "Economic system"],
                    "correct": 1,
                    "explanation": "Culture includes all the shared beliefs, customs, arts, and ways of life that characterize a group of people."
                },
                {
                    "question": "What is supply and demand?",
                    "options": ["Government control", "Market forces", "Cultural practice", "Legal system"],
                    "correct": 1,
                    "explanation": "Supply and demand are market forces where supply is how much is available and demand is how much people want. They determine prices."
                }
            ]
        }

    def create_main_view(self):
        return ft.Container(
            ft.Column([
                ft.Text("👥 Social Studies", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900, text_align=ft.TextAlign.CENTER),
                ft.Text("Explore society, government, culture, and how people live together", size=16, color=ft.Colors.BLUE_700, text_align=ft.TextAlign.CENTER),
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
                                ft.Icon(ft.Icons.FORUM, size=30, color=ft.Colors.ORANGE_700),
                                ft.Text("Discussion", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_discussions(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.ORANGE_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                ], spacing=10, run_spacing=10),
                
                ft.Divider(height=20),
                
                # Topic Navigation
                ft.Container(
                    ft.Column([
                        ft.Text("📖 Social Studies Topics", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                        ft.Text("Explore specific areas of social studies", size=14, color=ft.Colors.BLUE_700),
                        ft.Divider(height=10),
                        
                        ft.ResponsiveRow([
                            ft.Container(
                                ft.ElevatedButton(
                                    content=ft.Column([
                                        ft.Icon(ft.Icons.ACCOUNT_BALANCE, size=35, color=ft.Colors.BLUE_700),
                                        ft.Text("Civics & Government", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                                        ft.Text("Learn about democracy, citizenship, and government systems", size=12, color=ft.Colors.BLUE_600, text_align=ft.TextAlign.CENTER)
                                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=8),
                                    on_click=lambda e: self.page.go("/civics"),
                                    style=ft.ButtonStyle(
                                        padding=20,
                                        bgcolor=ft.Colors.BLUE_50,
                                        shape=ft.RoundedRectangleBorder(radius=12)
                                    )
                                ),
                                col={'xs': 12, 'sm': 6, 'md': 4}
                            ),
                            ft.Container(
                                ft.ElevatedButton(
                                    content=ft.Column([
                                        ft.Icon(ft.Icons.TRENDING_UP, size=35, color=ft.Colors.GREEN_700),
                                        ft.Text("Economics", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                                        ft.Text("Understand money, markets, and economic systems", size=12, color=ft.Colors.GREEN_600, text_align=ft.TextAlign.CENTER)
                                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=8),
                                    on_click=lambda e: self.page.go("/economics"),
                                    style=ft.ButtonStyle(
                                        padding=20,
                                        bgcolor=ft.Colors.GREEN_50,
                                        shape=ft.RoundedRectangleBorder(radius=12)
                                    )
                                ),
                                col={'xs': 12, 'sm': 6, 'md': 4}
                            ),
                            ft.Container(
                                ft.ElevatedButton(
                                    content=ft.Column([
                                        ft.Icon(ft.Icons.GROUPS, size=35, color=ft.Colors.PURPLE_700),
                                        ft.Text("Culture & Society", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                                        ft.Text("Explore cultural diversity and social structures", size=12, color=ft.Colors.PURPLE_600, text_align=ft.TextAlign.CENTER)
                                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=8),
                                    on_click=lambda e: self.page.go("/culture"),
                                    style=ft.ButtonStyle(
                                        padding=20,
                                        bgcolor=ft.Colors.PURPLE_50,
                                        shape=ft.RoundedRectangleBorder(radius=12)
                                    )
                                ),
                                col={'xs': 12, 'sm': 6, 'md': 4}
                            ),
                        ], spacing=15, run_spacing=15),
                    ], spacing=15),
                    bgcolor=ft.Colors.AMBER_50,
                    border_radius=12,
                    padding=20,
                    border=ft.border.all(2, ft.Colors.AMBER_300),
                    margin=ft.margin.only(bottom=20)
                ),
                
                ft.Divider(height=20),
                
                # Quick overview
                ft.Container(
                    ft.Column([
                        ft.Text("📚 Social Studies Overview", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800),
                        ft.Text("Social Studies helps us understand how people live together in communities and societies.", size=14),
                        ft.Text("🏛️ Key Topics:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
                        ft.Column([
                            ft.Text("• Government and Democracy", size=14),
                            ft.Text("• Citizenship and Rights", size=14),
                            ft.Text("• Culture and Society", size=14),
                            ft.Text("• Economics and Geography", size=14),
                        ], spacing=5)
                    ], spacing=10),
                    bgcolor=ft.Colors.BLUE_50,
                    border_radius=10,
                    padding=15,
                    border=ft.border.all(2, ft.Colors.BLUE_200)
                )
            ], spacing=20),
            padding=20,
            expand=True
        )

    def show_ai_help(self):
        self.page.views.clear()
        
        query_field = ft.TextField(
            label="Ask about social studies...",
            hint_text="e.g., What is democracy?",
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
            "/social_studies/ai_help",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/social_studies")),
                    title=ft.Text("AI Social Studies Help"),
                    bgcolor=ft.Colors.BLUE_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("🤖 AI Social Studies Assistant", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                        query_field,
                        ft.ElevatedButton(
                            "Get Help",
                            on_click=handle_query,
                            style=ft.ButtonStyle(bgcolor=ft.Colors.BLUE_600, color=ft.Colors.WHITE)
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
            "/social_studies/quizzes",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/social_studies")),
                    title=ft.Text("Social Studies Quizzes"),
                    bgcolor=ft.Colors.BLUE_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("📝 Choose Quiz Level", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                        
                        ft.ResponsiveRow([
                            ft.Container(
                                ft.ElevatedButton(
                                    content=ft.Column([
                                        ft.Icon(ft.Icons.LOOKS_ONE, size=30, color=ft.Colors.GREEN_700),
                                        ft.Text("Basic", size=16, weight=ft.FontWeight.BOLD),
                                        ft.Text("Government & citizenship", size=12)
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
                                        ft.Text("Culture & economics", size=12)
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
            "/social_studies/quiz_question",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/social_studies/quizzes")),
                    title=ft.Text(f"Quiz - Question {self.quiz_question_index + 1}"),
                    bgcolor=ft.Colors.BLUE_700
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
            "/social_studies/quiz_explanation",
            [
                ft.AppBar(
                    title=ft.Text("Answer Explanation"),
                    bgcolor=ft.Colors.BLUE_700
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
                            style=ft.ButtonStyle(bgcolor=ft.Colors.BLUE_600, color=ft.Colors.WHITE)
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
            "/social_studies/quiz_results",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/social_studies")),
                    title=ft.Text("Quiz Results"),
                    bgcolor=ft.Colors.BLUE_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("Quiz Complete!", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                        ft.Text(f"Score: {self.quiz_score}/{total_questions} ({percentage:.0f}%)", size=20),
                        ft.Text(message, size=18, color=color, weight=ft.FontWeight.BOLD),
                        ft.ElevatedButton(
                            "Try Again",
                            on_click=lambda e: self.start_quiz(self.current_quiz_level),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.BLUE_600, color=ft.Colors.WHITE)
                        ),
                        ft.ElevatedButton(
                            "Back to Social Studies",
                            on_click=lambda e: self.page.go("/social_studies")
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
                "title": "🏛️ Government and Democracy",
                "content": "Government is how societies organize and make decisions. Key concepts:\n\n• **Democracy**: Rule by the people through elections\n• **Branches**: Executive (president), Legislative (congress), Judicial (courts)\n• **Separation of Powers**: Each branch has different roles to prevent abuse\n• **Constitution**: Supreme law that outlines government structure\n\n**Rights**: Freedom of speech, religion, press, assembly\n**Responsibilities**: Voting, following laws, serving on juries"
            },
            {
                "title": "🏆 Citizenship and Rights",
                "content": "Citizenship involves both rights and responsibilities:\n\n• **Rights**: Freedoms protected by law (speech, religion, fair trial)\n• **Responsibilities**: Duties citizens must fulfill (taxes, jury duty, voting)\n• **Civic Participation**: Voting, volunteering, staying informed\n• **Rule of Law**: Everyone is subject to the same laws\n\n**Good Citizenship**: Being informed, participating in democracy, respecting others' rights, contributing to community"
            },
            {
                "title": "🌍 Culture and Society",
                "content": "Culture shapes how people live together:\n\n• **Culture**: Shared beliefs, customs, arts, and ways of life\n• **Diversity**: Different cultures enrich society\n• **Traditions**: Practices passed down through generations\n• **Values**: Principles that guide behavior\n\n**Social Institutions**: Family, school, religion, government work together to organize society and meet people's needs"
            },
            {
                "title": "💰 Economics and Geography",
                "content": "How people use resources and organize space:\n\n• **Economics**: Study of how people meet needs and wants\n• **Supply and Demand**: Forces that determine prices\n• **Resources**: Natural, human, and capital resources\n• **Geography**: Where people live and why\n\n**Economic Systems**: Market (free enterprise), Command (government control), Mixed (combination of both)"
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
                        bgcolor=ft.Colors.BLUE_50,
                        border_radius=8
                    )
                ]
            )
            explanation_cards.append(card)
        
        view = ft.View(
            "/social_studies/explanations",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/social_studies")),
                    title=ft.Text("Social Studies Concepts"),
                    bgcolor=ft.Colors.BLUE_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("📚 Learn Social Studies", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                        ft.Text("Explore the fundamental concepts of social studies", size=16, color=ft.Colors.BLUE_700),
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

    def show_discussions(self):
        self.page.views.clear()
        
        discussion_topics = [
            "What makes a government fair?",
            "How can young people be good citizens?",
            "Why is cultural diversity important?",
            "What are the most important rights?",
            "How do communities solve problems together?"
        ]
        
        topic_cards = []
        for topic in discussion_topics:
            card = ft.Container(
                ft.Column([
                    ft.Text(topic, size=16, weight=ft.FontWeight.BOLD),
                    ft.Text("Click to explore this topic", size=12, color=ft.Colors.GREY_600),
                    ft.ElevatedButton(
                        "Discuss",
                        on_click=lambda e, t=topic: self.start_discussion(t),
                        style=ft.ButtonStyle(bgcolor=ft.Colors.ORANGE_600, color=ft.Colors.WHITE)
                    )
                ], spacing=10),
                bgcolor=ft.Colors.ORANGE_50,
                border_radius=10,
                padding=15,
                border=ft.border.all(1, ft.Colors.ORANGE_200)
            )
            topic_cards.append(card)
        
        view = ft.View(
            "/social_studies/discussions",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/social_studies")),
                    title=ft.Text("Discussion Topics"),
                    bgcolor=ft.Colors.BLUE_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("💬 Discussion Topics", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                        ft.Text("Choose a topic to explore and discuss", size=16, color=ft.Colors.BLUE_700),
                        ft.Column(topic_cards, spacing=15)
                    ], spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def start_discussion(self, topic):
        self.page.show_snack_bar(
            ft.SnackBar(content=ft.Text(f"Discussion about '{topic}' will be available soon!"))
        )

def social_studies_page(page: ft.Page):
    page.title = "Social Studies - Student AI Assistance"
    page.scroll = ft.ScrollMode.AUTO
    
    # Clear page content first
    page.clean()
    
    page.appbar = ft.AppBar(
        leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: page.go("/")),
        title=ft.Text("Social Studies"),
        bgcolor=ft.Colors.BLUE_700,
        center_title=True
    )
    
    module = SocialStudiesModule(page)
    page.add(module.create_main_view())
