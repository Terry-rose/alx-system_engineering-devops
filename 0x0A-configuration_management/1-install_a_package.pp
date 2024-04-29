# Puppet manifest to install Flask from pip3 with a specific version (2.1.0)

# Install python3-pip package

package { 'python3-pip':
  ensure => installed,
}

# Execute pip3 command to install Flask version 2.1.0

exec { 'install_flask':
  command     => '/usr/bin/pip3 install Flask==2.1.0',
  path        => ['/bin', '/usr/bin'],
  environment => [],
  unless      => '/usr/bin/pip3 show Flask | grep -q "Version: 2.1.0"',
  require     => Package['python3-pip'],
}

