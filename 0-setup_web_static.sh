#!/usr/bin/env bash
# Set up your web servers for the deployment of web_static

sudo apt-get update
sudo apt-get install -y nginx
sudo mkdir -p /data/web_static/{releases/test,shared}
sudo touch /data/web_static/releases/test/index.html
sudo chmod go+w /data/web_static/releases/test/index.html
echo "<html>
	<head>
	</head>   
	<body>    
		<h1>Test deployment</h1> 
	</body> 
</html>" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
echo "server {         
	listen 80;
	listen [::]:80 default_server;
	root /var/www/html;
	add_header X-Served-By 172670-web-01; 
	index  index.html;
	location /redirect_me {
		return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;               }      
	error_page 404 /error.html;
	location /404 { 
		root /var/www/html/;
		internal;
	}       
	location /hbnb_static/ {
		alias /data/web_static/current/;
	} 
}" > /etc/nginx/sites-available/default
sudo service nginx restart
