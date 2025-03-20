import qrcode
import cv2

msg = "hello world"
qr = qrcode.QRCode(version=1, box_size=6, border=5)
qr.add_data(msg)
qr.make()

img = qr.make_image(fill_color="green", back_color="white")
file_path = f"{msg}.png"
img.save(file_path)

image = cv2.imread(file_path)
detector = cv2.QRCodeDetector()
data, vertices_array, binary_qrcode = detector.detectAndDecode(image)
if vertices_array is not None:
    print(data)
else:
    print("Data failure")