# Feowl User Interface
## Installation
### Dependancies
You must have a basic Apache and PHP environement:

	sudo apt-get install apache2 php5 libapache2-mod-php5 php5-curlhave

### System configuration
The Kohana installation <b>must be at the root of your virtual host or domain</b>.

Also, you have to allow writing on <em>UI/application/cache</em> and <em>UI/application/logs</em> directories (replace 	&lt;path> by the path of the Feowl directory):

	cd <path>
	chomd 777 -Rf UI/application/logs UI/application/cache

### API access
Every Feowl installation must use a unique key for the API. [Do not hesitate to ask for a key!](mailto:contact@feowl.com)
To setup your key, from the Feowl direcotry type:

	cp UI/application/config/apiauth.php.template UI/application/config/apiauth.php
	nano UI/application/config/apiauth.php
	
And replace:

	return array(
		"default" => array(
			"username" => "",
			"api_key"  => ""
		)
	);
	
By your credentials:

	return array(
		"default" => array(
			"username" => "example-user",
			"api_key"  => "example-key"
		)
	);
