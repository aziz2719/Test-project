FROM python:3.9.7
#то с чего начинатся должно все базовый образ питона
ENV PYTHONDONTWRITEBYTECODE 1 
#запрещает Python записывать файлы pyc на диск 
ENV PYTHONUNBUFFERED=1
#запрещает Python буферизовать stdout и stderr

#создание папки
WORKDIR /app
#переход в эту папку
COPY ./requirements.txt .
#копирует файлы и директории в контейнер
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
#из текущей директории . в папку app
COPY . .



#docker build -t digital .
#docker images
#docker run digital
