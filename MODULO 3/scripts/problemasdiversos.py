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
def listar_alumnos(cantidad_alumnos):
    lista_alumnos = []
    for i in range(cantidad_alumnos):
        alumno = {}
        # Ingreso de nombre de alumno
        alumno['nombre'] = input('Ingrese el nombre del alumno {}: '.format(i+1))
    
        # ingreso de notas
        alumno['nota1'] = ingresar_nota()
        alumno['nota2'] = ingresar_nota()
        alumno['nota3'] = ingresar_nota()
    
        # agregando alumno a lista alumnos
        lista_alumnos.append(alumno)
    
    return lista_alumnos
n = int(input('Cantidad de alumnos a ingresar: '))
n

lista_alumnos = listar_alumnos(n)
lista_alumnos