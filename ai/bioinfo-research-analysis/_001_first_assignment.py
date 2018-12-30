# per lane two reads
# per sample 4 zipped files ( 2 lane * 2 read)
# output 4 files

import os
from pathlib import Path

import patoolib

parent_directory = Path("C:\\ML\\research-data\\PTB-MOS 20180711_NIBMG\\Project_AHFKL3BCX2")
output_directory = Path("D:\\Output")

zip_file_extraction_property = {
    "L001_R1_001.fastq.gz": output_directory / "L001_R1_001",
    "L001_R2_001.fastq.gz": output_directory / "L001_R2_001",
    "L002_R1_001.fastq.gz": output_directory / "L002_R1_001",
    "L002_R2_001.fastq.gz": output_directory / "L002_R2_001"
}

os.chdir(parent_directory)


def extract_files():
    for sample_directory in os.listdir('.'):
        path_url = parent_directory / sample_directory
        if path_url.is_dir():
            for file_name in os.listdir(path_url):
                output_directory = zip_file_extraction_property.get(file_name[-20:], None)
                if output_directory:
                    patoolib.extract_archive(str(parent_directory / sample_directory / file_name), outdir=output_directory, verbosity=-1)


extract_files()
