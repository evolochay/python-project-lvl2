from gendiff.gendiff import generate_diff
import pytest
import json


def read_file(file_path):
    with open(file_path, 'r') as file:
        result = file.read()
    return result


def test_error():
    with pytest.raises(FileNotFoundError):
        generate_diff('./tests/fixtures/file1.json', 'stylish')


TEST_DATA = [
    ('./tests/fixtures/file1.json', './tests/fixtures/file2.json',
     'stylish', './tests/fixtures/result_stylish.txt'),
    ('./tests/fixtures/file1.yml', './tests/fixtures/file2.yml',
     'stylish', './tests/fixtures/result_stylish.txt'),
    ('./tests/fixtures/file1.json', './tests/fixtures/file2.json',
     'plain', './tests/fixtures/plain_result.txt'),
    ('./tests/fixtures/file1.yml', './tests/fixtures/file2.yml',
     'plain', './tests/fixtures/plain_result.txt')
]


@pytest.mark.parametrize('file1, file2, format, result_path', TEST_DATA)
def test_gendiff(file1, file2, format, result_path):
    result = read_file(result_path)
    assert generate_diff(file1, file2, format) == result


def is_json(json_data):
    try:
        json.loads(json_data)
    except ValueError:
        return False
    return True


@pytest.mark.parametrize('data_file1, data_file2',
                         [('./tests/fixtures/file1.yml',
                           './tests/fixtures/file2.json'),
                          ('./tests/fixtures/file1.json',
                           './tests/fixtures/file1.json')])
                           
def test_gendiff_json(data_file1, data_file2):
    result1 = generate_diff(data_file1, data_file2, 'json')
    result2 = generate_diff(data_file1, data_file2)
    assert is_json(result1) is True
    assert is_json(result2) is False