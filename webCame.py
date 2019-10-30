import cv2
#--------------------------------------------------------------------\
#--------------------------------------------------------------------\

#Tao mot ham bat camera laptop va trich xuat hinh anh truc tiep tu Webcam laptop
#Su dung ham VideoCapture cua thu vien Open CV
#--------------------------------------------------------------------\
#--------------------------------------------------------------------\

def show_webcam(mirror=False):
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        if mirror:
            img = cv2.flip(img, 1)
        cv2.imshow('Leitor', img)
        if cv2.waitKey(1) == 27:
            break  # esc to quit
    cv2.destroyAllWindows()

#--------------------------------------------------------------------\
def main():
    show_webcam(mirror=True)

#--------------------------------------------------------------------\
if __name__ == '__main__':
    main()
#--------------------------------------------------------------------\
#--------------------------------------------------------------------\