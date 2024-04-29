# Puppet manifest to kill a process named killmenow if it is running

# Execute pkill command to kill the process named killmenow

exec { 'killmenow':
  command     => '/usr/bin/pkill -f killmenow',
  path        => ['/bin', '/usr/bin'],
  onlyif      => '/usr/bin/pgrep -f killmenow',
}

