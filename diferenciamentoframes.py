import cv2

video = cv2.VideoCapture(0)
ret,img = video.read()
proximo_img = img

while True:
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    proximo_img_gray = cv2.cvtColor(proximo_img, cv2.COLOR_BGR2GRAY)

    img_sub = cv2.absdiff(img_gray, proximo_img_gray)

    cv2.imshow("Diferenciamento de frames", img_sub)

    if cv2.waitKey(2) == 32:
        break

    proximo_img = img.copy()
    ret,img = video.read()

video.realase()
cv2.destroyAllWindows()
    
