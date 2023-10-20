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

    
    def agregaCliente():
        count=0
        listaClientes=[]
        while count<3:
            miBanco= Banco() 
            count=count+1          
            listaClientes.append(miBanco.cliente)
        return listaClientes

    def ingreso(usuario, ingreso):
        usuario[1]=usuario[1]+ingreso
        print(f"el usuario {usuario[0]} tiene ${usuario[1]}")
        
    def retiro(usuario, retiro):
        if usuario[1]<=retiro:
            print("No tiene la cantidad suficiente para retirar")
        else:
            usuario[1]=usuario[1]-retiro
            print(f"el usuario {usuario[0]} tiene ${usuario[1]}")

    def buscaCliente(listaCliente, opcion):
        clienteEncontrado=""
        for cliente in listaCliente:
            if cliente[0]==opcion:
                print(f"Usted selecciono el cliente {cliente[0]}")
                clienteEncontrado=cliente
        return clienteEncontrado




def opciones():
    clientes=Banco.agregaCliente()
    opcion=int(input("1 para ingresar dinero, 2 para retirar, enter para salir"))
    nombreCliente= input("Ingrese el nombre del cliente a buscar: ")
    while opcion == 1 or opcion == 2:
        if opcion==1:
            dinero=int(input("Ingrese la cantidad de dinero a ingresar: "))
            Banco.ingreso(Banco.buscaCliente(clientes,nombreCliente), dinero)
            opcion=int(input("1 para ingresar dinero, 2 para retirar, enter para salir"))
        elif opcion==2:
            dinero=int(input("Ingrese la cantidad de dinero a ingresar: "))
            Banco.retiro(Banco.buscaCliente(clientes,nombreCliente), dinero)
            opcion=int(input("1 para ingresar dinero, 2 para retirar, enter para salir"))


opciones()


    # for i in listaClientes:
    #     print(f"Los clientes son {i[0]}"
    # opcion=input("Escriba el nombre del cliente: ")
    # for cliente in listaClientes:
    #     if cliente[0]==opcion:
    #         print(f"Usted selecciono el cliente {cliente[0]}")
    #         sigue=int(input("Si desea continuar ingrese 1, 2 para otro cliente: "))
    #         while sigue==1:
    #             opcion2=int(input("ingrese 1 para ingresar dinero, 2 para retirar, 3 para salir: "))
    #             if opcion2==1:

    #             elif opcion2==2:
    #                 dinero=int(input("Ingrese la cantidad de dinero a retirar: "))
    #                 Banco.retiro(cliente, dinero)