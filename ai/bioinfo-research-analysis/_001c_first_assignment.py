# per lane two reads
# per sample 4 zipped files ( 2 lane * 2 read)
# output 4 files

import os
from pathlib import Path

import patoolib

input_directory = Path("D:\\Output")

file_directories = [
    "L001_R1_001",
    "L001_R2_001",
    "L002_R1_001",
    "L002_R2_001"
]

for file_directory in file_directories:
    with open(input_directory / (file_directory + '.txt'), 'w') as merged_file:
        for file_name in os.listdir(input_directory / file_directory):
            with open(input_directory / file_directory / file_name, 'r') as source_file:
                merged_file.write(source_file.read())
                merged_file.write('\n')
            print('{} file has been merged'.format(file_name))
