# Mozio Providers
 REST API that allow Mozio service providers to register themselves and add their service areas. 

[Online version](http://35.237.53.137/docs/)

### External Documentation:

* [Django](https://docs.djangoproject.com/en/2.0/releases/2.0/)
* [GeoDjango](https://docs.djangoproject.com/en/2.1/ref/contrib/gis/tutorial/)
* [Postgis](https://postgis.net/documentation/)

### Requirements to run locally:
* Linux-based system
* [Python 3.6](https://www.python.org/)
* [PostgreSQL](https://www.postgresql.org/)
* [PostGIS](https://postgis.net/install/)

### PostGIS Requirements:
* [GEOS](http://trac.osgeo.org/geos)
* [PROJ.4](https://github.com/OSGeo/proj.4/wiki/)
* [GDAL](https://trac.osgeo.org/gdal/)

### Configuration  
Available settings:  
**PROVIDER_LANGUAGES**  
A tuple of language ISO codes with their full name.  
Used as choices for `language` field of `Provider` model.  

**PROVIDER_CURRENCIES**  
A tuple of currency codes with their full name.  
Used as choices for `currency` field of `Provider` model.  

