# Car Data Analysis

This repository contains code for analyzing and visualizing car data.

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Testing](#testing)

## Introduction

The Car Data Analysis project provides a framework for analyzing and visualizing vehicle trajectory data. It includes functionality for segmenting the data, filtering segments based on user-defined criteria, and plotting the trajectories.

## Project Structure

The project is structured as follows:

- `main.py`: The main script that utilizes the `VehicleData` class to analyze and plot the data.
- `tests/`: Directory containing unit tests for the project.
- `framework/VehicleData.py`: Python module containing the `VehicleData` class implementation.

## Usage

To use the AMAG Data Analysis project, follow these steps:

1. Clone the repository to your local machine.
	```bash
	git clone https://github.com/mehedi-sust/car-data-analysis.git
	```
2. Install the required dependencies installed .
	```bash
	pip install -r requirements.txt
	```
3. Make sure you have the correct `data.npy` file.
4. Update the file paths in `main.py` to point to your data file. Run `main.py` to analyze and plot the data.
	```bash
	python3 main.py
	```


## Testing

Unit tests are provided to ensure the correctness of the project. The tests can be found in the `tests/` directory. To run the tests, execute the following command:

```bash
python -m unittest discover tests
```