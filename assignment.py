import random

# Between 10-20 questions
MIN_QUESTIONS = 10
MAX_QUESTIONS = 20

# Only allow 2-digit numbers
MIN_VALUE = 10
MAX_VALUE = 99

# Code should print same questions on every run:
# This means random seed must be constant
SEED = 1

def generate_question(question):
    """Return a single question.

    Returns the same question every time is called, for a specific question number."""

    # Initialise random number generator with a seed that is always the same for a specific question
    random.seed(SEED*question)
    
    # Generate first and second number
    first = random.randint(MIN_VALUE, MAX_VALUE)
    second = random.randint(MIN_VALUE, MAX_VALUE)

    # Return print with result inlined
    return f"What is {first} + {second}?; {first+second}"


def ask_questions():
    """Prints between 10-20 questions regarding addition of 2 2-digit numbers.

    Prints the same questions between runs, assuming SEED is unchanged."""

    random.seed(SEED)
    num_questions = random.randint(MIN_QUESTIONS, MAX_QUESTIONS)

    for q in range(num_questions):
        print(generate_question(q))


if __name__ == "__main__":   
    ask_questions()

