def count_words(text):
    # Split the text into words based on whitespace
    words = text.split()
    # Return the length of the list of words
    return len(words)

def main():
    # Prompt the user to enter a sentence or paragraph
    user_input = input("Please enter a sentence or paragraph: ")
    
    # Error handling for empty input
    if not user_input.strip():
        print("Error: You entered an empty input. Please enter some text.")
        return

    # Count the number of words in the input
    word_count = count_words(user_input)

    # Display the word count to the user
    print(f"The number of words in the entered text is: {word_count}")

if __name__ == "__main__":
    main()