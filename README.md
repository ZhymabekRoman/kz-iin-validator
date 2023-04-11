# kz-iin-validator

[![codecov](https://img.shields.io/codecov/c/github/ZhymabekRoman/kz-iin-validator?style=flat-square)](https://app.codecov.io/github/ZhymabekRoman/kz-iin-validator)
[![tests](https://img.shields.io/github/actions/workflow/status/ZhymabekRoman/kz-iin-validator/pytest.yml?branch=main&style=flat-square)](https://github.com/ZhymabekRoman/kz-iin-validator/actions)

**kz-iin-validator** - Библиотека для проверки и извлечения данных из ИИН на Python 3. ИИН - это Индивидуальный Идентификационный Номер граждан Республики Казахстан (РК) и юридических лиц РК

## Возможности:
- Production-ready библиотека
- 100% code coverage - Библиотека полностью покрыта тестами
- Zero-depency - Не требует дополнительных зависимостей
- Базовая валидация данных ИИН, таких как дата, месяц, год
- Генератор ИИН
- Два варианта валидации: стандратное (по умолчанию) и дополнительно с использованием регулярных выражении (включается через аргумент `weak_fast_check=True`, не рекомендуется к использованию) 
- Проверка целостности по хэш сумме ИИН. Алгоритм формирования ИИН регулируется Постановлением правительства РК "Об утверждении Программы перехода на единый номер физического (юридического) лица (индивидуальный идентификационный номер (бизнес-идентификационный номер) в целях создания Национальных реестров идентификационных номеров Республики Казахстан" от 11 июня 2003 года N 565 - [Ссылка на источник приказа](https://adilet.zan.kz/rus/docs/P030000565_)

## Требования:
- Python 3.7 и выше * **
> \* судя по информации утилиты Vermin

> ** я могу адаптировать (забэкпортить) библиотеку для более старых версии Python, но стоит ли оно? Если что дайте мне знать

## TODO:
- Реализовать поддержку валидации БИН
- Улучшеная документация
- Static type hint using Mypy

## Схема формирования ИИН:
<details>
  <summary>Схема</summary>
    <img src="https://raw.githubusercontent.com/ZhymabekRoman/kz-iin-validator/main/images/iin_schema.webp" alt="Schema IIN" />
</details>

## Установка:
### PyPI:
```bash
python3 -m pip install kz-iin-validator
```
### Из GIT репозиторий:
```bash
python3 -m pip install git+https://github.com/ZhymabekRoman/kz-iin-validator
```

## Использование:
### Валидация ИИН:
```python
from kz_iin_validator import validate_iin

iin = "061211600012"
validated_iin, error = validate_iin(iin)

print(f"ИИН: {iin}")

# Print IIN owner gender:
print(f"Пол: {validated_iin.gender.name.upper()}")

# Print IIN owner born information:
print(f"День: {validated_iin.born_date.day}")
print(f"Месяц: {validated_iin.born_date.month}")
print(f"Год: {validated_iin.born_date.year}")

# or directly access to datetime object:
# validated_iin.born_date._datetime
```

### Генератор ИИН:
```python
from kz_iin_validator import generate_iin

generated_iin = generate_iin()
print(generated_iin) # return generated valid IIN as string
```
