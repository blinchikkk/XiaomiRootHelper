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
        
        
def reboot(method):
    commands = {
    '1': ['adb', 'reboot'],
    '2': ['fastboot', 'reboot'],
    '3': ['fastboot', 'reboot', 'recovery'],
    '4': ['adb', 'reboot', 'recovery'],
    '5': ['adb', 'reboot', 'fastboot']
    }
    
    if str(method) in commands:
        command = commands[method]
    else:
        command = ['fastboot', 'reboot']
        
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for output in process.stdout:
            sys.stdout.write(output)
            sys.stdout.flush()
        
        process.wait()
    except subprocess.CalledProcessError as e:
        print(f"Ошибка выполнения команды: {e.output}")


def unlock_bootloader():
    try:
        if os.name == 'nt':
            os.system('cd mediatek_client')
            process = subprocess.Popen(['python', 'mtk', 'da','seccfg', 'unlock'], 
                                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        else:
            process = subprocess.Popen(['cd', 'mediatek_client', '&&', 'python3', 'mtk', 'da', 'seccfg', 'unlock'],
                                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        
        while True:
            output = process.stdout.readline()
            if not output and process.poll() is not None:
                break
            sys.stdout.write(output)
            sys.stdout.flush()

    except subprocess.CalledProcessError as e:
        print(f"Ошибка выполнения команды fastboot: {e.output}")
