#!/bin/bash

echo "# 1.Setting variables to correct directory"
# Edit variables to match your directories location
DAFTLISTINGS='/home/pi/GitHub/daftlistings-galway'
WORDPRESS='/var/www/html/wordpress' # Main WordPress directory
echo "DAFTLISTINGS directory = " $DAFTLISTINGS
echo "WORDPRESS directory = " $WORDPRESS

echo "# 2.Running search_and-write_to_db.py"
python3 $DAFTLISTINGS/search_and_write_to_db.py

echo "# 3.Running plot_results.py"
python3 $DAFTLISTINGS/plot_results.py

# Uncomment/comment the desired step 4.
echo "# 4.Importing plot to wordpress using simple cp command"
cp $DAFTLISTINGS/price_average.png $WORDPRESS/wp-content/uploads/2020/06/

# echo "# 4. Importing plot to wordpress using wp-cli"
# sudo wp media import $DAFTLISTINGS/price_average.png --allow-root
