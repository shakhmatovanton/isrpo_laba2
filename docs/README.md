# Документация  
---

## 1. Общее описание решения
---

Это учебная библиотека python функций для вычисления площади и периметра геометрических фигур: квадрата и круга. 
Проект включает в себя 2 модуля:
- `square.py` - функции для квадрата
- `circle.py` - функции для круга

Используемые формулы:

| фигура  | периметр | площадь |
|---------|----------|---------- 
| круг    | 2πR      | πR²     |
| квадрат | 4a       | a²      |

## 2. Описание функций
---

### square.py

#### area()

Возвращает площадь квадарата с данной стороной

**пример вызова:**
```
python3
>>> from square import area
>>> area(5)
25
```

#### perimeter()

Возвращает периметр квадрата с данной стороной

**пример вызова:**
```
python3
>>> from square import perimeter
>>> perimeter(5)
20
```

### circle.py

#### area

Возвращает площадь круга данного радиуса

**пример вызова:**
```
python3
>>> from circle import area
>>> area(5)
78.53981633974483
```

#### perimeter

Возвращает длину окружности данного радиуса

**пример вызова:**
```
python3
>>> from circle import perimeter
>>> perimeter(5)
31.41592653589793
```

> [!IMPORTANT]
> Аргумент должен быть положительным числом.

## История изменения проекта с хешами комитов 

c9f9d8d (HEAD -> main) add: add documentation
64d5dd9 feat: add function comment bloks in square.py
26564c6 feat: Add function comment blocks in circle.py
7d6bde6 add: add square.py with functions area and perimeter
6d8a7ac add: add circle.py with functions area and perimeter
d7503c1 add: add docs with readme
677c0cb (origin/main, origin/HEAD) Initial commit














