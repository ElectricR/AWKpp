from zipfile import ZipFile
import argparse
import random
import math
import statistics
import csv
from io import TextIOWrapper
from itertools import islice
from pprint import pprint

parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()

with open(args.filename) as program_file:
    arch_file = program_file.readline().strip()
    predicate = ' and '.join(filter(lambda x: x.strip() != '', program_file.read().strip().split('\n')))
    with ZipFile(arch_file) as zf:
        csv_file_name = arch_file[:-4]
        with zf.open(csv_file_name) as input_file, open("output.csv", 'w', encoding='utf-8') as output_file:
            reader = csv.DictReader(TextIOWrapper(input_file, 'utf-8'))
            writer = csv.DictWriter(output_file, fieldnames=reader.fieldnames)
            writer.writeheader()
            for row in reader:
                if eval(predicate):
                    writer.writerow(row)
