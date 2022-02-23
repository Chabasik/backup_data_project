import os
import shutil
from time import sleep

archive_file = os.path.sep.join([ "...", "name.zip"])
dest_usb_flash =  os.path.sep.join(['D:' + chr(92)])

# Check for insert USB directory
def wait_for_usb():
    print("Waiting for usb at D:")
    while True:
        if os.path.isdir('D:'):
            break
        else:
            print("Detecting...")
            sleep(3)

def usb():
    wait_for_usb()
    
    # If archive "name.zip" in USB - rewrite him (delete and write new), else just write
    dest_arch_remove = os.path.sep.join([dest_usb_flash, "name.zip"])
    if os.path.exists(dest_arch_remove):
        os.remove(dest_arch_remove)

    shutil.copy(archive_file, dest_usb_flash)
    print('Arhive now is copy to USB')

if __name__ == "__main__":
    usb()