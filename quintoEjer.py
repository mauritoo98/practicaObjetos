# un banco tiene tres clientes que pueden hacer depositos y extracciones se requiere
# que el banco calcule al finalizar el dia la cantidad de dinero que hay depositado y tambien
# que posee cada cliente

class Banco:

    def __init__(self):
        self.cliente=[]
        self.comienzo=0
        self.nombreCliente=input("Ingrese el nombre del cliente: ")
        self.cliente.append(self.nombreCliente)
        self.cliente.append(self.comienzo)

    def ingreso(usuario, ingreso):
        usuario[1]=usuario[1]+ingreso
        print(f"el usuario {usuario[0]} tiene ${usuario[1]}")
        
    def retiro(usuario, retiro):
        if usuario[1]<=retiro:
            print("No tiene la cantidad suficiente para retirar")
        else:
            usuario[1]=usuario[1]-retiro
            print(f"el usuario {usuario[0]} tiene ${usuario[1]}")


def opciones():
    count=0
    listaClientes=[]
    while count<3:
        count=count+1
        miBanco= Banco()           
        listaClientes.append(miBanco.cliente)

    for cliente in listaClientes:
        print(f"Los clientes son {cliente[0]}")
    opcion=input("Escriba el nombre del cliente: ")
    for cliente in listaClientes:
        while cliente[0]==opcion:
            print(f"Usted selecciono el cliente {cliente[0]}")
            sigue=int(input("Si desea continuar ingrese 1, 2 para otro cliente: "))
            while sigue==1:
                opcion2=int(input("ingrese 1 para ingresar dinero, 2 para retirar, 3 para salir: "))
                if opcion2==1:
                    dinero=int(input("Ingrese la cantidad de dinero a ingresar: "))
                    Banco.ingreso(cliente, dinero)
                elif opcion2==2:
                    dinero=int(input("Ingrese la cantidad de dinero a retirar: "))
                    Banco.retiro(cliente, dinero)
                else:
                    sigue=int(input("Si desea continuar ingrese 1, 2 para otro cliente: "))

opciones()