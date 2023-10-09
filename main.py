import os
import subprocess

active = True

def run_fastboot_command():
    try:
        output = subprocess.check_output(['fastboot', 'devices'], stderr=subprocess.STDOUT, text=True)
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
        check_path = os.path.exists(os.path.join(os.path.dirname(__file__), 'fastboot.exe'))
        if check_path:
            if answer == 1:
                run_fastboot_command()
        else:
            print('Ошибка! fastboot.exe не найден!')
                
if __name__ == "__main__":
    main()
