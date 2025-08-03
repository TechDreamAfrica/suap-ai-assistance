import flet as ft
import random
import math


class MatricesModule:
    """Comprehensive Matrices learning module"""
    
    def __init__(self, page: ft.Page):
        self.page = page
        self.current_question = 0
        self.score = 0
        self.quiz_questions = self._generate_quiz_questions()
        self.selected_answer = None
        
    def show_page(self):
        """Main entry point for the module"""
        self.show_main_page()
        
    def show_main_page(self, page=None):
        """Show the main matrices page
        Args:
            page: Optional page reference. If not provided, uses self.page
        """
        if page is None:
            page = self.page
        self.page = page  # Update the page reference
            
        view = ft.View(
            "/matrices",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: page.go_back()),
                    title=ft.Text("Matrices"),
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
        
        # AppBar with navigation
        self.page.appbar = ft.AppBar(
            leading=ft.IconButton(
                ft.Icons.ARROW_BACK,
                on_click=lambda e: self.page.go("/maths"),
                tooltip="Back to Mathematics"
            ),
            title=ft.Text("Matrices"),
            bgcolor=ft.Colors.BLUE_700,
            center_title=True
        )
        
        # Main content
        content = ft.Container(
            ft.Column([
                # Header
                ft.Container(
                    ft.Column([
                        ft.Text(
                            "🎯 Matrices",
                            size=32,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.BLUE_900,
                            text_align=ft.TextAlign.CENTER
                        ),
                        ft.Text(
                            "Master linear algebra with matrices and their operations",
                            size=16,
                            color=ft.Colors.BLUE_700,
                            text_align=ft.TextAlign.CENTER
                        ),
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    bgcolor=ft.Colors.BLUE_50,
                    border_radius=15,
                    padding=20,
                    margin=ft.margin.only(bottom=20)
                ),
                
                # Learning objectives
                ft.Container(
                    ft.Column([
                        ft.Text("🎯 Learning Objectives", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                        ft.Text("• Understand matrix notation and dimensions", size=14),
                        ft.Text("• Perform matrix addition and subtraction", size=14),
                        ft.Text("• Master matrix multiplication", size=14),
                        ft.Text("• Calculate determinants and inverses", size=14),
                        ft.Text("• Solve systems of linear equations", size=14),
                        ft.Text("• Apply matrices in real-world problems", size=14),
                    ], spacing=8),
                    bgcolor=ft.Colors.GREEN_50,
                    border_radius=10,
                    padding=20,
                    margin=ft.margin.only(bottom=20)
                ),
                
                # Action buttons
                ft.ResponsiveRow([
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.SCHOOL, size=30, color=ft.Colors.BLUE_700),
                                ft.Text("Learn Concepts", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            style=ft.ButtonStyle(
                                padding=20,
                                bgcolor=ft.Colors.BLUE_50,
                                shape=ft.RoundedRectangleBorder(radius=10)
                            ),
                            on_click=lambda e: self.show_learning_content()
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.QUIZ, size=30, color=ft.Colors.GREEN_700),
                                ft.Text("Practice Quiz", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            style=ft.ButtonStyle(
                                padding=20,
                                bgcolor=ft.Colors.GREEN_50,
                                shape=ft.RoundedRectangleBorder(radius=10)
                            ),
                            on_click=lambda e: self.show_quiz()
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.LIGHTBULB_OUTLINE, size=30, color=ft.Colors.ORANGE_700),
                                ft.Text("Examples", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            style=ft.ButtonStyle(
                                padding=20,
                                bgcolor=ft.Colors.ORANGE_50,
                                shape=ft.RoundedRectangleBorder(radius=10)
                            ),
                            on_click=lambda e: self.show_examples()
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.HELP_OUTLINE, size=30, color=ft.Colors.PURPLE_700),
                                ft.Text("AI Help", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            style=ft.ButtonStyle(
                                padding=20,
                                bgcolor=ft.Colors.PURPLE_50,
                                shape=ft.RoundedRectangleBorder(radius=10)
                            ),
                            on_click=lambda e: self.show_ai_help()
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                ], spacing=15, run_spacing=15),
                
                ft.Divider(height=20),
                
                # Overview content
                ft.Container(
                    ft.Column([
                        ft.Text("📐 Matrices Overview", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                        ft.Text("Matrices are rectangular arrays of numbers arranged in rows and columns. They are fundamental tools in linear algebra, used to solve systems of equations, perform transformations, and model complex relationships in science and engineering.", size=14),
                        
                        ft.Divider(height=10),
                        
                        ft.Text("🔑 Key Concepts:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_800),
                        ft.Text("• Matrix dimensions: rows × columns", size=14),
                        ft.Text("• Matrix operations: addition, subtraction, multiplication", size=14),
                        ft.Text("• Special matrices: identity, zero, transpose", size=14),
                        ft.Text("• Determinants and matrix inverses", size=14),
                        ft.Text("• Systems of linear equations", size=14),
                        
                        ft.Divider(height=10),
                        
                        ft.Text("🌟 Applications:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_800),
                        ft.Text("• Computer graphics and 3D transformations", size=14),
                        ft.Text("• Solving engineering problems", size=14),
                        ft.Text("• Data analysis and statistics", size=14),
                        ft.Text("• Economics and optimization", size=14),
                        ft.Text("• Machine learning algorithms", size=14),
                    ], spacing=10),
                    bgcolor=ft.Colors.GREY_50,
                    border_radius=10,
                    padding=20
                )
            ], spacing=20),
            padding=20,
            expand=True
        )
        
        self.page.add(content)
        self.page.update()
    
    def show_learning_content(self):
        """Display comprehensive learning content"""
        self.page.clean()
        
        content = ft.Container(
            ft.Column([
                # Header
                ft.Row([
                    ft.IconButton(
                        ft.Icons.ARROW_BACK,
                        on_click=lambda e: self.show_page(),
                        tooltip="Back to Matrices"
                    ),
                    ft.Text(
                        "📚 Matrices: Complete Guide",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLUE_900
                    )
                ], alignment=ft.MainAxisAlignment.START),
                
                ft.Divider(),
                
                # Content sections
                ft.Container(
                    ft.Column([
                        ft.Text("1. Matrix Basics", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800),
                        ft.Text("A matrix is a rectangular array of numbers arranged in rows and columns.", size=14),
                        ft.Container(
                            ft.Column([
                                ft.Text("Matrix Notation:", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("A = [aᵢⱼ] where i = row, j = column", size=14),
                                ft.Text("Dimensions: m × n (m rows, n columns)", size=14),
                                ft.Text("Example 2×3 matrix:", size=14),
                                ft.Text("A = [1  2  3]", size=14, style=ft.TextStyle(italic=True)),
                                ft.Text("    [4  5  6]", size=14, style=ft.TextStyle(italic=True)),
                                ft.Text("Element a₁₂ = 2 (row 1, column 2)", size=14),
                            ], spacing=5),
                            bgcolor=ft.Colors.BLUE_50,
                            padding=10,
                            border_radius=5,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                    ], spacing=8),
                    bgcolor=ft.Colors.WHITE,
                    border_radius=10,
                    padding=15,
                    margin=ft.margin.only(bottom=15)
                ),
                
                ft.Container(
                    ft.Column([
                        ft.Text("2. Matrix Addition and Subtraction", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_800),
                        ft.Text("Matrices can be added or subtracted if they have the same dimensions.", size=14),
                        ft.Container(
                            ft.Column([
                                ft.Text("Rule: Add/subtract corresponding elements", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("(A ± B)ᵢⱼ = aᵢⱼ ± bᵢⱼ", size=14),
                                ft.Text("Example:", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("[1  2] + [5  6] = [6   8]", size=14, style=ft.TextStyle(italic=True)),
                                ft.Text("[3  4]   [7  8]   [10 12]", size=14, style=ft.TextStyle(italic=True)),
                                ft.Text("Only works for matrices of same size!", size=14),
                            ], spacing=5),
                            bgcolor=ft.Colors.GREEN_50,
                            padding=10,
                            border_radius=5,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                    ], spacing=8),
                    bgcolor=ft.Colors.WHITE,
                    border_radius=10,
                    padding=15,
                    margin=ft.margin.only(bottom=15)
                ),
                
                ft.Container(
                    ft.Column([
                        ft.Text("3. Matrix Multiplication", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_800),
                        ft.Text("Matrix multiplication follows specific rules and is NOT commutative (AB ≠ BA).", size=14),
                        ft.Container(
                            ft.Column([
                                ft.Text("Rule: (AB)ᵢⱼ = Σ(aᵢₖ × bₖⱼ)", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("For A(m×n) × B(n×p) = C(m×p)", size=14),
                                ft.Text("Number of columns in A = number of rows in B", size=14),
                                ft.Text("Example: A(2×3) × B(3×2) = C(2×2)", size=14),
                                ft.Text("[1  2  3] × [7   8] = [1×7+2×9+3×11  1×8+2×10+3×12]", size=14, style=ft.TextStyle(italic=True)),
                                ft.Text("[4  5  6]   [9  10]   [4×7+5×9+6×11  4×8+5×10+6×12]", size=14, style=ft.TextStyle(italic=True)),
                                ft.Text("           [11 12]", size=14, style=ft.TextStyle(italic=True)),
                                ft.Text("Result: [58  64]", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("        [139 154]", size=14, weight=ft.FontWeight.BOLD),
                            ], spacing=5),
                            bgcolor=ft.Colors.ORANGE_50,
                            padding=10,
                            border_radius=5,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                    ], spacing=8),
                    bgcolor=ft.Colors.WHITE,
                    border_radius=10,
                    padding=15,
                    margin=ft.margin.only(bottom=15)
                ),
                
                ft.Container(
                    ft.Column([
                        ft.Text("4. Special Matrices", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_800),
                        ft.Text("Several types of matrices have special properties and uses.", size=14),
                        ft.Container(
                            ft.Column([
                                ft.Text("Identity Matrix (I): All diagonal elements = 1, others = 0", size=14),
                                ft.Text("I₂ = [1  0]    I₃ = [1  0  0]", size=14, style=ft.TextStyle(italic=True)),
                                ft.Text("     [0  1]         [0  1  0]", size=14, style=ft.TextStyle(italic=True)),
                                ft.Text("                    [0  0  1]", size=14, style=ft.TextStyle(italic=True)),
                                ft.Text("Zero Matrix (O): All elements = 0", size=14),
                                ft.Text("Transpose (Aᵀ): Rows become columns", size=14),
                                ft.Text("Square Matrix: Number of rows = number of columns", size=14),
                            ], spacing=5),
                            bgcolor=ft.Colors.PURPLE_50,
                            padding=10,
                            border_radius=5,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                    ], spacing=8),
                    bgcolor=ft.Colors.WHITE,
                    border_radius=10,
                    padding=15,
                    margin=ft.margin.only(bottom=15)
                ),
                
                ft.Container(
                    ft.Column([
                        ft.Text("5. Determinants", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.RED_800),
                        ft.Text("Determinants are scalar values calculated from square matrices.", size=14),
                        ft.Container(
                            ft.Column([
                                ft.Text("2×2 Matrix: det(A) = ad - bc", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("For A = [a  b]", size=14),
                                ft.Text("        [c  d]", size=14),
                                ft.Text("3×3 Matrix: Use cofactor expansion", size=14),
                                ft.Text("det(A) = a₁₁(a₂₂a₃₃ - a₂₃a₃₂) - a₁₂(a₂₁a₃₃ - a₂₃a₃₁) + a₁₃(a₂₁a₃₂ - a₂₂a₃₁)", size=14),
                                ft.Text("Properties:", size=14, weight=ft.FontWeight.BOLD),
                                ft.Text("• det(AB) = det(A) × det(B)", size=14),
                                ft.Text("• If det(A) = 0, matrix is singular (no inverse)", size=14),
                            ], spacing=5),
                            bgcolor=ft.Colors.RED_50,
                            padding=10,
                            border_radius=5,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                    ], spacing=8),
                    bgcolor=ft.Colors.WHITE,
                    border_radius=10,
                    padding=15,
                    margin=ft.margin.only(bottom=15)
                ),
                
                # Back button
                ft.Container(
                    ft.ElevatedButton(
                        "Back to Matrices",
                        icon=ft.Icons.ARROW_BACK,
                        on_click=lambda e: self.show_page(),
                        style=ft.ButtonStyle(
                            bgcolor=ft.Colors.BLUE_700,
                            color=ft.Colors.WHITE,
                            padding=20
                        )
                    ),
                    alignment=ft.alignment.center,
                    margin=ft.margin.only(top=20)
                )
            ], spacing=15, scroll=ft.ScrollMode.AUTO),
            padding=20,
            expand=True
        )
        
        self.page.add(content)
        self.page.update()
    
    def show_examples(self):
        """Display worked examples"""
        self.page.clean()
        
        content = ft.Container(
            ft.Column([
                # Header
                ft.Row([
                    ft.IconButton(
                        ft.Icons.ARROW_BACK,
                        on_click=lambda e: self.show_page(),
                        tooltip="Back to Matrices"
                    ),
                    ft.Text(
                        "💡 Matrices: Worked Examples",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.ORANGE_900
                    )
                ], alignment=ft.MainAxisAlignment.START),
                
                ft.Divider(),
                
                # Example 1
                ft.Container(
                    ft.Column([
                        ft.Text("Example 1: Matrix Addition", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800),
                        ft.Text("Problem: Add the matrices A and B", size=14),
                        ft.Text("A = [2  -1]    B = [3   4]", size=14, style=ft.TextStyle(italic=True)),
                        ft.Text("    [0   3]        [1  -2]", size=14, style=ft.TextStyle(italic=True)),
                        ft.Text("Solution:", size=14, weight=ft.FontWeight.BOLD),
                        ft.Text("Step 1: Check dimensions - both are 2×2 ✓", size=14),
                        ft.Text("Step 2: Add corresponding elements", size=14),
                        ft.Text("A + B = [2+3   -1+4] = [5   3]", size=14),
                        ft.Text("        [0+1    3-2]   [1   1]", size=14),
                        ft.Container(
                            ft.Text("Answer: [5  3]\n        [1  1]", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
                            bgcolor=ft.Colors.GREEN_50,
                            padding=10,
                            border_radius=5,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                    ], spacing=8),
                    bgcolor=ft.Colors.WHITE,
                    border_radius=10,
                    padding=15,
                    margin=ft.margin.only(bottom=20)
                ),
                
                # Example 2
                ft.Container(
                    ft.Column([
                        ft.Text("Example 2: Matrix Multiplication", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_800),
                        ft.Text("Problem: Multiply matrices A and B", size=14),
                        ft.Text("A = [1  2]    B = [5  6]", size=14, style=ft.TextStyle(italic=True)),
                        ft.Text("    [3  4]        [7  8]", size=14, style=ft.TextStyle(italic=True)),
                        ft.Text("Solution:", size=14, weight=ft.FontWeight.BOLD),
                        ft.Text("Step 1: Check compatibility - A(2×2) × B(2×2) → C(2×2) ✓", size=14),
                        ft.Text("Step 2: Calculate each element", size=14),
                        ft.Text("c₁₁ = (1×5) + (2×7) = 5 + 14 = 19", size=14),
                        ft.Text("c₁₂ = (1×6) + (2×8) = 6 + 16 = 22", size=14),
                        ft.Text("c₂₁ = (3×5) + (4×7) = 15 + 28 = 43", size=14),
                        ft.Text("c₂₂ = (3×6) + (4×8) = 18 + 32 = 50", size=14),
                        ft.Container(
                            ft.Text("Answer: AB = [19  22]\n             [43  50]", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
                            bgcolor=ft.Colors.GREEN_50,
                            padding=10,
                            border_radius=5,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                    ], spacing=8),
                    bgcolor=ft.Colors.WHITE,
                    border_radius=10,
                    padding=15,
                    margin=ft.margin.only(bottom=20)
                ),
                
                # Example 3
                ft.Container(
                    ft.Column([
                        ft.Text("Example 3: Calculating Determinant (2×2)", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_800),
                        ft.Text("Problem: Find the determinant of matrix A", size=14),
                        ft.Text("A = [3  -2]", size=14, style=ft.TextStyle(italic=True)),
                        ft.Text("    [1   4]", size=14, style=ft.TextStyle(italic=True)),
                        ft.Text("Solution:", size=14, weight=ft.FontWeight.BOLD),
                        ft.Text("Step 1: Use formula det(A) = ad - bc", size=14),
                        ft.Text("Where a=3, b=-2, c=1, d=4", size=14),
                        ft.Text("Step 2: Calculate", size=14),
                        ft.Text("det(A) = (3×4) - (-2×1)", size=14),
                        ft.Text("det(A) = 12 - (-2)", size=14),
                        ft.Text("det(A) = 12 + 2 = 14", size=14),
                        ft.Container(
                            ft.Text("Answer: det(A) = 14", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
                            bgcolor=ft.Colors.GREEN_50,
                            padding=10,
                            border_radius=5,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                    ], spacing=8),
                    bgcolor=ft.Colors.WHITE,
                    border_radius=10,
                    padding=15,
                    margin=ft.margin.only(bottom=20)
                ),
                
                # Example 4
                ft.Container(
                    ft.Column([
                        ft.Text("Example 4: Matrix Inverse (2×2)", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.RED_800),
                        ft.Text("Problem: Find the inverse of matrix A", size=14),
                        ft.Text("A = [2  1]", size=14, style=ft.TextStyle(italic=True)),
                        ft.Text("    [3  2]", size=14, style=ft.TextStyle(italic=True)),
                        ft.Text("Solution:", size=14, weight=ft.FontWeight.BOLD),
                        ft.Text("Step 1: Calculate determinant", size=14),
                        ft.Text("det(A) = (2×2) - (1×3) = 4 - 3 = 1", size=14),
                        ft.Text("Step 2: Since det(A) ≠ 0, inverse exists", size=14),
                        ft.Text("Step 3: Use formula A⁻¹ = (1/det(A)) × [d  -b]", size=14),
                        ft.Text("                                    [-c   a]", size=14),
                        ft.Text("A⁻¹ = (1/1) × [2  -1] = [2  -1]", size=14),
                        ft.Text("              [-3   2]   [-3   2]", size=14),
                        ft.Container(
                            ft.Text("Answer: A⁻¹ = [2  -1]\n              [-3   2]", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
                            bgcolor=ft.Colors.GREEN_50,
                            padding=10,
                            border_radius=5,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        ft.Text("Verification: A × A⁻¹ = I (identity matrix)", size=14, style=ft.TextStyle(italic=True)),
                    ], spacing=8),
                    bgcolor=ft.Colors.WHITE,
                    border_radius=10,
                    padding=15,
                    margin=ft.margin.only(bottom=20)
                ),
                
                # Back button
                ft.Container(
                    ft.ElevatedButton(
                        "Back to Matrices",
                        icon=ft.Icons.ARROW_BACK,
                        on_click=lambda e: self.show_page(),
                        style=ft.ButtonStyle(
                            bgcolor=ft.Colors.ORANGE_700,
                            color=ft.Colors.WHITE,
                            padding=20
                        )
                    ),
                    alignment=ft.alignment.center,
                    margin=ft.margin.only(top=20)
                )
            ], spacing=15, scroll=ft.ScrollMode.AUTO),
            padding=20,
            expand=True
        )
        
        self.page.add(content)
        self.page.update()
    
    def _generate_quiz_questions(self):
        """Generate quiz questions for matrices"""
        questions = [
            {
                "question": "What is the dimension of a matrix with 3 rows and 4 columns?",
                "options": ["3×4", "4×3", "12", "7"],
                "correct": 0,
                "explanation": "Matrix dimensions are written as rows × columns, so 3 rows and 4 columns = 3×4"
            },
            {
                "question": "What is [1 2] + [3 4]?",
                "options": ["[4 6]", "[3 8]", "[1 8]", "[4 2]"],
                "correct": 0,
                "explanation": "Add corresponding elements: [1+3, 2+4] = [4, 6]"
            },
            {
                "question": "What is the determinant of [2 3; 1 4]?",
                "options": ["5", "8", "11", "-5"],
                "correct": 0,
                "explanation": "det = (2×4) - (3×1) = 8 - 3 = 5"
            },
            {
                "question": "Can you multiply a 2×3 matrix by a 4×2 matrix?",
                "options": ["Yes", "No", "Sometimes", "Only if square"],
                "correct": 1,
                "explanation": "No, because the number of columns in the first matrix (3) ≠ number of rows in the second matrix (4)"
            },
            {
                "question": "What is the result dimension when multiplying a 2×3 matrix by a 3×4 matrix?",
                "options": ["2×4", "3×3", "2×3", "Cannot multiply"],
                "correct": 0,
                "explanation": "When multiplying A(m×n) × B(n×p), the result is C(m×p), so 2×3 × 3×4 = 2×4"
            },
            {
                "question": "Which matrix is the 2×2 identity matrix?",
                "options": ["[1 0; 0 1]", "[0 1; 1 0]", "[1 1; 1 1]", "[2 0; 0 2]"],
                "correct": 0,
                "explanation": "The identity matrix has 1s on the diagonal and 0s elsewhere"
            },
            {
                "question": "What is [2 1] × [1; 3]?",
                "options": ["[5]", "[2; 3]", "[2 3; 1 1]", "Cannot multiply"],
                "correct": 0,
                "explanation": "(2×1) × (1×3) → (2×1): [2×1 + 1×3] = [5]"
            },
            {
                "question": "A matrix has no inverse if its determinant is:",
                "options": ["0", "1", "Negative", "Greater than 1"],
                "correct": 0,
                "explanation": "A matrix is singular (non-invertible) when its determinant equals 0"
            },
            {
                "question": "What is the transpose of [1 2; 3 4]?",
                "options": ["[1 3; 2 4]", "[4 3; 2 1]", "[2 1; 4 3]", "[1 2; 3 4]"],
                "correct": 0,
                "explanation": "Transpose switches rows and columns: first row becomes first column, etc."
            },
            {
                "question": "Matrix multiplication is:",
                "options": ["Commutative", "Not commutative", "Sometimes commutative", "Distributive only"],
                "correct": 1,
                "explanation": "Matrix multiplication is not commutative: AB ≠ BA in general"
            }
        ]
        
        return random.sample(questions, len(questions))
    
    def show_quiz(self):
        """Display quiz interface"""
        self.current_question = 0
        self.score = 0
        self.selected_answer = None
        self._display_question()
    
    def _display_question(self):
        """Display current quiz question"""
        self.page.clean()
        
        if self.current_question >= len(self.quiz_questions):
            self._show_quiz_results()
            return
        
        question_data = self.quiz_questions[self.current_question]
        progress = (self.current_question + 1) / len(self.quiz_questions)
        
        content = ft.Container(
            ft.Column([
                # Header
                ft.Row([
                    ft.IconButton(
                        ft.Icons.ARROW_BACK,
                        on_click=lambda e: self.show_page(),
                        tooltip="Back to Matrices"
                    ),
                    ft.Text(
                        f"Quiz Question {self.current_question + 1} of {len(self.quiz_questions)}",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.GREEN_900
                    )
                ], alignment=ft.MainAxisAlignment.START),
                
                # Progress bar
                ft.Container(
                    ft.ProgressBar(value=progress, bgcolor=ft.Colors.GREEN_100, color=ft.Colors.GREEN_600),
                    margin=ft.margin.only(bottom=20)
                ),
                
                # Question
                ft.Container(
                    ft.Column([
                        ft.Text(
                            question_data["question"],
                            size=18,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.BLUE_900
                        ),
                    ]),
                    bgcolor=ft.Colors.BLUE_50,
                    border_radius=10,
                    padding=20,
                    margin=ft.margin.only(bottom=20)
                ),
                
                # Answer options
                ft.Column([
                    ft.RadioGroup(
                        content=ft.Column([
                            ft.Radio(value=i, label=option, label_style=ft.TextStyle(size=16))
                            for i, option in enumerate(question_data["options"])
                        ], spacing=10),
                        on_change=self._on_answer_selected
                    )
                ], spacing=10),
                
                # Submit button
                ft.Container(
                    ft.ElevatedButton(
                        "Submit Answer",
                        icon=ft.Icons.CHECK,
                        on_click=lambda e: self._submit_answer(),
                        disabled=True,
                        style=ft.ButtonStyle(
                            bgcolor=ft.Colors.GREEN_600,
                            color=ft.Colors.WHITE,
                            padding=15
                        )
                    ),
                    alignment=ft.alignment.center,
                    margin=ft.margin.only(top=20)
                ),
                
                # Score display
                ft.Container(
                    ft.Text(
                        f"Current Score: {self.score}/{self.current_question}",
                        size=16,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.PURPLE_700,
                        text_align=ft.TextAlign.CENTER
                    ),
                    alignment=ft.alignment.center,
                    margin=ft.margin.only(top=10)
                )
            ], spacing=15),
            padding=20,
            expand=True
        )
        
        self.page.add(content)
        self.page.update()
    
    def _on_answer_selected(self, e):
        """Handle answer selection"""
        self.selected_answer = int(e.control.value)
        # Enable submit button
        for control in self.page.controls:
            if hasattr(control, 'content'):
                self._enable_submit_button(control.content)
        self.page.update()
    
    def _enable_submit_button(self, control):
        """Recursively find and enable submit button"""
        if hasattr(control, 'controls'):
            for child in control.controls:
                if isinstance(child, ft.ElevatedButton) and hasattr(child, 'text') and child.text == "Submit Answer":
                    child.disabled = False
                    return
                elif hasattr(child, 'content'):
                    self._enable_submit_button(child.content)
                elif hasattr(child, 'controls'):
                    self._enable_submit_button(child)
    
    def _submit_answer(self):
        """Submit the selected answer"""
        if self.selected_answer is None:
            return
        
        question_data = self.quiz_questions[self.current_question]
        is_correct = self.selected_answer == question_data["correct"]
        
        if is_correct:
            self.score += 1
        
        self._show_answer_feedback(is_correct, question_data["explanation"])
    
    def _show_answer_feedback(self, is_correct, explanation):
        """Show feedback for the submitted answer"""
        self.page.clean()
        
        feedback_color = ft.Colors.GREEN_600 if is_correct else ft.Colors.RED_600
        feedback_icon = ft.Icons.CHECK_CIRCLE if is_correct else ft.Icons.CANCEL
        feedback_text = "Correct!" if is_correct else "Incorrect"
        
        content = ft.Container(
            ft.Column([
                ft.Container(
                    ft.Column([
                        ft.Icon(feedback_icon, size=60, color=feedback_color),
                        ft.Text(
                            feedback_text,
                            size=24,
                            weight=ft.FontWeight.BOLD,
                            color=feedback_color,
                            text_align=ft.TextAlign.CENTER
                        )
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    alignment=ft.alignment.center,
                    margin=ft.margin.only(bottom=20)
                ),
                
                ft.Container(
                    ft.Column([
                        ft.Text("Explanation:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                        ft.Text(explanation, size=14, color=ft.Colors.BLUE_800),
                    ], spacing=10),
                    bgcolor=ft.Colors.BLUE_50,
                    border_radius=10,
                    padding=20,
                    margin=ft.margin.only(bottom=20)
                ),
                
                ft.Container(
                    ft.ElevatedButton(
                        "Next Question" if self.current_question < len(self.quiz_questions) - 1 else "Show Results",
                        icon=ft.Icons.ARROW_FORWARD,
                        on_click=lambda e: self._next_question(),
                        style=ft.ButtonStyle(
                            bgcolor=ft.Colors.BLUE_600,
                            color=ft.Colors.WHITE,
                            padding=15
                        )
                    ),
                    alignment=ft.alignment.center
                )
            ], spacing=15),
            padding=20,
            expand=True
        )
        
        self.page.add(content)
        self.page.update()
    
    def _next_question(self):
        """Move to next question"""
        self.current_question += 1
        self.selected_answer = None
        self._display_question()
    
    def _show_quiz_results(self):
        """Show final quiz results"""
        self.page.clean()
        
        percentage = (self.score / len(self.quiz_questions)) * 100
        
        if percentage >= 90:
            grade = "A+"
            message = "Outstanding! You've mastered matrix operations!"
            color = ft.Colors.GREEN_600
        elif percentage >= 80:
            grade = "A"
            message = "Excellent work! You have a strong understanding of matrices."
            color = ft.Colors.GREEN_600
        elif percentage >= 70:
            grade = "B"
            message = "Good job! You understand most matrix concepts."
            color = ft.Colors.BLUE_600
        elif percentage >= 60:
            grade = "C"
            message = "Fair work. Review the examples and try again."
            color = ft.Colors.ORANGE_600
        else:
            grade = "F"
            message = "Keep practicing! Review the learning content and examples."
            color = ft.Colors.RED_600
        
        content = ft.Container(
            ft.Column([
                ft.Text(
                    "🎉 Quiz Complete!",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.PURPLE_900,
                    text_align=ft.TextAlign.CENTER
                ),
                
                ft.Container(
                    ft.Column([
                        ft.Text(f"Your Score: {self.score}/{len(self.quiz_questions)}", size=24, weight=ft.FontWeight.BOLD),
                        ft.Text(f"Percentage: {percentage:.1f}%", size=20),
                        ft.Text(f"Grade: {grade}", size=20, weight=ft.FontWeight.BOLD, color=color),
                        ft.Text(message, size=16, text_align=ft.TextAlign.CENTER),
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
                    bgcolor=ft.Colors.PURPLE_50,
                    border_radius=15,
                    padding=30,
                    margin=ft.margin.only(bottom=30)
                ),
                
                ft.ResponsiveRow([
                    ft.Container(
                        ft.ElevatedButton(
                            "Retake Quiz",
                            icon=ft.Icons.REFRESH,
                            on_click=lambda e: self.show_quiz(),
                            style=ft.ButtonStyle(
                                bgcolor=ft.Colors.BLUE_600,
                                color=ft.Colors.WHITE,
                                padding=15
                            )
                        ),
                        col={'xs': 12, 'sm': 6}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            "Back to Matrices",
                            icon=ft.Icons.ARROW_BACK,
                            on_click=lambda e: self.show_page(),
                            style=ft.ButtonStyle(
                                bgcolor=ft.Colors.GREEN_600,
                                color=ft.Colors.WHITE,
                                padding=15
                            )
                        ),
                        col={'xs': 12, 'sm': 6}
                    ),
                ], spacing=15)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20),
            padding=20,
            expand=True
        )
        
        self.page.add(content)
        self.page.update()
    
    def show_ai_help(self):
        """Display AI help interface"""
        self.page.clean()
        
        # Create text field for user input
        user_input = ft.TextField(
            label="Ask me anything about matrices...",
            multiline=True,
            min_lines=3,
            max_lines=5,
            border_radius=10,
            bgcolor=ft.Colors.WHITE
        )
        
        # Chat messages container
        chat_messages = ft.Column([], spacing=10, scroll=ft.ScrollMode.AUTO, height=300)
        
        def send_message(e):
            user_question = user_input.value.strip()
            if not user_question:
                return
            
            # Add user message
            chat_messages.controls.append(
                ft.Container(
                    ft.Text(f"You: {user_question}", size=14, color=ft.Colors.BLUE_900),
                    bgcolor=ft.Colors.BLUE_50,
                    border_radius=10,
                    padding=10,
                    alignment=ft.alignment.center_right
                )
            )
            
            # Generate AI response
            ai_response = self._generate_ai_response(user_question)
            chat_messages.controls.append(
                ft.Container(
                    ft.Text(f"AI Tutor: {ai_response}", size=14, color=ft.Colors.GREEN_900),
                    bgcolor=ft.Colors.GREEN_50,
                    border_radius=10,
                    padding=10,
                    alignment=ft.alignment.center_left
                )
            )
            
            user_input.value = ""
            self.page.update()
        
        content = ft.Container(
            ft.Column([
                # Header
                ft.Row([
                    ft.IconButton(
                        ft.Icons.ARROW_BACK,
                        on_click=lambda e: self.show_page(),
                        tooltip="Back to Matrices"
                    ),
                    ft.Text(
                        "🤖 AI Tutor - Matrices Help",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.PURPLE_900
                    )
                ], alignment=ft.MainAxisAlignment.START),
                
                ft.Divider(),
                
                # Instructions
                ft.Container(
                    ft.Column([
                        ft.Text("💬 Ask me anything about matrices!", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_800),
                        ft.Text("I can help with:", size=14),
                        ft.Text("• Matrix operations (addition, multiplication)", size=12),
                        ft.Text("• Determinants and inverses", size=12),
                        ft.Text("• Special matrices and properties", size=12),
                        ft.Text("• Real-world applications", size=12),
                    ], spacing=5),
                    bgcolor=ft.Colors.PURPLE_50,
                    border_radius=10,
                    padding=15,
                    margin=ft.margin.only(bottom=20)
                ),
                
                # Chat area
                ft.Container(
                    chat_messages,
                    bgcolor=ft.Colors.GREY_50,
                    border_radius=10,
                    padding=10,
                    margin=ft.margin.only(bottom=20)
                ),
                
                # Input area
                ft.Row([
                    ft.Container(user_input, expand=True),
                    ft.IconButton(
                        ft.Icons.SEND,
                        icon_color=ft.Colors.PURPLE_700,
                        on_click=send_message,
                        tooltip="Send message"
                    )
                ], spacing=10),
                
                # Quick help buttons
                ft.Text("Quick Help:", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_800),
                ft.ResponsiveRow([
                    ft.Container(
                        ft.ElevatedButton(
                            "Operations",
                            on_click=lambda e: self._quick_help("operations"),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.PURPLE_100)
                        ),
                        col={'xs': 6, 'sm': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            "Multiplication",
                            on_click=lambda e: self._quick_help("multiplication"),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.PURPLE_100)
                        ),
                        col={'xs': 6, 'sm': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            "Determinants",
                            on_click=lambda e: self._quick_help("determinants"),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.PURPLE_100)
                        ),
                        col={'xs': 6, 'sm': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            "Applications",
                            on_click=lambda e: self._quick_help("applications"),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.PURPLE_100)
                        ),
                        col={'xs': 6, 'sm': 3}
                    ),
                ], spacing=10)
            ], spacing=15),
            padding=20,
            expand=True
        )
        
        self.page.add(content)
        self.page.update()
    
    def _quick_help(self, topic):
        """Handle quick help buttons"""
        responses = {
            "operations": "Basic matrix operations: Addition/subtraction (same dimensions), scalar multiplication (multiply each element), and matrix multiplication (rows × columns). Remember: matrices must have compatible dimensions for operations.",
            "multiplication": "Matrix multiplication: A(m×n) × B(n×p) = C(m×p). The number of columns in A must equal the number of rows in B. Not commutative: AB ≠ BA. Each element is the dot product of row and column.",
            "determinants": "Determinants exist only for square matrices. For 2×2: det = ad-bc. For larger matrices, use cofactor expansion. If det = 0, the matrix is singular (no inverse). det(AB) = det(A) × det(B).",
            "applications": "Matrices are used in: computer graphics (transformations), solving systems of equations, data analysis, economics (input-output models), engineering (structural analysis), and machine learning algorithms."
        }
        
        # Add the response to chat
        chat_messages = None
        for control in self.page.controls:
            if hasattr(control, 'content'):
                chat_messages = self._find_chat_messages(control.content)
                if chat_messages:
                    break
        
        if chat_messages:
            chat_messages.controls.append(
                ft.Container(
                    ft.Text(f"AI Tutor: {responses[topic]}", size=14, color=ft.Colors.GREEN_900),
                    bgcolor=ft.Colors.GREEN_50,
                    border_radius=10,
                    padding=10,
                    alignment=ft.alignment.center_left
                )
            )
            self.page.update()
    
    def _find_chat_messages(self, control):
        """Recursively find chat messages container"""
        if hasattr(control, 'controls'):
            for child in control.controls:
                if isinstance(child, ft.Column) and hasattr(child, 'height') and child.height == 300:
                    return child
                elif hasattr(child, 'content'):
                    result = self._find_chat_messages(child.content)
                    if result:
                        return result
                elif hasattr(child, 'controls'):
                    result = self._find_chat_messages(child)
                    if result:
                        return result
        return None
    
    def _generate_ai_response(self, question):
        """Generate AI tutor response based on question"""
        question_lower = question.lower()
        
        if "multiplication" in question_lower or "multiply" in question_lower:
            return "Matrix multiplication requires the number of columns in the first matrix to equal the number of rows in the second. The result has dimensions from the outer dimensions. Each element is calculated as the dot product of the corresponding row and column. Want me to show a specific example?"
        
        elif "addition" in question_lower or "add" in question_lower:
            return "Matrix addition is element-wise: add corresponding elements. Both matrices must have the same dimensions. For example, [1,2] + [3,4] = [4,6]. It's commutative: A+B = B+A. What specific addition would you like help with?"
        
        elif "determinant" in question_lower:
            return "Determinants are scalar values for square matrices. For 2×2: det = ad-bc. For 3×3, use cofactor expansion. If det = 0, the matrix has no inverse. Determinants tell us about the matrix's invertibility and geometric properties."
        
        elif "inverse" in question_lower:
            return "A matrix has an inverse only if its determinant ≠ 0. For 2×2 matrix A=[a,b;c,d], A⁻¹ = (1/det(A)) × [d,-b;-c,a]. The inverse satisfies A × A⁻¹ = I (identity matrix). Need help finding a specific inverse?"
        
        elif "dimension" in question_lower or "size" in question_lower:
            return "Matrix dimensions are written as rows × columns. A 3×4 matrix has 3 rows and 4 columns. For operations: addition needs same dimensions, multiplication needs inner dimensions to match (columns of first = rows of second)."
        
        elif "transpose" in question_lower:
            return "The transpose of a matrix swaps rows and columns. If A has element aᵢⱼ, then Aᵀ has element aⱼᵢ. For example, [1,2;3,4]ᵀ = [1,3;2,4]. Useful property: (AB)ᵀ = BᵀAᵀ."
        
        elif "identity" in question_lower:
            return "The identity matrix I has 1s on the main diagonal and 0s elsewhere. It's the multiplicative identity: A × I = I × A = A. Each size has its own identity matrix: I₂, I₃, etc. It's like the number 1 for matrices."
        
        elif "system" in question_lower or "equation" in question_lower:
            return "Matrices can solve systems of linear equations using Ax = b form. Here A is the coefficient matrix, x is the variable vector, and b is the constant vector. Solution: x = A⁻¹b (if A is invertible). Want to see an example?"
        
        else:
            return "Great question about matrices! I can help with matrix operations (addition, multiplication), properties (determinants, inverses), special matrices (identity, transpose), or applications (solving systems). What specific aspect would you like to explore?"


def matrices_page(page: ft.Page):
    """Main entry point for Matrices module"""
    module = MatricesModule(page)
    module.show_page()
