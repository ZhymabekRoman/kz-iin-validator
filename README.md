[![codecov](https://codecov.io/github/ZhymabekRoman/kz-iin-validator/branch/main/graph/badge.svg?token=MKDYG85FVD)](https://codecov.io/github/ZhymabekRoman/kz-iin-validator)

**kz-iin-validator** - Библиотека для проверки и извлечения данных из ИИН на Python 3. ИИН - это Индивидуальный Идентификационный Номер граждан Республики Казахстан (РК) и юридических лиц РК

## Возможности:
- Production ready библиотека
- Базовая валидация данных ИИН, таких как дата, месяц, год
- Генератор ИИН
- Проверка и валидация хэш суммы ИИН. Алгоритм формирования ИИН регулируется Постановлением правительства РК "Об утверждении Программы перехода на единый номер физического (юридического) лица (индивидуальный идентификационный номер (бизнес-идентификационный номер) в целях создания Национальных реестров идентификационных номеров Республики Казахстан" от 11 июня 2003 года N 565 https://adilet.zan.kz/rus/docs/P030000565_

## Схема формирования ИИН:
<details>
  <summary>Схема</summary>
    <img src="https://raw.githubusercontent.com/ZhymabekRoman/kz-iin-validator/main/images/iin_schema.webp" alt="Schema IIN" />
</details>

## Установка:
```bash
python3 -m pip install git+https://github.com/ZhymabekRoman/kz-iin-validator
```

## Использование:
```python
from kz_iin_validator import validate_iin

validated_iin = validate_iin("061211600012")
```
