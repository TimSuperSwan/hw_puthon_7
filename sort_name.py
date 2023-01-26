def name_export(data_line):
    data_list = data_line.split()
    return data_list[1]
def name_sorting():
    with open('file.txt', 'r') as f1, open('file_sorted_name.txt', 'w') as f2:
        contains = f1.readlines()
        contains.sort(key=name_export)
        # print(contains)
        for i in contains:
            f2.write(f'{i}')


