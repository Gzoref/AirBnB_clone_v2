#Puppet execute 0
exec {'web_static':
  command  => 'sudo apt-get update && sudo apt-get -y install nginx && sudo service nginx start && sudo mkdir -p /data/ && sudo mkdir -p /data/web_static/ && sudo mkdir -p /data/web_static/releases/ && sudo mkdir -p /data/web_static/shared/ && sudo mkdir -p /data/web_static/releases/test/ && sudo echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html && sudo ln -sf /data/web_static/releases/test/ /data/web_static/current && sudo chown -R ubuntu: /data/ && var="location /hbnb_static {\n alias /data/web_static/current/;\n}\n" && sudo sed -i "43i${{var" /etc/nginx/sites-available/default && sudo service nginx restart',
    provider => 'shell',
}
