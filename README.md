# ui-automation-python-playwright

Проект по автоматизации UI-тестирования сайта Sauce Demo с использованием Python, pytest и Playwright.

Проект демонстрирует базовые навыки QA Automation: написание UI-автотестов на Python, запуск тестов через pytest, управление браузером через Playwright, использование Page Object Model, работу с тестовыми фикстурами и оформление тестовой документации.

## Тестируемый сайт

- Сайт: Sauce Demo
- URL: `https://www.saucedemo.com/`

## Стек технологий

- Python
- pytest
- Playwright
- pytest-playwright
- Page Object Model
- Allure Report

## Структура проекта

```text
ui-automation-python-playwright/
    README.md
    requirements.txt
    pytest.ini
    conftest.py
    .gitignore
    pages/
        login_page.py
        inventory_page.py
        cart_page.py
        checkout_step_one.py
    tests/
        test_login.py
        test_inventory.py
        test_cart.py
        test_checkout_one.py
    docs/
        test-plan.md
        checklils.md
        test-cases.md
        bug-reports.md
        test-report.md
    reports/
    screenshots/
```

## Подготовка окружения

Перейдите в папку проекта:

```shell
cd E:\qa_portfolio\ui-automation-python-playwright
```

Создайте и активируйте виртуальное окружение:

```shell
python -m venv .venv
.\.venv\Scripts\activate
```

Если команда `python` не найдена, установите Python и добавьте его в `PATH`, затем пересоздайте `.venv`.

Установите зависимости:

```shell
pip install -r requirements.txt
```

Установите браузеры Playwright:

```shell
playwright install
```

При необходимости можно установить только конкретный браузер:

```shell
playwright install chromium
playwright install firefox
playwright install webkit
```

## Запуск тестов

Запуск всех тестов:

```shell
pytest
```

Запуск конкретного файла:

```shell
pytest tests/test_login.py
```

Запуск конкретного теста:

```shell
pytest tests/test_login.py::test_successful_login
```

Запуск с подробным выводом уже включен в `pytest.ini` через параметр `addopts = -v`.

## Параметры запуска pytest и Playwright

Запуск в видимом браузере:

```shell
pytest --headed
```

Запуск в конкретном браузере:

```shell
pytest --browser chromium
pytest --browser firefox
pytest --browser webkit
```

Запуск в нескольких браузерах:

```shell
pytest --browser chromium --browser firefox --browser webkit
```

Запуск через конкретный канал браузера, например Chrome или Edge:

```shell
pytest --browser chromium --browser-channel chrome
pytest --browser chromium --browser-channel msedge
```

Замедление действий браузера, удобно для отладки:

```shell
pytest --headed --slowmo 500
```

Запуск с эмуляцией устройства:

```shell
pytest --device "iPhone 13"
```

Сохранение скриншотов:

```shell
pytest --screenshot only-on-failure
pytest --screenshot on
pytest --screenshot off
```

Полностраничный скриншот:

```shell
pytest --screenshot only-on-failure --full-page-screenshot
```

Сохранение видео:

```shell
pytest --video retain-on-failure
pytest --video on
pytest --video off
```

Сохранение trace-файлов Playwright:

```shell
pytest --tracing retain-on-failure
pytest --tracing on
pytest --tracing off
```

Папка для артефактов Playwright:

```shell
pytest --output reports/playwright
```

Открытие trace-файла:

```shell
playwright show-trace path/to/trace.zip
```

## Allure Report

Запуск тестов с сохранением результатов Allure:

```shell
pytest --alluredir=reports/allure-results
```

Запуск с очисткой старых результатов Allure:

```shell
pytest --alluredir=reports/allure-results --clean-alluredir
```

Генерация HTML-отчета:

```shell
allure generate reports/allure-results -o reports/allure-report --clean
```

Открытие отчета в браузере:

```shell
allure open reports/allure-report
```

Для генерации HTML-отчета должен быть установлен Allure CLI. Python-пакет `allure-pytest` отвечает только за запись результатов тестов в формате Allure.

## pytest.ini

В проекте настроены базовые параметры pytest:

```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_functions = test_*
addopts = -v
pythonpath = .
```

- `testpaths = tests` - pytest ищет тесты в папке `tests`.
- `python_files = test_*.py` - тестовые файлы должны начинаться с `test_`.
- `python_functions = test_*` - тестовые функции должны начинаться с `test_`.
- `addopts = -v` - подробный вывод при запуске тестов.
- `pythonpath = .` - корень проекта добавлен в путь импорта, поэтому тесты импортируют классы из `pages`.

## Тестовые данные

В `conftest.py` используются тестовые пользователи Sauce Demo:

- `standard_user` - валидный пользователь.
- `locked_out_user` - заблокированный пользователь.
- `invalid_user` / `invalid_password` - невалидные данные.
- Пароль для валидного пользователя: `secret_sauce`.

Базовый URL задан в `conftest.py`:

```python
BASE_URL = "https://www.saucedemo.com/"
```

## Полезные команды

Очистка кеша pytest:

```shell
pytest --cache-clear
```

Запуск с коротким traceback:

```shell
pytest --tb=short
```

Остановка после первого падения:

```shell
pytest -x
```

Повторный запуск только последнего упавшего набора:

```shell
pytest --lf
```

## Какие тесты реализованы

1. Тесты авторизации:
   - [x] Успешная авторизация с валидными данными.
   - [x] Попытка авторизации с заблокированным пользователем.
   - [x] Попытка авторизации с невалидными данными.

2. Тесты страницы товаров:
   - [x]Проверка отображения всех товаров.
   - [x]Проверка сортировки товаров по цене и названию.

3. Тесты страницы корзины:
   - [x] Проверка отображения корзины.
   - [x] Проверка добавления в корзину.
   - [x] Проверка удаления из корзины.
   - [x] Проверка возврата к покупкам.
   - [x] Проверка перехода к оформлению заказа.
   - [x] Проверка бургер-меню.

