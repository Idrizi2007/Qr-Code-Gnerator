QR Code Generator
This script generates a QR code for a given text and saves it as an image file.

Requirements
Make sure you have the qrcode library installed. You can install it using pip:

bash
Copy code
pip install qrcode[pil]
Usage
Edit the Script:

Set the text variable to the content you want to encode in the QR code.
Set the file_name variable to the desired name for the output image file (e.g., qr_code.png).
Run the Script: Execute the script using Python. It will generate a QR code image and save it with the specified file name.

bash
Copy code
python your_script_name.py
Check the Output: The QR code image will be saved in the same directory as the script, with the name specified in the file_name variable.
Example
If you set text to "Hello, World!" and file_name to "hello_world.png", running the script will create a QR code with the content "Hello, World!" and save it as hello_world.png.

Notes
The QR code is generated with a default version and error correction level. You can adjust these parameters in the generate_qr_code function if needed.
The QR code image will have a white foreground and a black background by default. You can customize these colors in the make_image method.
Feel free to adjust the content to better fit your specific needs!
