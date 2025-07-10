import flet as ft
import random
import math

def get_arithmetic_ai_help(query, topic="basic_arithmetic"):
    """AI help for Basic Arithmetic concepts"""
    try:
        responses = {
            "addition": "Addition is combining two or more numbers to get their sum. Start with smaller numbers and use strategies like counting on, making 10, or using number lines.",
            "subtraction": "Subtraction is taking away one number from another. Think of it as the opposite of addition. Use strategies like counting back, number lines, or borrowing in multi-digit problems.",
            "multiplication": "Multiplication is repeated addition. For example, 3 × 4                                    on_click=lambda e: self.page.go_back(),means adding 3 four times (3+3+3+3=12). Learn times tables and use strategies like skip counting.",
            "division": "Division is splitting a number into equal groups. It's the opposite of multiplication. For example, 12 ÷ 3 means how many groups of 3 can you make from 12?",
            "order": "Order of operations follows PEMDAS: Parentheses, Exponents, Multiplication/Division (left to right), Addition/Subtraction (left to right).",
            "decimal": "Decimals represent parts of whole numbers. The place value determines the decimal's worth - tenths, hundredths, thousandths, etc.",
            "fraction": "Fractions show parts of a whole. The top number (numerator) shows how many parts you have, the bottom (denominator) shows total parts.",
            "rounding": "Rounding makes numbers simpler to work with. Look at the digit to the right of where you're rounding - if it's 5 or more, round up; if less than 5, round down.",
            "estimation": "Estimation helps you check if your answer makes sense. Round numbers to make quick mental calculations before solving exactly.",
            "word problem": "For word problems: 1) Read carefully, 2) Identify what you need to find, 3) Determine which operation to use, 4) Solve, 5) Check if your answer makes sense.",
        }
        
        query_lower = query.lower()
        for key, response in responses.items():
            if key in query_lower:
                return f"🤖 Math AI Helper: {response}"
        
        return f"🤖 Math AI Helper: I can help with addition, subtraction, multiplication, division, order of operations, decimals, fractions, rounding, estimation, and word problems. Ask me about any specific topic!"
    except Exception:
        return f"🤖 Math AI Helper: I'm here to help with basic arithmetic! Ask about specific operations or concepts."

def basic_arithmetic_page(page: ft.Page):
    """Basic Arithmetic learning page"""
    page.title = f"Basic Arithmetic - Mathematics Learning"
    page.scroll = ft.ScrollMode.AUTO
    
    # Clear page content first
    page.clean()
    
    # Create module instance
    module = BasicArithmeticModule(page)
    
    # AppBar with back button
    page.appbar = ft.AppBar(
        leading=ft.IconButton(
            ft.Icons.ARROW_BACK,
            on_click=lambda e: page.go("/maths")
        ),
        title=ft.Text("Basic Arithmetic"),
        bgcolor=ft.Colors.BLUE_700,
        center_title=True
    )
    
    # Add main view
    page.add(module.create_main_view())

class BasicArithmeticModule:
    def __init__(self, page):
        self.page = page
        self.current_quiz_level = "basic"
        self.quiz_score = 0
        self.quiz_question_index = 0
        self.current_correct_index = 0
        self.current_shuffled_options = []  # Store shuffled options for feedback
        
        # Comprehensive quiz questions (50+ questions across different levels)
        self.quiz_questions = {
            "basic": [
                # Addition Questions (1-15)
                {"question": "What is 7 + 5?", "options": ["12", "11", "13", "10"], "correct": 0, "explanation": "7 + 5 = 12. Count on from 7: 8, 9, 10, 11, 12."},
                {"question": "What is 15 + 8?", "options": ["22", "23", "24", "21"], "correct": 1, "explanation": "15 + 8 = 23. Break it down: 15 + 5 = 20, then 20 + 3 = 23."},
                {"question": "What is 34 + 29?", "options": ["63", "62", "64", "61"], "correct": 0, "explanation": "34 + 29 = 63. Add ones: 4 + 9 = 13 (write 3, carry 1). Add tens: 3 + 2 + 1 = 6."},
                {"question": "What is 156 + 87?", "options": ["243", "242", "244", "241"], "correct": 0, "explanation": "156 + 87 = 243. Add column by column: 6+7=13, 5+8+1=14, 1+0+1=2."},
                {"question": "What is 0 + 25?", "options": ["25", "0", "50", "1"], "correct": 0, "explanation": "Adding zero to any number gives the same number. 0 + 25 = 25."},
                
                # Subtraction Questions (16-30)
                {"question": "What is 12 - 5?", "options": ["7", "8", "6", "9"], "correct": 0, "explanation": "12 - 5 = 7. Count back from 12: 11, 10, 9, 8, 7."},
                {"question": "What is 23 - 9?", "options": ["14", "15", "13", "16"], "correct": 0, "explanation": "23 - 9 = 14. Break it down: 23 - 3 = 20, then 20 - 6 = 14."},
                {"question": "What is 50 - 27?", "options": ["23", "24", "22", "25"], "correct": 0, "explanation": "50 - 27 = 23. Borrow from tens: 50 becomes 40 + 10, then 10 - 7 = 3, 4 - 2 = 2."},
                {"question": "What is 100 - 45?", "options": ["55", "54", "56", "53"], "correct": 0, "explanation": "100 - 45 = 55. Think: 100 - 40 = 60, then 60 - 5 = 55."},
                {"question": "What is 75 - 0?", "options": ["75", "0", "70", "5"], "correct": 0, "explanation": "Subtracting zero from any number gives the same number. 75 - 0 = 75."},
                
                # Basic Multiplication (31-40)
                {"question": "What is 6 × 3?", "options": ["18", "17", "19", "16"], "correct": 0, "explanation": "6 × 3 = 18. Think of it as 6 + 6 + 6 = 18."},
                {"question": "What is 7 × 4?", "options": ["28", "27", "29", "26"], "correct": 0, "explanation": "7 × 4 = 28. Count by 7s: 7, 14, 21, 28."},
                {"question": "What is 9 × 5?", "options": ["45", "44", "46", "43"], "correct": 0, "explanation": "9 × 5 = 45. When multiplying by 5, the answer ends in 0 or 5."},
                {"question": "What is 8 × 0?", "options": ["0", "8", "80", "1"], "correct": 0, "explanation": "Any number multiplied by 0 equals 0. 8 × 0 = 0."},
                {"question": "What is 12 × 2?", "options": ["24", "23", "25", "22"], "correct": 0, "explanation": "12 × 2 = 24. Double 12: 12 + 12 = 24."},
                
                # Basic Division (41-50)
                {"question": "What is 15 ÷ 3?", "options": ["5", "4", "6", "3"], "correct": 0, "explanation": "15 ÷ 3 = 5. How many groups of 3 in 15? 3, 6, 9, 12, 15 = 5 groups."},
                {"question": "What is 24 ÷ 4?", "options": ["6", "5", "7", "4"], "correct": 0, "explanation": "24 ÷ 4 = 6. Think: 4 × 6 = 24, so 24 ÷ 4 = 6."},
                {"question": "What is 35 ÷ 5?", "options": ["7", "6", "8", "5"], "correct": 0, "explanation": "35 ÷ 5 = 7. Count by 5s to 35: 5, 10, 15, 20, 25, 30, 35 = 7 counts."},
                {"question": "What is 0 ÷ 8?", "options": ["0", "8", "1", "Cannot divide"], "correct": 0, "explanation": "Zero divided by any non-zero number equals 0. 0 ÷ 8 = 0."},
                {"question": "What is 48 ÷ 6?", "options": ["8", "7", "9", "6"], "correct": 0, "explanation": "48 ÷ 6 = 8. Think: 6 × 8 = 48, so 48 ÷ 6 = 8."}
            ],
            "intermediate": [
                # Multi-digit operations and word problems
                {"question": "Sarah has 145 stickers. She gives away 67 stickers. How many does she have left?", "options": ["78", "77", "79", "76"], "correct": 0, "explanation": "145 - 67 = 78. This is a subtraction word problem."},
                {"question": "A box contains 24 pencils. How many pencils are in 7 boxes?", "options": ["168", "167", "169", "166"], "correct": 0, "explanation": "24 × 7 = 168. Multiply: 24 × 7 = (20 × 7) + (4 × 7) = 140 + 28 = 168."},
                {"question": "What is 456 + 789?", "options": ["1245", "1244", "1246", "1243"], "correct": 0, "explanation": "456 + 789 = 1245. Add column by column: 6+9=15, 5+8+1=14, 4+7+1=12."},
                {"question": "What is 832 - 495?", "options": ["337", "336", "338", "335"], "correct": 0, "explanation": "832 - 495 = 337. Use borrowing for each column."},
                {"question": "What is 15 × 23?", "options": ["345", "344", "346", "343"], "correct": 0, "explanation": "15 × 23 = 345. Use the standard algorithm: 15 × 3 = 45, 15 × 20 = 300, total = 345."},
                {"question": "What is 144 ÷ 12?", "options": ["12", "11", "13", "10"], "correct": 0, "explanation": "144 ÷ 12 = 12. Think: 12 × 12 = 144."},
                {"question": "Round 347 to the nearest hundred.", "options": ["300", "400", "350", "340"], "correct": 0, "explanation": "347 rounds to 300. The tens digit is 4, which is less than 5, so round down."},
                {"question": "What is 0.5 + 0.3?", "options": ["0.8", "0.7", "0.9", "0.6"], "correct": 0, "explanation": "0.5 + 0.3 = 0.8. Add the decimal parts: 5 + 3 = 8 tenths."},
                {"question": "What is 2.7 - 1.4?", "options": ["1.3", "1.2", "1.4", "1.1"], "correct": 0, "explanation": "2.7 - 1.4 = 1.3. Subtract the decimal parts: 7 - 4 = 3 tenths, 2 - 1 = 1."},
                {"question": "What is 1/2 + 1/4?", "options": ["3/4", "2/4", "1/4", "4/4"], "correct": 0, "explanation": "1/2 + 1/4 = 2/4 + 1/4 = 3/4. Convert 1/2 to 2/4 first."},
                {"question": "If you buy 3 packs of gum for $1.25 each, how much do you spend?", "options": ["$3.75", "$3.50", "$4.00", "$3.25"], "correct": 0, "explanation": "$1.25 × 3 = $3.75. Multiply the price by the number of packs."},
                {"question": "What is 6² (6 squared)?", "options": ["36", "35", "37", "34"], "correct": 0, "explanation": "6² = 6 × 6 = 36. Squaring means multiplying a number by itself."},
                {"question": "What is 100 ÷ 4?", "options": ["25", "24", "26", "23"], "correct": 0, "explanation": "100 ÷ 4 = 25. Think: 4 × 25 = 100."},
                {"question": "What is 7 × 8 × 0?", "options": ["0", "56", "7", "8"], "correct": 0, "explanation": "Any multiplication involving 0 equals 0. 7 × 8 × 0 = 0."},
                {"question": "Estimate 89 + 112 by rounding to the nearest ten.", "options": ["200", "190", "210", "180"], "correct": 0, "explanation": "89 rounds to 90, 112 rounds to 110. 90 + 110 = 200."}
            ],
            "advanced": [
                # Complex problems and applications
                {"question": "What is (12 + 8) × (15 - 7)?", "options": ["160", "159", "161", "158"], "correct": 0, "explanation": "(12 + 8) × (15 - 7) = 20 × 8 = 160. Follow order of operations: parentheses first."},
                {"question": "A recipe calls for 2.5 cups of flour. If you want to make 3 batches, how much flour do you need?", "options": ["7.5 cups", "7 cups", "8 cups", "6.5 cups"], "correct": 0, "explanation": "2.5 × 3 = 7.5 cups. Multiply the amount per batch by the number of batches."},
                {"question": "What is 15% of 80?", "options": ["12", "11", "13", "10"], "correct": 0, "explanation": "15% of 80 = 0.15 × 80 = 12. Convert percentage to decimal and multiply."},
                {"question": "If 5x = 35, what is x?", "options": ["7", "6", "8", "5"], "correct": 0, "explanation": "x = 35 ÷ 5 = 7. Divide both sides by 5 to solve for x."},
                {"question": "What is the average of 12, 16, 20, and 24?", "options": ["18", "17", "19", "16"], "correct": 0, "explanation": "(12 + 16 + 20 + 24) ÷ 4 = 72 ÷ 4 = 18. Add all numbers and divide by count."},
                {"question": "What is 3⁴ (3 to the power of 4)?", "options": ["81", "80", "82", "79"], "correct": 0, "explanation": "3⁴ = 3 × 3 × 3 × 3 = 9 × 9 = 81."},
                {"question": "What is √64?", "options": ["8", "7", "9", "6"], "correct": 0, "explanation": "√64 = 8 because 8 × 8 = 64."},
                {"question": "Convert 3/5 to a decimal.", "options": ["0.6", "0.5", "0.7", "0.4"], "correct": 0, "explanation": "3 ÷ 5 = 0.6. Divide the numerator by the denominator."},
                {"question": "What is 2.4 × 1.5?", "options": ["3.6", "3.5", "3.7", "3.4"], "correct": 0, "explanation": "2.4 × 1.5 = 3.6. Multiply: 24 × 15 = 360, then place decimal (1+1=2 places)."},
                {"question": "If a car travels 240 miles in 4 hours, what is its average speed?", "options": ["60 mph", "59 mph", "61 mph", "58 mph"], "correct": 0, "explanation": "Speed = Distance ÷ Time = 240 ÷ 4 = 60 miles per hour."}
            ]
        }

    def create_main_view(self):
        return ft.Container(
            ft.Column([
                ft.Text("🧮 Basic Arithmetic", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900, text_align=ft.TextAlign.CENTER),
                ft.Text("Master the fundamental operations of mathematics", size=16, color=ft.Colors.BLUE_700, text_align=ft.TextAlign.CENTER),
                ft.Divider(height=30),
                
                # Navigation buttons
                ft.ResponsiveRow([
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.HELP, size=30, color=ft.Colors.BLUE_700),
                                ft.Text("Math AI Help", size=14, weight=ft.FontWeight.BOLD)
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
                                ft.Icon(ft.Icons.SCHOOL_OUTLINED, size=30, color=ft.Colors.PURPLE_700),
                                ft.Text("Learn Topics", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_learning_content(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.PURPLE_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.FITNESS_CENTER, size=30, color=ft.Colors.ORANGE_700),
                                ft.Text("Practice Test", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_practice_test(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.ORANGE_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                ], spacing=10, run_spacing=10),
                
                ft.Divider(height=20),
                
                # Learning overview
                ft.Container(
                    ft.Column([
                        ft.Text("📚 What You'll Learn", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800),
                        ft.Text("Master the four basic operations and their applications", size=14),
                        
                        ft.Text("🎯 Learning Topics:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
                        ft.Column([
                            ft.Text("➕ Addition: Single and multi-digit numbers", size=14),
                            ft.Text("➖ Subtraction: With and without borrowing", size=14),
                            ft.Text("✖️ Multiplication: Times tables and multi-digit", size=14),
                            ft.Text("➗ Division: Basic division and remainders", size=14),
                            ft.Text("🔢 Decimals: Adding, subtracting decimals", size=14),
                            ft.Text("📊 Fractions: Basic fraction operations", size=14),
                            ft.Text("📝 Word Problems: Real-world applications", size=14),
                        ], spacing=5),
                        
                        # Quick stats
                        ft.ResponsiveRow([
                            ft.Container(
                                ft.Column([
                                    ft.Icon(ft.Icons.QUIZ, size=25, color=ft.Colors.BLUE_700),
                                    ft.Text("50+", size=16, weight=ft.FontWeight.BOLD),
                                    ft.Text("Quiz Questions", size=12)
                                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                                bgcolor=ft.Colors.BLUE_50,
                                border_radius=10,
                                padding=10,
                                col={'xs': 6, 'sm': 3}
                            ),
                            ft.Container(
                                ft.Column([
                                    ft.Icon(ft.Icons.SMART_TOY, size=25, color=ft.Colors.GREEN_700),
                                    ft.Text("AI", size=16, weight=ft.FontWeight.BOLD),
                                    ft.Text("Helper", size=12)
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
                                    ft.Icon(ft.Icons.ASSIGNMENT, size=25, color=ft.Colors.ORANGE_700),
                                    ft.Text("Tests", size=16, weight=ft.FontWeight.BOLD),
                                    ft.Text("& Practice", size=12)
                                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                                bgcolor=ft.Colors.ORANGE_50,
                                border_radius=10,
                                padding=10,
                                col={'xs': 6, 'sm': 3}
                            ),
                        ], spacing=10, run_spacing=10)
                    ], spacing=15),
                    bgcolor=ft.Colors.BLUE_50,
                    border_radius=10,
                    padding=15,
                    border=ft.border.all(2, ft.Colors.BLUE_200)
                )
            ], spacing=20),
            padding=20,
            expand=True
        )

    # Navigation helper methods
    def go_back_to_main(self):
        """Navigate back to the main Basic Arithmetic page"""
        self.page.views.clear()
        self.page.add(self.create_main_view())
        self.page.update()
    
    def go_back_to_quizzes(self):
        """Navigate back to the quiz selection page"""
        self.show_quizzes()
    
    def go_back_to_quiz_question(self):
        """Navigate back to the current quiz question"""
        self.show_quiz_question()

    # AI Help methods
    def show_ai_help(self):
        self.page.views.clear()
        
        query_field = ft.TextField(
            label="Ask about Basic Arithmetic...",
            hint_text="e.g., How do I add multi-digit numbers? What's the best way to memorize times tables?",
            multiline=True,
            min_lines=3,
            expand=True
        )
        
        response_text = ft.Text("", size=14, selectable=True)
        
        def handle_query(e):
            if query_field.value:
                response = get_arithmetic_ai_help(query_field.value)
                response_text.value = response
                self.page.update()
        
        view = ft.View(
            "/basic_arithmetic/ai_help",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.go_back_to_main()),
                    title=ft.Text("Math AI Helper - Basic Arithmetic"),
                    bgcolor=ft.Colors.BLUE_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("🤖 Math AI Assistant", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                        ft.Text("Get personalized help with basic arithmetic concepts", size=16, color=ft.Colors.BLUE_700),
                        query_field,
                        ft.ElevatedButton(
                            "Get Help",
                            on_click=handle_query,
                            style=ft.ButtonStyle(bgcolor=ft.Colors.BLUE_700, color=ft.Colors.WHITE)
                        ),
                        ft.Container(response_text, bgcolor=ft.Colors.GREY_100, border_radius=10, padding=15, expand=True),
                        
                        # Quick help topics
                        ft.Text("💡 Quick Help Topics:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
                        ft.ResponsiveRow([
                            ft.Container(
                                ft.ElevatedButton(
                                    "Addition Tips",
                                    on_click=lambda e: (setattr(query_field, 'value', 'addition'), handle_query(e)),
                                    style=ft.ButtonStyle(bgcolor=ft.Colors.GREEN_50)
                                ),
                                col={'xs': 6, 'sm': 3}
                            ),
                            ft.Container(
                                ft.ElevatedButton(
                                    "Subtraction Help",
                                    on_click=lambda e: (setattr(query_field, 'value', 'subtraction'), handle_query(e)),
                                    style=ft.ButtonStyle(bgcolor=ft.Colors.ORANGE_50)
                                ),
                                col={'xs': 6, 'sm': 3}
                            ),
                            ft.Container(
                                ft.ElevatedButton(
                                    "Multiplication",
                                    on_click=lambda e: (setattr(query_field, 'value', 'multiplication'), handle_query(e)),
                                    style=ft.ButtonStyle(bgcolor=ft.Colors.PURPLE_50)
                                ),
                                col={'xs': 6, 'sm': 3}
                            ),
                            ft.Container(
                                ft.ElevatedButton(
                                    "Division Guide",
                                    on_click=lambda e: (setattr(query_field, 'value', 'division'), handle_query(e)),
                                    style=ft.ButtonStyle(bgcolor=ft.Colors.PINK_50)
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

    def show_quizzes(self):
        self.page.views.clear()
        
        view = ft.View(
            "/basic_arithmetic/quizzes",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.go_back_to_main()),
                    title=ft.Text("Basic Arithmetic Quizzes"),
                    bgcolor=ft.Colors.GREEN_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("📝 Choose Your Quiz Level", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_900),
                        ft.Text("Select the difficulty level that matches your skill", size=16, color=ft.Colors.GREEN_700),
                        
                        ft.ResponsiveRow([
                            ft.Container(
                                ft.Card(
                                    ft.Container(
                                        ft.Column([
                                            ft.Icon(ft.Icons.STAR_OUTLINE, size=40, color=ft.Colors.GREEN_600),
                                            ft.Text("Basic Level", size=18, weight=ft.FontWeight.BOLD),
                                            ft.Text("Addition, Subtraction\nBasic Multiplication & Division", text_align=ft.TextAlign.CENTER),
                                            ft.Text("20 Questions", size=12, color=ft.Colors.GREEN_600),
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
                                            ft.Text("Multi-digit Operations\nWord Problems & Decimals", text_align=ft.TextAlign.CENTER),
                                            ft.Text("15 Questions", size=12, color=ft.Colors.ORANGE_600),
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
                                            ft.Text("Complex Operations\nPercentages & Algebra", text_align=ft.TextAlign.CENTER),
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
        
        # Shuffle questions for variety
        questions = self.quiz_questions[level].copy()
        random.shuffle(questions)
        self.current_quiz_questions = questions[:min(len(questions), 10)]  # Limit to 10 questions per quiz
        
        self.show_quiz_question()

    def show_quiz_question(self):
        if self.quiz_question_index >= len(self.current_quiz_questions):
            self.show_quiz_results()
            return
        
        question_data = self.current_quiz_questions[self.quiz_question_index]
        
        # Randomize answer options
        options = question_data["options"].copy()
        correct_answer = options[question_data["correct"]]
        
        # Shuffle options and find new correct index
        random.shuffle(options)
        new_correct_index = options.index(correct_answer)
        
        # Store the shuffled state for feedback
        self.current_correct_index = new_correct_index
        self.current_shuffled_options = options.copy()
        
        self.page.views.clear()
        
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
            f"/basic_arithmetic/quiz/{self.current_quiz_level}",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.go_back_to_quizzes()),
                    title=ft.Text(f"{self.current_quiz_level.title()} Quiz"),
                    bgcolor=ft.Colors.GREEN_700
                ),
                ft.Container(
                    ft.Column([
                        # Progress indicator
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
                        
                        # Question
                        ft.Container(
                            ft.Column([
                                ft.Text("❓ Question:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
                                ft.Text(question_data["question"], size=18, weight=ft.FontWeight.BOLD),
                            ], spacing=10),
                            padding=20,
                            bgcolor=ft.Colors.BLUE_50,
                            border_radius=10,
                            border=ft.border.all(2, ft.Colors.BLUE_200)
                        ),
                        
                        # Options
                        ft.Text("Choose your answer:", size=16, weight=ft.FontWeight.BOLD),
                        ft.ResponsiveRow(option_buttons, spacing=10, run_spacing=10),
                        
                        # Score display
                        ft.Container(
                            ft.Text(f"Current Score: {self.quiz_score}/{self.quiz_question_index}", 
                                   size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
                            padding=10,
                            bgcolor=ft.Colors.GREEN_50,
                            border_radius=5
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

    def answer_question(self, selected_index):
        question_data = self.current_quiz_questions[self.quiz_question_index]
        is_correct = selected_index == self.current_correct_index
        
        if is_correct:
            self.quiz_score += 1
        
        # Store the original data for feedback display
        self.show_answer_feedback(question_data, selected_index, is_correct)

    def show_answer_feedback(self, question_data, selected_index, is_correct):
        self.page.views.clear()
        
        feedback_color = ft.Colors.GREEN_700 if is_correct else ft.Colors.RED_700
        feedback_icon = ft.Icons.CHECK_CIRCLE if is_correct else ft.Icons.CANCEL
        feedback_text = "Correct!" if is_correct else "Incorrect"
        
        # Get the correct answer text and user's selected answer text
        correct_answer = question_data["options"][question_data["correct"]]
        user_selected_answer = self.current_shuffled_options[selected_index]
        
        view = ft.View(
            f"/basic_arithmetic/quiz/{self.current_quiz_level}/feedback",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.go_back_to_quiz_question()),
                    title=ft.Text("Answer Feedback"),
                    bgcolor=feedback_color
                ),
                ft.Container(
                    ft.Column([
                        ft.Container(
                            ft.Column([
                                ft.Icon(feedback_icon, size=50, color=feedback_color),
                                ft.Text(feedback_text, size=24, weight=ft.FontWeight.BOLD, color=feedback_color),
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
                            padding=20
                        ),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("Question:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
                                ft.Text(question_data["question"], size=16),
                                
                                ft.Text("Your Answer:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
                                ft.Text(f"{chr(65+selected_index)}. {user_selected_answer}", size=16),
                                
                                ft.Text("Correct Answer:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
                                ft.Text(f"{correct_answer}", size=16),
                                
                                ft.Text("Explanation:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_700),
                                ft.Text(question_data["explanation"], size=14, color=ft.Colors.GREY_800),
                            ], spacing=10),
                            padding=20,
                            bgcolor=ft.Colors.GREY_50,
                            border_radius=10
                        ),
                        
                        ft.ElevatedButton(
                            "Next Question" if self.quiz_question_index + 1 < len(self.current_quiz_questions) else "See Results",
                            on_click=self.next_question,
                            style=ft.ButtonStyle(bgcolor=ft.Colors.BLUE_700, color=ft.Colors.WHITE, padding=20)
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

    def next_question(self, e):
        self.quiz_question_index += 1
        self.show_quiz_question()

    def show_quiz_results(self):
        self.page.views.clear()
        
        percentage = (self.quiz_score / len(self.current_quiz_questions)) * 100
        
        if percentage >= 90:
            grade = "A+"
            grade_color = ft.Colors.GREEN_700
            message = "Excellent work! You've mastered this level!"
        elif percentage >= 80:
            grade = "A"
            grade_color = ft.Colors.GREEN_600
            message = "Great job! You have a solid understanding!"
        elif percentage >= 70:
            grade = "B"
            grade_color = ft.Colors.BLUE_600
            message = "Good work! Keep practicing to improve!"
        elif percentage >= 60:
            grade = "C"
            grade_color = ft.Colors.ORANGE_600
            message = "You're getting there! Review the topics and try again!"
        else:
            grade = "F"
            grade_color = ft.Colors.RED_600
            message = "Don't give up! Review the learning materials and practice more!"
        
        view = ft.View(
            f"/basic_arithmetic/quiz/{self.current_quiz_level}/results",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.go_back_to_quizzes()),
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
                                ft.Text(f"Score: {self.quiz_score}/{len(self.current_quiz_questions)} ({percentage:.1f}%)", size=20),
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
                                    on_click=lambda e: self.go_back_to_main(),
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

    def show_learning_content(self):
        view = ft.View(
            "/basic_arithmetic/learn",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.go_back_to_main()),
                    title=ft.Text("Learn Basic Arithmetic"),
                    bgcolor=ft.Colors.PURPLE_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("📚 Basic Arithmetic Learning Guide", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_900),
                        ft.Text("Master the four fundamental operations of mathematics", size=16, color=ft.Colors.PURPLE_700),
                        
                        # Addition Section
                        ft.Container(
                            ft.Column([
                                ft.Text("➕ Addition", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
                                ft.Text("Addition is combining two or more numbers to find their total (sum).", size=14),
                                
                                ft.Text("🎯 Key Concepts:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_600),
                                ft.Column([
                                    ft.Text("• Commutative Property: 5 + 3 = 3 + 5", size=14),
                                    ft.Text("• Associative Property: (2 + 3) + 4 = 2 + (3 + 4)", size=14),
                                    ft.Text("• Identity Property: Any number + 0 = that number", size=14),
                                ], spacing=5),
                                
                                ft.Text("📝 Strategies:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_600),
                                ft.Column([
                                    ft.Text("• Count on: Start with the larger number and count up", size=14),
                                    ft.Text("• Make 10: Break numbers to make groups of 10", size=14),
                                    ft.Text("• Doubles: Learn doubles like 6+6=12, then use near doubles", size=14),
                                    ft.Text("• Column method: Line up place values and add column by column", size=14),
                                ], spacing=5),
                                
                                ft.Container(
                                    ft.Column([
                                        ft.Text("Example: 47 + 28", size=16, weight=ft.FontWeight.BOLD),
                                        ft.Text("Step 1: Add ones: 7 + 8 = 15 (write 5, carry 1)", size=14),
                                        ft.Text("Step 2: Add tens: 4 + 2 + 1 = 7", size=14),
                                        ft.Text("Answer: 75", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
                                    ], spacing=5),
                                    bgcolor=ft.Colors.GREEN_50,
                                    padding=10,
                                    border_radius=5
                                )
                            ], spacing=10),
                            bgcolor=ft.Colors.GREEN_50,
                            padding=15,
                            border_radius=10,
                            border=ft.border.all(2, ft.Colors.GREEN_200)
                        ),
                        
                        # Subtraction Section
                        ft.Container(
                            ft.Column([
                                ft.Text("➖ Subtraction", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_700),
                                ft.Text("Subtraction is taking away one number from another to find the difference.", size=14),
                                
                                ft.Text("🎯 Key Concepts:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_600),
                                ft.Column([
                                    ft.Text("• Subtraction is the opposite of addition", size=14),
                                    ft.Text("• Any number - 0 = that number", size=14),
                                    ft.Text("• Any number - itself = 0", size=14),
                                ], spacing=5),
                                
                                ft.Text("📝 Strategies:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_600),
                                ft.Column([
                                    ft.Text("• Count back: Start with the first number and count backwards", size=14),
                                    ft.Text("• Think addition: What + second number = first number?", size=14),
                                    ft.Text("• Number line: Use a number line to visualize", size=14),
                                    ft.Text("• Borrowing: When the top digit is smaller, borrow from the next column", size=14),
                                ], spacing=5),
                                
                                ft.Container(
                                    ft.Column([
                                        ft.Text("Example: 63 - 28", size=16, weight=ft.FontWeight.BOLD),
                                        ft.Text("Step 1: Can't do 3 - 8, so borrow from tens", size=14),
                                        ft.Text("Step 2: 13 - 8 = 5 (ones place)", size=14),
                                        ft.Text("Step 3: 5 - 2 = 3 (tens place)", size=14),
                                        ft.Text("Answer: 35", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_700),
                                    ], spacing=5),
                                    bgcolor=ft.Colors.ORANGE_50,
                                    padding=10,
                                    border_radius=5
                                )
                            ], spacing=10),
                            bgcolor=ft.Colors.ORANGE_50,
                            padding=15,
                            border_radius=10,
                            border=ft.border.all(2, ft.Colors.ORANGE_200)
                        ),
                        
                        # Multiplication Section
                        ft.Container(
                            ft.Column([
                                ft.Text("✖️ Multiplication", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_700),
                                ft.Text("Multiplication is repeated addition - adding a number to itself multiple times.", size=14),
                                
                                ft.Text("🎯 Key Concepts:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_600),
                                ft.Column([
                                    ft.Text("• Commutative Property: 4 × 6 = 6 × 4", size=14),
                                    ft.Text("• Associative Property: (2 × 3) × 4 = 2 × (3 × 4)", size=14),
                                    ft.Text("• Identity Property: Any number × 1 = that number", size=14),
                                    ft.Text("• Zero Property: Any number × 0 = 0", size=14),
                                ], spacing=5),
                                
                                ft.Text("📝 Strategies:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_600),
                                ft.Column([
                                    ft.Text("• Skip counting: Count by the first number", size=14),
                                    ft.Text("• Times tables: Memorize multiplication facts 1-12", size=14),
                                    ft.Text("• Arrays: Visualize as rows and columns", size=14),
                                    ft.Text("• Doubling: Use known facts to find new ones", size=14),
                                ], spacing=5),
                                
                                ft.Container(
                                    ft.Column([
                                        ft.Text("Example: 7 × 8", size=16, weight=ft.FontWeight.BOLD),
                                        ft.Text("Strategy 1: 7 × 8 = (7 × 4) × 2 = 28 × 2 = 56", size=14),
                                        ft.Text("Strategy 2: Skip count by 7s eight times: 7, 14, 21, 28, 35, 42, 49, 56", size=14),
                                        ft.Text("Answer: 56", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_700),
                                    ], spacing=5),
                                    bgcolor=ft.Colors.PURPLE_50,
                                    padding=10,
                                    border_radius=5
                                )
                            ], spacing=10),
                            bgcolor=ft.Colors.PURPLE_50,
                            padding=15,
                            border_radius=10,
                            border=ft.border.all(2, ft.Colors.PURPLE_200)
                        ),
                        
                        # Division Section
                        ft.Container(
                            ft.Column([
                                ft.Text("➗ Division", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
                                ft.Text("Division is splitting a number into equal groups or finding how many times one number fits into another.", size=14),
                                
                                ft.Text("🎯 Key Concepts:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_600),
                                ft.Column([
                                    ft.Text("• Division is the opposite of multiplication", size=14),
                                    ft.Text("• Any number ÷ 1 = that number", size=14),
                                    ft.Text("• Any number ÷ itself = 1", size=14),
                                    ft.Text("• 0 ÷ any number = 0", size=14),
                                ], spacing=5),
                                
                                ft.Text("📝 Strategies:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_600),
                                ft.Column([
                                    ft.Text("• Think multiplication: What × divisor = dividend?", size=14),
                                    ft.Text("• Share equally: Distribute items into equal groups", size=14),
                                    ft.Text("• Repeated subtraction: How many times can you subtract?", size=14),
                                    ft.Text("• Long division: Step-by-step process for larger numbers", size=14),
                                ], spacing=5),
                                
                                ft.Container(
                                    ft.Column([
                                        ft.Text("Example: 84 ÷ 7", size=16, weight=ft.FontWeight.BOLD),
                                        ft.Text("Think: What × 7 = 84?", size=14),
                                        ft.Text("7 × 10 = 70, 7 × 12 = 84", size=14),
                                        ft.Text("Answer: 12", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
                                    ], spacing=5),
                                    bgcolor=ft.Colors.BLUE_50,
                                    padding=10,
                                    border_radius=5
                                )
                            ], spacing=10),
                            bgcolor=ft.Colors.BLUE_50,
                            padding=15,
                            border_radius=10,
                            border=ft.border.all(2, ft.Colors.BLUE_200)
                        ),
                        
                        # Practice Tips
                        ft.Container(
                            ft.Column([
                                ft.Text("💡 Practice Tips", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.TEAL_700),
                                ft.Column([
                                    ft.Text("✓ Practice a little bit every day", size=14),
                                    ft.Text("✓ Start with easier problems and work up to harder ones", size=14),
                                    ft.Text("✓ Use visual aids like number lines, counters, or drawings", size=14),
                                    ft.Text("✓ Check your work by doing the opposite operation", size=14),
                                    ft.Text("✓ Don't rush - accuracy is more important than speed", size=14),
                                    ft.Text("✓ Ask for help when you're stuck", size=14),
                                ], spacing=8),
                            ], spacing=15),
                            bgcolor=ft.Colors.TEAL_50,
                            padding=15,
                            border_radius=10,
                            border=ft.border.all(2, ft.Colors.TEAL_200)
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

    def show_practice_test(self):
        # Mix questions from all levels for comprehensive test
        all_questions = []
        for level in self.quiz_questions:
            all_questions.extend(self.quiz_questions[level][:5])  # 5 from each level
        
        random.shuffle(all_questions)
        self.current_quiz_questions = all_questions[:15]  # 15-question practice test
        self.current_quiz_level = "practice_test"
        self.quiz_score = 0
        self.quiz_question_index = 0
        
        self.page.views.clear()
        
        view = ft.View(
            "/basic_arithmetic/practice_test",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.go_back_to_main()),
                    title=ft.Text("Practice Test"),
                    bgcolor=ft.Colors.ORANGE_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("🎯 Basic Arithmetic Practice Test", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_900),
                        ft.Text("A comprehensive test covering all arithmetic operations", size=16, color=ft.Colors.ORANGE_700),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("📋 Test Information:", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_700),
                                ft.Text("• 15 questions covering all difficulty levels", size=14),
                                ft.Text("• Mix of basic, intermediate, and advanced problems", size=14),
                                ft.Text("• All four operations: +, -, ×, ÷", size=14),
                                ft.Text("• Includes word problems and multi-step calculations", size=14),
                                ft.Text("• Take your time and show your work", size=14),
                                
                                ft.Text("🏆 Scoring:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_700),
                                ft.Text("• 90-100%: Excellent mastery", size=14),
                                ft.Text("• 80-89%: Good understanding", size=14),
                                ft.Text("• 70-79%: Needs some practice", size=14),
                                ft.Text("• Below 70%: Review fundamentals", size=14),
                            ], spacing=10),
                            padding=20,
                            bgcolor=ft.Colors.ORANGE_50,
                            border_radius=10,
                            border=ft.border.all(2, ft.Colors.ORANGE_200)
                        ),
                        
                        ft.ElevatedButton(
                            "Start Practice Test",
                            on_click=lambda e: self.show_quiz_question(),
                            style=ft.ButtonStyle(
                                bgcolor=ft.Colors.ORANGE_700,
                                color=ft.Colors.WHITE,
                                padding=ft.Padding(30, 15, 30, 15)
                            )
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

# Make sure the page function is available for routing
def basic_arithmetic_page(page: ft.Page):
    """Basic Arithmetic learning page"""
    page.title = f"Basic Arithmetic - Mathematics Learning"
    page.scroll = ft.ScrollMode.AUTO
    
    # Clear page content first
    page.clean()
    
    # Create module instance
    module = BasicArithmeticModule(page)
    
    # AppBar with back button
    page.appbar = ft.AppBar(
        leading=ft.IconButton(
            ft.Icons.ARROW_BACK,
            on_click=lambda e: page.go("/maths")
        ),
        title=ft.Text("Basic Arithmetic"),
        bgcolor=ft.Colors.BLUE_700,
        center_title=True
    )
    
    # Add main view
    page.add(module.create_main_view())
