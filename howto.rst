[14/12/2016@12:54:10]-[chotard@lappc-p664] ~/Work/qserv_test $ ssh qserv-user-master-1
Last login: Mon Dec 12 18:15:09 2016 from qserv-user-gateway
[qserv@qserv-user-master-1 ~]$ ls
[qserv@qserv-user-master-1 ~]$ 
[qserv@qserv-user-master-1 ~]$ 
[qserv@qserv-user-master-1 ~]$ pwd
/home/qserv
[qserv@qserv-user-master-1 ~]$ docker ps
CONTAINER ID        IMAGE                    COMMAND                  CREATED             STATUS              PORTS               NAMES
068fd9fe71c2        qserv/qserv:dev_master   "/bin/sh -c /qserv/sc"   42 hours ago        Up 42 hours                             qserv
[qserv@qserv-user-master-1 ~]$ docker inspect qserv
[
    {
        "Id": "068fd9fe71c2080fd74ad9cf1abafe09aab9debd88e2ea43a29b684b5d7b8063",
        "Created": "2016-12-12T17:26:53.373883453Z",
        "Path": "/bin/sh",
        "Args": [
            "-c",
            "/qserv/scripts/start.sh"
        ],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 31387,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2016-12-12T17:26:53.563194182Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:9bd1c55b82d859b3afcc9a47a2a3e354e44bf5657dd8fb4126463aa7015741a2",
        "ResolvConfPath": "/var/lib/docker/containers/068fd9fe71c2080fd74ad9cf1abafe09aab9debd88e2ea43a29b684b5d7b8063/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/068fd9fe71c2080fd74ad9cf1abafe09aab9debd88e2ea43a29b684b5d7b8063/hostname",
        "HostsPath": "/var/lib/docker/containers/068fd9fe71c2080fd74ad9cf1abafe09aab9debd88e2ea43a29b684b5d7b8063/hosts",
        "LogPath": "/var/lib/docker/containers/068fd9fe71c2080fd74ad9cf1abafe09aab9debd88e2ea43a29b684b5d7b8063/068fd9fe71c2080fd74ad9cf1abafe09aab9debd88e2ea43a29b684b5d7b8063-json.log",
        "Name": "/qserv",
        "RestartCount": 0,
        "Driver": "overlay",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "",
        "ExecIDs": null,
        "HostConfig": {
            "Binds": [
                "/qserv/log:/qserv/run/var/log"
            ],
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "host",
            "PortBindings": {},
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "CapAdd": null,
            "CapDrop": null,
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "ConsoleSize": [
                0,
                0
            ],
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": null,
            "BlkioDeviceReadBps": null,
            "BlkioDeviceWriteBps": null,
            "BlkioDeviceReadIOps": null,
            "BlkioDeviceWriteIOps": null,
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DiskQuota": 0,
            "KernelMemory": 0,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": -1,
            "OomKillDisable": false,
            "PidsLimit": 0,
            "Ulimits": [
                {
                    "Name": "memlock",
                    "Hard": 10737418240,
                    "Soft": 10737418240
                }
            ],
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0
        },
        "GraphDriver": {
            "Name": "overlay",
            "Data": {
                "LowerDir": "/var/lib/docker/overlay/e88fab440b705a17c07506b3880954be33d9e36d3050be870c69678dc8e9f3f0/root",
                "MergedDir": "/var/lib/docker/overlay/01822f7d30d465326cd49c17be44157540150ca7989abf604906771ed33a5dbd/merged",
                "UpperDir": "/var/lib/docker/overlay/01822f7d30d465326cd49c17be44157540150ca7989abf604906771ed33a5dbd/upper",
                "WorkDir": "/var/lib/docker/overlay/01822f7d30d465326cd49c17be44157540150ca7989abf604906771ed33a5dbd/work"
            }
        },
        "Mounts": [
            {
                "Source": "/qserv/log",
                "Destination": "/qserv/run/var/log",
                "Mode": "",
                "RW": true,
                "Propagation": "rprivate"
            }
        ],
        "Config": {
            "Hostname": "qserv-user-master-1",
            "Domainname": "",
            "User": "qserv",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "ExposedPorts": {
                "1094/tcp": {},
                "2131/tcp": {},
                "4040/tcp": {},
                "5012/tcp": {}
            },
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "QSERV_MASTER=qserv-user-master-1",
                "SET_CONTAINER_TIMEZONE=true",
                "CONTAINER_TIMEZONE=Europe/Madrid",
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "Cmd": [
                "/bin/sh",
                "-c",
                "/qserv/scripts/start.sh"
            ],
            "Image": "qserv/qserv:dev_master",
            "Volumes": null,
            "WorkingDir": "/qserv",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": {}
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "06b45996aeca11607af81667e523999c63bab3519f5d34e0c05ec30f80093b64",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {},
            "SandboxKey": "/var/run/docker/netns/default",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "",
            "Gateway": "",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "",
            "IPPrefixLen": 0,
            "IPv6Gateway": "",
            "MacAddress": "",
            "Networks": {
                "host": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "NetworkID": "6642b533a9531ff9b617929f5dffdf673723bc281063a7da95cade35e14c1e26",
                    "EndpointID": "2eb4b4f36b4ec56801cdb5315d0d00c5690c990f5b85c585642dca71df3e4401",
                    "Gateway": "",
                    "IPAddress": "",
                    "IPPrefixLen": 0,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": ""
                }
            }
        }
    }
]
[qserv@qserv-user-master-1 ~]$ 
[qserv@qserv-user-master-1 ~]$ 
[qserv@qserv-user-master-1 ~]$ 
[qserv@qserv-user-master-1 ~]$ 
[qserv@qserv-user-master-1 ~]$ ls
[qserv@qserv-user-master-1 ~]$ 
[qserv@qserv-user-master-1 ~]$ ls /qserv/log/
master  mysqld.log  mysql-proxy.log  mysql-proxy-lua.log  qserv-watcher.log  qserv-wmgr.log  xrootd-console.log
[qserv@qserv-user-master-1 ~]$ id
uid=1000(qserv) gid=1001(qserv) groups=1001(qserv),1000(docker) context=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023
[qserv@qserv-user-master-1 ~]$ docker exec -it qserv bash
qserv@qserv-user-master-1:/qserv$ docker
bash: docker: command not found
qserv@qserv-user-master-1:/qserv$ ls
data  master  qserv_client_error.log  qserv_client_info.log  run  scripts  stack
qserv@qserv-user-master-1:/qserv$ . /qserv/stack/loadLSST.bash 
qserv@qserv-user-master-1:/qserv$ git
usage: git [--version] [--help] [-C <path>] [-c name=value]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p|--paginate|--no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]

The most commonly used git commands are:
   add        Add file contents to the index
   bisect     Find by binary search the change that introduced a bug
   branch     List, create, or delete branches
   checkout   Checkout a branch or paths to the working tree
   clone      Clone a repository into a new directory
   commit     Record changes to the repository
   diff       Show changes between commits, commit and working tree, etc
   fetch      Download objects and refs from another repository
   grep       Print lines matching a pattern
   init       Create an empty Git repository or reinitialize an existing one
   log        Show commit logs
   merge      Join two or more development histories together
   mv         Move or rename a file, a directory, or a symlink
   pull       Fetch from and integrate with another repository or a local branch
   push       Update remote refs along with associated objects
   rebase     Forward-port local commits to the updated upstream head
   reset      Reset current HEAD to the specified state
   rm         Remove files from the working tree and from the index
   show       Show various types of objects
   status     Show the working tree status
   tag        Create, list, delete or verify a tag object signed with GPG

'git help -a' and 'git help -g' lists available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
qserv@qserv-user-master-1:/qserv$ cd /qserv/run/var/log/
qserv@qserv-user-master-1:/qserv/run/var/log$ mkdir work
qserv@qserv-user-master-1:/qserv/run/var/log$ setup qserv_distrib
qserv@qserv-user-master-1:/qserv/run/var/log$ qserv-data-loader.pya--help 
bash: qserv-data-loader.pya--help: command not found
qserv@qserv-user-master-1:/qserv/run/var/log$ qserv-data-loader.py --help
usage: qserv-data-loader.py [-h] [-v] [--verbose-all] [-V LOG_CONF] -f PATH
                            [-d PATH] [-t PATH] [-k] [-s] [-1] [-c CSSCONN]
                            [-r] [-C] [-H HOST] [-P PORT_NUMBER] [-W STRING]
                            [-x SECRET] [-E PATH] [-i DB_NAME] [-e]
                            database table schema [data [data ...]]

Single-node data loading script for Qserv.

positional arguments:
  database              Database name, Expected to exist and have correct
                        permissions.
  table                 Table name, must not exist.
  schema                Table schema file (should contain CREATE [TABLE|VIEW]
                        ... statement).
  data                  Input data files (CSV or anything that partitioner
                        accepts). Input can be empty, e.g. in case of defining
                        SQL view instead of regular table.

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         More verbose output, can use several times.
  --verbose-all         Apply verbosity to all loggers, by default only loader
                        level is set.
  -V LOG_CONF, --log-cfg LOG_CONF
                        Absolute path to file containing pythonlogger standard
                        configuration file

Partitioning options:
  Options defining how partitioning is performed

  -f PATH, --config PATH
                        Partitioner configuration file, required, more than
                        one acceptable.
  -d PATH, --chunks-dir PATH
                        Directory where to store chunk data, must have enough
                        space to keep all data. If option --skip-partition is
                        specified (without --one-table) then directory must
                        exist and have existing data in it. Otherwise
                        directory must be empty or do not exist. def:
                        ./loader_chunks.
  -t PATH, --tmp-dir PATH
                        Directory for non-chunk temporary files, e.g.
                        uncompressed data files. By default temporary
                        directory with random name inside chunks-dir is
                        created to hold temporary data.
  -k, --keep-chunks     If specified then chunks will not be deleted after
                        loading.
  -s, --skip-partition  If specified then skip partitioning, chunks must exist
                        already if option --one-table is not specified (from
                        previous run with -k option).
  -1, --one-table       If specified then load whole dataset into one table.
                        This is useful for testing quries against mysql
                        directly. If --skip-partition is specified then
                        original non-partitioned data will be loaded,
                        otherwise data will be partitioned but still loaded
                        into a single table.

CSS options:
  Options controlling CSS metadata

  -c CSSCONN, --css-conn CSSCONN
                        Connection string for CSS, def:
                        mysql://qsmaster@127.0.0.1:13306/qservCssData.
  -r, --css-remove      Remove CSS table info if it already exists.
  -C, --no-css          Disable CSS updates.

Database options:
  Options for database connection

  -H HOST, --host HOST  Host name for czar wmgr service, def: localhost.
  -P PORT_NUMBER, --port PORT_NUMBER
                        Port number to use for czar wmgr connection, def:
                        5012.
  -W STRING, --worker STRING
                        Node name for worker server, may be specified more
                        than once. If missing then czar server is used to
                        store worker data. If more than one node is given then
                        chunks are distributed randomly across all hosts. If
                        CSS is used then nodes must already be defined in CSS
                        (using qserv-admin command "CREATE NODE ..."). If CSS
                        is disabled (with --no-css) then node name will be
                        treated as a host name.
  -x SECRET, --secret SECRET
                        Path name for the file with wmgr secret.

Control options:
  Options for controlling other operations

  -E PATH, --empty-chunks PATH
                        Path name for "empty chunks" file, if not specified
                        then this file is not produced.
  -i DB_NAME, --index-db DB_NAME
                        Name of the database which keeps czar-side object
                        index, def: qservMeta. Index is generated only for
                        director table which is specified with dirTable option
                        in configuration file. Set to empty string to avoid
                        building index. If name is not empty then database
                        must already exist.
  -e, --delete-tables   If specified then existing tables in database will be
                        deleted if they exist, this includes both data and
                        metadata.
qserv@qserv-user-master-1:/qserv/run/var/log$ cd work/
qserv@qserv-user-master-1:/qserv/run/var/log/work$ git clone https://github.com/nicolaschotard/qserv_testdata.git
Cloning into 'qserv_testdata'...
remote: Counting objects: 1873, done.        
remote: Total 1873 (delta 0), reused 0 (delta 0), pack-reused 1873        
Receiving objects: 100% (1873/1873), 274.37 MiB | 55.64 MiB/s, done.
Resolving deltas: 100% (939/939), done.
Checking connectivity... done.
qserv@qserv-user-master-1:/qserv/run/var/log/work$ cd qserv_testdata/
qserv@qserv-user-master-1:/qserv/run/var/log/work/qserv_testdata$ setup -k -r .
qserv@qserv-user-master-1:/qserv/run/var/log/work/qserv_testdata$ setup qserv_distrib -t qserv-dev
qserv@qserv-user-master-1:/qserv/run/var/log/work/qserv_testdata$ eups list -s
antlr                 2.7.7.lsst1 	b2060 b2065 b2069 b2068 b1731 w_2015_44 w_2015_45 w_2015_47 w_2015_40 w_2015_43 qserv-dev b2114 b2113 b1942 b1823 b1824 b1825 b1700 dax_2015_11 dax_2015_10 b1709 b1660 b1899 b1894 b1893 v11_1_rc1 b1817 b1812 2015_08 2015_09 b2376 w_2015_35 w_2015_37 w_2015_36 b2108 w_2015_38 b1710 b1711 b2162 b1716 b2007 b1888 b1880 v11_0 b1802 b1809 dax_2016_05 dax_2016_04 dax_2016_03 dax_2016_02 dax_2016_01 current w_2016_06 qserv-test w_2016_03 b2295 b1969 w_2016_08 b1781 b2393 b1765 b1764 b1767 b1761 t20150915-b1692 b2443 b1867 b1687 b2247 b2244 qserv_2016_06 b1875 t20150914-b1688 w_2016_15 v11_0_rc2 v11_0_rc3 w_2016_10 b1872 b1790 b1791 fe_test v12_1_1 v12_1_2 m_2015_10 qserv_latest b1778 w_2016_28 b2285 b2317 b1643 b2098 w_2016_20 b2254 w_2016_26 b1694 b1908 b1947 b1865 b1647 t20150914-b1690 b1900 b1689 b2115 b1997 b1748 n_2015_10_29 b1852 b1918 qserv_2016_08 b1856 b1679 fe_test_dax b1677 qserv_2016_02 qserv_2016_01 b2221 b1675 qserv_2016_05 qserv_2016_04 qserv_2016_03 b2043 b2122 qserv_2015_10 b1641 v12_1 noanaconda b1690 b1693 b1692 b1755 v12_1_2_rc1 b1753 b1926 b1922 t20150914-b1689 b1849 test w_2016_12 fe_test4 w_2016_05 fe_test2 b1842 b1843 qserv b2294 v12_1_rc1 b2296 v11_0_rc1 b2478 b2058 b2293 b1728 b1683 fe_test_qserv b1725 b1688 w_2015_39 qserv_2015_11 w_2015_50 b1935 v12_0_rc1 dax_2016_06 setup
apr                   1.5.2      	sims b2060 dax_latest b2065 b2069 b2068 b2214 b2211 b2219 qserv-dev b2114 b2113 b1942 b2171 b2172 b2412 test w_2016_39 b2261 b2393 w_2016_08 b2453 t_2016_34_2 b2108 b2115 b2162 b2007 t_2016_34 dax_2016_08 dax_2016_06 dax_2016_05 dax_2016_04 dax_2016_03 dax_2016_02 current qserv-test b2295 b2466 b1969 b2376 b2151 b2404 b2159 b2346 b2249 b2247 b2244 b2478 w_2016_15 w_2016_12 w_2016_10 v12_1_2_rc1 b2471 b2474 w_2016_19 fe_test b2417 v12_1_1 b2413 b2410 v12_1_2 qserv_latest w_2016_28 b2043 b2317 b2095 b2098 w_2016_20 b2254 w_2016_26 b1947 sims_2_3_2 w_2016_46 sims_2_3_0 sims_2_3_1 b2446 t_2016_44_3 t_2016_44_2 b2443 b1997 w_2016_38 b2307 t_2016_44 t_2016_45 w_2016_34 w_2016_35 w_2016_36 w_2016_37 w_2016_32 ephemtest qserv_2016_08 fe_test_dax qserv_2016_03 qserv_2016_02 b2221 qserv_2016_06 qserv_2016_05 qserv_2016_04 b2280 b2285 b2122 b2289 b2288 v12_1 v12_0 dax_F16_2016_11_pre1 b1926 b1922 b2332 b2030 b2238 w_2016_41 w_2016_40 w_2016_43 w_2016_42 w_2016_45 w_2016_44 w_2016_47 w_latest b2294 v12_1_rc1 b2296 b2058 b2293 fe_test_qserv b1935 v12_0_rc1 b2323 b2435 b2202 setup
apr_util              1.5.4      	sims b2060 dax_latest b2065 b2069 b2068 b2214 b2211 b2219 qserv-dev b2114 b2113 b1942 b2171 b2172 b2412 test w_2016_39 b2261 b2393 w_2016_08 b2453 t_2016_34_2 b2108 b2115 b2162 b2007 t_2016_34 dax_2016_08 dax_2016_06 dax_2016_05 dax_2016_04 dax_2016_03 dax_2016_02 current qserv-test b2295 b2466 b1969 b2376 b2151 b2404 b2159 b2346 b2249 b2247 b2244 b2478 w_2016_15 w_2016_12 w_2016_10 v12_1_2_rc1 b2471 b2474 w_2016_19 fe_test b2417 v12_1_1 b2413 b2410 v12_1_2 qserv_latest w_2016_28 b2043 b2317 b2095 b2098 w_2016_20 b2254 w_2016_26 b1947 sims_2_3_2 w_2016_46 sims_2_3_0 sims_2_3_1 b2446 t_2016_44_3 t_2016_44_2 b2443 b1997 w_2016_38 b2307 t_2016_44 t_2016_45 w_2016_34 w_2016_35 w_2016_36 w_2016_37 w_2016_32 ephemtest qserv_2016_08 fe_test_dax qserv_2016_03 qserv_2016_02 b2221 qserv_2016_06 qserv_2016_05 qserv_2016_04 b2280 b2285 b2122 b2289 b2288 v12_1 v12_0 dax_F16_2016_11_pre1 b1926 b1922 b2332 b2030 b2238 w_2016_41 w_2016_40 w_2016_43 w_2016_42 w_2016_45 w_2016_44 w_2016_47 w_latest b2294 v12_1_rc1 b2296 b2058 b2293 fe_test_qserv b1935 v12_0_rc1 b2323 b2435 b2202 setup
base                  12.1-1-g5ff2bce 	sims b2417 b2413 dax_F16_2016_11_pre1 b2435 b2443 current qserv-dev sims_2_3_2 b2446 test b2466 w_2016_45 w_2016_47 w_latest t_2016_44_3 t_2016_44_2 t_2016_45 b2478 b2453 b2471 w_2016_46 b2474 setup
boost                 1.60.lsst1+1 	sims b2417 b2412 b2413 b2410 dax_F16_2016_11_pre1 b2453 b2332 current qserv-dev sims_2_3_2 b2446 test b2466 w_2016_43 w_2016_42 w_2016_45 b2376 w_2016_47 w_2016_46 b2404 b2393 t_2016_44_3 t_2016_44_2 w_2016_41 b2443 t_2016_44 t_2016_45 w_2016_44 b2478 b2435 b2346 b2471 w_latest b2474 setup
db                    12.1-1-gdcaa69e+1 	b2453 t_2016_45 b2443 current b2435 qserv-dev b2446 w_2016_45 w_2016_46 setup
doxygen               1.8.5.lsst1 	sims b2060 dax_latest b2065 dax_2016_03 b2069 b2068 b1918 sims_2_2_2 sims_2_2_1 b2214 w_2016_05 opsim_3_3_8 b2211 opsim_3_3_6 opsim_3_3_7 b2219 qserv-dev b1947 b2113 b1865 b1942 b2171 b2036 b2172 b2412 sims_2_2_4b sims_2_2_4c test b1899 b1894 b1893 fe_test4 b2307 b2261 w_2016_08 b2453 b2102 b2103 t_2016_34_2 b2346 b2115 b2162 b2003 b2002 b2007 b1888 t_2016_34 b1880 b1882 b1887 dax_2016_08 dax_2016_06 dax_2016_05 dax_2016_04 sims_2_2_3 dax_2016_02 dax_2016_01 sims_2_2_0 current b1962 w_2016_06 qserv-test b2295 b2466 b1969 b2376 b2088 b2151 b2404 b2393 b2108 b2091 b2159 b2221 b2084 b2249 b2247 b2246 b2244 b1875 w_2016_15 w_2016_12 w_2016_10 b1872 v12_1_2_rc1 b2471 b2474 b1971 w_2016_19 b2099 fe_test b2417 v12_1_1 b2413 b2410 v12_1_2 b1980 b1982 b1989 qserv_latest w_2016_28 b2043 b2317 b1867 b2098 w_2016_20 b2254 w_2016_26 b1866 b1908 b2114 sims_2_3_2 w_2016_46 sims_2_3_0 sims_2_3_1 b1900 b2446 t_2016_44_3 t_2016_44_2 b2255 b1990 b2443 b1997 b1995 b1999 w_2016_38 w_2016_39 t_2016_44 t_2016_45 w_2016_34 w_2016_35 w_2016_36 w_2016_37 w_2016_32 ephemtest qserv_2016_08 fe_test_dax qserv_2016_03 qserv_2016_02 qserv_2016_01 b1916 qserv_2016_06 qserv_2016_05 qserv_2016_04 sims_development b2280 b2285 b2122 b2289 b2288 v12_1 v12_0 noanaconda dax_F16_2016_11_pre1 b1926 b1923 b1922 b1921 b2332 b2030 b2238 w_2016_41 w_2016_40 w_2016_43 w_2016_42 w_2016_45 w_2016_44 w_2016_47 w_latest b2294 v12_1_rc1 b2296 b2478 b2058 b2293 b2095 fe_test_qserv b1935 v12_0_rc1 b2323 sims_2_2_6 b2435 fe_test3 sims_2_2_4 sims_testing b2202 setup
flask                 0.10.1.lsst2+2 	b2478 b2393 qserv-dev current b2443 test dax_F16_2016_11_pre1 b2474 b2376 w_latest setup
libevent              2.0.16.lsst2 	b2060 b2065 b2069 b2068 w_2016_05 w_2015_47 qserv-dev b2114 b2113 b1942 b1823 b1824 b1825 dax_2015_11 b1899 b1894 b1893 v11_1_rc1 b1817 b1812 b2376 b2108 b2115 b2162 b2007 b1888 b1880 qserv b1802 dax_2016_06 dax_2016_05 dax_2016_04 dax_2016_03 dax_2016_02 dax_2016_01 current w_2016_06 qserv-test w_2016_03 b2295 b1969 w_2016_08 b2393 b2247 b2244 b2478 w_2016_15 w_2016_12 w_2016_10 b1872 b1790 b1791 fe_test v12_1_1 v12_1_2 qserv_latest w_2016_28 b2043 b2317 b1867 b2098 w_2016_20 b2254 w_2016_26 b1908 b1947 b1865 b1900 b2443 b1997 b1852 b1918 qserv_2016_08 b1856 fe_test_dax qserv_2016_03 qserv_2016_02 qserv_2016_01 b2221 qserv_2016_06 qserv_2016_05 qserv_2016_04 b2285 b2122 v12_1 noanaconda b1875 b1922 b1849 test fe_test4 b1842 b1843 b1926 b2294 v12_1_rc1 b2296 b2058 b2293 v12_1_2_rc1 fe_test_qserv qserv_2015_11 w_2015_50 b1935 v12_0_rc1 b1809 setup
log                   12.1-4-gad3b865+2 	sims b2478 dax_F16_2016_11_pre1 t_2016_45 b2466 b2443 current b2435 qserv-dev sims_2_3_2 b2474 b2446 test b2471 b2453 w_2016_46 w_2016_45 w_2016_47 w_latest setup
log4cxx               0.10.0.lsst7 	sims b2478 dax_F16_2016_11_pre1 t_2016_45 b2466 b2443 current b2435 qserv-dev sims_2_3_2 b2474 b2446 test b2471 b2453 w_2016_46 w_2016_45 w_2016_47 w_latest setup
lsst                  12.1.rc1-1-g32aa4ec 	b2261 b2280 w_2016_38 b2249 b2285 dax_2016_08 v12_1_rc1 b2289 b2288 b2255 b2293 current dax_latest w_2016_39 setup
lua                   5.1.4.lsst1 	b2060 b2065 b2069 b2068 b1731 w_2015_44 w_2015_45 w_2015_47 w_2015_40 w_2015_43 qserv-dev b2114 b2113 b1942 b1823 b1824 b1825 b1700 dax_2015_11 dax_2015_10 b1709 b1660 b1899 b1894 b1893 v11_1_rc1 b1817 b1812 2015_08 2015_09 b2376 w_2015_35 w_2015_37 w_2015_36 b2108 w_2015_38 b1710 b1711 b2162 b1716 b2007 b1888 b1880 v11_0 b1802 b1809 dax_2016_05 dax_2016_04 dax_2016_03 dax_2016_02 dax_2016_01 current w_2016_06 qserv-test w_2016_03 b2295 b1969 w_2016_08 b1781 b2393 b1765 b1764 b1767 b1761 t20150915-b1692 b2443 b1867 b1687 b2247 b2244 qserv_2016_06 b1875 t20150914-b1688 w_2016_15 v11_0_rc2 v11_0_rc3 w_2016_10 b1872 b1790 b1791 fe_test v12_1_1 v12_1_2 m_2015_10 qserv_latest b1778 w_2016_28 b2285 b2317 b1643 b2098 w_2016_20 b2254 w_2016_26 b1694 b1908 b1947 b1865 b1647 t20150914-b1690 b1900 b1689 b2115 b1997 b1748 n_2015_10_29 b1852 b1918 qserv_2016_08 b1856 b1679 fe_test_dax b1677 qserv_2016_02 qserv_2016_01 b2221 b1675 qserv_2016_05 qserv_2016_04 qserv_2016_03 b2043 b2122 qserv_2015_10 b1641 v12_1 noanaconda b1690 b1693 b1692 b1755 v12_1_2_rc1 b1753 b1926 b1922 t20150914-b1689 b1849 test w_2016_12 fe_test4 w_2016_05 fe_test2 b1842 b1843 qserv b2294 v12_1_rc1 b2296 v11_0_rc1 b2478 b2058 b2293 b1728 b1683 fe_test_qserv b1725 b1688 w_2015_39 qserv_2015_11 w_2015_50 b1935 v12_0_rc1 dax_2016_06 setup
mariadb               10.1.18-1-g0e935dc 	b2453 t_2016_45 b2443 current b2435 qserv-dev b2446 w_2016_45 w_2016_46 setup
mariadbclient         10.1.18-1-g12235e0 	b2453 t_2016_45 b2443 current b2435 qserv-dev b2446 w_2016_45 w_2016_46 setup
mysqlproxy            0.8.5+15   	current b2443 qserv-dev setup
mysqlpython           1.2.3.lsst2+9 	b2453 t_2016_45 b2443 current b2435 qserv-dev b2446 w_2016_45 w_2016_46 setup
partition             12.0+9     	b2478 b2393 qserv-dev current b2443 test b2376 setup
protobuf              2.6.1.lsst4+1 	b2478 b2393 qserv-dev current b2443 test b2376 setup
python                0.0.6      	sims qserv-dev b2446 b2412 w_2016_41 b2393 b2453 b2346 w_2016_46 b2466 b2376 b2404 b2478 b2471 b2474 b2417 b2413 b2410 sims_2_3_2 t_2016_44_3 t_2016_44_2 b2443 t_2016_44 t_2016_45 dax_F16_2016_11_pre1 b2332 test w_2016_43 w_2016_42 w_2016_45 w_2016_44 w_2016_47 w_latest b2326 b2435 setup
python_future         0.15.2+2   	sims b2417 b2412 b2413 b2410 dax_F16_2016_11_pre1 b2453 b2332 current qserv-dev sims_2_3_2 b2446 test b2466 w_2016_43 w_2016_42 w_2016_45 b2376 w_2016_47 w_2016_46 b2404 b2393 t_2016_44_3 t_2016_44_2 w_2016_41 b2443 t_2016_44 t_2016_45 w_2016_44 b2478 b2435 b2346 b2471 w_latest b2474 setup
python_mysqlclient    1.3.7.lsst1+6 	b2453 t_2016_45 b2443 current b2435 qserv-dev b2446 w_2016_45 w_2016_46 setup
pyyaml                3.11.lsst1+3 	sims b2417 b2412 b2413 b2410 dax_F16_2016_11_pre1 b2453 b2332 current qserv-dev sims_2_3_2 b2446 test b2466 w_2016_43 w_2016_42 w_2016_45 b2376 w_2016_47 w_2016_46 b2404 b2393 t_2016_44_3 t_2016_44_2 w_2016_41 b2443 t_2016_44 t_2016_45 w_2016_44 b2478 b2435 b2346 b2471 w_latest b2474 setup
qserv                 12.1-13-g5513aea+3 	current b2443 qserv-dev setup
qserv_distrib         1.0.0+641  	current b2443 qserv-dev setup
qserv_testdata        12.0+68    	current b2443 qserv-dev setup
requests              2.9.1.lsst1+1 	b2478 current b2443 test qserv-dev setup
scisql                0.3.5+22   	b2453 t_2016_45 b2443 current b2435 qserv-dev b2446 w_2016_45 w_2016_46 setup
scons                 2.5.0.lsst2+1 	sims qserv-dev b2446 b2412 w_2016_41 b2393 b2453 b2346 w_2016_46 b2466 b2376 b2404 b2478 b2471 b2474 b2417 b2413 b2410 sims_2_3_2 t_2016_44_3 t_2016_44_2 b2443 t_2016_44 t_2016_45 dax_F16_2016_11_pre1 b2332 test w_2016_43 w_2016_42 w_2016_45 w_2016_44 w_2016_47 w_latest b2435 setup
sconsUtils            12.1+1     	sims b2417 b2412 b2413 b2410 b2332 b2404 dax_F16_2016_11_pre1 qserv-dev sims_2_3_2 b2446 test b2466 w_2016_43 w_2016_42 w_2016_45 b2376 w_2016_47 w_2016_46 b2453 b2393 t_2016_44_3 t_2016_44_2 w_2016_41 b2443 t_2016_45 t_2016_44 w_2016_44 b2478 b2435 b2346 b2471 w_latest b2474 setup
sphgeom               12.1+2     	b2478 current b2443 test qserv-dev setup
sqlalchemy            1.0.8.lsst3+3 	sims b2417 b2412 b2413 b2410 dax_F16_2016_11_pre1 b2453 b2332 current qserv-dev sims_2_3_2 b2446 test b2466 w_2016_43 w_2016_42 w_2016_45 b2376 w_2016_47 w_2016_46 b2404 b2393 t_2016_44_3 t_2016_44_2 w_2016_41 b2443 t_2016_44 t_2016_45 w_2016_44 b2478 b2435 b2346 b2471 w_latest b2474 setup
swig                  3.0.10     	sims dax_latest b2214 b2211 b2219 qserv-dev b2446 b2171 b2172 b2412 w_2016_41 b2307 b2261 b2393 b2453 t_2016_34_2 b2346 w_2016_46 b2162 t_2016_34 dax_2016_08 current qserv-test b2295 b2466 b2376 b2151 b2404 b2159 b2249 b2247 b2244 b2478 v12_1_2_rc1 b2471 b2474 fe_test b2417 v12_1_1 b2413 b2410 v12_1_2 qserv_latest b2317 b2254 b2443 sims_2_3_2 sims_2_3_0 sims_2_3_1 t_2016_44_3 t_2016_44_2 w_2016_38 w_2016_39 t_2016_44 t_2016_45 w_2016_34 w_2016_35 w_2016_36 w_2016_37 w_2016_32 ephemtest qserv_2016_08 b2221 b2280 b2285 b2289 b2288 v12_1 dax_F16_2016_11_pre1 b2332 b2238 test w_2016_40 w_2016_43 w_2016_42 w_2016_45 w_2016_44 w_2016_47 w_latest b2294 v12_1_rc1 b2296 b2293 b2323 b2435 b2202 setup
xrootd                lsst-dev-g7b8f5ca36f 	b2478 current b2443 test qserv-dev setup
qserv@qserv-user-master-1:/qserv/run/var/log/work/qserv_testdata$ 
qserv@qserv-user-master-1:/qserv/run/var/log/work/qserv_testdata$ 
qserv@qserv-user-master-1:/qserv/run/var/log/work/qserv_testdata$ setup -k -r .                   
qserv@qserv-user-master-1:/qserv/run/var/log/work/qserv_testdata$ cd datasets/case0
case01/ case02/ case03/ case04/ case05/ 
qserv@qserv-user-master-1:/qserv/run/var/log/work/qserv_testdata$ cd datasets/case0
case01/ case02/ case03/ case04/ case05/ 
qserv@qserv-user-master-1:/qserv/run/var/log/work/qserv_testdata$ cd datasets/     
qserv@qserv-user-master-1:/qserv/run/var/log/work/qserv_testdata/datasets$ du -skh *
2.3M	case01
1.1M	case02
77M	case03
30M	case04
3.8M	case05
qserv@qserv-user-master-1:/qserv/run/var/log/work/qserv_testdata/datasets$ cp -r case03/ case06
qserv@qserv-user-master-1:/qserv/run/var/log/work/qserv_testdata/datasets$ cd ..
qserv@qserv-user-master-1:/qserv/run/var/log/work/qserv_testdata$ ls
README.txt  SConstruct  bin  datasets  python  ups
qserv@qserv-user-master-1:/qserv/run/var/log/work/qserv_testdata$ 
qserv@qserv-user-master-1:/qserv/run/var/log/work/qserv_testdata$ 
qserv@qserv-user-master-1:/qserv/run/var/log/work/qserv_testdata$ qserv-check-integration.py --help
usage: qserv-check-integration.py [-h] [-V LOG_CONF] [-i CASE_ID]
                                  [-m {mysql,qserv,all}] [-l]
                                  [-t TESTDATA_DIR] [-o OUT_DIR]
                                  [-s STOP_AT_QUERY] [-T WORK_DIR] [-C] [-D]
                                  [-I CUSTOM_CASE_ID] [-U USERNAME]

Launch one Qserv integration test with fine-grained parameters, usefull for
developers in order to debug/test manually a specific part of Qserv.
Configuration values are read from ~/.lsst/qserv.conf.

optional arguments:
  -h, --help            show this help message and exit
  -V LOG_CONF, --log-cfg LOG_CONF
                        Absolute path to file containing pythonlogger standard
                        configuration file (default:
                        /home/qserv/.lsst/logging.ini)

General options:
  Options related to data loading and querying

  -i CASE_ID, --case-id CASE_ID
                        Test case number (default: 01)
  -m {mysql,qserv,all}, --mode {mysql,qserv,all}
                        Qserv test modes (direct mysql connection, or via
                        qserv) (default: all)

Load options:
  Options related to data loading

  -l, --load            Load test dataset prior to query execution (default:
                        False)
  -t TESTDATA_DIR, --testdata-dir TESTDATA_DIR
                        Absolute path to directory containing test datasets.
                        This value is set, by precedence, by this option, and
                        then by QSERV_TESTDATA_DIR/datasets/ if
                        QSERV_TESTDATA_DIR environment variable is not empty
                        (default:
                        /qserv/run/var/log/work/qserv_testdata/datasets)

Query options:
  Options related to query execution

  -o OUT_DIR, --out-dir OUT_DIR
                        Absolute path to directory for storing query
                        results.The results will be stored in
                        <OUT_DIR>/qservTest_case<CASE_ID>/ (default:
                        /qserv/run/tmp)
  -s STOP_AT_QUERY, --stop-at-query STOP_AT_QUERY
                        Stop at query with given number (default: 10000)

Input dataset customization options:
  Options related to input data set customization

  -T WORK_DIR, --work-dir WORK_DIR
                        Absolute path to parent directory where source test
                        datasets will be copied, and big datasets will be
                        eventually downloaded (default: /qserv/run/tmp)
  -C, --custom          If <WORK_DIR>/case<CASE_ID> doesn't exists, copy it
                        from <TESTDATA_DIR>, disable load and query
                        operations, and had to be performed before them
                        (default: False)
  -D, --download        Download big datasets using rsync over ssh, implies
                        --custom, enable batch mode with ~/.ssh/config and
                        ssh-agent (default: False)
  -I CUSTOM_CASE_ID, --custom-case-id CUSTOM_CASE_ID
                        Rename custom test to case/CUSTOM_CASE_ID (default:
                        None)
  -U USERNAME, --username USERNAME
                        rsync username (default: None)
qserv@qserv-user-master-1:/qserv/run/var/log/work/qserv_testdata$ qserv-check-integration.py --load --case=06
2016-12-14 13:13:58,784 - lsst.qserv.tests.benchmark - INFO - Loading data from /qserv/run/var/log/work/qserv_testdata/datasets/case06/data (mysql mode)
2016-12-14 13:13:58,785 - lsst.qserv.tests.mysqlDbLoader - INFO - Create, load table Science_Ccd_Exposure_Metadata_coadd_r
2016-12-14 13:14:00,585 - lsst.qserv.tests.mysqlDbLoader - INFO - Partitioned data loaded for table Science_Ccd_Exposure_Metadata_coadd_r
2016-12-14 13:14:00,585 - lsst.qserv.tests.mysqlDbLoader - INFO - Create, load table AvgForcedPhotYearly
2016-12-14 13:14:00,908 - lsst.qserv.tests.mysqlDbLoader - INFO - Partitioned data loaded for table AvgForcedPhotYearly
2016-12-14 13:14:00,909 - lsst.qserv.tests.mysqlDbLoader - INFO - Create, load table Science_Ccd_Exposure_Metadata
2016-12-14 13:14:06,103 - lsst.qserv.tests.mysqlDbLoader - INFO - Partitioned data loaded for table Science_Ccd_Exposure_Metadata
2016-12-14 13:14:06,103 - lsst.qserv.tests.mysqlDbLoader - INFO - Create, load table ZZZ_Db_Description
2016-12-14 13:14:06,398 - lsst.qserv.tests.mysqlDbLoader - INFO - Partitioned data loaded for table ZZZ_Db_Description
2016-12-14 13:14:06,399 - lsst.qserv.tests.mysqlDbLoader - INFO - Create, load table RefObject
2016-12-14 13:14:06,644 - lsst.qserv.tests.mysqlDbLoader - INFO - Partitioned data loaded for table RefObject
2016-12-14 13:14:06,644 - lsst.qserv.tests.mysqlDbLoader - INFO - Create, load table RefDeepSrcMatch
2016-12-14 13:14:06,892 - lsst.qserv.tests.mysqlDbLoader - INFO - Partitioned data loaded for table RefDeepSrcMatch
2016-12-14 13:14:06,892 - lsst.qserv.tests.mysqlDbLoader - INFO - Create, load table Science_Ccd_Exposure_coadd_r
2016-12-14 13:14:07,182 - lsst.qserv.tests.mysqlDbLoader - INFO - Partitioned data loaded for table Science_Ccd_Exposure_coadd_r
2016-12-14 13:14:07,183 - lsst.qserv.tests.mysqlDbLoader - INFO - Create, load table Science_Ccd_Exposure
2016-12-14 13:14:07,505 - lsst.qserv.tests.mysqlDbLoader - INFO - Partitioned data loaded for table Science_Ccd_Exposure
2016-12-14 13:14:07,505 - lsst.qserv.tests.mysqlDbLoader - INFO - Create, load table AvgForcedPhot
2016-12-14 13:14:07,760 - lsst.qserv.tests.mysqlDbLoader - INFO - Partitioned data loaded for table AvgForcedPhot
2016-12-14 13:14:07,760 - lsst.qserv.tests.mysqlDbLoader - INFO - Create, load table DeepCoadd_To_Htm10
2016-12-14 13:14:08,012 - lsst.qserv.tests.mysqlDbLoader - INFO - Partitioned data loaded for table DeepCoadd_To_Htm10
2016-12-14 13:14:08,012 - lsst.qserv.tests.mysqlDbLoader - INFO - Create, load table LeapSeconds
2016-12-14 13:14:08,256 - lsst.qserv.tests.mysqlDbLoader - INFO - Partitioned data loaded for table LeapSeconds
2016-12-14 13:14:08,256 - lsst.qserv.tests.mysqlDbLoader - INFO - Create, load table DeepCoadd
2016-12-14 13:14:08,498 - lsst.qserv.tests.mysqlDbLoader - INFO - Partitioned data loaded for table DeepCoadd
2016-12-14 13:14:08,499 - lsst.qserv.tests.mysqlDbLoader - INFO - Create, load table DeepCoadd_Metadata
2016-12-14 13:14:08,737 - lsst.qserv.tests.mysqlDbLoader - INFO - Partitioned data loaded for table DeepCoadd_Metadata
2016-12-14 13:14:08,738 - lsst.qserv.tests.mysqlDbLoader - INFO - Create, load table Science_Ccd_Exposure_To_Htm10_coadd_r
2016-12-14 13:14:09,027 - lsst.qserv.tests.mysqlDbLoader - INFO - Partitioned data loaded for table Science_Ccd_Exposure_To_Htm10_coadd_r
2016-12-14 13:14:09,028 - lsst.qserv.tests.mysqlDbLoader - INFO - Create, load table LeapSeconds
2016-12-14 13:14:09,255 - lsst.qserv.tests.mysqlDbLoader - INFO - Partitioned data loaded for table LeapSeconds
2016-12-14 13:14:09,255 - lsst.qserv.tests.mysqlDbLoader - INFO - Create, load table DeepCoadd
2016-12-14 13:14:09,494 - lsst.qserv.tests.mysqlDbLoader - INFO - Partitioned data loaded for table DeepCoadd
2016-12-14 13:14:09,494 - lsst.qserv.tests.mysqlDbLoader - INFO - Create, load table DeepCoadd_Metadata
2016-12-14 13:14:09,727 - lsst.qserv.tests.mysqlDbLoader - INFO - Partitioned data loaded for table DeepCoadd_Metadata
2016-12-14 13:14:09,728 - lsst.qserv.tests.mysqlDbLoader - INFO - Create, load table Filter
2016-12-14 13:14:09,959 - lsst.qserv.tests.mysqlDbLoader - INFO - Partitioned data loaded for table Filter
2016-12-14 13:14:09,960 - lsst.qserv.tests.mysqlDbLoader - INFO - Create, load table RunDeepSource
2016-12-14 13:14:10,275 - lsst.qserv.tests.mysqlDbLoader - INFO - Partitioned data loaded for table RunDeepSource
2016-12-14 13:14:10,275 - lsst.qserv.tests.mysqlDbLoader - INFO - Create, load table RunDeepForcedSource
2016-12-14 13:14:19,218 - lsst.qserv.tests.mysqlDbLoader - INFO - Partitioned data loaded for table RunDeepForcedSource
2016-12-14 13:14:19,219 - lsst.qserv.tests.benchmark - INFO - Launch 0002.1_fetchRunAndFieldById.sql against mysql
2016-12-14 13:14:19,327 - lsst.qserv.tests.benchmark - INFO - Launch 0002.2_fetchRunAndFieldById.sql against mysql
2016-12-14 13:14:19,335 - lsst.qserv.tests.benchmark - INFO - Launch 0006_selectExposure.sql against mysql
2016-12-14 13:14:19,343 - lsst.qserv.tests.benchmark - INFO - Launch 0009_selectCCDExposure.sql against mysql
2016-12-14 13:14:19,350 - lsst.qserv.tests.benchmark - INFO - Launch 0011_selectDeepCoadd.sql against mysql
2016-12-14 13:14:19,355 - lsst.qserv.tests.benchmark - INFO - Launch 0012_selectDistinctDeepCoaddWithGivenTractPatchFiltername.sql against mysql
2016-12-14 13:14:19,361 - lsst.qserv.tests.benchmark - INFO - Launch 0013_selectDeepCoadd2.sql against mysql
2016-12-14 13:14:19,367 - lsst.qserv.tests.benchmark - INFO - Launch 0014_selectDeepCoadd3.sql against mysql
2016-12-14 13:14:19,373 - lsst.qserv.tests.benchmark - INFO - Launch 0018_selectDeepCoaddWithGivenTractPatchFiltername.sql against mysql
2016-12-14 13:14:19,379 - lsst.qserv.tests.benchmark - INFO - Launch 0019.1_selectRunDeepSourceDeepcoaddDeepsrcmatchRefobject.sql against mysql
2016-12-14 13:14:19,386 - lsst.qserv.tests.benchmark - INFO - Launch 0019.2_selectRunDeepSourceDeepcoaddDeepsrcmatchRefobject.sql against mysql
2016-12-14 13:14:19,392 - lsst.qserv.tests.benchmark - INFO - Launch 0022_selectScienceCCDExposureWithFilternameFieldCamcolRun.sql against mysql
2016-12-14 13:14:19,399 - lsst.qserv.tests.benchmark - INFO - Launch 0023_selectScienceCCDExposureWithFilternameFieldCamcolRun.sql against mysql
2016-12-14 13:14:19,406 - lsst.qserv.tests.benchmark - INFO - Launch 0025_selectScienceCCDExposureWithFilternameFieldCamcolRun.sql against mysql
2016-12-14 13:14:19,413 - lsst.qserv.tests.benchmark - INFO - Launch 0028_selectScienceCCDExposure.sql against mysql
2016-12-14 13:14:19,421 - lsst.qserv.tests.benchmark - INFO - Launch 0031_selectEmptyString.sql against mysql
2016-12-14 13:14:19,427 - lsst.qserv.tests.benchmark - INFO - Test case #06: 16 queries launched on a total of 54
2016-12-14 13:14:19,432 - lsst.qserv.tests.qservDbLoader - INFO - Running on node: worker1
2016-12-14 13:14:19,432 - lsst.qserv.tests.qservDbLoader - INFO - Running on node: worker3
2016-12-14 13:14:19,432 - lsst.qserv.tests.qservDbLoader - INFO - Running on node: worker2
2016-12-14 13:14:19,432 - lsst.qserv.tests.qservDbLoader - INFO - Running on node: worker4
2016-12-14 13:14:19,432 - lsst.qserv.tests.qservDbLoader - INFO - Drop and create MySQL database for Qserv: qservTest_case06_qserv
2016-12-14 13:14:19,539 - lsst.qserv.tests.qservDbLoader - INFO - Drop CSS database for Qserv
2016-12-14 13:14:19,540 - lsst.qserv.tests.qservDbLoader - INFO - Drop CSS database: qservTest_case06_qserv
2016-12-14 13:14:19,540 - lsst.qserv.tests.benchmark - INFO - Loading data from /qserv/run/var/log/work/qserv_testdata/datasets/case06/data (qserv mode)
2016-12-14 13:14:19,540 - lsst.qserv.tests.qservDbLoader - INFO - Partition data, create and load table Science_Ccd_Exposure_Metadata_coadd_r
2016-12-14 13:14:26,081 - lsst.qserv.tests.qservDbLoader - INFO - Partitioned data loaded for table Science_Ccd_Exposure_Metadata_coadd_r
2016-12-14 13:14:26,082 - lsst.qserv.tests.qservDbLoader - INFO - Partition data, create and load table AvgForcedPhotYearly
2016-12-14 13:14:27,020 - lsst.qserv.tests.qservDbLoader - INFO - Partitioned data loaded for table AvgForcedPhotYearly
2016-12-14 13:14:27,021 - lsst.qserv.tests.qservDbLoader - INFO - Partition data, create and load table Science_Ccd_Exposure_Metadata
2016-12-14 13:14:46,233 - lsst.qserv.tests.qservDbLoader - INFO - Partitioned data loaded for table Science_Ccd_Exposure_Metadata
2016-12-14 13:14:46,234 - lsst.qserv.tests.qservDbLoader - INFO - Partition data, create and load table ZZZ_Db_Description
2016-12-14 13:14:46,752 - lsst.qserv.tests.qservDbLoader - INFO - Partitioned data loaded for table ZZZ_Db_Description
2016-12-14 13:14:46,752 - lsst.qserv.tests.qservDbLoader - INFO - Partition data, create and load table RefObject
2016-12-14 13:14:47,235 - lsst.qserv.tests.qservDbLoader - INFO - Partitioned data loaded for table RefObject
2016-12-14 13:14:47,235 - lsst.qserv.tests.qservDbLoader - INFO - Partition data, create and load table RefDeepSrcMatch
2016-12-14 13:14:47,734 - lsst.qserv.tests.qservDbLoader - INFO - Partitioned data loaded for table RefDeepSrcMatch
2016-12-14 13:14:47,734 - lsst.qserv.tests.qservDbLoader - INFO - Partition data, create and load table Science_Ccd_Exposure_coadd_r
2016-12-14 13:14:48,309 - lsst.qserv.tests.qservDbLoader - INFO - Partitioned data loaded for table Science_Ccd_Exposure_coadd_r
2016-12-14 13:14:48,309 - lsst.qserv.tests.qservDbLoader - INFO - Partition data, create and load table Science_Ccd_Exposure
2016-12-14 13:14:49,093 - lsst.qserv.tests.qservDbLoader - INFO - Partitioned data loaded for table Science_Ccd_Exposure
2016-12-14 13:14:49,094 - lsst.qserv.tests.qservDbLoader - INFO - Partition data, create and load table AvgForcedPhot
2016-12-14 13:14:49,599 - lsst.qserv.tests.qservDbLoader - INFO - Partitioned data loaded for table AvgForcedPhot
2016-12-14 13:14:49,599 - lsst.qserv.tests.qservDbLoader - INFO - Partition data, create and load table DeepCoadd_To_Htm10
2016-12-14 13:14:50,146 - lsst.qserv.tests.qservDbLoader - INFO - Partitioned data loaded for table DeepCoadd_To_Htm10
2016-12-14 13:14:50,146 - lsst.qserv.tests.qservDbLoader - INFO - Partition data, create and load table LeapSeconds
2016-12-14 13:14:50,652 - lsst.qserv.tests.qservDbLoader - INFO - Partitioned data loaded for table LeapSeconds
2016-12-14 13:14:50,652 - lsst.qserv.tests.qservDbLoader - INFO - Partition data, create and load table DeepCoadd
2016-12-14 13:14:51,179 - lsst.qserv.tests.qservDbLoader - INFO - Partitioned data loaded for table DeepCoadd
2016-12-14 13:14:51,179 - lsst.qserv.tests.qservDbLoader - INFO - Partition data, create and load table DeepCoadd_Metadata
2016-12-14 13:14:51,690 - lsst.qserv.tests.qservDbLoader - INFO - Partitioned data loaded for table DeepCoadd_Metadata
2016-12-14 13:14:51,690 - lsst.qserv.tests.qservDbLoader - INFO - Partition data, create and load table Science_Ccd_Exposure_To_Htm10_coadd_r
2016-12-14 13:14:52,338 - lsst.qserv.tests.qservDbLoader - INFO - Partitioned data loaded for table Science_Ccd_Exposure_To_Htm10_coadd_r
2016-12-14 13:14:52,338 - lsst.qserv.tests.qservDbLoader - INFO - Partition data, create and load table LeapSeconds
2016-12-14 13:14:52,788 - lsst.qserv.tests.qservDbLoader - INFO - Partitioned data loaded for table LeapSeconds
2016-12-14 13:14:52,789 - lsst.qserv.tests.qservDbLoader - INFO - Partition data, create and load table DeepCoadd
2016-12-14 13:14:53,271 - lsst.qserv.tests.qservDbLoader - INFO - Partitioned data loaded for table DeepCoadd
2016-12-14 13:14:53,271 - lsst.qserv.tests.qservDbLoader - INFO - Partition data, create and load table DeepCoadd_Metadata
2016-12-14 13:14:53,814 - lsst.qserv.tests.qservDbLoader - INFO - Partitioned data loaded for table DeepCoadd_Metadata
2016-12-14 13:14:53,815 - lsst.qserv.tests.qservDbLoader - INFO - Partition data, create and load table Filter
2016-12-14 13:14:54,273 - lsst.qserv.tests.qservDbLoader - INFO - Partitioned data loaded for table Filter
2016-12-14 13:14:54,274 - lsst.qserv.tests.qservDbLoader - INFO - Partition data, create and load table RunDeepSource
2016-12-14 13:14:56,152 - lsst.qserv.tests.qservDbLoader - INFO - Partitioned data loaded for table RunDeepSource
2016-12-14 13:14:56,152 - lsst.qserv.tests.qservDbLoader - INFO - Partition data, create and load table RunDeepForcedSource
2016-12-14 13:15:08,726 - lsst.qserv.tests.qservDbLoader - INFO - Partitioned data loaded for table RunDeepForcedSource
2016-12-14 13:15:19,659 - lsst.qserv.tests.benchmark - INFO - Launch 0002.1_fetchRunAndFieldById.sql against qserv
2016-12-14 13:15:29,261 - lsst.qserv.tests.benchmark - INFO - Launch 0002.2_fetchRunAndFieldById.sql against qserv
2016-12-14 13:15:29,368 - lsst.qserv.tests.benchmark - INFO - Launch 0006_selectExposure.sql against qserv
2016-12-14 13:15:29,474 - lsst.qserv.tests.benchmark - INFO - Launch 0009_selectCCDExposure.sql against qserv
2016-12-14 13:15:29,577 - lsst.qserv.tests.benchmark - INFO - Launch 0011_selectDeepCoadd.sql against qserv
2016-12-14 13:15:29,680 - lsst.qserv.tests.benchmark - INFO - Launch 0012_selectDistinctDeepCoaddWithGivenTractPatchFiltername.sql against qserv
2016-12-14 13:15:29,805 - lsst.qserv.tests.benchmark - INFO - Launch 0013_selectDeepCoadd2.sql against qserv
2016-12-14 13:15:29,921 - lsst.qserv.tests.benchmark - INFO - Launch 0014_selectDeepCoadd3.sql against qserv
2016-12-14 13:15:30,023 - lsst.qserv.tests.benchmark - INFO - Launch 0018_selectDeepCoaddWithGivenTractPatchFiltername.sql against qserv
2016-12-14 13:15:30,121 - lsst.qserv.tests.benchmark - INFO - Launch 0019.1_selectRunDeepSourceDeepcoaddDeepsrcmatchRefobject.sql against qserv
2016-12-14 13:15:30,246 - lsst.qserv.tests.benchmark - INFO - Launch 0019.2_selectRunDeepSourceDeepcoaddDeepsrcmatchRefobject.sql against qserv
2016-12-14 13:15:30,390 - lsst.qserv.tests.benchmark - INFO - Launch 0022_selectScienceCCDExposureWithFilternameFieldCamcolRun.sql against qserv
2016-12-14 13:15:30,491 - lsst.qserv.tests.benchmark - INFO - Launch 0023_selectScienceCCDExposureWithFilternameFieldCamcolRun.sql against qserv
2016-12-14 13:15:30,627 - lsst.qserv.tests.benchmark - INFO - Launch 0025_selectScienceCCDExposureWithFilternameFieldCamcolRun.sql against qserv
2016-12-14 13:15:30,728 - lsst.qserv.tests.benchmark - INFO - Launch 0028_selectScienceCCDExposure.sql against qserv
2016-12-14 13:15:30,827 - lsst.qserv.tests.benchmark - INFO - Launch 0031_selectEmptyString.sql against qserv
2016-12-14 13:15:30,924 - lsst.qserv.tests.benchmark - INFO - Test case #06: 16 queries launched on a total of 54
2016-12-14 13:15:30,924 - lsst.qserv.tests.benchmark - INFO - Tables/Views not loaded: ['DeepForcedSource', 'DeepSource']
2016-12-14 13:15:30,926 - lsst.qserv.tests.benchmark - INFO - MySQL/Qserv results are identical
qserv@qserv-user-master-1:/qserv/run/var/log/work/qserv_testdata$ qserv-check-integration.py --help --load --case=06
usage: qserv-check-integration.py [-h] [-V LOG_CONF] [-i CASE_ID]
                                  [-m {mysql,qserv,all}] [-l]
                                  [-t TESTDATA_DIR] [-o OUT_DIR]
                                  [-s STOP_AT_QUERY] [-T WORK_DIR] [-C] [-D]
                                  [-I CUSTOM_CASE_ID] [-U USERNAME]

Launch one Qserv integration test with fine-grained parameters, usefull for
developers in order to debug/test manually a specific part of Qserv.
Configuration values are read from ~/.lsst/qserv.conf.

optional arguments:
  -h, --help            show this help message and exit
  -V LOG_CONF, --log-cfg LOG_CONF
                        Absolute path to file containing pythonlogger standard
                        configuration file (default:
                        /home/qserv/.lsst/logging.ini)

General options:
  Options related to data loading and querying

  -i CASE_ID, --case-id CASE_ID
                        Test case number (default: 01)
  -m {mysql,qserv,all}, --mode {mysql,qserv,all}
                        Qserv test modes (direct mysql connection, or via
                        qserv) (default: all)

Load options:
  Options related to data loading

  -l, --load            Load test dataset prior to query execution (default:
                        False)
  -t TESTDATA_DIR, --testdata-dir TESTDATA_DIR
                        Absolute path to directory containing test datasets.
                        This value is set, by precedence, by this option, and
                        then by QSERV_TESTDATA_DIR/datasets/ if
                        QSERV_TESTDATA_DIR environment variable is not empty
                        (default:
                        /qserv/run/var/log/work/qserv_testdata/datasets)

Query options:
  Options related to query execution

  -o OUT_DIR, --out-dir OUT_DIR
                        Absolute path to directory for storing query
                        results.The results will be stored in
                        <OUT_DIR>/qservTest_case<CASE_ID>/ (default:
                        /qserv/run/tmp)
  -s STOP_AT_QUERY, --stop-at-query STOP_AT_QUERY
                        Stop at query with given number (default: 10000)

Input dataset customization options:
  Options related to input data set customization

  -T WORK_DIR, --work-dir WORK_DIR
                        Absolute path to parent directory where source test
                        datasets will be copied, and big datasets will be
                        eventually downloaded (default: /qserv/run/tmp)
  -C, --custom          If <WORK_DIR>/case<CASE_ID> doesn't exists, copy it
                        from <TESTDATA_DIR>, disable load and query
                        operations, and had to be performed before them
                        (default: False)
  -D, --download        Download big datasets using rsync over ssh, implies
                        --custom, enable batch mode with ~/.ssh/config and
                        ssh-agent (default: False)
  -I CUSTOM_CASE_ID, --custom-case-id CUSTOM_CASE_ID
                        Rename custom test to case/CUSTOM_CASE_ID (default:
                        None)
  -U USERNAME, --username USERNAME
                        rsync username (default: None)
qserv@qserv-user-master-1:/qserv/run/var/log/work/qserv_testdata$ qserv-check-integration.py ^C-load --case=06       
qserv@qserv-user-master-1:/qserv/run/var/log/work/qserv_testdata$ vi ~/.lsst/ 
.my.cnf      logging.ini  qserv.conf   
qserv@qserv-user-master-1:/qserv/run/var/log/work/qserv_testdata$ vi ~/.lsst/logging.ini 
bash: vi: command not found
qserv@qserv-user-master-1:/qserv/run/var/log/work/qserv_testdata$ cat ~/.lsst/logging.ini  
[loggers]
keys=root,CSS,lsst.qserv,lsst.qserv.admin.commons,lsst.qserv.admin.dataLoader,lsst.qserv.admin.dataDuplicator,lsst.qserv.tests,lsst.qserv.tests.sql,QADM

[handlers]
keys=console,info_file,error_file

[formatters]
keys=simpleFormatter

[handler_console]
class=logging.StreamHandler
level=DEBUG
formatter=simpleFormatter
args=(sys.stdout,)

[handler_info_file]
class=logging.handlers.RotatingFileHandler
level=INFO
formatter=simpleFormatter
args=('qserv_client_info.log', 'a', 10485760, 20, 'utf8')

[handler_error_file]
class=logging.handlers.RotatingFileHandler
level=ERROR
formatter=simpleFormatter
args=('qserv_client_error.log', 'a', 10485760, 20, 'utf8')

[formatter_simpleFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
datefmt=

[logger_root]
level=WARN
handlers=console,info_file,error_file

[logger_CSS]
level=NOTSET
handlers=console,info_file,error_file
propagate=0
qualname=CSS

[logger_QADM]
level=NOTSET
handlers=console,info_file,error_file
propagate=0
qualname=QADM

[logger_lsst.qserv]
level=NOTSET
handlers=console,info_file,error_file
propagate=0
qualname=lsst.qserv

[logger_lsst.qserv.admin.commons]
level=NOTSET
handlers=console,info_file,error_file
propagate=0
qualname=lsst.qserv.admin.commons

[logger_lsst.qserv.admin.dataLoader]
level=NOTSET
handlers=console,info_file,error_file
propagate=0
qualname=lsst.qserv.admin.dataLoader

[logger_lsst.qserv.admin.dataDuplicator]
level=NOTSET
handlers=console,info_file,error_file
propagate=0
qualname=lsst.qserv.admin.dataDuplicator

[logger_lsst.qserv.tests]
level=INFO
handlers=console,info_file,error_file
propagate=0
qualname=lsst.qserv.tests

[logger_lsst.qserv.tests.sql]
level=WARN
handlers=console,info_file,error_file
propagate=0
qualname=lsst.qserv.tests.sql
qserv@qserv-user-master-1:/qserv/run/var/log/work/qserv_testdata$                         
qserv@qserv-user-master-1:/qserv/run/var/log/work/qserv_testdata$ 
qserv@qserv-user-master-1:/qserv/run/var/log/work/qserv_testdata$ 
qserv@qserv-user-master-1:/qserv/run/var/log/work/qserv_testdata$ qserv-check-integration.py --help --load --case=06
usage: qserv-check-integration.py [-h] [-V LOG_CONF] [-i CASE_ID]
                                  [-m {mysql,qserv,all}] [-l]
                                  [-t TESTDATA_DIR] [-o OUT_DIR]
                                  [-s STOP_AT_QUERY] [-T WORK_DIR] [-C] [-D]
                                  [-I CUSTOM_CASE_ID] [-U USERNAME]

Launch one Qserv integration test with fine-grained parameters, usefull for
developers in order to debug/test manually a specific part of Qserv.
Configuration values are read from ~/.lsst/qserv.conf.

optional arguments:
  -h, --help            show this help message and exit
  -V LOG_CONF, --log-cfg LOG_CONF
                        Absolute path to file containing pythonlogger standard
                        configuration file (default:
                        /home/qserv/.lsst/logging.ini)

General options:
  Options related to data loading and querying

  -i CASE_ID, --case-id CASE_ID
                        Test case number (default: 01)
  -m {mysql,qserv,all}, --mode {mysql,qserv,all}
                        Qserv test modes (direct mysql connection, or via
                        qserv) (default: all)

Load options:
  Options related to data loading

  -l, --load            Load test dataset prior to query execution (default:
                        False)
  -t TESTDATA_DIR, --testdata-dir TESTDATA_DIR
                        Absolute path to directory containing test datasets.
                        This value is set, by precedence, by this option, and
                        then by QSERV_TESTDATA_DIR/datasets/ if
                        QSERV_TESTDATA_DIR environment variable is not empty
                        (default:
                        /qserv/run/var/log/work/qserv_testdata/datasets)

Query options:
  Options related to query execution

  -o OUT_DIR, --out-dir OUT_DIR
                        Absolute path to directory for storing query
                        results.The results will be stored in
                        <OUT_DIR>/qservTest_case<CASE_ID>/ (default:
                        /qserv/run/tmp)
  -s STOP_AT_QUERY, --stop-at-query STOP_AT_QUERY
                        Stop at query with given number (default: 10000)

Input dataset customization options:
  Options related to input data set customization

  -T WORK_DIR, --work-dir WORK_DIR
                        Absolute path to parent directory where source test
                        datasets will be copied, and big datasets will be
                        eventually downloaded (default: /qserv/run/tmp)
  -C, --custom          If <WORK_DIR>/case<CASE_ID> doesn't exists, copy it
                        from <TESTDATA_DIR>, disable load and query
                        operations, and had to be performed before them
                        (default: False)
  -D, --download        Download big datasets using rsync over ssh, implies
                        --custom, enable batch mode with ~/.ssh/config and
                        ssh-agent (default: False)
  -I CUSTOM_CASE_ID, --custom-case-id CUSTOM_CASE_ID
                        Rename custom test to case/CUSTOM_CASE_ID (default:
                        None)
  -U USERNAME, --username USERNAME
                        rsync username (default: None)
qserv@qserv-user-master-1:/qserv/run/var/log/work/qserv_testdata$         
