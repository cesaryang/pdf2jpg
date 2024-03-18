import os
from pdf2image import convert_from_path
from PIL import Image

# 删除已存在的pic目录
if os.path.exists('./pic'):
    os.system('rm -r ./pic')

# 创建新的pic目录
os.mkdir('./pic')

# 获取当前目录下所有pdf文件
pdf_files = [file for file in os.listdir('.') if file.endswith('.pdf')]

# 转换pdf文件为jpg格式并保存在pic目录下
for pdf_file in pdf_files:
    pages = convert_from_path(pdf_file, 150)
    for i, page in enumerate(pages):
        page.save(f'./pic/{pdf_file}_{i+1}.jpg', 'JPEG', quality=80)