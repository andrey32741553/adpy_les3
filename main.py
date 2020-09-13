from datetime import datetime as dt
from countrylinks_class import CountryLinks
import os

if not os.path.isdir('C:\\logfiles'):
    os.makedirs('C:\\logfiles')

url = 'https://raw.githubusercontent.com/mledoze/countries/master/countries.json'


def path_for_saving(path):
    def logging(old_function):
        def new_function():
            date_time = f'Дата и время создания: {dt.today()}'
            foo_name = f'Имя функции: {old_function.__name__}'
            foo_arguments = f'Аргументы функции: {path}'
            old_foo_result = old_function()
            with open(path, 'w', encoding='utf-8') as file:
                file.write(
                    date_time + '\n' +
                    '\n' + foo_name + '\n' +
                    '\n' + foo_arguments + '\n' +
                    '\n' + 'Результат выполнения: ' + '\n'
                )
                for line in old_foo_result:
                    file.write(line + '\n')
        return new_function()
    return logging


@path_for_saving('C:\\logfiles\\logfile.txt')
def decorating_function():
    result = CountryLinks(url)
    return result
