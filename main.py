from datetime import datetime as dt
from adpy_les2.countrylinks_class import CountryLinks
import os

if not os.path.isdir('C:\\logfiles'):
    os.makedirs('C:\\logfiles')

url = 'https://raw.githubusercontent.com/mledoze/countries/master/countries.json'


def path_for_saving(path):
    def logging(old_function):
        def new_function(old_foo_name, *args):
            date_time = f'Дата и время создания: {dt.today()}'
            foo_name = f'Имя функции: {old_function.__name__}'
            foo_arguments = f'Аргументы функции: {old_foo_name}, {args}'
            old_foo_result = old_function(old_foo_name, *args)
            for line in old_foo_result:
                print(line)
            with open(path, 'w', encoding='utf-8') as file:
                file.write(
                    date_time + '\n' +
                    '\n' + foo_name + '\n' +
                    '\n' + foo_arguments + '\n' +
                    '\n' + 'Результат выполнения: ' + '\n'
                )
                for line in old_foo_result:
                    file.write(line + '\n')
            return f'{date_time},\n{foo_name},\n{foo_arguments},\n{old_foo_result}'
        return new_function
    return logging


@path_for_saving('C:\\logfiles\\logfile.txt')
def decorating_function(old_foo_name, *args):
    result_list = []
    result = old_foo_name(*args)
    for line in result:
        result_list.append(line)
    return result_list


print(decorating_function(CountryLinks, url))
