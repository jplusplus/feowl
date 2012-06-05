BOOTSTRAP = ./css/bootstrap.css
BOOTSTRAP_MIN = ./css/bootstrap.min.css
BOOTSTRAP_LESS = ./less/bootstrap.less
BOOTSTRAP_RESPONSIVE = ./css/bootstrap-responsive.css
BOOTSTRAP_RESPONSIVE_MIN = ./css/bootstrap-responsive.min.css
BOOTSTRAP_RESPONSIVE_LESS = ./less/responsive.less

DATE=$(shell date +%I:%M%p)
CHECK=\033[32m✔\033[39m


Built:	
	@echo "Building Bootstrap..."
	@recess --compile ${BOOTSTRAP_LESS} > ${BOOTSTRAP}
	@recess --compile --compress ${BOOTSTRAP_LESS} > ${BOOTSTRAP_MIN}
	@recess --compile --compress ${BOOTSTRAP_RESPONSIVE_LESS} > ${BOOTSTRAP_RESPONSIVE_MIN}	
	@recess --compile ${BOOTSTRAP_RESPONSIVE_LESS} > ${BOOTSTRAP_RESPONSIVE}
	@echo "Compiling LESS with Recess...               ${CHECK} Done"

