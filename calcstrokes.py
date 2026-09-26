from strokes import strokes
import csv

output_lines = []
with open('D://neu 2.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row:  # skip empty rows
            print(row[0][0] + ',' + str(strokes(row[0][0])))

            line = row[0][0] + ',' + str(strokes(row[0][0]))
            output_lines.append(line)

with open('D://output.csv', 'w', encoding='utf-8', newline='') as outfile:
    for line in sorted(output_lines, key=lambda line: int(line.split(',')[1])):
        outfile.write(line + '\n')