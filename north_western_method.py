def make_basis(transport_table_price, demand_colomn, production_line):
    transportation_burden = [[0] * len(transport_table_price[0]) for i in
                             range(len(transport_table_price))]  # создаем таблицу для хранения объема перевозки

    residue_line = production_line  # храним остаток производства
    residue_colomn = demand_colomn  # храним остаток спроса

    for i in range(len(transportation_burden)):
        for j in range(len(transport_table_price[0])):
            if residue_colomn[i] == 0 or residue_line[j] == 0:  # проверка на нуль остаток производства и спроса
                continue

            if production_line[j] <= demand_colomn[i]:  # если спроси больше либо равен предложению
                transportation_burden[i][j] = production_line[j]
                residue_colomn[i] = demand_colomn[i] - production_line[j]
                residue_line[j] = 0
            else:  # если спрос меньше предложения
                transportation_burden[i][j] = demand_colomn[i]
                residue_line[j] = production_line[j] - demand_colomn[i]
                residue_colomn[i] = 0

    print(transportation_burden)
