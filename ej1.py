


#Crear una funcion que elimine x caracteres de una lista
def eliminar_caracteres():
    lista = ["#Juan", "Pe#dro", "#98Maria", "##Jose", "#Luis","#Candace#"]
    lista2 = []
    for i in lista:
        if i[0] == "#":
            lista2.append(i.replace("#", ""))
        
    return eliminar_numeros(lista2)

def eliminar_numeros(lista2):
    for i in lista2:
        if i.isalpha() == False:
            lista2.remove(i)
    return lista2


if __name__ == "__main__":
    print(eliminar_caracteres())    

