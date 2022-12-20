import time, csv


def convert_file(input_file_name, output_file_name, show_xml = False):
    input_file = open(input_file_name + ".json", 'r', encoding='cp1251')
    csvfile = open('1.csv', 'w', newline='')

    csv_ar = file_to_csv(input_file)


    with open('1.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for elem in csv_ar:
            spamwriter.writerow(elem)

    input_file.close()


def file_to_csv(file):
    
    lines = file.readlines()
    lines.pop(0)
    lines.pop(0)
    lines.pop(-1)
    lines.pop(-1)

    tf = True
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n', '').replace('\"', '')
        if lines[i][-1] == ',':
            lines[i] = lines[i][:-1]
    
    while "%" in lines:
        lines.remove("%")

    for i in range(len(lines)):
        lines[i] = lines[i].replace("\t", "", 2)
        lines[i] = lines[i].split(": ")

    for elem in lines:
        print(elem)

    csv_ar = [["timetable"]]

    for i in range(len(lines)):
        row = lines[i]
        if "}" in row[0]:
            continue
        if row[0][0] != "\t" and row[1] != '{':
            csv_ar.append(['\t', row[0], row[1]])

        elif row[0][0] != "\t" and row[1] == '{':
            csv_ar.append(['\t', row[0]])

            j = i + 1
            while "}" not in lines[j][0]:
                key = lines[j][0].replace("\t", "")
                value = lines[j][1]
                csv_ar.append(["\t", "\t", str(key), str(value)])
                j += 1

    return csv_ar



start_time = time.perf_counter()
for n in range(10):
    convert_file("1","1")

print(time.perf_counter() - start_time)