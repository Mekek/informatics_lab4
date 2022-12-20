from dict2xml import dict2xml
import json
import time


def convert_file(input_file_name, output_file_name, show_xml = False):
    input_file = open(input_file_name + ".json", 'r', encoding='utf-8')
    output_file = open(output_file_name + ".xml", 'w', encoding='utf-8')
    # xml = file_to_xml(input_file)
    xml = file_to_xml(input_file)
    output_file.write(xml)
    input_file.close()
    output_file.close()
    # if show_xml:
    #     print(xml)


def file_to_xml(file):
    data = json.load(file)
    return dict2xml(data, wrap="all", indent="  ")


start_time = time.perf_counter()
# convert_file('1', '1')
for n in range(10):
    convert_file("1","1")
print(time.perf_counter() - start_time)