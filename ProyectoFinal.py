#El archivo .xml esta fuera de la carpeta ProyectoFinalProgra3
import cv2, serial, time

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 30)
ser = serial.Serial('COM4', 9600)

while True:
    _, img = cap.read()
    if not _:
        print("Error al leer la imagen de la cámara.")
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    if len(faces) > 0:
        time.sleep(2)
        ser.write(b'1')  # Enviar comando '1' si se detecta un rostro
        print("Comando enviado: 1")
    else:
        time.sleep(2)
        ser.write(b'0')  # Enviar comando '0' si no se detecta ningún rostro
        print("Comando enviado: 0")

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('Proyecto Final', img)

    teclaEsc = cv2.waitKey(30)
    if teclaEsc == 27:  # Presionar la tecla 'Esc' para salir
        break

cap.release()
cv2.destroyAllWindows()