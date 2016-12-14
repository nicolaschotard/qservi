# qservi
Qserv integration into science analysis pipeline

The goal of this project if to test qserv on real data processed
through the LSST stack. Here is what we would like to cover:

- Process data through the stack and produced different catalogs
  (`forced_src`, `deepCoadd_meas`, `deepCoadd_forced_src`,etc.). This
  step is actually indepent and must be done prior to this work.
- Create a qserv instance:

  - dowload and untar the following file (clone from github?)::

      https://jira.lsstcorp.org/secure/attachment/28458/28458_qserv.tgz

  - or clone it from the `qserv <https://github.com/lsst/qserv>`_
    github repository?      
  - add the content of qserv/admin/tools/provision/ssh_config into
    your ~/.ssh/config file
  - install shmux: http://web.taranis.org/shmux/
  - go to qserv/admin/tools/docker/deployment/parallel and launch
    ``run-multinode-tests.sh`` which will launch the integration tests
  - other scripts in this directory are useful to run trivial
    management operation on Qserv nodes.
  - you can connect with ssh to each machine using a set of
    private/public keys. Ask Fabrice to send you these keys.
  - more info `here
    <https://github.com/lsst/qserv/tree/master/admin/tools/provision>`_
    
- Load the catalogs into a qserv:

  - What is the data format expected by qserv?
  - How to go from the stack output format to the qserv intput format?

    - Catalogs are stored in fits files
    - How to access the scema?
    - How to create csv files from these fits files? Is there a way to
      do that already implemented in the stack? Check on community or
      start a discussion about that if needed

  - Start the test with one or two catalogs, and a small part of the sky
  - Write a script to take of that automatically. It should be able to
    load any catalog
  - See the qserv_testdata `repository
    <https://github.com/lsst/qserv_testdata>`_

- How to query the data?

  - python interface to query into qserv; native qserv tools? django?
    something else?
  - implement standard queries into the `Clusters
    <https://github.com/nicolaschotard/Clusters>`_ pipelne
    
