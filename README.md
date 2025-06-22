# Программа генерации случайных паролей

Эта программа предназначена для генерации случайных паролей с заданным количеством символов. Пароли могут содержать буквы верхнего и нижнего регистра, цифры и специальные символы.

## Особенности

- Генерация случайных паролей заданной длины.
- Возможность использовать буквы, цифры и специальные символы в паролях.
- Простое и понятное консольное приложение.
- ПУСТО
## Начало работы

Для использования этой программы вам понадобится Python версии 3.6 или выше.

## Запуск тестов

Тесты написаны с использованием библиотеки pytest. Для установки введите:
```bash
pip install pytest
```

Затем вы можете запустить тесты из корневой директории проекта следующей командой:
```bash
pytest
```
# README.MD PAVEL (UPDATE)
## Тесты:
Тест, что при генерации используются только допустимые символы
```bash
def test_password_characters():
valid_characters = string.ascii_letters + string.digits + string.punctuation
password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
for char in password:
    assert char in valid_characters
```

Тест, что проверяет првильную длину
```bash
def test_len():
    password = generate_password(100)
    assert len(password) == 100
```

Тест, что проверяет не повторяемость паролей
```bash
def test_povtorenie():
    password1 = generate_password(10)
    password2 = generate_password(10)
    assert password1 != password2
```

## Автор

Kodland
