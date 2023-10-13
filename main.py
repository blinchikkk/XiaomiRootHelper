import os
import subprocess
import sys
from datetime import datetime
# Функция для получения абсолютного пути к файлу в папке "images"


def run_fastboot_command():
    try:
        process = subprocess.Popen(
            ['fastboot', 'devices'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        while True:
            output = process.stdout.readline()
            if not output and process.poll() is not None:
                break
            sys.stdout.write(output)
            sys.stdout.flush()
    except subprocess.CalledProcessError as e:
        print(f"Ошибка выполнения команды fastboot: {e.output}")











def main(active=True):
    base_path = os.path.dirname(__file__)
    while active:
        print('[1] Посмотреть устройства в FastBoot.\n'
              '[2] Установка Recovery.\n'
              '[3] Установка Ядра.\n'
              '[4] Перезагрузка.\n'
              '[5] Выход.\n')

        choice = input('Ваш выбор: ')

                

        elif choice == '3':
            print('[1] fastboot flash boot_ab (Рекомендуем).\n'
                  '[2] fastboot flash boot (Прошивка в активный слот).\n')
            method = input('Ваш выбор: ')
            if method in ['1', '2']:
                make_backup(base_path, 'boot')
                install_boot(int(method))
            else:
                print()
        elif choice == '4':
            print('[1] Перезагрузка с помощью ADB.\n'
                  '[2] Перезагрузка с помощью FastBoot. (Если устройство находится в режиме FastBoot)')
            method = input('Ваш выбор: ')
            if method in ['1', '2']:
                if method == '1':
                    print('[1] Перезагрузка.\n'
                          '[2] Перезагрузка в FastBoot.\n'
                          '[3] Перезагрузка в Recovery.\n')
                    del method
                    method = input('Ваш выбор: ')
                    if method in ['1', '2', '3']:
                        reboot(1, method)
                elif method == '2':
                    print('[1] Перезагрузка в систему.\n'
                          '[2] Перезагрузка в Recovery.\n')
                    method = input('Ваш выбор: ')
                    if method in ['1', '2']:
                        reboot(2, method)
        elif choice == '5':
            active = False
        else:
            print('Ошибка! Неверный выбор!')


if __name__ == "__main__":
    main()
