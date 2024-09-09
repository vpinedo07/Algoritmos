"""
Programa que calcula la edad de perro y un gato
en años humanos
"""
#Calcula la edad del perro y el gato en años humanos
def calculate_pet_ages(human_years):
    #Al primer año
    if human_years == 1:
        cat_years = 15
        dog_years = 15
    #Al segundo año
    elif human_years == 2:
        cat_years = 15 + 9
        dog_years = 15 + 9
    #Más de dos años
    else:
        cat_years = 15 + 9 + (human_years - 2) * 4
        dog_years = 15 + 9 + (human_years - 2) * 5

    #Devuelve una lista con los años humnos, gato y perro
    return [human_years, cat_years, dog_years]


# Ejemplo de uso
#human_years = 15
human_years = int(input("Dame los años humanos: "))

#Llama a la función para los cálculos
ages = calculate_pet_ages(human_years)
print("Los años humanos son: " + str(human_years))
print(f"Los años del gato son: {ages[1]}")
print(f"Los años del perro son: {ages[2]}")
#Imprime el tipo de datos devuelto por la función
#print (type(ages))
