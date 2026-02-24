#Import Libraries
import time_manager, word_counter
#Open txt file
def run():
    while True: 
        #Get file path from user
        options = input("""--- Document Word Count Updater ---\n1. Update document info\n2. View document\n3. Add content to document\n4. Exit\nEnter your choice (1-4): """)#Get file path from user
        if options == "1": file_path = input("Enter the exact file path for your document: ")#Get access to the file
        elif options == "2":#Edit document and update last modified time and word count
            try: 
                #get last modified time of the file
                last_modified = time_manager.update_doc_info(file_path)
                with open(file_path, "r+") as file: 
                    content = file.read()
            except: print("That file can't be found")
            else: print(content)
        elif options == "3":
            try:
                # Read existing content
                with open(file_path, 'r') as f:
                    lines = f.readlines()

                # Remove old metadata if present
                if len(lines) >= 2:
                    if lines[-1].startswith("Word Count:") and lines[-2].startswith("Last Updated:"):
                        lines = lines[:-3]  # remove last three metadata lines

                # Write back cleaned content
                with open(file_path, 'w') as f:
                    f.writelines(lines)

                # Add new content with "press Enter twice to end"
                print("Enter the content you want to add. Press Enter twice to finish:")
                new_lines = []
                while True:
                    line = input()
                    if line == "":
                        break
                    new_lines.append(line)

                # Write new content
                with open(file_path, "a") as file:
                    for line in new_lines:
                        file.write(line + "\n")

                # Update metadata after writing new content
                last_modified = time_manager.update_doc_info(file_path)
                word_count = word_counter.word_count(file_path)

                # Append updated metadata
                with open(file_path, "a") as file:
                    file.write(f"\n{last_modified}\n{word_count}\n")

            except:
                print("That file can't be found")

