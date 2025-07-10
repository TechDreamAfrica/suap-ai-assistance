# Sua Pa Student AI Learning Management System

An interactive mathematics learning platform built with Flet for Python, designed for comprehensive mathematical education from basic arithmetic to advanced calculus.

## Features

### 📚 Comprehensive Mathematics Curriculum

- **Basic Level**: Arithmetic, Fractions & Decimals, Number Patterns
- **Intermediate Level**: Algebra, Geometry, Trigonometry, Quadratic Equations
- **Advanced Level**: Calculus, Linear Functions, Statistics & Probability
- **Expert Level**: Matrices, Complex Numbers, Differential Equations, Vector Calculus, Number Theory

### 🎯 Interactive Learning Components

- **Explanations**: Clear, step-by-step topic explanations
- **Practice**: Interactive exercises for each topic
- **Quizzes**: Assessment tools to test understanding
- **AI Help**: Intelligent assistance for problem-solving

### 📱 Mobile-First Design

- Responsive layout optimized for mobile devices
- Touch-friendly interface elements
- Smooth navigation between topics
- Modern card-based UI design

### 🧭 Multi-Subject Platform

- Mathematics (Primary focus)
- Science, Physics, Chemistry, Biology
- English, Literature, History
- Computing, Geography, Art & Design

## Installation

### For Development

1. Install Python 3.8 or higher
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   python main.py
   ```

### Building Android APK

1. Install Flet build tools:
   ```
   pip install flet
   ```
2. Build APK:
   ```
   flet build apk
   ```

## Project Structure

```
desktop/
├── main.py                 # Main application entry point
├── maths_tutor.py         # Mathematics dashboard
├── science.py             # Science subjects
├── english.py             # English subject
├── computing.py           # Computing subject
├── physics.py             # Physics subject
├── history_teller.py      # History subject
├── other_subjects.py      # Additional subjects
├── topics/                # Mathematics topic modules
│   ├── basic_arithmetic.py
│   ├── fractions_decimals.py
│   ├── number_patterns.py
│   ├── algebra.py
│   ├── geometry.py
│   ├── trigonometry.py
│   ├── quadratic_equations.py
│   ├── statistics_probability.py
│   ├── linear_functions.py
│   ├── calculus.py
│   ├── matrices.py
│   ├── complex_numbers.py
│   ├── differential_equations.py
│   ├── vector_calculus.py
│   └── number_theory.py
├── assets/                # App icons and images
├── requirements.txt       # Python dependencies
├── pyproject.toml        # Project configuration
└── README.md             # This file
```

## Usage

1. **Home Dashboard**: Navigate between different subjects
2. **Mathematics Section**: Access 15 comprehensive math topics
3. **Topic Pages**: Each topic includes explanation, practice, quiz, and AI help
4. **Responsive Design**: Works seamlessly on phones, tablets, and desktop

## Configuration

The app is configured in `pyproject.toml` with the following settings:

- App Name: Sua Pa LMS
- Package ID: com.techdreamafrica.suapalms
- Target SDK: Android 34
- Minimum SDK: Android 21 (Android 5.0)

## Contributing

This project is developed by Tech Dream Africa as an educational platform for students in Africa and beyond.

## License

MIT License - See project configuration for details.

## Support

For support and updates, contact Tech Dream Africa.
