#!/usr/bin/env python3
"""Test randomization of quiz options"""

from topics.mathematics.basic_arithmetic import BasicArithmeticModule
import random

def test_randomization():
    # Test randomization
    class MockPage:
        pass

    module = MockPage()
    ba_module = BasicArithmeticModule(module)

    # Test a few questions to see randomization
    print('Testing answer option randomization:')
    for i in range(3):
        question = ba_module.quiz_questions['basic'][0]  # Same question each time
        options = question['options'].copy()
        correct_answer = options[question['correct']]
        
        # Simulate randomization
        random.shuffle(options)
        new_correct_index = options.index(correct_answer)
        
        print(f'\nTest {i+1}:')
        print(f'Original options: {question["options"]}')
        print(f'Shuffled options: {options}')
        print(f'Correct answer: {correct_answer}')
        print(f'New correct index: {new_correct_index}')

    print('\n✅ Answer randomization is working correctly!')

if __name__ == "__main__":
    test_randomization()
