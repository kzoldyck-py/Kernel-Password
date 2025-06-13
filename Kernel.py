import os
import random
import string
import time
from tkinter import filedialog, Tk
from colorama import init, Fore, Style

# Inicializar colorama para colores en la terminal
init()

def banner():
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.RED + r"""
  _  __                    _   ____                                     _ 
 | |/ /___ _ __ _ __   ___| | |  _ \ __ _ ___ _____      _____  _ __ __| |
 | ' // _ \ '__| '_ \ / _ \ | | |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` |
 | . \  __/ |  | | | |  __/ | |  __/ (_| \__ \__ \\ V  V / (_) | | | (_| |
 |_|\_\___|_|  |_| |_|\___|_| |_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|
                                                                          
                                                                          
    """ + Style.RESET_ALL)
    print(Fore.CYAN + "                   GENERADOR DE CONTRASEÑAS SEGURAS - KERNEL PASSWORD" + Style.RESET_ALL)
    print("-" * 80)

def generar_contraseña(longitud=12, mayusculas=True, numeros=True, simbolos=True):
    caracteres = string.ascii_lowercase
    if mayusculas:
        caracteres += string.ascii_uppercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation

    return ''.join(random.choice(caracteres) for _ in range(longitud))

def guardar_contraseña(nombre, contraseña):
    root = Tk()
    root.withdraw()  # Ocultar la ventana principal de Tkinter
    ruta = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Archivos de texto", "*.txt")],
        title="Guardar contraseña como..."
    )
    if ruta:
        with open(ruta, "w") as archivo:
            archivo.write(f"Nombre: {nombre}\nContraseña: {contraseña}")
        print(Fore.GREEN + f"\n[✔] Contraseña guardada exitosamente en:\n{ruta}" + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + "\n[!] No se guardó ningún archivo." + Style.RESET_ALL)

def main():
    banner()
    try:
        nombre = input(Fore.CYAN + "[?] ¿Para qué es esta contraseña?: " + Style.RESET_ALL).strip()
        longitud = int(input(Fore.CYAN + "[?] Longitud (12-32): " + Style.RESET_ALL))
        if longitud < 12 or longitud > 32:
            print(Fore.RED + "[!] La longitud debe estar entre 12 y 32." + Style.RESET_ALL)
            return

        mayusculas = input(Fore.CYAN + "[?] ¿Incluir mayúsculas? (S/n): " + Style.RESET_ALL).lower() != 'n'
        numeros = input(Fore.CYAN + "[?] ¿Incluir números? (S/n): " + Style.RESET_ALL).lower() != 'n'
        simbolos = input(Fore.CYAN + "[?] ¿Incluir símbolos? (S/n): " + Style.RESET_ALL).lower() != 'n'

        print(Fore.YELLOW + "\n[+] Generando contraseña..." + Style.RESET_ALL)
        time.sleep(1)

        contraseña = generar_contraseña(longitud, mayusculas, numeros, simbolos)

        print(Fore.GREEN + "\n[✔] CONTRASEÑA GENERADA:" + Style.RESET_ALL)
        print(Fore.LIGHTMAGENTA_EX + contraseña + Style.RESET_ALL)

        guardar_contraseña(nombre, contraseña)

    except ValueError:
        print(Fore.RED + "[!] Error: ingresa un número válido." + Style.RESET_ALL)
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Operación cancelada por el usuario." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
