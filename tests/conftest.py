import pytest
import selenium.webdriver
import json

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
def config(scope='session'):
    with open('../config.json') as config_file:
        config = json.load(config_file)

    assert config['browser'] in ["Chrome", "Firefox", "Headless Chrome"]
    assert isinstance(config['implicitly_wait'], int)
    assert config['implicitly_wait'] > 0

    return config

@pytest.fixture
def browser(config):

    if config['browser'] == 'Firefox':
        b = selenium.webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome()
    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        b = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f'The "{config['browser']}" browser is not supported.')

    b.implicitly_wait(config['implicitly_wait'])

    yield b

    b.quit()