import allure
from commons.yaml_utils import load_yaml
from commons.runner_utils import runner
import pytest

@pytest.mark.api
def test_yaml():
    my_var = {}
    data = load_yaml("tests/test_api.yaml")
    allure.title(data['name'])

    for step in data['steps']:
        for k,v in step.items():
            runner(k,v,my_var)