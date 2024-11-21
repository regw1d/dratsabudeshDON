import time

while True:
    user_input = input("Введи число от 0 до 1 дон : ")

    if user_input.lower() == "e":
        print("пока  дон!")
        break

    try:
        aboba = int(user_input)

        if aboba == 0:
            print("Уважение жиесть дон")
            time.sleep(2)
            print("Молодец дон")

        elif aboba > 1:
            print("Уважиния жи нет дон >:(")
            time.sleep(2)
            print("Я сказал дон от 0 до 1 дон")

        else:
            print("Ле дон 1 на 1 да дон?")
            time.sleep(2)
            print("ну че ты ссыкло дон")

    except ValueError:
        print("введи корректное число дон")
