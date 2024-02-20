# set new limit

file { '/etc/default/nginx':
  ensure  => file,
  content => "ULIMIT=\"-n 10000\"\n",
}

exec { 'restart_nginx':
  command     => 'service nginx restart',
  provider => 'shell',
}
