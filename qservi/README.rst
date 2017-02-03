Data format
===========

What is the data format expected by qserv?

- How to go from the stack output format to the qserv intput format?

  - Catalogs are stored in fits files
  - How to access the schema?
  - How to create csv files from these fits files? Is there a way to
    do that already implemented in the stack? Check on community or
    start a discussion about that if needed

- Start the test with one or two catalogs, and a small part of the sky
- Write a script to take care of that automatically. It should be able to
  load any catalog
- See the qserv_testdata `repository
  <https://github.com/lsst/qserv_testdata>`_


Type conversion when writing the data in ``csv`` files::

  types = {'bool': 'boolean',
           'float32': 'float',
           'float64': 'double',
           'int32': 'int(11)',
           'int64': 'bigint(20)',
           'string24': 'char(16)',
           'string8': 'char(5)'}

There is a limit on the number of character for a key, apparently set to 64.

Queries
=======

Ordering
````````

How to order the data. Apparently needed to compare mysql qnd qserv results.

Add the follwoing add bfore the query (in your .sql file)::

  -- pragma sortresult

Or this one at then end of your query::

  ORDER BY id;

The query will actually be a bit different, but the result shoud be the same.

Strange thing when making queries on the objectId column, we have to use::

  ObjectId = ...

instead of::

  objectId = ...

Same with other "ID" keys (e.g., ``deepCoadd_measId``->`DeepCoadd_measId`)

Check the DB interactively
==========================

Command line
````````````

The online command is::

  mysql --host=qserv-user-master-1 --port=4040 --user=qsmaster --batch THEDB -e "THEQUERY"


The DB can be ``qservTest_case06_mysql`` or ``qservTest_case06_qserv`` in our case.

Interactively
`````````````
Open a mysql terminal::

  mysql --socket /qserv/run/var/lib/mysql/mysql.sock --user=root --pass=CHANGEME

Select the DB::
  
  use qservTest_case06_mysql; # or _qserv for the qserv DB

Do a query::

  select coord_ra_deg,deepCoadd_measId from deepCoadd_meas where deepCoadd_measId=1100182716504;

DB scehma
=========

Current DB schema that I have in mind. It will be updated as I
understand better waht I'm doing.

..image:: lsstdb.png
