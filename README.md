# ui-automation-python-playwright
Проект по автоматизации UI-тестирования с использованием Python, pytest и Playwright.

# UI Automation Testing with Python and Playwright

Этот репозиторий содержит учебный проект по автоматизации UI-тестирования сайта Sauce Demo.

Проект демонтрирует базовые навыки QA Automation: написание автотестов на Python, запуск тестов через pytest, управление браузером через Playwright, использование Page Object Model и оформление тестовой документации.

## Тестируемый сайт

- Сайт: Sauce Demo
- URL: https://www.saucedemo.com/

## Стек технологий

- Python
- pytest
- Playwright
- Page Object Model
- Allure Report


## Структура проекта
```text
ui-automation-python-playwright/
    README.md
    requirements.txt
    pages/
        inventory_page.py
        login_page.py
    tests/
        test_inventory.py
        test_login.py
    test_data/
    docs/
    pytest.ini
    .gitignore
```

## Установка зависимостей

```text 
pip install -r requirements.txt
```
## Установка браузеров Playwright

```text
playwright install
```

## Цель проекта

Показать умение создавать простые, понятные и поддерживаемые UI-автотесты для веб-приложения.
В проекте будут использоваться автоматические проверки UI-сценариев, тестовые данные, Page Object Model и базовая тестовая документация.