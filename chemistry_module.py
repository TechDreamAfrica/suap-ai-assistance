import flet as ft
import random
import math

def get_ai_help(query, topic="chemistry"):
    """AI help response for Chemistry"""
    try:
        responses = {
            "atoms": "Atoms are the basic building blocks of matter. They consist of a nucleus (containing protons and neutrons) surrounded by electrons. The number of protons determines the element. Atoms can bond together to form molecules and compounds.",
            "elements": "Elements are pure substances made of only one type of atom. They are organized in the periodic table by atomic number. Each element has unique properties like atomic mass, electron configuration, and chemical behavior.",
            "compounds": "Compounds are substances made of two or more different elements chemically bonded together. They have different properties from their component elements. Examples include water (H₂O), salt (NaCl), and carbon dioxide (CO₂).",
            "reactions": "Chemical reactions occur when atoms rearrange to form new substances. They involve breaking and forming chemical bonds. Reactions can be synthesis (combining), decomposition (breaking apart), or displacement (exchanging atoms).",
            "acids": "Acids are substances that donate hydrogen ions (H⁺) in solution. They have a pH less than 7, taste sour, and react with metals and bases. Common acids include hydrochloric acid (HCl), sulfuric acid (H₂SO₄), and citric acid.",
            "bases": "Bases are substances that accept hydrogen ions or donate hydroxide ions (OH⁻). They have a pH greater than 7, feel slippery, and neutralize acids. Common bases include sodium hydroxide (NaOH) and ammonia (NH₃).",
            "periodic": "The periodic table organizes elements by atomic number and shows patterns in properties. Elements in the same column (group) have similar properties. It helps predict how elements will behave and what compounds they'll form.",
            "bonds": "Chemical bonds hold atoms together in compounds. Ionic bonds form between metals and nonmetals (electron transfer). Covalent bonds form between nonmetals (electron sharing). Metallic bonds occur in metals (electron sea).",
            "molecules": "Molecules are groups of atoms bonded together. They can be elements (O₂, N₂) or compounds (H₂O, CO₂). Molecular shape affects properties. Polar molecules have uneven charge distribution, while nonpolar molecules have even distribution.",
            "states": "Matter exists in different states: solid (fixed shape and volume), liquid (fixed volume, variable shape), gas (variable shape and volume), and plasma (ionized gas). State changes occur with energy changes."
        }
        
        query_lower = query.lower()
        for key, response in responses.items():
            if key in query_lower:
                return f"🤖 AI Helper: {response}"
        
        return "🤖 AI Helper: Chemistry studies matter and its properties, composition, and reactions. Ask about atoms, elements, compounds, reactions, acids, bases, or bonds for specific help!"
    except Exception:
        return "🤖 AI Helper: I'm here to help with chemistry concepts! Try asking about atoms, elements, compounds, or chemical reactions."

class ChemistryModule:
    def __init__(self, page):
        self.page = page
        self.current_quiz_level = "basic"
        self.quiz_score = 0
        self.quiz_question_index = 0
        
        # Quiz questions
        self.quiz_questions = {
            "basic": [
                {
                    "question": "What is the basic unit of matter?",
                    "options": ["Molecule", "Atom", "Element", "Compound"],
                    "correct": 1,
                    "explanation": "Atoms are the basic building blocks of all matter. They cannot be broken down into simpler substances by chemical means."
                },
                {
                    "question": "What is the chemical symbol for water?",
                    "options": ["H₂O", "HO", "H₂O₂", "OH"],
                    "correct": 0,
                    "explanation": "Water is H₂O, meaning it has 2 hydrogen atoms and 1 oxygen atom bonded together."
                },
                {
                    "question": "What determines an element's identity?",
                    "options": ["Number of electrons", "Number of protons", "Number of neutrons", "Atomic mass"],
                    "correct": 1,
                    "explanation": "The number of protons (atomic number) determines what element an atom is. This never changes for a given element."
                }
            ],
            "intermediate": [
                {
                    "question": "What type of bond forms between a metal and nonmetal?",
                    "options": ["Covalent", "Ionic", "Metallic", "Hydrogen"],
                    "correct": 1,
                    "explanation": "Ionic bonds form when metals transfer electrons to nonmetals, creating charged ions that attract each other."
                },
                {
                    "question": "What is the pH of a neutral solution?",
                    "options": ["0", "7", "14", "1"],
                    "correct": 1,
                    "explanation": "A neutral solution has a pH of 7. Solutions with pH less than 7 are acidic, greater than 7 are basic."
                },
                {
                    "question": "What happens during a chemical reaction?",
                    "options": ["Atoms are destroyed", "Atoms are created", "Bonds are broken and formed", "Nothing changes"],
                    "correct": 2,
                    "explanation": "In chemical reactions, chemical bonds are broken and new bonds form, but atoms are neither created nor destroyed."
                }
            ],
            "advanced": [
                {
                    "question": "What is Avogadro's number approximately?",
                    "options": ["6.02 × 10²³", "3.14 × 10⁸", "9.81 × 10⁹", "1.60 × 10¹⁹"],
                    "correct": 0,
                    "explanation": "Avogadro's number (6.02 × 10²³) is the number of particles in one mole of a substance."
                },
                {
                    "question": "What is the electron configuration of carbon?",
                    "options": ["1s² 2s² 2p²", "1s² 2s² 2p⁶", "1s² 2s⁴", "1s² 2p⁴"],
                    "correct": 0,
                    "explanation": "Carbon has 6 electrons: 2 in the 1s orbital, 2 in the 2s orbital, and 2 in the 2p orbitals."
                },
                {
                    "question": "What is the molarity of a solution with 2 moles of solute in 1 liter of solution?",
                    "options": ["1 M", "2 M", "3 M", "0.5 M"],
                    "correct": 1,
                    "explanation": "Molarity = moles of solute / liters of solution = 2 mol / 1 L = 2 M"
                }
            ]
        }

    def create_main_view(self):
        return ft.Container(
            ft.Column([
                ft.Text("🧪 Chemistry", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_900, text_align=ft.TextAlign.CENTER),
                ft.Text("Explore chemical reactions, formulas, and laboratory experiments", size=16, color=ft.Colors.GREEN_700, text_align=ft.TextAlign.CENTER),
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
                                ft.Icon(ft.Icons.CALCULATE, size=30, color=ft.Colors.ORANGE_700),
                                ft.Text("Calculator", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_calculator(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.ORANGE_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                ], spacing=10, run_spacing=10),
                
                ft.Divider(height=20),
                
                # Quick overview
                ft.Container(
                    ft.Column([
                        ft.Text("📚 Chemistry Overview", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_800),
                        ft.Text("Chemistry is the science that studies matter, its properties, and how it changes.", size=14),
                        ft.Text("⚗️ Key Topics:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
                        ft.Column([
                            ft.Text("• Atoms and Elements", size=14),
                            ft.Text("• Chemical Bonds and Compounds", size=14),
                            ft.Text("• Chemical Reactions", size=14),
                            ft.Text("• Acids, Bases, and pH", size=14),
                        ], spacing=5)
                    ], spacing=10),
                    bgcolor=ft.Colors.GREEN_50,
                    border_radius=10,
                    padding=15,
                    border=ft.border.all(2, ft.Colors.GREEN_200)
                )
            ], spacing=20),
            padding=20,
            expand=True
        )

    def show_ai_help(self):
        self.page.views.clear()
        
        query_field = ft.TextField(
            label="Ask about chemistry...",
            hint_text="e.g., What are atoms made of?",
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
            "/chemistry/ai_help",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/chemistry")),
                    title=ft.Text("AI Chemistry Help"),
                    bgcolor=ft.Colors.GREEN_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("🤖 AI Chemistry Assistant", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_900),
                        query_field,
                        ft.ElevatedButton(
                            "Get Help",
                            on_click=handle_query,
                            style=ft.ButtonStyle(bgcolor=ft.Colors.GREEN_600, color=ft.Colors.WHITE)
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
            "/chemistry/quizzes",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/chemistry")),
                    title=ft.Text("Chemistry Quizzes"),
                    bgcolor=ft.Colors.GREEN_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("📝 Choose Quiz Level", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_900),
                        
                        ft.ResponsiveRow([
                            ft.Container(
                                ft.ElevatedButton(
                                    content=ft.Column([
                                        ft.Icon(ft.Icons.LOOKS_ONE, size=30, color=ft.Colors.GREEN_700),
                                        ft.Text("Basic", size=16, weight=ft.FontWeight.BOLD),
                                        ft.Text("Atoms & molecules", size=12)
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
                                        ft.Text("Bonds & reactions", size=12)
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
                                        ft.Text("Calculations", size=12)
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
            "/chemistry/quiz_question",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/chemistry/quizzes")),
                    title=ft.Text(f"Quiz - Question {self.quiz_question_index + 1}"),
                    bgcolor=ft.Colors.GREEN_700
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
            "/chemistry/quiz_explanation",
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
            "/chemistry/quiz_results",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/chemistry")),
                    title=ft.Text("Quiz Results"),
                    bgcolor=ft.Colors.GREEN_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("Quiz Complete!", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_900),
                        ft.Text(f"Score: {self.quiz_score}/{total_questions} ({percentage:.0f}%)", size=20),
                        ft.Text(message, size=18, color=color, weight=ft.FontWeight.BOLD),
                        ft.ElevatedButton(
                            "Try Again",
                            on_click=lambda e: self.start_quiz(self.current_quiz_level),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.GREEN_600, color=ft.Colors.WHITE)
                        ),
                        ft.ElevatedButton(
                            "Back to Chemistry",
                            on_click=lambda e: self.page.go("/chemistry")
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
                "title": "⚛️ Atoms and Elements",
                "content": "Atoms are the basic building blocks of matter:\n\n• **Nucleus**: Contains protons (+) and neutrons (neutral)\n• **Electrons**: Negatively charged particles orbiting the nucleus\n• **Atomic Number**: Number of protons, determines element identity\n• **Mass Number**: Protons + neutrons\n\n**Elements** are pure substances with only one type of atom. The periodic table organizes elements by properties."
            },
            {
                "title": "🔗 Chemical Bonds",
                "content": "Chemical bonds hold atoms together:\n\n• **Ionic Bonds**: Electrons transferred from metal to nonmetal\n• **Covalent Bonds**: Electrons shared between nonmetals\n• **Metallic Bonds**: Electrons shared in a 'sea' around metal atoms\n\n**Polarity**: Unequal sharing creates polar molecules (like water). Equal sharing creates nonpolar molecules."
            },
            {
                "title": "⚗️ Chemical Reactions",
                "content": "Chemical reactions rearrange atoms to form new substances:\n\n• **Reactants**: Starting materials\n• **Products**: New substances formed\n• **Conservation**: Atoms are neither created nor destroyed\n• **Types**: Synthesis (A + B → AB), Decomposition (AB → A + B), Displacement\n\n**Balancing**: Chemical equations must have equal atoms on both sides."
            },
            {
                "title": "🧪 Acids, Bases, and pH",
                "content": "Acids and bases are important chemical groups:\n\n• **Acids**: Donate H⁺ ions, pH < 7, taste sour\n• **Bases**: Accept H⁺ ions, pH > 7, feel slippery\n• **Neutral**: pH = 7 (pure water)\n• **pH Scale**: 0-14, measures acidity/basicity\n\n**Neutralization**: Acid + Base → Salt + Water"
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
                        bgcolor=ft.Colors.GREEN_50,
                        border_radius=8
                    )
                ]
            )
            explanation_cards.append(card)
        
        view = ft.View(
            "/chemistry/explanations",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/chemistry")),
                    title=ft.Text("Chemistry Concepts"),
                    bgcolor=ft.Colors.GREEN_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("📚 Learn Chemistry", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_900),
                        ft.Text("Explore the fundamental concepts of chemistry", size=16, color=ft.Colors.GREEN_700),
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

    def show_calculator(self):
        self.page.views.clear()
        
        # Calculator inputs
        moles_field = ft.TextField(label="Moles", value="", width=150)
        volume_field = ft.TextField(label="Volume (L)", value="", width=150)
        mass_field = ft.TextField(label="Mass (g)", value="", width=150)
        molar_mass_field = ft.TextField(label="Molar Mass (g/mol)", value="", width=150)
        
        result_text = ft.Text("", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_900)
        
        def calculate_molarity(e):
            try:
                moles = float(moles_field.value) if moles_field.value else 0
                volume = float(volume_field.value) if volume_field.value else 0
                if volume > 0:
                    molarity = moles / volume
                    result_text.value = f"Molarity: {molarity:.2f} M"
                else:
                    result_text.value = "Volume must be greater than 0"
                self.page.update()
            except ValueError:
                result_text.value = "Please enter valid numbers"
                self.page.update()
        
        def calculate_moles_from_mass(e):
            try:
                mass = float(mass_field.value) if mass_field.value else 0
                molar_mass = float(molar_mass_field.value) if molar_mass_field.value else 0
                if molar_mass > 0:
                    moles = mass / molar_mass
                    result_text.value = f"Moles: {moles:.3f} mol"
                else:
                    result_text.value = "Molar mass must be greater than 0"
                self.page.update()
            except ValueError:
                result_text.value = "Please enter valid numbers"
                self.page.update()
        
        def calculate_mass_from_moles(e):
            try:
                moles = float(moles_field.value) if moles_field.value else 0
                molar_mass = float(molar_mass_field.value) if molar_mass_field.value else 0
                mass = moles * molar_mass
                result_text.value = f"Mass: {mass:.2f} g"
                self.page.update()
            except ValueError:
                result_text.value = "Please enter valid numbers"
                self.page.update()
        
        view = ft.View(
            "/chemistry/calculator",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/chemistry")),
                    title=ft.Text("Chemistry Calculator"),
                    bgcolor=ft.Colors.GREEN_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("🧮 Chemistry Calculator", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_900),
                        
                        ft.Text("Enter values and click calculate:", size=16),
                        
                        ft.ResponsiveRow([
                            ft.Container(moles_field, col={'xs': 12, 'sm': 6, 'md': 3}),
                            ft.Container(volume_field, col={'xs': 12, 'sm': 6, 'md': 3}),
                            ft.Container(mass_field, col={'xs': 12, 'sm': 6, 'md': 3}),
                            ft.Container(molar_mass_field, col={'xs': 12, 'sm': 6, 'md': 3}),
                        ], spacing=10),
                        
                        ft.Divider(height=20),
                        
                        ft.ResponsiveRow([
                            ft.Container(
                                ft.ElevatedButton(
                                    "Calculate\nMolarity",
                                    on_click=calculate_molarity,
                                    style=ft.ButtonStyle(bgcolor=ft.Colors.BLUE_600, color=ft.Colors.WHITE, padding=15)
                                ),
                                col={'xs': 12, 'sm': 6, 'md': 4}
                            ),
                            ft.Container(
                                ft.ElevatedButton(
                                    "Mass to\nMoles",
                                    on_click=calculate_moles_from_mass,
                                    style=ft.ButtonStyle(bgcolor=ft.Colors.GREEN_600, color=ft.Colors.WHITE, padding=15)
                                ),
                                col={'xs': 12, 'sm': 6, 'md': 4}
                            ),
                            ft.Container(
                                ft.ElevatedButton(
                                    "Moles to\nMass",
                                    on_click=calculate_mass_from_moles,
                                    style=ft.ButtonStyle(bgcolor=ft.Colors.ORANGE_600, color=ft.Colors.WHITE, padding=15)
                                ),
                                col={'xs': 12, 'sm': 6, 'md': 4}
                            ),
                        ], spacing=10),
                        
                        ft.Divider(height=20),
                        
                        ft.Container(
                            result_text,
                            bgcolor=ft.Colors.GREEN_50,
                            border_radius=10,
                            padding=20,
                            border=ft.border.all(2, ft.Colors.GREEN_200)
                        )
                    ], spacing=15),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

def chemistry_page(page: ft.Page):
    page.title = "Chemistry - Student AI Assistance"
    page.scroll = ft.ScrollMode.AUTO
    
    # Clear page content first
    page.clean()
    
    page.appbar = ft.AppBar(
        leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: page.go("/")),
        title=ft.Text("Chemistry"),
        bgcolor=ft.Colors.GREEN_700,
        center_title=True
    )
    
    module = ChemistryModule(page)
    page.add(module.create_main_view())
