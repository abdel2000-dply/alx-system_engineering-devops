# Add a custom HTTP header (on web-01 and web-02)
exec { 'http header':
  command  => 'sudo apt-get update -y && sudo apt-get install nginx -y && sudo sed -i "s/server_name _;/server_name _;\n\tadd_header X-Served-By \"$hostname\";/" /etc/nginx/sites-available/default && sudo service nginx restart',
  provider => shell,
}
