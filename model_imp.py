def import_words(words):
    with open('file.txt', 'a') as file:
        file.write(f'{words} ')
    file.close
abc = ['id: ','first name: ','second name: ','phone number: ','comments: ']

def import_data():
    for i in range(len(abc)):
        import_words(input(f'{abc[i]}'))
    with open('file.txt', 'a') as file:
            file.write('\n')
    file.close