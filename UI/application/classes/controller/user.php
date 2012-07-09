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
 
    public $template = "template/sub_template.tpl";
	
	public function before(){
		try {
			$this->session = Session::instance();
		} catch(ErrorException $e) {
			session_destroy();
		}
		// Execute parent::before first
		parent::before();
		// Open session
		$this->session = Session::instance();
	}
	
	 //Use the after method to load static files
	public function after()
	{
		// Adds all javascript files
		$this->template->files_javascript = array(		
			url::base()."assets/js/script-user.js",
			"http://jzaefferer.github.com/jquery-validation/jquery.validate.js"
		);	
		parent::after();
	}
	
    public function action_index()
    {
        // Load the user information
        $user = Auth::instance()->get_user();
         
        // if a user is not logged in, redirect to login page
        if (!$user)
        {
            Request::current()->redirect('user/login');
        }else{
			Request::current()->redirect('contribute');
		}
    }
     
	 //post to the api to creat an account for a contributor
    public function action_signup()
    {
        $this->template->right_content = View::factory('user/signup.tpl')
            ->bind('error_1', $error_1)->bind('error_2', $error_2);
		$this->template->left_content = View::factory('user/signup_info.tpl');
             
        if (HTTP_Request::POST == $this->request->method())
        {    //echo "I love Feowl"; exit;
			try{
				//build json items
				$json_items['name'] = Arr::get($_POST,'username');	
				$json_items['password'] = Arr::get($_POST,'userpassword');
				$json_items['email'] = Arr::get($_POST,'useremail');	
				$json_items['language'] = Arr::get($_POST,'language');				 	 
				//send to api
				$data_string = json_encode($json_items);   
				$results =Model_Contributors::create_contributor($data_string);
                 
				$http_status = json_decode($results['http_status']);
				$json_result = json_decode($results['json_result'], true); 
				 
				if($http_status == 201){
					$notice = "Thanks for signing up! We would sent you an email to
					verity your account";
					//set notice in session
					$this->session->set('alert', $notice);
					Request::current()->redirect('home');
				}elseif(isset($json_result['error_message'])){
					$error_1 = $json_result['error_message']; 
				}else{
					//error 400 :)
					if(isset($json_result['name'][0])):
						$error_1 = $json_result['name'][0]." ";
					endif;
					if(isset($json_result['email'][0])):
						$error_2 = $json_result['email'][0]; 
					endif;
				}
			
				//@todo force login to next step
			}
			catch(Exception $e) {
                // Set failure message TODO: Set various notices
				$this->session->set('alert', "Technical Error :)");
            }
		}
    }
     
	//login the user
    public function action_login()
    {
        $this->template->right_content = View::factory('user/login.tpl')
            ->bind('message', $message);
		$this->template->left_content = View::factory('user/login_info.tpl');
         
        if (HTTP_Request::POST == $this->request->method())
        {
		   // Attempt to login user
            $remember = array_key_exists('remember', $this->request->post());
            $user = Auth::instance()->login($this->request->post('email'), $this->request->post('password'), $remember);

            // If successful, redirect user to contribute page
            if ($user)
            {
                Request::current()->redirect('contribute');
				$this->session->set('alert', print_r($user));
				Request::current()->redirect('home');
            }
            else
            {
                $message = 'Username and password don\'t match';
            }
        }
    }
     
	 //logout the user
    public function action_logout()
    {
        // Log user out
        Auth::instance()->logout();
         
        // Redirect to login page
        Request::current()->redirect('user/login');
    }
	
}