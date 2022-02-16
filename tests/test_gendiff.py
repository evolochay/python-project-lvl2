import pytest
import json
from fixtures.result_json import EXPECTED_STRING
from gendiff.gendiff import generate_diff


@pytest.fixture
def first_file():
    return 'tests/fixtures/file1.json'


@pytest.fixture
def second_file():
    return 'tests/fixtures/file2.json'


def test1(first_file, second_file):
    assert generate_diff(first_file, second_file) == EXPECTED_STRING