import time
from datetime import datetime

#Начальное время 20:12 
hour = 20
minute = 12

#Конечное время 21:12
finish_hour = 21
finish_minute = 12


start_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, hour, minute)
finish_time= datetime(datetime.now().year, datetime.now().month, datetime.now().day, finish_hour, finish_minute)

#Путь до файла к hosts для Windows
hosts = r'C:/Windows/System32/drivers/etc/hosts'
#Путь до файла к hosts для Linux систем
# hosts = r'/etc/hosts'

redirect_url = '127.0.0.1'

#Список сайтов которые мы ограничиваем
block_sites = ['www.vk.com', 'vk.com']

while True:
    if start_time < datetime.now() > finish_time:
        print('Доступ ограничен')
        with open(hosts, 'r+') as file:
            src = file.read()

            for site in block_sites:
                if site in src:
                    pass
                else:
                    file.write(f'{redirect_url} {site}\n')

    else:
        with open(hosts, 'r+') as file:
            src = file.readlines()
            file.seek(0)

            for line in src:
                if not any(site in line for site in block_sites):
                    file.write(line)
            file.truncate()
        print('Доступ открыт')
    time.sleep(5)
