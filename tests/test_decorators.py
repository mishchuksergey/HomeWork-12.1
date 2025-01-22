import pytest

from src.decorators import log


def test_log():
    """Тест декоратора при выводе информации в указанный файл."""

    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y

    with open("logs/mylog.txt") as file:
        message = file.read()
        assert message == "my_function ok\n"


def test_log_console(capsys):
    """Тест декоратора при выводе информации в консоль."""

    @log()
    def my_function(x, y):
        return x + y

    my_function(6, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


def test_log_err():
    """Тест обработки исключений"""

    @log()
    def my_function():

        with pytest.raises(Exception, match="Exception"):
            my_function()
