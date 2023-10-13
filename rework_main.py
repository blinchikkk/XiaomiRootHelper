import os
from functions import fb_devices, make_backup, install_recovery, \
    install_boot
from messages import * 
def main():
    base_path = os.path.dirname(__file__)
    
    while True:
        print('[1] Посмотреть устройства в FastBoot.\n'
              '[2] Установка Recovery.\n'
              '[3] Установка Ядра.\n'
              '[4] Перезагрузка.\n'
              '[5] Выход.\n')
        
        choice = input('Ваш выбор >> ')
        
        if choice == '1':
            fb_devices()
        elif choice == '2':
            print(fastboot_choise_2_first)
            
            choice = input('Ваш выбор >> ')
            if choice in ['1', '2']:
                
                make_backup(base_path=base_path, section='recovery')
                install_recovery(int(choice))
            else:
                print(method_error)
            
        elif choice == '3':
            print(fastboot_choise_3_first)
            choice = input('Ваш выбор >> ')
            
            if choice in ['1', '2']:
                make_backup(base_path=base_path, section='boot')
                install_boot(int(choice))
            else:
                print(method_error)
        elif choice == '4':
            
        
            
            
if __name__ == '__main__':
    main()
    