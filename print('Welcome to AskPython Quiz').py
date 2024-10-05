# Print the welcome message for the quiz
print('Welcome to AskPython Quiz')

# Prompt the user if they are ready to play the quiz and store their response
answer = input('Are you ready to play the Quiz? (yes/no): ')
score = 0  # Initialize the score counter
total_questions = 3  # Total number of questions in the quiz

# Check if the user is ready to play
if answer.lower() == 'yes':  # Convert the answer to lowercase for case-insensitive comparison
    # First question
    answer = input('Question 1: What is your favorite programming language? ')
    if answer.lower() == 'python':  # Check if the answer is 'python'
        score += 1  # Increment the score if the answer is correct
        print('Correct!')  # Print a message indicating the answer is correct
    else:
        print('Wrong Answer :(')  # Print a message indicating the answer is wrong

    # Second question
    answer = input('Question 2: Do you follow any author on AskPython? ')
    if answer.lower() == 'yes':  # Check if the answer is 'yes'
        score += 1  # Increment the score if the answer is correct
        print('Correct!')  # Print a message indicating the answer is correct
    else:
        print('Wrong Answer :(')  # Print a message indicating the answer is wrong

    # Third question
    answer = input('Question 3: What is the name of your favorite website for learning Python? ')
    if answer.lower() == 'askpython':  # Check if the answer is 'askpython'
        score += 1  # Increment the score if the answer is correct
        print('Correct!')  # Print a message indicating the answer is correct
    else:
        print('Wrong Answer :(')  # Print a message indicating the answer is wrong

    # Print the final score and percentage
    print(f'Thank you for playing this small quiz game! You attempted {score} questions correctly.')
    mark = (score / total_questions) * 100  # Calculate the percentage score
    print(f'Marks obtained: {mark:.1f}%')  # Print the percentage score with one decimal place
else:
    print('Goodbye!')  # Print a message if the user is not ready to play