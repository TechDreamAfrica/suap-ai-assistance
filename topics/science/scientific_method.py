import flet as ft
import random

def get_scientific_method_ai_help(query, topic="scientific_method"):
    """AI help for Scientific Method concepts"""
    try:
        responses = {
            "hypothesis": "A hypothesis is an educated guess or prediction about what will happen in an experiment. It should be testable and based on observations. Format: 'If [cause], then [effect], because [reasoning].'",
            "variable": "Variables are factors that can change in an experiment. Independent variable (what you change), dependent variable (what you measure), controlled variables (what you keep the same).",
            "observation": "Observations are what you notice using your senses or instruments. They should be objective, detailed, and recorded accurately. Distinguish between qualitative (descriptive) and quantitative (numerical) observations.",
            "experiment": "Experiments test hypotheses by changing one variable while keeping others constant. Good experiments have controls, are repeatable, and test only one factor at a time.",
            "conclusion": "Conclusions summarize what the data shows. They should state whether the hypothesis was supported or not, explain what was learned, and suggest further investigations.",
            "control": "Controls are parts of experiments that don't receive the treatment being tested. They help show that changes are due to your independent variable, not other factors.",
            "data": "Data is information collected during experiments. It can be qualitative (descriptions) or quantitative (numbers). Organize data in tables, graphs, or charts for analysis.",
            "theory": "A scientific theory is a well-supported explanation for natural phenomena, backed by extensive evidence. Theories can be modified as new evidence emerges.",
            "law": "Scientific laws describe what happens under certain conditions, while theories explain why it happens. Laws are often mathematical relationships.",
            "bias": "Bias can affect scientific results. Minimize bias through blind studies, controls, large sample sizes, and peer review. Always consider alternative explanations.",
        }
        
        query_lower = query.lower()
        for key, response in responses.items():
            if key in query_lower:
                return f"🔬 Scientific Method Helper: {response}"
        
        return f"🔬 Scientific Method Helper: I can help with hypotheses, variables, observations, experiments, conclusions, controls, data analysis, theories, and avoiding bias. Ask me about any step of the scientific method!"
    except Exception:
        return f"🔬 Scientific Method Helper: I'm here to help with the scientific method! Ask about observations, hypotheses, experiments, or data analysis."

class ScientificMethodModule:
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
                {"question": "What is the first step of the scientific method?", "options": ["Make a hypothesis", "Ask a question", "Do an experiment", "Collect data"], "correct": 1, "explanation": "The scientific method begins with asking a question about something you observe in the world."},
                {"question": "A hypothesis should be:", "options": ["Always correct", "Testable", "Complicated", "A proven fact"], "correct": 1, "explanation": "A hypothesis must be testable through experiments or observations to be useful in science."},
                {"question": "What is an independent variable?", "options": ["What you measure", "What you keep the same", "What you change", "The result"], "correct": 2, "explanation": "The independent variable is what you deliberately change in an experiment to test its effect."},
                {"question": "Why do we need a control group?", "options": ["To save time", "To compare results", "To make it harder", "To use more materials"], "correct": 1, "explanation": "A control group provides a baseline for comparison, helping us determine if our treatment caused the observed changes."},
                {"question": "Good observations should be:", "options": ["Quick", "Objective and detailed", "Based on opinions", "Simple"], "correct": 1, "explanation": "Scientific observations should be objective (fact-based) and detailed to provide accurate information."},
                {"question": "What should you do if your hypothesis is wrong?", "options": ["Hide the results", "Change the data", "Learn from it and revise", "Give up"], "correct": 2, "explanation": "Wrong hypotheses are valuable learning opportunities. Revise your understanding and try again."},
                {"question": "Which is a dependent variable?", "options": ["Temperature you set", "Amount of light provided", "Plant growth measured", "Type of soil used"], "correct": 2, "explanation": "The dependent variable is what you measure to see the effect - in this case, plant growth."},
                {"question": "What makes an experiment reliable?", "options": ["Using expensive equipment", "Getting expected results", "Being repeatable", "Taking a long time"], "correct": 2, "explanation": "Reliable experiments can be repeated by others and give consistent results."},
                {"question": "Qualitative data includes:", "options": ["Numbers only", "Descriptions and observations", "Measurements only", "Time only"], "correct": 1, "explanation": "Qualitative data describes qualities, characteristics, and properties that can't be measured numerically."},
                {"question": "The scientific method is:", "options": ["Only for scientists", "A way to answer questions", "Always the same steps", "Only for laboratories"], "correct": 1, "explanation": "The scientific method is a systematic way to investigate questions and can be used by anyone."}
            ],
            "intermediate": [
                {"question": "What is the difference between a theory and a hypothesis?", "options": ["No difference", "Theory is tested, hypothesis is not", "Hypothesis is tested, theory is proven", "Theory explains, hypothesis predicts"], "correct": 3, "explanation": "A theory explains why something happens (well-supported), while a hypothesis predicts what will happen (to be tested)."},
                {"question": "In a drug trial, what is a placebo?", "options": ["The real drug", "A fake treatment", "A side effect", "The control group"], "correct": 1, "explanation": "A placebo is a fake treatment that looks like the real one, used to control for psychological effects."},
                {"question": "What is peer review?", "options": ["Scientists reviewing each other's work", "Students grading papers", "Checking equipment", "Reading textbooks"], "correct": 0, "explanation": "Peer review is when other scientists examine research before publication to check methods and conclusions."},
                {"question": "Which bias occurs when researchers see what they expect?", "options": ["Selection bias", "Confirmation bias", "Observer bias", "Publication bias"], "correct": 2, "explanation": "Observer bias happens when researchers unconsciously influence results based on their expectations."},
                {"question": "What makes a good scientific question?", "options": ["Very broad", "Testable and specific", "About opinions", "Already answered"], "correct": 1, "explanation": "Good scientific questions are specific, testable through experiments, and lead to measurable outcomes."},
                {"question": "What is a double-blind study?", "options": ["Two experiments", "Neither researcher nor subject knows the treatment", "Two control groups", "Repeating twice"], "correct": 1, "explanation": "In double-blind studies, neither the researcher nor the participant knows who receives which treatment, reducing bias."},
                {"question": "What should you do with outliers in data?", "options": ["Always remove them", "Always keep them", "Investigate and decide", "Ignore them"], "correct": 2, "explanation": "Outliers should be investigated - they might reveal important information or indicate errors."},
                {"question": "What is the purpose of replication in science?", "options": ["To waste time", "To verify results", "To use more materials", "To confuse people"], "correct": 1, "explanation": "Replication helps verify that results are reliable and not due to chance or error."},
                {"question": "Which is NOT a controlled variable?", "options": ["Temperature kept at 25°C", "Using the same type of plant", "The growth rate measured", "Same amount of water given"], "correct": 2, "explanation": "Growth rate is the dependent variable being measured, not a controlled variable."},
                {"question": "What is correlation vs causation?", "options": ["Same thing", "Correlation shows relationship, causation shows cause", "Causation is stronger", "No difference"], "correct": 1, "explanation": "Correlation shows two things change together; causation shows one actually causes the other."}
            ],
            "advanced": [
                {"question": "What is statistical significance?", "options": ["Results are important", "Results are unlikely due to chance", "Results are large", "Results are perfect"], "correct": 1, "explanation": "Statistical significance means the results are probably not due to random chance (usually p < 0.05)."},
                {"question": "What is a Type I error?", "options": ["Equipment failure", "False positive", "Sample too small", "Wrong hypothesis"], "correct": 1, "explanation": "Type I error is rejecting a true hypothesis (false positive) - saying there's an effect when there isn't."},
                {"question": "What is the purpose of randomization?", "options": ["Make experiments harder", "Reduce bias and confounding", "Save time", "Use fewer subjects"], "correct": 1, "explanation": "Randomization helps ensure groups are similar and reduces bias from unknown factors."},
                {"question": "What is a confounding variable?", "options": ["The independent variable", "A variable that affects results but isn't controlled", "The dependent variable", "Random noise"], "correct": 1, "explanation": "Confounding variables affect the outcome but aren't controlled, potentially invalidating conclusions."},
                {"question": "What is meta-analysis?", "options": ["A big experiment", "Analyzing multiple studies together", "Using many variables", "Advanced statistics"], "correct": 1, "explanation": "Meta-analysis combines results from multiple studies to get more powerful conclusions."},
                {"question": "What is the null hypothesis?", "options": ["No hypothesis", "The opposite hypothesis", "No effect hypothesis", "Wrong hypothesis"], "correct": 2, "explanation": "The null hypothesis assumes no effect or difference - what we try to reject with evidence."},
                {"question": "What determines sample size?", "options": ["Available time", "Effect size and desired power", "Cost only", "Random choice"], "correct": 1, "explanation": "Sample size depends on expected effect size, desired statistical power, and significance level."},
                {"question": "What is external validity?", "options": ["Results apply to other situations", "Experiment was done correctly", "Data is accurate", "Equipment works"], "correct": 0, "explanation": "External validity means results can be generalized to other populations, settings, or conditions."},
                {"question": "What is publication bias?", "options": ["Preferring positive results", "Bad writing", "Wrong journals", "Slow publishing"], "correct": 0, "explanation": "Publication bias occurs when positive or significant results are more likely to be published than negative results."},
                {"question": "What is the replication crisis?", "options": ["Too many studies", "Many studies can't be reproduced", "Equipment problems", "Not enough funding"], "correct": 1, "explanation": "The replication crisis refers to many scientific studies being difficult or impossible to reproduce."}
            ]
        }

    def create_main_view(self):
        return ft.Container(
            ft.Column([
                ft.Text("🔬 Scientific Method", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.TEAL_900, text_align=ft.TextAlign.CENTER),
                ft.Text("Master the systematic approach to scientific investigation", size=16, color=ft.Colors.TEAL_700, text_align=ft.TextAlign.CENTER),
                ft.Divider(height=30),
                
                # Navigation buttons
                ft.ResponsiveRow([
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.SCHOOL_OUTLINED, size=30, color=ft.Colors.BLUE_700),
                                ft.Text("Learn Method", size=14, weight=ft.FontWeight.BOLD)
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
                                ft.Text("Practice Quiz", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_quizzes(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.GREEN_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.LIGHTBULB_OUTLINE, size=30, color=ft.Colors.ORANGE_700),
                                ft.Text("Examples", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_examples(),
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
                        ft.Text("Master the systematic approach scientists use to understand the natural world", size=14),
                        
                        ft.Text("Key Steps:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.TEAL_700),
                        ft.Column([
                            ft.Text("1. Observe: Notice something interesting", size=14),
                            ft.Text("2. Question: Ask what, why, or how", size=14),
                            ft.Text("3. Hypothesize: Make an educated guess", size=14),
                            ft.Text("4. Experiment: Test your hypothesis", size=14),
                            ft.Text("5. Analyze: Study the results", size=14),
                            ft.Text("6. Conclude: Determine what you learned", size=14),
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
                                    ft.Text("Method Steps", size=12)
                                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                                bgcolor=ft.Colors.GREEN_50,
                                border_radius=10,
                                padding=10,
                                col={'xs': 6, 'sm': 3}
                            ),
                            ft.Container(
                                ft.Column([
                                    ft.Icon(ft.Icons.SPEED, size=25, color=ft.Colors.PURPLE_700),
                                    ft.Text("3", size=16, weight=ft.FontWeight.BOLD),
                                    ft.Text("Difficulty Levels", size=12)
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
                                    ft.Text("Tutor Help", size=12)
                                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                                bgcolor=ft.Colors.ORANGE_50,
                                border_radius=10,
                                padding=10,
                                col={'xs': 6, 'sm': 3}
                            ),
                        ], spacing=10, run_spacing=10)
                    ], spacing=15),
                    bgcolor=ft.Colors.TEAL_50,
                    border_radius=10,
                    padding=15,
                    border=ft.border.all(2, ft.Colors.TEAL_200)
                )
            ], spacing=20),
            padding=20,
            expand=True
        )

    def show_main_page(self, page=None):
        if page is None:
            page = self.page
            
        view = ft.View(
            "/scientific_method",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: page.go("/")),
                    title=ft.Text("Scientific Method"),
                    bgcolor=ft.Colors.TEAL_700,
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
            "/scientific_method/learn",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=go_back),
                    title=ft.Text("Learn Scientific Method"),
                    bgcolor=ft.Colors.TEAL_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("The Scientific Method: Complete Guide", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.TEAL_900),
                        ft.Text("A systematic approach to understanding the natural world", size=16, color=ft.Colors.TEAL_700),
                        
                        # Step 1: Observation
                        ft.Container(
                            ft.Column([
                                ft.Text("1. Observation", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
                                ft.Text("Scientific investigations begin with careful observations of the world around us.", size=14),
                                
                                ft.Text("Types of Observations:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_600),
                                ft.Column([
                                    ft.Text("• Qualitative: Descriptive (color, texture, behavior)", size=14),
                                    ft.Text("• Quantitative: Numerical (measurements, counts)", size=14),
                                    ft.Text("• Direct: Using senses", size=14),
                                    ft.Text("• Indirect: Using instruments", size=14),
                                ], spacing=5),
                            ], spacing=10),
                            bgcolor=ft.Colors.BLUE_50,
                            padding=15,
                            border_radius=10,
                            border=ft.border.all(2, ft.Colors.BLUE_200)
                        ),
                        
                        # Step 2: Question
                        ft.Container(
                            ft.Column([
                                ft.Text("2. Ask Questions", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
                                ft.Text("Good observations lead to questions that can be investigated scientifically.", size=14),
                                
                                ft.Text("Good Scientific Questions:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_600),
                                ft.Column([
                                    ft.Text("• Are specific and focused", size=14),
                                    ft.Text("• Can be tested through experiments", size=14),
                                    ft.Text("• Have measurable outcomes", size=14),
                                    ft.Text("• Example: 'How does temperature affect plant growth?'", size=14),
                                ], spacing=5),
                            ], spacing=10),
                            bgcolor=ft.Colors.GREEN_50,
                            padding=15,
                            border_radius=10,
                            border=ft.border.all(2, ft.Colors.GREEN_200)
                        ),
                        
                        # Step 3: Hypothesis
                        ft.Container(
                            ft.Column([
                                ft.Text("3. Form Hypothesis", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_700),
                                ft.Text("A hypothesis is an educated guess that can be tested.", size=14),
                                
                                ft.Text("Good Hypothesis Format:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_600),
                                ft.Text("'If [cause], then [effect], because [reasoning]'", size=16, weight=ft.FontWeight.BOLD),
                                ft.Column([
                                    ft.Text("• Must be testable", size=14),
                                    ft.Text("• Should be specific", size=14),
                                    ft.Text("• Based on background knowledge", size=14),
                                    ft.Text("• Example: 'If temperature increases, then plants will grow faster, because heat speeds up chemical reactions.'", size=14),
                                ], spacing=5),
                            ], spacing=10),
                            bgcolor=ft.Colors.ORANGE_50,
                            padding=15,
                            border_radius=10,
                            border=ft.border.all(2, ft.Colors.ORANGE_200)
                        ),
                        
                        # Steps 4-6: Experiment, Analyze, Conclude
                        ft.Container(
                            ft.Column([
                                ft.Text("4-6. Experiment, Analyze, Conclude", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_700),
                                
                                ft.Text("4. Design and Conduct Experiments:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_600),
                                ft.Column([
                                    ft.Text("• Control variables (keep most things the same)", size=14),
                                    ft.Text("• Change only the independent variable", size=14),
                                    ft.Text("• Measure the dependent variable", size=14),
                                    ft.Text("• Use appropriate sample sizes", size=14),
                                ], spacing=5),
                                
                                ft.Text("5. Analyze Data:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_600),
                                ft.Column([
                                    ft.Text("• Organize data in tables and graphs", size=14),
                                    ft.Text("• Look for patterns and trends", size=14),
                                    ft.Text("• Use statistical analysis when appropriate", size=14),
                                ], spacing=5),
                                
                                ft.Text("6. Draw Conclusions:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_600),
                                ft.Column([
                                    ft.Text("• Was the hypothesis supported?", size=14),
                                    ft.Text("• What do the results mean?", size=14),
                                    ft.Text("• What are the limitations?", size=14),
                                    ft.Text("• What questions arise for future research?", size=14),
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
            "/scientific_method/quizzes",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=go_back),
                    title=ft.Text("Scientific Method Quizzes"),
                    bgcolor=ft.Colors.GREEN_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("Choose Your Quiz Level", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_900),
                        ft.Text("Test your understanding of the scientific method", size=16, color=ft.Colors.GREEN_700),
                        
                        ft.ResponsiveRow([
                            ft.Container(
                                ft.Card(
                                    ft.Container(
                                        ft.Column([
                                            ft.Icon(ft.Icons.STAR_OUTLINE, size=40, color=ft.Colors.GREEN_600),
                                            ft.Text("Basic Level", size=18, weight=ft.FontWeight.BOLD),
                                            ft.Text("Basic Steps\nSimple Concepts", text_align=ft.TextAlign.CENTER),
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
                                            ft.Text("Variables & Controls\nExperimental Design", text_align=ft.TextAlign.CENTER),
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
                                            ft.Text("Statistics & Bias\nResearch Methods", text_align=ft.TextAlign.CENTER),
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
            f"/scientific_method/quiz/{self.current_quiz_level}",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=go_back),
                    title=ft.Text(f"{self.current_quiz_level.title()} Quiz"),
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
            grade, grade_color, message = "A+", ft.Colors.GREEN_700, "Outstanding mastery of the scientific method!"
        elif score_percentage >= 80:
            grade, grade_color, message = "A", ft.Colors.GREEN_600, "Excellent understanding of scientific thinking!"
        elif score_percentage >= 70:
            grade, grade_color, message = "B", ft.Colors.BLUE_600, "Good grasp of scientific concepts!"
        elif score_percentage >= 60:
            grade, grade_color, message = "C", ft.Colors.ORANGE_600, "You're learning! Review and practice more."
        else:
            grade, grade_color, message = "F", ft.Colors.RED_600, "Keep studying! The scientific method takes practice."
        
        def go_back_from_results(e):
            if len(self.page.views) > 1:
                self.page.views.pop()
                self.page.update()
            else:
                self.show_quizzes()
        
        view = ft.View(
            "/scientific_method/quiz/results",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=go_back_from_results),
                    title=ft.Text("Quiz Results"),
                    bgcolor=grade_color
                ),
                ft.Container(
                    ft.Column([
                        ft.Container(
                            ft.Column([
                                ft.Icon(ft.Icons.EMOJI_EVENTS, size=60, color=grade_color),
                                ft.Text("Quiz Complete!", size=28, weight=ft.FontWeight.BOLD, color=grade_color),
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

    def show_quiz_ai_help(self, question):
        dialog = ft.AlertDialog(
            title=ft.Text("Scientific Method Helper", size=20, weight=ft.FontWeight.BOLD),
            content=ft.Container(
                ft.Column([
                    ft.Container(
                        ft.Column([
                            ft.Text("Question:", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.TEAL_700),
                            ft.Text(question, size=14),
                        ], spacing=5),
                        bgcolor=ft.Colors.TEAL_50,
                        padding=10,
                        border_radius=5
                    ),
                    ft.Divider(),
                    ft.Container(
                        ft.Column([
                            ft.Text("Hint:", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
                            ft.Text(get_scientific_method_ai_help(f"hint for {question}"), size=14),
                        ], spacing=5),
                        bgcolor=ft.Colors.GREEN_50,
                        padding=10,
                        border_radius=5
                    ),
                ], spacing=10, scroll=ft.ScrollMode.AUTO),
                height=300,
                width=500,
            ),
            actions=[ft.TextButton("Close", on_click=lambda e: self.close_dialog(), style=ft.ButtonStyle(color=ft.Colors.TEAL_700))],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()
    
    def close_dialog(self):
        if self.page.dialog:
            self.page.dialog.open = False
            self.page.update()

    def show_examples(self):
        def go_back(e):
            if len(self.page.views) > 1:
                self.page.views.pop()
                self.page.update()
            else:
                self.show_main_page()
        
        view = ft.View(
            "/scientific_method/examples",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=go_back),
                    title=ft.Text("Scientific Method Examples"),
                    bgcolor=ft.Colors.ORANGE_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("Scientific Method: Real Examples", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_900),
                        ft.Text("See how scientists apply the method to real problems", size=16, color=ft.Colors.ORANGE_700),
                        
                        # Example 1: Plant Growth Experiment
                        ft.Container(
                            ft.Column([
                                ft.Text("Example 1: Plant Growth Investigation", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_800),
                                
                                ft.Text("1. Observation:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
                                ft.Text("Some plants in the garden grow faster than others in different light conditions.", size=14),
                                
                                ft.Text("2. Question:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
                                ft.Text("How does the amount of sunlight affect plant growth?", size=14),
                                
                                ft.Text("3. Hypothesis:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
                                ft.Text("If plants receive more sunlight, then they will grow taller, because light is needed for photosynthesis.", size=14),
                                
                                ft.Text("4. Experiment:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
                                ft.Column([
                                    ft.Text("• Independent variable: Hours of sunlight (2, 4, 6, 8 hours)", size=14),
                                    ft.Text("• Dependent variable: Plant height after 2 weeks", size=14),
                                    ft.Text("• Controlled variables: Same plant type, soil, water, temperature", size=14),
                                    ft.Text("• Control group: Plants in normal classroom light", size=14),
                                ], spacing=5),
                                
                                ft.Text("5. Results:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
                                ft.Text("Plants with more sunlight grew significantly taller.", size=14),
                                
                                ft.Text("6. Conclusion:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
                                ft.Text("The hypothesis was supported. Sunlight amount directly affects plant growth rate.", size=14),
                            ], spacing=8),
                            bgcolor=ft.Colors.GREEN_50,
                            padding=15,
                            border_radius=10,
                            border=ft.border.all(2, ft.Colors.GREEN_200)
                        ),
                        
                        # Example 2: Medicine Testing
                        ft.Container(
                            ft.Column([
                                ft.Text("Example 2: Testing New Medicine", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800),
                                
                                ft.Text("1. Observation:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
                                ft.Text("A compound from tree bark seems to reduce headaches in traditional medicine.", size=14),
                                
                                ft.Text("2. Question:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
                                ft.Text("Does this compound effectively treat headaches compared to existing treatments?", size=14),
                                
                                ft.Text("3. Hypothesis:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
                                ft.Text("If patients take the tree bark compound, then their headaches will decrease more than with placebo, because the compound has anti-inflammatory properties.", size=14),
                                
                                ft.Text("4. Experiment:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
                                ft.Column([
                                    ft.Text("• Double-blind, randomized controlled trial", size=14),
                                    ft.Text("• 300 participants with chronic headaches", size=14),
                                    ft.Text("• Group 1: New compound, Group 2: Placebo, Group 3: Standard treatment", size=14),
                                    ft.Text("• Measure headache intensity and frequency for 3 months", size=14),
                                ], spacing=5),
                                
                                ft.Text("5. Results:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
                                ft.Text("New compound reduced headache intensity by 40% compared to 5% with placebo.", size=14),
                                
                                ft.Text("6. Conclusion:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
                                ft.Text("The compound shows promise, but more studies needed to confirm safety and optimal dosing.", size=14),
                            ], spacing=8),
                            bgcolor=ft.Colors.BLUE_50,
                            padding=15,
                            border_radius=10,
                            border=ft.border.all(2, ft.Colors.BLUE_200)
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

    def show_ai_help(self):
        query_field = ft.TextField(
            label="Ask about the Scientific Method...",
            hint_text="e.g., How do I write a good hypothesis? What's the difference between theory and law?",
            multiline=True,
            min_lines=3,
            expand=True
        )
        
        response_text = ft.Text("", size=14, selectable=True)
        
        def handle_query(e):
            if query_field.value:
                response = get_scientific_method_ai_help(query_field.value)
                response_text.value = response
                self.page.update()
        
        def go_back(e):
            if len(self.page.views) > 1:
                self.page.views.pop()
                self.page.update()
            else:
                self.show_main_page()
        
        view = ft.View(
            "/scientific_method/ai_help",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=go_back),
                    title=ft.Text("Scientific Method AI Helper"),
                    bgcolor=ft.Colors.PURPLE_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("Scientific Method AI Assistant", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_900),
                        ft.Text("Get help with any aspect of scientific investigation", size=16, color=ft.Colors.PURPLE_700),
                        query_field,
                        ft.ElevatedButton(
                            "Get Help",
                            on_click=handle_query,
                            style=ft.ButtonStyle(bgcolor=ft.Colors.PURPLE_700, color=ft.Colors.WHITE)
                        ),
                        ft.Container(response_text, bgcolor=ft.Colors.GREY_100, border_radius=10, padding=15, expand=True),
                        
                        ft.Text("Quick Help Topics:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_700),
                        ft.ResponsiveRow([
                            ft.Container(
                                ft.ElevatedButton(
                                    "Hypotheses",
                                    on_click=lambda e: (setattr(query_field, 'value', 'hypothesis'), handle_query(e)),
                                    style=ft.ButtonStyle(bgcolor=ft.Colors.GREEN_50)
                                ),
                                col={'xs': 6, 'sm': 3}
                            ),
                            ft.Container(
                                ft.ElevatedButton(
                                    "Variables",
                                    on_click=lambda e: (setattr(query_field, 'value', 'variable'), handle_query(e)),
                                    style=ft.ButtonStyle(bgcolor=ft.Colors.BLUE_50)
                                ),
                                col={'xs': 6, 'sm': 3}
                            ),
                            ft.Container(
                                ft.ElevatedButton(
                                    "Experiments",
                                    on_click=lambda e: (setattr(query_field, 'value', 'experiment'), handle_query(e)),
                                    style=ft.ButtonStyle(bgcolor=ft.Colors.ORANGE_50)
                                ),
                                col={'xs': 6, 'sm': 3}
                            ),
                            ft.Container(
                                ft.ElevatedButton(
                                    "Data Analysis",
                                    on_click=lambda e: (setattr(query_field, 'value', 'data'), handle_query(e)),
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

def scientific_method_page(page: ft.Page):
    """Scientific Method learning page"""
    page.title = "Scientific Method - Science Learning"
    page.scroll = ft.ScrollMode.AUTO
    page.clean()
    
    module = ScientificMethodModule(page)
    
    page.appbar = ft.AppBar(
        leading=ft.IconButton(
            ft.Icons.ARROW_BACK,
            on_click=lambda e: page.go("/science")
        ),
        title=ft.Text("Scientific Method"),
        bgcolor=ft.Colors.TEAL_700,
        center_title=True
    )
    
    page.add(module.create_main_view())