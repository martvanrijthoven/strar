from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class RegistrantNotRegisteredError(Exception):
    """Raised when registrant name does not exist in the register"""

    cls: type
    registrant_name: str
    register: Optional[dict]

    def __post_init__(self):
        super().__init__(self._message())

    def _message(self):
        if self.register is None:
            return self._empty_register_message()
        return self._register_name_not_found_message()

    def _prefix_message(self):
        return f"Registrant name '{self.registrant_name}' is not found in the register of class '{self.cls.__name__}'"

    def _empty_register_message(self):
        return f"""
        {self._prefix_message()} with an empty register.
        """

    def _register_name_not_found_message(self):
        return f"""
        {self._prefix_message()} with registrant names {tuple(self.register.keys())}.
        """
