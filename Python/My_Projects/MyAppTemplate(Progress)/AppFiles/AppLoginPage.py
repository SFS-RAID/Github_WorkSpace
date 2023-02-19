import customtkinter as tin
# import tkinter as ogtin
# import LoginSystem_copy

tin.set_appearance_mode('dark')
tin.set_default_color_theme('dark-blue')
main = tin.CTk()
main.geometry('500x350')

def login(us, pwd):
    print('Successful Login')

frame = tin.CTkFrame(master=main)
frame.pack(pady=20, padx=60, fill='both', expand=True)

label = tin.CTkLabel(master=frame, text='Login System', font=('Roboto', 24))
label.pack(pady=12, padx=10)

entry1 = tin.CTkEntry(master=frame, placeholder_text='Username')
entry1.pack(pady=12, padx=10)
entry2 = tin.CTkEntry(master=frame, placeholder_text='Password', show='*')
entry2.pack(pady=12, padx=10)

button = tin.CTkButton(master=frame, text='Login', command=lambda: login('admin', '1234'))
button.pack(pady=12, padx=10)

checkbox = tin.CTkCheckBox(master=frame, text='Remember Me')
checkbox.pack(pady=12, padx=10)

main.mainloop()