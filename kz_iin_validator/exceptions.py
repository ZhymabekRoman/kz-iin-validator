class IINValidateError(Exception):
    ...


class NonValidIINValue(IINValidateError):
    ...


class IINParseError(IINValidateError):
    ...


class NonActiveIIN(IINValidateError):
    ...


class IncorrectIINChecksum(IINValidateError):
    ...
