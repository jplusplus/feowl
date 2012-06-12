<<<<<<< HEAD
<?php
/**
 * Smarty plugin
 *
 * @package Smarty
 * @subpackage PluginsModifierCompiler
 */

/**
 * Smarty strip_tags modifier plugin
 *
 * Type:     modifier<br>
 * Name:     strip_tags<br>
 * Purpose:  strip html tags from text
 *
 * @link http://www.smarty.net/manual/en/language.modifier.strip.tags.php strip_tags (Smarty online manual)
 * @author Uwe Tews
 * @param array $params parameters
 * @return string with compiled code
 */
function smarty_modifiercompiler_strip_tags($params, $compiler)
{
   if (!isset($params[1])) {
        $params[1] = true;
    }
    if ($params[1] === true) {
        return "preg_replace('!<[^>]*?>!', ' ', {$params[0]})";
    } else {
        return 'strip_tags(' . $params[0] . ')';
    }
}

=======
<?php
/**
 * Smarty plugin
 *
 * @package Smarty
 * @subpackage PluginsModifierCompiler
 */

/**
 * Smarty strip_tags modifier plugin
 *
 * Type:     modifier<br>
 * Name:     strip_tags<br>
 * Purpose:  strip html tags from text
 *
 * @link http://www.smarty.net/manual/en/language.modifier.strip.tags.php strip_tags (Smarty online manual)
 * @author Uwe Tews
 * @param array $params parameters
 * @return string with compiled code
 */
function smarty_modifiercompiler_strip_tags($params, $compiler)
{
   if (!isset($params[1])) {
        $params[1] = true;
    }
    if ($params[1] === true) {
        return "preg_replace('!<[^>]*?>!', ' ', {$params[0]})";
    } else {
        return 'strip_tags(' . $params[0] . ')';
    }
}

>>>>>>> e27bf4a698bac9fe0d5e2ed0a6a42d10d47ec42f
?>