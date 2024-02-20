import json
import tkinter as tk
window = tk.Tk()
window.title("Tax Search v0.4")
window.geometry("480x360")
#print("What would you like to search by?\n(1)Name\n(2)Year")
#search_method = int(input("Type the number of the option you want:"))
filename=("C:/Users/mikuf/Downloads/TaxData/TaxData.json")
filename = open(filename)
file_data = json.load(filename)
count = 0
def get_search():
     textbox.delete("1.0", tk.END)
     count = 1
     s_term = search_term.get()
     for i in file_data["Tax_Data"]:
          if s_term in (i["Name"]):
               textbox.insert(("1.0"), (str(i)+"\n"))
               textbox.pack()

label = tk.Label(text="Type Search Name")
search_term = tk.Entry()
label.pack()
search_term.pack()
button = tk.Button(
     text = "Search!",
     width = 6,
     height = 1,
     command = get_search,
     relief = tk.RIDGE
     )
button.pack()
textbox = tk.Text()
textbox.pack()



#for i in file_data["Tax_Data"]:
 #    if search_term ==(i["Name"]):
  #       print(i)
