import pytest
import os
from src.csv_schema.commands.validate_csv import ValidateCsv


def test_it_validates_the_csv_filename(populated_config, mk_valid_csv):
    correct_csv_path = mk_valid_csv('test.csv')
    incorrect_csv_path = mk_valid_csv('testX.csv')

    # Incorrect path with no regex - should pass
    vc = ValidateCsv(incorrect_csv_path, populated_config.path)
    vc.execute()
    assert vc.config.filename.value.regex.value is None
    assert len(vc.errors) == 0

    # Correct path with regex - should pass
    populated_config.filename.value.regex.value = r'^test\.csv$'
    populated_config.save()
    vc = ValidateCsv(correct_csv_path, populated_config.path)
    vc.execute()
    assert len(vc.errors) == 0

    # Incorrect path with with regex - should not pass
    vc = ValidateCsv(incorrect_csv_path, populated_config.path)
    vc.execute()
    assert len(vc.errors) > 0
    assert 'does not match regex' in vc.errors[0]


def test_it_validates_the_headers(populated_config, valid_csv_path, invalid_csv_path):
    vc = ValidateCsv(valid_csv_path, populated_config.path)
    vc.execute()
    assert len(vc.errors) == 0

    vc = ValidateCsv(invalid_csv_path, populated_config.path)
    vc.execute()
    assert len(vc.errors) > 0
    assert 'Required column: "col3" not found.' in vc.errors[0]

def testit_validates_invalid_headers_position_type_value(invalid_position_type_value_populated_config, valid_csv_path):
    vc = ValidateCsv(valid_csv_path, invalid_position_type_value_populated_config.path)
    vc.execute()
    assert len(vc.errors) == 1
    assert 'Position value for column "col2" is not an int.' in vc.errors[0]

def testit_validates_invalid_headers_position_value_lower_than_1(invalid_position_value_lower_than_populated_config, valid_csv_path):
    vc = ValidateCsv(valid_csv_path, invalid_position_value_lower_than_populated_config.path)
    vc.execute()
    assert len(vc.errors) == 1
    assert 'Position value for column "col1" is lower than 1.' in vc.errors[0]

def testit_validates_invalid_headers_position_value_greater_than_size(invalid_position_value_greater_than_populated_config, valid_csv_path):
    vc = ValidateCsv(valid_csv_path, invalid_position_value_greater_than_populated_config.path)
    vc.execute()
    assert len(vc.errors) == 1
    assert 'Position value for column "col2" is greater than header size.' in vc.errors[0]

def testit_validates_invalid_headers_position_values(invalid_position_values_populated_config, valid_csv_path):
    vc = ValidateCsv(valid_csv_path, invalid_position_values_populated_config.path)
    vc.execute()
    assert len(vc.errors) == 2
    assert 'Position value for column "col2" is invalid.' in vc.errors[0]
    assert 'Position value for column "col3" is invalid.' in vc.errors[1]


def test_it_validates_the_data(populated_config, valid_csv_path, invalid_csv_path, mk_csv_file):
    vc = ValidateCsv(valid_csv_path, populated_config.path)
    vc.execute()
    assert len(vc.errors) == 0

    missing_col_value_csv = mk_csv_file(rows=['col1,col2,col3', 'a,b,'])
    vc = ValidateCsv(missing_col_value_csv, populated_config.path)
    vc.execute()
    assert len(vc.errors) > 0
    assert vc.errors[0] == 'Row number: 1, column: "col3", value: "" cannot be null or empty.".'
