# Lista principal donde se almacenarán los productos.
# Cada producto será una sublista de 3 elementos: [nombre, categoría, precio]
productos = []

# Bucle principal para mantener el menú, hasta que el usuario decida salir
ejecutando = True

while ejecutando:
    # Mostrar menú de opciones
    print("\n" + "=" * 40)
    print("Sistema de gestión básica de productos")
    print("=" * 40)
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    print("=" * 40)
    
    opcion = input("Ingrese una opción (1-5): ").strip()
    
    # ------------------------------------------------------------------
    # OPCIÓN 1: Agregar producto
    # ------------------------------------------------------------------
    if opcion == "1":
        print("\n--- AGREGAR PRODUCTO ---")
        
        # Ingreso y validación del nombre (no puede ser vacío)
        nombre = input("Ingrese el nombre del producto: ").strip()
        while nombre == "":
            print("El nombre no puede estar vacío. Intente nuevamente.")
            nombre = input("Ingrese el nombre del producto: ").strip()
            
        # Ingreso y validación de la categoría (no puede ser vacía)
        categoria = input("Ingrese la categoría del producto: ").strip()
        while categoria == "":
            print("La categoría no puede estar vacía. Intente nuevamente.")
            categoria = input("Ingrese la categoría del producto: ").strip()
            
        # Ingreso y validación del precio (debe ser un número entero válido y positivo)
        precio_valido = False
        precio = 0
        while not precio_valido:
            precio_input = input("Ingrese el precio (sin centavos): ").strip()
            if precio_input.isdigit():
                precio = int(precio_input)
                if precio > 0:
                    precio_valido = True
                else:
                    print("El precio debe ser un número mayor a 0.")
            else:
                print("Entrada inválida. Debe ingresar únicamente un número entero.")
                
        # Creación de la sublista del producto [nombre, categoría, precio]
        nuevo_producto = [nombre, categoria, precio]
        productos.append(nuevo_producto)
        print(f"\n¡Producto '{nombre}' agregado exitosamente!")

    # ------------------------------------------------------------------
    # OPCIÓN 2: Mostrar productos
    # ------------------------------------------------------------------
    elif opcion == "2":
        print("\n--- LISTA DE PRODUCTOS REGISTRADOS ---")
        if len(productos) == 0:
            print("No hay productos registrados en el sistema.")
        else:
            # Recorremos con range para obtener el índice y numerar los productos
            for i in range(len(productos)):
                prod = productos[i]
                # prod es una sublista: [nombre, categoría, precio]
                print(f"{i + 1}. Nombre: {prod[0]} | Categoría: {prod[1]} | Precio: ${prod[2]}")

    # ------------------------------------------------------------------
    # OPCIÓN 3: Buscar producto
    # ------------------------------------------------------------------
    elif opcion == "3":
        print("\n--- BUSCAR PRODUCTO ---")
        if len(productos) == 0:
            print("No hay productos en el sistema para buscar.")
        else:
            busqueda = input("Ingrese el nombre del producto a buscar: ").strip().lower()
            while busqueda == "":
                print("El producto buscado no puede estar vacío.")
                busqueda = input("Ingrese el nombre del producto a buscar: ").strip().lower()
                
            coincidencias = 0
            print("\nResultados encontrados:")
            
            for i in range(len(productos)):
                prod = productos[i]
                # Comparamos ignorando mayúsculas/minúsculas
                if busqueda in prod[0].lower():
                    print(f"- Posición #{i + 1} | Nombre: {prod[0]} | Categoría: {prod[1]} | Precio: ${prod[2]}")
                    coincidencias += 1
                    
            if coincidencias == 0:
                print("No se encontraron productos que coincidan con la búsqueda.")

    # ------------------------------------------------------------------
    # OPCIÓN 4: Eliminar producto
    # ------------------------------------------------------------------
    elif opcion == "4":
        print("\n--- ELIMINAR PRODUCTO ---")
        if len(productos) == 0:
            print("No hay productos registrados para eliminar.")
        else:
            # Primero mostramos los productos disponibles numerados
            print("Productos disponibles:")
            for i in range(len(productos)):
                prod = productos[i]
                print(f"{i + 1}. {prod[0]} (${prod[2]})")
                
            posicion_valida = False
            while not posicion_valida:
                num_input = input("\nIngrese el número de posición del producto a eliminar (o '0' para cancelar): ").strip()
                
                if num_input.isdigit():
                    num = int(num_input)
                    if num == 0:
                        print("Operación cancelada.")
                        posicion_valida = True
                    elif 1 <= num <= len(productos):
                        # Convertimos el número visible (1, 2, 3...) al índice real (0, 1, 2...)
                        indice_real = num - 1
                        producto_eliminado = productos.pop(indice_real)
                        print(f"\n¡El producto '{producto_eliminado[0]}' fue eliminado correctamente!")
                        posicion_valida = True
                    else:
                        print(f"Número fuera de rango. Ingrese un número entre 1 y {len(productos)}.")
                else:
                    print("Por favor, ingrese un número entero válido.")

    # ------------------------------------------------------------------
    # OPCIÓN 5: Salir del programa
    # ------------------------------------------------------------------
    elif opcion == "5":
        print("\n¡Gracias por utilizar el Sistema de gestión básica de productos! Hasta luego.")
        ejecutando = False

    # ------------------------------------------------------------------
    # Opción inválida del menú
    # ------------------------------------------------------------------
    else:
        print("\nOpción no válida. Por favor, seleccione un número entre 1 y 5.")