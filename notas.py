alumnos = [
    {"nombre": "Ana", "nota": 8.5},
    {"nombre": "Luis", "nota": 4.0},
    {"nombre": "Marta", "nota": 7.0},
    {"nombre": "Pablo", "nota": 3.5},
    {"nombre": "Sara", "nota": 9.0},
]
i=0
aprobados=0
suspendidos=0
media=0
for alumno in alumnos:
    print(alumno["nombre"].upper())
    print(alumno["nota"])
    if alumno["nota"]>=5:
        print("Aprobado")
        aprobados+=1
    else:
        print("Suspendido")
        suspendidos+=1
    media=media+alumno["nota"] 
media=round(media/len(alumnos),2)           
print(f"Hay {len(alumnos)} alumnos en total")
print(f"Hay {aprobados} aprobados y {suspendidos} suspendidos")
print(f"La media es: {media}")