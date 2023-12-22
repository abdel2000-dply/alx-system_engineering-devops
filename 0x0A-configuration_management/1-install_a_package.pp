# install flask version 2.1.0

package { 'python3.8':
  ensure => '3.8.10',
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

package { 'Werkzeug':
  ensure => '2.1.1',
  provider => 'pip',
  require  => Package['python3-pip'],
}
