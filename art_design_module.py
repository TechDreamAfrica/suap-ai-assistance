import flet as ft
import random
import time
import math

def get_ai_help(query, topic="art_design"):
    """AI help response for Art & Design"""
    try:
        responses = {
            "color": "Color theory involves understanding how colors work together. Primary colors (red, blue, yellow) mix to create secondary colors (green, orange, purple). Complementary colors are opposite on the color wheel and create contrast. Warm colors (reds, oranges, yellows) advance while cool colors (blues, greens, purples) recede. Color temperature affects mood and spatial perception.",
            "composition": "Composition is how elements are arranged in artwork. The rule of thirds divides space into nine sections, placing focal points on intersection lines. Balance can be symmetrical (formal) or asymmetrical (informal). Leading lines guide the viewer's eye. Framing draws attention to subjects. Depth is created through overlapping, size variation, and atmospheric perspective.",
            "drawing": "Drawing is the foundation of visual art. Start with basic shapes and contour lines. Practice observational drawing from life. Use light and shadow (chiaroscuro) to create form. Understand perspective: one-point for depth, two-point for corners, three-point for dramatic angles. Master proportion through measurement and comparison techniques.",
            "painting": "Painting techniques vary by medium. Watercolor is transparent and flows, requiring wet-on-wet and wet-on-dry techniques. Acrylic dries quickly, allowing layering and mixed media. Oil paint stays wet longer, enabling blending and detail work. Consider brushwork, impasto (thick paint), glazing (thin layers), and color mixing strategies.",
            "design": "Design combines aesthetic appeal with functional purpose. Typography communicates through letterforms - consider hierarchy, contrast, and readability. Layout uses grids for organization. White space (negative space) is as important as content. Visual hierarchy guides attention through size, color, position, and contrast.",
            "sculpture": "Sculpture exists in three dimensions. Additive processes include modeling with clay or building with materials. Subtractive processes involve carving stone or wood. Consider form, mass, volume, and negative space. Surface treatments affect how light interacts with the piece. Installation art transforms entire spaces.",
            "photography": "Photography captures light and time. Composition rules apply: rule of thirds, leading lines, framing. Control exposure through aperture (depth of field), shutter speed (motion), and ISO (sensitivity). Natural light changes throughout the day. Consider foreground, middle ground, and background relationships.",
            "digital": "Digital art uses software as a creative medium. Raster images (pixels) work well for painting and photo manipulation. Vector graphics (mathematical curves) are ideal for logos and illustrations. Layer-based workflows allow non-destructive editing. Understanding traditional art principles remains essential in digital creation.",
            "history": "Art history provides context for creative expression. Ancient art served religious and political functions. Renaissance brought perspective and humanism. Impressionism captured light and moment. Modern art explored abstraction and conceptual ideas. Contemporary art addresses current social and technological issues.",
            "techniques": "Master fundamental techniques through practice. Hatching and cross-hatching create value through line density. Stippling uses dots for texture. Blending creates smooth transitions. Dry brush techniques create texture. Scumbling applies broken color over existing layers. Each technique serves specific expressive purposes."
        }
        
        query_lower = query.lower()
        for key, response in responses.items():
            if key in query_lower:
                return f"🎨 AI Art Tutor: {response}"
        
        return "🎨 AI Art Tutor: Art & Design explores visual creativity and self-expression through various media and techniques. Ask about color theory, composition, drawing, painting, design principles, sculpture, photography, digital art, art history, or specific techniques for detailed guidance!"
    except Exception:
        return "🎨 AI Art Tutor: I'm here to help with all aspects of art and design! Try asking about color theory, drawing techniques, composition, or any creative process."

class ArtDesignModule:
    def __init__(self, page):
        self.page = page
        self.current_quiz_level = "basic"
        self.quiz_score = 0
        self.quiz_question_index = 0
        
        # Enhanced quiz questions
        self.quiz_questions = {
            "basic": [
                {
                    "question": "What are the primary colors?",
                    "options": ["Red, Green, Blue", "Red, Blue, Yellow", "Blue, Yellow, Orange", "Red, Yellow, Green"],
                    "correct": 1,
                    "explanation": "The primary colors are red, blue, and yellow. These colors cannot be created by mixing other colors and form the basis for all other colors in traditional color theory."
                },
                {
                    "question": "What is the rule of thirds in composition?",
                    "options": ["Divide image into 3 equal parts", "Use only 3 colors", "Have 3 main subjects", "Divide image into 9 sections"],
                    "correct": 3,
                    "explanation": "The rule of thirds divides an image into 9 equal sections with 2 horizontal and 2 vertical lines. Placing important elements along these lines or at intersections creates more dynamic and visually interesting compositions."
                },
                {
                    "question": "What creates secondary colors?",
                    "options": ["Adding white", "Mixing primary colors", "Adding black", "Using only one color"],
                    "correct": 1,
                    "explanation": "Secondary colors (green, orange, purple) are created by mixing two primary colors together. Red + Blue = Purple, Blue + Yellow = Green, Yellow + Red = Orange."
                },
                {
                    "question": "Which element of art refers to the lightness or darkness of a color?",
                    "options": ["Hue", "Saturation", "Value", "Intensity"],
                    "correct": 2,
                    "explanation": "Value refers to the lightness or darkness of a color. It's crucial for creating contrast, depth, and form in artwork. High contrast in values creates drama, while low contrast creates harmony."
                }
            ],
            "intermediate": [
                {
                    "question": "What are complementary colors?",
                    "options": ["Colors that look good together", "Colors opposite on color wheel", "Colors next to each other", "Colors with same intensity"],
                    "correct": 1,
                    "explanation": "Complementary colors are opposite each other on the color wheel (red-green, blue-orange, yellow-purple). They create strong contrast and visual vibration when placed next to each other."
                },
                {
                    "question": "What is chiaroscuro?",
                    "options": ["A painting technique", "Strong contrast of light and dark", "A type of sculpture", "A color mixing method"],
                    "correct": 1,
                    "explanation": "Chiaroscuro is an art technique using strong contrasts between light and dark to create dramatic effects, three-dimensional forms, and emotional impact. Masters like Caravaggio and Rembrandt were famous for this technique."
                },
                {
                    "question": "What is negative space?",
                    "options": ["Dark areas in art", "Empty space around objects", "Mistakes in artwork", "Background colors"],
                    "correct": 1,
                    "explanation": "Negative space is the empty area around and between objects in an artwork. It's as important as the positive space (the objects themselves) and can be used to create powerful compositions and illusions."
                },
                {
                    "question": "Which perspective technique uses two vanishing points?",
                    "options": ["One-point perspective", "Two-point perspective", "Three-point perspective", "Atmospheric perspective"],
                    "correct": 1,
                    "explanation": "Two-point perspective uses two vanishing points on the horizon line and is typically used when viewing the corner of an object, like the corner of a building. It creates more dynamic and realistic spatial depth."
                }
            ]
        }
        
        # Color wheel data for interactive tools
        self.color_relationships = {
            "primary": ["Red", "Blue", "Yellow"],
            "secondary": ["Green", "Orange", "Purple"],
            "complementary_pairs": [
                ("Red", "Green"),
                ("Blue", "Orange"), 
                ("Yellow", "Purple")
            ],
            "analogous_examples": [
                ["Red", "Red-Orange", "Orange"],
                ["Blue", "Blue-Green", "Green"],
                ["Yellow", "Yellow-Green", "Green"]
            ]
        }
        
        # Drawing tutorials
        self.drawing_tutorials = {
            "basic_shapes": {
                "title": "Master Basic Shapes",
                "description": "Learn to draw fundamental geometric shapes",
                "steps": [
                    "Start with circles - practice drawing smooth, even circles",
                    "Draw squares and rectangles with straight, parallel lines", 
                    "Practice triangles - equilateral, isosceles, and scalene",
                    "Combine shapes to create complex objects",
                    "Add depth with simple perspective techniques"
                ],
                "tips": [
                    "Use light, confident strokes",
                    "Practice daily for muscle memory",
                    "Don't worry about perfection initially",
                    "Focus on proportions and relationships"
                ]
            },
            "perspective": {
                "title": "Understanding Perspective",
                "description": "Create depth and dimension in your drawings",
                "steps": [
                    "One-point perspective: Draw a horizon line and vanishing point",
                    "Draw a square or rectangle in the foreground",
                    "Connect corners to vanishing point for depth",
                    "Practice with simple objects like boxes and buildings",
                    "Two-point perspective: Use two vanishing points for corners"
                ],
                "tips": [
                    "Start with simple geometric forms",
                    "Use a ruler for construction lines",
                    "Objects get smaller as they recede",
                    "Keep horizon line consistent"
                ]
            },
            "shading": {
                "title": "Light and Shadow Techniques",
                "description": "Bring your drawings to life with realistic shading",
                "steps": [
                    "Identify light source direction",
                    "Map out highlight, midtone, and shadow areas",
                    "Use hatching for controlled value gradations",
                    "Try cross-hatching for darker areas",
                    "Blend with stumps or fingers for smooth transitions"
                ],
                "tips": [
                    "Squint to see value relationships clearly",
                    "Start light and build up darkness gradually",
                    "Leave white paper for strongest highlights",
                    "Reflected light softens shadow edges"
                ]
            }
        }
        
        # Art history timeline
        self.art_movements = {
            "Renaissance": {
                "period": "14th-17th Century",
                "characteristics": "Perspective, humanism, classical subjects, realistic representation",
                "key_artists": ["Leonardo da Vinci", "Michelangelo", "Raphael"],
                "famous_works": ["Mona Lisa", "Sistine Chapel", "The School of Athens"]
            },
            "Impressionism": {
                "period": "1860s-1880s",
                "characteristics": "Light and atmosphere, visible brushstrokes, outdoor painting, everyday subjects",
                "key_artists": ["Claude Monet", "Pierre-Auguste Renoir", "Edgar Degas"],
                "famous_works": ["Water Lilies", "Luncheon of the Boating Party", "The Dance Class"]
            },
            "Cubism": {
                "period": "1907-1914",
                "characteristics": "Geometric forms, multiple perspectives, fragmented objects, abstract representation",
                "key_artists": ["Pablo Picasso", "Georges Braque", "Juan Gris"],
                "famous_works": ["Les Demoiselles d'Avignon", "Guernica", "Violin and Candlestick"]
            },
            "Abstract Expressionism": {
                "period": "1940s-1960s",
                "characteristics": "Non-representational, emotional expression, large scale, gestural brushwork",
                "key_artists": ["Jackson Pollock", "Mark Rothko", "Willem de Kooning"],
                "famous_works": ["No. 1, 1950", "Orange, Red, Yellow", "Woman I"]
            }
        }

    def create_main_view(self):
        return ft.Container(
            ft.Column([
                ft.Text("🎨 Art & Design Studio", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.PINK_900, text_align=ft.TextAlign.CENTER),
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
                                ft.Icon(ft.Icons.PALETTE, size=30, color=ft.Colors.GREEN_700),
                                ft.Text("Color Theory", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_color_theory(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.GREEN_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.DRAW, size=30, color=ft.Colors.ORANGE_700),
                                ft.Text("Drawing", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_drawing_tutorials(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.ORANGE_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.GRID_VIEW, size=30, color=ft.Colors.PURPLE_700),
                                ft.Text("Composition", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_composition_tools(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.PURPLE_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                ], spacing=10, run_spacing=10),
                
                ft.ResponsiveRow([
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.QUIZ_OUTLINED, size=30, color=ft.Colors.TEAL_700),
                                ft.Text("Art Quiz", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_quizzes(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.TEAL_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.HISTORY_EDU, size=30, color=ft.Colors.INDIGO_700),
                                ft.Text("Art History", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_art_history(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.INDIGO_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.CAMERA, size=30, color=ft.Colors.CYAN_700),
                                ft.Text("Photography", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_photography_basics(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.CYAN_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.COMPUTER, size=30, color=ft.Colors.DEEP_PURPLE_700),
                                ft.Text("Digital Art", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_digital_art(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.DEEP_PURPLE_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                ], spacing=10, run_spacing=10),
                
                ft.Divider(height=20),
                
                # Quick overview with creative project ideas
                ft.Container(
                    ft.Column([
                        ft.Text("🎨 Art & Design Overview", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.PINK_800),
                        ft.Text("Art & Design develops creativity, visual communication skills, and aesthetic appreciation through hands-on exploration.", size=14),
                        ft.Text("🎭 Core Skills:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PINK_700),
                        ft.Column([
                            ft.Text("• Color theory and color mixing techniques", size=14),
                            ft.Text("• Drawing fundamentals and observational skills", size=14),
                            ft.Text("• Composition and visual design principles", size=14),
                            ft.Text("• Art history and cultural context", size=14),
                            ft.Text("• Digital tools and modern media", size=14),
                            ft.Text("• Critical analysis and creative problem-solving", size=14),
                        ], spacing=5),
                        ft.Text("💡 Project Ideas:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PINK_700),
                        ft.Text("Try creating a self-portrait, designing a poster for a school event, or starting a nature sketchbook!", size=14, style=ft.TextStyle(italic=True))
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
            hint_text="e.g., How do I mix colors? or What makes a good composition?",
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
        
        # Quick question buttons
        quick_questions = [
            "What are warm and cool colors?",
            "How do I improve my drawing skills?", 
            "What is good composition?",
            "Tell me about perspective drawing",
            "How do I choose colors for my artwork?",
            "What are the elements of art?"
        ]
        
        def ask_quick_question(question):
            query_field.value = question
            handle_query(None)
        
        view = ft.View(
            "/art_design/ai_help",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/art_design")),
                    title=ft.Text("AI Art & Design Assistant"),
                    bgcolor=ft.Colors.PINK_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("🎨 AI Art & Design Assistant", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.PINK_900),
                        query_field,
                        ft.ElevatedButton(
                            "Get Help",
                            on_click=handle_query,
                            style=ft.ButtonStyle(bgcolor=ft.Colors.PINK_600, color=ft.Colors.WHITE)
                        ),
                        ft.Container(response_text, bgcolor=ft.Colors.GREY_100, border_radius=10, padding=15, expand=True),
                        ft.Text("💡 Quick Questions:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PINK_900),
                        ft.Wrap([
                            ft.ElevatedButton(
                                question,
                                on_click=lambda e, q=question: ask_quick_question(q),
                                style=ft.ButtonStyle(bgcolor=ft.Colors.PINK_100)
                            ) for question in quick_questions
                        ], spacing=10, run_spacing=10)
                    ], spacing=15),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def show_color_theory(self):
        self.page.views.clear()
        
        # Interactive color wheel component
        def create_color_info_card(title, colors, description):
            color_swatches = []
            color_map = {
                "Red": ft.Colors.RED, "Blue": ft.Colors.BLUE, "Yellow": ft.Colors.YELLOW,
                "Green": ft.Colors.GREEN, "Orange": ft.Colors.ORANGE, "Purple": ft.Colors.PURPLE,
                "Red-Orange": ft.Colors.DEEP_ORANGE, "Yellow-Green": ft.Colors.LIGHT_GREEN,
                "Blue-Green": ft.Colors.TEAL
            }
            
            for color in colors:
                color_swatches.append(
                    ft.Container(
                        ft.Text(color, size=10, color=ft.Colors.WHITE, text_align=ft.TextAlign.CENTER),
                        bgcolor=color_map.get(color, ft.Colors.GREY),
                        width=60,
                        height=40,
                        border_radius=5,
                        alignment=ft.alignment.center
                    )
                )
            
            return ft.Container(
                ft.Column([
                    ft.Text(title, size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_900),
                    ft.Row(color_swatches, spacing=5, wrap=True),
                    ft.Text(description, size=12)
                ], spacing=10),
                bgcolor=ft.Colors.GREEN_50,
                border_radius=10,
                padding=15,
                border=ft.border.all(1, ft.Colors.GREEN_200)
            )
        
        view = ft.View(
            "/art_design/color_theory",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/art_design")),
                    title=ft.Text("Color Theory Explorer"),
                    bgcolor=ft.Colors.GREEN_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("🌈 Interactive Color Theory", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_900),
                        ft.Text("Understand how colors work together to create harmony and contrast", size=16, color=ft.Colors.GREEN_700),
                        
                        create_color_info_card(
                            "Primary Colors",
                            self.color_relationships["primary"],
                            "Cannot be created by mixing other colors. Foundation of all other colors."
                        ),
                        
                        create_color_info_card(
                            "Secondary Colors", 
                            self.color_relationships["secondary"],
                            "Created by mixing two primary colors together."
                        ),
                        
                        ft.Text("🎨 Color Relationships:", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_900),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("Complementary Colors", size=16, weight=ft.FontWeight.BOLD),
                                ft.Text("Opposite colors on the wheel create strong contrast:", size=14),
                                *[ft.Row([
                                    ft.Container(bgcolor=ft.Colors.RED if pair[0] == "Red" else ft.Colors.BLUE if pair[0] == "Blue" else ft.Colors.YELLOW, width=40, height=30, border_radius=5),
                                    ft.Text("⟷", size=20),
                                    ft.Container(bgcolor=ft.Colors.GREEN if pair[1] == "Green" else ft.Colors.ORANGE if pair[1] == "Orange" else ft.Colors.PURPLE, width=40, height=30, border_radius=5),
                                    ft.Text(f"{pair[0]} + {pair[1]}", size=14)
                                ], spacing=10) for pair in self.color_relationships["complementary_pairs"]]
                            ], spacing=10),
                            bgcolor=ft.Colors.BLUE_50,
                            border_radius=10,
                            padding=15
                        ),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("Color Properties", size=16, weight=ft.FontWeight.BOLD),
                                ft.Text("• Hue: The color itself (red, blue, yellow)", size=14),
                                ft.Text("• Saturation: Intensity or purity of color", size=14),  
                                ft.Text("• Value: Lightness or darkness of color", size=14),
                                ft.Text("• Temperature: Warm colors advance, cool colors recede", size=14),
                            ], spacing=5),
                            bgcolor=ft.Colors.ORANGE_50,
                            border_radius=10,
                            padding=15
                        ),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("🎨 Try This Exercise!", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_900),
                                ft.Text("1. Find objects around you in primary colors", size=14),
                                ft.Text("2. Mix paints or colored pencils to create secondary colors", size=14),
                                ft.Text("3. Create a color wheel showing relationships", size=14),
                                ft.Text("4. Experiment with complementary color combinations", size=14)
                            ], spacing=5),
                            bgcolor=ft.Colors.PURPLE_50,
                            border_radius=10,
                            padding=15,
                            border=ft.border.all(2, ft.Colors.PURPLE_300)
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

    def show_drawing_tutorials(self):
        self.page.views.clear()
        
        tutorial_cards = []
        for tutorial_key, tutorial_data in self.drawing_tutorials.items():
            steps_widgets = [ft.Text(f"{i+1}. {step}", size=14) for i, step in enumerate(tutorial_data["steps"])]
            tips_widgets = [ft.Text(f"• {tip}", size=12, color=ft.Colors.BLUE_700) for tip in tutorial_data["tips"]]
            
            card = ft.Container(
                ft.Column([
                    ft.Text(tutorial_data["title"], size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_900),
                    ft.Text(tutorial_data["description"], size=14, color=ft.Colors.ORANGE_700),
                    ft.Text("📝 Steps:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_800),
                    ft.Column(steps_widgets, spacing=5),
                    ft.Text("💡 Tips:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800),
                    ft.Column(tips_widgets, spacing=3),
                    ft.ElevatedButton(
                        "Start Practice Session",
                        on_click=lambda e, key=tutorial_key: self.start_drawing_practice(key),
                        style=ft.ButtonStyle(bgcolor=ft.Colors.ORANGE_600, color=ft.Colors.WHITE)
                    )
                ], spacing=10),
                bgcolor=ft.Colors.ORANGE_50,
                border_radius=12,
                padding=20,
                border=ft.border.all(2, ft.Colors.ORANGE_200),
                margin=ft.margin.only(bottom=15)
            )
            tutorial_cards.append(card)
        
        view = ft.View(
            "/art_design/drawing_tutorials",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/art_design")),
                    title=ft.Text("Drawing Tutorials"),
                    bgcolor=ft.Colors.ORANGE_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("✏️ Master Drawing Skills", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_900),
                        ft.Text("Step-by-step tutorials to develop your drawing abilities", size=16, color=ft.Colors.ORANGE_700),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("🎯 Drawing Fundamentals", size=16, weight=ft.FontWeight.BOLD),
                                ft.Text("Drawing is like learning a language - start with basic 'vocabulary' (shapes and lines) then build complexity. Regular practice is more valuable than long, infrequent sessions.", size=14),
                                ft.Text("Essential supplies: Pencils (2H, HB, 2B, 4B), eraser, blending stump, good paper", size=14, style=ft.TextStyle(italic=True))
                            ], spacing=5),
                            bgcolor=ft.Colors.BLUE_50,
                            border_radius=8,
                            padding=15,
                            margin=ft.margin.only(bottom=20)
                        ),
                        
                        ft.Column(tutorial_cards, spacing=0)
                    ], spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def start_drawing_practice(self, tutorial_key):
        tutorial_data = self.drawing_tutorials[tutorial_key]
        
        self.page.views.clear()
        view = ft.View(
            "/art_design/drawing_practice",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.show_drawing_tutorials()),
                    title=ft.Text(f"Practice: {tutorial_data['title']}"),
                    bgcolor=ft.Colors.ORANGE_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text(f"🎨 {tutorial_data['title']} Practice", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_900),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("📋 Practice Checklist:", size=16, weight=ft.FontWeight.BOLD),
                                *[ft.Row([
                                    ft.Checkbox(value=False, on_change=lambda e: self.page.update()),
                                    ft.Text(step, size=14)
                                ]) for step in tutorial_data["steps"]]
                            ], spacing=10),
                            bgcolor=ft.Colors.ORANGE_50,
                            border_radius=10,
                            padding=15
                        ),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("🎯 Practice Timer", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_900),
                                ft.Text("Recommended practice: 15-30 minutes", size=14),
                                ft.Row([
                                    ft.ElevatedButton(
                                        "Start 15 min",
                                        on_click=lambda e: self.start_practice_timer(15),
                                        style=ft.ButtonStyle(bgcolor=ft.Colors.GREEN_600, color=ft.Colors.WHITE)
                                    ),
                                    ft.ElevatedButton(
                                        "Start 30 min", 
                                        on_click=lambda e: self.start_practice_timer(30),
                                        style=ft.ButtonStyle(bgcolor=ft.Colors.BLUE_600, color=ft.Colors.WHITE)
                                    )
                                ], spacing=10)
                            ], spacing=10),
                            bgcolor=ft.Colors.GREEN_50,
                            border_radius=10,
                            padding=15
                        ),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("💡 Remember:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                                *[ft.Text(f"• {tip}", size=14) for tip in tutorial_data["tips"]]
                            ], spacing=5),
                            bgcolor=ft.Colors.BLUE_50,
                            border_radius=10,
                            padding=15
                        ),
                        
                        ft.ElevatedButton(
                            "Complete Practice Session",
                            on_click=lambda e: self.complete_practice_session(),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.ORANGE_600, color=ft.Colors.WHITE)
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

    def start_practice_timer(self, minutes):
        self.page.show_snack_bar(
            ft.SnackBar(content=ft.Text(f"Practice timer started for {minutes} minutes! Focus on your drawing."))
        )

    def complete_practice_session(self):
        self.page.show_snack_bar(
            ft.SnackBar(content=ft.Text("Great job! Regular practice leads to improvement. Keep drawing!"))
        )

    def show_composition_tools(self):
        self.page.views.clear()
        
        # Rule of thirds visualization
        def create_composition_example(title, description, grid_overlay=False):
            # Create a simple visual example
            example_container = ft.Container(
                ft.Stack([
                    ft.Container(
                        bgcolor=ft.Colors.BLUE_100,
                        width=200,
                        height=150,
                        border_radius=5
                    ),
                    # Add grid overlay for rule of thirds
                    ft.Container(
                        ft.Column([
                            ft.Container(height=50, border=ft.border.only(bottom=ft.border.BorderSide(1, ft.Colors.RED_300))),
                            ft.Container(height=50, border=ft.border.only(bottom=ft.border.BorderSide(1, ft.Colors.RED_300))),
                            ft.Container(height=50)
                        ]),
                        width=200
                    ) if grid_overlay else None,
                    ft.Container(
                        ft.Column([
                            ft.Row([
                                ft.Container(width=66, border=ft.border.only(right=ft.border.BorderSide(1, ft.Colors.RED_300))),
                                ft.Container(width=67, border=ft.border.only(right=ft.border.BorderSide(1, ft.Colors.RED_300))),
                                ft.Container(width=67)
                            ])
                        ]),
                        height=150
                    ) if grid_overlay else None,
                    # Add sample subject at intersection point
                    ft.Positioned(
                        ft.Container(
                            ft.Icon(ft.Icons.CIRCLE, color=ft.Colors.YELLOW_700, size=20),
                            bgcolor=ft.Colors.YELLOW,
                            width=30,
                            height=30,
                            border_radius=15
                        ),
                        top=45,
                        left=60
                    ) if grid_overlay else None
                ]),
                margin=ft.margin.only(bottom=10)
            )
            
            return ft.Container(
                ft.Column([
                    ft.Text(title, size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_900),
                    example_container,
                    ft.Text(description, size=12)
                ], spacing=10),
                bgcolor=ft.Colors.PURPLE_50,
                border_radius=10,
                padding=15,
                border=ft.border.all(1, ft.Colors.PURPLE_200)
            )
        
        composition_principles = [
            {
                "title": "Rule of Thirds",
                "description": "Divide your image into 9 equal sections. Place important elements along these lines or at intersections.",
                "example": "Place horizon on upper or lower third line, not center"
            },
            {
                "title": "Leading Lines", 
                "description": "Use lines to guide the viewer's eye toward your focal point.",
                "example": "Roads, fences, shorelines can lead to your subject"
            },
            {
                "title": "Framing",
                "description": "Use elements in the scene to create a frame around your subject.",
                "example": "Tree branches, doorways, windows can frame your subject"
            },
            {
                "title": "Balance",
                "description": "Distribute visual weight evenly across your composition.",
                "example": "Large object on one side balanced by smaller objects on the other"
            }
        ]
        
        principle_cards = []
        for principle in composition_principles:
            card = ft.Container(
                ft.Column([
                    ft.Text(principle["title"], size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_900),
                    ft.Text(principle["description"], size=14),
                    ft.Container(
                        ft.Text(f"Example: {principle['example']}", size=12, style=ft.TextStyle(italic=True)),
                        bgcolor=ft.Colors.GREY_100,
                        border_radius=5,
                        padding=8
                    )
                ], spacing=10),
                bgcolor=ft.Colors.PURPLE_50,
                border_radius=10,
                padding=15,
                border=ft.border.all(1, ft.Colors.PURPLE_200),
                margin=ft.margin.only(bottom=10)
            )
            principle_cards.append(card)
        
        view = ft.View(
            "/art_design/composition",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/art_design")),
                    title=ft.Text("Composition Tools"),
                    bgcolor=ft.Colors.PURPLE_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("🔳 Composition Mastery", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_900),
                        ft.Text("Learn to arrange elements for powerful visual impact", size=16, color=ft.Colors.PURPLE_700),
                        
                        create_composition_example(
                            "Rule of Thirds Example",
                            "Subject placed at intersection point creates dynamic composition",
                            grid_overlay=True
                        ),
                        
                        ft.Text("📐 Composition Principles:", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_900),
                        ft.Column(principle_cards, spacing=0),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("🎯 Composition Exercise", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_900),
                                ft.Text("1. Take or find 5 photos/images", size=14),
                                ft.Text("2. Draw rule of thirds grid over each", size=14),
                                ft.Text("3. Identify where focal points fall", size=14),
                                ft.Text("4. Analyze which compositions work best and why", size=14),
                                ft.Text("5. Practice cropping images to improve composition", size=14)
                            ], spacing=5),
                            bgcolor=ft.Colors.GREEN_50,
                            border_radius=10,
                            padding=15,
                            border=ft.border.all(2, ft.Colors.GREEN_300)
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

    def show_quizzes(self):
        self.page.views.clear()
        
        view = ft.View(
            "/art_design/quizzes",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/art_design")),
                    title=ft.Text("Art & Design Quizzes"),
                    bgcolor=ft.Colors.TEAL_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("📝 Test Your Art Knowledge", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.TEAL_900),
                        ft.Text("Challenge yourself with interactive art and design questions", size=16, color=ft.Colors.TEAL_700),
                        
                        ft.ResponsiveRow([
                            ft.Container(
                                ft.ElevatedButton(
                                    content=ft.Column([
                                        ft.Icon(ft.Icons.LOOKS_ONE, size=30, color=ft.Colors.GREEN_700),
                                        ft.Text("Basic Level", size=16, weight=ft.FontWeight.BOLD),
                                        ft.Text("Color theory & composition basics", size=12, text_align=ft.TextAlign.CENTER),
                                        ft.Text("4 Questions", size=10, color=ft.Colors.GREY_600)
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
                                        ft.Text("Advanced techniques & art history", size=12, text_align=ft.TextAlign.CENTER),
                                        ft.Text("4 Questions", size=10, color=ft.Colors.GREY_600)
                                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                                    on_click=lambda e: self.start_quiz("intermediate"),
                                    style=ft.ButtonStyle(padding=20, bgcolor=ft.Colors.ORANGE_50, shape=ft.RoundedRectangleBorder(radius=10))
                                ),
                                col={'xs': 12, 'sm': 6}
                            ),
                        ], spacing=15),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("🎨 What You'll Learn:", size=16, weight=ft.FontWeight.BOLD),
                                ft.Text("• Color relationships and theory", size=14),
                                ft.Text("• Composition techniques and visual balance", size=14),
                                ft.Text("• Art terminology and concepts", size=14),
                                ft.Text("• Historical art movements and styles", size=14),
                                ft.Text("• Drawing and painting techniques", size=14)
                            ], spacing=5),
                            bgcolor=ft.Colors.BLUE_50,
                            border_radius=10,
                            padding=15,
                            margin=ft.margin.only(top=20)
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
                        bgcolor=ft.Colors.TEAL_50,
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
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.show_quizzes()),
                    title=ft.Text(f"Question {self.quiz_question_index + 1}"),
                    bgcolor=ft.Colors.TEAL_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Row([
                            ft.Text(f"Question {self.quiz_question_index + 1} of {len(questions)}", size=16, color=ft.Colors.GREY_600),
                            ft.Container(
                                ft.Text(f"Score: {self.quiz_score}/{self.quiz_question_index}", size=14, color=ft.Colors.BLUE_700),
                                bgcolor=ft.Colors.BLUE_50,
                                border_radius=5,
                                padding=ft.padding.symmetric(horizontal=8, vertical=4)
                            )
                        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                        ft.Text(question["question"], size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.TEAL_900),
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
                    bgcolor=ft.Colors.TEAL_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Icon(
                            ft.Icons.CHECK_CIRCLE if is_correct else ft.Icons.CANCEL,
                            size=60,
                            color=ft.Colors.GREEN if is_correct else ft.Colors.RED
                        ),
                        ft.Text(
                            "Excellent!" if is_correct else "Not quite right",
                            size=24,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.GREEN if is_correct else ft.Colors.RED
                        ),
                        ft.Container(
                            ft.Column([
                                ft.Text("Correct Answer:", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                                ft.Text(question['options'][question['correct']], size=16, color=ft.Colors.BLUE_700),
                                ft.Divider(),
                                ft.Text("Explanation:", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_900),
                                ft.Text(question["explanation"], size=14)
                            ], spacing=8),
                            bgcolor=ft.Colors.BLUE_50,
                            border_radius=10,
                            padding=15
                        ),
                        ft.ElevatedButton(
                            "Continue" if self.quiz_question_index + 1 < len(questions) else "See Results",
                            on_click=lambda e: self.next_question(),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.TEAL_600, color=ft.Colors.WHITE)
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
            message = "Outstanding artistic knowledge!"
            color = ft.Colors.GREEN
            emoji = "🏆"
        elif percentage >= 60:
            message = "Good grasp of art concepts!"
            color = ft.Colors.ORANGE
            emoji = "👍"
        else:
            message = "Keep exploring and learning!"
            color = ft.Colors.BLUE
            emoji = "📚"
        
        self.page.views.clear()
        view = ft.View(
            "/art_design/quiz_results",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/art_design")),
                    title=ft.Text("Quiz Results"),
                    bgcolor=ft.Colors.TEAL_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text(f"{emoji} Quiz Complete!", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.TEAL_900),
                        ft.Container(
                            ft.Column([
                                ft.Text(f"Your Score", size=16, weight=ft.FontWeight.BOLD),
                                ft.Text(f"{self.quiz_score}/{total_questions}", size=36, weight=ft.FontWeight.BOLD, color=color),
                                ft.Text(f"{percentage:.0f}%", size=20, color=color)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            bgcolor=ft.Colors.WHITE,
                            border_radius=15,
                            padding=20,
                            border=ft.border.all(3, color)
                        ),
                        ft.Text(message, size=18, color=color, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                        ft.Row([
                            ft.ElevatedButton(
                                "Try Again",
                                on_click=lambda e: self.start_quiz(self.current_quiz_level),
                                style=ft.ButtonStyle(bgcolor=ft.Colors.TEAL_600, color=ft.Colors.WHITE)
                            ),
                            ft.ElevatedButton(
                                "Try Other Level",
                                on_click=lambda e: self.show_quizzes()
                            ),
                            ft.ElevatedButton(
                                "Back to Studio",
                                on_click=lambda e: self.page.go("/art_design")
                            )
                        ], alignment=ft.MainAxisAlignment.CENTER, spacing=10, wrap=True)
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def show_art_history(self):
        self.page.views.clear()
        
        movement_cards = []
        for movement, details in self.art_movements.items():
            artists_text = ", ".join(details["key_artists"])
            works_text = ", ".join(details["famous_works"])
            
            card = ft.Container(
                ft.Column([
                    ft.Text(movement, size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.INDIGO_900),
                    ft.Container(
                        ft.Text(details["period"], size=14, weight=ft.FontWeight.W_500),
                        bgcolor=ft.Colors.INDIGO_200,
                        border_radius=5,
                        padding=ft.padding.symmetric(horizontal=8, vertical=4)
                    ),
                    ft.Text("Characteristics:", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.INDIGO_800),
                    ft.Text(details["characteristics"], size=13),
                    ft.Text("Key Artists:", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.INDIGO_800),
                    ft.Text(artists_text, size=13, style=ft.TextStyle(italic=True)),
                    ft.Text("Famous Works:", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.INDIGO_800),
                    ft.Text(works_text, size=13, style=ft.TextStyle(italic=True))
                ], spacing=8),
                bgcolor=ft.Colors.INDIGO_50,
                border_radius=12,
                padding=20,
                border=ft.border.all(2, ft.Colors.INDIGO_200),
                margin=ft.margin.only(bottom=15)
            )
            movement_cards.append(card)
        
        view = ft.View(
            "/art_design/art_history",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/art_design")),
                    title=ft.Text("Art History Timeline"),
                    bgcolor=ft.Colors.INDIGO_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("🏛️ Art Through the Ages", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.INDIGO_900),
                        ft.Text("Explore major art movements and their cultural impact", size=16, color=ft.Colors.INDIGO_700),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("🎨 Why Study Art History?", size=16, weight=ft.FontWeight.BOLD),
                                ft.Text("Art history helps us understand how artists responded to their times, developed new techniques, and influenced culture. Each movement built upon previous ones while breaking new ground.", size=14),
                                ft.Text("Key themes: Religious and political power, technological advances, social change, cultural exchange", size=14, style=ft.TextStyle(italic=True))
                            ], spacing=5),
                            bgcolor=ft.Colors.BLUE_50,
                            border_radius=10,
                            padding=15,
                            margin=ft.margin.only(bottom=20)
                        ),
                        
                        ft.Column(movement_cards, spacing=0),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("🔍 Art Analysis Activity", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_900),
                                ft.Text("Choose an artwork from any movement above and analyze:", size=14),
                                ft.Text("1. What do you see? (Describe literally)", size=13),
                                ft.Text("2. How is it made? (Technique, materials, composition)", size=13),
                                ft.Text("3. What does it mean? (Symbolism, historical context)", size=13),
                                ft.Text("4. Why does it matter? (Influence, innovation, cultural significance)", size=13)
                            ], spacing=5),
                            bgcolor=ft.Colors.GREEN_50,
                            border_radius=10,
                            padding=15,
                            border=ft.border.all(2, ft.Colors.GREEN_300)
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

    def show_photography_basics(self):
        self.page.views.clear()
        
        photography_topics = [
            {
                "title": "📐 Composition in Photography",
                "content": "Good composition transforms ordinary subjects into compelling images:\n\n• Rule of Thirds: Place subjects on imaginary grid lines\n• Leading Lines: Use roads, fences, or rivers to guide the eye\n• Framing: Use doorways, branches, or shadows as natural frames\n• Symmetry: Perfect balance creates formal, peaceful feeling\n• Fill the Frame: Get close to eliminate distractions",
                "tips": ["Move around your subject", "Try different angles", "Look for patterns and textures"]
            },
            {
                "title": "💡 Understanding Light",
                "content": "Photography means 'drawing with light' - understanding light is essential:\n\n• Golden Hour: Soft, warm light just after sunrise/before sunset\n• Blue Hour: Even, diffused light just after sunset\n• Harsh Light: Midday sun creates strong shadows and contrast\n• Backlighting: Light behind subject creates silhouettes or rim lighting\n• Direction: Front, side, and back lighting create different moods",
                "tips": ["Observe how light changes throughout the day", "Use shadows creatively", "Cloudy days provide soft, even light"]
            },
            {
                "title": "🎯 Camera Settings Basics",
                "content": "Master these fundamental camera controls:\n\n• Aperture: Controls depth of field (f/1.4 = shallow, f/11 = deep)\n• Shutter Speed: Controls motion blur (1/500s freezes, 1/30s blurs)\n• ISO: Controls sensor sensitivity (100 = clean, 1600+ = grainy)\n• Focus: Single point for precision, continuous for moving subjects\n• Exposure: Balance aperture, shutter, and ISO for proper brightness",
                "tips": ["Start in aperture priority mode", "Use faster shutter for action", "Lower ISO for better image quality"]
            },
            {
                "title": "🖼️ Visual Storytelling",
                "content": "Great photos tell stories and evoke emotions:\n\n• Decisive Moment: Capture peak action or emotion\n• Context: Include environment to tell fuller story\n• Series: Multiple images can build narrative\n• Perspective: Get low, get high, get close for impact\n• Emotion: Focus on expressions, gestures, and relationships",
                "tips": ["Be patient for the right moment", "Think about what you want to communicate", "Edit ruthlessly - show only your best work"]
            }
        ]
        
        topic_cards = []
        for topic in photography_topics:
            tips_text = "\n".join([f"• {tip}" for tip in topic["tips"]])
            
            card = ft.ExpansionTile(
                title=ft.Text(topic["title"], size=16, weight=ft.FontWeight.BOLD),
                subtitle=ft.Text("Tap to explore photography techniques"),
                controls=[
                    ft.Container(
                        ft.Column([
                            ft.Text(topic["content"], size=14),
                            ft.Text("💡 Pro Tips:", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.CYAN_700),
                            ft.Text(tips_text, size=13, color=ft.Colors.CYAN_600)
                        ], spacing=10),
                        padding=15,
                        bgcolor=ft.Colors.CYAN_50,
                        border_radius=8
                    )
                ]
            )
            topic_cards.append(card)
        
        view = ft.View(
            "/art_design/photography",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/art_design")),
                    title=ft.Text("Photography Basics"),
                    bgcolor=ft.Colors.CYAN_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("📷 Photography Fundamentals", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.CYAN_900),
                        ft.Text("Master the art of capturing light and telling visual stories", size=16, color=ft.Colors.CYAN_700),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("🎯 Photography Learning Path:", size=16, weight=ft.FontWeight.BOLD),
                                ft.Text("1. Master composition rules and when to break them", size=14),
                                ft.Text("2. Understand how light affects your images", size=14),
                                ft.Text("3. Learn camera controls (or smartphone camera modes)", size=14),
                                ft.Text("4. Practice visual storytelling techniques", size=14),
                                ft.Text("5. Develop your unique artistic voice", size=14)
                            ], spacing=5),
                            bgcolor=ft.Colors.BLUE_50,
                            border_radius=8,
                            padding=15,
                            border=ft.border.all(1, ft.Colors.BLUE_200),
                            margin=ft.margin.only(bottom=20)
                        ),
                        
                        ft.Column(topic_cards, spacing=10),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("📱 Smartphone Photography Challenge", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_900),
                                ft.Text("This week, take one photo each day focusing on:", size=14),
                                ft.Text("• Monday: Rule of thirds composition", size=13),
                                ft.Text("• Tuesday: Leading lines", size=13),
                                ft.Text("• Wednesday: Natural framing", size=13),
                                ft.Text("• Thursday: Golden hour light", size=13),
                                ft.Text("• Friday: Close-up details", size=13),
                                ft.Text("• Weekend: Your creative choice!", size=13)
                            ], spacing=5),
                            bgcolor=ft.Colors.GREEN_50,
                            border_radius=10,
                            padding=15,
                            border=ft.border.all(2, ft.Colors.GREEN_300)
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

    def show_digital_art(self):
        self.page.views.clear()
        
        digital_topics = [
            {
                "title": "🖥️ Digital Art Basics",
                "content": "Digital art uses technology as a creative medium while applying traditional art principles:\n\n• Raster vs Vector: Pixels (photos, painting) vs mathematical curves (logos, illustrations)\n• Resolution: Higher DPI for print, lower for web\n• Color Modes: RGB for screens, CMYK for printing\n• File Formats: PNG for transparency, JPEG for photos, SVG for vectors\n• Hardware: Graphics tablet, stylus, powerful computer",
                "software": ["Free: GIMP, Krita, Blender", "Paid: Photoshop, Illustrator, Procreate"]
            },
            {
                "title": "🎨 Digital Painting Techniques", 
                "content": "Digital painting combines traditional techniques with digital advantages:\n\n• Layers: Non-destructive editing, separate elements\n• Brushes: Customize texture, opacity, and behavior\n• Blending Modes: Multiply, overlay, screen for different effects\n• Masks: Hide/reveal parts without destroying pixels\n• Undo History: Experiment freely with unlimited undos",
                "software": ["Beginner: Krita (free), Procreate (iPad)", "Professional: Photoshop, Corel Painter"]
            },
            {
                "title": "📐 Vector Graphics Design",
                "content": "Vector graphics use mathematical equations to create scalable artwork:\n\n• Scalability: Infinite zoom without quality loss\n• Anchor Points: Control curves and shapes precisely\n• Typography: Perfect for logos and text-based designs\n• Clean Lines: Ideal for icons, illustrations, logos\n• Small File Sizes: Efficient for web graphics",
                "software": ["Free: Inkscape", "Professional: Illustrator, Figma"]
            },
            {
                "title": "🎬 Motion Graphics & 3D",
                "content": "Bring your art to life with animation and 3D modeling:\n\n• 2D Animation: Frame-by-frame or tweening\n• Motion Graphics: Animated text, logos, infographics\n• 3D Modeling: Create objects in virtual space\n• Texturing: Apply materials and lighting\n• Rendering: Convert 3D scenes to 2D images",
                "software": ["2D: After Effects, Toon Boom", "3D: Blender (free), Maya, Cinema 4D"]
            }
        ]
        
        topic_cards = []
        for topic in digital_topics:
            software_text = "\n".join(topic["software"])
            
            card = ft.ExpansionTile(
                title=ft.Text(topic["title"], size=16, weight=ft.FontWeight.BOLD),
                subtitle=ft.Text("Tap to explore digital art techniques"),
                controls=[
                    ft.Container(
                        ft.Column([
                            ft.Text(topic["content"], size=14),
                            ft.Text("💻 Software Options:", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.DEEP_PURPLE_700),
                            ft.Text(software_text, size=13, color=ft.Colors.DEEP_PURPLE_600)
                        ], spacing=10),
                        padding=15,
                        bgcolor=ft.Colors.DEEP_PURPLE_50,
                        border_radius=8
                    )
                ]
            )
            topic_cards.append(card)
        
        view = ft.View(
            "/art_design/digital_art",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/art_design")),
                    title=ft.Text("Digital Art Studio"),
                    bgcolor=ft.Colors.DEEP_PURPLE_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("💻 Digital Art Mastery", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.DEEP_PURPLE_900),
                        ft.Text("Explore digital creativity while applying traditional art principles", size=16, color=ft.Colors.DEEP_PURPLE_700),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("🎯 Digital Art Advantages:", size=16, weight=ft.FontWeight.BOLD),
                                ft.Text("• Unlimited colors and materials at no extra cost", size=14),
                                ft.Text("• Layers allow non-destructive experimentation", size=14),  
                                ft.Text("• Infinite undo lets you explore freely", size=14),
                                ft.Text("• Easy sharing and reproduction", size=14),
                                ft.Text("• Integration with traditional techniques", size=14),
                                ft.Text("Remember: Digital tools are just that - tools. Fundamental art skills still apply!", size=13, style=ft.TextStyle(italic=True))
                            ], spacing=5),
                            bgcolor=ft.Colors.BLUE_50,
                            border_radius=8,
                            padding=15,
                            border=ft.border.all(1, ft.Colors.BLUE_200),
                            margin=ft.margin.only(bottom=20)
                        ),
                        
                        ft.Column(topic_cards, spacing=10),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("🚀 Getting Started Project", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_900),
                                ft.Text("Create a simple digital self-portrait:", size=14),
                                ft.Text("1. Download free software (Krita, GIMP, or use phone app)", size=13),
                                ft.Text("2. Set up canvas: 1000x1000 pixels, 300 DPI", size=13),
                                ft.Text("3. Create background layer with solid color", size=13),
                                ft.Text("4. Add new layer for sketch using basic shapes", size=13),
                                ft.Text("5. Use separate layers for hair, eyes, clothing", size=13),
                                ft.Text("6. Experiment with different brushes and effects", size=13),
                                ft.Text("7. Save in native format (.kra, .xcf) AND export as PNG", size=13)
                            ], spacing=5),
                            bgcolor=ft.Colors.GREEN_50,
                            border_radius=10,
                            padding=15,
                            border=ft.border.all(2, ft.Colors.GREEN_300)
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

def art_design_page(page: ft.Page):
    page.title = "Art & Design - Student AI Assistance"
    page.scroll = ft.ScrollMode.AUTO
    
    # Clear page content first
    page.clean()
    
    page.appbar = ft.AppBar(
        leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: page.go("/")),
        title=ft.Text("Art & Design Studio"),
        bgcolor=ft.Colors.PINK_700,
        center_title=True
    )
    
    module = ArtDesignModule(page)
    page.add(module.create_main_view())