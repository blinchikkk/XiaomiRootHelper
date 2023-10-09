import os
import subprocess
import sys

def check_file_exists(file_path):
    return os.path.exists(file_path)


def run_fastboot_command():
    try:
        process = subprocess.Popen(['fastboot', 'devices'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        while True:
            output = process.stdout.readline()
            if not output and process.poll() is not None:
                break
            sys.stdout.write(output)
            sys.stdout.flush()
    except subprocess.CalledProcessError as e:
        print(f"Ошибка выполнения команды fastboot: {e.output}")

def install_recovery(method):
    try:
        option = 'recovery_ab' if method == 1 else 'recovery'
        process = subprocess.Popen(['fastboot', 'flash', option, 'recovery.img'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        while True:
            output = process.stdout.readline()
            if not output and process.poll() is not None:
                break
            sys.stdout.write(output)
            sys.stdout.flush()
    except subprocess.CalledProcessError as e:
        print(f"Ошибка выполнения команды fastboot: {e.output}")

def main(active=True):
    while active:
        print('[1] Посмотреть устройства в FastBoot.\n'
              '[2] Установка Recovery.\n'
              '[3] Установка Ядра.\n'
              '[4] Перезагрузка.\n'
              '[5] Выход.\n')

        choice = input('Ваш выбор: ')

        if choice == '1':
            run_fastboot_command()
        elif choice == '2':
            recovery_img_path = os.path.join(os.path.dirname(__file__), 'images', 'recovery.img')
            if check_file_exists(recovery_img_path):
                print('[1] fastboot flash recovery_ab (Рекомендуем).\n'
                      '[2] fastboot flash recovery (Прошивка в активный слот).\n')
                method = input('Ваш выбор: ')
                if method in ['1', '2']:
                    install_recovery(int(method))
                else:
                    print('Ошибка! Метод не найден!')
            else:
                print('Ошибка! Образ Recovery не найден. Пожалуйста, убедитесь, что файл называется recovery.img и находится в папке "images"')
        elif choice == '5':
            active = False
        else:
            print('Ошибка! Неверный выбор!')

if __name__ == "__main__":
    main()
