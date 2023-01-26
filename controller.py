import model_imp as imp
import model_exp as exp
import sort_name as sn
import sort_id as si

def controller ():
    end = 0
    while end != 1:
        point = input('Выберите тип операции:\n1 - ввод данных\n2 - поиск по id\n3 - сортировка по имени\n4 - сортировка по id\n5 - вывод имени и фамилии по id\n6 - завершить работу\n')
        if point == '1':
            imp.import_data()
        elif point == '2':
            x = (input('Введите id:'))
            print(' '.join(exp.export(x)[0]))
            # print(exp.export(x))
        elif point == '3':
            sn.name_sorting()
        elif point == '4':
            si.id_sorting()
        elif point == '5':
            y = (input('Введите id:'))
            print(exp.export(y)[0][1],exp.export(y)[0][2])
        elif point == '6':
            end = 1
        else:
            print('такой операции нет!')
