# Application code
import csv
treeFile = "tree.csv"

def get_Tree(content):
    result = {}
    result["x"] = []
    result["y"] = []
    with open(treeFile, newline='') as f:
        reader = csv.reader(f)
        input = content["name"];
        for record in reader:
          if str(record[1]) == str(input):
            result["class"] = record[0]
            result["number"] = record[2]
            result["value"] = record[3] 
    with open(treeFile, newline='') as f:
        reader = csv.reader(f)
        for temp in reader:
          if "class" in result and temp[0] == result["class"]:  
            result["x"].append(temp[2])
            result["y"].append(temp[3])
        print(result)    
    return result


