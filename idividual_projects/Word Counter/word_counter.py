#BB 1st Word Counter Project
#Split the content into words and count them
def word_count(file_path):
    with open(file_path, "r") as file: 
        content = file.read()
        words = content.split()
        num_words = len(words)
        return f"Word Count: {num_words}"#Return the word count in a readable format