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
    def __init__(self, page, parent_navigation_callback=None):
        self.page = page
        self.parent_navigation_callback = parent_navigation_callback  # Callback to parent page
        self.current_quiz_level = "basic"
        self.quiz_score = 0
        self.quiz_question_index = 0
        self.current_correct_index = 0
        self.current_shuffled_options = []
        self.current_quiz_questions = []
        
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

    def navigate_back(self):
        """Consistent back navigation"""
        if len(self.page.views) > 1:
            self.page.views.pop()
        else:
            # If this is the first view, create the main view
            self.show_main_page()
        self.page.update()

    def navigate_to_parent(self):
        """Navigate to parent page - close app or exit gracefully"""
        dialog = ft.AlertDialog(
            title=ft.Text("Exit Scientific Method"),
            content=ft.Text("Are you sure you want to exit the Scientific Method learning module?"),
            actions=[
                ft.TextButton("Cancel", on_click=lambda e: self.close_dialog()),
                ft.TextButton(
                    "Exit", 
                    on_click=lambda e: self.exit_app(),
                    style=ft.ButtonStyle(color=ft.Colors.RED_700)
                )
            ]
        )
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()

    def exit_app(self):
        """Exit the application"""
        self.close_dialog()
        self.page.window_close()

    def restart_app(self):
        """Restart the app (fallback navigation)"""
        self.close_dialog()
        self.show_main_page()

    def show_main_page(self):
        self.page.clean()
        self.page.add(
            ft.AppBar(
                leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.navigate_to_parent()),
                title=ft.Text("Scientific Method", color=ft.Colors.WHITE),
                bgcolor=ft.Colors.TEAL_700,
                center_title=True
            ),
            self.create_main_view()
        )
        self.page.update()

    def show_learning_content(self):
        self.page.clean()
        self.page.scroll = ft.ScrollMode.AUTO
        self.page.add(
            ft.AppBar(
                leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.navigate_back()),
                title=ft.Text("Learn Scientific Method", color=ft.Colors.WHITE),
                bgcolor=ft.Colors.TEAL_700
            ),
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
            ], spacing=20, scroll=ft.ScrollMode.AUTO, expand=True),
            ft.Container(height=20)  # Bottom padding
        )

    def show_quizzes(self):
        self.page.clean()
        self.page.scroll = ft.ScrollMode.AUTO
        self.page.add(
            ft.AppBar(
                leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.navigate_back()),
                title=ft.Text("Scientific Method Quizzes", color=ft.Colors.WHITE),
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
        )

    def start_quiz(self, level):
        """Initialize quiz with shuffled questions"""
        self.current_quiz_level = level
        self.quiz_score = 0
        self.quiz_question_index = 0
        
        # Get questions for the level and shuffle them
        questions = self.quiz_questions[level].copy()
        random.shuffle(questions)
        self.current_quiz_questions = questions[:min(len(questions), 10)]
        
        self.show_quiz_question()

    def show_quiz_question(self):
        """Display the current quiz question"""
        if self.quiz_question_index >= len(self.current_quiz_questions):
            self.show_quiz_results()
            return
            
        question_data = self.current_quiz_questions[self.quiz_question_index]
        
        # Shuffle the options and track the correct answer position
        options = question_data["options"].copy()
        correct_answer = options[question_data["correct"]]
        random.shuffle(options)
        self.current_correct_index = options.index(correct_answer)
        self.current_shuffled_options = options.copy()
        
        # Create option buttons
        option_buttons = []
        for i, option in enumerate(options):
            option_buttons.append(
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Text(f"{chr(65+i)}. {option}", size=16),
                        on_click=lambda e, idx=i: self.answer_question(idx),
                        style=ft.ButtonStyle(
                            padding=ft.Padding(20, 15, 20, 15),
                            shape=ft.RoundedRectangleBorder(radius=10),
                            bgcolor=ft.Colors.WHITE
                        ),
                        width=None
                    ),
                    col={'xs': 12, 'sm': 6},
                    margin=5
                )
            )
        
        self.page.clean()
        self.page.scroll = ft.ScrollMode.AUTO
        self.page.add(
            ft.AppBar(
                leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.navigate_back()),
                title=ft.Text(f"{self.current_quiz_level.title()} Quiz", color=ft.Colors.WHITE),
                bgcolor=ft.Colors.GREEN_700
            ),
            ft.Container(
                ft.Column([
                    # Progress indicator
                    ft.Container(
                        ft.Column([
                            ft.Text(f"Question {self.quiz_question_index + 1} of {len(self.current_quiz_questions)}", 
                                    size=16, color=ft.Colors.GREEN_700, weight=ft.FontWeight.BOLD),
                            ft.ProgressBar(
                                value=(self.quiz_question_index) / len(self.current_quiz_questions),
                                color=ft.Colors.GREEN_700,
                                bgcolor=ft.Colors.GREEN_100
                            )
                        ], spacing=10),
                        padding=15,
                        bgcolor=ft.Colors.GREEN_50,
                        border_radius=10
                    ),
                    
                    # Question display
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
                    
                    # Answer options
                    ft.Text("Choose your answer:", size=16, weight=ft.FontWeight.BOLD),
                    ft.ResponsiveRow(option_buttons, spacing=10, run_spacing=10),
                    
                    # Score and hint
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
        )

    def answer_question(self, selected_index):
        """Process the user's answer and show feedback"""
        is_correct = selected_index == self.current_correct_index
        if is_correct:
            self.quiz_score += 1
        
        self.show_answer_feedback(
            self.current_quiz_questions[self.quiz_question_index], 
            selected_index, 
            is_correct
        )

    def show_answer_feedback(self, question_data, selected_index, is_correct):
        """Show immediate feedback for the answer"""
        feedback_color = ft.Colors.GREEN_700 if is_correct else ft.Colors.RED_700
        feedback_icon = ft.Icons.CHECK_CIRCLE if is_correct else ft.Icons.CANCEL
        feedback_text = "Correct!" if is_correct else "Incorrect"
        
        correct_answer = question_data["options"][question_data["correct"]]
        user_selected = self.current_shuffled_options[selected_index]
        
        dialog = ft.AlertDialog(
            title=ft.Row([
                ft.Icon(feedback_icon, size=30, color=feedback_color),
                ft.Text(feedback_text, color=feedback_color, size=24, weight=ft.FontWeight.BOLD)
            ], alignment=ft.MainAxisAlignment.CENTER),
            content=ft.Container(
                ft.Column([
                    ft.Container(
                        ft.Column([
                            ft.Text("Your Answer:", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
                            ft.Text(user_selected, size=16),
                        ], spacing=5),
                        bgcolor=ft.Colors.BLUE_50,
                        padding=10,
                        border_radius=5
                    ),
                    ft.Container(
                        ft.Column([
                            ft.Text("Correct Answer:", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
                            ft.Text(correct_answer, size=16),
                        ], spacing=5),
                        bgcolor=ft.Colors.GREEN_50,
                        padding=10,
                        border_radius=5
                    ),
                    ft.Divider(),
                    ft.Container(
                        ft.Column([
                            ft.Text("Explanation:", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_700),
                            ft.Text(question_data["explanation"], size=14),
                        ], spacing=5),
                        bgcolor=ft.Colors.PURPLE_50,
                        padding=10,
                        border_radius=5
                    )
                ], spacing=10),
                width=500,
                height=300
            ),
            actions=[
                ft.ElevatedButton(
                    "Next Question", 
                    on_click=lambda e: self.next_question(),
                    style=ft.ButtonStyle(bgcolor=ft.Colors.TEAL_700, color=ft.Colors.WHITE)
                )
            ],
            actions_alignment=ft.MainAxisAlignment.CENTER,
        )
        
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()

    def next_question(self):
        """Move to the next question or show results"""
        # Close dialog
        if self.page.dialog:
            self.page.dialog.open = False
            self.page.update()
        
        # Move to next question
        self.quiz_question_index += 1
        
        if self.quiz_question_index < len(self.current_quiz_questions):
            self.show_quiz_question()
        else:
            self.show_quiz_results()

    def show_quiz_results(self):
        """Display final quiz results with grade"""
        score_percentage = (self.quiz_score / len(self.current_quiz_questions)) * 100
        
        if score_percentage >= 90:
            grade, grade_color, message = "A+", ft.Colors.GREEN_700, "Outstanding mastery of the scientific method!"
            grade_icon = ft.Icons.EMOJI_EVENTS
        elif score_percentage >= 80:
            grade, grade_color, message = "A", ft.Colors.GREEN_600, "Excellent understanding of scientific thinking!"
            grade_icon = ft.Icons.STAR
        elif score_percentage >= 70:
            grade, grade_color, message = "B", ft.Colors.BLUE_600, "Good grasp of scientific concepts!"
            grade_icon = ft.Icons.THUMB_UP
        elif score_percentage >= 60:
            grade, grade_color, message = "C", ft.Colors.ORANGE_600, "You're learning! Review and practice more."
            grade_icon = ft.Icons.SCHOOL
        else:
            grade, grade_color, message = "F", ft.Colors.RED_600, "Keep studying! The scientific method takes practice."
            grade_icon = ft.Icons.BOOK
        
        self.page.clean()
        self.page.scroll = ft.ScrollMode.AUTO
        self.page.add(
            ft.AppBar(
                leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.navigate_back()),
                title=ft.Text("Quiz Results", color=ft.Colors.WHITE),
                bgcolor=grade_color
            ),
            ft.Container(
                ft.Column([
                    # Results display
                    ft.Container(
                        ft.Column([
                            ft.Icon(grade_icon, size=60, color=grade_color),
                            ft.Text("Quiz Complete!", size=28, weight=ft.FontWeight.BOLD, color=grade_color),
                            ft.Text(f"Grade: {grade}", size=24, weight=ft.FontWeight.BOLD),
                            ft.Text(f"Score: {self.quiz_score}/{len(self.current_quiz_questions)} ({score_percentage:.1f}%)", size=20),
                            ft.Text(message, size=16, text_align=ft.TextAlign.CENTER, color=ft.Colors.GREY_700)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
                        padding=30,
                        bgcolor=ft.Colors.GREY_50,
                        border_radius=15
                    ),
                    
                    # Action buttons
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
                    ], spacing=10, run_spacing=10),
                    
                    # Performance breakdown
                    ft.Container(
                        ft.Column([
                            ft.Text("Performance Breakdown", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.TEAL_700),
                            ft.Text(f"Level: {self.current_quiz_level.title()}", size=14),
                            ft.Text(f"Questions Attempted: {len(self.current_quiz_questions)}", size=14),
                            ft.Text(f"Correct Answers: {self.quiz_score}", size=14),
                            ft.Text(f"Accuracy: {score_percentage:.1f}%", size=14),
                        ], spacing=5),
                        bgcolor=ft.Colors.TEAL_50,
                        padding=15,
                        border_radius=10
                    )
                ], spacing=30),
                padding=20,
                expand=True,
                scroll=ft.ScrollMode.AUTO
            )
        )

    def show_quiz_ai_help(self, question):
        """Show AI help for quiz question"""
        help_response = get_scientific_method_ai_help(f"hint for {question}")
        
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
                            ft.Text(help_response, size=14),
                        ], spacing=5),
                        bgcolor=ft.Colors.GREEN_50,
                        padding=10,
                        border_radius=5
                    ),
                ], spacing=10),
                width=500,
                height=300
            ),
            actions=[
                ft.TextButton(
                    "Close", 
                    on_click=lambda e: self.close_dialog(), 
                    style=ft.ButtonStyle(color=ft.Colors.TEAL_700)
                )
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()
    
    def close_dialog(self):
        """Close any open dialog"""
        if self.page.dialog:
            self.page.dialog.open = False
            self.page.update()

    def show_examples(self):
        """Show real-world examples of the scientific method"""
        self.page.clean()
        self.page.scroll = ft.ScrollMode.AUTO
        self.page.add(
            ft.AppBar(
                leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.navigate_back()),
                title=ft.Text("Scientific Method Examples", color=ft.Colors.WHITE),
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
                    
                    # Example 3: Physics Experiment
                    ft.Container(
                        ft.Column([
                            ft.Text("Example 3: Physics Investigation", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_800),
                            
                            ft.Text("1. Observation:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_700),
                            ft.Text("Objects of different weights seem to fall at different speeds.", size=14),
                            
                            ft.Text("2. Question:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_700),
                            ft.Text("Does the weight of an object affect how fast it falls?", size=14),
                            
                            ft.Text("3. Hypothesis:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_700),
                            ft.Text("If objects have different weights, then heavier objects will fall faster, because they have more gravitational force.", size=14),
                            
                            ft.Text("4. Experiment:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_700),
                            ft.Column([
                                ft.Text("• Drop objects of different weights from same height", size=14),
                                ft.Text("• Control for air resistance (vacuum chamber)", size=14),
                                ft.Text("• Measure time to fall", size=14),
                                ft.Text("• Repeat multiple times for accuracy", size=14),
                            ], spacing=5),
                            
                            ft.Text("5. Results:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_700),
                            ft.Text("All objects fell at the same rate when air resistance was eliminated.", size=14),
                            
                            ft.Text("6. Conclusion:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_700),
                            ft.Text("The hypothesis was NOT supported. Weight doesn't affect fall rate in a vacuum - gravity accelerates all objects equally.", size=14),
                        ], spacing=8),
                        bgcolor=ft.Colors.PURPLE_50,
                        padding=15,
                        border_radius=10,
                        border=ft.border.all(2, ft.Colors.PURPLE_200)
                    ),
                ], spacing=20),
                padding=20,
                expand=True
            )
        )

    def show_ai_help(self):
        """Show AI help interface"""
        query_field = ft.TextField(
            label="Ask about the Scientific Method...",
            hint_text="e.g., How do I write a good hypothesis? What's the difference between theory and law?",
            multiline=True,
            min_lines=3,
            expand=True
        )
        
        response_container = ft.Container(
            ft.Text("Ask a question to get personalized help with the scientific method!", size=14),
            bgcolor=ft.Colors.GREY_100, 
            border_radius=10, 
            padding=15, 
            height=200
        )
        
        def handle_query(e):
            if query_field.value and query_field.value.strip():
                response = get_scientific_method_ai_help(query_field.value)
                response_container.content = ft.Text(response, size=14, selectable=True)
                self.page.update()
        
        # Quick help buttons
        quick_help_buttons = []
        help_topics = [
            ("Hypotheses", "hypothesis"),
            ("Variables", "variable"),
            ("Experiments", "experiment"),
            ("Data Analysis", "data"),
            ("Observations", "observation"),
            ("Controls", "control"),
            ("Theories", "theory"),
            ("Bias", "bias")
        ]
        
        for topic_name, topic_key in help_topics:
            quick_help_buttons.append(
                ft.Container(
                    ft.ElevatedButton(
                        topic_name,
                        on_click=lambda e, key=topic_key: self.quick_help(key, query_field, response_container),
                        style=ft.ButtonStyle(bgcolor=ft.Colors.PURPLE_50, color=ft.Colors.PURPLE_800)
                    ),
                    col={'xs': 6, 'sm': 4, 'md': 3}
                )
            )
        
        self.page.clean()
        self.page.scroll = ft.ScrollMode.AUTO
        self.page.add(
            ft.AppBar(
                leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.navigate_back()),
                title=ft.Text("Scientific Method AI Helper", color=ft.Colors.WHITE),
                bgcolor=ft.Colors.PURPLE_700
            ),
            ft.Container(
                ft.Column([
                    ft.Text("Scientific Method AI Assistant", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_900),
                    ft.Text("Get help with any aspect of scientific investigation", size=16, color=ft.Colors.PURPLE_700),
                    
                    ft.Row([
                        query_field,
                        ft.ElevatedButton(
                            "Get Help",
                            on_click=handle_query,
                            style=ft.ButtonStyle(bgcolor=ft.Colors.PURPLE_700, color=ft.Colors.WHITE)
                        )
                    ], spacing=10),
                    
                    response_container,
                    
                    ft.Text("Quick Help Topics:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_700),
                    ft.ResponsiveRow(quick_help_buttons, spacing=10, run_spacing=10)
                ], spacing=15),
                padding=20,
                expand=True
            )
        )

    def quick_help(self, topic, query_field, response_container):
        """Handle quick help button clicks"""
        query_field.value = topic
        response = get_scientific_method_ai_help(topic)
        response_container.content = ft.Text(response, size=14, selectable=True)
        self.page.update()

def scientific_method_page(page: ft.Page):
    """Scientific Method learning page - main entry point"""
    page.title = "Scientific Method - Science Learning"
    page.scroll = ft.ScrollMode.AUTO
    
    module = ScientificMethodModule(page)
    module.show_main_page()

def main(page: ft.Page):
    """Main function to run the app"""
    page.title = "Scientific Method Learning App"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.spacing = 0
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
    def __init__(self, page, parent_navigation_callback=None):
        self.page = page
        self.parent_navigation_callback = parent_navigation_callback  # Callback to parent page
        self.current_quiz_level = "basic"
        self.quiz_score = 0
        self.quiz_question_index = 0
        self.current_correct_index = 0
        self.current_shuffled_options = []
        self.current_quiz_questions = []
        
        # Navigation stack for back button functionality
        self.navigation_stack = []
        
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

    def push_to_navigation_stack(self, page_name):
        """Add current page to navigation stack"""
        self.navigation_stack.append(page_name)

    def navigate_back(self):
        """Go back to previous page in navigation stack"""
        if len(self.navigation_stack) > 0:
            # Pop the current page
            self.navigation_stack.pop()
            
            # If there's a previous page, navigate to it
            if len(self.navigation_stack) > 0:
                previous_page = self.navigation_stack[-1]
                self.navigate_to_page(previous_page)
            else:
                # No more pages in stack, go to main
                self.show_main_page()
        else:
            # Empty stack, go to main
            self.show_main_page()

    def navigate_to_parent(self):
        """Navigate to parent page using navigation stack"""
        if len(self.navigation_stack) > 0:
            # Go back to previous page
            self.navigate_back()
        else:
            # No navigation history, show exit dialog
            dialog = ft.AlertDialog(
                title=ft.Text("Exit Scientific Method"),
                content=ft.Text("Are you sure you want to exit the Scientific Method learning module?"),
                actions=[
                    ft.TextButton("Cancel", on_click=lambda e: self.close_dialog()),
                    ft.TextButton(
                        "Exit", 
                        on_click=lambda e: self.exit_app(),
                        style=ft.ButtonStyle(color=ft.Colors.RED_700)
                    )
                ]
            )
            self.page.dialog = dialog
            dialog.open = True
            self.page.update()

    def navigate_to_page(self, page_name):
        """Navigate to specific page by name"""
        if page_name == "main":
            self.show_main_page()
        elif page_name == "learning":
            self.show_learning_content()
        elif page_name == "quizzes":
            self.show_quizzes()
        elif page_name == "examples":
            self.show_examples()
        elif page_name == "ai_help":
            self.show_ai_help()
        elif page_name == "quiz_question":
            self.show_quiz_question()
        else:
            # Default fallback
            self.show_main_page()

    def exit_app(self):
        """Exit the application"""
        self.close_dialog()
        try:
            self.page.window_close()
        except:
            # If window_close doesn't work, just show main page
            self.show_main_page()

    def show_main_page(self):
        # Clear navigation stack when returning to main page
        self.navigation_stack = []
        self.page.clean()
        self.page.add(
            ft.AppBar(
                leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.navigate_to_parent()),
                title=ft.Text("Scientific Method", color=ft.Colors.WHITE),
                bgcolor=ft.Colors.TEAL_700,
                center_title=True
            ),
            self.create_main_view()
        )
        self.page.update()

    def show_learning_content(self):
        self.push_to_navigation_stack("main")  # Track where we came from
        self.page.clean()
        self.page.scroll = ft.ScrollMode.AUTO
        self.page.add(
            ft.AppBar(
                leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.navigate_back()),
                title=ft.Text("Learn Scientific Method", color=ft.Colors.WHITE),
                bgcolor=ft.Colors.TEAL_700
            ),
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
            ], spacing=20, scroll=ft.ScrollMode.AUTO, expand=True),
            ft.Container(height=20)  # Bottom padding
        )

    def show_quizzes(self):
        self.push_to_navigation_stack("main")  # Track where we came from
        self.page.clean()
        self.page.scroll = ft.ScrollMode.AUTO
        self.page.add(
            ft.AppBar(
                leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.navigate_back()),
                title=ft.Text("Scientific Method Quizzes", color=ft.Colors.WHITE),
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
        )

    def start_quiz(self, level):
        """Initialize quiz with shuffled questions"""
        self.push_to_navigation_stack("quizzes")  # Track where we came from
        self.current_quiz_level = level
        self.quiz_score = 0
        self.quiz_question_index = 0
        
        # Get questions for the level and shuffle them
        questions = self.quiz_questions[level].copy()
        random.shuffle(questions)
        self.current_quiz_questions = questions[:min(len(questions), 10)]
        
        self.show_quiz_question()

    def show_quiz_question(self):
        """Display the current quiz question"""
        if self.quiz_question_index >= len(self.current_quiz_questions):
            self.show_quiz_results()
            return
            
        question_data = self.current_quiz_questions[self.quiz_question_index]
        
        # Shuffle the options and track the correct answer position
        options = question_data["options"].copy()
        correct_answer = options[question_data["correct"]]
        random.shuffle(options)
        self.current_correct_index = options.index(correct_answer)
        self.current_shuffled_options = options.copy()
        
        # Create option buttons
        option_buttons = []
        for i, option in enumerate(options):
            option_buttons.append(
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Text(f"{chr(65+i)}. {option}", size=16),
                        on_click=lambda e, idx=i: self.answer_question(idx),
                        style=ft.ButtonStyle(
                            padding=ft.Padding(20, 15, 20, 15),
                            shape=ft.RoundedRectangleBorder(radius=10),
                            bgcolor=ft.Colors.WHITE
                        ),
                        width=None
                    ),
                    col={'xs': 12, 'sm': 6},
                    margin=5
                )
            )
        
        self.page.clean()
        self.page.scroll = ft.ScrollMode.AUTO
        self.page.add(
            ft.AppBar(
                leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.navigate_back()),
                title=ft.Text(f"{self.current_quiz_level.title()} Quiz", color=ft.Colors.WHITE),
                bgcolor=ft.Colors.GREEN_700
            ),
            ft.Container(
                ft.Column([
                    # Progress indicator
                    ft.Container(
                        ft.Column([
                            ft.Text(f"Question {self.quiz_question_index + 1} of {len(self.current_quiz_questions)}", 
                                    size=16, color=ft.Colors.GREEN_700, weight=ft.FontWeight.BOLD),
                            ft.ProgressBar(
                                value=(self.quiz_question_index) / len(self.current_quiz_questions),
                                color=ft.Colors.GREEN_700,
                                bgcolor=ft.Colors.GREEN_100
                            )
                        ], spacing=10),
                        padding=15,
                        bgcolor=ft.Colors.GREEN_50,
                        border_radius=10
                    ),
                    
                    # Question display
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
                    
                    # Answer options
                    ft.Text("Choose your answer:", size=16, weight=ft.FontWeight.BOLD),
                    ft.ResponsiveRow(option_buttons, spacing=10, run_spacing=10),
                    
                    # Score and hint
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
        )

    def answer_question(self, selected_index):
        """Process the user's answer and show feedback"""
        is_correct = selected_index == self.current_correct_index
        if is_correct:
            self.quiz_score += 1
        
        self.show_answer_feedback(
            self.current_quiz_questions[self.quiz_question_index], 
            selected_index, 
            is_correct
        )

    def show_answer_feedback(self, question_data, selected_index, is_correct):
        """Show immediate feedback for the answer"""
        feedback_color = ft.Colors.GREEN_700 if is_correct else ft.Colors.RED_700
        feedback_icon = ft.Icons.CHECK_CIRCLE if is_correct else ft.Icons.CANCEL
        feedback_text = "Correct!" if is_correct else "Incorrect"
        
        correct_answer = question_data["options"][question_data["correct"]]
        user_selected = self.current_shuffled_options[selected_index]
        
        dialog = ft.AlertDialog(
            title=ft.Row([
                ft.Icon(feedback_icon, size=30, color=feedback_color),
                ft.Text(feedback_text, color=feedback_color, size=24, weight=ft.FontWeight.BOLD)
            ], alignment=ft.MainAxisAlignment.CENTER),
            content=ft.Container(
                ft.Column([
                    ft.Container(
                        ft.Column([
                            ft.Text("Your Answer:", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
                            ft.Text(user_selected, size=16),
                        ], spacing=5),
                        bgcolor=ft.Colors.BLUE_50,
                        padding=10,
                        border_radius=5
                    ),
                    ft.Container(
                        ft.Column([
                            ft.Text("Correct Answer:", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
                            ft.Text(correct_answer, size=16),
                        ], spacing=5),
                        bgcolor=ft.Colors.GREEN_50,
                        padding=10,
                        border_radius=5
                    ),
                    ft.Divider(),
                    ft.Container(
                        ft.Column([
                            ft.Text("Explanation:", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_700),
                            ft.Text(question_data["explanation"], size=14),
                        ], spacing=5),
                        bgcolor=ft.Colors.PURPLE_50,
                        padding=10,
                        border_radius=5
                    )
                ], spacing=10),
                width=500,
                height=300
            ),
            actions=[
                ft.ElevatedButton(
                    "Next Question", 
                    on_click=lambda e: self.next_question(),
                    style=ft.ButtonStyle(bgcolor=ft.Colors.TEAL_700, color=ft.Colors.WHITE)
                )
            ],
            actions_alignment=ft.MainAxisAlignment.CENTER,
        )
        
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()

    def next_question(self):
        """Move to the next question or show results"""
        # Close dialog
        if self.page.dialog:
            self.page.dialog.open = False
            self.page.update()
        
        # Move to next question
        self.quiz_question_index += 1
        
        if self.quiz_question_index < len(self.current_quiz_questions):
            self.show_quiz_question()
        else:
            self.show_quiz_results()

    def show_quiz_results(self):
        """Display final quiz results with grade"""
        self.push_to_navigation_stack("quiz_question")  # Track where we came from
        score_percentage = (self.quiz_score / len(self.current_quiz_questions)) * 100
        
        if score_percentage >= 90:
            grade, grade_color, message = "A+", ft.Colors.GREEN_700, "Outstanding mastery of the scientific method!"
            grade_icon = ft.Icons.EMOJI_EVENTS
        elif score_percentage >= 80:
            grade, grade_color, message = "A", ft.Colors.GREEN_600, "Excellent understanding of scientific thinking!"
            grade_icon = ft.Icons.STAR
        elif score_percentage >= 70:
            grade, grade_color, message = "B", ft.Colors.BLUE_600, "Good grasp of scientific concepts!"
            grade_icon = ft.Icons.THUMB_UP
        elif score_percentage >= 60:
            grade, grade_color, message = "C", ft.Colors.ORANGE_600, "You're learning! Review and practice more."
            grade_icon = ft.Icons.SCHOOL
        else:
            grade, grade_color, message = "F", ft.Colors.RED_600, "Keep studying! The scientific method takes practice."
            grade_icon = ft.Icons.BOOK
        
        self.page.clean()
        self.page.scroll = ft.ScrollMode.AUTO
        self.page.add(
            ft.AppBar(
                leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.navigate_back()),
                title=ft.Text("Quiz Results", color=ft.Colors.WHITE),
                bgcolor=grade_color
            ),
            ft.Container(
                ft.Column([
                    # Results display
                    ft.Container(
                        ft.Column([
                            ft.Icon(grade_icon, size=60, color=grade_color),
                            ft.Text("Quiz Complete!", size=28, weight=ft.FontWeight.BOLD, color=grade_color),
                            ft.Text(f"Grade: {grade}", size=24, weight=ft.FontWeight.BOLD),
                            ft.Text(f"Score: {self.quiz_score}/{len(self.current_quiz_questions)} ({score_percentage:.1f}%)", size=20),
                            ft.Text(message, size=16, text_align=ft.TextAlign.CENTER, color=ft.Colors.GREY_700)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
                        padding=30,
                        bgcolor=ft.Colors.GREY_50,
                        border_radius=15
                    ),
                    
                    # Action buttons
                    ft.ResponsiveRow([
                        ft.Container(
                            ft.ElevatedButton(
                                "Try Again",
                                on_click=lambda e: self.restart_quiz(),
                                style=ft.ButtonStyle(bgcolor=ft.Colors.BLUE_700, color=ft.Colors.WHITE, padding=15)
                            ),
                            col={'xs': 12, 'sm': 6, 'md': 4}
                        ),
                        ft.Container(
                            ft.ElevatedButton(
                                "Different Level",
                                on_click=lambda e: self.navigate_to_page("quizzes"),
                                style=ft.ButtonStyle(bgcolor=ft.Colors.GREEN_700, color=ft.Colors.WHITE, padding=15)
                            ),
                            col={'xs': 12, 'sm': 6, 'md': 4}
                        ),
                        ft.Container(
                            ft.ElevatedButton(
                                "Back to Main",
                                on_click=lambda e: self.navigate_to_page("main"),
                                style=ft.ButtonStyle(bgcolor=ft.Colors.PURPLE_700, color=ft.Colors.WHITE, padding=15)
                            ),
                            col={'xs': 12, 'sm': 6, 'md': 4}
                        ),
                    ], spacing=10, run_spacing=10),
                    
                    # Performance breakdown
                    ft.Container(
                        ft.Column([
                            ft.Text("Performance Breakdown", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.TEAL_700),
                            ft.Text(f"Level: {self.current_quiz_level.title()}", size=14),
                            ft.Text(f"Questions Attempted: {len(self.current_quiz_questions)}", size=14),
                            ft.Text(f"Correct Answers: {self.quiz_score}", size=14),
                            ft.Text(f"Accuracy: {score_percentage:.1f}%", size=14),
                        ], spacing=5),
                        bgcolor=ft.Colors.TEAL_50,
                        padding=15,
                        border_radius=10
                    )
                ], spacing=30),
                padding=20,
                expand=True,
                scroll=ft.ScrollMode.AUTO
            )
        )

    def show_quiz_ai_help(self, question):
        """Show AI help for quiz question"""
        help_response = get_scientific_method_ai_help(f"hint for {question}")
        
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
                            ft.Text(help_response, size=14),
                        ], spacing=5),
                        bgcolor=ft.Colors.GREEN_50,
                        padding=10,
                        border_radius=5
                    ),
                ], spacing=10),
                width=500,
                height=300
            ),
            actions=[
                ft.TextButton(
                    "Close", 
                    on_click=lambda e: self.close_dialog(), 
                    style=ft.ButtonStyle(color=ft.Colors.TEAL_700)
                )
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()
    
    def close_dialog(self):
        """Close any open dialog"""
        if self.page.dialog:
            self.page.dialog.open = False
            self.page.update()

    def show_examples(self):
        """Show real-world examples of the scientific method"""
        self.push_to_navigation_stack("main")  # Track where we came from
        self.page.clean()
        self.page.scroll = ft.ScrollMode.AUTO
        self.page.add(
            ft.AppBar(
                leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.navigate_back()),
                title=ft.Text("Scientific Method Examples", color=ft.Colors.WHITE),
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
                    
                    # Example 3: Physics Experiment
                    ft.Container(
                        ft.Column([
                            ft.Text("Example 3: Physics Investigation", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_800),
                            
                            ft.Text("1. Observation:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_700),
                            ft.Text("Objects of different weights seem to fall at different speeds.", size=14),
                            
                            ft.Text("2. Question:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_700),
                            ft.Text("Does the weight of an object affect how fast it falls?", size=14),
                            
                            ft.Text("3. Hypothesis:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_700),
                            ft.Text("If objects have different weights, then heavier objects will fall faster, because they have more gravitational force.", size=14),
                            
                            ft.Text("4. Experiment:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_700),
                            ft.Column([
                                ft.Text("• Drop objects of different weights from same height", size=14),
                                ft.Text("• Control for air resistance (vacuum chamber)", size=14),
                                ft.Text("• Measure time to fall", size=14),
                                ft.Text("• Repeat multiple times for accuracy", size=14),
                            ], spacing=5),
                            
                            ft.Text("5. Results:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_700),
                            ft.Text("All objects fell at the same rate when air resistance was eliminated.", size=14),
                            
                            ft.Text("6. Conclusion:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_700),
                            ft.Text("The hypothesis was NOT supported. Weight doesn't affect fall rate in a vacuum - gravity accelerates all objects equally.", size=14),
                        ], spacing=8),
                        bgcolor=ft.Colors.PURPLE_50,
                        padding=15,
                        border_radius=10,
                        border=ft.border.all(2, ft.Colors.PURPLE_200)
                    ),
                ], spacing=20),
                padding=20,
                expand=True
            )
        )

    def show_ai_help(self):
        """Show AI help interface"""
        query_field = ft.TextField(
            label="Ask about the Scientific Method...",
            hint_text="e.g., How do I write a good hypothesis? What's the difference between theory and law?",
            multiline=True,
            min_lines=3,
            expand=True
        )
        
        response_container = ft.Container(
            ft.Text("Ask a question to get personalized help with the scientific method!", size=14),
            bgcolor=ft.Colors.GREY_100, 
            border_radius=10, 
            padding=15, 
            height=200
        )
        
        def handle_query(e):
            if query_field.value and query_field.value.strip():
                response = get_scientific_method_ai_help(query_field.value)
                response_container.content = ft.Text(response, size=14, selectable=True)
                self.page.update()
        
        # Quick help buttons
        quick_help_buttons = []
        help_topics = [
            ("Hypotheses", "hypothesis"),
            ("Variables", "variable"),
            ("Experiments", "experiment"),
            ("Data Analysis", "data"),
            ("Observations", "observation"),
            ("Controls", "control"),
            ("Theories", "theory"),
            ("Bias", "bias")
        ]
        
        for topic_name, topic_key in help_topics:
            quick_help_buttons.append(
                ft.Container(
                    ft.ElevatedButton(
                        topic_name,
                        on_click=lambda e, key=topic_key: self.quick_help(key, query_field, response_container),
                        style=ft.ButtonStyle(bgcolor=ft.Colors.PURPLE_50, color=ft.Colors.PURPLE_800)
                    ),
                    col={'xs': 6, 'sm': 4, 'md': 3}
                )
            )
        
        self.page.clean()
        self.page.scroll = ft.ScrollMode.AUTO
        self.page.add(
            ft.AppBar(
                leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.navigate_back()),
                title=ft.Text("Scientific Method AI Helper", color=ft.Colors.WHITE),
                bgcolor=ft.Colors.PURPLE_700
            ),
            ft.Container(
                ft.Column([
                    ft.Text("Scientific Method AI Assistant", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_900),
                    ft.Text("Get help with any aspect of scientific investigation", size=16, color=ft.Colors.PURPLE_700),
                    
                    ft.Row([
                        query_field,
                        ft.ElevatedButton(
                            "Get Help",
                            on_click=handle_query,
                            style=ft.ButtonStyle(bgcolor=ft.Colors.PURPLE_700, color=ft.Colors.WHITE)
                        )
                    ], spacing=10),
                    
                    response_container,
                    
                    ft.Text("Quick Help Topics:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_700),
                    ft.ResponsiveRow(quick_help_buttons, spacing=10, run_spacing=10)
                ], spacing=15),
                padding=20,
                expand=True
            )
        )

    def restart_quiz(self):
        """Restart the current quiz level"""
        # Clear navigation stack for fresh start
        self.navigation_stack = ["quizzes"]  # Set up to go back to quizzes page
        self.start_quiz(self.current_quiz_level)

    def quick_help(self, topic, query_field, response_container):
        """Handle quick help button clicks"""
        query_field.value = topic
        response = get_scientific_method_ai_help(topic)
        response_container.content = ft.Text(response, size=14, selectable=True)
        self.page.update()

def scientific_method_page(page: ft.Page):
    """Scientific Method learning page - main entry point"""
    page.title = "Scientific Method - Science Learning"
    page.scroll = ft.ScrollMode.AUTO
    
    module = ScientificMethodModule(page)
    module.show_main_page()

def main(page: ft.Page):
    """Main function to run the app"""
    page.title = "Scientific Method Learning App"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.spacing = 0
    
    scientific_method_page(page)

if __name__ == "__main__":
    ft.app(target=main)
    scientific_method_page(page)

if __name__ == "__main__":
    ft.app(target=main)