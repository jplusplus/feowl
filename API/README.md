# Installation of the FEOWL API
## Install software dependency

postgres 9.1
postgis 1.5
python >=2.6
python-gdal

#### Python Packages (Should use a virtual environment)
`$ pip install -r requirements.txt`

# Database
(try sudo su; su - postgres)

### Install Postgis

`sudo su postgres -c'createdb -E UTF8 -U postgres template_postgis'`
`sudo su postgres -c'createlang -d template_postgis plpgsql;'`
`sudo su postgres -c'psql -U postgres -d template_postgis -c"CREATE EXTENSION hstore;"'`
`sudo su postgres -c'psql -U postgres -d template_postgis -f /usr/share/postgresql/9.1/contrib/postgis-1.5/postgis.sql'`
`sudo su postgres -c'psql -U postgres -d template_postgis -f /usr/share/postgresql/9.1/contrib/postgis-1.5/spatial_ref_sys.sql'`
`sudo su postgres -c'psql -U postgres -d template_postgis -c"select postgis_lib_version();"'`
`sudo su postgres -c'psql -U postgres -d template_postgis -c "GRANT ALL ON geometry_columns TO PUBLIC;"'`
`sudo su postgres -c'psql -U postgres -d template_postgis -c "GRANT ALL ON spatial_ref_sys TO PUBLIC;"'`
`sudo su postgres -c'psql -U postgres -d template_postgis -c "GRANT ALL ON geography_columns TO PUBLIC;"'`


### Make a real template
`UPDATE pg_database SET datistemplate = TRUE WHERE datname = 'template_postgis';`

### Create database user for Django

`createuser -U postgres --createdb --no-createrole --no-superuser --login --pwprompt feowl_django`

Enter password *passwd123*

### Create Database
`createdb --template=template_postgis --owner=feowl_django feowl`

### Create Database Tables
`python ./manage.py syncdb`
