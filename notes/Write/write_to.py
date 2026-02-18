"""with open("notes/reading.txt", "r+") as file: content = file.read(); content += "/nI wrote on my file!"; file.write(content)
print("code end")

with open("notes/writing.txt", "a") as file: file.write("\nThis is more of my file!")

print("code end")"""

import csv

with open("notes/Write/holder.csv", "r+", newline='') as csvfile:
    fieldnames = ["username", "color"]
    reader = csv.reader(csvfile)
    for line in reader:
        print(f"{fieldnames[0]}: {line[0]}, favorite color: {line[1]}")
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #writer.writeheader()
    writer.writerow({'username': 'aUser', 'color': 'pink'})
    writer.writerow({'username': 'basicPerson', 'color': 'red'})
    writer.writerow({'username': 'anotherUser', 'color': 'green'})
    writer.writerow({'username': 'thirdUser', 'color': 'blue'})
                     
print("code end")