import time
import re


def convert_file(input_file_name, output_file_name, show_xml = False):
    input_file = open(input_file_name + ".json", 'r', encoding='utf-8')
    output_file = open(output_file_name + ".xml", 'w', encoding='utf-8')
    xml = file_to_xml(input_file)
    output_file.write(xml)
    input_file.close()
    output_file.close()


def file_to_xml(file):
    
    lines = file.readlines()
    lines.pop(0)
    lines.pop(0)
    lines.pop(-1)
    lines.pop(-1)

    tf = True

    xml = "<timetable>\n"
    flag = False

    for i in range(len(lines)):
        row = lines[i]
        
        # print(row)
        key = re.findall(r'\w+', row) #key[0]
        # key = re.findall(r'"\w*":', row)
        value = re.findall(r':.+', row)
        if len(key) == 0 and len(value) == 0:
            key.append('')
            value.append('')
        if len(value) != 0:
            value[0] = re.sub(r': "', '', value[0])
            value[0] = re.sub(r': {', '', value[0])
            if '[' not in value[0] and ']' not in value[0]:
                value[0] = re.sub(r',', '', value[0])
            elif len(value[0]) > 0:
                if value[0][-1] == ',':
                    value[0] = value[0][-1]
            value[0] = re.sub(r'"', '', value[0])
            value[0] = re.sub(r': ', '', value[0])
        print(key, value)
        print(len(key), len(value))

        if len(key[0]) == 0 and len(value[0]) == 0:
            flag = False
            xml += "\t" + f"</{main_key[0]}>\n"

        elif flag:
            xml += "\t" * 2 +  f"<{key[0]}>{value[0]}</{key[0]}>\n"
        elif len(key[0]) > 0 and len(value[0]) == 0:
            xml += "\t" + f"<{key[0]}>\n"
            main_key = key
            flag = True

        elif len(key[0]) > 0 and len(value[0]) > 0:
            xml += "\t" +  f"<{key[0]}>{value[0]}</{key[0]}>\n"
    xml += "</timetable>"

    return xml



start_time = time.perf_counter()
# convert_file('1', '1')
for n in range(10):
    convert_file("1","1")
print(time.perf_counter() - start_time)