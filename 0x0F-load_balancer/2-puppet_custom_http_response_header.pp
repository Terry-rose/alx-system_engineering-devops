# Puppet manifest to configure Nginx with a custom HTTP response header

# Define a custom HTTP response header
file { '/etc/nginx/conf.d/custom_http_header.conf':
  ensure  => file,
  # Add a custom HTTP response header 'X-Served-By' with the value of the server's hostname
  content => "add_header X-Served-By $::hostname;",
  notify  => Service['nginx'],
}

# Restart Nginx service to apply changes
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => File['/etc/nginx/conf.d/custom_http_header.conf'],
}

