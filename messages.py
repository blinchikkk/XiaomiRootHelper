from colorama import init, Fore, Back, Style

init()

fastboot_choise_2_first = '''\n[1] fastboot flash recovery_ab (Рекомендуем).
[2] fastboot flash recovery (Прошивка в активный слот).\n'''


fastboot_choise_3_first = '''\n[1] fastboot flash boot_ab (Рекомендуем).
[2] fastboot flash boot (Прошивка в активный слот).\n'''

reboot_message_first = '''\n[1] Перезагрузка (ADB)
[2] Перезагрузка в систему. (FastBoot)
[3] Перезагрузка в Recovery. (FastBoot)
[4] Перезагрузка в Recovery. (ADB)
[5] Перезагрука в FastBoot. (ADB)\n'''

method_error = 'Ошибка! Метод не найден!'

instruments_menu = f'''\n[1] Разблокировка загрузчика ({Fore.RED}MediaTek Only!{Style.RESET_ALL}).
[2] Очистка разделов.
[3] Техническая информации об устройстве.
[4] Проверка состояния загрузчика.'''


erase_menu = f'''\n[1] Очистка /system
[2] Очистка /userdata
[3] Очистка /recovery
[4] Очистка /boot
[5] Очистка /cache
[6] Очистка /radio
[7] Очистка /data (сброс настроек)'''
