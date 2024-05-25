from django_rpyc.decorators import register
from django_rpyc.server import DjangoRpycService


def test_register_with_name():
    @register("my_service")
    class MyService:
        pass

    assert "my_service" in DjangoRpycService.MAPPING
    assert DjangoRpycService.MAPPING["my_service"] == MyService


def test_register_without_name():
    @register
    class MyService:
        pass

    assert "myservice" in DjangoRpycService.MAPPING
    assert DjangoRpycService.MAPPING["myservice"] == MyService


def test_register_with_non_string_name():
    @register(123)
    class MyService:
        pass

    assert "myservice" in DjangoRpycService.MAPPING
    assert DjangoRpycService.MAPPING[123] == MyService


def test_register_with_name_printing(capfd):
    @register("my_service")
    class MyService:
        pass

    captured = capfd.readouterr()
    assert "Registered: Name: my_service, Class: MyService" in captured.out


def test_register_without_name_printing(capfd):
    @register
    class MyService:
        pass

    captured = capfd.readouterr()
    assert "Registered: Name: myservice, Class: MyService" in captured.out


def test_register_with_non_string_name_printing(capfd):
    @register(123)
    class MyService:
        pass

    captured = capfd.readouterr()
    assert "Registered: Name: 123, Class: MyService" in captured.out
