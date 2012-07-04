<?php defined('SYSPATH') or die('No direct access allowed.');

Route::set('i18nget/generate', 'i18nget/generate(/<from_path>(/<to_path>))', array(
        'from_path' => '[a-zA-Z-_0-9]+',
        'to_path' => '[a-zA-Z-_0-9]+',
    ))
	->defaults(array(
		'controller' => 'i18nget',
		'action'     => 'generate',
        'from_path'  => 'application',
        'to_path'    => NULL,
	));

