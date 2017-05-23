Suade
========

An API for reporting


:License: MIT



Basic Commands
--------------

API Endpoints
^^^^^^^^^^^^^


+---------------------+------------------------+ 
| Endpoints           | Comments               | 
+=====================+========================+ 
|/api/reports/        | list all report        | 
+---------------------+------------------------+ 
|/api/report/<id>/    | list specific report   | 
+---------------------+------------+-----------+ 
|/api/repot/<id>.xml/ | list report in XML     | 
+---------------------+------------------------+
|/api/report/<id>.pdf/| list report in PDF     |
+---------------------+------------------------+

    

Running tests
~~~~~~~~~~~~~

::

  $ python app-test.py




Deployment
----------

The following details how to deploy this application.


Heroku
^^^^^^

 $ git push heroku master



