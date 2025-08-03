import flet as ft
import random
import math

class StatisticsProbabilityModule:
    def __init__(self, page=None):
        self.page = page
        self.current_quiz_questions = []
        self.current_question_index = 0
        self.user_answers = []
        self.quiz_score = 0
        self.quiz_difficulty = "basic"
        self.practice_test_questions = []
        self.practice_test_score = 0
        self.practice_test_answers = []
    
    def show_page(self):
        """Main entry point for the module"""
        self.show_main_page()
        
    def show_main_page(self, page=None):
        """Show the main statistics and probability page
        Args:
            page: Optional page reference. If not provided, uses self.page
        """
        if page is None:
            page = self.page
        self.page = page  # Update the page reference
            
        view = ft.View(
            "/statistics_probability",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: page.go_back()),
                    title=ft.Text("Statistics & Probability"),
                    bgcolor=ft.Colors.BLUE_700,
                    center_title=True
                ),
                self.create_main_view()
            ]
        )
        
        # Clear existing views and show main view
        page.views.clear()
        page.views.append(view)
        page.update()
        
        # Learning content data
        self.learning_content = {
            "descriptive": {
                "title": "Descriptive Statistics",
                "content": [
                    "Descriptive statistics summarize and describe data characteristics.",
                    "Mean: The average of all values (sum ÷ count).",
                    "Median: The middle value when data is arranged in order.",
                    "Mode: The most frequently occurring value in the dataset.",
                    "Range: The difference between maximum and minimum values.",
                    "Standard deviation measures how spread out data points are from the mean."
                ]
            },
            "probability": {
                "title": "Basic Probability",
                "content": [
                    "Probability measures the likelihood of an event occurring.",
                    "Probability = Number of favorable outcomes ÷ Total possible outcomes.",
                    "Probability values range from 0 (impossible) to 1 (certain).",
                    "Independent events: The outcome of one doesn't affect the other.",
                    "Dependent events: The outcome of one affects the probability of the other.",
                    "Conditional probability: P(A|B) = probability of A given that B has occurred."
                ]
            },
            "distributions": {
                "title": "Probability Distributions",
                "content": [
                    "A probability distribution shows all possible outcomes and their probabilities.",
                    "Normal distribution: Bell-shaped curve, symmetric around the mean.",
                    "Binomial distribution: For situations with two possible outcomes.",
                    "Uniform distribution: All outcomes are equally likely.",
                    "The area under a probability distribution curve equals 1.",
                    "68-95-99.7 rule: In normal distribution, data within 1, 2, 3 standard deviations."
                ]
            },
            "sampling": {
                "title": "Sampling and Inference",
                "content": [
                    "Sampling involves selecting a subset of a population for analysis.",
                    "Random sampling ensures each member has equal chance of selection.",
                    "Sample size affects the accuracy of population estimates.",
                    "Confidence intervals provide a range of likely values for a parameter.",
                    "Hypothesis testing determines if observed differences are significant.",
                    "P-value indicates the probability of getting results by chance alone."
                ]
            }
        }

    def statistics_probability_page(self, page: ft.Page):
        """Main Statistics & Probability page"""
        page.title = "Statistics & Probability - Mathematics Learning"
        page.scroll = ft.ScrollMode.AUTO
        page.clean()

        def go_back_to_main(e):
            page.go("/maths")

        # Main content with tabs
        def on_tab_change(e):
            selected_index = e.control.selected_index
            if selected_index == 0:
                self.show_learning_content(page)
            elif selected_index == 1:
                self.show_practice_quiz(page)
            elif selected_index == 2:
                self.show_ai_help(page)
            elif selected_index == 3:
                self.show_examples(page)

        # AppBar
        page.appbar = ft.AppBar(
            leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=go_back_to_main),
            title=ft.Text("Statistics & Probability", color=ft.Colors.WHITE),
            bgcolor=ft.Colors.BLUE_700,
            center_title=True
        )

        # Main container with tabs
        main_content = ft.Container(
            ft.Column([
                ft.Text(
                    "📊 Statistics & Probability",
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Text(
                    "Master statistical concepts and probability theory",
                    size=18,
                    color=ft.Colors.BLUE_700,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Divider(height=20),
                
                ft.Tabs(
                    selected_index=0,
                    on_change=on_tab_change,
                    tabs=[
                        ft.Tab(text="📚 Learn", icon=ft.Icons.SCHOOL),
                        ft.Tab(text="📝 Quiz", icon=ft.Icons.QUIZ),
                        ft.Tab(text="🤖 AI Help", icon=ft.Icons.SMART_TOY),
                        ft.Tab(text="💡 Examples", icon=ft.Icons.LIGHTBULB)
                    ],
                    indicator_color=ft.Colors.BLUE_700,
                    label_color=ft.Colors.BLUE_900,
                    unselected_label_color=ft.Colors.BLUE_400
                )
            ], spacing=20),
            padding=20,
            expand=True
        )
        
        page.add(main_content)
        # Show learning content by default
        self.show_learning_content(page)

    # Navigation helper methods
    def go_back_to_main(self, page: ft.Page):
        page.go("/maths")

    def go_back_to_statistics_main(self, page: ft.Page):
        self.statistics_probability_page(page)

    def show_learning_content(self, page: ft.Page):
        """Show learning content with topics"""
        page.clean()
        
        # AppBar
        page.appbar = ft.AppBar(
            leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.go_back_to_statistics_main(page)),
            title=ft.Text("Statistics & Probability - Learn", color=ft.Colors.WHITE),
            bgcolor=ft.Colors.BLUE_700,
            center_title=True
        )

        # Create learning content cards
        content_cards = []
        for topic_key, topic_data in self.learning_content.items():
            content_list = []
            for item in topic_data["content"]:
                content_list.append(ft.Text(f"• {item}", size=14, color=ft.Colors.BLUE_800))
            
            card = ft.Card(
                content=ft.Container(
                    ft.Column([
                        ft.Text(topic_data["title"], size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                        ft.Divider(height=10),
                        ft.Column(content_list, spacing=8)
                    ], spacing=10),
                    padding=20
                ),
                elevation=5,
                margin=ft.margin.only(bottom=15)
            )
            content_cards.append(card)

        # Main content
        content = ft.Container(
            ft.Column([
                ft.Text(
                    "📊 Statistics & Probability Learning",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Text(
                    "Master the fundamentals of statistics and probability",
                    size=16,
                    color=ft.Colors.BLUE_700,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Divider(height=20),
                
                ft.Column(content_cards, spacing=10, scroll=ft.ScrollMode.AUTO)
            ], spacing=20),
            padding=20,
            expand=True
        )
        
        page.add(content)

    def generate_quiz_questions(self, difficulty="basic"):
        """Generate quiz questions based on difficulty"""
        questions = []
        
        if difficulty == "basic":
            # Basic statistics and probability questions
            questions.extend([
                {
                    "question": "What is the mean of the numbers 4, 6, 8, 10?",
                    "options": ["6", "7", "8", "9"],
                    "correct": 1,
                    "explanation": "Mean = (4 + 6 + 8 + 10) ÷ 4 = 28 ÷ 4 = 7"
                },
                {
                    "question": "If you roll a fair six-sided die, what is the probability of rolling a 3?",
                    "options": ["1/6", "1/3", "1/2", "3/6"],
                    "correct": 0,
                    "explanation": "There is 1 favorable outcome (rolling 3) out of 6 possible outcomes, so P = 1/6"
                },
                {
                    "question": "What is the median of the numbers 2, 5, 8, 11, 14?",
                    "options": ["5", "8", "11", "7"],
                    "correct": 1,
                    "explanation": "The median is the middle value when numbers are arranged in order: 8"
                },
                {
                    "question": "If you flip a coin twice, what is the probability of getting two heads?",
                    "options": ["1/4", "1/2", "1/3", "2/3"],
                    "correct": 0,
                    "explanation": "P(HH) = P(H) × P(H) = 1/2 × 1/2 = 1/4"
                },
                {
                    "question": "What is the mode of the numbers 3, 5, 7, 5, 9, 5?",
                    "options": ["3", "5", "7", "9"],
                    "correct": 1,
                    "explanation": "The mode is the most frequently occurring value: 5 appears three times"
                }
            ])
        
        elif difficulty == "intermediate":
            questions.extend([
                {
                    "question": "What is the range of the numbers 12, 8, 15, 3, 20?",
                    "options": ["12", "15", "17", "20"],
                    "correct": 2,
                    "explanation": "Range = Maximum - Minimum = 20 - 3 = 17"
                },
                {
                    "question": "If P(A) = 0.3 and P(B) = 0.4, and A and B are independent, what is P(A and B)?",
                    "options": ["0.12", "0.7", "0.35", "0.24"],
                    "correct": 0,
                    "explanation": "For independent events: P(A and B) = P(A) × P(B) = 0.3 × 0.4 = 0.12"
                },
                {
                    "question": "In a normal distribution, approximately what percentage of data falls within 1 standard deviation of the mean?",
                    "options": ["68%", "95%", "99.7%", "50%"],
                    "correct": 0,
                    "explanation": "In a normal distribution, about 68% of data falls within 1 standard deviation of the mean"
                },
                {
                    "question": "What is the probability of drawing a red card from a standard deck of cards?",
                    "options": ["1/4", "1/2", "1/3", "2/3"],
                    "correct": 1,
                    "explanation": "There are 26 red cards out of 52 total cards, so P = 26/52 = 1/2"
                }
            ])
        
        elif difficulty == "advanced":
            questions.extend([
                {
                    "question": "If the standard deviation of a dataset is 5, what is the variance?",
                    "options": ["10", "25", "5", "√5"],
                    "correct": 1,
                    "explanation": "Variance = (Standard deviation)² = 5² = 25"
                },
                {
                    "question": "In a binomial distribution with n=10 and p=0.3, what is the expected value?",
                    "options": ["3", "7", "10", "0.3"],
                    "correct": 0,
                    "explanation": "Expected value = n × p = 10 × 0.3 = 3"
                },
                {
                    "question": "What is the probability of getting exactly 2 heads in 5 coin flips?",
                    "options": ["5/32", "10/32", "15/32", "20/32"],
                    "correct": 1,
                    "explanation": "Using binomial probability: C(5,2) × (1/2)² × (1/2)³ = 10 × 1/32 = 10/32"
                }
            ])
        
        return random.sample(questions, min(5, len(questions)))

    def show_practice_quiz(self, page: ft.Page):
        """Show practice quiz options"""
        page.clean()
        
        # AppBar
        page.appbar = ft.AppBar(
            leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.go_back_to_statistics_main(page)),
            title=ft.Text("Statistics & Probability - Quiz", color=ft.Colors.WHITE),
            bgcolor=ft.Colors.BLUE_700,
            center_title=True
        )

        # Quiz difficulty selection
        def start_quiz(e):
            difficulty = e.control.data
            self.quiz_difficulty = difficulty
            self.current_quiz_questions = self.generate_quiz_questions(difficulty)
            self.current_question_index = 0
            self.user_answers = []
            self.quiz_score = 0
            self.show_quiz_question(page)

        content = ft.Container(
            ft.Column([
                ft.Text(
                    "📝 Practice Quiz",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Text(
                    "Test your knowledge of statistics and probability",
                    size=16,
                    color=ft.Colors.BLUE_700,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Divider(height=30),
                
                ft.Text("Select Difficulty Level:", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                
                ft.Column([
                    ft.ElevatedButton(
                        "📚 Basic Level",
                        data="basic",
                        on_click=start_quiz,
                        style=ft.ButtonStyle(
                            padding=20,
                            bgcolor=ft.Colors.GREEN_100,
                            color=ft.Colors.GREEN_900,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        width=300
                    ),
                    ft.ElevatedButton(
                        "📊 Intermediate Level",
                        data="intermediate",
                        on_click=start_quiz,
                        style=ft.ButtonStyle(
                            padding=20,
                            bgcolor=ft.Colors.ORANGE_100,
                            color=ft.Colors.ORANGE_900,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        width=300
                    ),
                    ft.ElevatedButton(
                        "🏆 Advanced Level",
                        data="advanced",
                        on_click=start_quiz,
                        style=ft.ButtonStyle(
                            padding=20,
                            bgcolor=ft.Colors.RED_100,
                            color=ft.Colors.RED_900,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        width=300
                    )
                ], spacing=15, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            ], spacing=20, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=20,
            expand=True
        )
        
        page.add(content)

    def update_difficulty(self, difficulty):
        """Update quiz difficulty"""
        self.quiz_difficulty = difficulty

    def show_quiz_question(self, page: ft.Page):
        """Show current quiz question"""
        page.clean()
        
        if self.current_question_index >= len(self.current_quiz_questions):
            self.show_quiz_results(page)
            return

        question = self.current_quiz_questions[self.current_question_index]
        
        # AppBar
        page.appbar = ft.AppBar(
            leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.show_practice_quiz(page)),
            title=ft.Text(f"Question {self.current_question_index + 1}/{len(self.current_quiz_questions)}", color=ft.Colors.WHITE),
            bgcolor=ft.Colors.BLUE_700,
            center_title=True
        )

        # Question content
        def answer_question(e):
            selected_option = e.control.data
            self.answer_question(page, selected_option)

        option_buttons = []
        for i, option in enumerate(question["options"]):
            option_buttons.append(
                ft.ElevatedButton(
                    f"{chr(65 + i)}. {option}",
                    data=i,
                    on_click=answer_question,
                    style=ft.ButtonStyle(
                        padding=15,
                        bgcolor=ft.Colors.BLUE_50,
                        color=ft.Colors.BLUE_900,
                        shape=ft.RoundedRectangleBorder(radius=10)
                    ),
                    width=400
                )
            )

        content = ft.Container(
            ft.Column([
                ft.Text(
                    f"Question {self.current_question_index + 1}",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Container(
                    ft.Text(
                        question["question"],
                        size=18,
                        text_align=ft.TextAlign.CENTER,
                        color=ft.Colors.BLUE_800
                    ),
                    bgcolor=ft.Colors.BLUE_50,
                    border_radius=10,
                    padding=20,
                    margin=ft.margin.only(top=20, bottom=20)
                ),
                ft.Column(option_buttons, spacing=10, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            ], spacing=20, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=20,
            expand=True
        )
        
        page.add(content)

    def answer_question(self, page: ft.Page, selected_option):
        """Process answer and show feedback"""
        question = self.current_quiz_questions[self.current_question_index]
        is_correct = selected_option == question["correct"]
        
        self.user_answers.append(selected_option)
        if is_correct:
            self.quiz_score += 1
            
        self.show_answer_feedback(page, is_correct, question)

    def show_answer_feedback(self, page: ft.Page, is_correct, question):
        """Show feedback for the answer"""
        page.clean()
        
        # AppBar
        page.appbar = ft.AppBar(
            title=ft.Text("Answer Feedback", color=ft.Colors.WHITE),
            bgcolor=ft.Colors.BLUE_700,
            center_title=True,
            automatically_imply_leading=False
        )

        def next_question(e):
            self.current_question_index += 1
            self.show_quiz_question(page)

        feedback_color = ft.Colors.GREEN_700 if is_correct else ft.Colors.RED_700
        feedback_icon = ft.Icons.CHECK_CIRCLE if is_correct else ft.Icons.CANCEL
        feedback_text = "Correct!" if is_correct else "Incorrect!"

        content = ft.Container(
            ft.Column([
                ft.Icon(feedback_icon, size=60, color=feedback_color),
                ft.Text(
                    feedback_text,
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=feedback_color,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("Explanation:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                        ft.Text(question["explanation"], size=14, color=ft.Colors.BLUE_800)
                    ], spacing=10),
                    bgcolor=ft.Colors.BLUE_50,
                    border_radius=10,
                    padding=20,
                    margin=ft.margin.only(top=20, bottom=20)
                ),
                ft.ElevatedButton(
                    "Next Question" if self.current_question_index < len(self.current_quiz_questions) - 1 else "View Results",
                    on_click=next_question,
                    style=ft.ButtonStyle(
                        padding=20,
                        bgcolor=ft.Colors.BLUE_700,
                        color=ft.Colors.WHITE,
                        shape=ft.RoundedRectangleBorder(radius=10)
                    )
                )
            ], spacing=20, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=20,
            expand=True
        )
        
        page.add(content)

    def show_quiz_results(self, page: ft.Page):
        """Show quiz results and score"""
        page.clean()
        
        # AppBar
        page.appbar = ft.AppBar(
            title=ft.Text("Quiz Results", color=ft.Colors.WHITE),
            bgcolor=ft.Colors.BLUE_700,
            center_title=True,
            automatically_imply_leading=False
        )

        percentage = (self.quiz_score / len(self.current_quiz_questions)) * 100
        
        def retake_quiz(e):
            self.show_practice_quiz(page)

        def back_to_main(e):
            self.go_back_to_statistics_main(page)

        # Determine performance message
        if percentage >= 80:
            performance_msg = "Excellent work! 🎉"
            performance_color = ft.Colors.GREEN_700
        elif percentage >= 60:
            performance_msg = "Good job! 👍"
            performance_color = ft.Colors.BLUE_700
        else:
            performance_msg = "Keep practicing! 💪"
            performance_color = ft.Colors.ORANGE_700

        content = ft.Container(
            ft.Column([
                ft.Text(
                    "Quiz Complete!",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Container(
                    ft.Column([
                        ft.Text(f"Your Score: {self.quiz_score}/{len(self.current_quiz_questions)}", size=24, weight=ft.FontWeight.BOLD),
                        ft.Text(f"Percentage: {percentage:.1f}%", size=20),
                        ft.Text(performance_msg, size=18, color=performance_color, weight=ft.FontWeight.BOLD)
                    ], spacing=10, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    bgcolor=ft.Colors.BLUE_50,
                    border_radius=10,
                    padding=30,
                    margin=ft.margin.only(top=20, bottom=20)
                ),
                ft.Row([
                    ft.ElevatedButton(
                        "Retake Quiz",
                        on_click=retake_quiz,
                        style=ft.ButtonStyle(
                            padding=20,
                            bgcolor=ft.Colors.ORANGE_100,
                            color=ft.Colors.ORANGE_900,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        )
                    ),
                    ft.ElevatedButton(
                        "Back to Main",
                        on_click=back_to_main,
                        style=ft.ButtonStyle(
                            padding=20,
                            bgcolor=ft.Colors.BLUE_100,
                            color=ft.Colors.BLUE_900,
                            shape=ft.RoundedRectangleBorder(radius=10)
                        )
                    )
                ], spacing=20, alignment=ft.MainAxisAlignment.CENTER)
            ], spacing=20, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=20,
            expand=True
        )
        
        page.add(content)

    def show_ai_help(self, page: ft.Page):
        """Show AI help for statistics and probability"""
        page.clean()
        
        # AppBar
        page.appbar = ft.AppBar(
            leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.go_back_to_statistics_main(page)),
            title=ft.Text("Statistics & Probability - AI Help", color=ft.Colors.WHITE),
            bgcolor=ft.Colors.BLUE_700,
            center_title=True
        )

        # AI help topics
        def show_help_topic(e):
            topic = e.control.data
            self.show_specific_help(page, topic)

        help_topics = [
            ("mean_median_mode", "📊 Mean, Median, Mode"),
            ("basic_probability", "🎲 Basic Probability"),
            ("distributions", "📈 Probability Distributions"),
            ("sampling", "📋 Sampling Methods"),
            ("hypothesis_testing", "🔬 Hypothesis Testing"),
            ("confidence_intervals", "📏 Confidence Intervals")
        ]

        topic_buttons = []
        for topic_key, topic_title in help_topics:
            topic_buttons.append(
                ft.ElevatedButton(
                    topic_title,
                    data=topic_key,
                    on_click=show_help_topic,
                    style=ft.ButtonStyle(
                        padding=20,
                        bgcolor=ft.Colors.BLUE_50,
                        color=ft.Colors.BLUE_900,
                        shape=ft.RoundedRectangleBorder(radius=10)
                    ),
                    width=350
                )
            )

        content = ft.Container(
            ft.Column([
                ft.Text(
                    "🤖 AI Help - Statistics & Probability",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Text(
                    "Get help with specific statistics and probability topics",
                    size=16,
                    color=ft.Colors.BLUE_700,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Divider(height=30),
                
                ft.Text("Choose a topic for detailed help:", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                
                ft.Column(topic_buttons, spacing=15, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            ], spacing=20, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=20,
            expand=True
        )
        
        page.add(content)

    def show_specific_help(self, page: ft.Page, topic_key):
        """Show specific help for a topic"""
        help_content = {
            "mean_median_mode": {
                "title": "Mean, Median, Mode",
                "content": [
                    "MEAN (Average):",
                    "• Add all numbers and divide by count",
                    "• Example: (2, 4, 6, 8) → (2+4+6+8)÷4 = 5",
                    "",
                    "MEDIAN (Middle value):",
                    "• Arrange numbers in order, find middle",
                    "• Example: (2, 4, 6, 8, 10) → Median = 6",
                    "• For even count: average of two middle numbers",
                    "",
                    "MODE (Most frequent):",
                    "• The value that appears most often",
                    "• Example: (2, 3, 3, 4, 5) → Mode = 3"
                ]
            },
            "basic_probability": {
                "title": "Basic Probability",
                "content": [
                    "PROBABILITY FORMULA:",
                    "• P(event) = Favorable outcomes ÷ Total outcomes",
                    "• Values range from 0 to 1 (or 0% to 100%)",
                    "",
                    "EXAMPLES:",
                    "• Coin flip: P(heads) = 1/2 = 0.5",
                    "• Die roll: P(getting 3) = 1/6 ≈ 0.167",
                    "• Deck of cards: P(red card) = 26/52 = 1/2",
                    "",
                    "INDEPENDENT EVENTS:",
                    "• P(A and B) = P(A) × P(B)",
                    "• Example: P(two heads) = 1/2 × 1/2 = 1/4"
                ]
            },
            "distributions": {
                "title": "Probability Distributions",
                "content": [
                    "NORMAL DISTRIBUTION:",
                    "• Bell-shaped curve, symmetric around mean",
                    "• 68% of data within 1 standard deviation",
                    "• 95% within 2 standard deviations",
                    "• 99.7% within 3 standard deviations",
                    "",
                    "BINOMIAL DISTRIBUTION:",
                    "• For situations with exactly two outcomes",
                    "• Example: Number of heads in 10 coin flips",
                    "",
                    "UNIFORM DISTRIBUTION:",
                    "• All outcomes equally likely",
                    "• Example: Rolling a fair die"
                ]
            },
            "sampling": {
                "title": "Sampling Methods",
                "content": [
                    "RANDOM SAMPLING:",
                    "• Each member has equal chance of selection",
                    "• Reduces bias in results",
                    "",
                    "SAMPLE SIZE:",
                    "• Larger samples generally more accurate",
                    "• Trade-off between accuracy and cost",
                    "",
                    "SAMPLING ERROR:",
                    "• Difference between sample and population",
                    "• Decreases with larger sample sizes",
                    "",
                    "CONFIDENCE LEVEL:",
                    "• How sure we are about our estimate",
                    "• Common levels: 90%, 95%, 99%"
                ]
            },
            "hypothesis_testing": {
                "title": "Hypothesis Testing",
                "content": [
                    "NULL HYPOTHESIS (H₀):",
                    "• Statement of no effect or no difference",
                    "• What we assume to be true initially",
                    "",
                    "ALTERNATIVE HYPOTHESIS (H₁):",
                    "• Statement we want to test",
                    "• Opposite of null hypothesis",
                    "",
                    "P-VALUE:",
                    "• Probability of getting results by chance",
                    "• Small p-value (< 0.05) suggests significant result",
                    "",
                    "CONCLUSION:",
                    "• If p < 0.05: Reject null hypothesis",
                    "• If p ≥ 0.05: Fail to reject null hypothesis"
                ]
            },
            "confidence_intervals": {
                "title": "Confidence Intervals",
                "content": [
                    "DEFINITION:",
                    "• Range of values likely to contain true parameter",
                    "• Expressed as: estimate ± margin of error",
                    "",
                    "CONFIDENCE LEVEL:",
                    "• 95% confidence: If we repeated sampling 100 times,",
                    "  95 intervals would contain the true value",
                    "",
                    "MARGIN OF ERROR:",
                    "• Half the width of confidence interval",
                    "• Depends on sample size and confidence level",
                    "",
                    "INTERPRETATION:",
                    "• Wider interval = less precision",
                    "• Higher confidence = wider interval"
                ]
            }
        }

        topic_data = help_content.get(topic_key, {"title": "Topic", "content": ["Help content not available."]})
        
        page.clean()
        
        # AppBar
        page.appbar = ft.AppBar(
            leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.show_ai_help(page)),
            title=ft.Text(f"AI Help - {topic_data['title']}", color=ft.Colors.WHITE),
            bgcolor=ft.Colors.BLUE_700,
            center_title=True
        )

        # Content
        content_items = []
        for item in topic_data["content"]:
            if item == "":
                content_items.append(ft.Divider(height=10))
            else:
                content_items.append(ft.Text(item, size=14, color=ft.Colors.BLUE_800))

        content = ft.Container(
            ft.Column([
                ft.Text(
                    f"🤖 {topic_data['title']}",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Container(
                    ft.Column(content_items, spacing=8),
                    bgcolor=ft.Colors.BLUE_50,
                    border_radius=10,
                    padding=20,
                    margin=ft.margin.only(top=20)
                )
            ], spacing=20),
            padding=20,
            expand=True
        )
        
        page.add(content)

    def show_examples(self, page: ft.Page):
        """Show worked examples"""
        page.clean()
        
        # AppBar
        page.appbar = ft.AppBar(
            leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.go_back_to_statistics_main(page)),
            title=ft.Text("Statistics & Probability - Examples", color=ft.Colors.WHITE),
            bgcolor=ft.Colors.BLUE_700,
            center_title=True
        )

        # Example problems
        examples = [
            {
                "title": "Finding Mean, Median, Mode",
                "problem": "Find the mean, median, and mode of: 2, 3, 5, 3, 7, 3, 8",
                "solution": [
                    "Mean = (2 + 3 + 5 + 3 + 7 + 3 + 8) ÷ 7 = 31 ÷ 7 ≈ 4.43",
                    "Median: Arrange in order: 2, 3, 3, 3, 5, 7, 8",
                    "Middle value (4th position) = 3",
                    "Mode = 3 (appears most frequently - 3 times)"
                ]
            },
            {
                "title": "Basic Probability",
                "problem": "What's the probability of drawing a face card from a standard deck?",
                "solution": [
                    "Face cards: Jacks, Queens, Kings",
                    "Number of face cards = 4 × 3 = 12",
                    "Total cards = 52",
                    "P(face card) = 12/52 = 3/13 ≈ 0.231 or 23.1%"
                ]
            },
            {
                "title": "Independent Events",
                "problem": "What's the probability of rolling two 6s with two dice?",
                "solution": [
                    "P(first die shows 6) = 1/6",
                    "P(second die shows 6) = 1/6",
                    "Since events are independent:",
                    "P(both show 6) = 1/6 × 1/6 = 1/36 ≈ 0.028 or 2.8%"
                ]
            },
            {
                "title": "Normal Distribution",
                "problem": "In a normal distribution with mean 100 and standard deviation 15, what percentage of values fall between 85 and 115?",
                "solution": [
                    "85 = 100 - 15 = mean - 1 standard deviation",
                    "115 = 100 + 15 = mean + 1 standard deviation",
                    "By the 68-95-99.7 rule:",
                    "About 68% of values fall within 1 standard deviation",
                    "Therefore, 68% of values fall between 85 and 115"
                ]
            }
        ]

        example_cards = []
        for example in examples:
            solution_items = []
            for step in example["solution"]:
                solution_items.append(ft.Text(f"• {step}", size=13, color=ft.Colors.BLUE_800))
            
            card = ft.Card(
                content=ft.Container(
                    ft.Column([
                        ft.Text(example["title"], size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                        ft.Text("Problem:", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800),
                        ft.Text(example["problem"], size=14, color=ft.Colors.BLUE_700),
                        ft.Text("Solution:", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800),
                        ft.Column(solution_items, spacing=5)
                    ], spacing=10),
                    padding=15
                ),
                elevation=3,
                margin=ft.margin.only(bottom=15)
            )
            example_cards.append(card)

        content = ft.Container(
            ft.Column([
                ft.Text(
                    "💡 Worked Examples",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE_900,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Text(
                    "Step-by-step solutions to common statistics and probability problems",
                    size=16,
                    color=ft.Colors.BLUE_700,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Divider(height=20),
                
                ft.Column(example_cards, spacing=10, scroll=ft.ScrollMode.AUTO)
            ], spacing=20),
            padding=20,
            expand=True
        )
        
        page.add(content)

def show_examples(page):
    """Show examples"""
    page.snack_bar = ft.SnackBar(
        content=ft.Text("Examples section coming soon! Explore worked examples and detailed explanations."),
        bgcolor=ft.Colors.ORANGE_100
    )
    page.snack_bar.open = True
    page.update()


def statistics_probability_page(page: ft.Page):
    """Main entry point for Statistics & Probability module"""
    module = StatisticsProbabilityModule()
    module.show_main_page(page)
