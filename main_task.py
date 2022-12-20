import time


def convert_file(input_file_name, output_file_name, show_xml = False):
    input_file = open(input_file_name + ".json", 'r', encoding='utf-8')
    output_file = open(output_file_name + ".xml", 'w', encoding='utf-8')
    xml = file_to_xml(input_file)
    output_file.write(xml)
    input_file.close()
    output_file.close()
    # if show_xml:
    #     print(xml)


def file_to_xml(file):
    
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


    xml = "<timetable>\n"

    for i in range(len(lines)):
        row = lines[i]
        if "}" in row[0]:
            continue
        if row[0][0] != "\t" and row[1] != '{':
            xml += "\t" + f"<{row[0]}>{row[1]}</{row[0]}>\n"

        elif row[0][0] != "\t" and row[1] == '{':
            xml += "\t" + f"<{row[0]}>\n"

            j = i + 1
            while "}" not in lines[j][0]:
                key = lines[j][0].replace("\t", "")
                value = lines[j][1]
                xml += "\t" * 2 +  f"<{key}>{value}</{key}>\n"
                j += 1
            xml += "\t" + f"</{row[0]}>\n"
            
    xml += "</timetable>"

    return xml



start_time = time.perf_counter()
# convert_file('1', '1')
for n in range(10):
    convert_file("1","1")

print(time.perf_counter() - start_time)