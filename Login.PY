Contraseña="123"
intentos=0
Correcto=False

while intentos<=2:
    ContIngresada=(input("Introduzca la contraseña: "))
    if ContIngresada==Contraseña:
        print("bienvenido")
        Correcto=True
        break
    elif intentos==2:
        print("Haz rebasado la cantidad maxima de intentos")
        break
    else:
        intentos+=1

if Correcto:
    intentosOp=0
    while intentosOp<=2:
        num1=float(input("Ingrese el primer valor: "))
        num2=float(input("Ingrese el segundo numero: "))
        op1=input("Ingrese la operacion (suma, resta, multiplicacion, division): ")
        op2=op1.upper()
        Sum=num1+num2
        Res=num1-num2
        Mul=num1*num2
        Div=num1/num2
        if op2=="SUMA":
            print(f"El resultado de la suma es: {Sum}")
            break
        elif op2=="RESTA":
            print(f"El resultado de la resta es: {Res}")
            break
        elif op2=="MULTIPLICACION":
            print(f"El resultado de la multiplicacion es: {Mul}")
            break
        elif op2=="DIVISION":
            print(f"El resultado de la division es: {Div}")
            break
        elif intentosOp==2:
            print("Haz cometido muchos errores")
            break
        else:
            print("Error, operacion no encontrada")
            intentosOp+=1

print("Fin del Programa")