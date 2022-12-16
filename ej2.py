#imprimir numeros sin usar numeros.
def contar_lista1():
    lista = ["a", "a", "a", "b", "b","c"]
    return lista.count("c"), lista.count("b"), lista.count("a")

 
if __name__ == "__main__":
    print("puedo escribir números como", contar_lista1())
