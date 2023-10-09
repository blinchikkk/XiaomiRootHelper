import os
import subprocess

active = True


def run_fastboot_command():
    try:
        output = subprocess.check_output(
            ['fastboot', 'devices'], stderr=subprocess.STDOUT, text=True)
        print(output)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка выполнения команды fastboot: {e.output}")


def twrp(method):
    try:
        if method == 1:
            output = subprocess.check_output(
                ['fastboot', 'flash', 'recovery_ab', 'recovery.img'], stderr=subprocess.STDOUT, text=True)
        elif method == 2:
            output = subprocess.check_output(
                ['fastboot', 'flash', 'recovery', 'recovery.img'], stderr=subprocess.STDOUT, text=True)
        print(output)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка выполнения команды fastboot: {e.output}")


def main():
    while active is True:
        print('[1] Посмотреть устройства в FastBoot.\n'
              '[2] Установка Recovery.\n'
              '[3] Установка Ядра.\n'
              '[4] Перезагрузка.\n'
              '[5] Выход.\n')

        answer = input('Ваш выбор: ')
        answer = int(answer)
        check_path = os.path.exists(os.path.join(
            os.path.dirname(__file__), 'fastboot.exe'))
        if check_path:
            if answer == 1:
                run_fastboot_command()

            elif answer == 2:
                check_path = os.path.exists(os.path.join(
                    os.path.dirname(__file__), 'images', 'recovery.img'))
                if check_path:
                    print('[1] fastboot flash recovery_ab (Рекомендуем).\n'
                          '[2] fastboot flash recovery (Прошивка в активный слот).\n')
                    answer = int(input('Ваш выбор: '))
                    if answer == 1:
                        twrp(1)
                    elif answer == 2:
                        twrp(2)
                    else:
                        print('Ошибка! Метод не найден!')
                else:
                    print(
                        'Ошибка! Образ Recovery не найден. Пожалуйста убедитесь что файл называется recovery.img и находится в папке "images"')

        else:
            print('Ошибка! fastboot.exe не найден!')


if __name__ == "__main__":
    main()
