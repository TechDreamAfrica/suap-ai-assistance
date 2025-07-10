import flet as ft
import random

def get_ai_help(query, topic="chemistry_fixed"):
    """Enhanced AI help with comprehensive Chemistry Fixed knowledge"""
    try:
        responses = {
            "concept": "Chemistry Fixed involves scientific principles that help us understand the natural world. It's based on observation, experimentation, and evidence-based reasoning.",
            "method": "The scientific method is crucial for studying Chemistry Fixed. Start with observations, form hypotheses, conduct experiments, and analyze results to draw conclusions.",
            "application": "Chemistry Fixed has many real-world applications in technology, medicine, environmental science, and everyday life. Understanding these concepts helps solve practical problems.",
            "experiment": "Experiments in Chemistry Fixed help us test theories and discover new knowledge. Always follow safety procedures and record observations carefully.",
            "theory": "Scientific theories in Chemistry Fixed are well-supported explanations based on extensive evidence. They help predict and explain natural phenomena.",
            "law": "Scientific laws in Chemistry Fixed describe consistent patterns in nature that have been repeatedly observed and tested.",
            "discovery": "Many important discoveries in Chemistry Fixed have changed our understanding of the world and led to technological advances.",
            "research": "Current research in Chemistry Fixed continues to expand our knowledge and opens new possibilities for innovation and problem-solving.",
        }
        
        query_lower = query.lower()
        for key, response in responses.items():
            if key in query_lower:
                return f"🤖 AI Helper: {response}"
        
        return "🤖 AI Helper: I'm here to help with Chemistry Fixed concepts! Ask me about specific topics for detailed explanations."
    except Exception:
        return "🤖 AI Helper: I'm here to help with Chemistry Fixed concepts! Try asking about specific topics."

class ChemistryFixedModule:
    def __init__(self, page):
        self.page = page
        self.current_quiz_level = "basic"
        self.quiz_score = 0
        self.quiz_question_index = 0
        
        # Enhanced quiz questions with 50+ questions across three difficulty levels
        self.quiz_questions = {
            "basic": [
                {
                    "question": "What is the fundamental concept of Chemistry Fixed?",
                    "options": ['Basic concept', 'Advanced concept', 'Complex theory', 'Simple idea'],
                    "correct": 0,
                    "explanation": "This is the correct answer for Chemistry Fixed because it represents the fundamental understanding needed at the basic level."
                },
                {
                    "question": "Which of these is most important in Chemistry Fixed?",
                    "options": ['Understanding', 'Memorization', 'Speed', 'Guessing'],
                    "correct": 0,
                    "explanation": "This is the correct answer for Chemistry Fixed because it represents the fundamental understanding needed at the basic level."
                },
                {
                    "question": "What is the primary goal of studying Chemistry Fixed?",
                    "options": ['Learning', 'Testing', 'Competing', 'Passing'],
                    "correct": 0,
                    "explanation": "This is the correct answer for Chemistry Fixed because it represents the fundamental understanding needed at the basic level."
                },
                {
                    "question": "How would you describe Chemistry Fixed to a beginner?",
                    "options": ['Simple explanation', 'Complex theory', 'Advanced formula', 'Difficult concept'],
                    "correct": 0,
                    "explanation": "This is the correct answer for Chemistry Fixed because it represents the fundamental understanding needed at the basic level."
                },
                {
                    "question": "What is the best way to learn Chemistry Fixed?",
                    "options": ['Practice', 'Memorization', 'Guessing', 'Copying'],
                    "correct": 0,
                    "explanation": "This is the correct answer for Chemistry Fixed because it represents the fundamental understanding needed at the basic level."
                },
                {
                    "question": "Which skill is most developed through Chemistry Fixed?",
                    "options": ['Problem solving', 'Memory', 'Speed', 'Luck'],
                    "correct": 0,
                    "explanation": "This is the correct answer for Chemistry Fixed because it represents the fundamental understanding needed at the basic level."
                },
                {
                    "question": "What makes Chemistry Fixed important?",
                    "options": ['Real-world application', 'Test scores', 'Competition', 'Difficulty'],
                    "correct": 0,
                    "explanation": "This is the correct answer for Chemistry Fixed because it represents the fundamental understanding needed at the basic level."
                },
                {
                    "question": "How does Chemistry Fixed connect to other subjects?",
                    "options": ['Interdisciplinary', 'Isolated', 'Unrelated', 'Separate'],
                    "correct": 0,
                    "explanation": "This is the correct answer for Chemistry Fixed because it represents the fundamental understanding needed at the basic level."
                },
                {
                    "question": "What is the foundation of Chemistry Fixed?",
                    "options": ['Basic principles', 'Advanced theory', 'Complex formulas', 'Difficult concepts'],
                    "correct": 0,
                    "explanation": "This is the correct answer for Chemistry Fixed because it represents the fundamental understanding needed at the basic level."
                },
                {
                    "question": "Why is Chemistry Fixed taught in schools?",
                    "options": ['Essential knowledge', 'Tradition', 'Difficulty', 'Testing'],
                    "correct": 0,
                    "explanation": "This is the correct answer for Chemistry Fixed because it represents the fundamental understanding needed at the basic level."
                },
                {
                    "question": "What approach works best for Chemistry Fixed?",
                    "options": ['Step-by-step', 'Random', 'Rushed', 'Memorized'],
                    "correct": 0,
                    "explanation": "This is the correct answer for Chemistry Fixed because it represents the fundamental understanding needed at the basic level."
                },
                {
                    "question": "How can Chemistry Fixed be made easier?",
                    "options": ['Clear examples', 'More complexity', 'Faster pace', 'Less practice'],
                    "correct": 0,
                    "explanation": "This is the correct answer for Chemistry Fixed because it represents the fundamental understanding needed at the basic level."
                },
                {
                    "question": "What is the key to success in Chemistry Fixed?",
                    "options": ['Understanding', 'Speed', 'Memorization', 'Guessing'],
                    "correct": 0,
                    "explanation": "This is the correct answer for Chemistry Fixed because it represents the fundamental understanding needed at the basic level."
                },
                {
                    "question": "Which method helps learn Chemistry Fixed better?",
                    "options": ['Interactive practice', 'Passive reading', 'Memorization', 'Copying'],
                    "correct": 0,
                    "explanation": "This is the correct answer for Chemistry Fixed because it represents the fundamental understanding needed at the basic level."
                },
                {
                    "question": "What makes Chemistry Fixed interesting?",
                    "options": ['Practical applications', 'Difficulty', 'Complexity', 'Testing'],
                    "correct": 0,
                    "explanation": "This is the correct answer for Chemistry Fixed because it represents the fundamental understanding needed at the basic level."
                },
                {
                    "question": "How does Chemistry Fixed help in daily life?",
                    "options": ['Problem solving', 'Testing', 'Competition', 'Grades'],
                    "correct": 0,
                    "explanation": "This is the correct answer for Chemistry Fixed because it represents the fundamental understanding needed at the basic level."
                },
                {
                    "question": "What is the most important aspect of Chemistry Fixed?",
                    "options": ['Core concepts', 'Advanced topics', 'Difficult problems', 'Test preparation'],
                    "correct": 0,
                    "explanation": "This is the correct answer for Chemistry Fixed because it represents the fundamental understanding needed at the basic level."
                },
                {
                    "question": "How should beginners approach Chemistry Fixed?",
                    "options": ['Start with basics', 'Jump to advanced', 'Memorize everything', 'Skip fundamentals'],
                    "correct": 0,
                    "explanation": "This is the correct answer for Chemistry Fixed because it represents the fundamental understanding needed at the basic level."
                },
                {
                    "question": "What builds confidence in Chemistry Fixed?",
                    "options": ['Practice and success', 'Difficulty', 'Competition', 'Fear'],
                    "correct": 0,
                    "explanation": "This is the correct answer for Chemistry Fixed because it represents the fundamental understanding needed at the basic level."
                },
                {
                    "question": "Why is Chemistry Fixed considered valuable?",
                    "options": ['Develops thinking', 'Easy grades', 'Simple topics', 'No challenge'],
                    "correct": 0,
                    "explanation": "This is the correct answer for Chemistry Fixed because it represents the fundamental understanding needed at the basic level."
                },
            ],
            "intermediate": [
                {
                    "question": "What are the advanced concepts in Chemistry Fixed?",
                    "options": ['Complex applications', 'Basic ideas', 'Simple concepts', 'Elementary topics'],
                    "correct": 0,
                    "explanation": "This represents the intermediate level understanding of Chemistry Fixed, requiring deeper knowledge and application skills."
                },
                {
                    "question": "How do you apply Chemistry Fixed in real situations?",
                    "options": ['Practical problem solving', 'Memorization', 'Guessing', 'Copying'],
                    "correct": 0,
                    "explanation": "This represents the intermediate level understanding of Chemistry Fixed, requiring deeper knowledge and application skills."
                },
                {
                    "question": "What skills does Chemistry Fixed develop?",
                    "options": ['Critical thinking', 'Memory only', 'Speed only', 'Guessing only'],
                    "correct": 0,
                    "explanation": "This represents the intermediate level understanding of Chemistry Fixed, requiring deeper knowledge and application skills."
                },
                {
                    "question": "Which strategy works best for complex Chemistry Fixed problems?",
                    "options": ['Systematic approach', 'Random trying', 'Guessing', 'Memorization'],
                    "correct": 0,
                    "explanation": "This represents the intermediate level understanding of Chemistry Fixed, requiring deeper knowledge and application skills."
                },
                {
                    "question": "How does Chemistry Fixed connect to advanced topics?",
                    "options": ['Building blocks', 'Isolated topics', 'Unrelated concepts', 'Separate subjects'],
                    "correct": 0,
                    "explanation": "This represents the intermediate level understanding of Chemistry Fixed, requiring deeper knowledge and application skills."
                },
                {
                    "question": "What makes Chemistry Fixed challenging?",
                    "options": ['Complex relationships', 'Simple memorization', 'Easy concepts', 'Basic ideas'],
                    "correct": 0,
                    "explanation": "This represents the intermediate level understanding of Chemistry Fixed, requiring deeper knowledge and application skills."
                },
                {
                    "question": "How can you improve in Chemistry Fixed?",
                    "options": ['Deliberate practice', 'Passive reading', 'Memorization', 'Guessing'],
                    "correct": 0,
                    "explanation": "This represents the intermediate level understanding of Chemistry Fixed, requiring deeper knowledge and application skills."
                },
                {
                    "question": "What is the next level after basic Chemistry Fixed?",
                    "options": ['Advanced applications', 'Same level', 'Easier topics', 'Unrelated subjects'],
                    "correct": 0,
                    "explanation": "This represents the intermediate level understanding of Chemistry Fixed, requiring deeper knowledge and application skills."
                },
                {
                    "question": "How do experts approach Chemistry Fixed?",
                    "options": ['Pattern recognition', 'Memorization', 'Guessing', 'Random methods'],
                    "correct": 0,
                    "explanation": "This represents the intermediate level understanding of Chemistry Fixed, requiring deeper knowledge and application skills."
                },
                {
                    "question": "What makes Chemistry Fixed powerful?",
                    "options": ['Versatile applications', 'Limited use', 'Simple applications', 'No applications'],
                    "correct": 0,
                    "explanation": "This represents the intermediate level understanding of Chemistry Fixed, requiring deeper knowledge and application skills."
                },
                {
                    "question": "Which principle governs Chemistry Fixed?",
                    "options": ['Underlying logic', 'Random rules', 'Memorized facts', 'Guessed principles'],
                    "correct": 0,
                    "explanation": "This represents the intermediate level understanding of Chemistry Fixed, requiring deeper knowledge and application skills."
                },
                {
                    "question": "How does Chemistry Fixed relate to other fields?",
                    "options": ['Cross-disciplinary', 'Isolated', 'Unrelated', 'Separate'],
                    "correct": 0,
                    "explanation": "This represents the intermediate level understanding of Chemistry Fixed, requiring deeper knowledge and application skills."
                },
                {
                    "question": "What is the key insight in Chemistry Fixed?",
                    "options": ['Deep understanding', 'Surface knowledge', 'Memorization', 'Guessing'],
                    "correct": 0,
                    "explanation": "This represents the intermediate level understanding of Chemistry Fixed, requiring deeper knowledge and application skills."
                },
                {
                    "question": "How can Chemistry Fixed be mastered?",
                    "options": ['Consistent practice', 'Occasional study', 'Memorization', 'Guessing'],
                    "correct": 0,
                    "explanation": "This represents the intermediate level understanding of Chemistry Fixed, requiring deeper knowledge and application skills."
                },
                {
                    "question": "What distinguishes good Chemistry Fixed students?",
                    "options": ['Problem-solving ability', 'Memorization speed', 'Guessing accuracy', 'Test-taking skills'],
                    "correct": 0,
                    "explanation": "This represents the intermediate level understanding of Chemistry Fixed, requiring deeper knowledge and application skills."
                },
            ],
            "advanced": [
                {
                    "question": "What are the cutting-edge developments in Chemistry Fixed?",
                    "options": ['Latest research', 'Old methods', 'Basic concepts', 'Simple ideas'],
                    "correct": 0,
                    "explanation": "This represents advanced understanding of Chemistry Fixed, requiring sophisticated analysis and synthesis skills."
                },
                {
                    "question": "How do you create original solutions in Chemistry Fixed?",
                    "options": ['Creative thinking', 'Memorization', 'Copying', 'Guessing'],
                    "correct": 0,
                    "explanation": "This represents advanced understanding of Chemistry Fixed, requiring sophisticated analysis and synthesis skills."
                },
                {
                    "question": "What is the theoretical foundation of Chemistry Fixed?",
                    "options": ['Theoretical principles', 'Random rules', 'Memorized facts', 'Guessed theories'],
                    "correct": 0,
                    "explanation": "This represents advanced understanding of Chemistry Fixed, requiring sophisticated analysis and synthesis skills."
                },
                {
                    "question": "How does Chemistry Fixed advance knowledge?",
                    "options": ['Research and innovation', 'Memorization', 'Repetition', 'Copying'],
                    "correct": 0,
                    "explanation": "This represents advanced understanding of Chemistry Fixed, requiring sophisticated analysis and synthesis skills."
                },
                {
                    "question": "What are the limitations of Chemistry Fixed?",
                    "options": ['Boundary conditions', 'No limitations', 'Simple constraints', 'Easy boundaries'],
                    "correct": 0,
                    "explanation": "This represents advanced understanding of Chemistry Fixed, requiring sophisticated analysis and synthesis skills."
                },
                {
                    "question": "How do you prove results in Chemistry Fixed?",
                    "options": ['Rigorous methods', 'Guessing', 'Memorization', 'Copying'],
                    "correct": 0,
                    "explanation": "This represents advanced understanding of Chemistry Fixed, requiring sophisticated analysis and synthesis skills."
                },
                {
                    "question": "What is the future of Chemistry Fixed?",
                    "options": ['Emerging applications', 'Unchanged field', 'Declining importance', 'Simple applications'],
                    "correct": 0,
                    "explanation": "This represents advanced understanding of Chemistry Fixed, requiring sophisticated analysis and synthesis skills."
                },
                {
                    "question": "How does Chemistry Fixed influence other fields?",
                    "options": ['Interdisciplinary impact', 'No influence', 'Limited impact', 'Isolated field'],
                    "correct": 0,
                    "explanation": "This represents advanced understanding of Chemistry Fixed, requiring sophisticated analysis and synthesis skills."
                },
                {
                    "question": "What makes Chemistry Fixed research valuable?",
                    "options": ['Novel insights', 'Repetition', 'Memorization', 'Copying'],
                    "correct": 0,
                    "explanation": "This represents advanced understanding of Chemistry Fixed, requiring sophisticated analysis and synthesis skills."
                },
                {
                    "question": "How do you evaluate Chemistry Fixed theories?",
                    "options": ['Critical analysis', 'Acceptance', 'Memorization', 'Guessing'],
                    "correct": 0,
                    "explanation": "This represents advanced understanding of Chemistry Fixed, requiring sophisticated analysis and synthesis skills."
                },
                {
                    "question": "What is the complexity of Chemistry Fixed?",
                    "options": ['Multidimensional', 'Simple', 'Linear', 'Basic'],
                    "correct": 0,
                    "explanation": "This represents advanced understanding of Chemistry Fixed, requiring sophisticated analysis and synthesis skills."
                },
                {
                    "question": "How does Chemistry Fixed handle uncertainty?",
                    "options": ['Systematic methods', 'Ignoring uncertainty', 'Guessing', 'Memorization'],
                    "correct": 0,
                    "explanation": "This represents advanced understanding of Chemistry Fixed, requiring sophisticated analysis and synthesis skills."
                },
                {
                    "question": "What are the ethical considerations in Chemistry Fixed?",
                    "options": ['Responsible application', 'No ethics', 'Simple rules', 'Basic guidelines'],
                    "correct": 0,
                    "explanation": "This represents advanced understanding of Chemistry Fixed, requiring sophisticated analysis and synthesis skills."
                },
                {
                    "question": "How do you optimize Chemistry Fixed solutions?",
                    "options": ['Advanced algorithms', 'Random methods', 'Guessing', 'Memorization'],
                    "correct": 0,
                    "explanation": "This represents advanced understanding of Chemistry Fixed, requiring sophisticated analysis and synthesis skills."
                },
                {
                    "question": "What is the philosophical basis of Chemistry Fixed?",
                    "options": ['Fundamental principles', 'Random thoughts', 'Memorized ideas', 'Guessed concepts'],
                    "correct": 0,
                    "explanation": "This represents advanced understanding of Chemistry Fixed, requiring sophisticated analysis and synthesis skills."
                },
            ],
        }

    def create_main_view(self):
        return ft.Container(
            ft.Column([
                ft.Text("📚 Chemistry Fixed", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900, text_align=ft.TextAlign.CENTER),
                ft.Text("Explore the fundamentals and advanced concepts of Chemistry Fixed", size=16, color=ft.Colors.BLUE_700, text_align=ft.TextAlign.CENTER),
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
                                ft.Icon(ft.Icons.FITNESS_CENTER, size=30, color=ft.Colors.ORANGE_700),
                                ft.Text("Practice", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_practice(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.ORANGE_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                ], spacing=10, run_spacing=10),
                
                ft.Divider(height=20),
                
                # Quick overview
                ft.Container(
                    ft.Column([
                        ft.Text("📖 Chemistry Fixed Overview", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800),
                        ft.Text("Master the essential concepts and applications of Chemistry Fixed through interactive learning.", size=14),
                        ft.Text("🎯 Learning Objectives:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
                        ft.Column([
                            ft.Text("• Understand fundamental concepts", size=14),
                            ft.Text("• Apply knowledge to solve problems", size=14),
                            ft.Text("• Develop critical thinking skills", size=14),
                            ft.Text("• Connect ideas across disciplines", size=14),
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
            label="Ask about Chemistry Fixed...",
            hint_text="e.g., What are the key concepts?",
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
            "/chemistry_fixed/ai_help",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/chemistry_fixed")),
                    title=ft.Text("AI Chemistry Fixed Help"),
                    bgcolor=ft.Colors.TEAL_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("🤖 AI Chemistry Fixed Assistant", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                        query_field,
                        ft.ElevatedButton(
                            "Get Help",
                            on_click=handle_query,
                            style=ft.ButtonStyle(bgcolor=ft.Colors.TEAL_700, color=ft.Colors.WHITE)
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
            "/chemistry_fixed/quizzes",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/chemistry_fixed")),
                    title=ft.Text("Chemistry Fixed Quizzes"),
                    bgcolor=ft.Colors.TEAL_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("📝 Choose Quiz Level", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                        
                        ft.ResponsiveRow([
                            ft.Container(
                                ft.ElevatedButton(
                                    content=ft.Column([
                                        ft.Icon(ft.Icons.LOOKS_ONE, size=30, color=ft.Colors.GREEN_700),
                                        ft.Text("Basic", size=16, weight=ft.FontWeight.BOLD),
                                        ft.Text("Foundation concepts", size=12)
                                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                                    on_click=lambda e: self.start_quiz("basic"),
                                    style=ft.ButtonStyle(padding=20, bgcolor=ft.Colors.GREEN_50, shape=ft.RoundedRectangleBorder(radius=10))
                                ),
                                col={'xs': 12, 'sm': 4}
                            ),
                            ft.Container(
                                ft.ElevatedButton(
                                    content=ft.Column([
                                        ft.Icon(ft.Icons.LOOKS_TWO, size=30, color=ft.Colors.ORANGE_700),
                                        ft.Text("Intermediate", size=16, weight=ft.FontWeight.BOLD),
                                        ft.Text("Applied knowledge", size=12)
                                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                                    on_click=lambda e: self.start_quiz("intermediate"),
                                    style=ft.ButtonStyle(padding=20, bgcolor=ft.Colors.ORANGE_50, shape=ft.RoundedRectangleBorder(radius=10))
                                ),
                                col={'xs': 12, 'sm': 4}
                            ),
                            ft.Container(
                                ft.ElevatedButton(
                                    content=ft.Column([
                                        ft.Icon(ft.Icons.LOOKS_3, size=30, color=ft.Colors.RED_700),
                                        ft.Text("Advanced", size=16, weight=ft.FontWeight.BOLD),
                                        ft.Text("Expert level", size=12)
                                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                                    on_click=lambda e: self.start_quiz("advanced"),
                                    style=ft.ButtonStyle(padding=20, bgcolor=ft.Colors.RED_50, shape=ft.RoundedRectangleBorder(radius=10))
                                ),
                                col={'xs': 12, 'sm': 4}
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
            "/chemistry_fixed/quiz_question",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/chemistry_fixed/quizzes")),
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
            "/chemistry_fixed/quiz_explanation",
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
                            style=ft.ButtonStyle(bgcolor=ft.Colors.TEAL_700, color=ft.Colors.WHITE)
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
            "/chemistry_fixed/quiz_results",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/chemistry_fixed")),
                    title=ft.Text("Quiz Results"),
                    bgcolor=ft.Colors.TEAL_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("Quiz Complete!", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                        ft.Text(f"Score: {self.quiz_score}/{total_questions} ({percentage:.0f}%)", size=20),
                        ft.Text(message, size=18, color=color, weight=ft.FontWeight.BOLD),
                        ft.ElevatedButton(
                            "Try Again",
                            on_click=lambda e: self.start_quiz(self.current_quiz_level),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.TEAL_700, color=ft.Colors.WHITE)
                        ),
                        ft.ElevatedButton(
                            "Back to Chemistry Fixed",
                            on_click=lambda e: self.page.go("/chemistry_fixed")
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
                "title": "🎯 Core Concepts",
                "content": "Fundamental principles and ideas that form the foundation of Chemistry Fixed. Understanding these concepts is essential for building more advanced knowledge."
            },
            {
                "title": "🔬 Applications",
                "content": "Real-world applications and practical uses of Chemistry Fixed. These examples show how concepts connect to everyday life and professional fields."
            },
            {
                "title": "🧠 Problem Solving",
                "content": "Strategies and approaches for solving problems in Chemistry Fixed. Developing problem-solving skills is crucial for applying knowledge effectively."
            },
            {
                "title": "🔗 Connections",
                "content": "How Chemistry Fixed relates to other subjects and areas of knowledge. Understanding these connections helps develop a more complete understanding."
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
                        bgcolor=ft.Colors.BLUE_50,
                        border_radius=8
                    )
                ]
            )
            explanation_cards.append(card)
        
        view = ft.View(
            "/chemistry_fixed/explanations",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/chemistry_fixed")),
                    title=ft.Text("Chemistry Fixed Concepts"),
                    bgcolor=ft.Colors.TEAL_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("📚 Learn Chemistry Fixed", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                        ft.Text("Explore the fundamental concepts and applications", size=16, color=ft.Colors.BLUE_700),
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

    def show_practice(self):
        self.page.views.clear()
        
        view = ft.View(
            "/chemistry_fixed/practice",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/chemistry_fixed")),
                    title=ft.Text("Chemistry Fixed Practice"),
                    bgcolor=ft.Colors.TEAL_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("🎯 Practice Chemistry Fixed", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                        ft.Text("Interactive exercises and practice problems", size=16, color=ft.Colors.BLUE_700),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("🔧 Practice Activities", size=18, weight=ft.FontWeight.BOLD),
                                ft.Text("• Work through guided examples", size=14),
                                ft.Text("• Solve practice problems", size=14),
                                ft.Text("• Apply concepts to new situations", size=14),
                                ft.Text("• Review and reflect on learning", size=14),
                            ], spacing=5),
                            bgcolor=ft.Colors.BLUE_50,
                            border_radius=10,
                            padding=15,
                            border=ft.border.all(2, ft.Colors.BLUE_200)
                        ),
                        
                        ft.ElevatedButton(
                            "Start Practice Session",
                            on_click=lambda e: self.start_quiz("basic"),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.TEAL_700, color=ft.Colors.WHITE)
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

def chemistry_fixed_page(page: ft.Page):
    page.title = "Chemistry Fixed - Science Hub"
    page.scroll = ft.ScrollMode.AUTO
    
    # Clear page content first
    page.clean()
    
    page.appbar = ft.AppBar(
        leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: page.go("/science")),
        title=ft.Text("Chemistry Fixed"),
        bgcolor=ft.Colors.TEAL_700,
        center_title=True
    )
    
    module = ChemistryFixedModule(page)
    page.add(module.create_main_view())
