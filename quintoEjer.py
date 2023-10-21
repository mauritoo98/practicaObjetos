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
        nombreCliente=""
        objetoCliente=[]
        clienteExiste= False
        for cliente in listaCliente:
            if cliente[0]==opcion:
                print(f"Usted selecciono el cliente {cliente[0]}")
                nombreCliente= cliente
                clienteExiste=True
                objetoCliente.append(nombreCliente)
                objetoCliente.append(clienteExiste)
        return objetoCliente


def opciones():

    clientes=Banco.agregaCliente()
    seguir=1
    while seguir==1:
        opcion=input("Ingrese el nombre a buscar: ")
        objetoDevolucion=Banco.buscaCliente(clientes, opcion)
        if len(objetoDevolucion)==2:
            print("Ese cliente existe")
            objetoCliente=objetoDevolucion[0]
            opcion2=int(input("Si desea ingresar dinero escriba 1, para retirar 2, sino enter: "))
            if opcion2==1:
                    ingreso=int(input("Ingrese la cantidad a ingresar: "))
                    Banco.ingreso(objetoCliente, ingreso)
            elif opcion2==2:
                    egreso=int(input("Ingrese la cantidad a retirar: "))
                    Banco.retiro(objetoCliente, egreso)
            else:
                break
        else: 
            print("Ese cliente no existe")
        seguir=int(input("Si desea seguir ingrese 1, para salir 2: "))
    totalMes=0
    for i in clientes:
        print(f"El cliente {i[0]} tiene {i[1]}")
        totalMes=i[1]+totalMes
    print(f"El total depositado en el banco es de {totalMes}")

opciones()