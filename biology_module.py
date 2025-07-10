import flet as ft
import random

def get_ai_help(query, topic="biology"):
    """AI help response for Biology"""
    try:
        responses = {
            "cells": "Cells are the basic units of life. All living things are made of cells. Prokaryotic cells (bacteria) lack a nucleus, while eukaryotic cells (plants, animals, fungi) have a nucleus. Cells contain organelles like mitochondria, ribosomes, and chloroplasts (in plants).",
            "dna": "DNA (deoxyribonucleic acid) carries genetic information. It's made of nucleotides with bases A, T, G, C. DNA is found in the nucleus and determines traits. It replicates during cell division and codes for proteins through transcription and translation.",
            "evolution": "Evolution is the change in species over time. It occurs through natural selection, where organisms with favorable traits survive and reproduce more. Evidence includes fossils, DNA similarities, and observed changes in populations.",
            "ecosystem": "An ecosystem includes all living things and their environment in an area. It has producers (plants), consumers (animals), and decomposers (bacteria, fungi). Energy flows through food chains, and nutrients cycle through the ecosystem.",
            "photosynthesis": "Photosynthesis is how plants make food using sunlight. The equation is: 6CO₂ + 6H₂O + light energy → C₆H₁₂O₆ + 6O₂. It occurs in chloroplasts and produces glucose and oxygen. This process is essential for life on Earth.",
            "genetics": "Genetics is the study of heredity. Genes are sections of DNA that code for traits. Alleles are different versions of genes. Dominant alleles mask recessive ones. Genetic crosses can predict offspring traits using Punnett squares.",
            "anatomy": "Anatomy is the study of body structure. Humans have organ systems: circulatory (heart, blood), respiratory (lungs), digestive (stomach, intestines), nervous (brain, nerves), and others. Each system has specific functions.",
            "ecology": "Ecology studies relationships between organisms and their environment. It includes populations (same species), communities (different species), and ecosystems. Interactions include predation, competition, symbiosis, and food webs."
        }
        
        query_lower = query.lower()
        for key, response in responses.items():
            if key in query_lower:
                return f"🤖 AI Helper: {response}"
        
        return "🤖 AI Helper: Biology is the study of living things. Ask about cells, DNA, evolution, ecosystems, photosynthesis, genetics, anatomy, or ecology for specific help!"
    except Exception:
        return "🤖 AI Helper: I'm here to help with biology concepts! Try asking about cells, DNA, evolution, or ecosystems."

class BiologyModule:
    def __init__(self, page):
        self.page = page
        self.current_quiz_level = "basic"
        self.quiz_score = 0
        self.quiz_question_index = 0
        
        # Quiz questions
        self.quiz_questions = {
            "basic": [
                {
                    "question": "What is the basic unit of life?",
                    "options": ["Atom", "Molecule", "Cell", "Tissue"],
                    "correct": 2,
                    "explanation": "Cells are the basic units of life. All living things are made of one or more cells."
                },
                {
                    "question": "What do plants use to make food?",
                    "options": ["Photosynthesis", "Respiration", "Digestion", "Circulation"],
                    "correct": 0,
                    "explanation": "Plants use photosynthesis to convert sunlight, water, and carbon dioxide into glucose (food) and oxygen."
                },
                {
                    "question": "Where is DNA found in animal cells?",
                    "options": ["Cytoplasm", "Nucleus", "Mitochondria", "Ribosomes"],
                    "correct": 1,
                    "explanation": "DNA is found in the nucleus of animal cells. It contains the genetic instructions for the organism."
                }
            ],
            "intermediate": [
                {
                    "question": "What is the powerhouse of the cell?",
                    "options": ["Nucleus", "Ribosome", "Mitochondria", "Chloroplast"],
                    "correct": 2,
                    "explanation": "Mitochondria are called the powerhouse of the cell because they produce ATP (energy) through cellular respiration."
                },
                {
                    "question": "Which type of reproduction produces genetically identical offspring?",
                    "options": ["Sexual", "Asexual", "Both", "Neither"],
                    "correct": 1,
                    "explanation": "Asexual reproduction produces genetically identical offspring because only one parent contributes genetic material."
                },
                {
                    "question": "What is the role of decomposers in an ecosystem?",
                    "options": ["Produce food", "Eat plants", "Break down dead matter", "Provide oxygen"],
                    "correct": 2,
                    "explanation": "Decomposers break down dead organic matter, recycling nutrients back into the ecosystem."
                }
            ],
            "advanced": [
                {
                    "question": "What is the complementary base to adenine in DNA?",
                    "options": ["Guanine", "Cytosine", "Thymine", "Uracil"],
                    "correct": 2,
                    "explanation": "In DNA, adenine pairs with thymine, and guanine pairs with cytosine. These are complementary base pairs."
                },
                {
                    "question": "What is the primary difference between prokaryotic and eukaryotic cells?",
                    "options": ["Size", "Nucleus", "Cell wall", "Ribosomes"],
                    "correct": 1,
                    "explanation": "Prokaryotic cells lack a membrane-bound nucleus, while eukaryotic cells have a nucleus surrounded by a membrane."
                },
                {
                    "question": "What is the end product of glycolysis?",
                    "options": ["Glucose", "Pyruvate", "ATP", "Oxygen"],
                    "correct": 1,
                    "explanation": "Glycolysis breaks down glucose into two molecules of pyruvate, producing ATP and NADH in the process."
                }
            ]
        }

    def create_main_view(self):
        return ft.Container(
            ft.Column([
                ft.Text("🌱 Biology", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.TEAL_900, text_align=ft.TextAlign.CENTER),
                ft.Text("Discover life sciences, anatomy, ecology, and biological processes", size=16, color=ft.Colors.TEAL_700, text_align=ft.TextAlign.CENTER),
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
                                ft.Icon(ft.Icons.BIOTECH, size=30, color=ft.Colors.ORANGE_700),
                                ft.Text("Lab", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_virtual_lab(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.ORANGE_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                ], spacing=10, run_spacing=10),
                
                ft.Divider(height=20),
                
                # Quick overview
                ft.Container(
                    ft.Column([
                        ft.Text("📚 Biology Overview", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.TEAL_800),
                        ft.Text("Biology is the study of living things and how they interact with their environment.", size=14),
                        ft.Text("🔬 Key Topics:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.TEAL_700),
                        ft.Column([
                            ft.Text("• Cells and Genetics", size=14),
                            ft.Text("• Evolution and Ecology", size=14),
                            ft.Text("• Human Anatomy and Physiology", size=14),
                            ft.Text("• Photosynthesis and Respiration", size=14),
                        ], spacing=5)
                    ], spacing=10),
                    bgcolor=ft.Colors.TEAL_50,
                    border_radius=10,
                    padding=15,
                    border=ft.border.all(2, ft.Colors.TEAL_200)
                )
            ], spacing=20),
            padding=20,
            expand=True
        )

    def show_ai_help(self):
        self.page.views.clear()
        
        query_field = ft.TextField(
            label="Ask about biology...",
            hint_text="e.g., How do cells divide?",
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
            "/biology/ai_help",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/biology")),
                    title=ft.Text("AI Biology Help"),
                    bgcolor=ft.Colors.TEAL_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("🤖 AI Biology Assistant", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.TEAL_900),
                        query_field,
                        ft.ElevatedButton(
                            "Get Help",
                            on_click=handle_query,
                            style=ft.ButtonStyle(bgcolor=ft.Colors.TEAL_600, color=ft.Colors.WHITE)
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
            "/biology/quizzes",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/biology")),
                    title=ft.Text("Biology Quizzes"),
                    bgcolor=ft.Colors.TEAL_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("📝 Choose Quiz Level", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.TEAL_900),
                        
                        ft.ResponsiveRow([
                            ft.Container(
                                ft.ElevatedButton(
                                    content=ft.Column([
                                        ft.Icon(ft.Icons.LOOKS_ONE, size=30, color=ft.Colors.GREEN_700),
                                        ft.Text("Basic", size=16, weight=ft.FontWeight.BOLD),
                                        ft.Text("Cells & life", size=12)
                                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                                    on_click=lambda e: self.start_quiz("basic"),
                                    style=ft.ButtonStyle(padding=20, bgcolor=ft.Colors.GREEN_50, shape=ft.RoundedRectangleBorder(radius=10))
                                ),
                                col={'xs': 12, 'sm': 6, 'md': 4}
                            ),
                            ft.Container(
                                ft.ElevatedButton(
                                    content=ft.Column([
                                        ft.Icon(ft.Icons.LOOKS_TWO, size=30, color=ft.Colors.ORANGE_700),
                                        ft.Text("Intermediate", size=16, weight=ft.FontWeight.BOLD),
                                        ft.Text("Ecology & genetics", size=12)
                                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                                    on_click=lambda e: self.start_quiz("intermediate"),
                                    style=ft.ButtonStyle(padding=20, bgcolor=ft.Colors.ORANGE_50, shape=ft.RoundedRectangleBorder(radius=10))
                                ),
                                col={'xs': 12, 'sm': 6, 'md': 4}
                            ),
                            ft.Container(
                                ft.ElevatedButton(
                                    content=ft.Column([
                                        ft.Icon(ft.Icons.LOOKS_3, size=30, color=ft.Colors.RED_700),
                                        ft.Text("Advanced", size=16, weight=ft.FontWeight.BOLD),
                                        ft.Text("Molecular biology", size=12)
                                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                                    on_click=lambda e: self.start_quiz("advanced"),
                                    style=ft.ButtonStyle(padding=20, bgcolor=ft.Colors.RED_50, shape=ft.RoundedRectangleBorder(radius=10))
                                ),
                                col={'xs': 12, 'sm': 6, 'md': 4}
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
            "/biology/quiz_question",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/biology/quizzes")),
                    title=ft.Text(f"Quiz - Question {self.quiz_question_index + 1}"),
                    bgcolor=ft.Colors.TEAL_700
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
            "/biology/quiz_explanation",
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
            "/biology/quiz_results",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/biology")),
                    title=ft.Text("Quiz Results"),
                    bgcolor=ft.Colors.TEAL_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("Quiz Complete!", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.TEAL_900),
                        ft.Text(f"Score: {self.quiz_score}/{total_questions} ({percentage:.0f}%)", size=20),
                        ft.Text(message, size=18, color=color, weight=ft.FontWeight.BOLD),
                        ft.ElevatedButton(
                            "Try Again",
                            on_click=lambda e: self.start_quiz(self.current_quiz_level),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.TEAL_600, color=ft.Colors.WHITE)
                        ),
                        ft.ElevatedButton(
                            "Back to Biology",
                            on_click=lambda e: self.page.go("/biology")
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
                "title": "🔬 Cells and Life",
                "content": "Cells are the basic units of life:\n\n• **Cell Types**: Prokaryotic (no nucleus) vs Eukaryotic (has nucleus)\n• **Cell Parts**: Nucleus (DNA), mitochondria (energy), ribosomes (proteins)\n• **Cell Division**: Mitosis (growth) and meiosis (reproduction)\n• **Cell Membrane**: Controls what enters and exits\n\n**Plant vs Animal**: Plants have cell walls and chloroplasts, animals have centrioles"
            },
            {
                "title": "🧬 Genetics and DNA",
                "content": "Genetics is the study of heredity:\n\n• **DNA**: Genetic material with bases A, T, G, C\n• **Genes**: Sections of DNA that code for traits\n• **Chromosomes**: Structures containing DNA\n• **Heredity**: Traits passed from parents to offspring\n\n**Mendel's Laws**: Dominant and recessive alleles determine traits"
            },
            {
                "title": "🌿 Photosynthesis and Respiration",
                "content": "How organisms get and use energy:\n\n• **Photosynthesis**: Plants make glucose using sunlight\n  - 6CO₂ + 6H₂O + light → C₆H₁₂O₆ + 6O₂\n• **Cellular Respiration**: Cells break down glucose for energy\n  - C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O + ATP\n\n**Energy Flow**: Sun → Plants → Animals → Decomposers"
            },
            {
                "title": "🌍 Evolution and Ecology",
                "content": "How life changes and interacts:\n\n• **Evolution**: Change in species over time\n• **Natural Selection**: Survival of the fittest\n• **Ecosystems**: Living and non-living things interacting\n• **Food Chains**: Energy flow from producers to consumers\n\n**Biodiversity**: Variety of life supports ecosystem stability"
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
                        bgcolor=ft.Colors.TEAL_50,
                        border_radius=8
                    )
                ]
            )
            explanation_cards.append(card)
        
        view = ft.View(
            "/biology/explanations",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/biology")),
                    title=ft.Text("Biology Concepts"),
                    bgcolor=ft.Colors.TEAL_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("📚 Learn Biology", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.TEAL_900),
                        ft.Text("Explore the fundamental concepts of biology", size=16, color=ft.Colors.TEAL_700),
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

    def show_virtual_lab(self):
        self.page.views.clear()
        
        experiments = [
            {
                "title": "🔬 Microscopy",
                "description": "Observe different cell types under the microscope",
                "procedure": "1. Prepare slide\n2. Focus microscope\n3. Observe structures\n4. Draw what you see"
            },
            {
                "title": "🌱 Photosynthesis",
                "description": "Test the factors affecting photosynthesis rate",
                "procedure": "1. Set up plant in light\n2. Count oxygen bubbles\n3. Change light intensity\n4. Record results"
            },
            {
                "title": "🧬 DNA Extraction",
                "description": "Extract DNA from fruits using household items",
                "procedure": "1. Mash fruit\n2. Add soap and salt\n3. Filter mixture\n4. Add alcohol to see DNA"
            },
            {
                "title": "🦋 Genetics",
                "description": "Use Punnett squares to predict inheritance",
                "procedure": "1. Choose parent traits\n2. Set up Punnett square\n3. Fill in combinations\n4. Calculate probabilities"
            }
        ]
        
        experiment_cards = []
        for exp in experiments:
            card = ft.Container(
                ft.Column([
                    ft.Text(exp["title"], size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.TEAL_900),
                    ft.Text(exp["description"], size=14, color=ft.Colors.TEAL_700),
                    ft.ExpansionTile(
                        title=ft.Text("Procedure", size=14, weight=ft.FontWeight.BOLD),
                        controls=[
                            ft.Container(
                                ft.Text(exp["procedure"], size=12),
                                padding=10,
                                bgcolor=ft.Colors.TEAL_50,
                                border_radius=5
                            )
                        ]
                    ),
                    ft.ElevatedButton(
                        "Start Experiment",
                        on_click=lambda e, title=exp["title"]: self.start_experiment(title),
                        style=ft.ButtonStyle(bgcolor=ft.Colors.TEAL_600, color=ft.Colors.WHITE)
                    )
                ], spacing=10),
                bgcolor=ft.Colors.TEAL_50,
                border_radius=10,
                padding=15,
                border=ft.border.all(1, ft.Colors.TEAL_200)
            )
            experiment_cards.append(card)
        
        view = ft.View(
            "/biology/virtual_lab",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/biology")),
                    title=ft.Text("Virtual Biology Lab"),
                    bgcolor=ft.Colors.TEAL_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("🧪 Virtual Lab", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.TEAL_900),
                        ft.Text("Conduct virtual biology experiments", size=16, color=ft.Colors.TEAL_700),
                        ft.Column(experiment_cards, spacing=15)
                    ], spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def start_experiment(self, experiment_title):
        self.page.show_snack_bar(
            ft.SnackBar(content=ft.Text(f"Virtual experiment '{experiment_title}' will be available soon!"))
        )

def biology_page(page: ft.Page):
    page.title = "Biology - Student AI Assistance"
    page.scroll = ft.ScrollMode.AUTO
    
    # Clear page content first
    page.clean()
    
    page.appbar = ft.AppBar(
        leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: page.go("/")),
        title=ft.Text("Biology"),
        bgcolor=ft.Colors.TEAL_700,
        center_title=True
    )
    
    module = BiologyModule(page)
    page.add(module.create_main_view())
