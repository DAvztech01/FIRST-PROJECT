import os
import time

shutdown = input("Restart PC? (yes/no): ").lower()

if shutdown == "no":
    print("Restart cancelled.")
    quit()
else:     
    try:
        print("Restarting in...")
        for i in range(5, 0, -1):
            print(f'{i}...Press Ctrl + C to abort')
            time.sleep(5)
        os.system('shutdown /r /t 1')
    except KeyboardInterrupt:
        os.system('shutdown /a')
        print("Restart Aborted")