class Socio:
    def __init__(self):
        self.socio=[]
        self.nombre=input("Ingrese el nombre: ")
        self.antiguedad=int(input("Ingrese la antiguedad en años: "))
        self.socio.append(self.nombre)
        self.socio.append(self.antiguedad)

    
class Club:
    count=0
    def __init__(self):
        self.socios=[]
        while len(self.socios)<3:
            listSocios=Socio()
            self.socios.append(listSocios)
            self.count=self.count+1

miClub= Club()


antiguo=0
nombre=""
for socio in miClub.socios:
    if socio.socio[1]>antiguo:
        nombre=socio.socio[0]
        antiguo=socio.socio[1]
    else:
        continue

print(f"El socio mas antiguo es {nombre} con {antiguo} años")