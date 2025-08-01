#!/bin/bash
RD="./resources/"
UI_FILE="${RD}/main_window.ui"
PY_FILE="${RD}/main_window.py"
# Генерация py-кода из ui-файла
pyside6-uic "$UI_FILE" -o "$PY_FILE"
# # Данный код запускает конвертирование из ui в py, дополнительно - он добавляет возможность ставить в DoubleSpinBox и "," , и "." 
# # Запускать в терминале bash по команде (переходим в нужную директорию в bash): cd "C:\Users\NotfullinIF\Desktop\Testing_git2\1\репозиторий\frontend\userforms" 
# # И следующая команда: ".\ui_to_py.sh" 
# # На данный момент в скрипте прописана конвертация файлов: y1.ui

#     # Путь к исходному ui-файлу и выходному py-файлу y1
# UI_FILE="y1.ui"
# PY_FILE="y1.py"
# # Генерация py-кода из ui-файла
# pyside6-uic "$UI_FILE" -o "$PY_FILE"
# # Добавляем строку после всех строк import
# sed -i '/^import resources_rc/a \
# \n\
# class CustomDoubleSpinbox(QDoubleSpinBox):\n\    def validate(self, text: str, pos: int) -> tuple[int, str, int]:\n\        text = text.replace(".", ",")\n\        return super().validate(text, pos)\n\    def valueFromText(self, text: str) -> float:\n\        text = text.replace(",", ".")\n\        return float(text)\n\    \n\QDoubleSpinBox=CustomDoubleSpinbox # Ваш дополнительный код здесь!' "$PY_FILE"
# echo "1. Преобразование y1.ui успешно выполнено!"