from hangman import word_list, stages, logo, hint_map
import random

# Print the game logo
print(f"{logo}\n")

# Randomly choose a word from the list
chosen_word = random.choice(word_list)

# Initialize variables
placeholder = ""
correct_letters = []

# Display a hint for the chosen word
word_length = len(chosen_word)
print("--GUESS THE LETTERS TO FILL THE BLANKS AND MAKE A WORD✍️--\n")  
hint = hint_map.get(chosen_word, "No hint available")
print(f"🔍 HINT: It's a {hint}")

# Display blank placeholders for the chosen word
for letter in range(word_length):    
    placeholder += "_"
print(placeholder)    

print("\n***********You have 6 lifeline ************\n")
levels = 6  # Total lives

game_over = False
while not game_over:
    display = ""
    guess = input("Guess a letter:")

    # Check if letter was already guessed
    if guess in correct_letters:
        print(f"You have already guessed {guess}.")
        continue

    # If guess is correct, add to correct_letters list
    if guess in chosen_word:
        correct_letters.append(guess)

    # Build the display string with guessed letters and blanks
    for letter in chosen_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    # If guess was incorrect, reduce a life
    if guess not in chosen_word:
        levels -= 1
        
        if levels > 0:
            print("You guessed wrong. So you lose a life😖.")
            print(stages[levels])  # Show hangman stage
            print(f"You have {levels} lives left")
        else:
            game_over = True
            print("\n💀 GAME OVER 💀")

    # If word is fully guessed
    if "_" not in display:
        game_over = True
        print("🪄 YOU WIN 🪄")
