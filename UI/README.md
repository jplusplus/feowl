### Kohana PHP Framework, version 3.1 (release)

This is the current release version of [Kohana](http://kohanaframework.org/).
Setup the framework your localhost.

### Twitter Bootstrap v2.0.3

The file are placed in /assets/css and /assets/js

### Modules

To make it light we just load five(5) modules :  auth, cache, database, orm, userguide

 Kohana::modules(array(
	 'auth'       => MODPATH.'auth',       // Basic authentication
	// 'cache'      => MODPATH.'cache',      // Caching with multiple backends
	 'database'   => MODPATH.'database',   // Database access
	 'orm'        => MODPATH.'orm',        // Object Relationship Mapping
	 'userguide'  => MODPATH.'userguide',  // User guide and API documentation
	));
 
