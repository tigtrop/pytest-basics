import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--rounding_index",
        action="store",
        default='0',  # Set your default value here
        help="rounding index"
    )

@pytest.fixture
def rounding_index(request):
    return request.config.getoption("--rounding_index")