import math  # Importamos la librería "math" para hacer cálculos matemáticos.
import matplotlib.pyplot as plt  # Importamos matplotlib para crear gráficos.


# Función para leer datos desde un archivo
def read_data(filename):
    """
    Esta función lee un archivo y guarda los datos en listas.
    - filename: nombre del archivo a leer.
    Retorna tres listas: sexos, pesos en T1 y pesos en T2.
    """
    genders, weights_t1, weights_t2 = [], [], []
    with open(filename, 'r') as file:  # Abrimos el archivo en modo lectura
        for line in file:  # Leemos línea por línea
            gender, t1, t2 = line.strip().split(':')  # Dividimos la línea en 3 partes usando ":"
            if t1 != '-' and t2 != '-':  # Ignoramos las líneas con valores faltantes ("-")
                genders.append(gender)  # Guardamos el género (H o F)
                weights_t1.append(float(t1))  # Guardamos el peso en T1 (convertido a número)
                weights_t2.append(float(t2))  # Guardamos el peso en T2 (convertido a número)
    return genders, weights_t1, weights_t2  # Retornamos las 3 listas


# Función para calcular los puntajes
def calculate_scores(weights_t1, weights_t2):
    """
    Calcula los puntajes usando la fórmula dada.
    Retorna una lista con los puntajes.
    """
    scores = []
    for t1, t2 in zip(weights_t1, weights_t2):  # Iteramos sobre las listas de pesos
        score = math.sqrt((t2 ** 2) / t1) * 100  # Aplicamos la fórmula del puntaje
        scores.append(score)  # Guardamos el puntaje calculado
    return scores  # Retornamos la lista de puntajes


# Función para calcular el promedio de puntajes
def average_score(scores, genders, target_gender):
    """
    Calcula el promedio de puntajes para un grupo específico (H, F o todos '*').
    - scores: lista de puntajes.
    - genders: lista de géneros (H o F).
    - target_gender: grupo a filtrar ('H', 'F' o '*').
    """
    filtered_scores = [score for score, gender in zip(scores, genders) if
                       gender == target_gender or target_gender == '*']
    if len(filtered_scores) == 0:  # Si no hay datos en el grupo
        return 0
    return sum(filtered_scores) / len(filtered_scores)  # Retornamos el promedio calculado


# Función para extraer datos de un género específico
def extract_sublist(data, genders, target_gender):
    """
    Extrae los datos (pesos) de un grupo específico (H o F).
    """
    return [value for value, gender in zip(data, genders) if gender == target_gender]


# Función para graficar los datos
def plot_graph(weights_t1, weights_t2, genders, title):
    """
    Crea dos gráficos:
    - Izquierda: Hombres
    - Derecha: Mujeres
    Muestra la relación entre el peso en T1 y el peso en T2.
    """
    # Extraemos los datos por género
    male_t1 = extract_sublist(weights_t1, genders, 'H')
    male_t2 = extract_sublist(weights_t2, genders, 'H')
    female_t1 = extract_sublist(weights_t1, genders, 'F')
    female_t2 = extract_sublist(weights_t2, genders, 'F')

    # Creamos una figura con dos gráficos
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Gráfico para hombres
    ax1.scatter(male_t1, male_t2, color='blue')  # Dibujamos puntos en azul
    ax1.set_title('Hombres')  # Título del gráfico
    ax1.set_xlabel('Peso en T1')  # Etiqueta del eje X
    ax1.set_ylabel('Peso en T2')  # Etiqueta del eje Y

    # Gráfico para mujeres
    ax2.scatter(female_t1, female_t2, color='red')  # Dibujamos puntos en rojo
    ax2.set_title('Mujeres')
    ax2.set_xlabel('Peso en T1')
    ax2.set_ylabel('Peso en T2')

    # Título principal y mostrar gráficos
    plt.suptitle(title)
    plt.tight_layout()
    plt.show()


# Programa principal
def main():
    """
    Esta es la función principal. Aquí leemos los datos, calculamos los puntajes,
    imprimimos los promedios y mostramos los gráficos.
    """
    # Paso 1: Leer los datos de los archivos
    exp_genders, exp_t1, exp_t2 = read_data('experimental.txt')  # Datos del grupo experimental
    ctrl_genders, ctrl_t1, ctrl_t2 = read_data('controle.txt')  # Datos del grupo control

    # Paso 2: Calcular los puntajes
    exp_scores = calculate_scores(exp_t1, exp_t2)
    ctrl_scores = calculate_scores(ctrl_t1, ctrl_t2)

    # Paso 3: Imprimir los promedios
    print("Promedios del Grupo Experimental")
    print("Hombres:", average_score(exp_scores, exp_genders, 'H'))
    print("Mujeres:", average_score(exp_scores, exp_genders, 'F'))
    print("Combinado:", average_score(exp_scores, exp_genders, '*'))

    print("\nPromedios del Grupo Control")
    print("Hombres:", average_score(ctrl_scores, ctrl_genders, 'H'))
    print("Mujeres:", average_score(ctrl_scores, ctrl_genders, 'F'))
    print("Combinado:", average_score(ctrl_scores, ctrl_genders, '*'))

    # Paso 4: Crear gráficos
    plot_graph(exp_t1, exp_t2, exp_genders, "Grupo Experimental")
    plot_graph(ctrl_t1, ctrl_t2, ctrl_genders, "Grupo Control")


# Ejecutar el programa principal
if __name__ == "__main__":
    main()
