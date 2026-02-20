#Import Libraries
import time_manager
#Open txt file
while True: 
    #Get file path from user
    options = input("""--- Document Word Count Updater ---\n1. Update document info\n2. View document\n3. Add content to document\n4. Exit\nEnter your choice (1-4): """)
    if options == "1": file_path = input("Enter the exact file path for your document: ")
    elif options == "2":
        try: 
            #get last modified time of the file
            last_modified = time_manager.update_doc_info(file_path)
            with open(file_path, "r+") as file: 
                content = file.read()
        except: print("That file can't be found")
        else: print(content)
    elif options == "3":