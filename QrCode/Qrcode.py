import qrcode
import qrcode.constants
def generate_qr_code(text, file_name):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="white", back_color="black")
    img.save(file_name)
text = "https://www.instagram.com/reel/C4J-jBMLKnk/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA=="
file_name = "qr_code.png"
generate_qr_code(text, file_name)
print(f"QR code saved as {file_name}")