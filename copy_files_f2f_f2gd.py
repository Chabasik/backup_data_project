import shutil
import os
import zipfile
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# The program copies files from selected folders to the archive. The archive is sent to the specified folder.
# And additionally, the archive is downloaded to Google Drive.
# You need enough disk space and the client_secrets.json file in folder where file starts to work program properly.

arch_name = str("name_archive" + ".zip") 

fol_path_1 = os.path.sep.join(['C:', 'Eample', 'needed_folder'])
fol_path_2 = os.path.sep.join(['...'])
fol_path_3 = os.path.sep.join(['...'])
backup_folders = [ fol_path_1, fol_path_2, fol_path_3 ] 
dest = os.path.sep.join([" ... " ]) # Add path, where need copy folder (destination)
ignore_file = []  # If need ignore some files 

def archive_construct(arch, folder_list, mode):
    num = 0
    num_ignore = 0
    z = zipfile.ZipFile(arch, mode, zipfile.ZIP_DEFLATED, True)
    for add_folder in folder_list:
        for root, dirs, files in os.walk(add_folder):
            for file in files:
                if file in ignore_file:
                    print("Ignore! - ", str(file))
                    num_ignore += 1
                    continue
                path = os.path.join(root, file)
                z.write(path)
                print(num, path)
                num += 1
    z.close()
    print("------------------------------")
    print("Add: ", num)
    print("Ignore: ", num_ignore)

def copy_folder_to_folder():  # Check for rewrite archive
    file_exist = os.path.sep.join([dest, arch_name])
    if os.path.exists(file_exist):
        os.remove(file_exist)           
    archive_construct(arch_name, backup_folders, "w")
    base_located_archive = os.path.sep.join(["...", arch_name])   # The path where the archive is located
    shutil.move(base_located_archive, dest)
    print("Archive move - succes")
    print("------------------------------")

def copy_folder_to_google_drive():
    # Create a Google authentication object and authorize in Google Drive
    gauth = GoogleAuth()
    drive = GoogleDrive(gauth)
 
    main_file_path = os.path.sep.join([ dest, arch_name])
    # Create a file, upload the file to Google Drive
    my_file = drive.CreateFile({'title' : arch_name})
    my_file.SetContentFile(main_file_path)
    my_file.Upload()

    print('File' + arch_name + 'was uploaded!')
    print("------------------------------")

def full_copy():
    copy_folder_to_folder()
    copy_folder_to_google_drive()
    print("The program has completed")

if __name__ == "__main__":
    full_copy()
exit()
