# Puppet manifest to create a file in /tmp with specific permissions, ownership, and content

# Define a file resource to create the file /tmp/school

file { '/tmp/school':
  ensure   => 'file',
  content  => 'I love Puppet',
  mode     => '0744',
  owner    => 'www-data',
  group    => 'www-data',
}

