#Import Libraries
import datetime, os
#Use time library to track when the file was last updated
def update_doc_info(file_path):
    mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))#Get the last modified time of the file and format it to be more readable
    mod_time = str(mod_time)#Cut off the milliseconds from the modified time
    clean_mod = mod_time[:19]
    return f"Last Updated: {clean_mod}"#Return the last modified time in a readable format
#test code
if __name__ == "__main__":
    test_file_path = "notes/reading.txt"
    update_doc_info(test_file_path)