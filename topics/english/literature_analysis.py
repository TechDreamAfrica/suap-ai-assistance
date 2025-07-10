import flet as ft
import random

def get_ai_help(query, topic="literature_analysis"):
    """Enhanced AI help with comprehensive Literature Analysis knowledge"""
    try:
        responses = {
            "grammar": "Literature Analysis focuses on the rules and structure of language. Understanding grammar helps communicate clearly and effectively.",
            "writing": "Effective writing in Literature Analysis requires planning, organization, and careful attention to audience and purpose.",
            "reading": "Critical reading skills in Literature Analysis help analyze and interpret texts, identify main ideas, and understand author's intent.",
            "vocabulary": "Building vocabulary in Literature Analysis enhances communication skills and helps express ideas more precisely.",
            "style": "Writing style in Literature Analysis involves choosing appropriate tone, voice, and structure for different audiences and purposes.",
            "analysis": "Literary analysis in Literature Analysis involves examining themes, characters, plot, and literary devices to understand deeper meanings.",
            "expression": "Clear expression in Literature Analysis requires organizing thoughts logically and using appropriate language for the situation.",
            "communication": "Effective communication in Literature Analysis involves both speaking and listening skills, as well as understanding non-verbal cues.",
        }
        
        query_lower = query.lower()
        for key, response in responses.items():
            if key in query_lower:
                return f"🤖 AI Helper: {response}"
        
        return "🤖 AI Helper: I'm here to help with Literature Analysis concepts! Ask me about specific topics for detailed explanations."
    except Exception:
        return "🤖 AI Helper: I'm here to help with Literature Analysis concepts! Try asking about specific topics."

class LiteratureAnalysisModule:
    def __init__(self, page):
        self.page = page
        self.current_quiz_level = "basic"
        self.quiz_score = 0
        self.quiz_question_index = 0
        
        # Enhanced quiz questions with 50+ questions across three difficulty levels
        self.quiz_questions = {
            "basic": [
                {
                    "question": "What is the fundamental concept of Literature Analysis?",
                    "options": ['Basic concept', 'Advanced concept', 'Complex theory', 'Simple idea'],
                    "correct": 0,
                    "explanation": "This is the correct answer for Literature Analysis because it represents the fundamental understanding needed at the basic level."
                },
                {
                    "question": "Which of these is most important in Literature Analysis?",
                    "options": ['Understanding', 'Memorization', 'Speed', 'Guessing'],
                    "correct": 0,
                    "explanation": "This is the correct answer for Literature Analysis because it represents the fundamental understanding needed at the basic level."
                },
                {
                    "question": "What is the primary goal of studying Literature Analysis?",
                    "options": ['Learning', 'Testing', 'Competing', 'Passing'],
                    "correct": 0,
                    "explanation": "This is the correct answer for Literature Analysis because it represents the fundamental understanding needed at the basic level."
                },
                {
                    "question": "How would you describe Literature Analysis to a beginner?",
                    "options": ['Simple explanation', 'Complex theory', 'Advanced formula', 'Difficult concept'],
                    "correct": 0,
                    "explanation": "This is the correct answer for Literature Analysis because it represents the fundamental understanding needed at the basic level."
                },
                {
                    "question": "What is the best way to learn Literature Analysis?",
                    "options": ['Practice', 'Memorization', 'Guessing', 'Copying'],
                    "correct": 0,
                    "explanation": "This is the correct answer for Literature Analysis because it represents the fundamental understanding needed at the basic level."
                },
                {
                    "question": "Which skill is most developed through Literature Analysis?",
                    "options": ['Problem solving', 'Memory', 'Speed', 'Luck'],
                    "correct": 0,
                    "explanation": "This is the correct answer for Literature Analysis because it represents the fundamental understanding needed at the basic level."
                },
                {
                    "question": "What makes Literature Analysis important?",
                    "options": ['Real-world application', 'Test scores', 'Competition', 'Difficulty'],
                    "correct": 0,
                    "explanation": "This is the correct answer for Literature Analysis because it represents the fundamental understanding needed at the basic level."
                },
                {
                    "question": "How does Literature Analysis connect to other subjects?",
                    "options": ['Interdisciplinary', 'Isolated', 'Unrelated', 'Separate'],
                    "correct": 0,
                    "explanation": "This is the correct answer for Literature Analysis because it represents the fundamental understanding needed at the basic level."
                },
                {
                    "question": "What is the foundation of Literature Analysis?",
                    "options": ['Basic principles', 'Advanced theory', 'Complex formulas', 'Difficult concepts'],
                    "correct": 0,
                    "explanation": "This is the correct answer for Literature Analysis because it represents the fundamental understanding needed at the basic level."
                },
                {
                    "question": "Why is Literature Analysis taught in schools?",
                    "options": ['Essential knowledge', 'Tradition', 'Difficulty', 'Testing'],
                    "correct": 0,
                    "explanation": "This is the correct answer for Literature Analysis because it represents the fundamental understanding needed at the basic level."
                },
                {
                    "question": "What approach works best for Literature Analysis?",
                    "options": ['Step-by-step', 'Random', 'Rushed', 'Memorized'],
                    "correct": 0,
                    "explanation": "This is the correct answer for Literature Analysis because it represents the fundamental understanding needed at the basic level."
                },
                {
                    "question": "How can Literature Analysis be made easier?",
                    "options": ['Clear examples', 'More complexity', 'Faster pace', 'Less practice'],
                    "correct": 0,
                    "explanation": "This is the correct answer for Literature Analysis because it represents the fundamental understanding needed at the basic level."
                },
                {
                    "question": "What is the key to success in Literature Analysis?",
                    "options": ['Understanding', 'Speed', 'Memorization', 'Guessing'],
                    "correct": 0,
                    "explanation": "This is the correct answer for Literature Analysis because it represents the fundamental understanding needed at the basic level."
                },
                {
                    "question": "Which method helps learn Literature Analysis better?",
                    "options": ['Interactive practice', 'Passive reading', 'Memorization', 'Copying'],
                    "correct": 0,
                    "explanation": "This is the correct answer for Literature Analysis because it represents the fundamental understanding needed at the basic level."
                },
                {
                    "question": "What makes Literature Analysis interesting?",
                    "options": ['Practical applications', 'Difficulty', 'Complexity', 'Testing'],
                    "correct": 0,
                    "explanation": "This is the correct answer for Literature Analysis because it represents the fundamental understanding needed at the basic level."
                },
                {
                    "question": "How does Literature Analysis help in daily life?",
                    "options": ['Problem solving', 'Testing', 'Competition', 'Grades'],
                    "correct": 0,
                    "explanation": "This is the correct answer for Literature Analysis because it represents the fundamental understanding needed at the basic level."
                },
                {
                    "question": "What is the most important aspect of Literature Analysis?",
                    "options": ['Core concepts', 'Advanced topics', 'Difficult problems', 'Test preparation'],
                    "correct": 0,
                    "explanation": "This is the correct answer for Literature Analysis because it represents the fundamental understanding needed at the basic level."
                },
                {
                    "question": "How should beginners approach Literature Analysis?",
                    "options": ['Start with basics', 'Jump to advanced', 'Memorize everything', 'Skip fundamentals'],
                    "correct": 0,
                    "explanation": "This is the correct answer for Literature Analysis because it represents the fundamental understanding needed at the basic level."
                },
                {
                    "question": "What builds confidence in Literature Analysis?",
                    "options": ['Practice and success', 'Difficulty', 'Competition', 'Fear'],
                    "correct": 0,
                    "explanation": "This is the correct answer for Literature Analysis because it represents the fundamental understanding needed at the basic level."
                },
                {
                    "question": "Why is Literature Analysis considered valuable?",
                    "options": ['Develops thinking', 'Easy grades', 'Simple topics', 'No challenge'],
                    "correct": 0,
                    "explanation": "This is the correct answer for Literature Analysis because it represents the fundamental understanding needed at the basic level."
                },
            ],
            "intermediate": [
                {
                    "question": "What are the advanced concepts in Literature Analysis?",
                    "options": ['Complex applications', 'Basic ideas', 'Simple concepts', 'Elementary topics'],
                    "correct": 0,
                    "explanation": "This represents the intermediate level understanding of Literature Analysis, requiring deeper knowledge and application skills."
                },
                {
                    "question": "How do you apply Literature Analysis in real situations?",
                    "options": ['Practical problem solving', 'Memorization', 'Guessing', 'Copying'],
                    "correct": 0,
                    "explanation": "This represents the intermediate level understanding of Literature Analysis, requiring deeper knowledge and application skills."
                },
                {
                    "question": "What skills does Literature Analysis develop?",
                    "options": ['Critical thinking', 'Memory only', 'Speed only', 'Guessing only'],
                    "correct": 0,
                    "explanation": "This represents the intermediate level understanding of Literature Analysis, requiring deeper knowledge and application skills."
                },
                {
                    "question": "Which strategy works best for complex Literature Analysis problems?",
                    "options": ['Systematic approach', 'Random trying', 'Guessing', 'Memorization'],
                    "correct": 0,
                    "explanation": "This represents the intermediate level understanding of Literature Analysis, requiring deeper knowledge and application skills."
                },
                {
                    "question": "How does Literature Analysis connect to advanced topics?",
                    "options": ['Building blocks', 'Isolated topics', 'Unrelated concepts', 'Separate subjects'],
                    "correct": 0,
                    "explanation": "This represents the intermediate level understanding of Literature Analysis, requiring deeper knowledge and application skills."
                },
                {
                    "question": "What makes Literature Analysis challenging?",
                    "options": ['Complex relationships', 'Simple memorization', 'Easy concepts', 'Basic ideas'],
                    "correct": 0,
                    "explanation": "This represents the intermediate level understanding of Literature Analysis, requiring deeper knowledge and application skills."
                },
                {
                    "question": "How can you improve in Literature Analysis?",
                    "options": ['Deliberate practice', 'Passive reading', 'Memorization', 'Guessing'],
                    "correct": 0,
                    "explanation": "This represents the intermediate level understanding of Literature Analysis, requiring deeper knowledge and application skills."
                },
                {
                    "question": "What is the next level after basic Literature Analysis?",
                    "options": ['Advanced applications', 'Same level', 'Easier topics', 'Unrelated subjects'],
                    "correct": 0,
                    "explanation": "This represents the intermediate level understanding of Literature Analysis, requiring deeper knowledge and application skills."
                },
                {
                    "question": "How do experts approach Literature Analysis?",
                    "options": ['Pattern recognition', 'Memorization', 'Guessing', 'Random methods'],
                    "correct": 0,
                    "explanation": "This represents the intermediate level understanding of Literature Analysis, requiring deeper knowledge and application skills."
                },
                {
                    "question": "What makes Literature Analysis powerful?",
                    "options": ['Versatile applications', 'Limited use', 'Simple applications', 'No applications'],
                    "correct": 0,
                    "explanation": "This represents the intermediate level understanding of Literature Analysis, requiring deeper knowledge and application skills."
                },
                {
                    "question": "Which principle governs Literature Analysis?",
                    "options": ['Underlying logic', 'Random rules', 'Memorized facts', 'Guessed principles'],
                    "correct": 0,
                    "explanation": "This represents the intermediate level understanding of Literature Analysis, requiring deeper knowledge and application skills."
                },
                {
                    "question": "How does Literature Analysis relate to other fields?",
                    "options": ['Cross-disciplinary', 'Isolated', 'Unrelated', 'Separate'],
                    "correct": 0,
                    "explanation": "This represents the intermediate level understanding of Literature Analysis, requiring deeper knowledge and application skills."
                },
                {
                    "question": "What is the key insight in Literature Analysis?",
                    "options": ['Deep understanding', 'Surface knowledge', 'Memorization', 'Guessing'],
                    "correct": 0,
                    "explanation": "This represents the intermediate level understanding of Literature Analysis, requiring deeper knowledge and application skills."
                },
                {
                    "question": "How can Literature Analysis be mastered?",
                    "options": ['Consistent practice', 'Occasional study', 'Memorization', 'Guessing'],
                    "correct": 0,
                    "explanation": "This represents the intermediate level understanding of Literature Analysis, requiring deeper knowledge and application skills."
                },
                {
                    "question": "What distinguishes good Literature Analysis students?",
                    "options": ['Problem-solving ability', 'Memorization speed', 'Guessing accuracy', 'Test-taking skills'],
                    "correct": 0,
                    "explanation": "This represents the intermediate level understanding of Literature Analysis, requiring deeper knowledge and application skills."
                },
            ],
            "advanced": [
                {
                    "question": "What are the cutting-edge developments in Literature Analysis?",
                    "options": ['Latest research', 'Old methods', 'Basic concepts', 'Simple ideas'],
                    "correct": 0,
                    "explanation": "This represents advanced understanding of Literature Analysis, requiring sophisticated analysis and synthesis skills."
                },
                {
                    "question": "How do you create original solutions in Literature Analysis?",
                    "options": ['Creative thinking', 'Memorization', 'Copying', 'Guessing'],
                    "correct": 0,
                    "explanation": "This represents advanced understanding of Literature Analysis, requiring sophisticated analysis and synthesis skills."
                },
                {
                    "question": "What is the theoretical foundation of Literature Analysis?",
                    "options": ['Theoretical principles', 'Random rules', 'Memorized facts', 'Guessed theories'],
                    "correct": 0,
                    "explanation": "This represents advanced understanding of Literature Analysis, requiring sophisticated analysis and synthesis skills."
                },
                {
                    "question": "How does Literature Analysis advance knowledge?",
                    "options": ['Research and innovation', 'Memorization', 'Repetition', 'Copying'],
                    "correct": 0,
                    "explanation": "This represents advanced understanding of Literature Analysis, requiring sophisticated analysis and synthesis skills."
                },
                {
                    "question": "What are the limitations of Literature Analysis?",
                    "options": ['Boundary conditions', 'No limitations', 'Simple constraints', 'Easy boundaries'],
                    "correct": 0,
                    "explanation": "This represents advanced understanding of Literature Analysis, requiring sophisticated analysis and synthesis skills."
                },
                {
                    "question": "How do you prove results in Literature Analysis?",
                    "options": ['Rigorous methods', 'Guessing', 'Memorization', 'Copying'],
                    "correct": 0,
                    "explanation": "This represents advanced understanding of Literature Analysis, requiring sophisticated analysis and synthesis skills."
                },
                {
                    "question": "What is the future of Literature Analysis?",
                    "options": ['Emerging applications', 'Unchanged field', 'Declining importance', 'Simple applications'],
                    "correct": 0,
                    "explanation": "This represents advanced understanding of Literature Analysis, requiring sophisticated analysis and synthesis skills."
                },
                {
                    "question": "How does Literature Analysis influence other fields?",
                    "options": ['Interdisciplinary impact', 'No influence', 'Limited impact', 'Isolated field'],
                    "correct": 0,
                    "explanation": "This represents advanced understanding of Literature Analysis, requiring sophisticated analysis and synthesis skills."
                },
                {
                    "question": "What makes Literature Analysis research valuable?",
                    "options": ['Novel insights', 'Repetition', 'Memorization', 'Copying'],
                    "correct": 0,
                    "explanation": "This represents advanced understanding of Literature Analysis, requiring sophisticated analysis and synthesis skills."
                },
                {
                    "question": "How do you evaluate Literature Analysis theories?",
                    "options": ['Critical analysis', 'Acceptance', 'Memorization', 'Guessing'],
                    "correct": 0,
                    "explanation": "This represents advanced understanding of Literature Analysis, requiring sophisticated analysis and synthesis skills."
                },
                {
                    "question": "What is the complexity of Literature Analysis?",
                    "options": ['Multidimensional', 'Simple', 'Linear', 'Basic'],
                    "correct": 0,
                    "explanation": "This represents advanced understanding of Literature Analysis, requiring sophisticated analysis and synthesis skills."
                },
                {
                    "question": "How does Literature Analysis handle uncertainty?",
                    "options": ['Systematic methods', 'Ignoring uncertainty', 'Guessing', 'Memorization'],
                    "correct": 0,
                    "explanation": "This represents advanced understanding of Literature Analysis, requiring sophisticated analysis and synthesis skills."
                },
                {
                    "question": "What are the ethical considerations in Literature Analysis?",
                    "options": ['Responsible application', 'No ethics', 'Simple rules', 'Basic guidelines'],
                    "correct": 0,
                    "explanation": "This represents advanced understanding of Literature Analysis, requiring sophisticated analysis and synthesis skills."
                },
                {
                    "question": "How do you optimize Literature Analysis solutions?",
                    "options": ['Advanced algorithms', 'Random methods', 'Guessing', 'Memorization'],
                    "correct": 0,
                    "explanation": "This represents advanced understanding of Literature Analysis, requiring sophisticated analysis and synthesis skills."
                },
                {
                    "question": "What is the philosophical basis of Literature Analysis?",
                    "options": ['Fundamental principles', 'Random thoughts', 'Memorized ideas', 'Guessed concepts'],
                    "correct": 0,
                    "explanation": "This represents advanced understanding of Literature Analysis, requiring sophisticated analysis and synthesis skills."
                },
            ],
        }

    def create_main_view(self):
        return ft.Container(
            ft.Column([
                ft.Text("📚 Literature Analysis", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900, text_align=ft.TextAlign.CENTER),
                ft.Text("Explore the fundamentals and advanced concepts of Literature Analysis", size=16, color=ft.Colors.BLUE_700, text_align=ft.TextAlign.CENTER),
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
                        ft.Text("📖 Literature Analysis Overview", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800),
                        ft.Text("Master the essential concepts and applications of Literature Analysis through interactive learning.", size=14),
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
            label="Ask about Literature Analysis...",
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
            "/literature_analysis/ai_help",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/literature_analysis")),
                    title=ft.Text("AI Literature Analysis Help"),
                    bgcolor=ft.Colors.BLUE_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("🤖 AI Literature Analysis Assistant", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                        query_field,
                        ft.ElevatedButton(
                            "Get Help",
                            on_click=handle_query,
                            style=ft.ButtonStyle(bgcolor=ft.Colors.BLUE_700, color=ft.Colors.WHITE)
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
            "/literature_analysis/quizzes",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/literature_analysis")),
                    title=ft.Text("Literature Analysis Quizzes"),
                    bgcolor=ft.Colors.BLUE_700
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
            "/literature_analysis/quiz_question",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/literature_analysis/quizzes")),
                    title=ft.Text(f"Quiz - Question {self.quiz_question_index + 1}"),
                    bgcolor=ft.Colors.BLUE_700
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
            "/literature_analysis/quiz_explanation",
            [
                ft.AppBar(
                    title=ft.Text("Answer Explanation"),
                    bgcolor=ft.Colors.BLUE_700
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
                            style=ft.ButtonStyle(bgcolor=ft.Colors.BLUE_700, color=ft.Colors.WHITE)
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
            "/literature_analysis/quiz_results",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/literature_analysis")),
                    title=ft.Text("Quiz Results"),
                    bgcolor=ft.Colors.BLUE_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("Quiz Complete!", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                        ft.Text(f"Score: {self.quiz_score}/{total_questions} ({percentage:.0f}%)", size=20),
                        ft.Text(message, size=18, color=color, weight=ft.FontWeight.BOLD),
                        ft.ElevatedButton(
                            "Try Again",
                            on_click=lambda e: self.start_quiz(self.current_quiz_level),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.BLUE_700, color=ft.Colors.WHITE)
                        ),
                        ft.ElevatedButton(
                            "Back to Literature Analysis",
                            on_click=lambda e: self.page.go("/literature_analysis")
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
                "content": "Fundamental principles and ideas that form the foundation of Literature Analysis. Understanding these concepts is essential for building more advanced knowledge."
            },
            {
                "title": "🔬 Applications",
                "content": "Real-world applications and practical uses of Literature Analysis. These examples show how concepts connect to everyday life and professional fields."
            },
            {
                "title": "🧠 Problem Solving",
                "content": "Strategies and approaches for solving problems in Literature Analysis. Developing problem-solving skills is crucial for applying knowledge effectively."
            },
            {
                "title": "🔗 Connections",
                "content": "How Literature Analysis relates to other subjects and areas of knowledge. Understanding these connections helps develop a more complete understanding."
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
            "/literature_analysis/explanations",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/literature_analysis")),
                    title=ft.Text("Literature Analysis Concepts"),
                    bgcolor=ft.Colors.BLUE_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("📚 Learn Literature Analysis", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
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
            "/literature_analysis/practice",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/literature_analysis")),
                    title=ft.Text("Literature Analysis Practice"),
                    bgcolor=ft.Colors.BLUE_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("🎯 Practice Literature Analysis", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
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
                            style=ft.ButtonStyle(bgcolor=ft.Colors.BLUE_700, color=ft.Colors.WHITE)
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

def literature_analysis_page(page: ft.Page):
    page.title = "Literature Analysis - English Hub"
    page.scroll = ft.ScrollMode.AUTO
    
    # Clear page content first
    page.clean()
    
    page.appbar = ft.AppBar(
        leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: page.go("/english")),
        title=ft.Text("Literature Analysis"),
        bgcolor=ft.Colors.BLUE_700,
        center_title=True
    )
    
    module = LiteratureAnalysisModule(page)
    page.add(module.create_main_view())
