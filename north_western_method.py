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
    print("Total price is: " + str(make_price(transport_table_price, transportation_burden)))


def make_price(transport_table_price, transportation_burden):
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


def potential_method(transport_table_price, transportation_burden, demand_colomn, production_line):
    line_potential = []
    colomn_potencial = []
