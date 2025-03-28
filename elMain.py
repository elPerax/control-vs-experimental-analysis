import math  # Importamos la librería "math" para hacer cálculos matemáticos.
import matplotlib.pyplot as plt  # Importamos matplotlib para crear gráficos.



def read_data(filename):
    """
    Esta función lee un archivo y guarda los datos en listas.
    - filename: nombre del archivo a leer.
    Retorna tres listas: sexos, pesos en T1 y pesos en T2.
    """
    genders, weights_t1, weights_t2 = [], [], []
    with open(filename, 'r') as file:
        for line in file:  # Leemos línea por línea
            gender, t1, t2 = line.strip().split(':')
            if t1 != '-' and t2 != '-':
                genders.append(gender)
                weights_t1.append(float(t1))
                weights_t2.append(float(t2))
    return genders, weights_t1, weights_t2


def calculate_scores(weights_t1, weights_t2):
    """
    Calcula los puntajes usando la fórmula dada.
    Retorna una lista con los puntajes.
    """
    scores = []
    for t1, t2 in zip(weights_t1, weights_t2):
        score = math.sqrt((t2 ** 2) / t1) * 100
        scores.append(score)
    return scores



def average_score(scores, genders, target_gender):

    filtered_scores = [score for score, gender in zip(scores, genders)
                       if gender == target_gender or target_gender == '*']
    if len(filtered_scores) == 0:  # Si no hay datos en el grupo
        return 0
    return sum(filtered_scores) / len(filtered_scores)  # Retornamos el promedio calculado


def extract_sublist(data, genders, target_gender):

    return [value for value, gender in zip(data, genders) if gender == target_gender]



def plot_graph(weights_t1, weights_t2, genders, title):

    # Extraemos los datos por género
    male_t1 = extract_sublist(weights_t1, genders, 'H')
    male_t2 = extract_sublist(weights_t2, genders, 'H')
    female_t1 = extract_sublist(weights_t1, genders, 'F')
    female_t2 = extract_sublist(weights_t2, genders, 'F')


    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))


    ax1.scatter(male_t1, male_t2, color='blue')  # Dibujamos puntos en azul
    ax1.set_title('Hombres')  # Título del gráfico
    ax1.set_xlabel('Peso en T1')  # Etiqueta del eje X
    ax1.set_ylabel('Peso en T2')  # Etiqueta del eje Y


    ax2.scatter(female_t1, female_t2, color='red')  # Dibujamos puntos en rojo
    ax2.set_title('Mujeres')
    ax2.set_xlabel('Peso en T1')
    ax2.set_ylabel('Peso en T2')

    # Título principal y mostrar gráficos
    plt.suptitle(title)
    plt.tight_layout()
    plt.show()



def main():


    exp_genders, exp_t1, exp_t2 = read_data('experimental.txt')  # Datos del grupo experimental
    ctrl_genders, ctrl_t1, ctrl_t2 = read_data('controle.txt')  # Datos del grupo control


    exp_scores = calculate_scores(exp_t1, exp_t2)
    ctrl_scores = calculate_scores(ctrl_t1, ctrl_t2)


    print("Promedios del Grupo Experimental")
    print("Hombres:", average_score(exp_scores, exp_genders, 'H'))
    print("Mujeres:", average_score(exp_scores, exp_genders, 'F'))
    print("Combinado:", average_score(exp_scores, exp_genders, '*'))

    print("\nPromedios del Grupo Control")
    print("Hombres:", average_score(ctrl_scores, ctrl_genders, 'H'))
    print("Mujeres:", average_score(ctrl_scores, ctrl_genders, 'F'))
    print("Combinado:", average_score(ctrl_scores, ctrl_genders, '*'))

    plot_graph(exp_t1, exp_t2, exp_genders, "Grupo Experimental")
    plot_graph(ctrl_t1, ctrl_t2, ctrl_genders, "Grupo Control")


if __name__ == "__main__":
    main()