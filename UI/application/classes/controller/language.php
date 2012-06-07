<?php defined('SYSPATH') or die('No direct script access.');
 
 /**
 * language controller, Change the language of the interface
 *
 * @package    Feowl/Language
 * @author     Feowl Team
 * @copyright  (c) 2012 Feowl Team
 * @license    http://feowl.tumblr.com/
 */
class Controller_Language extends Controller {

	function action_change($lang) {

	   if(!in_array($lang, array('fr', 'en') )) {
	      $lang = 'en';
	   }

	   Cookie::set('lang', $lang);
	   I18n::lang($lang);
	   Request::current()->redirect('/');
	}

}