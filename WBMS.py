import customtkinter as ctk
import threading
import time
import pywhatkit as kit
import pyautogui as key
from tkinter import filedialog, messagebox
from PIL import Image

# Set the appearance mode and color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class WhatsAppBulkMessenger(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("WhatsApp Bulk Messenger")
        self.geometry("850x650")
        
        # Initialize variables
        self.country_codes = ["+91", "+1", "+44", "+61"]  # Example list of country codes
        self.selected_country_code = self.country_codes[0]
        self.phone_numbers_file = ctk.StringVar()
        self.photo_path = ctk.StringVar()
        self.message_file = ctk.StringVar()
        self.sent_count = ctk.IntVar()

        # Main frame
        main_frame = ctk.CTkFrame(self, corner_radius=15)
        main_frame.grid(padx=20, pady=20, sticky="nsew")
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Title
        ctk.CTkLabel(main_frame, text="WhatsApp Bulk Messenger", font=("Helvetica", 20, "bold")).grid(row=0, column=1, pady=10, padx=10)

        # Country code selection
        ctk.CTkLabel(main_frame, text="Select Country Code:", font=("Helvetica", 12, "bold")).grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.country_code_menu = ctk.CTkOptionMenu(main_frame, values=self.country_codes)
        self.country_code_menu.set(self.selected_country_code)
        self.country_code_menu.grid(row=1, column=1, padx=10, pady=10)

        # Phone numbers file
        ctk.CTkLabel(main_frame, text="Select Phone Numbers File:", font=("Helvetica", 12, "bold")).grid(row=2, column=0, padx=10, pady=10, sticky="w")
        ctk.CTkEntry(main_frame, textvariable=self.phone_numbers_file, width=400).grid(row=2, column=1, padx=10, pady=10)
        ctk.CTkButton(main_frame, text="Browse", command=self.browse_phone_numbers_file).grid(row=2, column=2, padx=10, pady=10)

        # Photo path (optional)
        ctk.CTkLabel(main_frame, text="Select Photo Path (optional):", font=("Helvetica", 12, "bold")).grid(row=3, column=0, padx=10, pady=10, sticky="w")
        ctk.CTkEntry(main_frame, textvariable=self.photo_path, width=400).grid(row=3, column=1, padx=10, pady=10)
        ctk.CTkButton(main_frame, text="Browse", command=self.browse_photo).grid(row=3, column=2, padx=10, pady=10)

        # Message file (optional)
        ctk.CTkLabel(main_frame, text="Select Message File (optional):", font=("Helvetica", 12, "bold")).grid(row=4, column=0, padx=10, pady=10, sticky="w")
        ctk.CTkEntry(main_frame, textvariable=self.message_file, width=400).grid(row=4, column=1, padx=10, pady=10)
        ctk.CTkButton(main_frame, text="Browse", command=self.browse_message_file).grid(row=4, column=2, padx=10, pady=10)

        # Enter message
        ctk.CTkLabel(main_frame, text="Enter Message:", font=("Helvetica", 12, "bold")).grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.message = ctk.CTkTextbox(main_frame, height=200, width=600)
        self.message.grid(row=5, column=1, columnspan=2, padx=10, pady=10)

        # Send and Exit buttons
        ctk.CTkButton(main_frame, text="Send", command=self.start_sending_messages).grid(row=6, column=1, padx=10, pady=10)
        ctk.CTkButton(main_frame, text="Exit", command=self.exit_program).grid(row=6, column=2, padx=10, pady=10)

        # Sent count
        ctk.CTkLabel(main_frame, text="Sent Count:", font=("Helvetica", 12, "bold")).grid(row=7, column=0, padx=10, pady=10, sticky="w")
        self.count_label = ctk.CTkLabel(main_frame, textvariable=self.sent_count)
        self.count_label.grid(row=7, column=1, padx=10, pady=10, sticky="w")

        # Log
        ctk.CTkLabel(main_frame, text="Log:", font=("Helvetica", 12, "bold")).grid(row=8, column=0, padx=10, pady=10, sticky="w")
        self.log = ctk.CTkTextbox(main_frame, height=200, width=600)
        self.log.grid(row=8, column=1, columnspan=2, padx=10, pady=10, sticky="w")

        # Trace changes to the message_file variable
        self.message_file.trace_add('write', self.on_message_file_change)

    def on_message_file_change(self, *args):
        if self.message_file.get():
            self.message.configure(state="disabled")
        else:
            self.message.configure(state="normal")

    def browse_phone_numbers_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        self.phone_numbers_file.set(file_path)

    def browse_photo(self):
        photo_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        self.photo_path.set(photo_path)

    def browse_message_file(self):
        message_file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        self.message_file.set(message_file_path)

    def read_phone_numbers(self, file_path):
        try:
            with open(file_path, 'r') as file:
                country_code = self.country_code_menu.get()
                phone_numbers = [country_code + line.strip() for line in file.readlines() if line.strip()]
            return phone_numbers
        except Exception as e:
            self.log_message(f"Failed to read phone numbers: {e}")
            return []

    def read_message_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                message = file.read()
            return message
        except Exception as e:
            self.log_message(f"Failed to read message file: {e}")
            return ""

    def send_photo(self, phone, photo_path, message):
        try:
            if photo_path:
                kit.sendwhats_image(phone, photo_path, message, 15)
            else:
                kit.sendwhatmsg_instantly(phone, message)
            self.log_message(f"Message sent to {phone}")
            self.sent_count.set(self.sent_count.get() + 1)
            time.sleep(5)  # To give time for the message to be sent
            key.press("enter")
            time.sleep(5)
            key.hotkey('ctrl', 'w')
        except Exception as e:
            self.log_message(f"Failed to send message to {phone}: {e}")

    def send_bulk_message(self):
        phone_numbers_file = self.phone_numbers_file.get()
        photo_path = self.photo_path.get()
        message = self.message.get("1.0", "end").strip()

        if self.message_file.get():
            message = self.read_message_from_file(self.message_file.get())

        if not phone_numbers_file or not message:
            messagebox.showerror("Error", "Please fill in all fields except photo path (optional).")
            return

        phone_numbers = self.read_phone_numbers(phone_numbers_file)
        if not phone_numbers:
            messagebox.showerror("Error", "No valid phone numbers found.")
            return

        for phone in phone_numbers:
            self.send_photo(phone, photo_path, message)
            phone_numbers.remove(phone)
            if not phone_numbers:
                self.log_message("All messages sent.")
                break

    def start_sending_messages(self):
        threading.Thread(target=self.send_bulk_message).start()

    def log_message(self, message):
        self.log.configure(state="normal")
        self.log.insert("end", message + "\n")
        self.log.configure(state="disabled")
        self.log.see("end")

    def exit_program(self):
        self.destroy()

if __name__ == "__main__":
    app = WhatsAppBulkMessenger()
    app.mainloop()
