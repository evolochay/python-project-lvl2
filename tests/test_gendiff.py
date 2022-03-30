from unittest import result
import json
import os
from fixtures.result_json import EXPECTED_STRING
from gendiff.gendiff import generate_diff


def test_json_files():
    assert EXPECTED_STRING == generate_diff(
        './tests/fixtures/file1.json', './tests/fixtures/file2.json', 'stylish')


def test_yaml_files():
    assert EXPECTED_STRING == generate_diff(
        './tests/fixtures/file1.yml', './tests/fixtures/file2.yml', 'stylish')


def read_file(file_path):
    with open(file_path, 'r') as file:
        result = file.read()
    return result


def test_plain_format():
    result = read_file('./tests/fixtures/plain_result.txt')
    print(result)
    assert read_file('./tests/fixtures/plain_result.txt') == generate_diff(
        './tests/fixtures/file1.json', './tests/fixtures/file2.json', 'plain')
