import glob
import os

current_path = os.path.abspath(__file__)
print(current_path)

pdf_files = glob.glob('C:\\Users\\Silr0\\Desktop\\**\\*.pdf',recursive=True)

for pdf_file in pdf_files:
    print(pdf_file)