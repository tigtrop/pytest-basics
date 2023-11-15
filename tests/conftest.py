import pytest
import selenium.webdriver
from chromedriver_py import binary_path

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

@pytest.fixture
def browser():

    svc = selenium.webdriver.ChromeService(executable_path=binary_path)
    b = selenium.webdriver.Chrome(service=svc)
    # b = selenium.webdriver.Chrome()
    b.implicitly_wait(10)

    yield b

    b.quit()