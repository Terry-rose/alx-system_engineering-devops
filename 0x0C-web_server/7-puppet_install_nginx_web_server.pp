# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}

# Define the default Nginx configuration file
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Create a custom index.html file
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Package['nginx'],
}

# Create a custom 404 page
file { '/var/www/html/404.html':
  ensure  => file,
  content => 'Ceci n\'est pas une page',
  require => Package['nginx'],
}

# Define Nginx server block for redirection
nginx::resource::vhost { 'redirect_me':
  ensure    => present,
  listen_ip => '0.0.0.0',
  listen_port => '80',
  server_name => 'localhost',
  www_root    => '/var/www/html',
  redirect    => 'https://www.example.com',
  redirect_status => 'permanent',
}

