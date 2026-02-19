while True: 
    file_path = input("Enter the file path: \n>")
    try: 
        with open(file_path, "r+") as file: 
            for line in file: 
                print(f"Hello {line.strip()}")
            content = file.read()
    except: print("That file can't be found")
    else: print(content); break