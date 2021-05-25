import random


def make_basis(transport_table_price, demand_colomn, production_line):
    transportation_burden = [[0] * len(transport_table_price[0]) for i in
                             range(len(transport_table_price))]  # создаем таблицу для хранения объема перевозки

    residue_line = production_line  # храним остаток производства
    residue_colomn = demand_colomn  # храним остаток спроса

    for i in range(len(transportation_burden)):
        for j in range(len(transportation_burden[0])):
            if residue_colomn[i] == 0 or residue_line[j] == 0:  # проверка на нуль остаток производства и спроса
                continue

            if production_line[j] <= demand_colomn[i]:  # если спрос больше, либо равен предложению
                transportation_burden[i][j] = production_line[j]
                residue_colomn[i] = demand_colomn[i] - production_line[j]
                residue_line[j] = 0
            else:  # если спрос меньше предложения
                transportation_burden[i][j] = demand_colomn[i]
                residue_line[j] = production_line[j] - demand_colomn[i]
                residue_colomn[i] = 0

    print(transportation_burden)
    print("Total price is: " + str(total_price(transport_table_price, transportation_burden)))
    potential_method(transport_table_price, transportation_burden, demand_colomn, production_line)


def total_price(transport_table_price, transportation_burden):
    final_price = 0

    for i in range(len(transportation_burden)):
        for j in range(len(transportation_burden[0])):
            final_price += transport_table_price[i][j] * transportation_burden[i][j]

    return final_price


def find_max_price(transport_table_price):
    max = 0
    max_colomn = 0
    max_line = 0

    for i in range(len(transport_table_price)):
        for j in range(len(transport_table_price[0])):
            if max < transport_table_price[i][j]:
                max = transport_table_price[i][j]
                max_line = i
                max_colomn = j

    return max_line, max_colomn


def find_max_residual(transport_table_price, line_potential, colomn_potencial):
    max = 0
    max_colomn = 0
    max_line = 0

    for i in range(len(transport_table_price)):
        for j in range(len(transport_table_price[0])):
            residial = line_potential[j] + colomn_potencial[i] - transport_table_price[i][j]
            if max < residial:
                max = residial
                max_line = i
                max_colomn = j

    return max_line, max_colomn


def potential_method(transport_table_price, transportation_burden, demand_colomn, production_line):
    line_potential = [0 for i in range(len(transport_table_price[0]))]

    colomn_potencial = [0 for i in range(len(transport_table_price))]

    max_line, max_colomn = find_max_price(transport_table_price)

    line_potential[max_colomn] = random.randint(0, transport_table_price[max_line][max_colomn])

    colomn_potencial[max_line] = transport_table_price[max_line][max_colomn] - line_potential[max_colomn]

    for i in range(len(transport_table_price)):
        for j in range(len(transport_table_price[0])):

            if transportation_burden[i][j] != 0:
                if line_potential[j] != 0 and colomn_potencial[i] == 0:
                    colomn_potencial[i] = transport_table_price[i][j] - line_potential[j]

                elif line_potential[j] == 0 and colomn_potencial[i] != 0:
                    line_potential[j] = transport_table_price[i][j] - colomn_potencial[i]

    summa_of_potentials = [[0] * len(transport_table_price[0]) for i in
                           range(len(transport_table_price))]  # создаем двумерный массив для хранения суммы потенциалов

    for i in range(len(transport_table_price)):  # заполняем массив суммы потенциалов
        for j in range(len(transport_table_price[0])):
            if transportation_burden[i][j] == 0:
                summa_of_potentials[i][j] = line_potential[j] + colomn_potencial[i]

    print(find_max_residual(transport_table_price,line_potential,colomn_potencial))
