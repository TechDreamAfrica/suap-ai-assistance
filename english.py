import flet as ft
import random
import time

def get_ai_help(query, topic="english"):
    """AI help response for English learning"""
    try:
        responses = {
            "grammar": "Grammar is the system of rules that governs language structure. Key areas include parts of speech (nouns, verbs, adjectives), tenses (past, present, future), sentence structure (subject-verb-object), and punctuation. Understanding grammar helps you communicate clearly and effectively.",
            "vocabulary": "Vocabulary is your collection of known words. Effective learning strategies include: reading extensively, using context clues, learning word roots/prefixes/suffixes, practicing with flashcards, and using new words in sentences. Aim to learn 10-15 new words weekly.",
            "writing": "Good writing involves planning, drafting, revising, and editing. Key elements include clear thesis statements, logical organization, supporting evidence, smooth transitions, and proper grammar. Different writing types include narrative, descriptive, persuasive, and expository.",
            "reading": "Reading comprehension involves understanding main ideas, supporting details, author's purpose, and making inferences. Active reading strategies include previewing text, asking questions, making connections, and summarizing. Practice with various text types improves skills.",
            "pronunciation": "Pronunciation involves correct sound production, stress patterns, and intonation. Focus on problem sounds, practice with minimal pairs, use phonetic symbols, listen to native speakers, and record yourself speaking. Consistent practice improves clarity.",
            "speaking": "Speaking skills include fluency, accuracy, pronunciation, and confidence. Practice through conversations, presentations, reading aloud, and shadowing exercises. Don't fear mistakes - they're part of learning. Focus on communication over perfection.",
            "listening": "Listening comprehension requires active attention and processing. Strategies include predicting content, listening for key words, understanding context, and taking notes. Practice with various accents, speeds, and topics to improve skills.",
            "punctuation": "Punctuation marks organize writing and clarify meaning. Key marks include periods (.), commas (,), semicolons (;), colons (:), question marks (?), exclamation points (!), and apostrophes ('). Each has specific rules for usage."
        }
        
        query_lower = query.lower()
        for key, response in responses.items():
            if key in query_lower:
                return f"🤖 AI Helper: {response}"
        
        return "🤖 AI Helper: English learning covers grammar, vocabulary, writing, reading, speaking, listening, and pronunciation. Ask about any of these areas for specific help!"
    except Exception:
        return "🤖 AI Helper: I'm here to help with English learning! Try asking about grammar, vocabulary, writing, or reading skills."

class EnglishModule:
    def __init__(self, page):
        self.page = page
        self.current_quiz_level = "basic"
        self.quiz_score = 0
        self.quiz_question_index = 0
        
        # Vocabulary database
        self.vocabulary_words = {
            "basic": [
                {"word": "abundant", "definition": "existing in large quantities; plentiful", "example": "The garden had an abundant harvest this year.", "synonyms": ["plentiful", "ample", "copious"]},
                {"word": "benevolent", "definition": "well-meaning and kindly", "example": "The benevolent teacher helped struggling students after class.", "synonyms": ["kind", "generous", "charitable"]},
                {"word": "candid", "definition": "truthful and straightforward; frank", "example": "She gave a candid opinion about the project.", "synonyms": ["honest", "direct", "frank"]},
                {"word": "diligent", "definition": "showing care and effort in work", "example": "The diligent student studied every night.", "synonyms": ["hardworking", "conscientious", "thorough"]}
            ],
            "intermediate": [
                {"word": "eloquent", "definition": "fluent and persuasive in speaking or writing", "example": "The eloquent speaker moved the audience to tears.", "synonyms": ["articulate", "expressive", "persuasive"]},
                {"word": "fortuitous", "definition": "happening by chance, especially fortunately", "example": "Their meeting was fortuitous and led to a great friendship.", "synonyms": ["lucky", "fortunate", "serendipitous"]},
                {"word": "gregarious", "definition": "fond of company; sociable", "example": "Her gregarious nature made her popular at parties.", "synonyms": ["sociable", "outgoing", "friendly"]},
                {"word": "indigenous", "definition": "originating naturally in a place; native", "example": "The indigenous plants thrived in the local climate.", "synonyms": ["native", "original", "local"]}
            ]
        }
        
        # Reading passages
        self.reading_passages = {
            "beginner": {
                "title": "The Importance of Reading",
                "text": "Reading is one of the most valuable skills a person can develop. It opens doors to knowledge, entertainment, and personal growth. When we read regularly, we improve our vocabulary, enhance our writing abilities, and expand our understanding of the world. Reading also exercises our minds, improving concentration and critical thinking skills. Whether fiction or non-fiction, books transport us to different places and perspectives. In today's digital age, the ability to read and comprehend text quickly and accurately is more important than ever.",
                "questions": [
                    {
                        "question": "What is the main idea of the passage?",
                        "options": ["Reading is entertaining", "Reading is a valuable skill with many benefits", "Books are better than digital media", "Reading improves vocabulary only"],
                        "correct": 1
                    },
                    {
                        "question": "According to the passage, reading helps improve:",
                        "options": ["Only vocabulary", "Only writing", "Vocabulary, writing, and critical thinking", "Only entertainment value"],
                        "correct": 2
                    }
                ]
            },
            "intermediate": {
                "title": "Climate Change and Its Effects",
                "text": "Climate change represents one of the most pressing challenges of our time. Scientific evidence overwhelmingly indicates that human activities, particularly the emission of greenhouse gases, are driving unprecedented changes in Earth's climate system. These changes manifest in rising global temperatures, shifting precipitation patterns, and increasing frequency of extreme weather events. The consequences extend beyond environmental impacts, affecting agriculture, water resources, human health, and economic stability. Addressing climate change requires both mitigation strategies to reduce emissions and adaptation measures to cope with unavoidable changes. International cooperation, technological innovation, and individual action all play crucial roles in this global effort.",
                "questions": [
                    {
                        "question": "What is the primary cause of climate change mentioned in the passage?",
                        "options": ["Natural weather cycles", "Solar radiation changes", "Human activities and greenhouse gas emissions", "Ocean temperature variations"],
                        "correct": 2
                    },
                    {
                        "question": "The passage suggests that addressing climate change requires:",
                        "options": ["Only reducing emissions", "Only adaptation measures", "Both mitigation and adaptation strategies", "Only international cooperation"],
                        "correct": 2
                    }
                ]
            }
        }
        
        # Grammar rules and exercises
        self.grammar_topics = {
            "Present Tenses": {
                "rules": [
                    "Simple Present: I work, She works (habitual actions, facts)",
                    "Present Continuous: I am working (ongoing actions now)",
                    "Present Perfect: I have worked (completed actions with present relevance)",
                    "Present Perfect Continuous: I have been working (ongoing actions started in past)"
                ],
                "exercises": [
                    {
                        "question": "Choose the correct form: She _____ to school every day.",
                        "options": ["go", "goes", "going", "gone"],
                        "correct": 1,
                        "explanation": "Use simple present 'goes' for habitual actions with third person singular."
                    }
                ]
            },
            "Past Tenses": {
                "rules": [
                    "Simple Past: I worked (completed actions in the past)",
                    "Past Continuous: I was working (ongoing actions in the past)",
                    "Past Perfect: I had worked (actions completed before another past action)",
                    "Past Perfect Continuous: I had been working (ongoing past actions before another past action)"
                ],
                "exercises": [
                    {
                        "question": "Choose the correct form: When I arrived, they _____ dinner.",
                        "options": ["eat", "ate", "were eating", "have eaten"],
                        "correct": 2,
                        "explanation": "Use past continuous 'were eating' for ongoing action when another action occurred."
                    }
                ]
            }
        }

    def create_main_view(self):
        return ft.Container(
            ft.Column([
                ft.Text("📖 English Language Center", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900, text_align=ft.TextAlign.CENTER),
                ft.Text("Master grammar, vocabulary, reading, and writing skills", size=16, color=ft.Colors.BLUE_700, text_align=ft.TextAlign.CENTER),
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
                                ft.Icon(ft.Icons.SPELLCHECK, size=30, color=ft.Colors.GREEN_700),
                                ft.Text("Grammar", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_grammar(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.GREEN_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.LIBRARY_BOOKS, size=30, color=ft.Colors.ORANGE_700),
                                ft.Text("Vocabulary", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_vocabulary(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.ORANGE_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.CHROME_READER_MODE, size=30, color=ft.Colors.PURPLE_700),
                                ft.Text("Reading", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_reading(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.PURPLE_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                ], spacing=10, run_spacing=10),
                
                ft.ResponsiveRow([
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.EDIT, size=30, color=ft.Colors.PINK_700),
                                ft.Text("Writing", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_writing(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.PINK_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.QUIZ, size=30, color=ft.Colors.TEAL_700),
                                ft.Text("Practice Tests", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_practice_tests(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.TEAL_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.RECORD_VOICE_OVER, size=30, color=ft.Colors.INDIGO_700),
                                ft.Text("Speaking", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_speaking(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.INDIGO_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.HEADSET, size=30, color=ft.Colors.BROWN_700),
                                ft.Text("Listening", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_listening(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.BROWN_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                ], spacing=10, run_spacing=10),
                
                ft.Divider(height=20),
                
                # Quick overview
                ft.Container(
                    ft.Column([
                        ft.Text("📚 English Learning Overview", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800),
                        ft.Text("Develop comprehensive English language skills through structured learning modules.", size=14),
                        ft.Text("🎯 Core Skills:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
                        ft.Column([
                            ft.Text("• Grammar and sentence structure", size=14),
                            ft.Text("• Vocabulary building and usage", size=14),
                            ft.Text("• Reading comprehension strategies", size=14),
                            ft.Text("• Writing techniques and practice", size=14),
                            ft.Text("• Speaking and listening skills", size=14),
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
            label="Ask about English learning...",
            hint_text="e.g., How do I improve my grammar?",
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
            "/english/ai_help",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/english")),
                    title=ft.Text("AI English Assistant"),
                    bgcolor=ft.Colors.BLUE_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("🤖 AI English Learning Assistant", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
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

    def show_grammar(self):
        self.page.views.clear()
        
        grammar_cards = []
        for topic, content in self.grammar_topics.items():
            rules_text = "\n".join([f"• {rule}" for rule in content["rules"]])
            
            card = ft.ExpansionTile(
                title=ft.Text(topic, size=18, weight=ft.FontWeight.BOLD),
                subtitle=ft.Text("Click to explore grammar rules and exercises"),
                controls=[
                    ft.Container(
                        ft.Column([
                            ft.Text("Grammar Rules:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
                            ft.Text(rules_text, size=14),
                            ft.ElevatedButton(
                                "Practice Exercises",
                                on_click=lambda e, t=topic: self.start_grammar_exercise(t),
                                style=ft.ButtonStyle(bgcolor=ft.Colors.GREEN_600, color=ft.Colors.WHITE)
                            )
                        ], spacing=10),
                        padding=15,
                        bgcolor=ft.Colors.GREEN_50,
                        border_radius=8
                    )
                ]
            )
            grammar_cards.append(card)
        
        view = ft.View(
            "/english/grammar",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/english")),
                    title=ft.Text("Grammar Learning"),
                    bgcolor=ft.Colors.GREEN_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("📝 Grammar Mastery", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_900),
                        ft.Text("Learn essential grammar rules and practice with exercises", size=16, color=ft.Colors.GREEN_700),
                        ft.Column(grammar_cards, spacing=10)
                    ], spacing=15),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def start_grammar_exercise(self, topic):
        if topic in self.grammar_topics and "exercises" in self.grammar_topics[topic]:
            exercises = self.grammar_topics[topic]["exercises"]
            if exercises:
                self.show_grammar_question(topic, exercises[0], 0)
            else:
                self.page.show_snack_bar(ft.SnackBar(content=ft.Text(f"Exercises for {topic} coming soon!")))
        else:
            self.page.show_snack_bar(ft.SnackBar(content=ft.Text(f"Exercises for {topic} coming soon!")))

    def show_grammar_question(self, topic, exercise, index):
        option_buttons = []
        for i, option in enumerate(exercise["options"]):
            option_buttons.append(
                ft.ElevatedButton(
                    option,
                    on_click=lambda e, idx=i: self.answer_grammar_question(topic, exercise, idx),
                    style=ft.ButtonStyle(
                        padding=15,
                        bgcolor=ft.Colors.GREEN_50,
                        shape=ft.RoundedRectangleBorder(radius=8)
                    ),
                    expand=True
                )
            )
        
        self.page.views.clear()
        view = ft.View(
            "/english/grammar_exercise",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.show_grammar()),
                    title=ft.Text(f"Grammar: {topic}"),
                    bgcolor=ft.Colors.GREEN_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text(f"Exercise: {topic}", size=16, color=ft.Colors.GREY_600),
                        ft.Text(exercise["question"], size=18, weight=ft.FontWeight.BOLD),
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

    def answer_grammar_question(self, topic, exercise, selected_index):
        is_correct = selected_index == exercise["correct"]
        
        self.page.views.clear()
        view = ft.View(
            "/english/grammar_explanation",
            [
                ft.AppBar(
                    title=ft.Text("Answer Explanation"),
                    bgcolor=ft.Colors.GREEN_700
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
                        ft.Text(f"Correct answer: {exercise['options'][exercise['correct']]}", size=16),
                        ft.Container(
                            ft.Text(exercise["explanation"], size=14),
                            bgcolor=ft.Colors.GREEN_50,
                            border_radius=10,
                            padding=15
                        ),
                        ft.ElevatedButton(
                            "Back to Grammar",
                            on_click=lambda e: self.show_grammar(),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.GREEN_600, color=ft.Colors.WHITE)
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

    def show_vocabulary(self):
        self.page.views.clear()
        
        def show_word_details(word_data):
            dialog = ft.AlertDialog(
                modal=True,
                title=ft.Text(word_data["word"].title(), size=24, weight=ft.FontWeight.BOLD),
                content=ft.Container(
                    ft.Column([
                        ft.Text("Definition:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_700),
                        ft.Text(word_data["definition"], size=14),
                        ft.Text("Example:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_700),
                        ft.Text(word_data["example"], size=14, italic=True),
                        ft.Text("Synonyms:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_700),
                        ft.Text(", ".join(word_data["synonyms"]), size=14),
                    ], spacing=10),
                    width=400
                ),
                actions=[ft.TextButton("Close", on_click=lambda e: close_dialog())]
            )
            
            def close_dialog():
                dialog.open = False
                self.page.update()
            
            self.page.dialog = dialog
            dialog.open = True
            self.page.update()

        level_cards = []
        for level, words in self.vocabulary_words.items():
            word_buttons = []
            for word_data in words:
                word_buttons.append(
                    ft.ElevatedButton(
                        word_data["word"].title(),
                        on_click=lambda e, wd=word_data: show_word_details(wd),
                        style=ft.ButtonStyle(bgcolor=ft.Colors.ORANGE_100)
                    )
                )
            
            card = ft.Container(
                ft.Column([
                    ft.Text(f"{level.title()} Vocabulary", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_900),
                    ft.Text(f"Learn {len(words)} essential words", size=14, color=ft.Colors.ORANGE_700),
                    ft.ResponsiveRow([
                        ft.Container(button, col={'xs': 12, 'sm': 6, 'md': 3}) for button in word_buttons
                    ], spacing=10, run_spacing=10),
                    ft.ElevatedButton(
                        f"Practice {level.title()} Quiz",
                        on_click=lambda e, l=level: self.start_vocabulary_quiz(l),
                        style=ft.ButtonStyle(bgcolor=ft.Colors.ORANGE_600, color=ft.Colors.WHITE)
                    )
                ], spacing=15),
                bgcolor=ft.Colors.ORANGE_50,
                border_radius=12,
                padding=20,
                border=ft.border.all(2, ft.Colors.ORANGE_200),
                margin=ft.margin.only(bottom=15)
            )
            level_cards.append(card)
        
        view = ft.View(
            "/english/vocabulary",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/english")),
                    title=ft.Text("Vocabulary Building"),
                    bgcolor=ft.Colors.ORANGE_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("📚 Vocabulary Mastery", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_900),
                        ft.Text("Build your word power with structured vocabulary learning", size=16, color=ft.Colors.ORANGE_700),
                        ft.Column(level_cards, spacing=0)
                    ], spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def start_vocabulary_quiz(self, level):
        words = self.vocabulary_words.get(level, [])
        if not words:
            self.page.show_snack_bar(ft.SnackBar(content=ft.Text("Vocabulary quiz coming soon!")))
            return
        
        # Generate quiz questions from vocabulary
        quiz_word = random.choice(words)
        wrong_options = [w["definition"] for w in words if w != quiz_word][:3]
        options = wrong_options + [quiz_word["definition"]]
        random.shuffle(options)
        correct_index = options.index(quiz_word["definition"])
        
        option_buttons = []
        for i, option in enumerate(options):
            option_buttons.append(
                ft.ElevatedButton(
                    option,
                    on_click=lambda e, idx=i: self.answer_vocabulary_question(quiz_word, idx, correct_index),
                    style=ft.ButtonStyle(
                        padding=15,
                        bgcolor=ft.Colors.ORANGE_50,
                        shape=ft.RoundedRectangleBorder(radius=8)
                    ),
                    expand=True
                )
            )
        
        self.page.views.clear()
        view = ft.View(
            "/english/vocabulary_quiz",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.show_vocabulary()),
                    title=ft.Text(f"Vocabulary Quiz: {level.title()}"),
                    bgcolor=ft.Colors.ORANGE_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("Vocabulary Quiz", size=16, color=ft.Colors.GREY_600),
                        ft.Text(f"What does '{quiz_word['word']}' mean?", size=18, weight=ft.FontWeight.BOLD),
                        ft.Text("Choose the correct definition:", size=14, color=ft.Colors.GREY_700),
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

    def answer_vocabulary_question(self, quiz_word, selected_index, correct_index):
        is_correct = selected_index == correct_index
        
        self.page.views.clear()
        view = ft.View(
            "/english/vocabulary_answer",
            [
                ft.AppBar(
                    title=ft.Text("Answer Explanation"),
                    bgcolor=ft.Colors.ORANGE_700
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
                        ft.Text(f"Word: {quiz_word['word']}", size=18, weight=ft.FontWeight.BOLD),
                        ft.Container(
                            ft.Column([
                                ft.Text(f"Definition: {quiz_word['definition']}", size=14),
                                ft.Text(f"Example: {quiz_word['example']}", size=14, italic=True),
                                ft.Text(f"Synonyms: {', '.join(quiz_word['synonyms'])}", size=14)
                            ], spacing=8),
                            bgcolor=ft.Colors.ORANGE_50,
                            border_radius=10,
                            padding=15
                        ),
                        ft.ElevatedButton(
                            "Back to Vocabulary",
                            on_click=lambda e: self.show_vocabulary(),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.ORANGE_600, color=ft.Colors.WHITE)
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

    def show_reading(self):
        self.page.views.clear()
        
        passage_cards = []
        for level, passage_data in self.reading_passages.items():
            card = ft.Container(
                ft.Column([
                    ft.Text(f"{level.title()} Level", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_900),
                    ft.Text(passage_data["title"], size=16, weight=ft.FontWeight.W_500),
                    ft.Text(passage_data["text"][:150] + "...", size=14, color=ft.Colors.GREY_700),
                    ft.ElevatedButton(
                        "Read & Practice",
                        on_click=lambda e, l=level: self.start_reading_exercise(l),
                        style=ft.ButtonStyle(bgcolor=ft.Colors.PURPLE_600, color=ft.Colors.WHITE)
                    )
                ], spacing=10),
                bgcolor=ft.Colors.PURPLE_50,
                border_radius=12,
                padding=20,
                border=ft.border.all(2, ft.Colors.PURPLE_200),
                margin=ft.margin.only(bottom=15)
            )
            passage_cards.append(card)
        
        view = ft.View(
            "/english/reading",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/english")),
                    title=ft.Text("Reading Comprehension"),
                    bgcolor=ft.Colors.PURPLE_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("📖 Reading Comprehension", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_900),
                        ft.Text("Improve reading skills with structured passages and questions", size=16, color=ft.Colors.PURPLE_700),
                        ft.Container(
                            ft.Column([
                                ft.Text("Reading Strategies:", size=16, weight=ft.FontWeight.BOLD),
                                ft.Text("• Preview the text before reading", size=14),
                                ft.Text("• Look for main ideas and supporting details", size=14),
                                ft.Text("• Make connections to prior knowledge", size=14),
                                ft.Text("• Ask questions while reading", size=14),
                                ft.Text("• Summarize what you've read", size=14),
                            ], spacing=5),
                            bgcolor=ft.Colors.BLUE_50,
                            border_radius=8,
                            padding=15,
                            border=ft.border.all(1, ft.Colors.BLUE_200),
                            margin=ft.margin.only(bottom=20)
                        ),
                        ft.Column(passage_cards, spacing=0)
                    ], spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def start_reading_exercise(self, level):
        passage_data = self.reading_passages.get(level)
        if not passage_data:
            return
        
        self.page.views.clear()
        view = ft.View(
            "/english/reading_passage",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.show_reading()),
                    title=ft.Text("Reading Exercise"),
                    bgcolor=ft.Colors.PURPLE_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text(passage_data["title"], size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_900),
                        ft.Container(
                            ft.Text(passage_data["text"], size=14, selectable=True),
                            bgcolor=ft.Colors.WHITE,
                            border_radius=8,
                            padding=20,
                            border=ft.border.all(1, ft.Colors.PURPLE_200)
                        ),
                        ft.ElevatedButton(
                            "Answer Questions",
                            on_click=lambda e: self.show_reading_questions(level, 0),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.PURPLE_600, color=ft.Colors.WHITE)
                        )
                    ], spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def show_reading_questions(self, level, question_index):
        passage_data = self.reading_passages.get(level)
        if not passage_data or question_index >= len(passage_data["questions"]):
            return
        
        question_data = passage_data["questions"][question_index]
        option_buttons = []
        
        for i, option in enumerate(question_data["options"]):
            option_buttons.append(
                ft.ElevatedButton(
                    option,
                    on_click=lambda e, idx=i: self.answer_reading_question(level, question_index, idx),
                    style=ft.ButtonStyle(
                        padding=15,
                        bgcolor=ft.Colors.PURPLE_50,
                        shape=ft.RoundedRectangleBorder(radius=8)
                    ),
                    expand=True
                )
            )
        
        self.page.views.clear()
        view = ft.View(
            "/english/reading_question",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.start_reading_exercise(level)),
                    title=ft.Text(f"Question {question_index + 1}"),
                    bgcolor=ft.Colors.PURPLE_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text(f"Question {question_index + 1} of {len(passage_data['questions'])}", size=16, color=ft.Colors.GREY_600),
                        ft.Text(question_data["question"], size=18, weight=ft.FontWeight.BOLD),
                        ft.Text("Choose the best answer:", size=14, color=ft.Colors.GREY_700),
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

    def answer_reading_question(self, level, question_index, selected_index):
        passage_data = self.reading_passages.get(level)
        question_data = passage_data["questions"][question_index]
        is_correct = selected_index == question_data["correct"]
        
        self.page.views.clear()
        view = ft.View(
            "/english/reading_answer",
            [
                ft.AppBar(
                    title=ft.Text("Answer Result"),
                    bgcolor=ft.Colors.PURPLE_700
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
                        ft.Text(f"Correct answer: {question_data['options'][question_data['correct']]}", size=16),
                        ft.Row([
                            ft.ElevatedButton(
                                "Next Question" if question_index + 1 < len(passage_data["questions"]) else "Finish",
                                on_click=lambda e: (
                                    self.show_reading_questions(level, question_index + 1) 
                                    if question_index + 1 < len(passage_data["questions"]) 
                                    else self.show_reading()
                                ),
                                style=ft.ButtonStyle(bgcolor=ft.Colors.PURPLE_600, color=ft.Colors.WHITE)
                            ),
                            ft.ElevatedButton(
                                "Back to Reading",
                                on_click=lambda e: self.show_reading()
                            )
                        ], alignment=ft.MainAxisAlignment.CENTER, spacing=10)
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def show_writing(self):
        self.page.views.clear()
        
        writing_tools = [
            {
                "title": "Essay Structure",
                "description": "Learn to organize essays with introduction, body, and conclusion",
                "content": "A well-structured essay has:\n\n1. Introduction: Hook, background, thesis statement\n2. Body Paragraphs: Topic sentence, evidence, analysis, transition\n3. Conclusion: Restate thesis, summarize points, closing thought\n\nEach paragraph should focus on one main idea and connect logically to the next."
            },
            {
                "title": "Paragraph Development",
                "description": "Master the art of writing coherent paragraphs",
                "content": "Strong paragraphs include:\n\n• Topic sentence (main idea)\n• Supporting sentences (evidence, examples)\n• Concluding sentence (transition or summary)\n\nUse transitions like 'furthermore,' 'however,' 'in conclusion' to connect ideas."
            },
            {
                "title": "Writing Process",
                "description": "Follow a systematic approach to writing",
                "content": "The writing process:\n\n1. Prewriting: Brainstorm, outline, research\n2. Drafting: Write first draft without worrying about perfection\n3. Revising: Improve content, organization, clarity\n4. Editing: Fix grammar, spelling, punctuation\n5. Publishing: Share final version"
            }
        ]
        
        tool_cards = []
        for tool in writing_tools:
            card = ft.ExpansionTile(
                title=ft.Text(tool["title"], size=18, weight=ft.FontWeight.BOLD),
                subtitle=ft.Text(tool["description"]),
                controls=[
                    ft.Container(
                        ft.Text(tool["content"], size=14),
                        padding=15,
                        bgcolor=ft.Colors.PINK_50,
                        border_radius=8
                    )
                ]
            )
            tool_cards.append(card)
        
        # Writing practice area
        writing_practice = ft.Container(
            ft.Column([
                ft.Text("✍️ Writing Practice", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.PINK_900),
                ft.Text("Practice your writing skills with this interactive area:", size=14),
                ft.TextField(
                    label="Write your essay, paragraph, or story here...",
                    multiline=True,
                    min_lines=10,
                    max_lines=15,
                    border_color=ft.Colors.PINK_300
                ),
                ft.Row([
                    ft.ElevatedButton(
                        "Check Grammar",
                        on_click=lambda e: self.page.show_snack_bar(ft.SnackBar(content=ft.Text("Grammar checker coming soon!"))),
                        style=ft.ButtonStyle(bgcolor=ft.Colors.PINK_600, color=ft.Colors.WHITE)
                    ),
                    ft.ElevatedButton(
                        "Get Feedback",
                        on_click=lambda e: self.page.show_snack_bar(ft.SnackBar(content=ft.Text("AI feedback coming soon!"))),
                        style=ft.ButtonStyle(bgcolor=ft.Colors.PINK_600, color=ft.Colors.WHITE)
                    ),
                    ft.ElevatedButton(
                        "Clear Text",
                        on_click=lambda e: self.page.show_snack_bar(ft.SnackBar(content=ft.Text("Text cleared!")))
                    )
                ], alignment=ft.MainAxisAlignment.CENTER, spacing=10)
            ], spacing=15),
            bgcolor=ft.Colors.PINK_50,
            border_radius=12,
            padding=20,
            border=ft.border.all(2, ft.Colors.PINK_200)
        )
        
        view = ft.View(
            "/english/writing",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/english")),
                    title=ft.Text("Writing Skills"),
                    bgcolor=ft.Colors.PINK_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("✍️ Writing Mastery", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.PINK_900),
                        ft.Text("Develop strong writing skills through guided learning and practice", size=16, color=ft.Colors.PINK_700),
                        ft.Column(tool_cards, spacing=5),
                        writing_practice
                    ], spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def show_practice_tests(self):
        self.page.views.clear()
        
        test_types = [
            {
                "title": "Grammar Test",
                "description": "Test your understanding of English grammar rules",
                "icon": ft.Icons.SPELLCHECK,
                "color": ft.Colors.GREEN_700,
                "action": lambda: self.page.show_snack_bar(ft.SnackBar(content=ft.Text("Grammar test coming soon!")))
            },
            {
                "title": "Vocabulary Test",
                "description": "Challenge your knowledge of English words",
                "icon": ft.Icons.LIBRARY_BOOKS,
                "color": ft.Colors.ORANGE_700,
                "action": lambda: self.page.show_snack_bar(ft.SnackBar(content=ft.Text("Vocabulary test coming soon!")))
            },
            {
                "title": "Reading Comprehension",
                "description": "Test your reading and understanding skills",
                "icon": ft.Icons.CHROME_READER_MODE,
                "color": ft.Colors.PURPLE_700,
                "action": lambda: self.page.show_snack_bar(ft.SnackBar(content=ft.Text("Reading test coming soon!")))
            },
            {
                "title": "Writing Assessment",
                "description": "Get evaluated on your writing skills",
                "icon": ft.Icons.EDIT,
                "color": ft.Colors.PINK_700,
                "action": lambda: self.page.show_snack_bar(ft.SnackBar(content=ft.Text("Writing assessment coming soon!")))
            }
        ]
        
        test_cards = []
        for test in test_types:
            card = ft.Container(
                ft.Column([
                    ft.Icon(test["icon"], size=40, color=test["color"]),
                    ft.Text(test["title"], size=18, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                    ft.Text(test["description"], size=14, text_align=ft.TextAlign.CENTER),
                    ft.ElevatedButton(
                        "Start Test",
                        on_click=lambda e, action=test["action"]: action(),
                        style=ft.ButtonStyle(bgcolor=test["color"], color=ft.Colors.WHITE)
                    )
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15),
                bgcolor=ft.Colors.WHITE,
                border_radius=12,
                padding=20,
                border=ft.border.all(2, test["color"]),
                margin=ft.margin.only(bottom=15)
            )
            test_cards.append(card)
        
        view = ft.View(
            "/english/practice_tests",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/english")),
                    title=ft.Text("Practice Tests"),
                    bgcolor=ft.Colors.TEAL_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("📝 Practice Tests", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.TEAL_900),
                        ft.Text("Test your English skills with comprehensive assessments", size=16, color=ft.Colors.TEAL_700),
                        ft.Column(test_cards, spacing=0)
                    ], spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def show_speaking(self):
        self.page.views.clear()
        
        speaking_activities = [
            {
                "title": "Pronunciation Practice",
                "description": "Work on difficult sounds and word stress",
                "tips": [
                    "Record yourself speaking and compare to native speakers",
                    "Practice tongue twisters for difficult sounds",
                    "Focus on word stress patterns",
                    "Use phonetic symbols to understand sounds"
                ]
            },
            {
                "title": "Conversation Skills",
                "description": "Build fluency in everyday conversations",
                "tips": [
                    "Practice common conversation starters",
                    "Learn to ask follow-up questions",
                    "Practice active listening skills",
                    "Use appropriate body language and eye contact"
                ]
            },
            {
                "title": "Public Speaking",
                "description": "Develop confidence in formal speaking situations",
                "tips": [
                    "Start with short presentations on familiar topics",
                    "Practice organizing your thoughts clearly",
                    "Work on projecting your voice",
                    "Use gestures and visual aids effectively"
                ]
            }
        ]
        
        activity_cards = []
        for activity in speaking_activities:
            tips_text = "\n".join([f"• {tip}" for tip in activity["tips"]])
            
            card = ft.ExpansionTile(
                title=ft.Text(activity["title"], size=18, weight=ft.FontWeight.BOLD),
                subtitle=ft.Text(activity["description"]),
                controls=[
                    ft.Container(
                        ft.Column([
                            ft.Text("Practice Tips:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.INDIGO_700),
                            ft.Text(tips_text, size=14)
                        ], spacing=10),
                        padding=15,
                        bgcolor=ft.Colors.INDIGO_50,
                        border_radius=8
                    )
                ]
            )
            activity_cards.append(card)
        
        view = ft.View(
            "/english/speaking",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/english")),
                    title=ft.Text("Speaking Skills"),
                    bgcolor=ft.Colors.INDIGO_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("🎤 Speaking Mastery", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.INDIGO_900),
                        ft.Text("Improve your English speaking confidence and fluency", size=16, color=ft.Colors.INDIGO_700),
                        ft.Container(
                            ft.Column([
                                ft.Text("Speaking Strategies:", size=16, weight=ft.FontWeight.BOLD),
                                ft.Text("• Practice regularly, even if just talking to yourself", size=14),
                                ft.Text("• Don't worry about making mistakes - they help you learn", size=14),
                                ft.Text("• Focus on communication over perfection", size=14),
                                ft.Text("• Listen to and imitate native speakers", size=14),
                                ft.Text("• Join conversation groups or language exchanges", size=14),
                            ], spacing=5),
                            bgcolor=ft.Colors.BLUE_50,
                            border_radius=8,
                            padding=15,
                            border=ft.border.all(1, ft.Colors.BLUE_200),
                            margin=ft.margin.only(bottom=20)
                        ),
                        ft.Column(activity_cards, spacing=10)
                    ], spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def show_listening(self):
        self.page.views.clear()
        
        listening_exercises = [
            {
                "title": "Active Listening",
                "description": "Develop focused listening skills",
                "strategies": [
                    "Predict what you'll hear before listening",
                    "Listen for main ideas, not every word",
                    "Take notes on key information",
                    "Ask for clarification when needed"
                ]
            },
            {
                "title": "Different Accents",
                "description": "Understand various English accents",
                "strategies": [
                    "Expose yourself to British, American, Australian English",
                    "Watch movies and shows from different countries",
                    "Listen to international news broadcasts",
                    "Practice with online accent training tools"
                ]
            },
            {
                "title": "Listening for Detail",
                "description": "Pick up specific information from speech",
                "strategies": [
                    "Focus on numbers, dates, and names",
                    "Listen for signal words like 'first,' 'finally,' 'however'",
                    "Practice with dictation exercises",
                    "Use subtitles initially, then remove them gradually"
                ]
            }
        ]
        
        exercise_cards = []
        for exercise in listening_exercises:
            strategies_text = "\n".join([f"• {strategy}" for strategy in exercise["strategies"]])
            
            card = ft.ExpansionTile(
                title=ft.Text(exercise["title"], size=18, weight=ft.FontWeight.BOLD),
                subtitle=ft.Text(exercise["description"]),
                controls=[
                    ft.Container(
                        ft.Column([
                            ft.Text("Strategies:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BROWN_700),
                            ft.Text(strategies_text, size=14)
                        ], spacing=10),
                        padding=15,
                        bgcolor=ft.Colors.BROWN_50,
                        border_radius=8
                    )
                ]
            )
            exercise_cards.append(card)
        
        view = ft.View(
            "/english/listening",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/english")),
                    title=ft.Text("Listening Skills"),
                    bgcolor=ft.Colors.BROWN_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("🎧 Listening Mastery", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BROWN_900),
                        ft.Text("Enhance your English listening comprehension abilities", size=16, color=ft.Colors.BROWN_700),
                        ft.Container(
                            ft.Column([
                                ft.Text("Listening Resources:", size=16, weight=ft.FontWeight.BOLD),
                                ft.Text("• Podcasts for English learners", size=14),
                                ft.Text("• TED Talks with transcripts", size=14),
                                ft.Text("• English news broadcasts", size=14),
                                ft.Text("• Audiobooks at your level", size=14),
                                ft.Text("• English music and songs", size=14),
                            ], spacing=5),
                            bgcolor=ft.Colors.BLUE_50,
                            border_radius=8,
                            padding=15,
                            border=ft.border.all(1, ft.Colors.BLUE_200),
                            margin=ft.margin.only(bottom=20)
                        ),
                        ft.Column(exercise_cards, spacing=10)
                    ], spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

def english_page(page: ft.Page):
    page.title = "English - Student AI Assistance"
    page.scroll = ft.ScrollMode.AUTO
    
    # Clear page content first
    page.clean()
    
    page.appbar = ft.AppBar(
        leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: page.go("/")),
        title=ft.Text("English Learning"),
        bgcolor=ft.Colors.BLUE_700,
        center_title=True
    )
    
    module = EnglishModule(page)
    page.add(module.create_main_view())

# Additional module implementations can be added here...