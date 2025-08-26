import flet as ft
import random
import math

def get_physics_ai_help(query, topic="physics"):
    """AI help for Physics concepts"""
    try:
        responses = {
            "force": "Force is a push or pull that can change an object's motion. Measured in Newtons (N). Newton's laws describe how forces affect motion: F = ma (Force = mass × acceleration).",
            "motion": "Motion is change in position over time. Key concepts: speed (distance/time), velocity (speed with direction), acceleration (change in velocity/time). Remember: velocity and acceleration are vectors.",
            "energy": "Energy is the ability to do work. Types include kinetic (motion), potential (stored), thermal, chemical, electrical. Energy is conserved - it changes forms but isn't created or destroyed.",
            "gravity": "Gravity is the attractive force between masses. On Earth, g ≈ 9.8 m/s². Weight = mg. Objects fall at the same rate in vacuum regardless of mass (ignoring air resistance).",
            "momentum": "Momentum = mass × velocity (p = mv). In collisions, total momentum is conserved. Impulse = change in momentum = force × time.",
            "wave": "Waves transfer energy without transferring matter. Key properties: wavelength, frequency, amplitude, speed. Wave speed = frequency × wavelength.",
            "electricity": "Electric current is moving charge. Voltage is electrical pressure, current is flow rate, resistance opposes flow. Ohm's Law: V = IR.",
            "magnet": "Magnetic fields surround magnets and moving charges. Like poles repel, opposite poles attract. Moving charges create magnetic fields; changing magnetic fields create electric fields.",
            "heat": "Heat is energy transfer due to temperature difference. Temperature measures average kinetic energy of particles. Heat flows from hot to cold until thermal equilibrium.",
            "light": "Light is electromagnetic radiation. Behaves as both wave and particle. Properties: reflection, refraction, diffraction, interference. Speed in vacuum: 3×10⁸ m/s.",
        }
        
        query_lower = query.lower()
        for key, response in responses.items():
            if key in query_lower:
                return f"⚡ Physics Helper: {response}"
        
        return f"⚡ Physics Helper: I can help with forces, motion, energy, gravity, momentum, waves, electricity, magnetism, heat, light, and more physics concepts. Ask me about any physics topic!"
    except Exception:
        return f"⚡ Physics Helper: I'm here to help with physics! Ask about forces, energy, motion, or any physics concept."

class PhysicsModule:
    def __init__(self, page):
        self.page = page
        self.current_quiz_level = "basic"
        self.quiz_score = 0
        self.quiz_question_index = 0
        self.current_correct_index = 0
        self.current_shuffled_options = []
        
        # Comprehensive quiz questions
        self.quiz_questions = {
            "basic": [
                {"question": "What is the unit of force?", "options": ["Joule", "Newton", "Watt", "Pascal"], "correct": 1, "explanation": "Force is measured in Newtons (N), named after Isaac Newton."},
                {"question": "According to Newton's first law, an object at rest will:", "options": ["Start moving", "Stay at rest unless acted upon by a force", "Fall down", "Speed up"], "correct": 1, "explanation": "Newton's first law (law of inertia) states that objects at rest stay at rest unless acted upon by an unbalanced force."},
                {"question": "What is the formula for speed?", "options": ["Force × time", "Distance ÷ time", "Mass × acceleration", "Energy ÷ time"], "correct": 1, "explanation": "Speed = distance ÷ time. This tells us how far something travels in a given time period."},
                {"question": "Energy cannot be:", "options": ["Transferred", "Stored", "Created or destroyed", "Measured"], "correct": 2, "explanation": "The law of conservation of energy states that energy cannot be created or destroyed, only transferred or transformed."},
                {"question": "What happens to potential energy as a ball falls?", "options": ["Increases", "Stays the same", "Converts to kinetic energy", "Disappears"], "correct": 2, "explanation": "As a ball falls, gravitational potential energy converts to kinetic energy (motion energy)."},
                {"question": "Which has more momentum: a truck or a bicycle at the same speed?", "options": ["Truck", "Bicycle", "Same momentum", "Cannot tell"], "correct": 0, "explanation": "Momentum = mass × velocity. The truck has much more mass, so more momentum at the same speed."},
                {"question": "Sound travels fastest through:", "options": ["Air", "Water", "Steel", "Vacuum"], "correct": 2, "explanation": "Sound travels fastest through solids like steel because particles are closer together for transmitting vibrations."},
                {"question": "What causes electric current?", "options": ["Moving electrons", "Static charges", "Magnetic fields", "Heat"], "correct": 0, "explanation": "Electric current is the flow of moving electric charges, typically electrons in conductors."},
                {"question": "Like magnetic poles:", "options": ["Attract", "Repel", "Don't interact", "Create sparks"], "correct": 1, "explanation": "Like magnetic poles (north-north or south-south) repel each other, while opposite poles attract."},
                {"question": "Heat always flows from:", "options": ["Cold to hot", "Hot to cold", "Big to small", "Fast to slow"], "correct": 1, "explanation": "Heat always flows from higher temperature to lower temperature until thermal equilibrium is reached."}
            ],
            "intermediate": [
                {"question": "What is Newton's second law?", "options": ["F = ma", "Every action has an equal and opposite reaction", "Objects at rest stay at rest", "E = mc²"], "correct": 0, "explanation": "Newton's second law: Force equals mass times acceleration (F = ma)."},
                {"question": "A 5 kg object accelerates at 2 m/s². What force is applied?", "options": ["7 N", "10 N", "3 N", "2.5 N"], "correct": 1, "explanation": "Using F = ma: Force = 5 kg × 2 m/s² = 10 N."},
                {"question": "What is the difference between mass and weight?", "options": ["No difference", "Mass is matter amount, weight is gravitational force", "Weight is bigger", "Mass changes with location"], "correct": 1, "explanation": "Mass is the amount of matter (constant), weight is the gravitational force on that mass (varies with gravity)."},
                {"question": "What is work in physics?", "options": ["Any effort", "Force × distance", "Power × time", "Energy ÷ time"], "correct": 1, "explanation": "Work = force × distance moved in the direction of the force. Measured in Joules."},
                {"question": "If you double the speed of a car, its kinetic energy:", "options": ["Doubles", "Stays same", "Quadruples", "Halves"], "correct": 2, "explanation": "Kinetic energy = ½mv². If velocity doubles, energy increases by 2² = 4 times."},
                {"question": "What is frequency?", "options": ["Wave height", "Wave speed", "Number of waves per second", "Wave length"], "correct": 2, "explanation": "Frequency is the number of wave cycles that pass a point in one second, measured in Hertz (Hz)."},
                {"question": "According to Ohm's law, if voltage increases and resistance stays constant:", "options": ["Current decreases", "Current increases", "Current stays same", "Power decreases"], "correct": 1, "explanation": "Ohm's law: V = IR. If V increases and R is constant, then I (current) must increase."},
                {"question": "What happens to current if you add more resistance to a circuit?", "options": ["Increases", "Decreases", "Stays same", "Becomes zero"], "correct": 1, "explanation": "More resistance opposes current flow, so current decreases (V = IR, if R increases, I decreases)."},
                {"question": "Why do we see lightning before hearing thunder?", "options": ["Light is brighter", "Sound is quieter", "Light travels faster than sound", "Sound travels faster"], "correct": 2, "explanation": "Light travels at 3×10⁸ m/s while sound travels at about 343 m/s in air, so light reaches us first."},
                {"question": "What is the relationship between wavelength and frequency?", "options": ["Directly proportional", "Inversely proportional", "No relationship", "Always equal"], "correct": 1, "explanation": "Wave speed = frequency × wavelength. For constant wave speed, as frequency increases, wavelength decreases."}
            ],
            "advanced": [
                {"question": "What is centripetal acceleration?", "options": ["Acceleration in circles", "Acceleration toward center of circular motion", "Acceleration away from center", "Tangential acceleration"], "correct": 1, "explanation": "Centripetal acceleration is the acceleration directed toward the center of circular motion: a = v²/r."},
                {"question": "In projectile motion, what is true about horizontal and vertical components?", "options": ["Both change constantly", "Horizontal constant, vertical changes", "Vertical constant, horizontal changes", "Both are zero"], "correct": 1, "explanation": "Horizontal velocity is constant (no horizontal forces), while vertical velocity changes due to gravity."},
                {"question": "What is the relationship between electric and magnetic fields?", "options": ["Unrelated", "Changing electric fields create magnetic fields", "Always perpendicular", "Magnetic fields are stronger"], "correct": 1, "explanation": "Maxwell's equations show that changing electric fields create magnetic fields and vice versa - they're aspects of electromagnetic fields."},
                {"question": "What is the photoelectric effect?", "options": ["Light creating heat", "Light knocking electrons from materials", "Electrons creating light", "Heat creating electricity"], "correct": 1, "explanation": "The photoelectric effect occurs when light photons knock electrons from material surfaces, demonstrating light's particle nature."},
                {"question": "What is the uncertainty principle?", "options": ["We can't know everything", "Position and momentum can't both be precisely known", "Experiments always have errors", "Quantum effects are random"], "correct": 1, "explanation": "Heisenberg's uncertainty principle states that position and momentum of particles cannot both be precisely determined simultaneously."},
                {"question": "What is special about the speed of light?", "options": ["It's very fast", "It's constant in all reference frames", "It's the fastest speed", "It's electromagnetic"], "correct": 1, "explanation": "According to special relativity, the speed of light in vacuum is constant for all observers regardless of their motion."},
                {"question": "What is entropy?", "options": ["A type of energy", "Measure of disorder", "Heat capacity", "Electrical property"], "correct": 1, "explanation": "Entropy is a measure of disorder or randomness in a system. It tends to increase over time (second law of thermodynamics)."},
                {"question": "What is the difference between AC and DC current?", "options": ["AC is faster", "AC alternates direction, DC flows one way", "DC is safer", "No difference"], "correct": 1, "explanation": "AC (alternating current) changes direction periodically, while DC (direct current) flows in one direction."},
                {"question": "What is escape velocity?", "options": ["Maximum safe speed", "Speed to leave Earth's gravity", "Speed of light", "Orbital speed"], "correct": 1, "explanation": "Escape velocity is the minimum speed needed for an object to escape a celestial body's gravitational field permanently."},
                {"question": "What is the Doppler effect?", "options": ["Change in wave frequency due to relative motion", "Bending of light", "Wave interference", "Sound reflection"], "correct": 0, "explanation": "The Doppler effect is the change in wave frequency when the source or observer is moving relative to each other."}
            ]
        }

    def create_main_view(self):
        return ft.Container(
            ft.Column([
                ft.Text("⚡ Physics", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.INDIGO_900, text_align=ft.TextAlign.CENTER),
                ft.Text("Explore the fundamental laws governing the universe", size=16, color=ft.Colors.INDIGO_700, text_align=ft.TextAlign.CENTER),
                ft.Divider(height=30),
                
                # Navigation buttons
                ft.ResponsiveRow([
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.SCHOOL_OUTLINED, size=30, color=ft.Colors.BLUE_700),
                                ft.Text("Learn Physics", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_learning_content(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.BLUE_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.QUIZ_OUTLINED, size=30, color=ft.Colors.GREEN_700),
                                ft.Text("Physics Quiz", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_quizzes(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.GREEN_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.CALCULATE_OUTLINED, size=30, color=ft.Colors.ORANGE_700),
                                ft.Text("Physics Calculator", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_calculator(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.ORANGE_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.HELP_OUTLINE, size=30, color=ft.Colors.PURPLE_700),
                                ft.Text("AI Help", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_ai_help(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.PURPLE_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                ], spacing=10, run_spacing=10),
                
                ft.Divider(height=20),
                
                # Learning overview
                ft.Container(
                    ft.Column([
                        ft.Text("What You'll Learn", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800),
                        ft.Text("Understand the fundamental principles that govern how the universe works", size=14),
                        
                        ft.Text("Core Topics:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.INDIGO_700),
                        ft.Column([
                            ft.Text("🚀 Mechanics: Forces, motion, energy", size=14),
                            ft.Text("⚡ Electricity & Magnetism: Circuits, fields", size=14),
                            ft.Text("🌊 Waves & Sound: Properties, behavior", size=14),
                            ft.Text("💡 Light & Optics: Reflection, refraction", size=14),
                            ft.Text("🔥 Thermodynamics: Heat, temperature", size=14),
                            ft.Text("⚛️ Modern Physics: Quantum, relativity", size=14),
                        ], spacing=5),
                        
                        # Quick stats
                        ft.ResponsiveRow([
                            ft.Container(
                                ft.Column([
                                    ft.Icon(ft.Icons.QUIZ, size=25, color=ft.Colors.BLUE_700),
                                    ft.Text("30+", size=16, weight=ft.FontWeight.BOLD),
                                    ft.Text("Quiz Questions", size=12)
                                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                                bgcolor=ft.Colors.BLUE_50,
                                border_radius=10,
                                padding=10,
                                col={'xs': 6, 'sm': 3}
                            ),
                            ft.Container(
                                ft.Column([
                                    ft.Icon(ft.Icons.SCIENCE, size=25, color=ft.Colors.GREEN_700),
                                    ft.Text("6", size=16, weight=ft.FontWeight.BOLD),
                                    ft.Text("Major Areas", size=12)
                                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                                bgcolor=ft.Colors.GREEN_50,
                                border_radius=10,
                                padding=10,
                                col={'xs': 6, 'sm': 3}
                            ),
                            ft.Container(
                                ft.Column([
                                    ft.Icon(ft.Icons.CALCULATE, size=25, color=ft.Colors.PURPLE_700),
                                    ft.Text("Built-in", size=16, weight=ft.FontWeight.BOLD),
                                    ft.Text("Calculator", size=12)
                                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                                bgcolor=ft.Colors.PURPLE_50,
                                border_radius=10,
                                padding=10,
                                col={'xs': 6, 'sm': 3}
                            ),
                            ft.Container(
                                ft.Column([
                                    ft.Icon(ft.Icons.PSYCHOLOGY, size=25, color=ft.Colors.ORANGE_700),
                                    ft.Text("AI", size=16, weight=ft.FontWeight.BOLD),
                                    ft.Text("Physics Help", size=12)
                                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                                bgcolor=ft.Colors.ORANGE_50,
                                border_radius=10,
                                padding=10,
                                col={'xs': 6, 'sm': 3}
                            ),
                        ], spacing=10, run_spacing=10)
                    ], spacing=15),
                    bgcolor=ft.Colors.INDIGO_50,
                    border_radius=10,
                    padding=15,
                    border=ft.border.all(2, ft.Colors.INDIGO_200)
                )
            ], spacing=20),
            padding=20,
            expand=True
        )

    def show_main_page(self, page=None):
        if page is None:
            page = self.page
            
        view = ft.View(
            "/physics",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: page.go("/")),
                    title=ft.Text("Physics"),
                    bgcolor=ft.Colors.INDIGO_700,
                    center_title=True
                ),
                self.create_main_view()
            ]
        )
        
        page.views.clear()
        page.views.append(view)
        page.update()

    def show_learning_content(self):
        def go_back(e):
            if len(self.page.views) > 1:
                self.page.views.pop()
                self.page.update()
            else:
                self.show_main_page()
        
        view = ft.View(
            "/physics/learn",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=go_back),
                    title=ft.Text("Learn Physics"),
                    bgcolor=ft.Colors.INDIGO_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("Physics: Complete Learning Guide", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.INDIGO_900),
                        ft.Text("Understanding the fundamental laws of nature", size=16, color=ft.Colors.INDIGO_700),
                        
                        # Mechanics
                        ft.Container(
                            ft.Column([
                                ft.Text("🚀 Mechanics", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
                                ft.Text("The study of motion and forces.", size=14),
                                
                                ft.Text("Newton's Three Laws:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_600),
                                ft.Column([
                                    ft.Text("1. Law of Inertia: Objects at rest stay at rest, moving objects stay moving (unless acted upon by force)", size=14),
                                    ft.Text("2. F = ma: Force equals mass times acceleration", size=14),
                                    ft.Text("3. Action-Reaction: For every action, there's an equal and opposite reaction", size=14),
                                ], spacing=5),
                                
                                ft.Text("Key Equations:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_600),
                                ft.Column([
                                    ft.Text("• Speed = distance/time", size=14),
                                    ft.Text("• Acceleration = change in velocity/time", size=14),
                                    ft.Text("• Force = mass × acceleration", size=14),
                                    ft.Text("• Work = force × distance", size=14),
                                ], spacing=5),
                            ], spacing=10),
                            bgcolor=ft.Colors.BLUE_50,
                            padding=15,
                            border_radius=10,
                            border=ft.border.all(2, ft.Colors.BLUE_200)
                        ),
                        
                        # Energy
                        ft.Container(
                            ft.Column([
                                ft.Text("⚡ Energy", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
                                ft.Text("Energy is the capacity to do work and comes in many forms.", size=14),
                                
                                ft.Text("Types of Energy:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_600),
                                ft.Column([
                                    ft.Text("• Kinetic Energy: KE = ½mv² (energy of motion)", size=14),
                                    ft.Text("• Potential Energy: PE = mgh (stored energy)", size=14),
                                    ft.Text("• Thermal Energy: Heat and temperature", size=14),
                                    ft.Text("• Chemical Energy: Stored in bonds", size=14),
                                    ft.Text("• Electrical Energy: Moving charges", size=14),
                                ], spacing=5),
                                
                                ft.Text("Conservation of Energy:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_600),
                                ft.Text("Energy cannot be created or destroyed, only transformed from one type to another.", size=14),
                            ], spacing=10),
                            bgcolor=ft.Colors.GREEN_50,
                            padding=15,
                            border_radius=10,
                            border=ft.border.all(2, ft.Colors.GREEN_200)
                        ),
                        
                        # Waves and Electricity
                        ft.Container(
                            ft.Column([
                                ft.Text("🌊⚡ Waves & Electricity", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_700),
                                
                                ft.Text("Wave Properties:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_600),
                                ft.Column([
                                    ft.Text("• Wavelength (λ): Distance between wave peaks", size=14),
                                    ft.Text("• Frequency (f): Waves per second (Hz)", size=14),
                                    ft.Text("• Amplitude: Wave height (energy)", size=14),
                                    ft.Text("• Speed = frequency × wavelength", size=14),
                                ], spacing=5),
                                
                                ft.Text("Electrical Basics:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_600),
                                ft.Column([
                                    ft.Text("• Voltage (V): Electrical pressure", size=14),
                                    ft.Text("• Current (I): Flow of charge (Amps)", size=14),
                                    ft.Text("• Resistance (R): Opposition to flow (Ohms)", size=14),
                                    ft.Text("• Ohm's Law: V = I × R", size=14),
                                    ft.Text("• Power = Voltage × Current", size=14),
                                ], spacing=5),
                            ], spacing=10),
                            bgcolor=ft.Colors.PURPLE_50,
                            padding=15,
                            border_radius=10,
                            border=ft.border.all(2, ft.Colors.PURPLE_200)
                        ),
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
        def go_back(e):
            if len(self.page.views) > 1:
                self.page.views.pop()
                self.page.update()
            else:
                self.show_main_page()
        
        view = ft.View(
            "/physics/quizzes",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=go_back),
                    title=ft.Text("Physics Quizzes"),
                    bgcolor=ft.Colors.GREEN_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("Choose Your Physics Quiz Level", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_900),
                        ft.Text("Test your understanding of physics concepts", size=16, color=ft.Colors.GREEN_700),
                        
                        ft.ResponsiveRow([
                            ft.Container(
                                ft.Card(
                                    ft.Container(
                                        ft.Column([
                                            ft.Icon(ft.Icons.STAR_OUTLINE, size=40, color=ft.Colors.GREEN_600),
                                            ft.Text("Basic Physics", size=18, weight=ft.FontWeight.BOLD),
                                            ft.Text("Forces & Motion\nBasic Energy", text_align=ft.TextAlign.CENTER),
                                            ft.Text("10 Questions", size=12, color=ft.Colors.GREEN_600),
                                            ft.ElevatedButton(
                                                "Start Basic Quiz",
                                                on_click=lambda e: self.start_quiz("basic"),
                                                style=ft.ButtonStyle(bgcolor=ft.Colors.GREEN_700, color=ft.Colors.WHITE)
                                            )
                                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
                                        padding=20
                                    )
                                ),
                                col={'xs': 12, 'sm': 6, 'md': 4}
                            ),
                            ft.Container(
                                ft.Card(
                                    ft.Container(
                                        ft.Column([
                                            ft.Icon(ft.Icons.STAR_HALF, size=40, color=ft.Colors.ORANGE_600),
                                            ft.Text("Intermediate", size=18, weight=ft.FontWeight.BOLD),
                                            ft.Text("Calculations & Waves\nElectricity Basics", text_align=ft.TextAlign.CENTER),
                                            ft.Text("10 Questions", size=12, color=ft.Colors.ORANGE_600),
                                            ft.ElevatedButton(
                                                "Start Intermediate",
                                                on_click=lambda e: self.start_quiz("intermediate"),
                                                style=ft.ButtonStyle(bgcolor=ft.Colors.ORANGE_700, color=ft.Colors.WHITE)
                                            )
                                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
                                        padding=20
                                    )
                                ),
                                col={'xs': 12, 'sm': 6, 'md': 4}
                            ),
                            ft.Container(
                                ft.Card(
                                    ft.Container(
                                        ft.Column([
                                            ft.Icon(ft.Icons.STAR, size=40, color=ft.Colors.PURPLE_600),
                                            ft.Text("Advanced", size=18, weight=ft.FontWeight.BOLD),
                                            ft.Text("Modern Physics\nComplex Concepts", text_align=ft.TextAlign.CENTER),
                                            ft.Text("10 Questions", size=12, color=ft.Colors.PURPLE_600),
                                            ft.ElevatedButton(
                                                "Start Advanced",
                                                on_click=lambda e: self.start_quiz("advanced"),
                                                style=ft.ButtonStyle(bgcolor=ft.Colors.PURPLE_700, color=ft.Colors.WHITE)
                                            )
                                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
                                        padding=20
                                    )
                                ),
                                col={'xs': 12, 'sm': 6, 'md': 4}
                            ),
                        ], spacing=20, run_spacing=20)
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
        questions = self.quiz_questions[level].copy()
        random.shuffle(questions)
        self.current_quiz_questions = questions[:min(len(questions), 10)]
        self.show_quiz_question()

    def show_quiz_question(self):
        if self.quiz_question_index >= len(self.current_quiz_questions):
            self.show_quiz_results()
            return
            
        question_data = self.current_quiz_questions[self.quiz_question_index]
        options = question_data["options"].copy()
        correct_answer = options[question_data["correct"]]
        
        random.shuffle(options)
        new_correct_index = options.index(correct_answer)
        self.current_correct_index = new_correct_index
        self.current_shuffled_options = options.copy()
        
        def go_back(e):
            if len(self.page.views) > 1:
                self.page.views.pop()
                self.page.update()
            else:
                self.show_quizzes()
        
        option_buttons = []
        for i, option in enumerate(options):
            option_buttons.append(
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Text(f"{chr(65+i)}. {option}", size=16),
                        on_click=lambda e, idx=i: self.answer_question(idx),
                        style=ft.ButtonStyle(
                            padding=ft.Padding(20, 15, 20, 15),
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        width=None,
                        expand=True
                    ),
                    col={'xs': 12, 'sm': 6},
                    margin=5
                )
            )
        
        view = ft.View(
            f"/physics/quiz/{self.current_quiz_level}",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=go_back),
                    title=ft.Text(f"{self.current_quiz_level.title()} Physics Quiz"),
                    bgcolor=ft.Colors.GREEN_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Container(
                            ft.Column([
                                ft.Text(f"Question {self.quiz_question_index + 1} of {len(self.current_quiz_questions)}", 
                                        size=16, color=ft.Colors.GREEN_700),
                                ft.ProgressBar(
                                    value=(self.quiz_question_index) / len(self.current_quiz_questions),
                                    color=ft.Colors.GREEN_700,
                                    bgcolor=ft.Colors.GREEN_100
                                )
                            ], spacing=10),
                            padding=10,
                            bgcolor=ft.Colors.GREEN_50,
                            border_radius=10
                        ),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("Question:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
                                ft.Text(question_data["question"], size=18, weight=ft.FontWeight.BOLD),
                            ], spacing=10),
                            padding=20,
                            bgcolor=ft.Colors.BLUE_50,
                            border_radius=10,
                            border=ft.border.all(2, ft.Colors.BLUE_200)
                        ),
                        
                        ft.Text("Choose your answer:", size=16, weight=ft.FontWeight.BOLD),
                        ft.ResponsiveRow(option_buttons, spacing=10, run_spacing=10),
                        
                        ft.Row([
                            ft.Container(
                                ft.Text(f"Current Score: {self.quiz_score}/{self.quiz_question_index}", 
                                       size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
                                padding=10,
                                bgcolor=ft.Colors.GREEN_50,
                                border_radius=5,
                                expand=True
                            ),
                            ft.Container(
                                ft.ElevatedButton(
                                    content=ft.Row([
                                        ft.Icon(ft.Icons.LIGHTBULB_OUTLINE, color=ft.Colors.AMBER_700),
                                        ft.Text("Get Hint", size=14)
                                    ], spacing=5),
                                    on_click=lambda e: self.show_quiz_ai_help(question_data["question"]),
                                    style=ft.ButtonStyle(bgcolor=ft.Colors.AMBER_50, color=ft.Colors.AMBER_900)
                                ),
                                padding=5
                            )
                        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
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
        is_correct = selected_index == self.current_correct_index
        if is_correct:
            self.quiz_score += 1
        self.show_answer_feedback(self.current_quiz_questions[self.quiz_question_index], selected_index, is_correct)

    def show_answer_feedback(self, question_data, selected_index, is_correct):
        feedback_color = ft.Colors.GREEN_700 if is_correct else ft.Colors.RED_700
        feedback_icon = ft.Icons.CHECK_CIRCLE if is_correct else ft.Icons.CANCEL
        feedback_text = "Correct!" if is_correct else "Incorrect"
        
        correct_answer = question_data["options"][question_data["correct"]]
        user_selected = self.current_shuffled_options[selected_index]
        
        dialog = ft.AlertDialog(
            title=ft.Text(feedback_text, color=feedback_color, size=24, weight=ft.FontWeight.BOLD),
            content=ft.Column([
                ft.Icon(feedback_icon, size=50, color=feedback_color),
                ft.Text(f"Your answer: {user_selected}", size=16),
                ft.Text(f"Correct answer: {correct_answer}", size=16),
                ft.Divider(),
                ft.Text("Explanation:", size=16, weight=ft.FontWeight.BOLD),
                ft.Text(question_data["explanation"], size=14)
            ], spacing=10, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            actions=[ft.TextButton("Next Question", on_click=lambda e: self.next_question(e))]
        )
        
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()

    def next_question(self, e):
        self.page.dialog.open = False
        self.page.update()
        self.quiz_question_index += 1
        if self.quiz_question_index < len(self.current_quiz_questions):
            self.show_quiz_question()
        else:
            self.show_quiz_results()

    def show_quiz_results(self):
        score_percentage = (self.quiz_score / len(self.current_quiz_questions)) * 100
        
        if score_percentage >= 90:
            grade, grade_color, message = "A+", ft.Colors.GREEN_700, "Outstanding physics mastery!"
        elif score_percentage >= 80:
            grade, grade_color, message = "A", ft.Colors.GREEN_600, "Excellent physics understanding!"
        elif score_percentage >= 70:
            grade, grade_color, message = "B", ft.Colors.BLUE_600, "Good grasp of physics concepts!"
        elif score_percentage >= 60:
            grade, grade_color, message = "C", ft.Colors.ORANGE_600, "You're learning! Keep practicing physics."
        else:
            grade, grade_color, message = "F", ft.Colors.RED_600, "Physics takes practice! Review the concepts."
        
        def go_back_from_results(e):
            if len(self.page.views) > 1:
                self.page.views.pop()
                self.page.update()
            else:
                self.show_quizzes()
        
        view = ft.View(
            "/physics/quiz/results",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=go_back_from_results),
                    title=ft.Text("Physics Quiz Results"),
                    bgcolor=grade_color
                ),
                ft.Container(
                    ft.Column([
                        ft.Container(
                            ft.Column([
                                ft.Icon(ft.Icons.EMOJI_EVENTS, size=60, color=grade_color),
                                ft.Text("Physics Quiz Complete!", size=28, weight=ft.FontWeight.BOLD, color=grade_color),
                                ft.Text(f"Grade: {grade}", size=24, weight=ft.FontWeight.BOLD),
                                ft.Text(f"Score: {self.quiz_score}/{len(self.current_quiz_questions)} ({score_percentage:.1f}%)", size=20),
                                ft.Text(message, size=16, text_align=ft.TextAlign.CENTER, color=ft.Colors.GREY_700)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
                            padding=30,
                            bgcolor=ft.Colors.GREY_50,
                            border_radius=15
                        ),
                        
                        ft.ResponsiveRow([
                            ft.Container(
                                ft.ElevatedButton(
                                    "Try Again",
                                    on_click=lambda e: self.start_quiz(self.current_quiz_level),
                                    style=ft.ButtonStyle(bgcolor=ft.Colors.BLUE_700, color=ft.Colors.WHITE, padding=15)
                                ),
                                col={'xs': 12, 'sm': 6, 'md': 4}
                            ),
                            ft.Container(
                                ft.ElevatedButton(
                                    "Different Level",
                                    on_click=lambda e: self.show_quizzes(),
                                    style=ft.ButtonStyle(bgcolor=ft.Colors.GREEN_700, color=ft.Colors.WHITE, padding=15)
                                ),
                                col={'xs': 12, 'sm': 6, 'md': 4}
                            ),
                            ft.Container(
                                ft.ElevatedButton(
                                    "Back to Main",
                                    on_click=lambda e: self.show_main_page(),
                                    style=ft.ButtonStyle(bgcolor=ft.Colors.PURPLE_700, color=ft.Colors.WHITE, padding=15)
                                ),
                                col={'xs': 12, 'sm': 6, 'md': 4}
                            ),
                        ], spacing=10, run_spacing=10)
                    ], spacing=30),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def show_calculator(self):
        """Physics calculator for common calculations"""
        def go_back(e):
            if len(self.page.views) > 1:
                self.page.views.pop()
                self.page.update()
            else:
                self.show_main_page()
        
        # Calculator fields
        mass_field = ft.TextField(label="Mass (kg)", width=150)
        acceleration_field = ft.TextField(label="Acceleration (m/s²)", width=150)
        force_result = ft.Text("", size=16, color=ft.Colors.BLUE_700)
        
        velocity_field = ft.TextField(label="Velocity (m/s)", width=150)
        kinetic_result = ft.Text("", size=16, color=ft.Colors.BLUE_700)
        
        height_field = ft.TextField(label="Height (m)", width=150)
        potential_result = ft.Text("", size=16, color=ft.Colors.BLUE_700)
        
        voltage_field = ft.TextField(label="Voltage (V)", width=150)
        resistance_field = ft.TextField(label="Resistance (Ω)", width=150)
        current_result = ft.Text("", size=16, color=ft.Colors.BLUE_700)
        
        def calculate_force(e):
            try:
                m = float(mass_field.value) if mass_field.value else 0
                a = float(acceleration_field.value) if acceleration_field.value else 0
                force = m * a
                force_result.value = f"Force = {force:.2f} N"
                self.page.update()
            except:
                force_result.value = "Error: Enter valid numbers"
                self.page.update()
        
        def calculate_kinetic_energy(e):
            try:
                m = float(mass_field.value) if mass_field.value else 0
                v = float(velocity_field.value) if velocity_field.value else 0
                ke = 0.5 * m * v * v
                kinetic_result.value = f"Kinetic Energy = {ke:.2f} J"
                self.page.update()
            except:
                kinetic_result.value = "Error: Enter valid numbers"
                self.page.update()
        
        def calculate_potential_energy(e):
            try:
                m = float(mass_field.value) if mass_field.value else 0
                h = float(height_field.value) if height_field.value else 0
                g = 9.8  # gravity
                pe = m * g * h
                potential_result.value = f"Potential Energy = {pe:.2f} J"
                self.page.update()
            except:
                potential_result.value = "Error: Enter valid numbers"
                self.page.update()
        
        def calculate_current(e):
            try:
                v = float(voltage_field.value) if voltage_field.value else 0
                r = float(resistance_field.value) if resistance_field.value else 0
                if r != 0:
                    i = v / r
                    current_result.value = f"Current = {i:.2f} A"
                else:
                    current_result.value = "Error: Resistance cannot be zero"
                self.page.update()
            except:
                current_result.value = "Error: Enter valid numbers"
                self.page.update()
        
        view = ft.View(
            "/physics/calculator",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=go_back),
                    title=ft.Text("Physics Calculator"),
                    bgcolor=ft.Colors.ORANGE_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("⚡ Physics Calculator", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_900),
                        ft.Text("Calculate common physics quantities", size=16, color=ft.Colors.ORANGE_700),
                        
                        # Force Calculator
                        ft.Container(
                            ft.Column([
                                ft.Text("Force Calculator (F = ma)", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
                                ft.Row([mass_field, acceleration_field], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
                                ft.ElevatedButton("Calculate Force", on_click=calculate_force, 
                                                style=ft.ButtonStyle(bgcolor=ft.Colors.BLUE_700, color=ft.Colors.WHITE)),
                                force_result
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
                            bgcolor=ft.Colors.BLUE_50,
                            padding=15,
                            border_radius=10
                        ),
                        
                        # Energy Calculators
                        ft.Container(
                            ft.Column([
                                ft.Text("Energy Calculators", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
                                
                                ft.Text("Kinetic Energy (KE = ½mv²)", size=16, weight=ft.FontWeight.BOLD),
                                ft.Row([velocity_field], alignment=ft.MainAxisAlignment.CENTER),
                                ft.ElevatedButton("Calculate Kinetic Energy", on_click=calculate_kinetic_energy,
                                                style=ft.ButtonStyle(bgcolor=ft.Colors.GREEN_700, color=ft.Colors.WHITE)),
                                kinetic_result,
                                
                                ft.Divider(),
                                
                                ft.Text("Potential Energy (PE = mgh)", size=16, weight=ft.FontWeight.BOLD),
                                ft.Row([height_field], alignment=ft.MainAxisAlignment.CENTER),
                                ft.ElevatedButton("Calculate Potential Energy", on_click=calculate_potential_energy,
                                                style=ft.ButtonStyle(bgcolor=ft.Colors.GREEN_700, color=ft.Colors.WHITE)),
                                potential_result
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
                            bgcolor=ft.Colors.GREEN_50,
                            padding=15,
                            border_radius=10
                        ),
                        
                        # Electrical Calculator
                        ft.Container(
                            ft.Column([
                                ft.Text("Ohm's Law Calculator (V = IR)", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_700),
                                ft.Row([voltage_field, resistance_field], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
                                ft.ElevatedButton("Calculate Current", on_click=calculate_current,
                                                style=ft.ButtonStyle(bgcolor=ft.Colors.PURPLE_700, color=ft.Colors.WHITE)),
                                current_result
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
                            bgcolor=ft.Colors.PURPLE_50,
                            padding=15,
                            border_radius=10
                        ),
                    ], spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def show_quiz_ai_help(self, question):
        dialog = ft.AlertDialog(
            title=ft.Text("Physics Helper", size=20, weight=ft.FontWeight.BOLD),
            content=ft.Container(
                ft.Column([
                    ft.Container(
                        ft.Column([
                            ft.Text("Question:", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.INDIGO_700),
                            ft.Text(question, size=14),
                        ], spacing=5),
                        bgcolor=ft.Colors.INDIGO_50,
                        padding=10,
                        border_radius=5
                    ),
                    ft.Divider(),
                    ft.Container(
                        ft.Column([
                            ft.Text("Physics Hint:", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
                            ft.Text(get_physics_ai_help(f"hint for {question}"), size=14),
                        ], spacing=5),
                        bgcolor=ft.Colors.GREEN_50,
                        padding=10,
                        border_radius=5
                    ),
                ], spacing=10, scroll=ft.ScrollMode.AUTO),
                height=300,
                width=500,
            ),
            actions=[ft.TextButton("Close", on_click=lambda e: self.close_dialog(), style=ft.ButtonStyle(color=ft.Colors.INDIGO_700))],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()
    
    def close_dialog(self):
        if self.page.dialog:
            self.page.dialog.open = False
            self.page.update()

    def show_ai_help(self):
        query_field = ft.TextField(
            label="Ask about Physics...",
            hint_text="e.g., How does Newton's second law work? What's the difference between speed and velocity?",
            multiline=True,
            min_lines=3,
            expand=True
        )
        
        response_text = ft.Text("", size=14, selectable=True)
        
        def handle_query(e):
            if query_field.value:
                response = get_physics_ai_help(query_field.value)
                response_text.value = response
                self.page.update()
        
        def go_back(e):
            if len(self.page.views) > 1:
                self.page.views.pop()
                self.page.update()
            else:
                self.show_main_page()
        
        view = ft.View(
            "/physics/ai_help",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=go_back),
                    title=ft.Text("Physics AI Helper"),
                    bgcolor=ft.Colors.PURPLE_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("Physics AI Assistant", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_900),
                        ft.Text("Get help with any physics concept or problem", size=16, color=ft.Colors.PURPLE_700),
                        query_field,
                        ft.ElevatedButton(
                            "Get Help",
                            on_click=handle_query,
                            style=ft.ButtonStyle(bgcolor=ft.Colors.PURPLE_700, color=ft.Colors.WHITE)
                        ),
                        ft.Container(response_text, bgcolor=ft.Colors.GREY_100, border_radius=10, padding=15, expand=True),
                        
                        ft.Text("Quick Physics Topics:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_700),
                        ft.ResponsiveRow([
                            ft.Container(
                                ft.ElevatedButton(
                                    "Forces & Motion",
                                    on_click=lambda e: (setattr(query_field, 'value', 'force and motion'), handle_query(e)),
                                    style=ft.ButtonStyle(bgcolor=ft.Colors.GREEN_50)
                                ),
                                col={'xs': 6, 'sm': 3}
                            ),
                            ft.Container(
                                ft.ElevatedButton(
                                    "Energy",
                                    on_click=lambda e: (setattr(query_field, 'value', 'energy'), handle_query(e)),
                                    style=ft.ButtonStyle(bgcolor=ft.Colors.BLUE_50)
                                ),
                                col={'xs': 6, 'sm': 3}
                            ),
                            ft.Container(
                                ft.ElevatedButton(
                                    "Electricity",
                                    on_click=lambda e: (setattr(query_field, 'value', 'electricity'), handle_query(e)),
                                    style=ft.ButtonStyle(bgcolor=ft.Colors.ORANGE_50)
                                ),
                                col={'xs': 6, 'sm': 3}
                            ),
                            ft.Container(
                                ft.ElevatedButton(
                                    "Waves & Light",
                                    on_click=lambda e: (setattr(query_field, 'value', 'wave and light'), handle_query(e)),
                                    style=ft.ButtonStyle(bgcolor=ft.Colors.PURPLE_50)
                                ),
                                col={'xs': 6, 'sm': 3}
                            ),
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

def physics_page(page: ft.Page):
    """Physics learning page"""
    page.title = "Physics - Science Learning"
    page.scroll = ft.ScrollMode.AUTO
    page.clean()
    
    module = PhysicsModule(page)
    
    page.appbar = ft.AppBar(
        leading=ft.IconButton(
            ft.Icons.ARROW_BACK,
            on_click=lambda e: page.go("/science")
        ),
        title=ft.Text("Physics"),
        bgcolor=ft.Colors.INDIGO_700,
        center_title=True
    )
    
    page.add(module.create_main_view())