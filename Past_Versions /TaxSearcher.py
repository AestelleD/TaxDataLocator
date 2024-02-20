import json
import tkinter as tk
window = tk.Tk()
window.title("Tax Search v1.0")

filename=("TaxData.json") #Load the file
filename = open(filename)
file_data = json.load(filename)
var = tk.StringVar()

def get_search():
     textbox.delete("1.0", tk.END)
     count = 1
     s_term = search_term.get()
     s_type = str(var.get())
     for i in file_data["Tax_Data"]:
          if s_term in (i[s_type]):
               textbox.insert(("1.0"), (str(i)+"\n"))
               textbox.pack()



how_to = tk.Label(text="How to use:\n\
1. Enter your search term in the box below\n\
2. Click on the type of search you would like to preform\n\
3. Click Search\n\
4. If you want to search something else, just change your inputs,\
 and then click Search again.\n\
")
how_to.pack()

label = tk.Label(text="Type Search term")
search_term = tk.Entry()
label.pack(padx=5, pady=5)
search_term.pack(padx=5, pady=5)
button = tk.Button(
     text = "Search!",
     width = 6,
     height = 1,
     command = get_search,
     relief = tk.RIDGE,
     )

R1 = tk.Radiobutton(text="Name", variable=var, value="Name")
R1.pack()
R2 = tk.Radiobutton(text="Year", variable=var, value="Year")
R2.pack()
R3 = tk.Radiobutton(text="Book", variable=var, value="Book")
R3.pack()
R4 = tk.Radiobutton(text="Page", variable=var, value="Page")
R4.pack()
R5 = tk.Radiobutton(text="Building Type", variable=var, value="Building")
R5.pack()
button.pack(padx=5, pady=5)
textbox = tk.Text()
textbox.pack()


