# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 10:18:04 2020

@author: izqui
"""

import os

#C:\Users\izqui\Downloads

folder = r"E:\DOCUMENTOS_DE_TRABAJO\MAESTRIA"


for root, dirs, files in os.walk(folder, topdown=False):
   lista_archivos = []
   for name in files:
      lista_archivos.append(os.path.join(root, name))
      
   lista_carpetas = []
   for name in dirs:
      lista_carpetas.append(os.path.join(root, name)) 
      print(os.path.join(root, name))


folder_name_len = len(folder)
extract_folder_names = [subfolder[folder_name_len +1:] for subfolder in lista_carpetas]
extract_folder_names_filter = [subfolder.upper() for subfolder in extract_folder_names if not subfolder.startswith('.',0)]
extract_folder_names_replace = [subfolder.replace(' ','_') for subfolder in extract_folder_names_filter]
extract_folder_names_replace1 = [subfolder.replace('-','_') for subfolder in extract_folder_names_replace]

extract_files_names = [file[folder_name_len +1:] for file in lista_archivos]
extract_files_names_replace = [subfolder.lower() for subfolder in extract_files_names]
extract_files_names_replace0 = [subfolder.replace(' ','_') for subfolder in extract_files_names_replace]
extract_files_names_replace1 = [subfolder.replace('-','_') for subfolder in extract_files_names_replace0]

lista_carpetas_filer = [subfolder for subfolder in lista_carpetas if not subfolder.startswith('.',folder_name_len+1)]
lista_carpetas_final = [folder + '\\'+ subfolder for subfolder in extract_folder_names_replace1 ]

for original_folder, renamed_folder in zip(lista_carpetas_filer,lista_carpetas_final):
    os.rename(original_folder,renamed_folder)


lista_archivos_final = [folder + '\\'+ file for file in extract_files_names_replace1 ]

for original_file, renamed_file in zip(lista_archivos,lista_archivos_final):
    os.rename(original_file,renamed_file)