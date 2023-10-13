import subprocess
import sys
import os
from datetime import datetime

def fb_devices():
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
        

def make_backup(base_path, section):
    check_backup_folder = os.path.exists(os.path.join(base_path, 'backups'))
    check_section_folder = os.path.exists(os.path.join(base_path, 'backups', section))
    
    if not check_backup_folder:
        os.mkdir(os.path.join(base_path, 'backups'))
        
    if not check_section_folder:
        os.mkdir(os.path.join(base_path, 'backups', section))
    
    timestamp = datetime.now().strftime("%Y.%m.%d %H:%M:%S")
    print('Запуск процесса создания дампа...')
    command = ['fastboot', 'dump', section, path]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    stdout, stderr = process.communicate()
    
    print(f"Команда выполнена с кодом возврата: {process.returncode}")
    
    print("Стандартный вывод:")
    print(stdout.decode())
    print("Ошибки:")
    print(stderr.decode())
    
    
def check_file_exists(file_path):
    return os.path.exists(file_path)


def get_absolute_path(filename):
    images_dir = os.path.join(os.path.dirname(__file__), 'images')
    return os.path.join(images_dir, filename)



def create_folder(path, name):
    full_path = os.path.join(path, name)

    try:
        os.mkdir(full_path)
        return os.path.join(full_path, name)
    
    except OSError as e:
        print(f'Ошибка! ({e})')
        
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