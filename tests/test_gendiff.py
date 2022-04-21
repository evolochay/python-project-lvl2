from gendiff.gendiff import generate_diff
import pytest


def read_file(file_path):
    with open(file_path, 'r') as file:
        result = file.read()
    return result


def test_error():
    with pytest.raises(UnboundLocalError):
        generate_diff('./tests/fixtures/file1.json', 'stylish')


TEST_DATA = [
    ('./tests/fixtures/file1.json', './tests/fixtures/file2.json',
     'stylish', './tests/fixtures/result_stylish.txt'),
    ('./tests/fixtures/file1.yml', './tests/fixtures/file2.yml',
     'stylish', './tests/fixtures/result_stylish.txt'),
    ('./tests/fixtures/file1.json', './tests/fixtures/file2.json',
     'plain', './tests/fixtures/plain_result.txt'),
    ('./tests/fixtures/file1.json', './tests/fixtures/file2.json',
     'json', './tests/fixtures/result_json.json'),
    ('./tests/fixtures/file1.yml', './tests/fixtures/file2.yml',
     'plain', './tests/fixtures/plain_result.txt')
]


@pytest.mark.parametrize('file1, file2, format, result_path', TEST_DATA)
def test_gendiff(file1, file2, format, result_path):
    result = read_file(result_path)
    assert generate_diff(file1, file2, format) == result
