print("Actidad 06")
prductos = {}
cantidad = int(input("Ingrese la cantidad de productos que desea ingresar: "))
for i in range(cantidad):
    print(f"\nPoducto #{i+1}: ")
    codigo = input("Ingrese codigo: ")
    nombre_producto = input("Ingrese el nomnbre de procducto: ")
    categoria = input("Ingrese la categoria del producto: ")
    talla = input("Ingrese la talla del producto: ")
    precio_unitario = input("Ingrese el precio unitario del producto: ")
    catidad_stock = input("Ingrese la cantidad en stock: ")

    prductos[codigo]= {
        "nombre del producto":nombre_producto,
        "categoria":categoria,
        "talla": talla,
        "precio unitario": precio_unitario,
        "cantidad en stock": catidad_stock,
    }