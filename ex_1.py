"""Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и
выводит на стандартный вывод сводную таблицу результатов всех матчей.
За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число
n
n — количество завершенных игр.
После этого идет
n
n строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков

Конкретный пример ввода-вывода приведён ниже.

Порядок вывода команд произвольный.
Спартак:2 0 0 2 0
Зенит:2 1 0 1 3
Локомотив:2 2 0 0 6
"""

n = int(input())
s = []
for i in range(n):
    s.append(input().split(";"))
"""
n = 3
s =[]
s.append("Спартак;9;Зенит;10".split(";"))
s.append("Локомотив;12;Зенит;3".split(";"))
s.append("Спартак;8;Локомотив;15".split(";"))
"""
commands = dict()
for i in range(n):
    if s[i][0] not in commands.keys():
        commands[s[i][0]] = {"games": 0, "victory": 0, "draw": 0, "looses": 0, "point": 0}
    if s[i][2] not in commands.keys():
        commands[s[i][2]] = {"games": 0, "victory": 0, "draw": 0, "looses": 0, "point": 0}

for i in range(n):
    commands[s[i][0]]["games"] = commands.get(s[i][0]).get("games", 0) + 1
    commands[s[i][2]]["games"] = commands[s[i][2]].setdefault("games", 0) + 1
    if int(s[i][1]) > int(s[i][3]):
        commands[s[i][0]]["victory"] = commands[s[i][0]].setdefault("victory", 0) + 1
        commands[s[i][0]]["point"] = commands[s[i][0]].setdefault("point", 0) + 3
        commands[s[i][2]]["loses"] = commands[s[i][2]].setdefault("loses", 0) + 1
    if int(s[i][1]) < int(s[i][3]):
        commands[s[i][2]]["victory"] = commands[s[i][2]].setdefault("victory", 0) + 1
        commands[s[i][2]]["point"] = commands[s[i][2]].setdefault("point", 0) + 3
        commands[s[i][0]]["loses"] = commands[s[i][0]].setdefault("loses", 0) + 1
    if int(s[i][1]) == int(s[i][3]):
        commands[s[i][2]]["draw"] = commands[s[i][2]].setdefault("draw", 0) + 1
        commands[s[i][2]]["point"] = commands[s[i][2]].setdefault("point", 0) + 1
        commands[s[i][0]]["draw"] = commands[s[i][0]].setdefault("draw", 0) + 1
        commands[s[i][0]]["point"] = commands[s[i][0]].setdefault("point", 0) + 1
s_out = []
for key, value in commands.items():
    s_out.append(str(key) + ": " + str(value.get("games", 0)) + " " + str(value.get("victory", 0)) + " " +
                 str(value.get("gate", 0)) + " " + str(value.get("loses", 0)) + " " + str(value.get("point", 0)))
for i in range(n):
    print(s_out[i])

