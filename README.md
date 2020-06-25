# daftlistings-galway
A python script to search for houses for sale in the Galway area and store results in a database locally.

## Description

This repo will assist you to review the Galway house market by retrieve data daily from [daft.ie](https://www.daft.ie), plotting the result and automatically importing to your WordPress media library.

The plot image will be copied directly to your upload folder. This allows you to create a page that will be automatically updated with the latest plot by add content to your post using the image block retrieve the picture from the URL. I have added [additional installation steps](https://github.com/goodshort/daftlistings-galway#install-wp-cli) if you would like to import your image using [wp-cli](https://make.wordpress.org/cli/handbook/).

You will find a live example on this [page](https://www.goodshort.me/projects/daftlinstings-galway). You will find as on this page a raw data table generated via the [WordPress Tables pluggin](https://wordpress.org/plugins/wptables/).

The installation steps will help you to install the required bits and to configure it based on your need. 

## Prerequisites

- mySQL/mariaDB
- Python3
  - [daftlistings](https://github.com/AnthonyBloomer/daftlistings)
  - [matplotlib](https://matplotlib.org/)

## Installing

### Disclaimer

- Below I am assuming you have already a database and python3 installed.
- Please consider to run these commands and scripts with appropriate user privileges to directories and files. I recommend either creating a dedicated user or using a user with with required privileges.
- The script below copies the plot directly in your `wp-content/uploads/` directory. This allows to use the same URL to point to the picture within your post.

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

### 4. Edit the scripts with your config
Edit [search_and_write_to_db.py](search_and_write_to_db.py) and [plot_results.py](plot_results.py) with your database credentials.

Edit [launch.sh](launch.sh) with the correct location of your WordPress installation and repo's location.

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
And add a line at the bottom of the file with absolute path to the script (ie. below to run my script everyday at 14:30)
```
30 14 * * *  /home/pi/GitHub/daftlistings-galway/launch.sh > /home/pi/GitHub/daftlistings-galway/cron.log 2>&1
```

## Extra

### Monitoring your cron jobs for any issues

If you created your cron job following the step above, you can view the log generated to troubleshoot with the command below:

```shell
less /home/pi/GitHub/daftlistings-galway/cron.log
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
