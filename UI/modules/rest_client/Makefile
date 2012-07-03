kohana :
	@echo "Verifying that all php files in this project are syntactically parsable..."
	@for i in `find . | grep .php$$`; do php -l $$i; done
	@echo "Verifying that all php files in this project conform to a general approximation of the Kohana style guidelines..."
	@for i in `find . | grep .php$$`; do echo $$i && phpcs --standard=Kohana $$i; done
