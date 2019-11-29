"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def ask_user_1():
    def user_say():
        while True:
            user_say = input('Как дела? ')
            if user_say == 'Хорошо':
                print('Ну пока')
                break
            else:
                print(f'Все говорят {user_say}, а ты купи слона')

    print(user_say()) 


if __name__ == "__main__":
    ask_user_1()
