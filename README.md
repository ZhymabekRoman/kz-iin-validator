# kz-iin-validator

[![MIT License](https://img.shields.io/pypi/l/kz-iin-validator.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![PyPI version](https://img.shields.io/pypi/v/kz-iin-validator.svg?style=flat-square)](https://pypi.org/project/kz-iin-validator/)
[![PyPI downloads](https://img.shields.io/pypi/dm/kz-iin-validator.svg?style=flat-square)](https://pypi.org/project/kz-iin-validator/)
[![codecov](https://img.shields.io/codecov/c/github/ZhymabekRoman/kz-iin-validator?style=flat-square)](https://app.codecov.io/github/ZhymabekRoman/kz-iin-validator)
[![tests](https://img.shields.io/github/actions/workflow/status/ZhymabekRoman/kz-iin-validator/pytest.yml?branch=main&style=flat-square)](https://github.com/ZhymabekRoman/kz-iin-validator/actions)

**kz-iin-validator** - Библиотека для проверки и извлечения данных из ИИН на Python 3. ИИН - это Индивидуальный Идентификационный Номер граждан Республики Казахстан (РК) и юридических лиц РК

## Возможности:
- Production-ready библиотека
- 100% code coverage - Библиотека полностью покрыта тестами
- Zero-depency - Не требует дополнительных зависимостей
- Базовая валидация данных ИИН, таких как дата, месяц, год
- Генератор ИИН
- Проверка целостности по хэш сумме ИИН. Алгоритм формирования ИИН регулируется Постановлением правительства РК "Об утверждении Программы перехода на единый номер физического (юридического) лица (индивидуальный идентификационный номер (бизнес-идентификационный номер) в целях создания Национальных реестров идентификационных номеров Республики Казахстан" от 11 июня 2003 года N 565 - [Ссылка на источник приказа](https://adilet.zan.kz/rus/docs/P030000565_)

## Требования:
- Python 3.7 и выше * **
> \* судя по информации утилиты Vermin

> ** я могу адаптировать (забэкпортить) библиотеку для более старых версии Python, но стоит ли оно? Если что дайте мне знать

## TODO:
- Реализовать поддержку валидации БИН
- Улучшить документация
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
from kz_iin_validator import safe_validate_iin, validate_iin

iin = "061211600012"
# use kz_iin_validator as in Golang (preferred in production)
validated_iin, error = safe_validate_iin(iin)
# or directly with exceptions raising:
# validated_iin = validate_iin(iin)

print(f"ИИН: {iin}")

# Print IIN owner gender:
print(f"Пол: {validated_iin.gender.name.upper()}")

# Print IIN owner born information:
print(f"День: {validated_iin.born_date.day}")
print(f"Месяц: {validated_iin.born_date.month}")
print(f"Год: {validated_iin.born_date.year}")

# or directly access to datetime object:
# validated_iin.born_date.datetime
```

### Генератор ИИН:
```python
from kz_iin_validator import generate_iin

generated_iin = generate_iin()
print(generated_iin) # return generated valid IIN as string
```

### Извлечь ИИН из текста:
```python
from kz_iin_validator import extract_iin

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit - 251112401047. Aliquam vel diam ac enim consequat rhoncus 700911204362!."

extracted_iin_list = extract_iin(text)
print(extracted_iin_list)
```
