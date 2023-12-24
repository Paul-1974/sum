# Начнём с образа ubuntu
FROM ubuntu
# Задаём переменную окружения, чтобы пользователь не
#участвовал в установке (выбор клавиатуры и прочее)
ENV DEBIAN_FRONTEND=noninteractive
# Копируем исполняемый файл в контейнер
COPY sum.py /sum.py
# Установим необходимые пакеты
RUN apt update
RUN apt install -y python3.10 
RUN apt install -y vim
RUN chmod +x /sum.py
#RUN python3.10 /sum.py
# Зададим стартовую команду для контейнера
CMD ["bash"]
