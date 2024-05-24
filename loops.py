def index_of_by_index(target, lista, start_index):
    for index in range(start_index, len(lista)):
        if lista[index] == target:
            return index
    return -1

colors = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]

print(index_of_by_index("Black", colors, 1))
print(index_of_by_index("Black", colors, 4)) 
print(index_of_by_index("Green", colors, 2))

print(" ")


def index_of_empty(lista):
    for index, value in enumerate(lista):
        if value == "":
            return index
    return -1

colors1 = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]
print(index_of_empty(colors1))
colors2 = ["Red", "Green", "", "", "Pink", "", "Black"]
print(index_of_empty(colors2))



print(" ")



def index_of(element, lista):
    for index, value in enumerate(lista):
        if value==element:
            return index
    return -1
colors = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]
print(index_of("Black", colors))
print(index_of("Blue", colors))   


print(" ")


def put(target, lista):
    for index, value in enumerate(lista):
        if value == "":
            lista[index] = target
            return index
    return -1

colors1 = ["Red", "Green", "", "", "Pink", "", "Black"]

print(put("Blue", colors1)) 
print(colors1) 

colors2 = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]

print(put("Blue", colors2)) 
print(colors2)  


print(" ")


def remove(target, lista):
    count = 0
    for index, value in enumerate(lista):
        if value == target:
            lista[index] = ""
            count += 1
    return count

colors = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]

print(remove("Black", colors))
print(colors)  

print(remove("Blue", colors)) 
print(colors)
