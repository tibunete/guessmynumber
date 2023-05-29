import random
from pygame import mixer
import game_pc_vs_user

def computer_guess():
    mixer.init()
    mixer.music.load('music.mp3')
    mixer.music.play()

    name = input("Ingresa tu nombre: ")
    x = int(input("Piensa en un número: "))
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(f'¿Es {guess} demasiado alto (H), demasiado bajo (L), o correcto (C)? ').lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    mixer.music.stop()

    print(f'¡Yay! ¡La computadora adivinó tu número, {guess}, correctamente!')

    with open('nombres.txt', 'a') as file:
        file.write(f'Nombre: {name}\n')

    with open('nombres.txt', 'r') as file:
        lines = file.readlines()
        last_five_names = lines[-5:]
        print("\nÚltimos 5 nombres almacenados:")
        for name_line in last_five_names:
            print(name_line.strip())

def adivinar_edad():
    print("\n¡Bienvenido al juego de adivinar la edad!")
    print("Ingresa una edad entre 1 y 100, y trataré de adivinarlo.")
    print("Cuando estés listo, ingresa la edad y presiona ENTER.")
    input()

    limite_inferior = 1
    limite_superior = 100
    intentos = 0

    while True:
        intentos += 1
        if limite_inferior != limite_superior:
            numero_adivinado = random.randint(limite_inferior, limite_superior)
        else:
            numero_adivinado = limite_inferior

        print("¿Tu edad es {}?".format(numero_adivinado))
        respuesta = input("Ingresa 'S' si es correcto, 'M' si tu edad es mayor o 'L' si es menor: ").lower()

        if respuesta == 's':
            print("¡Genial! Adiviné tu edad en {} intentos.".format(intentos))
            break
        elif respuesta == 'm':
            limite_inferior = numero_adivinado + 1
        elif respuesta == 'l':
            limite_superior = numero_adivinado - 1
        else:
            print("Respuesta inválida. Por favor, ingresa 'S', 'M' o 'L'.")



#Ventana de bienvenida al proyeto
import tkinter as tk
from tkinter import messagebox
from tkinter import *

#Ventana emergente
def ask_quit():
    if messagebox.askokcancel("", "El proyecto continuará en la terminal."):
        ventana.destroy()
#Ventana
ventana= tk.Tk()
ventana.geometry("400x400")
ventana.title("Proyecto")
ventana['bg'] = '#3498DB'
#Etiqueta
Label = tk.Label(ventana, text="Bienvenido al proyecto del grupo 372 !", font='Helvetica 15 bold', fg='white')
Label.config(bg="#3498DB")
Label.pack()
Label = tk.Label(ventana, text="Powered by Python", font='Helvetica 11 bold', fg='white')
Label.config(bg="#3498DB")
Label.pack()
#Boton
boton = tk.Button(text="Ir al menú de juegos", bg='#F4D03F' ,fg='black', font='Helvetica 11 bold', command=ask_quit)
boton.place(x=200, y=325)
# Imagen
image2 = tk.PhotoImage(file="logo.png")
label2 = tk.Label(image=image2)
label2.config(bg="#3498DB")
label2.pack()
ventana.mainloop()
#Aqui finaliza la ventana de bienvenido



def menu():
    while True:

        print("\n¡Bienvenido al Menú de Juegos!")
        print("1. Adivinar el número")
        print("2. Adivina la edad")
        print("3. Adivina el número User vs. PC")
        print("4. Salir")
        seleccion = input("Ingresa el número de juego que deseas jugar (1-4): ")


        if seleccion == '1':
            computer_guess()
        elif seleccion == '2':
            adivinar_edad()
        elif seleccion == '3':
            game_pc_vs_user.begin_game()
        elif seleccion == '4':
            print("¡Gracias por jugar!")
            break
        else:
            print("Selección inválida. Por favor, ingresa un número válido.")

menu()
