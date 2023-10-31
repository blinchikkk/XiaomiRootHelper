import os
from functions import fb_devices, install_recovery, \
    install_boot, reboot, unlock_bootloader
from messages import *
from colorama import init, Fore, Back, Style

init()

def return_text():
    platform_name = 'Windows' if os.name == 'nt' else 'Linux'
    version = "v.1.2.0"

    text = f"""{Fore.CYAN}
$$\   $$\ $$\                                   $$\ $$$$$$$\  $$\   $$\ 
$$ |  $$ |\__|                                  \__|$$  __$$\ $$ |  $$ |
\$$\ $$  |$$\  $$$$$$\   $$$$$$\  $$$$$$\$$$$\  $$\ $$ |  $$ |$$ |  $$ |
 \$$$$  / $$ | \____$$\ $$  __$$\ $$  _$$  _$$\ $$ |$$$$$$$  |$$$$$$$$ |
 $$  $$<  $$ | $$$$$$$ |$$ /  $$ |$$ / $$ / $$ |$$ |$$  __$$< $$  __$$ |
$$  /\$$\ $$ |$$  __$$ |$$ |  $$ |$$ | $$ | $$ |$$ |$$ |  $$ |$$ |  $$ |
$$ /  $$ |$$ |\$$$$$$$ |\$$$$$$  |$$ | $$ | $$ |$$ |$$ |  $$ |$$ |  $$ |
\__|  \__|\__| \_______| \______/ \__| \__| \__|\__|\__|  \__|\__|  \__|{Style.RESET_ALL}                                                
                    platform: {Fore.RED}{platform_name}{Style.RESET_ALL}
                    version: {Fore.GREEN}{version}{Style.RESET_ALL}
    """
    print(text)

def main():
    return_text()
    base_path = os.path.dirname(__file__)
    
    while True:
        print('[1] Посмотреть устройства в FastBoot.\n'
              '[2] Установка Recovery.\n'
              '[3] Установка Ядра.\n'
              '[4] Инструменты.\n'
              '[5] Перезагрузка.\n'
              '[10] Выход.\n')
        
        choice = input('Ваш выбор >> ')
#----------------------------------------------------
        if choice == '1':
            fb_devices()
#----------------------------------------------------
        elif choice == '2':
            print(fastboot_choise_2_first)
            
            choice = input('Ваш выбор >> ')
            if choice in ['1', '2']:
                
                install_recovery(int(choice))
            else:
                print(method_error)
#----------------------------------------------------
        elif choice == '3':
            print(fastboot_choise_3_first)
            choice = input('Ваш выбор >> ')
            
            if choice in ['1', '2']:
                install_boot(int(choice))
            else:
                print(method_error)
#----------------------------------------------------
        elif choice == '4':
            print(instruments_menu)
            choice = input('Ваш выбор >> ')

            if choice == 1:
                unlock_bootloader()
            elif choice == 2:
                print('In developing...')
#----------------------------------------------------
        elif choice == '5':
            print(reboot_message_first)
            choice = input('Ваш выбор >> ')
            
            if choice in ['1','2','3','4','5']:
                reboot(choice)
#----------------------------------------------------
        elif choice == '10':
            break
        else:
            print(method_error)
            
            
if __name__ == '__main__':
    main()
    