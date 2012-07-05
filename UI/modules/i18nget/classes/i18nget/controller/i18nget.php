<?php defined('SYSPATH') or die('No direct script access.');

class I18nget_Controller_I18nget extends Controller {

	public function before()
	{
		// Set default language
		I18n::$lang = Kohana::$config->load('i18n.default');
	}

    /*
     * Generates i18n Kohana translation files or amends files that miss translation keys
     *
     * Usage:
     * i18nget/generate/to_path/from_path
     *
     * Where "to_path" and "from_path" must either be "application" or a valid module name.
     * If "from_path" is omitted it defaults to "to_path"
     *
     * Examples
     * "i18nget/generate/application" generates files for your application in application/i18n/
     * "i18nget/generate/mymodule/application" generates files for mymodule in application/i18n/
     * "i18nget/generate/mymodule" generates files for mymodule in mymodule/i18n/
     *
     */
	public function action_generate()
	{
        // Restrict to cli mode
		if ( ! Kohana::$is_cli )
		{
			echo "<pre>\nUsage: php index.php --uri=\"i18nget/generate\" or\n";
			echo "       php index.php --uri=\"i18nget/generate_for/mymodule\" or\n";
			echo "       php index.php --uri=\"i18nget/generate_for/mymodule/application\"\n</pre>";
			return;
		}

        $user_paths  = array($this->request->param('from_path', 'application'));
        $user_paths []= $this->request->param('to_path', $user_paths[0]);

        //if we should check all i18n files in the projetcs or just module files
        $global_i18n = $user_paths[1] == 'application';

        foreach( $user_paths as $idx => $path_to_check )
        {
            //application?
            if( $path_to_check == 'application' )
            {
                $user_paths[$idx] = APPPATH;
                continue;
            }

            //module?
            $modules = array_slice(scandir(MODPATH), 2);
            if( !in_array($path_to_check, $modules) )
            {
                die("Your given option '$path_to_check' must either match 'application'" .
                    " or one of the module names:\n  " . join( "\n  ", $modules ));
            }
            else
            {
                $user_paths[$idx] = MODPATH . $path_to_check;
            }
        }

		$this->auto_render = FALSE;

		$path = $user_paths[0];
        $output_path = rtrim($user_paths[1], DIRECTORY_SEPARATOR) . DIRECTORY_SEPARATOR;

        echo "\nGenerating files for \n'$path'\ninto\n'{$output_path}i18n'\n\n";

		$data = array();
		$unique_phrases_helper = array();
		$scan_files = $this->get_dir_files($path, array('php', 'tpl'));

        //echo Debug::dump($this->request, 9999);
        //print_r(Request::$current->uri());
        //print_r($user_paths);
        //print_r($scan_files); return;

		foreach ($scan_files as $file)
		{
			$file_path_human = substr($file, strlen($path));
// 			echo Debug::dump($file_path_human, 9999);

			// Get each line of the file
			$file_lines = file($file, FILE_IGNORE_NEW_LINES);

			$data_file = array();

			foreach ($file_lines as $num_line => $file_line)
			{
				$num_line++;

// 				echo Kohana::debug($num_line, $file_line, $file_path_human);

// 				if (preg_match_all('/(?P<key>\w+):(?P<name>[\p{L}+|\D+])/u', $file_line, $matches))
// 				if (preg_match('/^(?P<name>.*?[^(TO|COPYTO)]+)( TO (?P<assignedto>\w[^(COPYTO)]+))?( COPYTO (?P<copyto>\w[^(TO)]+))?$/u', trim($email['Subject']), $matches))
// 				if (preg_match_all('/__\(\'(?P<phrase>.+)\'(, ?array\(.+\))?\)/u', $file_line, $matches))
// 				if (preg_match_all('/__\(\'(?P<phrase>.*)(, ?array\(.+\))?\'\)/u', $file_line, $matches))
// 				if (preg_match_all("/__\('(?P<phrase>.*?[^;])'\)/u", $file_line, $matches))
// 				if (preg_match_all("/__\([^'.+'$]\)/u", $file_line, $matches))
// 				if (preg_match_all("/__\([^_]+\)/u", $file_line, $matches))
// 				if (preg_match_all("/__\([^\b__]+\)/u", $file_line, $matches))
// 				if (preg_match_all("/__\((?P<phrase>((?!__).)+)\)/u", $file_line, $matches)) /// NOTE IT WORKS!!!
// 				if (preg_match_all("/__\((?P<phrase>((?!__)|(?!array).)+)\)/u", $file_line, $matches))
// 				if (preg_match_all("/__\(('|\")(?P<phrase>((?!__)|(?! ?array ?\().)+)('|\")/u", $file_line, $matches)) /// NOTE IT WORKS!!!
				
				// Classic matching for __ function
				if (preg_match_all("/__\(('|\")(?P<phrase>((?!__)|(?! ?array ?\().)+)('\)|',|\"\)|\",)/u", $file_line, $matches)) /// NOTE IT WORKS!!!
				{
// 					echo Kohana::debug($file_path_human, $num_line, $file_line, $matches);
// 					echo Kohana::debug($file_path_human, $num_line, $file_line, $matches['phrase']);
// 					echo Kohana::debug($matches['phrase']);

					$new_phrases = array_diff(array_unique($matches['phrase']), $unique_phrases_helper);

					if ($new_phrases)
					{
						$data_file[] = array(
							'line_number' => $num_line,
							'line_string' => $file_line,
							'phrases' => $new_phrases,
						);

						$unique_phrases_helper = array_merge($new_phrases, $unique_phrases_helper);
					}
				}

				// Additional matching for {__ t=''} function (smarty)
				if( preg_match_all("/{__\s+t\=(('|\")(?P<phrase>((?!__)|(?! ?array ?\().)+)('|\"))\s?}/u", $file_line, $matches) ) {
	
					$new_phrases = array_diff(array_unique($matches['phrase']), $unique_phrases_helper);

					if ($new_phrases) {

						$data_file[] = array(
							'line_number' => $num_line,
							'line_string' => $file_line,
							'phrases' => $new_phrases,
						);

						$unique_phrases_helper = array_merge($new_phrases, $unique_phrases_helper);
					}

				}
			}

			if ($data_file)
			{
				$data[] = array(
					'filepath' => $file,
					'filepath_human' => $file_path_human,
					'lines' => $data_file,
				);
			}

            /* if( strpos($file, 'format')!==False )
            {
                print_r($data_file);
                die('found');
            } */
		}

  		//echo Debug::dump($data, 9999);

		$languages = Kohana::$config->load('i18nget')->get('languages');
		$default_language = Kohana::$config->load('i18nget')->get('default');
		$orphe_phrases = array();

		// Fix phrases
		foreach ($unique_phrases_helper as $key => $phrase)
		{
			$unique_phrases_helper[$key] = str_replace('\\\'', '\'', $unique_phrases_helper[$key]);
			$unique_phrases_helper[$key] = str_replace('\\"', '"', $unique_phrases_helper[$key]);
		}



		// Add phrases present in current i18n language files but are not present in current code
		foreach ($languages as $language_code => $language)
		{
            if( $global_i18n )
            {
                //only if we write to application we want to look at kohana's complete CFS for i18n files.
			    $i18n_messages = array_keys(I18n::load($language_code));
            }
            else
            {
                //if we output in an i18n folder of a module, we are only interested in that modules current translations
                $lang_file = $this->lang_file_path( $output_path, $language_code );

                if( file_exists( $lang_file ) )
                {
                    $i18n_messages = array_keys(Kohana::load( $lang_file ));
                }
                else
                {
                    $i18n_messages = array();
                }
            }

            $orphe_phrases = array_merge($orphe_phrases, array_diff($i18n_messages, $unique_phrases_helper));
		}

		$orphe_phrases = array_unique($orphe_phrases);

        //print_r($unique_phrases_helper);
        //print_r($i18n_messages);
 		//print_r($orphe_phrases); //die();
		// Generate new i18n files
		foreach ($languages as $language_code => $language)
		{
			if ($default_language !== $language_code)
			{
                $filename = $this->lang_file_path($output_path, $language_code);

                //construct content before renaming original file
				$content = View::factory('i18nget/generate')
					->set(array(
                        'data' => $data,
					    'orphe_phrases' => $orphe_phrases,
					    'language_code' => $language_code,
                        'filename' => $filename,
					    'global_i18n' => $global_i18n,
                ))->render();

                //print_r($content);

                if ( file_exists($filename) AND Kohana::$config->load('i18nget')->get('should_make_backups') )
				{
					rename( $filename, $backup_name = $filename . '.old_' . time() );
                    echo "Backup file: ".substr($backup_name, strlen(DOCROOT))."\n";
				}


				if (FALSE === file_put_contents($filename, $content))
				{
					echo "There's an error writing the file: ".substr($filename, strlen(DOCROOT))."\n\n";
				}
				else
				{
					echo "File written: ".substr($filename, strlen(DOCROOT))."\n\n";
				}
			}
		}

		// Fix permissions
// 		system('chown marcalj:marcalj '.APPPATH.'logs/i18n/*');

		echo "Done!\n";
	}

    public function lang_file_path( $base_path, $lang_code )
    {
        // Split the language: language, region, locale, etc
        $parts = explode('-', $lang_code);
        // Create a path for this set of parts
        $path = implode(DIRECTORY_SEPARATOR, $parts);
        return rtrim($base_path, DIRECTORY_SEPARATOR) . DIRECTORY_SEPARATOR . 'i18n' . DIRECTORY_SEPARATOR . $path . '.php';
    }

	/**
	 * Working tests:
	 *
	 * <?php echo __('tèst1'); ?>
	 * <?php echo __('tést2 :mico', array(':mico' => I18n::$lang)); ?>
	 * <?php echo __('tëst3 :mico', array(':mico' => I18n::$lang)); ?><?php echo __('test4'); ?>
	 * <?php echo __('test5 :mico', array(':mico' => I18n::$lang)).__('test6'); ?>
	 * <?php echo __('test7 :mico', array(':mico' => HTML::anchor(Route::get('website/new-tradu')->uri(array('language' => I18n::$lang)), __('test8')))); ?>
	 * <?php echo __('test9 :mico', array(':mico' => HTML::anchor(Route::get('website/new-tradu')->uri(array('language' => I18n::$lang)), __('test10 :moco', array(':moco' => I18n::$lang))))); ?>
	 * <?php echo __('tést11'); ?><?php echo __('tést12'); ?>
	 * <?php echo __('test13'); ?><?php echo __('tëst14 :mico', array(':mico' => I18n::$lang)); ?>
	 * <?php echo __('tést15'); ?><?php echo __('tést16'); ?><?php echo __('tést17'); ?>
	 * <?php echo __('tést18_jodete'); ?>
	 * <?php echo __('tést19;'); ?>
	 * <?php echo __("tést20;"); ?>
	 * <?php echo __('tést21 you\'re'); ?>
	 * <?php echo __('tést21 "enviar"'); ?>
	 */


    /*
    * Recursive function to return an array of files under the given path,
    * filtered by the given file types
    */
	public function get_dir_files($dir, $types = NULL)
	{
		// Remove DIRECTORY_SEPARATOR at the end
		$dir = rtrim($dir, DIRECTORY_SEPARATOR);

		$path = '';

		$stack[] = $dir;

		while ($stack)
		{
			$thisdir = array_pop($stack);

			if ($dircont = scandir($thisdir))
			{
				$i = 0;

				while (isset($dircont[$i]))
				{
					if ($dircont[$i] !== '.' && $dircont[$i] !== '..')
					{
						$current_file = $thisdir.DIRECTORY_SEPARATOR.$dircont[$i];

						if (is_file($current_file))
						{
							if (is_array($types))
							{
								if (in_array(strtolower(pathinfo($thisdir.$dircont[$i], PATHINFO_EXTENSION)), $types, TRUE))
								{
									$path[] = $thisdir.DIRECTORY_SEPARATOR.$dircont[$i];
								}
							}
						}
						elseif (is_dir($current_file))
						{
							$stack[] = $current_file;
						}
					}

					$i++;
				}
			}
		}

		return $path;
	}

	/// FIXME use this function (alert!! it's recursive!)
	/**
	 * Recursively finds all of the files in the specified directory at any
	 * location in the [Cascading Filesystem](kohana/files), and returns an
	 * array of all the files found, sorted alphabetically.
	 *
	 *     // Find all view files.
	 *     $views = Kohana::list_files('views');
	 *
	 * @param   string  directory name
	 * @param   array   list of paths to search
	 * @return  array
	 */
// 	public static function list_files($directory = NULL, array $paths = NULL)

}