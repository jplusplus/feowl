<?php defined('SYSPATH') or die('No direct access allowed.');

return array
(
    //enable translation target languages, that we should generate files for
	'languages' => array(
		//'en' => 'English',  //only generates files config key 'default' is not 'en' !
		//'ca' => 'Català',
		//'es' => 'Español',
		'fr' => 'Français',
		//'de' => 'Deutsch',
	),

	// The default language corresponds to the language you wrote the translation strings in.
    // Only if you set it to False i18nget will generate files for this language
    // This is useful if you use keys like 'edit.profile' which still should be translated
	'default' => 'en',

    //whether we should copy translation files to __file__.old_timestamp
    //before generating the new file
    'should_make_backups' => false,
);