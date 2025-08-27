import flet as ft
import random
import time

def get_ai_help(query, topic="computing"):
    """AI help response for Computing & ICT"""
    try:
        responses = {
            "computer": "A computer is an electronic device that processes data using instructions (programs). Key components include hardware (CPU, RAM, storage, input/output devices) and software (operating system, applications). Understanding how these work together helps you use technology effectively.",
            "programming": "Programming is writing instructions for computers using code. Popular languages include Python (beginner-friendly), JavaScript (web development), and Java (applications). Start with basic concepts like variables, loops, and functions before moving to complex projects.",
            "python": "Python is an excellent programming language for beginners. It has simple syntax and is used for web development, data analysis, AI, and automation. Start with basic concepts: variables (storing data), functions (reusable code), and control structures (if/else, loops).",
            "web": "Web development involves creating websites using HTML (structure), CSS (styling), and JavaScript (interactivity). HTML defines content, CSS makes it look good, and JavaScript adds functionality. Start with basic HTML tags and work up to responsive design.",
            "html": "HTML (HyperText Markup Language) is the foundation of web pages. It uses tags like <h1> for headings, <p> for paragraphs, <div> for containers, and <a> for links. Each tag has opening and closing parts: <tag>content</tag>.",
            "css": "CSS (Cascading Style Sheets) controls how HTML looks. Use selectors to target elements, then apply properties like color, font-size, margin, and padding. You can style by tag name, class (.classname), or ID (#idname).",
            "javascript": "JavaScript makes web pages interactive. It can respond to clicks, validate forms, create animations, and update content dynamically. Key concepts include variables (let, const), functions, event handlers, and DOM manipulation.",
            "database": "Databases store and organize data efficiently. SQL (Structured Query Language) is used to retrieve and manipulate data. Basic operations include SELECT (get data), INSERT (add data), UPDATE (change data), and DELETE (remove data).",
            "network": "Networks connect computers to share resources and communicate. The internet is a global network using protocols like HTTP, TCP/IP. Understanding networks helps with web development, cybersecurity, and cloud computing.",
            "security": "Cybersecurity protects systems and data from threats. Key practices include strong passwords, regular updates, avoiding suspicious links, using antivirus software, and understanding phishing attacks. Always think before clicking or sharing personal information.",
            "ai": "Artificial Intelligence (AI) enables machines to perform tasks that typically require human intelligence. Machine learning is a subset where systems learn from data. Applications include voice assistants, recommendation systems, and image recognition."
        }
        
        query_lower = query.lower()
        for key, response in responses.items():
            if key in query_lower:
                return f"🤖 AI Helper: {response}"
        
        return "🤖 AI Helper: Computing covers hardware, software, programming, web development, databases, networks, and cybersecurity. Ask about specific topics like Python, HTML, databases, or cybersecurity for detailed help!"
    except Exception:
        return "🤖 AI Helper: I'm here to help with computing and ICT topics! Try asking about programming, web development, or computer fundamentals."

class ComputingModule:
    def __init__(self, page):
        self.page = page
        self.current_quiz_level = "basic"
        self.quiz_score = 0
        self.quiz_question_index = 0
        
        # Programming tutorials and examples
        self.programming_tutorials = {
            "python": {
                "title": "Python Programming Basics",
                "lessons": [
                    {
                        "title": "Variables and Data Types",
                        "content": "Variables store data in Python. Common types include:\n\n• Strings: text data in quotes\n• Integers: whole numbers\n• Floats: decimal numbers\n• Booleans: True/False values",
                        "code_example": """# Python Variables Example
name = "Alice"          # String
age = 16               # Integer
height = 5.4           # Float
is_student = True      # Boolean

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Student: {is_student}")"""
                    },
                    {
                        "title": "Control Structures",
                        "content": "Control structures direct program flow:\n\n• if/elif/else: make decisions\n• for loops: repeat code\n• while loops: repeat while condition is true",
                        "code_example": """# Control Structures Example
score = 85

# If-elif-else statement
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

# For loop example
for i in range(5):
    print(f"Count: {i}")"""
                    }
                ]
            },
            "web": {
                "title": "Web Development Fundamentals",
                "lessons": [
                    {
                        "title": "HTML Basics",
                        "content": "HTML structures web content using tags:\n\n• <h1>-<h6>: headings\n• <p>: paragraphs\n• <div>: containers\n• <a>: links\n• <img>: images",
                        "code_example": """<!DOCTYPE html>
<html>
<head>
    <title>My First Website</title>
</head>
<body>
    <h1>Welcome to My Site</h1>
    <p>This is a paragraph with some text.</p>
    
    <div>
        <h2>About Me</h2>
        <p>I'm learning web development!</p>
        <a href="https://example.com">Visit Example</a>
    </div>
</body>
</html>"""
                    },
                    {
                        "title": "CSS Styling",
                        "content": "CSS controls appearance and layout:\n\n• Selectors target elements\n• Properties define styling\n• Values specify how to style\n• Box model: margin, border, padding, content",
                        "code_example": """/* CSS Example */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
    background-color: #f0f0f0;
}

h1 {
    color: #333;
    text-align: center;
    border-bottom: 2px solid #007bff;
}

.container {
    max-width: 800px;
    margin: 0 auto;
    background-color: white;
    padding: 20px;
    border-radius: 8px;
}"""
                    }
                ]
            }
        }
        
        # Computing quiz questions
        self.quiz_questions = {
            "basic": [
                {
                    "question": "What does CPU stand for?",
                    "options": ["Computer Processing Unit", "Central Processing Unit", "Central Program Unit", "Computer Program Unit"],
                    "correct": 1,
                    "explanation": "CPU stands for Central Processing Unit. It's the 'brain' of the computer that executes instructions and performs calculations."
                },
                {
                    "question": "Which of these is a programming language?",
                    "options": ["HTML", "Python", "CSS", "HTTP"],
                    "correct": 1,
                    "explanation": "Python is a programming language. HTML and CSS are markup/styling languages, while HTTP is a network protocol."
                },
                {
                    "question": "What does WWW stand for?",
                    "options": ["World Wide Web", "World Wide Wait", "Web World Wide", "Wide World Web"],
                    "correct": 0,
                    "explanation": "WWW stands for World Wide Web, the system of interlinked web pages accessible via the internet."
                }
            ],
            "intermediate": [
                {
                    "question": "In web development, what does CSS primarily control?",
                    "options": ["Content structure", "Visual styling and layout", "Server-side logic", "Database connections"],
                    "correct": 1,
                    "explanation": "CSS (Cascading Style Sheets) primarily controls the visual styling and layout of web pages, including colors, fonts, spacing, and positioning."
                },
                {
                    "question": "Which SQL command is used to retrieve data from a database?",
                    "options": ["INSERT", "UPDATE", "SELECT", "DELETE"],
                    "correct": 2,
                    "explanation": "SELECT is used to retrieve data from a database. INSERT adds data, UPDATE modifies data, and DELETE removes data."
                },
                {
                    "question": "What is the main purpose of a firewall?",
                    "options": ["Speed up internet", "Prevent unauthorized access", "Store passwords", "Compress files"],
                    "correct": 1,
                    "explanation": "A firewall's main purpose is to prevent unauthorized access by monitoring and controlling incoming and outgoing network traffic."
                }
            ]
        }
        
        # Project ideas
        self.project_ideas = [
            {
                "title": "Personal Portfolio Website",
                "description": "Create a website showcasing your projects and skills",
                "technologies": ["HTML", "CSS", "JavaScript"],
                "difficulty": "Beginner",
                "steps": [
                    "Design the layout and structure",
                    "Create HTML pages (home, about, projects, contact)",
                    "Style with CSS (colors, fonts, layout)",
                    "Add JavaScript for interactivity",
                    "Test and deploy your site"
                ]
            },
            {
                "title": "Simple Calculator",
                "description": "Build a calculator that performs basic arithmetic operations",
                "technologies": ["Python", "Tkinter"],
                "difficulty": "Beginner",
                "steps": [
                    "Set up the GUI with buttons and display",
                    "Create functions for each operation (+, -, *, /)",
                    "Handle user input and button clicks",
                    "Display results and handle errors",
                    "Add advanced features (memory, history)"
                ]
            },
            {
                "title": "To-Do List App",
                "description": "Create an app to manage tasks and productivity",
                "technologies": ["HTML", "CSS", "JavaScript", "Local Storage"],
                "difficulty": "Intermediate",
                "steps": [
                    "Design the user interface",
                    "Implement add/remove task functionality",
                    "Add task completion tracking",
                    "Use local storage to save tasks",
                    "Add features like categories, due dates"
                ]
            }
        ]

    def create_main_view(self):
        return ft.Container(
            ft.Column([
                ft.Text("💻 Computing & ICT Center", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900, text_align=ft.TextAlign.CENTER),
                ft.Text("Master programming, web development, and digital literacy skills", size=16, color=ft.Colors.BLUE_700, text_align=ft.TextAlign.CENTER),
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
                                ft.Icon(ft.Icons.CODE, size=30, color=ft.Colors.PURPLE_700),
                                ft.Text("Programming", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_programming(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.PURPLE_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.WEB, size=30, color=ft.Colors.TEAL_700),
                                ft.Text("Web Dev", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_web_development(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.TEAL_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.COMPUTER, size=30, color=ft.Colors.GREEN_700),
                                ft.Text("Fundamentals", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_fundamentals(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.GREEN_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                ], spacing=10, run_spacing=10),
                
                ft.ResponsiveRow([
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.QUIZ, size=30, color=ft.Colors.ORANGE_700),
                                ft.Text("Tech Quiz", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_quizzes(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.ORANGE_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.LIGHTBULB, size=30, color=ft.Colors.PINK_700),
                                ft.Text("Projects", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_projects(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.PINK_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.SECURITY, size=30, color=ft.Colors.RED_700),
                                ft.Text("Cybersecurity", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_cybersecurity(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.RED_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.STORAGE, size=30, color=ft.Colors.INDIGO_700),
                                ft.Text("Databases", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_databases(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.INDIGO_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                ], spacing=10, run_spacing=10),
                
                ft.Divider(height=20),
                
                # Quick overview
                ft.Container(
                    ft.Column([
                        ft.Text("💻 Computing & ICT Overview", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800),
                        ft.Text("Develop comprehensive digital skills from basic computer literacy to advanced programming.", size=14),
                        ft.Text("🎯 Core Areas:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
                        ft.Column([
                            ft.Text("• Computer fundamentals and digital literacy", size=14),
                            ft.Text("• Programming in Python, JavaScript, and more", size=14),
                            ft.Text("• Web development with HTML, CSS, and JavaScript", size=14),
                            ft.Text("• Database design and management", size=14),
                            ft.Text("• Cybersecurity and digital safety", size=14),
                            ft.Text("• Project-based learning and practical skills", size=14),
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
            label="Ask about computing and ICT...",
            hint_text="e.g., How do I start programming? or What is a database?",
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
            "/computing/ai_help",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/computing")),
                    title=ft.Text("AI Computing Assistant"),
                    bgcolor=ft.Colors.BLUE_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("🤖 AI Computing & ICT Assistant", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                        query_field,
                        ft.ElevatedButton(
                            "Get Help",
                            on_click=handle_query,
                            style=ft.ButtonStyle(bgcolor=ft.Colors.BLUE_600, color=ft.Colors.WHITE)
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

    def show_programming(self):
        self.page.views.clear()
        
        language_cards = []
        for lang, tutorial in self.programming_tutorials.items():
            lessons_preview = f"{len(tutorial['lessons'])} lessons available"
            
            card = ft.Container(
                ft.Column([
                    ft.Text(tutorial["title"], size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_900),
                    ft.Text(lessons_preview, size=14, color=ft.Colors.PURPLE_700),
                    ft.ElevatedButton(
                        "Start Learning",
                        on_click=lambda e, language=lang: self.show_tutorial(language, 0),
                        style=ft.ButtonStyle(bgcolor=ft.Colors.PURPLE_600, color=ft.Colors.WHITE)
                    )
                ], spacing=15),
                bgcolor=ft.Colors.PURPLE_50,
                border_radius=12,
                padding=20,
                border=ft.border.all(2, ft.Colors.PURPLE_200),
                margin=ft.margin.only(bottom=15)
            )
            language_cards.append(card)
        
        # Code practice area
        code_practice = ft.Container(
            ft.Column([
                ft.Text("💻 Interactive Code Practice", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_900),
                ft.Text("Practice coding with this interactive editor:", size=14),
                ft.TextField(
                    label="Write your code here...",
                    hint_text="# Try writing some Python code\nprint('Hello, World!')",
                    multiline=True,
                    min_lines=8,
                    max_lines=12,
                    border_color=ft.Colors.PURPLE_300,
                    value=""
                ),
                ft.Row([
                    ft.ElevatedButton(
                        "Run Code",
                        on_click=lambda e: self.page.show_snack_bar(ft.SnackBar(content=ft.Text("Code execution coming soon!"))),
                        style=ft.ButtonStyle(bgcolor=ft.Colors.PURPLE_600, color=ft.Colors.WHITE)
                    ),
                    ft.ElevatedButton(
                        "Clear",
                        on_click=lambda e: self.page.show_snack_bar(ft.SnackBar(content=ft.Text("Code cleared!")))
                    ),
                    ft.ElevatedButton(
                        "Save",
                        on_click=lambda e: self.page.show_snack_bar(ft.SnackBar(content=ft.Text("Code saved locally!")))
                    )
                ], alignment=ft.MainAxisAlignment.CENTER, spacing=10)
            ], spacing=15),
            bgcolor=ft.Colors.PURPLE_50,
            border_radius=12,
            padding=20,
            border=ft.border.all(2, ft.Colors.PURPLE_200)
        )
        
        view = ft.View(
            "/computing/programming",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/computing")),
                    title=ft.Text("Programming Tutorials"),
                    bgcolor=ft.Colors.PURPLE_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("🐍 Programming Learning Center", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_900),
                        ft.Text("Learn programming with step-by-step tutorials and hands-on practice", size=16, color=ft.Colors.PURPLE_700),
                        ft.Column(language_cards, spacing=0),
                        code_practice
                    ], spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def show_tutorial(self, language, lesson_index):
        tutorial = self.programming_tutorials.get(language)
        if not tutorial or lesson_index >= len(tutorial["lessons"]):
            return
        
        lesson = tutorial["lessons"][lesson_index]
        
        self.page.views.clear()
        view = ft.View(
            "/computing/tutorial",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.show_programming()),
                    title=ft.Text(f"{tutorial['title']} - Lesson {lesson_index + 1}"),
                    bgcolor=ft.Colors.PURPLE_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text(lesson["title"], size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_900),
                        ft.Container(
                            ft.Text(lesson["content"], size=14),
                            bgcolor=ft.Colors.PURPLE_50,
                            border_radius=8,
                            padding=15,
                            border=ft.border.all(1, ft.Colors.PURPLE_200)
                        ),
                        ft.Text("Code Example:", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_900),
                        ft.Container(
                            ft.Text(lesson["code_example"], size=12, font_family="monospace", selectable=True),
                            bgcolor=ft.Colors.BLACK87,
                            border_radius=8,
                            padding=15
                        ),
                        ft.Row([
                            ft.ElevatedButton(
                                "Previous" if lesson_index > 0 else "Back to Programming",
                                on_click=lambda e: (
                                    self.show_tutorial(language, lesson_index - 1) 
                                    if lesson_index > 0 
                                    else self.show_programming()
                                ),
                                style=ft.ButtonStyle(bgcolor=ft.Colors.PURPLE_600, color=ft.Colors.WHITE)
                            ),
                            ft.ElevatedButton(
                                "Next Lesson" if lesson_index + 1 < len(tutorial["lessons"]) else "Complete",
                                on_click=lambda e: (
                                    self.show_tutorial(language, lesson_index + 1) 
                                    if lesson_index + 1 < len(tutorial["lessons"]) 
                                    else self.show_programming()
                                ),
                                style=ft.ButtonStyle(bgcolor=ft.Colors.PURPLE_600, color=ft.Colors.WHITE)
                            )
                        ], alignment=ft.MainAxisAlignment.CENTER, spacing=15)
                    ], spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def show_web_development(self):
        self.page.views.clear()
        
        web_topics = [
            {
                "title": "HTML Fundamentals",
                "description": "Learn the structure of web pages",
                "content": "HTML (HyperText Markup Language) is the foundation of all websites. Key concepts:\n\n• Elements and Tags: Building blocks of HTML\n• Document Structure: DOCTYPE, html, head, body\n• Common Tags: headings, paragraphs, links, images\n• Attributes: Additional information for elements\n• Semantic HTML: Meaningful structure for accessibility",
                "example": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Website</title>
</head>
<body>
    <header>
        <h1>Welcome to My Site</h1>
        <nav>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="home">
            <h2>Home Section</h2>
            <p>This is a paragraph with some content.</p>
        </section>
    </main>
</body>
</html>"""
            },
            {
                "title": "CSS Styling",
                "description": "Make your websites beautiful",
                "content": "CSS (Cascading Style Sheets) controls the visual appearance of web pages:\n\n• Selectors: Target HTML elements to style\n• Properties: Define what to change (color, size, position)\n• Values: Specify how to change it\n• Box Model: margin, border, padding, content\n• Layout: flexbox, grid, positioning",
                "example": """/* Basic CSS Styling */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Arial', sans-serif;
    line-height: 1.6;
    color: #333;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

.btn {
    display: inline-block;
    padding: 10px 20px;
    background: #007bff;
    color: white;
    text-decoration: none;
    border-radius: 5px;
    transition: background 0.3s;
}

.btn:hover {
    background: #0056b3;
}"""
            }
        ]
        
        topic_cards = []
        for topic in web_topics:
            card = ft.ExpansionTile(
                title=ft.Text(topic["title"], size=18, weight=ft.FontWeight.BOLD),
                subtitle=ft.Text(topic["description"]),
                controls=[
                    ft.Container(
                        ft.Column([
                            ft.Text(topic["content"], size=14),
                            ft.Text("Example Code:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.TEAL_700),
                            ft.Container(
                                ft.Text(topic["example"], size=12, font_family="monospace", selectable=True),
                                bgcolor=ft.Colors.BLACK87,
                                border_radius=8,
                                padding=15
                            )
                        ], spacing=10),
                        padding=15,
                        bgcolor=ft.Colors.TEAL_50,
                        border_radius=8
                    )
                ]
            )
            topic_cards.append(card)
        
        view = ft.View(
            "/computing/web_dev",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/computing")),
                    title=ft.Text("Web Development"),
                    bgcolor=ft.Colors.TEAL_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("🌐 Web Development Mastery", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.TEAL_900),
                        ft.Text("Learn to build modern, responsive websites from scratch", size=16, color=ft.Colors.TEAL_700),
                        ft.Container(
                            ft.Column([
                                ft.Text("Learning Path:", size=16, weight=ft.FontWeight.BOLD),
                                ft.Text("1. HTML - Structure your content", size=14),
                                ft.Text("2. CSS - Style and layout", size=14),
                                ft.Text("3. JavaScript - Add interactivity", size=14),
                                ft.Text("4. Responsive design - Mobile-friendly sites", size=14),
                                ft.Text("5. Modern frameworks - React, Vue, Angular", size=14),
                            ], spacing=5),
                            bgcolor=ft.Colors.BLUE_50,
                            border_radius=8,
                            padding=15,
                            border=ft.border.all(1, ft.Colors.BLUE_200),
                            margin=ft.margin.only(bottom=20)
                        ),
                        ft.Column(topic_cards, spacing=10)
                    ], spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def show_fundamentals(self):
        self.page.views.clear()
        
        fundamental_topics = [
            {
                "title": "Computer Hardware",
                "content": "Key hardware components:\n\n• CPU (Central Processing Unit): The brain of the computer\n• RAM (Random Access Memory): Temporary storage for active programs\n• Storage: Hard drives (HDD) and solid-state drives (SSD)\n• Motherboard: Connects all components\n• GPU (Graphics Processing Unit): Handles visual processing\n• Input/Output devices: Keyboard, mouse, monitor, speakers",
                "icon": ft.Icons.MEMORY
            },
            {
                "title": "Operating Systems",
                "content": "Operating systems manage computer resources:\n\n• Windows: Most common desktop OS\n• macOS: Apple's operating system\n• Linux: Open-source, popular for servers\n• Mobile OS: iOS and Android\n• Functions: File management, memory management, device drivers, user interface\n• File systems: How data is stored and organized",
                "icon": ft.Icons.DESKTOP_WINDOWS
            },
            {
                "title": "Software Types",
                "content": "Different categories of software:\n\n• System Software: OS, device drivers, utilities\n• Application Software: Programs for end users\n• Programming Software: Tools for developers\n• Open Source vs Proprietary\n• Software licensing and copyright\n• Software updates and security patches",
                "icon": ft.Icons.APPS
            },
            {
                "title": "Digital Literacy",
                "content": "Essential digital skills:\n\n• File management: Creating folders, organizing files\n• Internet basics: Browsing, searching, email\n• Digital communication: Email etiquette, video calls\n• Online safety: Password security, privacy settings\n• Digital footprint: Understanding online presence\n• Troubleshooting: Basic problem-solving skills",
                "icon": ft.Icons.LIGHTBULB
            }
        ]
        
        topic_cards = []
        for topic in fundamental_topics:
            card = ft.Container(
                ft.Column([
                    ft.Row([
                        ft.Icon(topic["icon"], size=30, color=ft.Colors.GREEN_700),
                        ft.Text(topic["title"], size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_900)
                    ], spacing=10),
                    ft.Text(topic["content"], size=14),
                ], spacing=15),
                bgcolor=ft.Colors.GREEN_50,
                border_radius=12,
                padding=20,
                border=ft.border.all(2, ft.Colors.GREEN_200),
                margin=ft.margin.only(bottom=15)
            )
            topic_cards.append(card)
        
        view = ft.View(
            "/computing/fundamentals",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/computing")),
                    title=ft.Text("Computer Fundamentals"),
                    bgcolor=ft.Colors.GREEN_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("💻 Computer Fundamentals", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_900),
                        ft.Text("Build a solid foundation in computing concepts and digital literacy", size=16, color=ft.Colors.GREEN_700),
                        ft.Column(topic_cards, spacing=0)
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
        self.page.views.clear()
        
        view = ft.View(
            "/computing/quizzes",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/computing")),
                    title=ft.Text("Technology Quizzes"),
                    bgcolor=ft.Colors.ORANGE_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("📝 Choose Quiz Level", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_900),
                        
                        ft.ResponsiveRow([
                            ft.Container(
                                ft.ElevatedButton(
                                    content=ft.Column([
                                        ft.Icon(ft.Icons.LOOKS_ONE, size=30, color=ft.Colors.GREEN_700),
                                        ft.Text("Basic", size=16, weight=ft.FontWeight.BOLD),
                                        ft.Text("Computer fundamentals", size=12)
                                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                                    on_click=lambda e: self.start_quiz("basic"),
                                    style=ft.ButtonStyle(padding=20, bgcolor=ft.Colors.GREEN_50, shape=ft.RoundedRectangleBorder(radius=10))
                                ),
                                col={'xs': 12, 'sm': 6}
                            ),
                            ft.Container(
                                ft.ElevatedButton(
                                    content=ft.Column([
                                        ft.Icon(ft.Icons.LOOKS_TWO, size=30, color=ft.Colors.ORANGE_700),
                                        ft.Text("Intermediate", size=16, weight=ft.FontWeight.BOLD),
                                        ft.Text("Programming & databases", size=12)
                                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                                    on_click=lambda e: self.start_quiz("intermediate"),
                                    style=ft.ButtonStyle(padding=20, bgcolor=ft.Colors.ORANGE_50, shape=ft.RoundedRectangleBorder(radius=10))
                                ),
                                col={'xs': 12, 'sm': 6}
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
                        bgcolor=ft.Colors.ORANGE_50,
                        shape=ft.RoundedRectangleBorder(radius=8)
                    ),
                    expand=True
                )
            )
        
        self.page.views.clear()
        view = ft.View(
            "/computing/quiz_question",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.show_quizzes()),
                    title=ft.Text(f"Quiz - Question {self.quiz_question_index + 1}"),
                    bgcolor=ft.Colors.ORANGE_700
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
            "/computing/quiz_explanation",
            [
                ft.AppBar(
                    title=ft.Text("Answer Explanation"),
                    bgcolor=ft.Colors.ORANGE_700
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
                            bgcolor=ft.Colors.ORANGE_50,
                            border_radius=10,
                            padding=15
                        ),
                        ft.ElevatedButton(
                            "Next Question",
                            on_click=lambda e: self.next_question(),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.ORANGE_600, color=ft.Colors.WHITE)
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
            message = "Excellent work!"
            color = ft.Colors.GREEN
        elif percentage >= 60:
            message = "Good job!"
            color = ft.Colors.ORANGE
        else:
            message = "Keep learning!"
            color = ft.Colors.RED
        
        self.page.views.clear()
        view = ft.View(
            "/computing/quiz_results",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/computing")),
                    title=ft.Text("Quiz Results"),
                    bgcolor=ft.Colors.ORANGE_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("Quiz Complete!", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_900),
                        ft.Text(f"Score: {self.quiz_score}/{total_questions} ({percentage:.0f}%)", size=20),
                        ft.Text(message, size=18, color=color, weight=ft.FontWeight.BOLD),
                        ft.ElevatedButton(
                            "Try Again",
                            on_click=lambda e: self.start_quiz(self.current_quiz_level),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.ORANGE_600, color=ft.Colors.WHITE)
                        ),
                        ft.ElevatedButton(
                            "Back to Computing",
                            on_click=lambda e: self.page.go("/computing")
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

    def show_projects(self):
        self.page.views.clear()
        
        project_cards = []
        for project in self.project_ideas:
            steps_text = "\n".join([f"{i+1}. {step}" for i, step in enumerate(project["steps"])])
            tech_text = ", ".join(project["technologies"])
            
            card = ft.Container(
                ft.Column([
                    ft.Text(project["title"], size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.PINK_900),
                    ft.Text(project["description"], size=14),
                    ft.Row([
                        ft.Container(
                            ft.Text(f"Difficulty: {project['difficulty']}", size=12, weight=ft.FontWeight.BOLD),
                            bgcolor=ft.Colors.PINK_200,
                            border_radius=5,
                            padding=ft.padding.symmetric(horizontal=8, vertical=4)
                        ),
                        ft.Container(
                            ft.Text(f"Tech: {tech_text}", size=12),
                            bgcolor=ft.Colors.BLUE_100,
                            border_radius=5,
                            padding=ft.padding.symmetric(horizontal=8, vertical=4)
                        )
                    ], spacing=10),
                    ft.ExpansionTile(
                        title=ft.Text("Project Steps", size=14, weight=ft.FontWeight.BOLD),
                        controls=[
                            ft.Container(
                                ft.Text(steps_text, size=12),
                                padding=10,
                                bgcolor=ft.Colors.PINK_50
                            )
                        ]
                    ),
                    ft.ElevatedButton(
                        "Start Project",
                        on_click=lambda e, title=project["title"]: self.start_project(title),
                        style=ft.ButtonStyle(bgcolor=ft.Colors.PINK_600, color=ft.Colors.WHITE)
                    )
                ], spacing=10),
                bgcolor=ft.Colors.PINK_50,
                border_radius=12,
                padding=20,
                border=ft.border.all(2, ft.Colors.PINK_200),
                margin=ft.margin.only(bottom=15)
            )
            project_cards.append(card)
        
        view = ft.View(
            "/computing/projects",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/computing")),
                    title=ft.Text("Computing Projects"),
                    bgcolor=ft.Colors.PINK_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("💡 Computing Project Ideas", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.PINK_900),
                        ft.Text("Build real projects to apply your computing skills", size=16, color=ft.Colors.PINK_700),
                        ft.Column(project_cards, spacing=0)
                    ], spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def start_project(self, project_title):
        self.page.show_snack_bar(
            ft.SnackBar(content=ft.Text(f"Project '{project_title}' guide coming soon! Check back for detailed tutorials."))
        )

    def show_cybersecurity(self):
        self.page.views.clear()
        
        security_topics = [
            {
                "title": "Password Security",
                "content": "Creating and managing secure passwords:\n\n• Use strong, unique passwords for each account\n• Include uppercase, lowercase, numbers, and symbols\n• Avoid personal information and common words\n• Use a password manager to store passwords securely\n• Enable two-factor authentication (2FA) when available\n• Change passwords if accounts are compromised",
                "icon": ft.Icons.LOCK
            },
            {
                "title": "Online Safety",
                "content": "Staying safe while browsing and communicating:\n\n• Verify website authenticity before entering personal info\n• Be cautious with email attachments and links\n• Use secure networks (avoid public WiFi for sensitive tasks)\n• Keep software and browsers updated\n• Be aware of social engineering tactics\n• Respect digital privacy and copyright laws",
                "icon": ft.Icons.SHIELD
            },
            {
                "title": "Data Protection",
                "content": "Protecting your personal and digital information:\n\n• Regular backups of important data\n• Use encryption for sensitive files\n• Understand privacy settings on social media\n• Be cautious about what you share online\n• Know your digital rights and responsibilities\n• Use reputable antivirus software",
                "icon": ft.Icons.SECURITY
            },
            {
                "title": "Recognizing Threats",
                "content": "Common cyber threats and how to avoid them:\n\n• Phishing: Fake emails/websites stealing information\n• Malware: Viruses, trojans, ransomware\n• Social engineering: Manipulating people for information\n• Identity theft: Unauthorized use of personal information\n• Online scams: Too-good-to-be-true offers\n• Cyberbullying: Harassment through digital platforms",
                "icon": ft.Icons.WARNING
            }
        ]
        
        topic_cards = []
        for topic in security_topics:
            card = ft.Container(
                ft.Column([
                    ft.Row([
                        ft.Icon(topic["icon"], size=30, color=ft.Colors.RED_700),
                        ft.Text(topic["title"], size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.RED_900)
                    ], spacing=10),
                    ft.Text(topic["content"], size=14),
                ], spacing=15),
                bgcolor=ft.Colors.RED_50,
                border_radius=12,
                padding=20,
                border=ft.border.all(2, ft.Colors.RED_200),
                margin=ft.margin.only(bottom=15)
            )
            topic_cards.append(card)
        
        view = ft.View(
            "/computing/cybersecurity",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/computing")),
                    title=ft.Text("Cybersecurity"),
                    bgcolor=ft.Colors.RED_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("🔒 Cybersecurity Essentials", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.RED_900),
                        ft.Text("Learn to protect yourself and your data in the digital world", size=16, color=ft.Colors.RED_700),
                        ft.Container(
                            ft.Column([
                                ft.Text("🚨 Remember:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.RED_800),
                                ft.Text("• Think before you click", size=14),
                                ft.Text("• Keep software updated", size=14),
                                ft.Text("• Use strong, unique passwords", size=14),
                                ft.Text("• Be skeptical of unsolicited messages", size=14),
                                ft.Text("• Backup important data regularly", size=14),
                            ], spacing=5),
                            bgcolor=ft.Colors.YELLOW_50,
                            border_radius=8,
                            padding=15,
                            border=ft.border.all(2, ft.Colors.YELLOW_300),
                            margin=ft.margin.only(bottom=20)
                        ),
                        ft.Column(topic_cards, spacing=0)
                    ], spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def show_databases(self):
        self.page.views.clear()
        
        database_content = """
        Databases store and organize information efficiently. Key concepts:

        📊 Database Fundamentals:
        • Tables: Store data in rows and columns
        • Primary Key: Unique identifier for each record
        • Foreign Key: Links tables together
        • Relationships: How tables connect (one-to-one, one-to-many)

        💾 Types of Databases:
        • Relational (SQL): MySQL, PostgreSQL, SQLite
        • NoSQL: MongoDB, Firebase (for flexible data)
        • Cloud Databases: AWS RDS, Google Cloud SQL

        🔍 SQL Basics:
        • SELECT: Retrieve data
        • INSERT: Add new records
        • UPDATE: Modify existing data
        • DELETE: Remove records
        • WHERE: Filter results
        • JOIN: Combine data from multiple tables

        🏗️ Database Design:
        • Plan your data structure
        • Normalize data (avoid duplication)
        • Define relationships between entities
        • Consider performance and scalability
        """
        
        sql_examples = """-- Basic SQL Examples

-- Select all students
SELECT * FROM students;

-- Select specific columns
SELECT name, age FROM students WHERE age > 16;

-- Insert a new student
INSERT INTO students (name, age, grade) 
VALUES ('John Doe', 17, 'A');

-- Update a student's grade
UPDATE students 
SET grade = 'A+' 
WHERE name = 'John Doe';

-- Delete a student record
DELETE FROM students 
WHERE age < 16;

-- Join tables to get student courses
SELECT students.name, courses.course_name
FROM students
JOIN enrollments ON students.id = enrollments.student_id
JOIN courses ON enrollments.course_id = courses.id;"""
        
        view = ft.View(
            "/computing/databases",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/computing")),
                    title=ft.Text("Database Fundamentals"),
                    bgcolor=ft.Colors.INDIGO_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("🗄️ Database Management", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.INDIGO_900),
                        ft.Text("Learn to design, create, and manage databases effectively", size=16, color=ft.Colors.INDIGO_700),
                        ft.Container(
                            ft.Text(database_content, size=14, selectable=True),
                            bgcolor=ft.Colors.INDIGO_50,
                            border_radius=8,
                            padding=20,
                            border=ft.border.all(1, ft.Colors.INDIGO_200)
                        ),
                        ft.Text("SQL Examples:", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.INDIGO_900),
                        ft.Container(
                            ft.Text(sql_examples, size=12, font_family="monospace", selectable=True),
                            bgcolor=ft.Colors.BLACK87,
                            border_radius=8,
                            padding=15
                        ),
                        ft.Row([
                            ft.ElevatedButton(
                                "Practice SQL",
                                on_click=lambda e: self.page.show_snack_bar(ft.SnackBar(content=ft.Text("Interactive SQL practice coming soon!"))),
                                style=ft.ButtonStyle(bgcolor=ft.Colors.INDIGO_600, color=ft.Colors.WHITE)
                            ),
                            ft.ElevatedButton(
                                "Database Projects",
                                on_click=lambda e: self.page.show_snack_bar(ft.SnackBar(content=ft.Text("Database project tutorials coming soon!")))
                            )
                        ], alignment=ft.MainAxisAlignment.CENTER, spacing=15)
                    ], spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

def computing_page(page: ft.Page):
    page.title = "Computing - Student AI Assistance"
    page.scroll = ft.ScrollMode.AUTO
    
    # Clear page content first
    page.clean()
    
    page.appbar = ft.AppBar(
        leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: page.go("/")),
        title=ft.Text("Computing Hub"),
        bgcolor=ft.Colors.BLUE_700,
        center_title=True
    )
    
    module = ComputingModule(page)
    page.add(module.create_main_view())