#!/usr/bin/env python3

import shutil
import os
import datetime
import tarfile

def backup_folder(src, dst):
    try:
        timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        backup_dir = os.path.join(dst, f"backup_{timestamp}")
        os.makedirs(backup_dir, exist_ok=True)

        if not any(os.scandir(src)):
            print("There are no files to backup ...")
            return None

        print(f"\n######## Beginning backup to {backup_dir}...\n")
        print(f"######## All folders and files will be copied to {backup_dir}...")

        dest_copy = os.path.join(backup_dir, os.path.basename(os.path.normpath(src)))
        shutil.copytree(src, dest_copy)

        archive_name = f"{backup_dir}.tar.gz"

        with tarfile.open(archive_name, mode="w:gz") as tar:
            tar.add(backup_dir, arcname=os.path.basename(backup_dir))
        
        print("######## Files backed up succesfully")
            
        return archive_name

    except Exception as e:
        print(f"######## An error occured: {str(e)}")
        return None

if __name__ == "__main__":
    source_folder = "/home/ea/"
    target_folder = "/tmp/backups/"

    backup_folder(source_folder, target_folder)








