# holbertoon limit user

file { '/etc/security/limits.conf':
  content => "
    holberton hard nofile 8192
    holberton soft nofile 8192
  ",
}
