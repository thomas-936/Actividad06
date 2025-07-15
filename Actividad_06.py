print("Actidad 06")
productos = {}
cantidad = int(input("Ingrese la cantidad de productos que desea ingresar: "))
for i in range(cantidad):
    print(f"\nPoducto #{i+1}: ")
    while True:
        codigo = input("Ingrese codigo: ")
        if codigo in productos:
            print("El codigo ya fue registrado (Ingrse uno nuevo): ")
        else:
            break

    nombre_producto = input("Ingrese el nombre de producto: ")
    categoria = input("Ingrese la categoria del producto: ")
    talla = input("Ingrese la talla del producto: ")

    while True:
        try:
            precio_unitario = float(input("Ingrese el precio unitario del producto: "))
            if precio_unitario <= 0:
                print("Ingrese una catidad mayor a 0")
            else:
                break
        except ValueError:
            print("Ingrese un número valido para el precio.")

    while True:
        try:
            cantidad_stock = int(input("Ingrese la cantidad en stock: "))
            if cantidad_stock < 0:
                print("Ingrese una cantidad de stock mayor a 0")
            else:
                break
        except ValueError:
            print("Ingrese un número valido para la cantidad.")

    productos[codigo]= {
        "nombre_producto": nombre_producto,
        "categoria":categoria,
        "talla": talla,
        "precio_unitario": precio_unitario,
        "stock": cantidad_stock,
    }

print("\nLista de Productos: ")
for codigo, data in productos.items():
    print(f"Codígo : {codigo}")
    print(f"Nombre del producto: {data['nombre_producto']}")
    print(f"Categoria :{data['categoria']} ")
    print(f"Talla : {data['talla']}")
    print(f"Precio Unitario : {data['precio_unitario']}")
    print(f"Stock : {data['stock']} unidades")

print("Bucar procuto.")
buscado = input("Ingrese el codigo del producto que desea buscar: ")
if buscado in productos:
    print(f"Nombre del producto : {productos[buscado]['nombre_producto']}")
    print(f"Categoria : {productos[buscado]['categoria']}")
    print(f"Talla : {productos[buscado]['talla']}")
    print(f"Precio Unitario : {productos[buscado]['precio_unitario']}")
    print(f"Cantidad en Stock : {productos[buscado]['stock']} unidades")
else:
    print("No existe un producto con ese código... ")

total = 0
for datos in productos.values():
    total+= datos['precio_unitario']* datos['stock']

print(f"El valor total del inventario es: Q{total}")

conteo_categoria = {}
for dato in productos.values():
    cat = dato['categoria']
    if cat in conteo_categoria:
        conteo_categoria[cat]+=1
    else:
        conteo_categoria[cat]=1

print("\nLa cantidad de productos por categoria es: ")
for categoria, cant in conteo_categoria.items():
    print(f"{categoria}: {cant} producto(s)")
