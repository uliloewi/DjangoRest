from strokes import strokes
import csv

output_lines = []

def get_unihan_code(char: str) -> str:
    # Get the decimal unicode value and convert it to uppercase Hex
    code_point = ord(char)
    return f"{code_point:04X}"

with open('D://siangxin.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row:  # skip empty rows
            print(row[0][0] + ',' + str(strokes(row[0][0])) + ',' + str(get_unihan_code(row[0][0])))

            line = row[0][0] + ',' + str(strokes(row[0][0])) + ',' + str(get_unihan_code(row[0][0]))
            output_lines.append(line)

with open('D://sh-output.csv', 'w', encoding='utf-8', newline='') as outfile:
    for line in sorted(output_lines, key=lambda l: (int(l.split(',')[1]), int(l.split(',')[2], 16))):
        outfile.write(line + '\n')