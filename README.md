# FakeP300
* Программа эмулирует получение сигнала о [P300](https://en.wikipedia.org/wiki/P300_(neuroscience)) при нажатии клавиши Enter в консоли

# Директории проекта
* .idea - информация для IDE (TODO добавить в .gitignore)
* src - содержит исходные коды модулей, подробнее будет рассмотрено далее
* venv - виртуальное окружение, содержит информацию о подключённых библиотеках в проекте

## Директория src
* [main.py](https://github.com/CatLearned/FakeP300/blob/master/src/main.py) - инициализирует синхронный сокет для отправки информации и ожидает нажатие

### [src/main.py](https://github.com/CatLearned/FakeP300/blob/master/src/main.py)
Параметры:

`host = 'localhost'` - IP адрес на который производить отправку, должен соответствовать значениям в проекте [StimulusPresentation](https://github.com/CatLearned/StimulusPresentation)

`port = 9000` - Порт на который отправлять, должен соответствовать значениям в проекте [StimulusPresentation](https://github.com/CatLearned/StimulusPresentation)

# Как работать с программой?
Описано в [Readme.md проекта StimulusPresentation](https://github.com/CatLearned/StimulusPresentation/blob/master/README.md)
