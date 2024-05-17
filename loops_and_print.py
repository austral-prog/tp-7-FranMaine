def enumerate_list(lista):
    result = []
    for index, value in enumerate(lista):
        if value:
            result.append(f"{len(result)}. {value}")
    return result

colors = ["Red", "Green", "", "White", "Black"]
enumerated_colors = enumerate_list(colors)
print(enumerated_colors)



def enumerate_backwards(lista):
    result=[]
    for index, color in enumerate(lista):
        if color:
            result.append(f'{len(result)}. {color[::-1]}')
    return result
colors = ["Red", "Green", "", "White", "Black"]
print(enumerate_backwards(colors))
