<h1>Как сделать доступным веб-сервер на компьютере доступным извне (через IP адрес вашего роутера)</h1>
<p>1.)Укажите в файлах конфигурации хост сервера 0.0.0.0 и  порт 8000</p>
<p>2.)Наберите в адресной строке браузера адрес "192.168.0.1". Это адрес роутера в вашей локальной сети</p>
<p>3.)Войдите в панель администратора вашего роутера</p>
<p>4.)Зайдите в раздел "проброс портов"</p>
<p>5.) В поле IP адрес укажите адрес вашего компьютера в локальной сети. Узнать его можно через команду "ipconfig" в Windows и "ifconfig" в Linux.</p>
<p>6.)В качестве порта начального укажите 80, в качестве назначения - 8000(или 443, в случае HTTPS)</p>
<p>7.)Сохраните изменения.</p>
<br>
<br>
<h1>How to make a web server on your computer accessible from outside (via your router's IP address)</h1>
<p>1.) Specify in the server host configuration files 0.0.0.0 and port 8000</p>
<p>2.) Enter "192.168.0.1" in the browser's address bar. This is the router's address in your local network</p>
<p>3.) Log in to your router's administrator panel</p>
<p>4.) Go to the "port forwarding" section</p>
<p>5.) In the IP address field, enter the address of your computer in the local network. You can find it using the "ipconfig" command in Windows and "ifconfig" in Linux.</p>
<p>6.) Specify 80 as the starting port and 8000 (or 443, for HTTPS) as the destination port</p>
<p>7.) Save the changes.</p>