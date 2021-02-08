# Anidado de funciones for. Generacion de triangulo con.
pyramid_width = 15
for i in range(0, pyramid_width):
    for j in range(0, pyramid_width - i):
        print(" ", end="")
    for k in range(0, 2 * i +1):
        print("0", end="")
    print("")
print("----------------------------------------")
# Funcion for, anidado. Generacion de flecha con if
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]
for row in picture:
    for pixel in row:
        if (pixel == 1):
            print("*", end="")
        else:
            print(" ", end="")
    print("")
print("----------------------------------------")

# Def, Funcion for, anidado. Generacion de flecha con if. Repeticion mediante definicion
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]
def show_tree():
    for image in picture:
        for pixel in image:
            if (pixel == 1):
                print("*", end="")
            else:
                print(" ", end="")
        print("")
show_tree()
show_tree()
