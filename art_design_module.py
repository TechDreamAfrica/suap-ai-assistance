import flet as ft
import random

def get_ai_help(query, topic="art_design"):
    """AI help response for Art & Design"""
    try:
        responses = {
            "color": "Color theory involves understanding how colors work together. Primary colors (red, blue, yellow) mix to create secondary colors (green, orange, purple). Complementary colors are opposite on the color wheel and create contrast. Color can convey mood, emotion, and meaning in art.",
            "composition": "Composition is how elements are arranged in artwork. Key principles include rule of thirds, balance (symmetrical/asymmetrical), emphasis (focal point), and movement (leading the eye). Good composition creates visual harmony and guides viewer attention.",
            "drawing": "Drawing is the foundation of visual art. Basic techniques include contour lines (outlines), shading (light/shadow), perspective (3D depth), and proportion (relative sizes). Practice with different materials: pencil, charcoal, ink, and digital tools.",
            "painting": "Painting involves applying pigment to surfaces. Techniques include blending colors, layering, brushwork, and texture creation. Paint types include watercolor (transparent), acrylic (fast-drying), and oil (slow-drying). Each has unique properties and uses.",
            "design": "Design combines art with function. Elements include line, shape, form, space, texture, and color. Principles include balance, contrast, emphasis, movement, pattern, repetition, and unity. Good design is both beautiful and purposeful.",
            "sculpture": "Sculpture is three-dimensional art. Methods include carving (subtractive), modeling (additive), and casting. Materials range from traditional (stone, wood, clay) to modern (metal, plastic, found objects). Consider form, space, and viewer interaction.",
            "photography": "Photography captures light and moments. Key concepts include composition, lighting, focus, and exposure. Digital photography allows editing and manipulation. Consider subject, background, angle, and storytelling in your images.",
            "digital": "Digital art uses technology as a medium. Tools include graphics tablets, software (Photoshop, Illustrator), and apps. Techniques from traditional art apply: color, composition, perspective. Digital art enables new possibilities like animation and interactive media."
        }
        
        query_lower = query.lower()
        for key, response in responses.items():
            if key in query_lower:
                return f"🤖 AI Helper: {response}"
        
        return "🤖 AI Helper: Art & Design explores visual creativity and self-expression. Ask about color, composition, drawing, painting, design, sculpture, photography, or digital art for specific help!"
    except Exception:
        return "🤖 AI Helper: I'm here to help with art and design! Try asking about color theory, drawing techniques, or design principles."

class ArtDesignModule:
    def __init__(self, page):
        self.page = page
        self.current_quiz_level = "basic"
        self.quiz_score = 0
        self.quiz_question_index = 0
        
        # Quiz questions
        self.quiz_questions = {
            "basic": [
                {
                    "question": "What are the primary colors?",
                    "options": ["Red, Green, Blue", "Red, Blue, Yellow", "Blue, Yellow, Orange", "Red, Yellow, Green"],
                    "correct": 1,
                    "explanation": "The primary colors are red, blue, and yellow. These colors cannot be created by mixing other colors."
                },
                {
                    "question": "What is the rule of thirds in composition?",
                    "options": ["Divide image into 3 equal parts", "Use only 3 colors", "Have 3 main subjects", "Divide image into 9 sections"],
                    "correct": 3,
                    "explanation": "The rule of thirds divides an image into 9 equal sections with 2 horizontal and 2 vertical lines. Placing subjects on these lines creates better composition."
                },
                {
                    "question": "What creates secondary colors?",
                    "options": ["Adding white", "Mixing primary colors", "Adding black", "Using only one color"],
                    "correct": 1,
                    "explanation": "Secondary colors (green, orange, purple) are created by mixing two primary colors together."
                }
            ],
            "intermediate": [
                {
                    "question": "What are complementary colors?",
                    "options": ["Colors that look good together", "Colors opposite on color wheel", "Colors next to each other", "Colors with same intensity"],
                    "correct": 1,
                    "explanation": "Complementary colors are opposite each other on the color wheel (red-green, blue-orange, yellow-purple) and create strong contrast."
                },
                {
                    "question": "What is chiaroscuro?",
                    "options": ["A painting technique", "Strong contrast of light and dark", "A type of sculpture", "A color mixing method"],
                    "correct": 1,
                    "explanation": "Chiaroscuro is an art technique using strong contrasts between light and dark to create dramatic effects and three-dimensional forms."
                },
                {
                    "question": "What is negative space?",
                    "options": ["Dark areas in art", "Empty space around objects", "Mistakes in artwork", "Background colors"],
                    "correct": 1,
                    "explanation": "Negative space is the empty area around and between objects in an artwork. It's as important as the positive space (the objects themselves)."
                }
            ]
        }

    def create_main_view(self):
        return ft.Container(
            ft.Column([
                ft.Text("🎨 Art & Design", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.PINK_900, text_align=ft.TextAlign.CENTER),
                ft.Text("Explore visual arts, design principles, and creative expression", size=16, color=ft.Colors.PINK_700, text_align=ft.TextAlign.CENTER),
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
                                ft.Icon(ft.Icons.PALETTE, size=30, color=ft.Colors.ORANGE_700),
                                ft.Text("Studio", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_art_studio(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.ORANGE_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                ], spacing=10, run_spacing=10),
                
                ft.Divider(height=20),
                
                # Quick overview
                ft.Container(
                    ft.Column([
                        ft.Text("📚 Art & Design Overview", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.PINK_800),
                        ft.Text("Art & Design develops creativity, visual communication skills, and aesthetic appreciation.", size=14),
                        ft.Text("🎭 Key Topics:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PINK_700),
                        ft.Column([
                            ft.Text("• Color Theory and Composition", size=14),
                            ft.Text("• Drawing and Painting Techniques", size=14),
                            ft.Text("• Design Principles and Elements", size=14),
                            ft.Text("• Digital Art and Photography", size=14),
                        ], spacing=5)
                    ], spacing=10),
                    bgcolor=ft.Colors.PINK_50,
                    border_radius=10,
                    padding=15,
                    border=ft.border.all(2, ft.Colors.PINK_200)
                )
            ], spacing=20),
            padding=20,
            expand=True
        )

    def show_ai_help(self):
        self.page.views.clear()
        
        query_field = ft.TextField(
            label="Ask about art & design...",
            hint_text="e.g., How do I improve my drawing skills?",
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
            "/art_design/ai_help",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/art_design")),
                    title=ft.Text("AI Art & Design Help"),
                    bgcolor=ft.Colors.PINK_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("🤖 AI Art & Design Assistant", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.PINK_900),
                        query_field,
                        ft.ElevatedButton(
                            "Get Help",
                            on_click=handle_query,
                            style=ft.ButtonStyle(bgcolor=ft.Colors.PINK_600, color=ft.Colors.WHITE)
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
            "/art_design/quizzes",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/art_design")),
                    title=ft.Text("Art & Design Quizzes"),
                    bgcolor=ft.Colors.PINK_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("📝 Choose Quiz Level", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.PINK_900),
                        
                        ft.ResponsiveRow([
                            ft.Container(
                                ft.ElevatedButton(
                                    content=ft.Column([
                                        ft.Icon(ft.Icons.LOOKS_ONE, size=30, color=ft.Colors.GREEN_700),
                                        ft.Text("Basic", size=16, weight=ft.FontWeight.BOLD),
                                        ft.Text("Color & composition", size=12)
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
                                        ft.Text("Art techniques", size=12)
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
            "/art_design/quiz_question",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/art_design/quizzes")),
                    title=ft.Text(f"Quiz - Question {self.quiz_question_index + 1}"),
                    bgcolor=ft.Colors.PINK_700
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
            "/art_design/quiz_explanation",
            [
                ft.AppBar(
                    title=ft.Text("Answer Explanation"),
                    bgcolor=ft.Colors.PINK_700
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
                            style=ft.ButtonStyle(bgcolor=ft.Colors.PINK_600, color=ft.Colors.WHITE)
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
            "/art_design/quiz_results",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/art_design")),
                    title=ft.Text("Quiz Results"),
                    bgcolor=ft.Colors.PINK_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("Quiz Complete!", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.PINK_900),
                        ft.Text(f"Score: {self.quiz_score}/{total_questions} ({percentage:.0f}%)", size=20),
                        ft.Text(message, size=18, color=color, weight=ft.FontWeight.BOLD),
                        ft.ElevatedButton(
                            "Try Again",
                            on_click=lambda e: self.start_quiz(self.current_quiz_level),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.PINK_600, color=ft.Colors.WHITE)
                        ),
                        ft.ElevatedButton(
                            "Back to Art & Design",
                            on_click=lambda e: self.page.go("/art_design")
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
                "title": "🎨 Elements of Art",
                "content": "Basic building blocks of visual art:\n\n• **Line**: Marks connecting points (straight, curved, thick, thin)\n• **Shape**: 2D enclosed areas (geometric, organic)\n• **Form**: 3D objects with volume\n• **Space**: Area around and between objects\n• **Color**: Hue, saturation, and value\n• **Texture**: Surface quality (rough, smooth, soft, hard)\n• **Value**: Lightness and darkness"
            },
            {
                "title": "🏗️ Principles of Design",
                "content": "Rules for organizing elements effectively:\n\n• **Balance**: Visual weight distribution (symmetrical, asymmetrical)\n• **Contrast**: Differences that create interest\n• **Emphasis**: Focal point that draws attention\n• **Movement**: Path eye follows through artwork\n• **Pattern**: Repeated elements\n• **Rhythm**: Regular repetition creating flow\n• **Unity**: Harmony among all elements"
            },
            {
                "title": "🌈 Color Theory",
                "content": "Understanding how colors work:\n\n• **Primary**: Red, blue, yellow (cannot be mixed)\n• **Secondary**: Green, orange, purple (mix 2 primaries)\n• **Tertiary**: Mix primary + secondary\n• **Complementary**: Opposite on color wheel\n• **Analogous**: Next to each other on wheel\n\n**Color Properties**: Hue (color), saturation (intensity), value (lightness/darkness)"
            },
            {
                "title": "✏️ Drawing & Painting",
                "content": "Fundamental art-making techniques:\n\n• **Contour Drawing**: Outline shapes and forms\n• **Shading**: Light and shadow create form\n• **Perspective**: Create illusion of depth\n• **Proportion**: Relative sizes of objects\n• **Gesture Drawing**: Quick sketches capturing movement\n\n**Painting**: Consider brush technique, color mixing, composition, and layering"
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
                        bgcolor=ft.Colors.PINK_50,
                        border_radius=8
                    )
                ]
            )
            explanation_cards.append(card)
        
        view = ft.View(
            "/art_design/explanations",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/art_design")),
                    title=ft.Text("Art & Design Concepts"),
                    bgcolor=ft.Colors.PINK_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("📚 Learn Art & Design", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.PINK_900),
                        ft.Text("Explore the fundamental concepts of art and design", size=16, color=ft.Colors.PINK_700),
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

    def show_art_studio(self):
        self.page.views.clear()
        
        studio_activities = [
            {
                "title": "🎨 Color Wheel Explorer",
                "description": "Interactive color theory learning tool",
                "action": "Explore Colors"
            },
            {
                "title": "✏️ Drawing Practice",
                "description": "Guided drawing exercises and techniques",
                "action": "Start Drawing"
            },
            {
                "title": "📸 Composition Analyzer",
                "description": "Learn composition through photo analysis",
                "action": "Analyze Photos"
            },
            {
                "title": "🖼️ Art History Timeline",
                "description": "Explore famous artworks and movements",
                "action": "Explore Art"
            }
        ]
        
        activity_cards = []
        for activity in studio_activities:
            card = ft.Container(
                ft.Column([
                    ft.Text(activity["title"], size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.PINK_900),
                    ft.Text(activity["description"], size=14, color=ft.Colors.PINK_700),
                    ft.ElevatedButton(
                        activity["action"],
                        on_click=lambda e, title=activity["title"]: self.start_studio_activity(title),
                        style=ft.ButtonStyle(bgcolor=ft.Colors.PINK_600, color=ft.Colors.WHITE)
                    )
                ], spacing=10),
                bgcolor=ft.Colors.PINK_50,
                border_radius=10,
                padding=15,
                border=ft.border.all(1, ft.Colors.PINK_200)
            )
            activity_cards.append(card)
        
        view = ft.View(
            "/art_design/art_studio",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/art_design")),
                    title=ft.Text("Art Studio"),
                    bgcolor=ft.Colors.PINK_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("🎨 Virtual Art Studio", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.PINK_900),
                        ft.Text("Interactive tools for art creation and learning", size=16, color=ft.Colors.PINK_700),
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

    def start_studio_activity(self, activity_title):
        self.page.show_snack_bar(
            ft.SnackBar(content=ft.Text(f"Studio activity '{activity_title}' will be available soon!"))
        )

def art_design_page(page: ft.Page):
    page.title = "Art & Design - Student AI Assistance"
    page.scroll = ft.ScrollMode.AUTO
    
    # Clear page content first
    page.clean()
    
    page.appbar = ft.AppBar(
        leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: page.go("/")),
        title=ft.Text("Art & Design"),
        bgcolor=ft.Colors.PINK_700,
        center_title=True
    )
    
    module = ArtDesignModule(page)
    page.add(module.create_main_view())