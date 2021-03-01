def ingresar_nota():

    try:
        nota = float(input("Introduce la nota(0 - 10): "))
        
        if nota >=0 and nota <= 10:
            return nota  # Importante romper la iteración si todo ha salido bien
        else:
            print('nota fuera del rango')
            ingresar_nota()
    except:
        print("Ha ocurrido un error, introduce bien la nota")
        ingresar_nota()