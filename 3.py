def validar_password(password):
    if len(password) < 8:
        return False
        
    numeros = 0
    mayusculas = 0
    minusculas = 0
    
    for caracter in password:
        if caracter.isdigit():
            numeros += 1
        elif caracter.isupper():
            mayusculas += 1
        elif caracter.islower():
            minusculas += 1
            
    if numeros >= 2 and mayusculas >= 1 and minusculas >= 1:
        return True
    else:
        return False

clave_usuario = input("para que la contraseña sea valida debe cumplir los siguientes requisitos: minimo 8 caracteres, al menos 2 números, al menos 1 letra mayúscula y al menos 1 letra minúscula. Ingrese su nueva contraseña: ")

if validar_password(clave_usuario):
    print("la contraseña es valida.")
else:
    print("la contraseña no es valida. No cumple con los requisitos de seguridad.")