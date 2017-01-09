qservi
======

**Qserv Integration into science analysis pipeline.**

The goal of this project is to test qserv on real data processed
through the LSST stack. First try will be to use it in the `Clusters
<https://github.com/nicolaschotard/Clusters>`_ pipeline. What we would
like to cover is presented in the following sections.

- process a set of data, and produce the catalogs
- create a qserv instance that we can use
- load the catalogs in qserv - build automatic tools to do it)
- query the data (build corresponding python tools)
- create a set of quesry test
- implement that into the Clusters pipeline
- test other DB
- extend that to other analysis

Data processing
---------------

Process data through the stack and produced different catalogs
(`forced_src`, `deepCoadd_meas`, `deepCoadd_forced_src`,etc.). This
step is actually independent and must be done prior to this work. See
the `reprocessing task force gihub page
<https://github.com/LSSTDESC/ReprocessingTaskForce>`_ for more info.

Create a qserv instance
-----------------------

How to
``````

- dowload and untar the following file::

    https://jira.lsstcorp.org/secure/attachment/28458/28458_qserv.tgz

- or clone it from the `qserv <https://github.com/lsst/qserv>`_
  github repository?
- add the content of qserv/admin/tools/provision/ssh_config into
  your ~/.ssh/config file
- you should have received the corresponding rsa keys and put them in
  your ~/.ssh/ directory
- install shmux: http://web.taranis.org/shmux/
- go to qserv/admin/tools/docker/deployment/parallel and launch
  ``run-multinode-tests.sh`` which will launch the integration tests
- other scripts in this directory are useful to run trivial
  management operation on Qserv nodes.
- you can connect with ssh to each machine using a set of
  private/public keys. Ask Fabrice to send you these keys.
- more info `here
  <https://github.com/lsst/qserv/tree/master/admin/tools/provision>`_

Questions
`````````

- Other ways to install and use qserv? 

Load the catalogs into qserv
----------------------------

How to
``````

See the `howto <howto.rst>`_ file.

Here is a list of command to run in order to test data, as it is
currently done to test qserv in continuous integration::

  # connect to teh VM on the cloud
  ssh qserv-user-master-1
  # launch a terminal in the docker container
  docker exec -it qserv bash
  # load the LSST environment (the stack)
  . /qserv/stack/loadLSST.bash
  # Setup qserv
  setup qserv_distrib -t qserv-dev
  # this directory is available inside and outside the container
  cd /qserv/run/var/log/
  # create a work directory
  mkdir work
  cd work/
  # Copy the test data
  git clone https://github.com/nicolaschotard/qserv_testdata.git
  cd qserv_testdata/
  # Setup the qserv_test_data package
  setup -k -r .
  # Create a new test dataset that we will modify later to put our data
  cp -r datasets/case03/ datasets/case06
  # Launch the test for case06
  qserv-check-integration.py --load --case=06

The test should have run.

Next steps:

- Replace the content of qserv_testdata/datasets/case06/data/ with our own
  data set (see next section)
- Check and update the query list in
  qserv_testdata/datasets/case06/queries/ with the real science
  queries we want to do (see last section)
- open a python terminal and try python-queries
  

Questions
`````````

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

Query the data
--------------

How do we make queries?

- python interface to query into qserv: native qserv tools? django?
  something else?
- implement standard queries into the `Clusters
  <https://github.com/nicolaschotard/Clusters>`_ pipeline

Query tests
-----------

What test do we want to run on qserv?

- check standard astronomical queries

  - magnitude or signal to noise cuts
  - specific target
  - specific area
  - combine several cuts
  - join several tables/catalogs

- check efficiency of queries
- check repeatability of queries
- build a test dataset, and make sure that queries give the same output over time
- is one big query better than many smaller ones?
- how complex can a query be?
- other tests?

Test other DBs
--------------

- MonetDB?
