def max_treasure(treasure_map):
    max = 0
    for fila in treasure_map:
        contador = 0
        for item in fila:
            if item != 0:
                contador = contador + item
                print("item " + str(item))
                print("contador " + str(contador))
            else: 
                if contador > max:
                    max = contador
                    print("item " + str(item))
                    print("max " + str(max))
                contador = 0
            if contador > max:
                max = contador
    return max

if __name__ == "__main__":
    treasure_map = [[3, 0, 0, 1, 2],[0, 1, 4, 0, 0],[5, 0, 0, 3, 3]]
    print(max_treasure(treasure_map))