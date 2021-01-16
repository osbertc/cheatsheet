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
file_dict = read_intents(read_file_path = "/content/drive/MyDrive/Colab Notebooks/app_alias_for_housing.json")
print(type(file_dict)) # log
file_dict # log

# get intents and phrases from file_dict
intents = ["intents, phrases"] # ready list with header
temp_file = []
for k,v in file_dict.items():
  temp_file.append(k)   # put intent in temp_file
  for k2 in v.items():
      if (','.join(list(v.keys()))) not in intents and temp_file: # check if duplicate
        temp_file.append(','.join(list(v.keys()))) # put phrases in temp_file
        intents.append(','.join(list(temp_file))) # join intent and phrases
        temp_file.clear() # clear temp_file for next intent
      else:
        break

print(type(intents))  # log
intents  # log

# function to write list to write_file_path
def write_list (write_file_path:str): 
  with open(write_file_path, 'w') as output:
    for row in intents:
     output.write(str(row) + '\n')
  return

write_list(write_file_path = "/content/drive/MyDrive/Colab Notebooks/intents.txt")