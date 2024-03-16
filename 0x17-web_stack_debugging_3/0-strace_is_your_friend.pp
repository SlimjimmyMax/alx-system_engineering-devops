<<<<<<< HEAD
# Fixing Apache returning a 500 error

exec { 'fix error':
  provider => 'shell',
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
=======
# Fixing Apache returning a 500 error

exec { 'fix error':
  provider => 'shell',
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
>>>>>>> fde99bb531be4b1a91450eef3f06cfff154f17f6
}