nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuál es tu edad? "))

if edad < 18:
    print(f"Hola, {nombre}, eres menor de edad.")
else:
    print(f"Hola, {nombre}, eres mayor de edad.")

print(f"¿Tu edad es igual a 18? {edad == 18}")
print(f"¿Tu edad es diferente de 18? {edad != 18}")