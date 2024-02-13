# Install nginx with puppet
package { 'nginx':
  ensure => 'installed',
}


file { '/var/www/html/index.html':
  ensure  => 'file',
  content => 'Hello World!',
  mode    => '0644',
  require => Package['nginx'],
}

exec { 'append_redirect_me':
  command => "/usr/bin/sed -i '/^}$/i \\\n\tlocation \\/redirect_me {return 301 https:\\/\\/www.youtube.com\\/watch?v=QH2-TGUlwu4;}' /etc/nginx/sites-available/default",
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}
