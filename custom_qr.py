#--------------------------------------------------------------------\
#--------------------------------------------------------------------\
#Import cac thu vien can su dung
from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import cv2
import pygame
#--------------------------------------------------------------------\
#--------------------------------------------------------------------\

# Xay dung trinh phan tich cu phap doi so va phan tich cac doi so
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", type=str, default="output.csv",)  #Tep luu du lieu output
args = vars(ap.parse_args())
#--------------------------------------------------------------------\
#--------------------------------------------------------------------\
# Bat dau Steam va cho phep trich xuat hinh anh tu webcame
print("[INFO] Chuong trinh dang chay! Cac output cua ban duoc in ra file output.csv")
vs = VideoStream(src=0).start()
# vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)
csv = open(args["output"], "w")
found = set()
#--------------------------------------------------------------------\
#--------------------------------------------------------------------\
# Cu phap vong lap xu ly cac frame anh khi dang steam!
while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=400)

    barcodes = pyzbar.decode(frame)

    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        text = "{}".format(barcodeData)
        cv2.putText(frame, '', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        if barcodeData not in found:

            csv.write("{}\n".format(barcodeData))
            csv.flush()

            found.clear()
            found.add(barcodeData)

    cv2.imshow("Scan QR code <test>", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break
#--------------------------------------------------------------------\
#--------------------------------------------------------------------\
#Ket thuc chuong trinh
print("[INFO] Chuong trinh ket thuc! Toan bo output cua ban da duoc luu vao file output.csv!")
csv.close()
cv2.destroyAllWindows()
vs.stop()
#--------------------------------------------------------------------\