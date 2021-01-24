# requirement.txt
import pandas as pd
import numpy as np
import json 

# mount to google drive
from google.colab import drive 
drive.mount("/content/drive") # need input access_token manually

# function to read read_file_path
def read_intents(read_file_path:str)->dict:
    data = json.load(open(read_file_path, "r", encoding="utf8"))
    return data

# import data
file_dict = read_intents(read_file_path = "/content/drive/MyDrive/Colab Notebooks/app_alias_for_housing_v2.json")["data"]
print(type(file_dict)) # log
file_dict # log

# get intents and phrases from file_dict
intents = ["intents, phrases"] # ready list with header
for k, v in file_dict.items():
  intents.append(f"{k.replace(',','，')},{'<br>'.join(v.keys()).replace(',','，').replace('?','？')}")  
print(type(intents)) #log
intents #log 

# function to write list to write_file_path
def write_list (write_file_path:str): 
  with open(write_file_path, 'w') as output:
    for row in intents:
     output.write(str(row) + '\n')
  return

write_list(write_file_path = "/content/drive/MyDrive/Colab Notebooks/intents.txt")
