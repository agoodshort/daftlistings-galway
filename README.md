# daftlistings-galway
A python script to search for houses for sales in Galway area and store results in a database.

## Description

The installation steps will help you to install the required bits and to configure it based on your need. 

## Prerequisites

- [wp-cli](https://make.wordpress.org/cli/handbook/) - _If required_
- mySQL/mariaDB
- Python3
  - [daftlistings](https://github.com/AnthonyBloomer/daftlistings)
  - [matplotlib](https://matplotlib.org/)

## Installing

### Disclaimer

- Below I am assuming you have already a database and python3 installed.
- Please consider to run these commands and scripts with appropriate user privileges to directories and files. I recommend either creating a dedicated user or using a user with with required privileges.

### 1. Install python libraries

```shell
pip install daftlistings
pip install matplotlib
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

### 5. Test the script
I recommend at first to run the script to be sure that everything happens as desired.
```shell
./launch.sh
```

### 6. Create a cron job

If the test in step 5. was successful, you can go ahead and automate this script to run everyday to retrieve data.

```shell
crontab -e
```
And add a line in the file with absolute path to the script (ie. below to run my script everyday at 14:00)
```
0 14 * * * /home/pi/GitHub/daftlistings-galway/launch.sh
```

## Extra

### Monitoring your cron jobs for any issues

```shell
grep CRON /var/log/syslog
```

### Install wp-cli

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

## Enhancement 
- [ ] Create a config file to store credential and wordpress location

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

- Special thanks to [AnthonyBloomer](https://github.com/AnthonyBloomer) for the [daftlistings](https://github.com/AnthonyBloomer/daftlistings) library. It seems that the [daft API](https://api.daft.ie/doc/) cannot be used by individuals.
