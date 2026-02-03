#Import nesssary libraries
import csv, msvcrt
#Import csv file and sepperate it in a dictionary
try: 
    with open("idividual_projects\Movie_Recommend\Movies list.csv", mode="r") as csv_file: 
        content = csv.reader(csv_file)
        headers = next(content)
        rows = []
        for line in content: rows.append({headers[0]: line[0], headers[1]: line[1]})
except: print("Can't find CSV")
else: 
    print(rows)
#Make function that detects different sections in dictionary that searches for the specific or general item. 
#Display the results by calling search function