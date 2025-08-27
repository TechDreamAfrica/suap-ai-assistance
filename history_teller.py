import flet as ft
import time
import random

class HistoryDatabase:
    """Simple database of historical information"""
    
    def __init__(self):
        self.periods = {
            "Ancient Civilizations": {
                "icon": ft.Icons.ACCOUNT_BALANCE,
                "color": ft.Colors.BROWN_700,
                "description": "Explore the cradle of human civilization",
                "topics": [
                    {
                        "title": "Ancient Egypt",
                        "content": "Ancient Egypt flourished along the Nile River for over 3,000 years. Known for pyramids, pharaohs, and hieroglyphics. The Great Pyramid of Giza is one of the Seven Wonders of the Ancient World.",
                        "key_facts": ["Pyramid construction began around 2580 BC", "Hieroglyphics were decoded using the Rosetta Stone", "Pharaohs were considered living gods"]
                    },
                    {
                        "title": "Ancient Greece",
                        "content": "Birthplace of democracy, philosophy, and the Olympic Games. Greek city-states like Athens and Sparta developed unique forms of government and culture.",
                        "key_facts": ["Athens developed the first democracy around 508 BC", "Olympic Games started in 776 BC", "Great philosophers: Socrates, Plato, Aristotle"]
                    },
                    {
                        "title": "Roman Empire",
                        "content": "One of history's largest empires, spanning from Britain to North Africa. Known for engineering, law, and military organization.",
                        "key_facts": ["Roman roads totaled over 250,000 miles", "The Colosseum could hold 50,000 spectators", "Roman law influences modern legal systems"]
                    }
                ]
            },
            "African History": {
                "icon": ft.Icons.TERRAIN,
                "color": ft.Colors.GREEN_700,
                "description": "Rich heritage of African kingdoms and civilizations",
                "topics": [
                    {
                        "title": "Kingdom of Kush",
                        "content": "Ancient African kingdom that ruled over Egypt for nearly a century. Located in present-day Sudan, known for iron production and trade.",
                        "key_facts": ["Ruled Egypt from 744-656 BC", "Built more pyramids than Egypt", "Master ironworkers and archers"]
                    },
                    {
                        "title": "Mali Empire",
                        "content": "West African empire famous for its wealth in gold and salt. Mansa Musa was one of the richest people in history.",
                        "key_facts": ["Peaked in the 13th-14th centuries", "Mansa Musa's pilgrimage to Mecca showcased immense wealth", "Timbuktu was a center of learning"]
                    },
                    {
                        "title": "Great Zimbabwe",
                        "content": "Medieval African city and trade center in present-day Zimbabwe. Known for its impressive stone architecture.",
                        "key_facts": ["Built between 1100-1450 CE", "Traded gold and ivory with Asia", "Name means 'stone houses' in Shona language"]
                    }
                ]
            },
            "Medieval Period": {
                "icon": ft.Icons.CASTLE,
                "color": ft.Colors.PURPLE_700,
                "description": "The age of knights, castles, and feudalism",
                "topics": [
                    {
                        "title": "Feudal System",
                        "content": "Social system based on land ownership and personal loyalty. Lords granted land to vassals in exchange for military service.",
                        "key_facts": ["Dominated Europe from 9th-15th centuries", "Based on mutual obligations", "Peasants worked the land for protection"]
                    },
                    {
                        "title": "The Crusades",
                        "content": "Series of religious wars between Christians and Muslims for control of holy sites in the Middle East.",
                        "key_facts": ["Lasted from 1095-1291", "Led to increased trade between East and West", "Introduced new technologies to Europe"]
                    },
                    {
                        "title": "Black Death",
                        "content": "Devastating pandemic that killed 30-60% of Europe's population in the 14th century.",
                        "key_facts": ["Peaked between 1347-1351", "Spread via trade routes", "Led to major social and economic changes"]
                    }
                ]
            },
            "Modern History": {
                "icon": ft.Icons.FACTORY,
                "color": ft.Colors.ORANGE_700,
                "description": "Industrial revolution to contemporary times",
                "topics": [
                    {
                        "title": "Industrial Revolution",
                        "content": "Period of major industrialization and innovation, starting in Britain in the late 18th century.",
                        "key_facts": ["Steam engine revolutionized transportation", "Factory system changed how goods were produced", "Led to urbanization and social changes"]
                    },
                    {
                        "title": "World War I",
                        "content": "Global conflict from 1914-1918 involving major world powers. Known as 'The Great War'.",
                        "key_facts": ["Triggered by assassination of Archduke Franz Ferdinand", "First war to use modern technology extensively", "Led to fall of several empires"]
                    },
                    {
                        "title": "World War II",
                        "content": "Global war from 1939-1945 between Axis and Allied powers. Most destructive conflict in human history.",
                        "key_facts": ["Involved over 30 countries", "Holocaust killed 6 million Jews", "Ended with atomic bombs on Japan"]
                    }
                ]
            }
        }
        
        # AI responses for different types of questions
        self.ai_responses = {
            "greetings": [
                "Hello! I'm your AI history tutor. I'm excited to explore the past with you!",
                "Greetings, time traveler! What historical adventure shall we embark on today?",
                "Welcome! I'm here to make history come alive. What fascinates you about the past?"
            ],
            "africa": [
                "Africa has incredibly rich history! Ancient kingdoms like Kush, Mali, and Songhai were centers of learning and trade.",
                "African civilizations were highly advanced - the Kingdom of Aksum was trading with Rome and India over 1,500 years ago!",
                "Did you know that Timbuktu in Mali was home to one of the world's first universities? It had over 25,000 students!"
            ],
            "egypt": [
                "Ancient Egypt is fascinating! The pyramids were built over 4,500 years ago using incredibly sophisticated techniques.",
                "Egyptian pharaohs were mummified to preserve their bodies for the afterlife. The process took 70 days!",
                "Cleopatra lived closer in time to the moon landing (1969) than to the construction of the Great Pyramid!"
            ],
            "war": [
                "Wars have shaped human history, though they've brought both innovation and destruction.",
                "Many modern technologies originated from wartime needs - the internet, GPS, and even duct tape!",
                "The longest war in history was the Reconquista in Spain, lasting 781 years (711-1492)."
            ],
            "general": [
                "History is full of surprising connections! What specific period or event interests you most?",
                "Every historical event has multiple perspectives. It's important to consider different viewpoints!",
                "The past influences our present in ways we might not even realize. What would you like to explore?"
            ]
        }

    def get_period_info(self, period_name):
        return self.periods.get(period_name, None)
    
    def generate_ai_response(self, question):
        """Generate AI-like response based on question keywords"""
        question_lower = question.lower()
        
        if any(word in question_lower for word in ["hello", "hi", "hey", "greetings"]):
            return random.choice(self.ai_responses["greetings"])
        elif any(word in question_lower for word in ["africa", "african", "mali", "egypt", "kush", "zimbabwe"]):
            return random.choice(self.ai_responses["africa"])
        elif any(word in question_lower for word in ["egypt", "pyramid", "pharaoh", "nile", "cleopatra"]):
            return random.choice(self.ai_responses["egypt"])
        elif any(word in question_lower for word in ["war", "battle", "fight", "conflict", "crusade"]):
            return random.choice(self.ai_responses["war"])
        else:
            return random.choice(self.ai_responses["general"])

def history_page(page: ft.Page):
    page.title = "History Teller - Student AI Assistance"
    page.scroll = ft.ScrollMode.AUTO
    
    # Initialize history database
    history_db = HistoryDatabase()
    
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

    # Question input field
    question_field = ft.TextField(
        label="What historical topic interests you?",
        multiline=True,
        min_lines=3,
        max_lines=5,
        border_color=ft.Colors.BLUE_300,
        value=""
    )
    
    # Response area
    ai_response_area = ft.Container(
        ft.Column([
            ft.Text("💡 AI History Tutor Response:", size=16, weight=ft.FontWeight.BOLD),
            ft.Text("Ask me anything about history!", size=14, color=ft.Colors.GREY_600)
        ]),
        bgcolor=ft.Colors.BLUE_50,
        border_radius=8,
        padding=15,
        visible=False
    )

    def show_period_details(period_name):
        """Show detailed information about a historical period"""
        period_info = history_db.get_period_info(period_name)
        if not period_info:
            return
        
        # Create content for the dialog
        topics_content = []
        for topic in period_info["topics"]:
            topic_card = ft.Container(
                ft.Column([
                    ft.Text(topic["title"], size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                    ft.Text(topic["content"], size=14),
                    ft.Text("Key Facts:", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
                    ft.Column([
                        ft.Text(f"• {fact}", size=12) for fact in topic["key_facts"]
                    ])
                ]),
                bgcolor=ft.Colors.WHITE,
                border_radius=8,
                padding=15,
                margin=ft.margin.only(bottom=10),
                border=ft.border.all(1, ft.Colors.BLUE_200)
            )
            topics_content.append(topic_card)
        
        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Row([
                ft.Icon(period_info["icon"], color=period_info["color"], size=30),
                ft.Text(period_name, size=20, weight=ft.FontWeight.BOLD)
            ]),
            content=ft.Container(
                ft.Column([
                    ft.Text(period_info["description"], size=16, weight=ft.FontWeight.W_500, color=ft.Colors.BLUE_700),
                    ft.Divider(),
                    ft.Column(topics_content, scroll=ft.ScrollMode.AUTO)
                ], scroll=ft.ScrollMode.AUTO),
                width=600,
                height=400
            ),
            actions=[
                ft.TextButton("Close", on_click=lambda e: close_dialog())
            ]
        )
        
        def close_dialog():
            dialog.open = False
            page.update()
        
        page.dialog = dialog
        dialog.open = True
        page.update()

    def handle_ai_question(e):
        """Handle AI tutor questions"""
        question = question_field.value.strip()
        if not question:
            page.show_snack_bar(
                ft.SnackBar(content=ft.Text("Please enter a question first!"))
            )
            return
        
        # Show loading state
        ai_response_area.content = ft.Column([
            ft.Text("💡 AI History Tutor Response:", size=16, weight=ft.FontWeight.BOLD),
            ft.Row([
                ft.ProgressRing(width=20, height=20),
                ft.Text("Thinking...", size=14)
            ])
        ])
        ai_response_area.visible = True
        page.update()
        
        # Simulate thinking time
        time.sleep(1)
        
        # Generate response
        response = history_db.generate_ai_response(question)
        
        # Update response area
        ai_response_area.content = ft.Column([
            ft.Text("💡 AI History Tutor Response:", size=16, weight=ft.FontWeight.BOLD),
            ft.Container(
                ft.Text(response, size=14),
                bgcolor=ft.Colors.WHITE,
                border_radius=8,
                padding=10,
                border=ft.border.all(1, ft.Colors.BLUE_200)
            ),
            ft.Text(f"Question: {question}", size=12, color=ft.Colors.GREY_600, italic=True)
        ])
        page.update()

    # Create clickable list tiles for historical periods
    def create_period_tile(period_name, period_info):
        return ft.Container(
            ft.ListTile(
                leading=ft.Icon(period_info["icon"], color=period_info["color"]),
                title=ft.Text(period_name, size=16, weight=ft.FontWeight.W_500),
                subtitle=ft.Text(period_info["description"]),
                trailing=ft.Icon(ft.Icons.ARROW_FORWARD_IOS),
                on_click=lambda e: show_period_details(period_name)
            ),
            bgcolor=ft.Colors.WHITE,
            border_radius=8,
            margin=ft.margin.only(bottom=5),
            border=ft.border.all(1, ft.Colors.BLUE_100)
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
            ft.Text("Click on any period to explore detailed information!", size=14, color=ft.Colors.BLUE_600),
            ft.Container(
                ft.Column([
                    create_period_tile(period_name, period_info) 
                    for period_name, period_info in history_db.periods.items()
                ]),
                bgcolor=ft.Colors.AMBER_50,
                border_radius=12,
                padding=10
            ),
            
            ft.Divider(height=20),
            
            # Interactive AI section
            ft.Text("Ask About History:", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
            ft.Text("Try asking: 'Tell me about ancient Egypt' or 'What was life like in medieval times?'", 
                   size=12, color=ft.Colors.GREY_600),
            question_field,
            ft.Row([
                ft.ElevatedButton(
                    "Get Historical Insights",
                    icon=ft.Icons.HISTORY_EDU,
                    style=ft.ButtonStyle(
                        color=ft.Colors.WHITE,
                        bgcolor=ft.Colors.BROWN_600,
                        shape=ft.RoundedRectangleBorder(radius=8)
                    ),
                    on_click=handle_ai_question
                ),
                ft.ElevatedButton(
                    "Clear",
                    icon=ft.Icons.CLEAR,
                    style=ft.ButtonStyle(
                        color=ft.Colors.BROWN_600,
                        bgcolor=ft.Colors.WHITE,
                        shape=ft.RoundedRectangleBorder(radius=8)
                    ),
                    on_click=lambda e: clear_response()
                )
            ], alignment=ft.MainAxisAlignment.CENTER),
            
            # AI response area
            ai_response_area,
            
            # Quick question buttons
            ft.Text("Quick Questions:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
            ft.Row([
                ft.ElevatedButton(
                    "African Kingdoms",
                    style=ft.ButtonStyle(bgcolor=ft.Colors.GREEN_100),
                    on_click=lambda e: ask_quick_question("Tell me about African kingdoms")
                ),
                ft.ElevatedButton(
                    "Ancient Egypt",
                    style=ft.ButtonStyle(bgcolor=ft.Colors.ORANGE_100),
                    on_click=lambda e: ask_quick_question("What made ancient Egypt special?")
                ),
                ft.ElevatedButton(
                    "Medieval Life",
                    style=ft.ButtonStyle(bgcolor=ft.Colors.PURPLE_100),
                    on_click=lambda e: ask_quick_question("What was life like in medieval times?")
                )
            ], alignment=ft.MainAxisAlignment.CENTER, wrap=True)
            
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15),
        padding=30,
        expand=True
    )
    
    def clear_response():
        question_field.value = ""
        ai_response_area.visible = False
        page.update()
    
    def ask_quick_question(question):
        question_field.value = question
        handle_ai_question(None)

    page.add(content)

# Example of how to use this in a main app
def main(page: ft.Page):
    page.title = "History Teller App"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    def route_change(route):
        page.views.clear()
        if page.route == "/" or page.route == "/history":
            history_page(page)
    
    page.on_route_change = route_change
    page.go("/history")

# Uncomment to run as standalone
# ft.app(target=main)