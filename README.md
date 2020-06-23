# daftlistings-galway
A python script to search for houses for sales in Galway area and store results in a database.

## Description

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Prerequisites

- mySQL/mariaDB
- [wp-cli](https://make.wordpress.org/cli/handbook/)
- Python3
  - [daftlistings](https://github.com/AnthonyBloomer/daftlistings)
  - [matplotlib](https://matplotlib.org/)

## Installing

Assuming you have already a database and python3 installed.

### 1. Install python libraries

```shell
pip install daftlistings
pip install matplotlib
```

### 2. Install wp-cli

```shell
# Download
curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar

# Check if it works
php wp-cli.phar --info

# Move wp-cli to your PATH
chmod +x wp-cli.phar
sudo mv wp-cli.phar /usr/local/bin/wp

# Check if everything is okay
wp --info
```

### 2. Clone this repository

```shell
git clone https://github.com/goodshort/daftlistings-galway.git
cd daftlistings-galway/
```

### 3. Create the database and tables
```shell
mysql -u <username> -p < database.sql
```

### 4. Add your credentials for database connection
Edit [search_and_write_to_db.py](search_and_write_to_db.py) and [plot_results.py](plot_results.py) with your database credentials.

### 5. Run the script

### To finish

## Enhancement 
- [ ] Create a config file to store credential and wordpress location

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

- Special thanks to [AnthonyBloomer](https://github.com/AnthonyBloomer) for the [daftlistings](https://github.com/AnthonyBloomer/daftlistings) library. It seems that the [daft API](https://api.daft.ie/doc/) cannot be used by individuals.
