"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():

    vocabulary =  {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "Пока": "Ну пока!"}


    def chat ():
        try:
            while True:
                user_say = input('Что надо?  ')
                if user_say == 'Как дела?':
                    print(vocabulary['Как дела?'])
                    user_say=input('Ещё что-то хотел?  '  )
                    if user_say== 'Что делаешь?':
                        print(vocabulary['Что делаешь?'])
                        break 
                    else:
                        print(f'Все говорят {user_say}, а ты купи слона') 
                else:
                    print(f'Все говорят {user_say}, а ты купи слона')
        except(KeyboardInterrupt):
            print("Пока")

            
                
    print(chat())


if __name__ == "__main__":
    ask_user()
