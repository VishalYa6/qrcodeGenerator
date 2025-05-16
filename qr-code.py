import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk

def generate_qr_code():
    data = entry.get()
    if data:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save("qrcode.png")

        # Display the QR code in the UI
        img = Image.open("qrcode.png")
        # Using Resampling.LANCZOS instead of ANTIALIAS
        img = img.resize((200, 200), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(img)

        qr_label.config(image=img)
        qr_label.image = img

        messagebox.showinfo("Success", "QR code generated and saved as qrcode.png")
    else:
        messagebox.showwarning("Input error", "Please enter data to generate QR code")

# Create the main window
root = tk.Tk()
root.title("QR Code Generator")

# Create and place the widgets
label = tk.Label(root, text="Enter data to encode in QR code:")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr_code)
generate_button.pack(pady=10)

qr_label = tk.Label(root)
qr_label.pack(pady=10)

# Run the application
root.mainloop()