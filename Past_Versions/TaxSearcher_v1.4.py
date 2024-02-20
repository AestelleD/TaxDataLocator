import json
import tkinter as tk
window = tk.Tk()
window.title("Tax Search v1.0")
window.columnconfigure([0], minsize=250)
window.rowconfigure([0,2], minsize=100)
filename=("TaxData.json") #Load the file
filename = open(filename)
file_data = json.load(filename)
var = tk.StringVar()


f2 = tk.Frame(window, padx=5,pady=5)
f2.grid(row=0,column=0)
f1 = tk.Frame(f2)
f1.grid(row=1,column=1,)

def get_search():
     textbox.delete("1.0", tk.END)
     count = 1
     s_term = search_term.get()
     s_type = str(var.get())
     for i in file_data["Tax_Data"]:
          if s_term in (i[s_type]):
               textbox.insert(("1.0"), (str(i)+"\n"))
               textbox.grid(row=2,column=0)


title = tk.Label(f2, text="Geauga County Historic Tax Locator",font=(25))
title.grid(row=0,column=0)
how_to = tk.Label(f2,text="How to use:\n\
1. Enter your search term in the box below\n\
2. Click on the type of search you would like to preform\n\
3. Click Search\n\
4. If you want to search something else, just change your inputs,\
 \nand then click Search again.\n\
",justify="left",relief = tk.RIDGE)
how_to.grid(row=1,column=0,)
search_term = tk.Entry(f2)
search_term.grid(row=2,column=0)
button = tk.Button(
     f1,
     text = "Search!",
     width = 6,
     height = 1,
     command = get_search,
     relief = tk.RIDGE,
     )

R1 = tk.Radiobutton(f1,text="Name", variable=var, value="Name")
R2 = tk.Radiobutton(f1,text="Year", variable=var, value="Year")
R3 = tk.Radiobutton(f1,text="Book", variable=var, value="Book")
R4 = tk.Radiobutton(f1,text="Page", variable=var, value="Page")
R5 = tk.Radiobutton(f1,text="Building Type", variable=var, value="Building")
R1.grid(row=0,column=1)
R2.grid(row=1,column=1)
R3.grid(row=2,column=1)
R4.grid(row=3,column=1)
R5.grid(row=4,column=1)
button.grid(row=5,column=1)
textbox = tk.Text()
textbox.grid(row=2,column=0)


