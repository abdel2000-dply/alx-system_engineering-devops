# install flask

package { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => '/usr/local/bin:/usr/bin',
  unless  => '/usr/bin/pip3 show Flask | grep -q "Version: 2.1.0"',
  require => Package['python3-pip'],
}
