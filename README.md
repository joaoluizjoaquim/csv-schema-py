# CSV Schema Definition and Validation

## Install

```bash
pip install csv-schema
```

## Usage
```text
usage: csv-schema [-h] [--version] {validate-config,validate-csv,generate-config} ...

CSV Schema

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit

Commands:
  {validate-config,validate-csv,generate-config}
    validate-config     Validates the CSV schema JSON configuration file.
    validate-csv        Validates a CSV file against a schema.
    generate-config     Generate a CSV schema JSON configuration file.

```

# Definition

The CSV file schema definition is defined in a JSON file in the following format.

## File Definition:

```json
{
  "name": null,
  "description": null,
  "filename": {
    "regex": null
  },
  "columns": []
}
```
| Property | Description |
| -------- | ----------- |
| name | The name of the schema. |
| description | The description of the schema. |
| filename | Properties for the name of the CSV filename to validate. |
| columns | List of column definitions. |


### filename
```json
{
  "regex": null
}
```
| Property | Description |
| -------- | ----------- |
| regex | Regular expression to validate the name of the CSV file being validated. |

## Column Definitions:

### string
```json
{
  "type": "string",
  "name": null,
  "required": true,
  "null_or_empty": false,
  "regex": null,
  "min": null,
  "max": null
}
```
| Property | Description |
| -------- | ----------- |
| type | The column type. |
| name | The name of the column. |
| required | Whether or not the column is required in the file. |
| null_or_empty | Whether or not the value can be null (missing) or an empty string. |
| regex | Regular expression to validate the column value. |
| min | The minimum length of the string. null for no limit. |
| max | The maximum length of the string. null for no limit. |

### integer
```json
{
  "type": "integer",
  "name": null,
  "required": true,
  "null_or_empty": false,
  "regex": null,
  "min": null,
  "max": null
}
```
| Property | Description |
| -------- | ----------- |
| type | The column type. |
| name | The name of the column. |
| required | Whether or not the column is required in the file. |
| null_or_empty | Whether or not the value can be null (missing) or an empty string. |
| regex | Regular expression to validate the column value. |
| min | The minimum value. null for no limit. |
| max | The maximum value. null for no limit. |

### decimal
```json
{
  "type": "decimal",
  "name": null,
  "required": true,
  "null_or_empty": false,
  "regex": null,
  "min": null,
  "max": null,
  "precision": 2
}
```
| Property | Description |
| -------- | ----------- |
| type | The column type. |
| name | The name of the column. |
| required | Whether or not the column is required in the file. |
| null_or_empty | Whether or not the value can be null (missing) or an empty string. |
| regex | Regular expression to validate the column value. |
| min | The minimum value. null for no limit. |
| max | The maximum value. null for no limit. |
| precision | The decimal point precision. |

### enum
```json
{
  "type": "enum",
  "name": null,
  "required": true,
  "null_or_empty": false,
  "values": []
}
```
| Property | Description |
| -------- | ----------- |
| type | The column type. |
| name | The name of the column. |
| required | Whether or not the column is required in the file. |
| null_or_empty | Whether or not the value can be null (missing) or an empty string. |
| values | Fixed set of constants. |

## Development

### Setup

```bash
pipenv --three
pipenv shell
make pip_install
make build
make install_local
```
See [Makefile](Makefile) for all commands.

### Update README Definitions
The schema definition is auto generated by running `scripts/generate_md_help.py`.
Copy/paste the output into the README.md file.

### Testing

- Create and activate a virtual environment:
- Run the tests: `make test`
