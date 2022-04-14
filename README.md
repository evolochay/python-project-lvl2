# Gendiff: difference generator

[![Maintainability](https://api.codeclimate.com/v1/badges/aedba14697f620e077a1/maintainability)](https://codeclimate.com/github/foxy-chay/python-project-lvl2/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/aedba14697f620e077a1/test_coverage)](https://codeclimate.com/github/foxy-chay/python-project-lvl2/test_coverage)

[![GitHub Actions Demo](https://github.com/foxy-chay/python-project-lvl2/actions/workflows/github-actions-demo.yml/badge.svg)](https://github.com/foxy-chay/python-project-lvl2/actions/workflows/github-actions-demo.yml)

[![Actions Status](https://github.com/foxy-chay/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/foxy-chay/python-project-lvl2/actions)

## Description:

Educational project.
Gendiff finds and prints difference between two .json or .yml/.yaml files. using and showing the chosen output format: 'plain', 'stylish', 'json'.

## Dependencies

- python 3.6+
- make

## Installation

- Install Poetry into your system. Follow official installation guide for your OS: 
  [Installation Documentation](https://python-poetry.org/docs/#installation)

- Build and install the project into your system
  ```
  make build
  make package-install
  ```

## Usage

### Calling programm:

gendiff --format path/to/file1 path/to/file2

### Calling help information:

gendiff -h

### By default the output format is 'stylish', but it can be changed with --format flag:

gendiff --format plain

### Asciinema step 6

[![asciicast](https://asciinema.org/a/pCTGRWEbRnQwU0kcQVxpAQh66.svg)](https://asciinema.org/a/pCTGRWEbRnQwU0kcQVxpAQh66)

### Asciinema step 7

[![asciicast](https://asciinema.org/a/ofUNnwZDSpmXQZifd2hTU26CY.svg)](https://asciinema.org/a/ofUNnwZDSpmXQZifd2hTU26CY)

### Asciinema step 8

[![asciicast](https://asciinema.org/a/gfxgEpm91xtegA54IZumI8XJ7.svg)](https://asciinema.org/a/gfxgEpm91xtegA54IZumI8XJ7)
