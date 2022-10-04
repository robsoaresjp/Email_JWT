from helpers import *


class TestHelpers:
    def test_remove_repeated(self):
        list_1 = [1,2,3,1]
        assert remove_repeated(list_1) == [1,2,3]

    def test_is_none_or_zero(self):
        assert isNoneOrZero(0) == True
        assert isNoneOrZero(None) == True
        assert isNoneOrZero('None') == False
        assert isNoneOrZero('aasdasd') == False

    def test_check_email(self):
        assert check_email('asd@asd.com') == True
        assert check_email('asd') == False

    def test_check_cpf(self):
        assert check_cpf('43268926843') == True
        assert check_cpf('432.689.268-43') == True
        assert check_cpf('111111') == False
        assert check_cpf('asdasd') == False
