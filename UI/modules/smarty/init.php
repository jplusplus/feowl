<<<<<<< HEAD
<?php defined('SYSPATH') or die('No direct access allowed.');
/**
 * Init file for smarty module. This sets up the demo which can be accessed at
 * {base_url}/smarty. Delete/rename/comment out this file if you don't want the
 * demo.
 *
 * @todo don't set route in production mode.
 *
 * @copyright  (c) 2011 Mr Anchovy
 * @license    http://kohanaframework.org/license
 */
if ( Kohana::$environment!==Kohana::PRODUCTION ) {
	Route::set('smarty', 'smarty(/<controller>)')
		->defaults(array(
			'controller' => 'smartydemo',
			'action'     => 'index',
		));
}
=======
<?php defined('SYSPATH') or die('No direct access allowed.');
/**
 * Init file for smarty module. This sets up the demo which can be accessed at
 * {base_url}/smarty. Delete/rename/comment out this file if you don't want the
 * demo.
 *
 * @todo don't set route in production mode.
 *
 * @copyright  (c) 2011 Mr Anchovy
 * @license    http://kohanaframework.org/license
 */
if ( Kohana::$environment!==Kohana::PRODUCTION ) {
	Route::set('smarty', 'smarty(/<controller>)')
		->defaults(array(
			'controller' => 'smartydemo',
			'action'     => 'index',
		));
}
>>>>>>> e27bf4a698bac9fe0d5e2ed0a6a42d10d47ec42f
