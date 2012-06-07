<?php defined('SYSPATH') or die('No direct script access.');

return array(
	/*
	* In languages.supported, the keys define the language uri string,
	* the first array element defines the i18n::lang, and the second
	* array element is the language name.
	*
	* NOTE: In languages.supported, keys that have a similar beginning
	* must be placed from longest to shortest to avoid regex problems.
	* Ex: 'fr_ca' must come before 'fr'.
	*
	* NOTE: The languages.default value must be one if the languages.supported keys.
	*/
	'languages' => array(

		'supported' => array(

			'en' => array(
				'code' => 'en-us',
				'locale' => array('en_US.utf-8'),
				'name' => 'English'
			),

			'fr' => array(
				'code' => 'fr-fr',
				'locale' => array('fr_FR.utf-8'),
				'name' => 'Français'
			),

		),

		'default' => 'en',
	),
);