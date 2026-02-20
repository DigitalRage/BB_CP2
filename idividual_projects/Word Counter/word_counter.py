#BB 1st Word Counter Project
#Import Libraries
def word_count(file_path):
    with open(file_path, "r") as file: 
        content = file.read()
        words = content.split()
        num_words = len(words)
        print(f"Number of words in the document: {num_words}")