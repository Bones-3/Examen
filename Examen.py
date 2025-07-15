productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}
stock = {'8475HD': [387990,10],
'2175HD': [327990,4],
'JjfFHD': [424990,1],
'fgdxFHD': [664990,21],
'123FHD': [290890,32],
'342FHD': [444990,7],
'GF75HD': [749990,2],
'UWU131HD': [349990,1],
'FS1230HD': [249990,0],
}

def stock_marca():
    while True:
        marca=input('Ingrese el nombre de la marca: ').lower() 
        if marca.isalpha():
            break
        else:
            print('Ingrese sólo letras')
    for clave, valor in productos.items():
        if valor[0].lower()==marca:
            print(f'{valor[0]}')
            for clave, valor in stock.items():
                print(f'{valor[1]}')

def busquedaporprecio():
    while True:
        try:
            precio_min = int(input('Ingrese precio mínimo: '))
            if precio_min:
                break
        except ValueError:
            print('Debe ingresar valores enteros!!')
    while True:
        try:
            precio_max = int(input('Ingrese precio máximo: '))
            if precio_max:
                break
        except ValueError:
            print('Debe ingresar valores enteros!!')
    for clave, valor in stock.items():
        if valor[0]>= precio_min and valor[0]<=precio_max:
            if valor[1] > 0:
                for clave, valor in productos.items():
                    print(f'{valor[0]}-{clave}')

def listadodeproductos():
    print('------- Listado de Notebooks Ordenados -------')
    for clave, valor in productos.items():
        print(f'{valor[0]}-{clave}-{valor[2]}-{valor[4]}')

def menu():
    print('***MENU PRINCIPAL***')
    print('1. Stock marca.')
    print('2. Búsqueda por precio.')
    print('3. Listado de productos.')
    print('4. Salir.')

while True:
    menu()
    opcion = input('Seleccione una opcion: ')
    if opcion == '1':
        stock_marca()
    elif opcion == '2':
        busquedaporprecio()
    elif opcion == '3':
        listadodeproductos()
    elif opcion == '4':
        print('Progrma finalizado.')
        break
    else:
        print('Debe seleccionar una opcion válida!!')