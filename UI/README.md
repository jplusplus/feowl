### Kohana PHP Framework, version 3.1 (release)

This is the current release version of [Kohana](http://kohanaframework.org/).
Setup the framework your localhost.

### Twitter Bootstrap v2.0.3

The file are placed in /assets/css and /assets/js

### Modules

To make it light we just load five(5) modules :  auth, cache, database, orm, userguide

 Kohana::modules(array(\n
	 'auth'       => MODPATH.'auth',\n       
	// 'cache'      => MODPATH.'cache',\n      
	 'database'   => MODPATH.'database',\n  
	 'orm'        => MODPATH.'orm',\n        
	 'userguide'  => MODPATH.'userguide',\n 
	));\n
 
###