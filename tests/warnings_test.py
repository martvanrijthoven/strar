from pytest import warns
from strar.registration import Registrar
from strar.utils import Text, chain_functions
from strar.warnings import DuplicateRegistrantNameWarning


class TestWarnings:
    def test_no_replace(self):
        with warns(DuplicateRegistrantNameWarning):

            class A(Registrar):
                AUTO = False
                CONVERT_NAME = lambda x: x
                REPLACE = False

            @A.register(("suba", "suba"))
            class SubA(A):
                pass

        with warns(DuplicateRegistrantNameWarning):

            class A(Registrar):
                AUTO = True
                CONVERT_NAME = lambda x: chain_functions(
                    x, Text.split_capitals_with_underscore, Text.lower
                )
                REPLACE = False

            @A.register(("sub_a",))
            class SubA(A):
                pass

    def test_replace(self):

        with warns(None) as record:

            class A(Registrar):
                AUTO = False
                CONVERT_NAME = lambda x: chain_functions(
                    x, Text.split_capitals_with_underscore, Text.lower
                )
                REPLACE = True

            @A.register(("sub_a",))
            class SubA(A):
                pass

            assert len(record) == 0

        with warns(None) as record:

            class A(Registrar):
                AUTO = False
                CONVERT_NAME = lambda x: x
                REPLACE = True

            @A.register(("suba", "suba"), replace=True)
            class SubA(A):
                pass

        assert len(record) == 0
