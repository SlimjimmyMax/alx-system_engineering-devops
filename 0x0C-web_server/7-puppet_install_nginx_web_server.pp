# manifest.pp

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure Nginx
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "# Nginx default configuration\n
              server {\n
                listen 80 default_server;\n
                listen [::]:80 default_server;\n
                root /var/www/html;\n
                index index.html index.htm;\n
                server_name _;\n
                location / {\n
                  try_files \$uri \$uri/ =404;\n
                }\n
                location /redirect_me {\n
                  return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n
                }\n
              }\n",
}

# Create a custom 404 page
file { '/var/www/html/not_found.html':
  ensure  => file,
  content => 'Ceci n\'est pas une page',
}

# Ensure Nginx is running and restart for changes to take effect
service { 'nginx':
  ensure    => running,
  enable    => true,
  require   => File['/etc/nginx/sites-available/default'],
  subscribe => File['/etc/nginx/sites-available/default'],
}
