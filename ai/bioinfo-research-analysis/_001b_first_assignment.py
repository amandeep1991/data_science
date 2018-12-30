# per lane two reads
# per sample 4 zipped files ( 2 lane * 2 read)
# output 4 files

import os
from pathlib import Path

import patoolib

# parent_directory = Path("C:\\ML\\research-data\\PTB-MOS 20180711_NIBMG\\Project_AHFKL3BCX2")
input_directory = Path("D:\\Output")

file_directories = [
    input_directory / "L001_R1_001",
    input_directory / "L001_R2_001",
    input_directory / "L002_R1_001",
    input_directory / "L002_R2_001"
]

for file_directory in file_directories:
    for file_name in os.listdir(file_directory):
        original_file_name = file_directory / file_name
        index_for_first_hypen = file_name.index('-')
        new_file_name = file_directory /  (file_name[:index_for_first_hypen].zfill(3) + file_name[index_for_first_hypen:])
        os.rename(str(original_file_name), str(new_file_name))
