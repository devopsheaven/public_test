import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="type1", help="my option: pass or fail"
    )


@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")
