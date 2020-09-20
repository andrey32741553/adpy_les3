from datetime import datetime as dt
from adpy_les2.countrylinks_class import CountryLinks
import os

if not os.path.isdir('C:\\logfiles'):
    os.makedirs('C:\\logfiles')


def logging_decorator(path):
    def logging(old_function):
        def new_function(*args, **kwargs):
            extract_old_foo_name = (str(kwargs.get('old_foo_name')).split('.'))[-1].strip(">'")
            date_time = f'Дата и время создания: {dt.today()}'
            foo_name = f'Имя функции создающей лог: {old_function.__name__}'
            old_func_name = f'Имя функции(класса), для которой создаётся лог: {extract_old_foo_name}'
            foo_arguments = f'Аргументы функции:{args}, {kwargs}'
            old_foo_result = old_function(*args, **kwargs)
            for line in old_foo_result:
                print(line)
            with open(path, 'w', encoding='utf-8') as file:
                file.write(
                    date_time + '\n' +
                    '\n' + foo_name + '\n' +
                    '\n' + old_func_name + '\n' +
                    '\n' + foo_arguments + '\n' +
                    '\n' + 'Результат выполнения: ' + '\n'
                )
                for line in old_foo_result:
                    file.write(line + '\n')
            return f'{date_time},\n{foo_name},\n{old_func_name},\n{foo_arguments},\n{old_foo_result}'
        return new_function
    return logging


@logging_decorator('C:\\logfiles\\logfile.txt')
def logging_foo(url, old_foo_name=CountryLinks):
    result_list = []
    result = old_foo_name(url)
    for line in result:
        result_list.append(line)
    return result_list


print(logging_foo(
    'https://raw.githubusercontent.com/mledoze/countries/master/countries.json',
    old_foo_name=CountryLinks))
