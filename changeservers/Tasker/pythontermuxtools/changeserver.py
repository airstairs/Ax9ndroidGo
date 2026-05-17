import os
import time

def check_file_content(filepath):
    # Check if the file exists first to avoid errors
    if os.path.exists(filepath):
        # Check if the file size is greater than 0 bytes
        if os.path.getsize(filepath) > 0:
            os.system("am start com.motorola.launcher3/com.android.launcher3.CustomizationPanelLauncher")
            time.sleep(1.3)
            os.system("rm thefile")
            os.system("touch thefile")
        else:
            print("The file is empty.")

    else:
        print("File not found.")



go = True
while go:
    # Usage
    check_file_content("thefile")
    time.sleep(2)
