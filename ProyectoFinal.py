<<<<<<< HEAD
#El archivo .xml esta fuera de la carpeta ProyectoFinalProgra3
import cv2, serial, time #librerias
=======
import cv2
import serial
import time
import tkinter as tk
from PIL import Image, ImageTk
>>>>>>> f7bbe945d64f8b5936bf41ac55b86e143e652855

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
<<<<<<< HEAD
cap.set(cv2.CAP_PROP_FPS, 30)#FPS cuadros por segundo
ser = serial.Serial('COM4', 9600) #puerto serial este puede cambiar depende maquina
=======
cap.set(cv2.CAP_PROP_FPS, 30)
ser = serial.Serial('COM3', 9600)
>>>>>>> f7bbe945d64f8b5936bf41ac55b86e143e652855

def send_command(command):
    ser.write(command.encode())
    print(f"Comando enviado: {command}")

def update_frame():
    _, img = cap.read()
    if not _:
        print("Error al leer la imagen de la cámara.")
        return

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

<<<<<<< HEAD
    if len(faces) > 0:
        time.sleep(2)#pausa en segundos
        ser.write(b'1')  # Enviar comando '1' si se detecta un rostro
        print("Comando enviado: 1")
    else:
        time.sleep(2)
        ser.write(b'0')  # Enviar comando '0' si no se detecta ningún rostro
        print("Comando enviado: 0")

=======
>>>>>>> f7bbe945d64f8b5936bf41ac55b86e143e652855
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(img)
    label.img = img  # Mantener una referencia al objeto PhotoImage
    label.config(image=img)
    label.after(10, update_frame)  # Actualizar la imagen cada 10 milisegundos

<<<<<<< HEAD
    #salir del programa
    teclaEsc = cv2.waitKey(30)
    if teclaEsc == 27:  # Presionar la tecla 'Esc' para salir
        break
=======
root = tk.Tk()
root.title("Reconocimiento Facial")

label = tk.Label(root)
label.pack(padx=10, pady=10)

update_frame() 

# Funciones para enviar comandos
button_1 = tk.Button(root, text="Abrir puerta", bg="green", command=lambda: send_command('1'))
button_1.pack(side=tk.TOP, padx=10, pady=10)

button_0 = tk.Button(root, text="Cerrar puerta", bg="red", command=lambda: send_command('0'))
button_0.pack(side=tk.TOP, padx=10, pady=10)

root.mainloop()
>>>>>>> f7bbe945d64f8b5936bf41ac55b86e143e652855

cap.release()
cv2.destroyAllWindows()
