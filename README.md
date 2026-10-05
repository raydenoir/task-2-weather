# Погода по городам

## Запуск

Python 3.7+

Поместите `Cities.txt` рядом с `main.py`, запуск:

```sh
python main.py
```

Либо можно передать другой файл аргументом:

```sh
python main.py "my cities.txt"
```

Ожидается один город на строку, пустые строки и повторяющиеся названия пропускаются.

Если погоду для города получить не удалось, выводится сообщение об ошибке, этот город пропускается и не учитывается в статистике.

## Результат выполнения на Cities.txt

```text
Moscow, Russia +14 °C
Khabarovsk, Russia +10 °C
Saint-Petersburg, Russia +12 °C
Vienna, Austria +22 °C
Izhevsk, Russia +7 °C
Perm, Russia +3 °C
NhaTrang, Vietnam +28 °C
Villach, Austria +18 °C

Russia - 5 cities, avg: +9.2 °C, min: +3 °C, max: +14 °C
Austria - 2 cities, avg: +20.0 °C, min: +18 °C, max: +22 °C
Vietnam - 1 cities, avg: +28.0 °C, min: +28 °C, max: +28 °C
```
