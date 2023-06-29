import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def send_mail():
    recipient = recipient_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", tk.END)

    # Code to send the email

    messagebox.showinfo("Success", "Email sent!")

# Create the main window
window = tk.Tk()
window.title("Mail Application")

# Set the background color
window.configure(bg="lightblue")

# Add the logo
logo_image = Image.open("download.jpg")
logo_image = logo_image.resize((25, 25), Image.ANTIALIAS)  # Adjust the size as per your requirements
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(window, image=logo_photo, bg="lightblue")
logo_label.pack(pady=10)

# Create a frame for the input fields
frame = tk.Frame(window, relief=tk.RAISED, borderwidth=2, bg="white")
frame.pack(pady=10)

# Create the labels and entry fields
recipient_label = tk.Label(frame, text="Recipient:", bg="white")
recipient_label.grid(row=0, column=0, sticky="e", padx=5, pady=5)
recipient_entry = tk.Entry(frame, relief=tk.SUNKEN, borderwidth=2)
recipient_entry.grid(row=0, column=1, padx=5, pady=5)

subject_label = tk.Label(frame, text="Subject:", bg="white")
subject_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)
subject_entry = tk.Entry(frame, relief=tk.SUNKEN, borderwidth=2)
subject_entry.grid(row=1, column=1, padx=5, pady=5)

message_label = tk.Label(frame, text="Message:", bg="white")
message_label.grid(row=2, column=0, sticky="ne", padx=5, pady=5)
message_text = tk.Text(frame, height=10, width=30, relief=tk.SUNKEN, borderwidth=2)
message_text.grid(row=2, column=1, padx=5, pady=5)

send_button = tk.Button(window, text="Send", command=send_mail, relief=tk.RAISED, borderwidth=2)
send_button.pack(pady=10)

# Start the main event loop
window.mainloop()
