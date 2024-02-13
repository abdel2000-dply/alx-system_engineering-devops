# fix typo phpp
exec { 'fix wp settings':
  command  => "/bin/sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
}
