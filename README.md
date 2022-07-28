# mail-service
Сервис по рассылке
## Установка и запуск
Установите все зависимости командой   
```pip install -r req.txt```  

Затем выполните миграции командой  
```yoyo apply --database postgresql://user:password@host:port/database ./migrations```

Запуск приложения командой  
```python app/main.py```
