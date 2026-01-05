# Python Serialization Layihəsi

Bu layihə Python serializasiya (serialization) texnologiyalarını öyrənmək üçün nümunələr və tapşırıqlar ehtiva edir.

## Tapşırıq 0: Əsas Serializasiya

### Məqsəd
Python dictionary-lərini JSON formatına çevirmək (serialize) və JSON faylından yenidən dictionary-ə çevirmək (deserialize).

### Fayl
- `task_00_basic_serialization.py`

### Funksiyalar

#### 1. `serialize_and_save_to_file(data, filename)`
Python dictionary-sini JSON formatına çevirir və fayla yazır.

**Parametrlər:**
- `data`: Serializasiya ediləcək Python dictionary-si
- `filename`: Nəticənin yazılacağı JSON faylının adı

**Nümunə:**
```python
data = {"name": "John", "age": 30}
serialize_and_save_to_file(data, 'output.json')
