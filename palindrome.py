# Palindrome

def main():
    word = input()
    cleaned_text = ''.join(char.lower() for char in word if char.isalnum())
    print(cleaned_text == cleaned_text[::-1])

if __name__ == "__main__":
    main()
