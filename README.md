# daftlistings-galway
A python script to search for houses for sales in Galway area and store results in a database.

## Description

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Prerequisites

- Python3
- [daftlistings](https://github.com/AnthonyBloomer/daftlistings)
- mySQL/mariaDB
- pip install matplotlib

## Installing

Assuming you have already a database and python3 installed.

### 1. Install the [daftlistings](https://github.com/AnthonyBloomer/daftlistings) library

pip install matplotlib

```
virtualenv env
source env/bin/activate
pip install daftlistings
```

### 2. Clone this repository

```
git clone https://github.com/goodshort/daftlistings-galway.git
```

### 3. Point the scripts to your database
Edit the database.sql with your database location and credentials.

### 4. Edit the script to match your research criteria

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

- Special thanks to [AnthonyBloomer](https://github.com/AnthonyBloomer) for the library as the [daft API](https://api.daft.ie/doc/) seems to not be a suitable solution for individuals.
