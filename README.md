# Python Block Sites

![MySenPai](https://pa1.narvii.com/6862/6098ddd3be86e6253a9a2174796bf3fba9c06867r1-500-260_hq.gif)

## Указать начальное и конечное время для блокировки сайта

```py
#Начальное время 20:12 
hour = 20
minute = 12

#Конечное время 21:12
finish_hour = 21
finish_minute = 12

```

## Список сайтов которые хотите заблокировать указывать как с 'www' так и с доменом '.com, .ru и т.д'

```py
block_sites = ['www.vk.com', 'vk.com']
```
## OC

- ### Если используете ос windows то нечего не изменять.
- ### Если используете ос linux-системы то убрать `hosts = r'C:/Windows/System32/drivers/etc/hosts' `.


```py
#Путь до файла к hosts для Windows
hosts = r'C:/Windows/System32/drivers/etc/hosts'
#Путь до файла к hosts для Linux систем
# hosts = r'/etc/hosts'
```

***
![MySenPai](https://pa1.narvii.com/8008/5ff3a5128bf7a511810414eecce8018a7b0a52cer1-500-282_hq.gif)
