# Домашнее задание к лекции #4 «Select-запросы, выборки из одной таблицы»
# Задание 2
# Написать SELECT-запросы, которые выведут информацию согласно инструкциям ниже.
# Внимание! Результаты запросов не должны быть пустыми (учтите при заполнении таблиц).
# Результатом работы будет 3 файла (с INSERT, SELECT запросами и CREATE запросами из предыдущего задания)
# в формате .sql (или .py/.ipynb, если вы будете писать запросы с использованием SQLAlchemy).
# 3 блок с SELECT запросами
import sqlalchemy


if __name__ == '__main__':
    db = 'postgresql://postgres:admin@localhost:5432/py49db'
    engine = sqlalchemy.create_engine(db)
    connection = engine.connect()
    # fff = 327
    # print(track_time(fff))


    # 1. название и год выхода альбомов, вышедших в 2018 году;
    sel = connection.execute("""
    SELECT album_name, album_year FROM album WHERE album.album_year = 2018;
    """).fetchall()
    print(f'1. Альбомы 2018 года выпуска:\n{sel}')

    # 2. название и продолжительность самого длительного трека;
    sel = connection.execute("""
    SELECT track_name, to_char(concat(track_time)::interval,'MI:SS') 
    FROM track ORDER BY track.track_time DESC LIMIT 1;
    """).fetchall()
    print(f'2. Самый длинный трек:\n{sel}')


    # 3. название треков, продолжительность которых не менее 3,5 минуты;
    sel = connection.execute("""
    SELECT track_name, to_char(concat(track_time)::interval,'MI:SS') 
    FROM track WHERE track.track_time >= 210;
    """).fetchall()
    print(f'3. Треки, продолжительность которых более 3,5 минуты:\n{sel}')


    # 4. названия сборников, вышедших в период с 2018 по 2020 год включительно;
    sel = connection.execute("""
    SELECT * FROM collection WHERE collection.collection_year between 2018 and 2020;
    """).fetchall()
    print(f'4. Сборники, вышедшие в период с 2018 по 2020 годы:\n{sel}')

    # 5. исполнители, чье имя состоит из 1 слова;
    sel = connection.execute("""
    SELECT * FROM artist WHERE artist.name NOT LIKE '%% %%';
    """).fetchall()
    print(f'5. Исполнители, чье имя состоит из 1 слова:\n{sel}')


    # 6. название треков, которые содержат слово "мой"/"my".
    sel = connection.execute("""
    SELECT * FROM track WHERE UPPER(track.track_name) like '%%MY%%' OR track.track_name like '%%МОЙ%%';
    """).fetchall()
    print(f'6. Название треков, которые содержат слово "мой"/"my":\n{sel}')


