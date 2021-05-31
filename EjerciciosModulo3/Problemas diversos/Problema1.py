def lista_alumnos(num_alumnos):
    alumnos=[]
    for n in range(num_alumnos):
        alumno = {}
        
        alumno['Nombre'] = input('Digite el nombre completo del alumno : ')
        alumno['Nota1'] = float(input('Digite nota 1 : '))
        alumno['Nota2'] = float(input('Digite nota 2 : '))
        alumno['Nota3'] = float(input('Digite nota 3 : '))
        
        alumnos.append(alumno)
    return alumnos

num_alumnos = int(input('Escriba la cantidad de alumnos : '))
list_alumnos = lista_alumnos(num_alumnos)
print(list_alumnos)



