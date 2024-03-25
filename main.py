import customtkinter

l = []

customtkinter.set_appearance_mode("System") 

customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk() 

app.geometry("800x360")

def button_function():
    text = input_field.get("0.0", "end")
    print(text)
    print([attacks[j] for j in l])

def checkbox_event(i):
    if i not in l:
        l.append(i)
    else:
        l.remove(i)


input_label = customtkinter.CTkLabel(master=app, text="Input URL",font=("Arial", 20))

input_label.place(relx=0.1, rely=0.1)


input_field = customtkinter.CTkTextbox(master=app, height=20, width=400,font=("Arial", 20))

input_field.place(relx=0.3, rely=0.1)

#attacks
attacks=["subdomain enumeration","email discovery","google dorking","password cracking","open ports and vuln","subdirectory enumeration"]

checkboxes = []

for i in range(3):
    checkbox = customtkinter.CTkCheckBox(master=app, text=attacks[i], command=lambda i=i: checkbox_event(i+1),font=("Arial", 20))
    checkbox.place(relx=0.1, rely=0.3 + i*0.1)
    checkboxes.append(checkbox)

for i in range(3):
    checkbox = customtkinter.CTkCheckBox(master=app, text=attacks[i+3], command=lambda i=i: checkbox_event(i+3),font=("Arial", 20))
    checkbox.place(relx=0.6, rely=0.3 + i*0.1)
    checkboxes.append(checkbox)




button = customtkinter.CTkButton(master=app, text="Start", command=button_function,font=("Arial", 20))

button.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)



app.mainloop()