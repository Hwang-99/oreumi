import os

folder_path = "C:\\Users\\silr0\\Desktop\\oruemi"

if not os.path.exists(folder_path):
    print(f"폴더 '{folder_path}'가 존재하지 않습니다.")
else:
    print(f"폴더 '{folder_path}'가 존재합니다.")

    