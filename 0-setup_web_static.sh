#!/usr/bin/env bash
# task 00
sudo apt-get -y install nginx
mkdir -p /data
mkdir -p /data/web_static
mkdir -p /data/web_static/releases
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test
printf "<html>
            <head>
            </head>
            <body>
            Holberton School
            </body>
    </html>" > /data/web_static/releases/test/index.html
FILE=/data/web_static/current
if [ -f "$FILE" ]
then
    rm /data/web_static/current
    ln -s /data/web_static/releases/test/ /data/web_static/current
else
    ln -s /data/web_static/releases/test/ /data/web_static/current
fi
chgrp -R ubuntu /data/
chown -R ubuntu /data/
sudo tee /etc/nginx/sites-available/default > /dev/null <<EOF
server {
        listen 80;
        listen [::]:80;
        server_name Holbi.com;
        root /var/www/html;
        index index.html;
        location / {
                 try_files $uri $uri/ =404;
                add_header X-Served-By 03-web-01;
        }

        location /hbnb_static/ {
                alias /data/web_static/current/;
                autoindex off;
        }
}
EOF
sudo service nginx restart