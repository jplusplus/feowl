<?php defined('SYSPATH') or die('No direct script access.');
 
/**
 * user controller, User Authentication on the web platform
 *
 * @package    Feowl/Auth
 * @author     Feowl Team
 * @copyright  (c) 2012 Feowl Team
 * @license    http://feowl.tumblr.com/
 */
class Controller_User extends Controller_Template {
 
    public function action_index()
    {
        $this->template->content = View::factory('user/info')
            ->bind('user', $user);
         
        // Load the user information
        $user = Auth::instance()->get_user();
         
        // if a user is not logged in, redirect to login page
        if (!$user)
        {
            Request::current()->redirect('user/signup');
        }
    }
     
    public function action_signup()
    {
        $this->template->content = View::factory('user/signup')
            ->bind('errors', $errors)
            ->bind('message', $message);
             
        if (HTTP_Request::POST == $this->request->method())
        {    
	
            try {
				//print_r($_POST);exit;	
                // Create the user using form values
                $user = ORM::factory('user')->create_user($this->request->post(), array(
                    'username',
                    'password',
                    'email',
                    'userphone',
					'userhome'
                ));
                 
                // Grant user login role
                $user->add('roles', ORM::factory('role', array('name' => 'login')));
                 
                // Set success message
                $message = "You have added user '{$user->username}' to the database";
				//@todo send welcome email
				//Print_r(Arr::get($_POST, 'username'));exit;
				Auth::Instance()->force_login(Arr::get($_POST, 'email'));
				// Reset values so form is not sticky
                $_POST = array();
				Request::current()->redirect('user/index');
				//@todo force login in to step 2
                 
            } catch (ORM_Validation_Exception $e) {
                 
                // Set failure message
                $message = 'There were errors, please see form below.';
                 
                // Set errors using custom messages
                $errors = $e->errors('models');
            }
        }
    }
     
    public function action_login()
    {
        $this->template->content = View::factory('user/login')
            ->bind('message', $message);
             
        if (HTTP_Request::POST == $this->request->method())
        {
            // Attempt to login user
            $remember = array_key_exists('remember', $this->request->post());
            $user = Auth::instance()->login($this->request->post('username'), $this->request->post('password'), $remember);
             
            // If successful, redirect user
            if ($user)
            {
                Request::current()->redirect('user/index');
            }
            else
            {
                $message = 'Username and password don\'t match';
            }
        }
    }
     
    public function action_logout()
    {
        // Log user out
        Auth::instance()->logout();
         
        // Redirect to login page
        Request::current()->redirect('user/login');
    }
 
}