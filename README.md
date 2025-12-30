# Stablecoins Yield Monitor

Автоматизированная система мониторинга доходности стейблкоинов с отправкой отчётов в Telegram.

## Описание

Приложение собирает данные о доходности стейблкоинов из различных протоколов (DefiLlama API и индивидуальные протоколы) каждый час, сохраняет историю в CSV файлы и отправляет сводные отчёты в Telegram.

## Архитектура

- **Scheduler**: APScheduler для планирования задач
- **Collectors**: Модули сбора данных из различных источников
- **Storage**: CSV файлы для хранения исторических данных
- **Reporting**: Telegram бот для отправки отчётов

## Быстрый старт

### 1. Создание виртуального окружения

```bash
python3.11 -m venv .venv
source .venv/bin/activate  # macOS/Linux
```

### 2. Установка зависимостей

```bash
pip install -r requirements.txt
```

Для разработки (опционально):

```bash
pip install -e ".[dev]"
```

### 3. Настройка окружения

Скопируйте `.env.example` в `.env` и заполните значения:

```bash
cp .env.example .env
```

Обязательные параметры:
- `TELEGRAM_BOT_TOKEN` - токен бота от @BotFather
- `TELEGRAM_CHAT_ID` - ID чата для отправки сообщений

### 4. Запуск локально

```bash
python -m src.main
```

### 5. Запуск в Docker

```bash
# Сборка образа
docker-compose build

# Запуск
docker-compose up -d

# Просмотр логов
docker-compose logs -f
```

## Структура проекта

```
stablecoins_yield_monitor/
├── src/
│   ├── main.py              # Точка входа, scheduler
│   ├── collectors/          # Модули сбора данных
│   │   ├── base.py          # Базовый класс коллектора
│   │   ├── defillama.py     # DefiLlama API клиент
│   │   └── protocols/       # Индивидуальные протоколы
│   ├── models/              # Pydantic модели данных
│   ├── storage/             # Работа с CSV
│   ├── reporting/           # Telegram репортер
│   └── config/              # Конфигурация
├── data/                    # CSV файлы с историей
├── tests/                   # Тесты
└── docker/                  # Docker конфигурация
```

## Следующие шаги

1. Создать Telegram бота через @BotFather и получить токен
2. Получить chat_id (отправить боту сообщение, затем проверить через API)
3. Заполнить `.env` реальными значениями
4. Реализовать коллекторы данных (DefiLlama и протоколы)
5. Реализовать сохранение в CSV
6. Реализовать Telegram репортер
7. Протестировать локально перед деплоем

## Разработка

Проект использует:
- Python 3.11+
- Async/await для всех I/O операций
- Pydantic для валидации данных
- Type hints обязательны
- PEP 8, максимальная длина строки 120 символов

## Лицензия

См. файл LICENSE
