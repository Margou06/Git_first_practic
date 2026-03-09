def calculator():
    while (10 > 3):
        print("\nПростой калькулятор")
        print("Доступные операции: плюс(+), минус(-), *, /, ** (возведение в степень), exit (выход)")

        # Получение выбора пользователя
        choice = input("Выберите операцию: ")

        # Проверка на выход
        if choice.lower() == 'exit':
            print("До свидания!")
            break

        # Получение чисел для операции
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: введите корректное число!")
            continue

        # Выполнение выбранной операции
        if choice == '+':
            print(f"Результат: {num1 + num2}")
        elif choice == '-':
            print(f"Результат: {num1 - num2}")
        elif choice == '*':
            print(f"Результат: {num1 * num2}")
        elif choice == '/':
            if num2 == 0:
                print("Ошибка: деление на ноль!")
            else:
                print(f"Результат: {num1 / num2}")
        elif choice == '**':
            print(f"Результат: {num1 ** num2}")
        else:
            print("Неизвестная операция!")

# Запуск калькулятора
calculator()
