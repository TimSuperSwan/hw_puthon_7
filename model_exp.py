def export (id):
    with open('file.txt','r') as file:
        contens = file.readlines()
        split_contens = list(map(lambda x: x.split(), contens))
        result = list(filter(lambda x: str(id) in x[0],split_contens))
        return result
        # return ' '.join(result[0])
        # print(' '.join(result[0]))

# print(export(8))