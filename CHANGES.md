CHANGES
===============

kz-iin-validator 0.7.0
-----------

### Changes between 0.6.0 and 0.7.0
 * `weak_fast_check` argument from functions `validate_iin` and `safe_validate_iin` was removed
 * IIN extractor from text was implemented in function `extract_iin`.

kz-iin-validator 0.6.0
-----------

### Changes between 0.5.0 and 0.6.0
 * Function `validate_iin` was renamed to `safe_validate_iin`
 * Private function `_validate_iin` was renamed to `validate_iin`
 * Private property `_datetime` was renamed to `datetime`
 * Argument `raise_exception=False` from `safe_validate_iin` was deleted
 * Fix typos: `lenght` to `length`
 * Minor fixes
