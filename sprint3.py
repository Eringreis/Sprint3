import random
import string

# Elaborar un programa que recorra una lista con los nombres de 10 de sus futuros usuarios
username_list = ['Ana','Erin','leia','Roberto','Julio','Dario','Luis','Pedro','Jose','Momo']

# Mediante una función, a todos los usuarios se les creará una cuenta automáticamente.
def create_account(name):
    phone = check_phone(input("Hola " + name + " Favor indicanos tu numero, (8 dígitos numéricos)"))
    return dict(name=name, password=create_password(), phone=phone)

#El programa debe verificar que el número telefónico tenga 8 dígitos numéricos.
def check_phone(input_phone):
    try:
        # Convert it into integer
        phone = int(input_phone)
        phone_str = str(phone)
        print("Input is an integer number. Number = ", phone)
        if len(phone_str) == 8:
            return phone_str
        else:
            return check_phone(input("(8 dígitos numéricos)"))
    except ValueError:
        return check_phone(input("(8 dígitos numéricos)"))

# Asigne una contraseña para cada cuenta.
def create_password(size=8, chars=string.ascii_letters + string.digits):
    return''.join(random.choice(chars) for _ in range(size))
 
def run():
    user_list = {}
    for username in username_list:
        user_list[username] = create_account(username)
    print(user_list)


run()
