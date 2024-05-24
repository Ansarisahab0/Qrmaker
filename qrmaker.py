import tkinter as tk
from tkinter import filedialog
import qrcode
from PIL import Image, ImageTk

def generate_qr():
    # Get the text from the entry widget
    data = entry.get()
    
    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Display the QR code in the Tkinter window
    img = img.resize((200, 200), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    qr_label.config(image=img)
    qr_label.image = img

def save_qr():
    # Get the text from the entry widget
    data = entry.get()
    
    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Ask the user for a file location to save the QR code
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    
    if file_path:
        img.save(file_path)

# Create the main window
root = tk.Tk()
root.title("QR Code Generator")

# Create and place the widgets
entry_label = tk.Label(root, text="Enter text or URL:")
entry_label.pack(pady=5)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=5)

save_button = tk.Button(root, text="Save QR Code", command=save_qr)
save_button.pack(pady=5)

qr_label = tk.Label(root)
qr_label.pack(pady=5)

# Run the application
root.mainloop()
