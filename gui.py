import tkinter as tk

class App():
    def __init__(self, root):
        # Login Frame
        self.root = root
        self.root.title("Web Automation GUI")

        login_frame = tk.Frame(self.root)
        login_frame.pack(padx=10, pady=10)

        tk.Label(login_frame, text="Username").grid(row=0, column=0, sticky="w")
        self.entry_username = tk.Entry(login_frame)
        self.entry_username.grid(row=0, column=1, sticky="e")

        tk.Label(login_frame, text="Password").grid(row=1, column=0, sticky="w")
        self.entry_password = tk.Entry(login_frame)
        self.entry_password.grid(row=1, column=1, sticky="e")

        # Form submission Frame
        form_frame = tk.Frame(self.root)
        form_frame.pack(padx=10, pady=10)

        tk.Label(form_frame, text="Full Name").grid(row=0, column=0, sticky="w")
        self.entry_full_name = tk.Entry(form_frame)
        self.entry_full_name.grid(row=0, column=1, sticky="e")

        tk.Label(form_frame, text="Email").grid(row=1, column=0, sticky="w")
        self.entry_email = tk.Entry(form_frame)
        self.entry_email.grid(row=1, column=1, sticky="e")

        tk.Label(form_frame, text="Current Address").grid(row=2, column=0, sticky="w")
        self.current_address = tk.Entry(form_frame)
        self.current_address.grid(row=2, column=1, sticky="e")

        tk.Label(form_frame, text="Permanent Address").grid(row=3, column=0, sticky="w")
        self.permanent_address = tk.Entry(form_frame)
        self.permanent_address.grid(row=3, column=1, sticky="e")

        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(padx=5, pady=5)

        tk.Button(button_frame, text="Submit", command=self.submit_data).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Close", command=self.close_browser).grid(row=0, column=1, padx=5)

    def submit_data(self):
        pass
    def close_browser(self):
        pass

root = tk.Tk()
app = App(root)
root.mainloop()
