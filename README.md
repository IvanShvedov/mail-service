# mail-service
Сервис по рассылке
## Установка и запуск
Установите все зависимости командой   
```pip install -r req.txt```  

Затем выполните миграции командой  
```yoyo apply --database postgresql://user:password@host:port/database ./migrations```

Запуск приложения командой  
```python app/main.py```

## Тест API
Есть заготовленные запросы в папке api_test 

## Что сделано
Create, Update, Delete с клиентами и рассылками
