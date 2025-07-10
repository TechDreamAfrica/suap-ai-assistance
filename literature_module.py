import flet as ft
import random

def get_ai_help(query, topic="literature"):
    """AI help response for Literature"""
    try:
        responses = {
            "poetry": "Poetry uses rhythm, rhyme, and imagery to express emotions and ideas. Types include sonnets, haikus, free verse, and ballads. Poetic devices include metaphor, simile, alliteration, and symbolism. Poetry often explores themes of love, nature, death, and human experience.",
            "novel": "A novel is a long fictional narrative that explores characters, plot, setting, and themes in depth. Elements include protagonist/antagonist, conflict, climax, and resolution. Novels can be classified by genre: romance, mystery, science fiction, historical fiction, etc.",
            "drama": "Drama is literature written for performance. It includes dialogue, stage directions, and character development. Types include tragedy (sad ending), comedy (happy ending), and history plays. Famous dramatists include Shakespeare, Sophocles, and modern playwrights.",
            "themes": "Literary themes are central ideas or messages in a work. Common themes include coming of age, good vs. evil, love and loss, social justice, and the human condition. Authors use characters, plot, and symbolism to develop themes.",
            "characters": "Character development shows how people in stories grow and change. Types include protagonist (main character), antagonist (opposing force), round characters (complex), and flat characters (simple). Character analysis examines motivations, conflicts, and relationships.",
            "symbolism": "Symbolism uses objects, colors, or actions to represent deeper meanings. Examples: dove for peace, red for passion/danger, seasons for life cycles. Authors use symbols to add layers of meaning and connect to universal human experiences.",
            "writing": "Creative writing includes fiction, poetry, and drama. Elements include voice, style, point of view, and literary devices. The writing process involves brainstorming, drafting, revising, and editing. Good writing shows rather than tells.",
            "analysis": "Literary analysis examines how authors create meaning through literary elements. This includes studying character development, themes, symbolism, setting, and style. Critical thinking skills help readers understand deeper meanings and author's purpose."
        }
        
        query_lower = query.lower()
        for key, response in responses.items():
            if key in query_lower:
                return f"🤖 AI Helper: {response}"
        
        return "🤖 AI Helper: Literature explores human experiences through poetry, novels, drama, and other written works. Ask about poetry, novels, drama, themes, characters, symbolism, writing, or analysis for specific help!"
    except Exception:
        return "🤖 AI Helper: I'm here to help with literature! Try asking about poetry, novels, drama, or literary analysis."

class LiteratureModule:
    def __init__(self, page):
        self.page = page
        self.current_quiz_level = "basic"
        self.quiz_score = 0
        self.quiz_question_index = 0
        
        # Quiz questions
        self.quiz_questions = {
            "basic": [
                {
                    "question": "What is the main character in a story called?",
                    "options": ["Antagonist", "Protagonist", "Narrator", "Author"],
                    "correct": 1,
                    "explanation": "The protagonist is the main character in a story, often the hero or central figure around whom the plot revolves."
                },
                {
                    "question": "What is a metaphor?",
                    "options": ["A comparison using 'like' or 'as'", "A direct comparison without 'like' or 'as'", "A sound device", "A type of rhyme"],
                    "correct": 1,
                    "explanation": "A metaphor is a direct comparison between two unlike things without using 'like' or 'as'. For example: 'Life is a journey.'"
                },
                {
                    "question": "What is the central message of a literary work called?",
                    "options": ["Plot", "Setting", "Theme", "Character"],
                    "correct": 2,
                    "explanation": "The theme is the central message, lesson, or meaning that the author wants to convey through the literary work."
                }
            ],
            "intermediate": [
                {
                    "question": "What is the difference between a simile and a metaphor?",
                    "options": ["No difference", "Simile uses 'like' or 'as'", "Metaphor is longer", "Simile is about people only"],
                    "correct": 1,
                    "explanation": "A simile compares two things using 'like' or 'as' ('brave as a lion'), while a metaphor makes a direct comparison ('he is a lion')."
                },
                {
                    "question": "What is dramatic irony?",
                    "options": ["When the author is being sarcastic", "When readers know something characters don't", "When a character is dramatic", "When the ending is sad"],
                    "correct": 1,
                    "explanation": "Dramatic irony occurs when readers or audience know something that the characters in the story do not know."
                },
                {
                    "question": "What is a sonnet?",
                    "options": ["A type of novel", "A 14-line poem", "A short story", "A type of drama"],
                    "correct": 1,
                    "explanation": "A sonnet is a 14-line poem, typically written in iambic pentameter, often exploring themes of love or beauty."
                }
            ]
        }

    def create_main_view(self):
        return ft.Container(
            ft.Column([
                ft.Text("📚 Literature", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.BROWN_900, text_align=ft.TextAlign.CENTER),
                ft.Text("Analyze literary works, poetry, and creative writing techniques", size=16, color=ft.Colors.BROWN_700, text_align=ft.TextAlign.CENTER),
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
                                ft.Icon(ft.Icons.CREATE, size=30, color=ft.Colors.ORANGE_700),
                                ft.Text("Writing", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_writing_tools(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.ORANGE_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                ], spacing=10, run_spacing=10),
                
                ft.Divider(height=20),
                
                # Quick overview
                ft.Container(
                    ft.Column([
                        ft.Text("📚 Literature Overview", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BROWN_800),
                        ft.Text("Literature explores human experiences through written works and helps us understand different perspectives.", size=14),
                        ft.Text("✍️ Key Topics:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BROWN_700),
                        ft.Column([
                            ft.Text("• Poetry and Literary Devices", size=14),
                            ft.Text("• Novels and Short Stories", size=14),
                            ft.Text("• Drama and Theater", size=14),
                            ft.Text("• Literary Analysis and Writing", size=14),
                        ], spacing=5)
                    ], spacing=10),
                    bgcolor=ft.Colors.BROWN_50,
                    border_radius=10,
                    padding=15,
                    border=ft.border.all(2, ft.Colors.BROWN_200)
                )
            ], spacing=20),
            padding=20,
            expand=True
        )

    def show_ai_help(self):
        self.page.views.clear()
        
        query_field = ft.TextField(
            label="Ask about literature...",
            hint_text="e.g., What is symbolism in literature?",
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
            "/literature/ai_help",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/literature")),
                    title=ft.Text("AI Literature Help"),
                    bgcolor=ft.Colors.BROWN_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("🤖 AI Literature Assistant", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BROWN_900),
                        query_field,
                        ft.ElevatedButton(
                            "Get Help",
                            on_click=handle_query,
                            style=ft.ButtonStyle(bgcolor=ft.Colors.BROWN_600, color=ft.Colors.WHITE)
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
            "/literature/quizzes",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/literature")),
                    title=ft.Text("Literature Quizzes"),
                    bgcolor=ft.Colors.BROWN_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("📝 Choose Quiz Level", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BROWN_900),
                        
                        ft.ResponsiveRow([
                            ft.Container(
                                ft.ElevatedButton(
                                    content=ft.Column([
                                        ft.Icon(ft.Icons.LOOKS_ONE, size=30, color=ft.Colors.GREEN_700),
                                        ft.Text("Basic", size=16, weight=ft.FontWeight.BOLD),
                                        ft.Text("Literary terms", size=12)
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
                                        ft.Text("Literary analysis", size=12)
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
            "/literature/quiz_question",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/literature/quizzes")),
                    title=ft.Text(f"Quiz - Question {self.quiz_question_index + 1}"),
                    bgcolor=ft.Colors.BROWN_700
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
            "/literature/quiz_explanation",
            [
                ft.AppBar(
                    title=ft.Text("Answer Explanation"),
                    bgcolor=ft.Colors.BROWN_700
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
                            style=ft.ButtonStyle(bgcolor=ft.Colors.BROWN_600, color=ft.Colors.WHITE)
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
            "/literature/quiz_results",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/literature")),
                    title=ft.Text("Quiz Results"),
                    bgcolor=ft.Colors.BROWN_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("Quiz Complete!", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.BROWN_900),
                        ft.Text(f"Score: {self.quiz_score}/{total_questions} ({percentage:.0f}%)", size=20),
                        ft.Text(message, size=18, color=color, weight=ft.FontWeight.BOLD),
                        ft.ElevatedButton(
                            "Try Again",
                            on_click=lambda e: self.start_quiz(self.current_quiz_level),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.BROWN_600, color=ft.Colors.WHITE)
                        ),
                        ft.ElevatedButton(
                            "Back to Literature",
                            on_click=lambda e: self.page.go("/literature")
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
                "title": "📝 Literary Elements",
                "content": "Basic building blocks of literature:\n\n• **Character**: People in the story (protagonist, antagonist)\n• **Plot**: Sequence of events (exposition, rising action, climax, resolution)\n• **Setting**: Time and place where story occurs\n• **Theme**: Central message or meaning\n• **Point of View**: Who tells the story (first person, third person)\n\n**Conflict**: Internal (within character) or external (character vs. outside force)"
            },
            {
                "title": "🎭 Literary Devices",
                "content": "Tools authors use to enhance writing:\n\n• **Metaphor**: Direct comparison ('Life is a journey')\n• **Simile**: Comparison using 'like' or 'as' ('brave as a lion')\n• **Symbolism**: Objects representing deeper meanings\n• **Irony**: Contrast between expectation and reality\n• **Foreshadowing**: Hints about future events\n\n**Imagery**: Descriptive language appealing to the senses"
            },
            {
                "title": "📖 Literary Genres",
                "content": "Different types of literature:\n\n• **Fiction**: Made-up stories (novels, short stories)\n• **Non-fiction**: True stories (biographies, essays)\n• **Poetry**: Verse with rhythm, rhyme, imagery\n• **Drama**: Plays written for performance\n\n**Sub-genres**: Mystery, romance, science fiction, fantasy, historical fiction, horror"
            },
            {
                "title": "✍️ Writing Techniques",
                "content": "Skills for effective writing:\n\n• **Voice**: Author's unique style and personality\n• **Tone**: Attitude toward subject (serious, humorous, sad)\n• **Style**: How author uses language (formal, informal)\n• **Structure**: How text is organized\n\n**Writing Process**: Brainstorm → Draft → Revise → Edit → Publish"
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
                        bgcolor=ft.Colors.BROWN_50,
                        border_radius=8
                    )
                ]
            )
            explanation_cards.append(card)
        
        view = ft.View(
            "/literature/explanations",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/literature")),
                    title=ft.Text("Literature Concepts"),
                    bgcolor=ft.Colors.BROWN_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("📚 Learn Literature", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BROWN_900),
                        ft.Text("Explore the fundamental concepts of literature", size=16, color=ft.Colors.BROWN_700),
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

    def show_writing_tools(self):
        self.page.views.clear()
        
        writing_tools = [
            {
                "title": "✍️ Story Starter",
                "description": "Get creative prompts to start your writing",
                "action": "Generate Prompt"
            },
            {
                "title": "📝 Poetry Workshop",
                "description": "Learn different poetry forms and techniques",
                "action": "Start Writing"
            },
            {
                "title": "🔍 Character Builder",
                "description": "Develop complex, interesting characters",
                "action": "Create Character"
            },
            {
                "title": "📚 Literary Analysis Helper",
                "description": "Guide for analyzing literary works",
                "action": "Start Analysis"
            }
        ]
        
        tool_cards = []
        for tool in writing_tools:
            card = ft.Container(
                ft.Column([
                    ft.Text(tool["title"], size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BROWN_900),
                    ft.Text(tool["description"], size=14, color=ft.Colors.BROWN_700),
                    ft.ElevatedButton(
                        tool["action"],
                        on_click=lambda e, title=tool["title"]: self.start_writing_tool(title),
                        style=ft.ButtonStyle(bgcolor=ft.Colors.BROWN_600, color=ft.Colors.WHITE)
                    )
                ], spacing=10),
                bgcolor=ft.Colors.BROWN_50,
                border_radius=10,
                padding=15,
                border=ft.border.all(1, ft.Colors.BROWN_200)
            )
            tool_cards.append(card)
        
        view = ft.View(
            "/literature/writing_tools",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/literature")),
                    title=ft.Text("Writing Tools"),
                    bgcolor=ft.Colors.BROWN_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("✍️ Creative Writing Tools", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BROWN_900),
                        ft.Text("Tools to help with your creative writing", size=16, color=ft.Colors.BROWN_700),
                        ft.Column(tool_cards, spacing=15)
                    ], spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def start_writing_tool(self, tool_title):
        self.page.show_snack_bar(
            ft.SnackBar(content=ft.Text(f"Writing tool '{tool_title}' will be available soon!"))
        )

def literature_page(page: ft.Page):
    page.title = "Literature - Student AI Assistance"
    page.scroll = ft.ScrollMode.AUTO
    
    # Clear page content first
    page.clean()
    
    page.appbar = ft.AppBar(
        leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: page.go("/")),
        title=ft.Text("Literature"),
        bgcolor=ft.Colors.BROWN_700,
        center_title=True
    )
    
    module = LiteratureModule(page)
    page.add(module.create_main_view())