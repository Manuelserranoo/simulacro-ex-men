def nueva_matriz():
    lista = [["1","2","3"],["4","5","6"], ["7","8","9"]]
    lista2 = []
    lista3 = []
    lista4 = []
    traspuesta = [lista2, lista3, lista4]
    for i in lista:
        for j in i[0]:
            lista2.append(j)
        for j in i[1]:
            lista3.append(j)
        for j in i[2]:
            lista4.append(j)
    return traspuesta


if __name__ == "__main__":
    print(nueva_matriz())
