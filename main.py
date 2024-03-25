import customtkinter

l = []

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")

# Function to be executed when the button is pressed
def button_function():
    text = input_field.get("0.0", "end")
    print(text)
    print(l)

def checkbox_event(i):
    if i not in l:
        l.append(i)
    else:
        l.remove(i)

# Label for input field
input_label = customtkinter.CTkLabel(master=app, text="Input URL")
input_label.place(relx=0.1, rely=0.1)

# Input field
input_field = customtkinter.CTkTextbox(master=app, height=20, width=200)
input_field.place(relx=0.3, rely=0.1)

# Checkboxes
checkboxes = []
for i in range(4):
    checkbox = customtkinter.CTkCheckBox(master=app, text=f"Checkbox {i+1}", command=lambda i=i: checkbox_event(i+1))
    checkbox.place(relx=0.1, rely=0.3 + i*0.1)
    checkboxes.append(checkbox)

for i in range(4):
    checkbox = customtkinter.CTkCheckBox(master=app, text=f"Checkbox {i+5}", command=lambda i=i: checkbox_event(i+5))
    checkbox.place(relx=0.6, rely=0.3 + i*0.1)
    checkboxes.append(checkbox)
 
# Submit button
button = customtkinter.CTkButton(master=app, text="Submit", command=button_function)
button.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)

app.mainloop()
