"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    school_stat = [
        {'school_class': '4а', 'scores': [3, 2, 4, 4, 5]  },
        {'school_class': '4б', 'scores': [5, 5, 3, 4, 5]  },
        {'school_class': '8a', 'scores': [4, 4, 4, 4, 5]  },
        ]


    for sum_sc in school_stat:
        sum_sc['avg_score_class'] = sum(sum_sc['scores'])/len(sum_sc['scores'])
        sum_sc['avg_score_all'] = sum([sum(sum_sc['scores']) for sum_sc in school_stat ])/sum([len(sum_sc['scores']) for sum_sc in school_stat ])
        print(sum_sc)
    
if __name__ == "__main__":
    main()
