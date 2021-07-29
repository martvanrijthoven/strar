from functools import lru_cache

from strar.errors import RegistrantNotRegisteredError
from strar.registration import Registrar

cache = lru_cache(maxsize=None)


class RegistrantFactory(Registrar):
    """Factory class for creating instances or retreive object references

    Class Atributes:
        STATIC (bool): Used to create static instances if the instantiation is identical

    Raises:
        RegistrantNotRegisteredError: raised when registrant name is not in the register

    """

    STATIC = False

    @classmethod
    def create(cls, registrant_name: str, return_type: bool = False, *args, **kwargs):
        if cls._REGISTER is None or registrant_name not in cls._REGISTER:
            raise RegistrantNotRegisteredError(
                cls=cls,
                registrant_name=registrant_name,
                register=cls._REGISTER,
            )
        class_type = cls.get_registrant(registrant_name)

        if return_type:
            return class_type

        if cls.STATIC:
            return cls._static_create(class_type, *args, **kwargs)
        return cls._create(class_type, *args, **kwargs)

    @classmethod
    @cache
    def _static_create(cls, class_type, *args, **kwargs):
        return cls._create(class_type, *args, **kwargs)

    @classmethod
    def _create(cls, class_type, *args, **kwargs):
        return class_type(*args, **kwargs)
