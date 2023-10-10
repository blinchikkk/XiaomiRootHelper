import os
import subprocess
import sys
from datetime import datetime
# Функция для получения абсолютного пути к файлу в папке "images"

def create_folder(path, name):
    full_path = os.path.join(path, name)

    try:
        os.mkdir(full_path)
        return os.path.join(full_path, name)
    
    except OSError as e:
        print(f'Ошибка! ({e})')
        
def get_absolute_path(filename):
    images_dir = os.path.join(os.path.dirname(__file__), 'images')
    return os.path.join(images_dir, filename)

def make_backup(base_path, section):
    # Проверяем, существует ли папка "backups"
    check_backup_folder = os.path.exists(os.path.join(base_path, 'backups'))
    
    # Если папки "backups" нет, создаем её
    if not check_backup_folder:
        os.mkdir(os.path.join(base_path, 'backups'))
    
    # Проверяем, существует ли папка для данной секции
    check_section_folder = os.path.exists(os.path.join(base_path, 'backups', section))
    
    # Если папки для секции нет, создаем её
    if not check_section_folder:
        os.mkdir(os.path.join(base_path, 'backups', section))
    
    # Создаем путь для сохранения бэкапа с уникальным временным штампом
    timestamp = datetime.now().strftime("%Y.%m.%d %H:%M:%S")
    path = os.path.join(base_path, 'backups', section, timestamp)
    
    # Запускаем команду fastboot dump
    command = ['fastboot', 'dump', section, path]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Дождитесь завершения процесса fastboot dump
    stdout, stderr = process.communicate()
    
    # Выведите статус завершения команды
    print(f"Команда выполнена с кодом возврата: {process.returncode}")
    
    # Выведите стандартный вывод и ошибки (если есть)
    print("Стандартный вывод:")
    print(stdout.decode())
    print("Ошибки:")
    print(stderr.decode())

            
            
def check_file_exists(file_path):
    return os.path.exists(file_path)


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


def install_recovery(method):
    try:
        option = 'recovery_ab' if method == 1 else 'recovery'
        recovery_img_path = get_absolute_path('recovery.img')
        process = subprocess.Popen(['fastboot', 'flash', option, recovery_img_path],
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        while True:
            output = process.stdout.readline()
            if not output and process.poll() is not None:
                break
            sys.stdout.write(output)
            sys.stdout.flush()
    except subprocess.CalledProcessError as e:
        print(f"Ошибка выполнения команды fastboot: {e.output}")


def install_boot(method):
    try:
        option = 'boot_ab' if method == 1 else 'boot'
        boot_img_path = get_absolute_path('boot.img')
        process = subprocess.Popen(['fastboot', 'flash', option, boot_img_path],
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        while True:
            output = process.stdout.readline()
            if not output and process.poll() is not None:
                break
            sys.stdout.write(output)
            sys.stdout.flush()
    except subprocess.CalledProcessError as e:
        print(f"Ошибка выполнения команды fastboot: {e.output}")


def reboot(method, type):
    def return_method(method, type):
        option = 'adb' if method == 1 else 'fastboot'
        reboot_type = None
        if method == 1:
            if type == 2:
                reboot_type = 'fastboot'
            elif type == 3:
                reboot_type = 'recovery'
            else:
                reboot_type = ''
        else:
            if type == 2:
                reboot_type = 'recovery'
            else:
                reboot_type = ''

        return [option, reboot_type]

    try:
        option = return_method(method, type)[0]
        reboot_location = return_method(method, type)[1]

        process = subprocess.Popen([option, reboot_location])
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
            print('[1] fastboot flash recovery_ab (Рекомендуем).\n'
                  '[2] fastboot flash recovery (Прошивка в активный слот).\n')
            method = input('Ваш выбор: ')
            if method in ['1', '2']:
                install_recovery(int(method))
            else:
                print('Ошибка! Метод не найден!')
        elif choice == '3':
            print('[1] fastboot flash boot_ab (Рекомендуем).\n'
                  '[2] fastboot flash boot (Прошивка в активный слот).\n')
            method = input('Ваш выбор: ')
            if method in ['1', '2']:
                install_boot(int(method))
            else:
                print('Ошибка! Метод не найден!')
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
