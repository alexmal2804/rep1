"""
Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка".
Попробуем написать подобную систему.
На вход программе первой строкой передаётся количество
d известных нам слов, после чего на d строках указываются эти слова.
Затем передаётся количество l строк текста для проверки, после чего l строк текста.
Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.
Sample Input:
4
champions
we
are
Stepik
3
We are the champignons
We Are The Champions
Stepic
Sample Output:
stepic
champignons
the
"""
d = int(input())
s = []
for i in range(d):
    s.append(input())
    print(s)
l = int(input())
p = []
for i in range(l):
    p.append(input().split(" "))
"""
d = 4
s = []
s.append("champions")
s.append("we")
s.append("are")
s.append("Stepik")
l = 3
p = []
p.append("We are the champignons".split(" "))
p.append("We Are The Champions".split(" "))
p.append("Stepic".split(" "))
"""
p = [item for sublist in p for item in sublist]
print(p, s)
out_list = []
for i in p:
    k = 0
    for j in s:
        if str(i).lower() == str(j).lower():
            k = 1
    if k == 0:
        out_list.append(str(i).lower())
out_list = list(set(out_list))
for i in out_list:
    print(i)
    



