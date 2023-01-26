def id_export(data_line):
    data_list = data_line.split()
    return int(data_list[0])
def id_sorting():
    with open('file.txt', 'r') as f1, open('file_sorted_id.txt', 'w') as f2:
        contains = f1.readlines()
        contains.sort(key=id_export)
        for i in contains:
            f2.write(f'{i}')