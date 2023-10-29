# Spark Changelog

This file is the changelog for Spark.

## Version 0.0.1-alpha-stable

### Added in v0.0.1-alpha-stable

* Printing to the console
* Setting variables
* Reading & Writing to files

### Changed in v0.0.1-alpha-stable

Nothing.

### Removed in v0.0.1-alpha-stable

Nothing.

## Version 0.0.2-alpha-stable

### Added in v0.0.2-alpha-stable

* Deleting files using '#delete_file'

### Changed in v0.0.2-alpha-stable

* File reading keyword changed to '#read_file'
* File writing keyword changed to '#write_file'

### Removed in v0.0.2-alpha-stable

Nothing.

## Version 0.0.3-alpha-stable

### Added in v0.0.3-alpha-stable

* GET requests using '#http_get' (requires 'http' module to be imported)
* 'import' keyword

### Changed in v0.0.3-alpha-stable

* Requiring the 'filesystem' module to be imported to use file operations

### Removed in v0.0.3-alpha-stable

Nothing.

## Version 0.0.4-alpha-stable

### Added in v0.0.4-alpha-stable

* `utils.py` file with general shared utilities.
* `parseArg(arg: str)` function for parsing an argument:
  * If it's a variable, return the variable's value
  * If it's the user input function, get user input
  * Replace '\' with ' '
* Introduce user input

### Changed in v0.0.4-alpha-stable

Nothing.

### Removed in v0.0.4-alpha-stable

Nothing.
