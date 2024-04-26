# Summarizer
При анализе данных мы работаем с большими массивами данных, которые могут содержать различные типы данных, такие как двоичные, числовые, данные о времени и классификационные переменные. Ручной анализ таких фреймов данных неэффективен, и было бы очень полезно получить некоторый статистический обзор фрейма данных.

## Описание задачи
Программа должна использовать фрейм данных pandas в качестве входных данных, выполнить итерацию по каждому столбцу фрейма данных и на основе типа данных столбца создать сводную статистику для каждого и распечатать ее в виде таблицы.
Вычисляемая сводка может включать следующие элементы:
- тип столбца;
- минимальное, максимальное значение;
- среднее, медиана, режим;
- процент нулевых строк;
- дисперсия и стандартное отклонение;
- межквартильный диапазон и коэффициент вариации;
- количество различных значений;

## Ввод
Фрейм данных Pandas и параметры для настройки вывода, например:
- output_type - "markdown", "html" или "xlsx";
- output_filename - имя выводимого файла без расширения(Например: "summarized");
Используется набор данных IRIS (https://archive.ics.uci.edu/ml/datasets/iris) в качестве примера ввода.

## Вывод
Отчет markdown, html или xlsx со сводной статистикой.

## Реализовано
- Проект на python
- Использован ООП-подход
- Решение протестировано
- Добавлен файл README
- Добавлен файл requirements.txt
- Python 3.10.10
- Pandas 2.2.2

## Пример использования
```
# Зададим названия колонок для датафрейма
headers = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
df = pd.read_csv('iris_data.csv', names=headers)

# Инициализируем объект
model = Summarizer(df)
# Вычисляем сведения
model.calc_summary()
# Сохраняем результат
model.output_save()
```