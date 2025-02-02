import subprocess
import threading
import time

def run_rclone():
    files_to_backup = ["shell.txt", "Mailer.txt", "password.txt", "random.txt"]
    source_folder = "/root/x/Shell/"
    destination = "liebert:/backup_shell/"
    
    while True:
        print("Menjalankan rclone copy untuk file tertentu...")
        
        for file in files_to_backup:
            source_path = source_folder + file
            subprocess.run(["rclone", "copy", source_path, destination, "--update", "-v"])
            
        print("Menunggu 30 menit sebelum menjalankan ulang...")
        time.sleep(1800)  # 30 menit

# Jalankan fungsi dalam thread terpisah
thread = threading.Thread(target=run_rclone, daemon=True)
thread.start()

# Menjaga script tetap berjalan
while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print("\nDihentikan oleh pengguna.")
        break
