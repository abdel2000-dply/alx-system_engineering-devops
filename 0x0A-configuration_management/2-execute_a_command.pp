# execute a command

exec { 'pkill killmenow':
  command  => '/usr/bin/pkill -f /killmenow'
}
