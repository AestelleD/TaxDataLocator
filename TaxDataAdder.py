import json

def write_json(new_data, filename=("C:/Users/mikuf/Downloads/TaxData/TaxData.json")):
    with open(filename,'r+') as file:
        filename = open(filename)
        file_data = json.load(filename)
        file_data["Tax_Data"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)

filename=("C:/Users/mikuf/Downloads/TaxData/TaxData.json")
while True:
    f = open(filename)
    json_file = json.load(f)
    print(json_file)

    Name = input("Enter Name:")
    Year = input("Enter Year:")
    Book = input("Enter Book:")
    Page = input("Enter Page:")


    new_data = {"Name":Name,
                "Year":Year,
                "Book":Book,
                "Page":Page
                }
    print(new_data)
    write_json(new_data)
                   
