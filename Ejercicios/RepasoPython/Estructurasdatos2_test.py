def main():
    lista_compra = set(())
    pregunta = "SI"

    while (pregunta == "SI"):
        articulo = str(input("Introduce un artículo: "))

        lista_compra.add(articulo)
        pregunta = str(
            input("¿Quieres añadir un artículos a lista (Si/No)?")).upper()

    print("Articulos añadidos:")

    for a in lista_compra:
        print(a)

    print(f"Número de artículos: {len(lista_compra)}")

main()