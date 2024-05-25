from django_rpyc.server import DjangoRpycService


def test_add_service():

    class MyService:
        pass

    name = "my_service"
    service = MyService

    result = DjangoRpycService.add_service(name, service)

    assert result == service
    assert name in DjangoRpycService.MAPPING
    assert DjangoRpycService.MAPPING[name] == service


def test_get_service_names():

    class MyService:
        pass

    DjangoRpycService.MAPPING.clear()

    name = "my_service"
    service = MyService

    DjangoRpycService.add_service(name, service)

    expected_names = [name]
    obj = DjangoRpycService()
    actual_names = obj.exposed_get_service_names()

    assert actual_names == expected_names


def test_exposed_use_existing_service():
    class MyService:
        pass

    DjangoRpycService.MAPPING.clear()

    name = "my_service"
    service = MyService

    DjangoRpycService.add_service(name, service)

    obj = DjangoRpycService()
    result = obj.exposed_use(name)

    assert isinstance(result, MyService)


def test_exposed_use_nonexistent_service():
    DjangoRpycService.MAPPING.clear()

    name = "nonexistent_service"

    obj = DjangoRpycService()

    try:
        obj.exposed_use(name)
        assert False, "Expected ValueError to be raised"
    except ValueError as e:
        assert str(e) == f"Service {name} not found"
