"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
    def compare (string1, string2):
        
        if type(string1) is not str or type(string2) is not str:
            return 0
        elif string1!=string2 and string2=='learn':
            return 3
        elif string1!=string2 and len(string1)>len(string2):
            return 2
        elif type(string1) is str and type(string2) is str and string1==string2: 
            return 1 
        else:
            return "Не совпадают условия задачи, подумайте хорошо, что вы пишите"  
 
    #Проверить, является ли то, что передано функции, строками. Если нет - вернуть 0
    string1=40
    string2='40'
    print(compare(string1, string2))

    #Если строки одинаковые, вернуть 1
    string1='40' 
    string2='40'
    print(compare(string1, string2))

    #Если строки разные и первая длиннее, вернуть 2
    string1='404' 
    string2='40'
    print(compare(string1, string2))

    #Если строки разные и вторая строка 'learn', возвращает 3
    string1='40' 
    string2='learn'
    print(compare(string1, string2))

    #Если не выполняются условия задачи
    string1='40' 
    string2='404'
    print(compare(string1, string2))

if __name__ == "__main__":
    main()

