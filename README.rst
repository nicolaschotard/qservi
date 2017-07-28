qservi: Qserv Integration into science pipelines
================================================

The goal of this project is to test Qserv on real data processed
through the LSST stack. First try will be to use it in the `Clusters
<https://github.com/nicolaschotard/Clusters>`_ pipeline. Here are the
steps we would like to cover:

- Process a set of data, and produce the catalogs (independent step);
- Create a local Qserv instance ready to ingest data;
- Transform the catalgos into a data format that Qserv can ingest;
- Load the catalogs in Qserv;
- Create a set of queries to test the basic functionnqlities of Aserv;
- Build of find python tools to make these queries;
- Implement that into the Clusters pipeline;
- Extend that to other analysis.

Data processing
---------------

Process data through the stack and produced different catalogs
(`forced_src`, `deepCoadd_meas`, `deepCoadd_forced_src`,etc.). This
step is actually independent and must be done prior to this work. See
the `reprocessing task force gihub page
<https://github.com/LSSTDESC/ReprocessingTaskForce>`_ for more info.

Create a local qserv instance
-----------------------------

- Install docker, if not already done
    - `dnf install docker`  (or equivalent, i.e. yum)
    - `sudo groupadd docker && sudo gpasswd -a ${USER} docker && sudo systemctl restart docker`
    - `sudo usermod -aG docker ${USE}`
    - `newgrp docker`
    - `sudo /bin/systemctl enable docker.service`
    - retart your computer
    - `docker info` (to ckeck that it worked)
- `git clone https://github.com/lsst/qserv`
- `cd qserv/admin/tools/docker/deployment/localhost`
- `cp env.example.sh env.sh`
- `./run-multinode-tests.sh`
- Integration tests should have run correctly. You should now be able to see you container runing using `docker info`.  

Load the catalogs into qserv
----------------------------

Here is a list of command to run in order to load you own data, as it is
currently done to test qserv in continuous integration::

  # Copy the test data
  git clone https://github.com/nicolaschotard/qserv_testdata.git
  # launch a terminal in the docker container
  docker exec -it qserv bash
  # load the LSST environment (the stack)
  . /qserv/stack/loadLSST.bash
  # Setup qserv
  setup qserv_distrib -t qserv-dev
  cd qserv_testdata/
  # Setup the qserv_test_data package
  setup -k -r .
  # Create a new test dataset that we will modify later to put our data
  cp -r datasets/case03/ datasets/case06
  # Launch the test for case06
  qserv-check-integration.py --load --case=06

The test should have run.

To change the log level::

  docker exec -it -u root qserv bash
  apt-get install emacs # if not already there
  export TERM=xterm
  emacs -nw ~/.lsst/logging.ini
  # and change the debug levels

Next steps:

- Replace the content of qserv_testdata/datasets/case06/data/ with our own
  data set (see next section)
- Check and update the query list in
  qserv_testdata/datasets/case06/queries/ with the real science
  queries we want to do (see last section)
- open a python terminal and try python-queries


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
