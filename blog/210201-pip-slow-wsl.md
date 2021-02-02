
[pdoc3](https://www.google.com/search?q=pdoc3&ie=UTF-8)
[pdoc3 · PyPI ](https://pypi.org/project/pdoc3/)
[pdoc3/pdoc: Auto-generate API documentation for Python projects ](https://github.com/pdoc3/pdoc)
[python pip not responding](https://www.google.com/search?q=python+pip+not+responding&ie=UTF-8)
[pip install does not response, but works well with option '--no-cache-dir' · Issue #3245 · pypa/pip ](https://github.com/pypa/pip/issues/3245)
[python pip hangs](https://www.google.com/search?q=python+pip+hangs&ie=UTF-8)
[python - Pip Install hangs](https://stackoverflow.com/questions/33925566/pip-install-hangs)
[pip hanging when trying to install packages : learnpython ](https://www.reddit.com/r/learnpython/comments/fn61mo/pip_hanging_when_trying_to_install_packages/)
[python PIP takes forever on WSL : bashonubuntuonwindows ](https://www.reddit.com/r/bashonubuntuonwindows/comments/8rplxw/python_pip_takes_forever_on_wsl/)
[Prefer A (IPv4) DNS lookups before AAAA(IPv6) lookups - Ask Ubuntu ](https://askubuntu.com/questions/32298/prefer-a-ipv4-dns-lookups-before-aaaaipv6-lookups/38468#38468)
[gai.conf pypi](https://www.google.com/search?q=gai.conf+pypi&gs_lcp=CgZwc3ktYWIQAzoHCAAQRxCwAzoECCMQJzoFCCEQoAFQrNAEWKvaBGCz3QRoAXACeACAAWeIAd8DkgEDNS4xmAEAoAEBqgEHZ3dzLXdpesgBCMABAQ&sclient=psy-ab&uact=5)
[ai.cdas · PyPI ](https://pypi.org/project/ai.cdas/)
[apt - Reinstallation of Ubuntu WSL 18.04 and Python3-pip installation issues - Ask Ubuntu ](https://askubuntu.com/questions/1242732/reinstallation-of-ubuntu-wsl-18-04-and-python3-pip-installation-issues)
[Ubuntu – Reinstallation of Ubuntu WSL 18.04 and Python3-pip installation issues – iTecTec ](https://itectec.com/ubuntu/ubuntu-reinstallation-of-ubuntu-wsl-18-04-and-python3-pip-installation-issues/)
[Disable IPv6 for python script](https://stackoverflow.com/questions/31519567/disable-ipv6-for-python-script)
[AAAA resolution](https://www.google.com/search?q=AAAA+resolution&ie=UTF-8)
[gai.conf(5): getaddrinfo config file - Linux man page ](https://linux.die.net/man/5/gai.conf)
[How to disable ubuntu 14.04 ipv6  DigitalOcean ](https://www.digitalocean.com/community/questions/how-to-disable-ubuntu-14-04-ipv6)



```
21/02/1 14:14:27 kvogel-elitebook:~/projects/primrose ±(master) ✗ 
❯ which pdoc
pdoc not found
❯ python3 -m pdoc
pdoc server ready at http://localhost:8080
```

[Loading...](http://localhost:8080/)... never loads

```
21/02/1 14:17:42 kvogel-elitebook:~/projects/primrose ±(master) ✗ 
❯ pip3 install pdoc3
[hangs]
21/02/1 14:20:02 kvogel-elitebook:~/projects/primrose ±(master) ✗ 
❯ python3 -m pip install pdoc3
[hangs]
```

>An AAAA record maps a domain name to the IP address (IPv6) of the computer hosting the domain.

```
21/02/1 14:24:11 kvogel-elitebook:~/p/primrose ±(master) ✗
❯ telnet pypi.org 80
Trying 151.101.192.223...
Connected to pypi.org.
Escape character is '^]'.
ls
^C^]
telnet> help
Commands may be abbreviated.  Commands are:

close           close current connection
logout          forcibly logout remote user and close the connection
display         display operating parameters
mode            try to enter line or character mode ('mode ?' for more)

open            connect to a site
quit            exit telnet
send            transmit special characters ('send ?' for more)
set             set operating parameters ('set ?' for more)
unset           unset operating parameters ('unset ?' for more)
status          print status information
toggle          toggle operating parameters ('toggle ?' for more)
slc             set treatment of special characters

z               suspend telnet
environ         change environment variables ('environ ?' for more)
telnet> quit
Connection closed.
21/02/1 14:25:05 kvogel-elitebook:~/p/primrose ±(master) ✗
❯ sudo vi /etc/gai.conf
[sudo] password for kvogel:
21/02/1 14:26:38 kvogel-elitebook:~/p/primrose ±(master) ✗
❯ sudo apt update
Hit:1 http://archive.ubuntu.com/ubuntu focal InRelease
Get:2 http://archive.ubuntu.com/ubuntu focal-updates InRelease [114 kB]
...
```

```
21/02/1 14:26:54 kvogel-elitebook:~/p/primrose ±(master) ✗
❯ ping pypi.org
PING pypi.org (151.101.192.223) 56(84) bytes of data.
64 bytes from 151.101.192.223 (151.101.192.223): icmp_seq=1 ttl=56 time=4.74 ms
64 bytes from 151.101.192.223 (151.101.192.223): icmp_seq=2 ttl=56 time=7.69 ms
64 bytes from 151.101.192.223 (151.101.192.223): icmp_seq=3 ttl=56 time=6.78 ms
^C
--- pypi.org ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2050ms
rtt min/avg/max/mdev = 4.741/6.405/7.692/1.233 ms
```


went back to look at terminal where I had entered `pip3 install -vvv pdoc3 --no-cache-dir` and thought it was doing nothing...:
```
21/02/1 14:22:40 kvogel-elitebook:~/projects/primrose ±(master) ✗ 
❯ pip3 install -vvv pdoc3 --no-cache-dir
User install by explicit request
Created temporary directory: /tmp/pip-ephem-wheel-cache-eoq2o_b3
Created temporary directory: /tmp/pip-req-tracker-xq_mui27
Initialized build tracking at /tmp/pip-req-tracker-xq_mui27
Created build tracker: /tmp/pip-req-tracker-xq_mui27
Entered build tracker: /tmp/pip-req-tracker-xq_mui27
Created temporary directory: /tmp/pip-install-b1uccvc_
1 location(s) to search for versions of pdoc3:
* https://pypi.org/simple/pdoc3/
Fetching project page and analyzing links: https://pypi.org/simple/pdoc3/
Getting page https://pypi.org/simple/pdoc3/
Found index url https://pypi.org/simple
Getting credentials from keyring for https://pypi.org/simple
Getting credentials from keyring for pypi.org
Starting new HTTPS connection (1): pypi.org:443
https://pypi.org:443 "GET /simple/pdoc3/ HTTP/1.1" 200 2795
  Found link https://files.pythonhosted.org/packages/10/78/de7f101b4fceaa63d7bea6f8d28da8c8f748bc7f5d51545230f1e95a3db5/pdoc3-0.3.11.tar.gz#sha256=abc18da1912b1e51abe90a7ef3b8e58d7dc98f8371fde214f60682f5dd0a4393 (from https://pypi.org/simple/pdoc3/), version: 0.3.11
  Found link https://files.pythonhosted.org/packages/be/3f/2852121882e196c5845da1423d04d6a793bd420795bd94bb8d79e83ffb04/pdoc3-0.3.12.tar.gz#sha256=72829a5592d15ede2dcdaf7a98a32b373d534866261a9c31bf2caa193039994c (from https://pypi.org/simple/pdoc3/), version: 0.3.12
  Found link https://files.pythonhosted.org/packages/6d/31/af570d2f1417f84219b88effb301b82e11674ee075433bae5489e7c255a7/pdoc3-0.3.13.tar.gz#sha256=b9cb99c54472aedeaf80d69e92e40ee25d8459d1c1e36968be54989edde15508 (from https://pypi.org/simple/pdoc3/), version: 0.3.13
  Found link https://files.pythonhosted.org/packages/4b/a4/ad54cb92f024cce700295a6cc2063f3766891467299e21a9633ac6c314d7/pdoc3-0.5.0.tar.gz#sha256=d98bcb5f7edf35e7d92bf7ca9b4886df4e766c78c3596f2939180a9ef913b11a (from https://pypi.org/simple/pdoc3/) (requires-python:>= 3.5), version: 0.5.0
  Found link https://files.pythonhosted.org/packages/37/c5/9bdeb263440b17fa274533e2b837f34b06803641c5673d2fdcfeb8803bc1/pdoc3-0.5.1.tar.gz#sha256=41c1bcf7503495e7d4122076c6271313bf028adce5cd700f30cca17af13ca088 (from https://pypi.org/simple/pdoc3/) (requires-python:>= 3.5), version: 0.5.1
  Found link https://files.pythonhosted.org/packages/a7/c6/70de76835e95bd6997465d95516deabce5f0fb4c224512a2924c644e2be6/pdoc3-0.5.2.tar.gz#sha256=1124004173612e1afd7bed3e948aae56e2523f92050b4584f49e7c971474c23f (from https://pypi.org/simple/pdoc3/) (requires-python:>= 3.5), version: 0.5.2
  Found link https://files.pythonhosted.org/packages/85/dd/860a5305706f7e728912ad446b5b5ba1bebd6ee9f8e92c29456b1ab5b734/pdoc3-0.5.3.tar.gz#sha256=8e11ef161c3dcd68d5a434d38ae55e2f8f5719470429d64e9b187d87e5f1d8d6 (from https://pypi.org/simple/pdoc3/) (requires-python:>= 3.5), version: 0.5.3
  Found link https://files.pythonhosted.org/packages/e2/87/317dd24867846221539c383446483055e9890b45d7b25916989c93155d12/pdoc3-0.5.4.tar.gz#sha256=6babd3d47e607d579ddba268dbe4c21aa54d4e7f29a514b8af4372636f038ead (from https://pypi.org/simple/pdoc3/) (requires-python:>= 3.5), version: 0.5.4
  Found link https://files.pythonhosted.org/packages/2a/91/e37dcb95afac1fd37222b8d928aab33ab735e2d18dedf9ba7ff99b897d4d/pdoc3-0.6.0.tar.gz#sha256=d40d581cbeeb31a7e269326940448b0f0b27500aeff3e5c73613bf99a840e788 (from https://pypi.org/simple/pdoc3/) (requires-python:>= 3.5), version: 0.6.0
  Found link https://files.pythonhosted.org/packages/6a/ba/a53acee4609bcbc874e982dfd5a3b0630a6deffead2db86d3bfaafb517a3/pdoc3-0.6.1.tar.gz#sha256=24b4c012a89c573742a41f8239a71249060e3484baf16d4f489baec788313182 (from https://pypi.org/simple/pdoc3/) (requires-python:>= 3.5), version: 0.6.1
  Found link https://files.pythonhosted.org/packages/51/96/bf85b7bd7c18c8f6f4f85720875de817f124da3ee1d07adea84c20cbbe67/pdoc3-0.6.2.tar.gz#sha256=bfc011da61a3edd4bb1ec2b8dcaa483776b67a30bf67a28760ab25edd9dc502c (from https://pypi.org/simple/pdoc3/) (requires-python:>= 3.5), version: 0.6.2
  Found link https://files.pythonhosted.org/packages/31/0c/0228d25f94bef5c529365c77ee4364787cb6802e2401deb5c55c120b8227/pdoc3-0.6.3.tar.gz#sha256=b144f61eb1f790e998dbbbe32785cd48eba587ebae00cfcf1a2408c8f4ffaca2 (from https://pypi.org/simple/pdoc3/) (requires-python:>= 3.5), version: 0.6.3
  Found link https://files.pythonhosted.org/packages/32/57/ae74ea7278b2f0ba22cfee4f872fb236f7abeb3218353ae9126945ed951b/pdoc3-0.6.4.tar.gz#sha256=85cbb0de17d1306157d19b08b67ad84817098c12ad9f92ec203b79d0307b6a25 (from https://pypi.org/simple/pdoc3/) (requires-python:>= 3.5), version: 0.6.4
  Found link https://files.pythonhosted.org/packages/c6/e9/32ef1c81e2716c854d5eaadd86f315d9217c7c8d1acf60a95855e0f3b932/pdoc3-0.7.0.tar.gz#sha256=f4a27fa0cc8cf6fb8772129a9d7e9ecb3bab72a6ffd2475c5ad861484f6aae3d (from https://pypi.org/simple/pdoc3/) (requires-python:>= 3.5), version: 0.7.0
  Found link https://files.pythonhosted.org/packages/7b/87/4bf1b71f4d357f96f768bf5df07a6a9a36e3571bf5df960441121c0f1cdc/pdoc3-0.7.1.tar.gz#sha256=c2cff1fc7a36b45be6e76561b0bd5a5b829ee7c5bb22e6338cfd891d460758c9 (from https://pypi.org/simple/pdoc3/) (requires-python:>= 3.5), version: 0.7.1
  Found link https://files.pythonhosted.org/packages/9b/bc/b1c36f5cb715da54b5a690050a3099480fa7be19e09d51d4f4c0594e74b0/pdoc3-0.7.2.tar.gz#sha256=df43a7f1a139a5a61e778f424f167719acc33ed71bf13b6c34c7ebd139866eb7 (from https://pypi.org/simple/pdoc3/) (requires-python:>= 3.5), version: 0.7.2
  Found link https://files.pythonhosted.org/packages/fe/b4/29796c99d73a833ddbefc51223255b2c214e078100501cc8eb66c8df20e9/pdoc3-0.7.3.tar.gz#sha256=dbc8163028ff62f714577834a4b0dfcc7eba34d8477a6c44d8f9dd44e62764a3 (from https://pypi.org/simple/pdoc3/) (requires-python:>= 3.5), version: 0.7.3
  Found link https://files.pythonhosted.org/packages/83/da/6d8bc253d58ee23ad309c030aef4fbe8f23d6b28e144f069a91c59b1667f/pdoc3-0.7.4.tar.gz#sha256=1a9393d6b1e8c2976c0e1a8d0b897ba5e5ea9515058470422cf57ee54293ab05 (from https://pypi.org/simple/pdoc3/) (requires-python:>= 3.5), version: 0.7.4
  Found link https://files.pythonhosted.org/packages/82/42/6704b93286f33986dc33cdc5fe636b622b2b1b893a68a96a15c61ab0b72e/pdoc3-0.7.5.tar.gz#sha256=ebca75b7fcf23f3b4320abe23339834d3f08c28517718e9d29e555fc38eeb33c (from https://pypi.org/simple/pdoc3/) (requires-python:>= 3.5), version: 0.7.5
  Found link https://files.pythonhosted.org/packages/56/49/0f8577808aa4e784650cff028519b4a5cff27feb3e227e50d2a3e9c474ac/pdoc3-0.8.0.tar.gz#sha256=793e7a83db96fc7a992bc593265a0963d0bdf7d66a1dd5d443a6c6ea885b73be (from https://pypi.org/simple/pdoc3/) (requires-python:>= 3.5), version: 0.8.0
  Found link https://files.pythonhosted.org/packages/11/1c/ce4459d7aab0890b6059a8c5cc3494c92d3a1cfe1938e2ae49555b3bf31a/pdoc3-0.8.1.tar.gz#sha256=d7b56e67b5e049d53dcde94245a28040b640b2e06c344fc58ab2bdf2d91dc00f (from https://pypi.org/simple/pdoc3/) (requires-python:>= 3.5), version: 0.8.1
  Found link https://files.pythonhosted.org/packages/05/ea/6b53f6708f93bc9d9ff2005fb66608799403927d4d840738049ed9d7aba7/pdoc3-0.8.2.tar.gz#sha256=fa8b851e0bdef77c37115e54ec55d6aed862d8bd4e865fd0f72ed058113c2e93 (from https://pypi.org/simple/pdoc3/) (requires-python:>= 3.5), version: 0.8.2
  Found link https://files.pythonhosted.org/packages/1b/ae/0bf8314a56ba26fa701f89b50542e0306a2097fe08aed5eb6098fe79925a/pdoc3-0.8.3.tar.gz#sha256=19bd1a72e1c82875a6927b244aca826dedb635ea2a7a36ac62cbe063a8ddc30d (from https://pypi.org/simple/pdoc3/) (requires-python:>= 3.5), version: 0.8.3
  Found link https://files.pythonhosted.org/packages/d9/79/dd3b035c0e3cdfdb972524138b9b6e623dcebbaf787e4e4af7d022b7c09d/pdoc3-0.8.4.tar.gz#sha256=9b2ec2279b004372810ab6b7465489ccf402428625dfecf3bd3f13b45aa5a3ea (from https://pypi.org/simple/pdoc3/) (requires-python:>= 3.5), version: 0.8.4
  Found link https://files.pythonhosted.org/packages/3b/5a/aea73303ed039c3f6122a4dcdb4356f9a0a40ca0def3887e45008300132e/pdoc3-0.8.5.tar.gz#sha256=63e59a7f723869e06d854c73215831dc04098f7038d9da3a1715be698e0d9551 (from https://pypi.org/simple/pdoc3/) (requires-python:>= 3.5), version: 0.8.5
  Found link https://files.pythonhosted.org/packages/0d/b5/021c2247f65483ab181c66a9503a240a5ec2718afd79d2a3876c9789daea/pdoc3-0.9.0.tar.gz#sha256=3d04d5d84e88e3b7e0953c501552a77c85de996221415fd3ed354967c08c1ba3 (from https://pypi.org/simple/pdoc3/) (requires-python:>= 3.5), version: 0.9.0
  Found link https://files.pythonhosted.org/packages/67/68/ce1035e720f1c5b80372164c389907d26cb488d600b42d136c75f587a427/pdoc3-0.9.1.tar.gz#sha256=e1848d5485b8dd4662272f83bb5f7df4a68e0a5d76c87be30327977777168894 (from https://pypi.org/simple/pdoc3/) (requires-python:>= 3.5), version: 0.9.1
  Found link https://files.pythonhosted.org/packages/48/05/6c987ce02df70ae11849a64c3ec2b32de68531d6b227e7dccdae7eb43fdb/pdoc3-0.9.2.tar.gz#sha256=9df5d931f25f353c69c46819a3bd03ef96dd286f2a70bb1b93a23a781f91faa1 (from https://pypi.org/simple/pdoc3/) (requires-python:>= 3.5), version: 0.9.2
Given no hashes to check 28 links for project 'pdoc3': discarding no candidates
Using version 0.9.2 (newest of versions: 0.3.11, 0.3.12, 0.3.13, 0.5.0, 0.5.1, 0.5.2, 0.5.3, 0.5.4, 0.6.0, 0.6.1, 0.6.2, 0.6.3, 0.6.4, 0.7.0, 0.7.1, 0.7.2, 0.7.3, 0.7.4, 0.7.5, 0.8.0, 0.8.1, 0.8.2, 0.8.3, 0.8.4, 0.8.5, 0.9.0, 0.9.1, 0.9.2)
Collecting pdoc3
  Created temporary directory: /tmp/pip-unpack-dipy4oy3
  Getting credentials from keyring for files.pythonhosted.org
  Starting new HTTPS connection (1): files.pythonhosted.org:443
  https://files.pythonhosted.org:443 "GET /packages/48/05/6c987ce02df70ae11849a64c3ec2b32de68531d6b227e7dccdae7eb43fdb/pdoc3-0.9.2.tar.gz HTTP/1.1" 200 84803
  Downloading pdoc3-0.9.2.tar.gz (84 kB)
     |████████████████████████████████| 84 kB 7.6 MB/s 
  Added pdoc3 from https://files.pythonhosted.org/packages/48/05/6c987ce02df70ae11849a64c3ec2b32de68531d6b227e7dccdae7eb43fdb/pdoc3-0.9.2.tar.gz#sha256=9df5d931f25f353c69c46819a3bd03ef96dd286f2a70bb1b93a23a781f91faa1 to build tracker '/tmp/pip-req-tracker-xq_mui27'
    Running setup.py (path:/tmp/pip-install-b1uccvc_/pdoc3/setup.py) egg_info for package pdoc3
    Running command python setup.py egg_info
    running egg_info
    creating /tmp/pip-install-b1uccvc_/pdoc3/pip-egg-info/pdoc3.egg-info
    writing /tmp/pip-install-b1uccvc_/pdoc3/pip-egg-info/pdoc3.egg-info/PKG-INFO
    writing dependency_links to /tmp/pip-install-b1uccvc_/pdoc3/pip-egg-info/pdoc3.egg-info/dependency_links.txt
    writing entry points to /tmp/pip-install-b1uccvc_/pdoc3/pip-egg-info/pdoc3.egg-info/entry_points.txt
    writing requirements to /tmp/pip-install-b1uccvc_/pdoc3/pip-egg-info/pdoc3.egg-info/requires.txt
    writing top-level names to /tmp/pip-install-b1uccvc_/pdoc3/pip-egg-info/pdoc3.egg-info/top_level.txt
    writing manifest file '/tmp/pip-install-b1uccvc_/pdoc3/pip-egg-info/pdoc3.egg-info/SOURCES.txt'
    reading manifest file '/tmp/pip-install-b1uccvc_/pdoc3/pip-egg-info/pdoc3.egg-info/SOURCES.txt'
    writing manifest file '/tmp/pip-install-b1uccvc_/pdoc3/pip-egg-info/pdoc3.egg-info/SOURCES.txt'
  Source in /tmp/pip-install-b1uccvc_/pdoc3 has version 0.9.2, which satisfies requirement pdoc3 from https://files.pythonhosted.org/packages/48/05/6c987ce02df70ae11849a64c3ec2b32de68531d6b227e7dccdae7eb43fdb/pdoc3-0.9.2.tar.gz#sha256=9df5d931f25f353c69c46819a3bd03ef96dd286f2a70bb1b93a23a781f91faa1
  Removed pdoc3 from https://files.pythonhosted.org/packages/48/05/6c987ce02df70ae11849a64c3ec2b32de68531d6b227e7dccdae7eb43fdb/pdoc3-0.9.2.tar.gz#sha256=9df5d931f25f353c69c46819a3bd03ef96dd286f2a70bb1b93a23a781f91faa1 from build tracker '/tmp/pip-req-tracker-xq_mui27'
1 location(s) to search for versions of mako:
* https://pypi.org/simple/mako/
Fetching project page and analyzing links: https://pypi.org/simple/mako/
Getting page https://pypi.org/simple/mako/
Found index url https://pypi.org/simple
Getting credentials from keyring for https://pypi.org/simple
Getting credentials from keyring for pypi.org
https://pypi.org:443 "GET /simple/mako/ HTTP/1.1" 200 5743
  Found link https://files.pythonhosted.org/packages/fe/60/2b0d8cdc3d311e68cd5daa046704b00b4aa89db51a30d22fcfbf34cb1ea1/Mako-0.1.0.tar.gz#sha256=5a727f19215a765041016debf52a2efa1690aff349d49dc05ac5aaffae9b93ab (from https://pypi.org/simple/mako/), version: 0.1.0
  Found link https://files.pythonhosted.org/packages/26/76/5def15b515d84f1663c7e196574701416699add3dbc757e0d0f74897f369/Mako-0.1.1.tar.gz#sha256=75e1dd5f9a04371816d5bd9044c2a63cc2b96589b20d8623b212ddb33e5b3e2f (from https://pypi.org/simple/mako/), version: 0.1.1
  Found link https://files.pythonhosted.org/packages/14/57/3880554038012a98995ee8bf191bf0436adc9f0fda2f7f955b5cfa88e2d8/Mako-0.1.2.tar.gz#sha256=847b028ddcbda13d02956b45a6dd1d0948f6a3e4c06cb1f2649e3831b14b274c (from https://pypi.org/simple/mako/), version: 0.1.2
  Found link https://files.pythonhosted.org/packages/19/cf/082eac96066e3db660198f0b292935bf7ca3208e98f878f640045b8e84c9/Mako-0.1.3.tar.gz#sha256=3d78a982b30f3a4912985528fc4e5cc547e324cce1e66b51943ef6df34fd418e (from https://pypi.org/simple/mako/), version: 0.1.3
  Found link https://files.pythonhosted.org/packages/87/a6/2baba6c75e8ba6638dee300f3cd14061165fb9df1d0145b9ff7c81200b51/Mako-0.1.4.tar.gz#sha256=17ae82eb9e3e0b01b530ff6f348cd9a93e393db665521e4c82ad952017ab9ec2 (from https://pypi.org/simple/mako/), version: 0.1.4
  Found link https://files.pythonhosted.org/packages/40/e8/b969c36259ab6d977e8f778070043da6854ecc7941ab80b75bd3e2a08351/Mako-0.1.5.tar.gz#sha256=299d789e5817e8dd34de8010e6336c630b64b634599538115b29836e79820f1b (from https://pypi.org/simple/mako/), version: 0.1.5
  Found link https://files.pythonhosted.org/packages/28/6e/e0143cd0719c2ab627a0b17a6faa8c6cd698da8db6dcc056ba71d8ff1eb4/Mako-0.1.6.tar.gz#sha256=ff2a90d697f0228d0de02590292a911707bb79a77e59f4a2be4b9d78240c2b76 (from https://pypi.org/simple/mako/), version: 0.1.6
  Found link https://files.pythonhosted.org/packages/0e/50/5adb93939309fde21e927a61a001c324c0543a3de976009bef67dc8164fd/Mako-0.1.7.tar.gz#sha256=572e835b963da6c4067a705a72f843df414c9780f8d6dfbaab940fb2b59b417b (from https://pypi.org/simple/mako/), version: 0.1.7
  Found link https://files.pythonhosted.org/packages/c6/f2/59effe868311e90541d080f881a31ad74a9350c3cee15b05ebc719bc2139/Mako-0.1.8.tar.gz#sha256=03c0a731e8e4df63692c863d7185e86d39425c17c5cb9c42847bdcd69da98c67 (from https://pypi.org/simple/mako/), version: 0.1.8
  Found link https://files.pythonhosted.org/packages/4b/94/6320382340fed33a3f586f409273a741facccf3c0410fde35e9df1b72e37/Mako-0.1.9.tar.gz#sha256=4a6a876030effa3554d612cf034fcf8c74522ad4eddc1a2a75f6e12bf67cc2de (from https://pypi.org/simple/mako/), version: 0.1.9
  Found link https://files.pythonhosted.org/packages/35/3a/e0fd1ef41e65180aecf629828389598e2b240779b36229f930c3524b38cf/Mako-0.1.10.tar.gz#sha256=bec55f4967c0bde2064cf0a0e89c7afb670473ca6f9f3b84ce0c21d426697002 (from https://pypi.org/simple/mako/), version: 0.1.10
  Found link https://files.pythonhosted.org/packages/06/e2/6f6d78ce184c0490c939402937f9b30c4843b74388a5ccef0ed87780ea7e/Mako-0.2.0.tar.gz#sha256=d5ded7d2f0f77cad8d1d8b3e4de1a95599cbd497a0884ac975deec31d4971d0d (from https://pypi.org/simple/mako/), version: 0.2.0
  Found link https://files.pythonhosted.org/packages/5d/cb/3e40d865ea7f6f69782b2976f0a673b4bf7ca9a36ef621a76ea83412a1d1/Mako-0.2.1.tar.gz#sha256=3a773204d134db69f2a00ce6844292832c606b5a998a175a740e1330c225632c (from https://pypi.org/simple/mako/), version: 0.2.1
  Found link https://files.pythonhosted.org/packages/70/ca/f80f43719e4fc32db230b381ba67816a29bb731a550cb2a5575c47c43acd/Mako-0.2.2.tar.gz#sha256=858b2ad7850db5e477ab81d7f355f82df33d90e4ed23a235184f380a925f2813 (from https://pypi.org/simple/mako/), version: 0.2.2
  Found link https://files.pythonhosted.org/packages/b3/24/734f630753f6615851d7fbae7c7b5c7c4807127d06c3ccd11272e43bb9fc/Mako-0.2.3.tar.gz#sha256=601de73cb2d8f44ccd91dcd2ec909b901c45e68ddaeb12e6dad312ed43abd6c2 (from https://pypi.org/simple/mako/), version: 0.2.3
  Found link https://files.pythonhosted.org/packages/65/b7/371df6136a2dceab36c1bd3947211b112f78225c4d0a6a3e20eb008cbc16/Mako-0.2.4.tar.gz#sha256=efab44f95e0d305ad684cddc0c42018520cb287ad7cdd4022e1ac9ba05dbd16e (from https://pypi.org/simple/mako/), version: 0.2.4
  Found link https://files.pythonhosted.org/packages/d5/06/91380b74ffdabc762ff205a17139bcd64011c60af240b9fbb37f3346b756/Mako-0.2.5.tar.gz#sha256=d0cd9121ae797b459ae55a66e3aa80b8d53a0ab2ca27f7e5eaa0540adcb20f19 (from https://pypi.org/simple/mako/), version: 0.2.5
  Found link https://files.pythonhosted.org/packages/03/85/a80680abcc1c3e88b8af7312cd14712ac6355f8bd88ff60503cbf420443f/Mako-0.3.0.tar.gz#sha256=a6aea34a2dfda9dd54ee35be78244dc6f7a97bd74d7811e69add190c00a0b3a8 (from https://pypi.org/simple/mako/), version: 0.3.0
  Found link https://files.pythonhosted.org/packages/75/68/05bfdeb245a6f15211127d2aa82c7e4ee1f02fe22825860b2f3b87adfc32/Mako-0.3.1.tar.gz#sha256=2b4ac7ef3973f12ff339813ae895a4e232d98052aa8136ed4301f3241fc424f7 (from https://pypi.org/simple/mako/), version: 0.3.1
  Found link https://files.pythonhosted.org/packages/ca/9a/f517da610f415636b3261bf501dd6fe58affcfbee840356b74867c0fc2c0/Mako-0.3.2.tar.gz#sha256=2c4dfc42dd0ea1a2273473569d37e6965c1397c1e6ea5c3071516064d981e816 (from https://pypi.org/simple/mako/), version: 0.3.2
  Found link https://files.pythonhosted.org/packages/0c/10/29b55f687c9e0ac7f57e1440f55ba30f11c49a3f261ca8a4ccda19948181/Mako-0.3.3.tar.gz#sha256=3c6d88c1d4de3d024fd8b7f6cacea5a9fe069a36eaf6ef8392a94474364e7af9 (from https://pypi.org/simple/mako/), version: 0.3.3
  Found link https://files.pythonhosted.org/packages/40/b4/4a663628f96c11d117b4f54c4e442fef6b99bcce3b2dbfd759804b50f705/Mako-0.3.4.tar.gz#sha256=7f7dc9b102c3d61627a4ca93b6144ebd59fe1fe6c0e46214558d4485a1ed0340 (from https://pypi.org/simple/mako/), version: 0.3.4
  Found link https://files.pythonhosted.org/packages/d8/f5/056dc88fe2eb34c5d128662cd0c1039e1f900198f24a70fcade80099f549/Mako-0.3.5.tar.gz#sha256=1e6a56245dc2b0d7993021fb1a0b65a3413397c7edccdca47866c3a06c0c6be9 (from https://pypi.org/simple/mako/), version: 0.3.5
  Found link https://files.pythonhosted.org/packages/aa/e1/c6e7d65a6da8e01cb185d03ff7c2a1578233a96c5f87e812f351c73d0d28/Mako-0.3.6.tar.gz#sha256=5e27102950259ca709e12082f37a91ed6f5de320371ae1ccb6d4ae2426052b6f (from https://pypi.org/simple/mako/), version: 0.3.6
  Found link https://files.pythonhosted.org/packages/fa/f6/db660acb4c9dcac47fe1b0e0ff7edc1d3817f68ddee14141e05e06c01fe8/Mako-0.4.0.tar.gz#sha256=8c83058cc772473abe67a195b2533a71c2ef9e3b87d56513a6185e2d3270d2ae (from https://pypi.org/simple/mako/), version: 0.4.0
  Found link https://files.pythonhosted.org/packages/c5/e9/d9ec4d44616f7b3628b168cab57bcd2196b4e9fa6880331552a5b21e6a74/Mako-0.4.1.tar.gz#sha256=c282a6bb1c15571e1bc1612df58e6b5bb8d3d7c57169e641434bb50d303af6e9 (from https://pypi.org/simple/mako/), version: 0.4.1
  Found link https://files.pythonhosted.org/packages/ff/4b/4ea6fbc150bb569cd89b81281a4b5dfbea11d72d8006be4d6fc72f04b0b7/Mako-0.4.2.tar.gz#sha256=3751a1a3fde4f3eaaa7037a491cb4f5d40d85ab882e4dabc094085c5deada423 (from https://pypi.org/simple/mako/), version: 0.4.2
  Found link https://files.pythonhosted.org/packages/05/27/e922e4bbd199c9b3b5f248d10c5b273a32fb23ec76117a8652015377d48e/Mako-0.5.0.tar.gz#sha256=41eb241ac229aa7095860207f9acbe40ff79cd4080579be9e5c6dd8ec0ad7d19 (from https://pypi.org/simple/mako/), version: 0.5.0
  Found link https://files.pythonhosted.org/packages/6b/41/4b72a9110e9fd4eebd011f5b02355f31ef55c8fa8a7804fb65b81f9a7b39/Mako-0.6.0.tar.gz#sha256=3f1508ee6b99ce470ee8f720104d841df85a432257b5f33c77d0d8037b2d93e8 (from https://pypi.org/simple/mako/), version: 0.6.0
  Found link https://files.pythonhosted.org/packages/3e/6b/8ee26e473a850a41f25221fcedd3bc97f6277e01a3219d0160c55604ef30/Mako-0.6.1.tar.gz#sha256=4b0a657bff7515ee2484f7863f2462f1cebfc2b1309df16e17658716c6e2f5a1 (from https://pypi.org/simple/mako/), version: 0.6.1
  Found link https://files.pythonhosted.org/packages/f2/59/b16f9afe72aa52ad104b0f4ebffa69c343072740af986cb7bcd44a8fb2df/Mako-0.6.2.tar.gz#sha256=0244ff8f3eea34893d60357cdc5465d297aa9c3061387743b6d54f7fd073d65c (from https://pypi.org/simple/mako/), version: 0.6.2
  Found link https://files.pythonhosted.org/packages/5a/72/d6d7b551e67a970480c4b57f2648c3b5f4b903b2c951245aabeb3b1d0e8f/Mako-0.7.0.tar.gz#sha256=61a09621988e5a4bdf90f4c82dda6c804ff2f0450a555eca22628da9cc1bb60f (from https://pypi.org/simple/mako/), version: 0.7.0
  Found link https://files.pythonhosted.org/packages/8c/2a/0cad9e137b04530bb76960f1df41c4b1ab94384910d44c56464bfc116f8c/Mako-0.7.1.tar.gz#sha256=e6eb92c5429bc8ec901ea059cbbc97c03a245ad566ee33e2c894f98869d231ee (from https://pypi.org/simple/mako/), version: 0.7.1
  Found link https://files.pythonhosted.org/packages/fa/8f/d901355a53ee1f4a2291580ddec7b7fdeba8fcaa45ded3e4241f26423f53/Mako-0.7.2.tar.gz#sha256=fe8698e845035586bd711a6748e4e40a208a58de276b9138026164700494b68f (from https://pypi.org/simple/mako/), version: 0.7.2
  Found link https://files.pythonhosted.org/packages/9b/82/32d68c0fdfb14e1ecfab42c1fc9810fe927c91e877f9db3ea8a9ce448a76/Mako-0.7.3.tar.gz#sha256=49842441d24d88d0ecfc38686d021cb3b1bee7abfc541e9fc7345e4620deeab6 (from https://pypi.org/simple/mako/), version: 0.7.3
  Found link https://files.pythonhosted.org/packages/3c/63/777708d2a8ad7beb57cdf2cc45cf740ed33c4a5f5b139d725815700c04eb/Mako-0.8.0.tar.gz#sha256=9f3b941e799e21775dced0553328fef725cb5e425a803d9f5230a4b39d8b702a (from https://pypi.org/simple/mako/), version: 0.8.0
  Found link https://files.pythonhosted.org/packages/ef/2e/fcd7241a6f0270ec990a8fcdb2f5a44e0ba9d8daeb2c8ecbb2e0d75501da/Mako-0.8.1.tar.gz#sha256=4791be305338b1fbe09054ec42fb606856599cdcdcde6f348858c13b5fa29158 (from https://pypi.org/simple/mako/), version: 0.8.1
  Found link https://files.pythonhosted.org/packages/ac/56/c78e792dc5970a744547519d961f026109342a5584f16150cb0eb8d8781c/Mako-0.9.0.tar.gz#sha256=c090ae3d775f714c572583f2bb7ace591847eab0d86accd81d17005411b10027 (from https://pypi.org/simple/mako/), version: 0.9.0
  Found link https://files.pythonhosted.org/packages/61/7d/752bd373eb816b744a979ba211ef4ce1871a917ab926a32991e231be3b5b/Mako-0.9.1.tar.gz#sha256=ed74d72b720a97a51590dfa839f2048ceeb76cc80d1d9ea5731a5262384316ae (from https://pypi.org/simple/mako/), version: 0.9.1
  Found link https://files.pythonhosted.org/packages/a7/91/d7314d46f4d86b7c841a673f10992855fdbf779a547b482779ee0b8a604b/Mako-1.0.0.tar.gz#sha256=a3cd72cfef507204b50f74ffcbfcfde7e856437891d3f6cfe780866986d006fe (from https://pypi.org/simple/mako/), version: 1.0.0
  Found link https://files.pythonhosted.org/packages/8e/a4/aa56533ecaa5f22ca92428f74e074d0c9337282933c722391902c8f9e0f8/Mako-1.0.1.tar.gz#sha256=45f0869febea59dab7efd256fb451c377cbb7947bef386ff0bb44627c31a8d1c (from https://pypi.org/simple/mako/), version: 1.0.1
  Found link https://files.pythonhosted.org/packages/12/f5/76009ed711e5f95385ffc872b226e3cf062c4c71f765c41a1f29789c52fd/Mako-1.0.2.tar.gz#sha256=2550c2e4528820db68cbcbe668add5c71ab7fa332b7eada7919044bf8697679e (from https://pypi.org/simple/mako/), version: 1.0.2
  Found link https://files.pythonhosted.org/packages/36/17/8f76e7acf8679ad70b23e61710152785d32de71a783a873a655f855d0d46/Mako-1.0.3.tar.gz#sha256=7644bc0ee35965d2e146dde31827b8982ed70a58281085fac42869a09764d38c (from https://pypi.org/simple/mako/), version: 1.0.3
  Found link https://files.pythonhosted.org/packages/7a/ae/925434246ee90b42e8ef57d3b30a0ab7caf9a2de3e449b876c56dcb48155/Mako-1.0.4.tar.gz#sha256=fed99dbe4d0ddb27a33ee4910d8708aca9ef1fe854e668387a9ab9a90cbf9059 (from https://pypi.org/simple/mako/), version: 1.0.4
  Found link https://files.pythonhosted.org/packages/20/ce/296b1037ed9b7803ed4e738b83ae244d2834e97e4ea24d52a6d46c12a884/Mako-1.0.5.tar.gz#sha256=e3e27cdd7abfd78337f33bd455f756c823c2d6224ad440a88f14bbd53a5ebc93 (from https://pypi.org/simple/mako/), version: 1.0.5
  Found link https://files.pythonhosted.org/packages/56/4b/cb75836863a6382199aefb3d3809937e21fa4cb0db15a4f4ba0ecc2e7e8e/Mako-1.0.6.tar.gz#sha256=48559ebd872a8e77f92005884b3d88ffae552812cdf17db6768e5c3be5ebbe0d (from https://pypi.org/simple/mako/), version: 1.0.6
  Found link https://files.pythonhosted.org/packages/eb/f3/67579bb486517c0d49547f9697e36582cd19dafb5df9e687ed8e22de57fa/Mako-1.0.7.tar.gz#sha256=4e02fde57bd4abb5ec400181e4c314f56ac3e49ba4fb8b0d50bba18cb27d25ae (from https://pypi.org/simple/mako/), version: 1.0.7
  Found link https://files.pythonhosted.org/packages/eb/69/6137c60cae2ab8c911bff510bb6d1d23a0189f75d114bb277606c6486b5f/Mako-1.0.8.tar.gz#sha256=04092940c0df49b01f43daea4f5adcecd0e50ef6a4b222be5ac003d5d84b2843 (from https://pypi.org/simple/mako/) (requires-python:>=2.6), version: 1.0.8
  Found link https://files.pythonhosted.org/packages/a1/bb/f4e5c056e883915c37bb5fb6fab7f00a923c395674f83bfb45c9ecf836b6/Mako-1.0.9.tar.gz#sha256=0728c404877cd4ca72c409c0ea372dc5f3b53fa1ad2bb434e1d216c0444ff1fd (from https://pypi.org/simple/mako/) (requires-python:>=2.6), version: 1.0.9
  Found link https://files.pythonhosted.org/packages/f9/93/63f78c552e4397549499169198698de23b559b52e57f27d967690811d16d/Mako-1.0.10.tar.gz#sha256=7165919e78e1feb68b4dbe829871ea9941398178fa58e6beedb9ba14acf63965 (from https://pypi.org/simple/mako/) (requires-python:>=2.6), version: 1.0.10
  Found link https://files.pythonhosted.org/packages/37/d7/2287b48aaeccdf2c75040fa5db69f6fad1877483aa6ce68316ab959ad1a0/Mako-1.0.11.tar.gz#sha256=889c7f16d5388092d4c585cf9def19cad089e9f848a7c40e03394553048362a6 (from https://pypi.org/simple/mako/) (requires-python:>=2.6), version: 1.0.11
  Found link https://files.pythonhosted.org/packages/0a/af/a6d8aa7b8909a36074f517b15222e3a2fbd5ef3452c0a686e3d43043dd3b/Mako-1.0.12.tar.gz#sha256=0cfa65de3a835e87eeca6ac856b3013aade55f49e32515f65d999f91a2324162 (from https://pypi.org/simple/mako/) (requires-python:>=2.6), version: 1.0.12
  Found link https://files.pythonhosted.org/packages/fa/29/8016763284d8fab844224f7cc5675cb4a388ebda0eb5a403260187e48435/Mako-1.0.13.tar.gz#sha256=95ee720cc3453063788515d55bd7ce4a2a77b7b209e4ac70ec5c86091eb02541 (from https://pypi.org/simple/mako/) (requires-python:>=2.6), version: 1.0.13
  Found link https://files.pythonhosted.org/packages/1b/a5/023aba3d69aacef6bfc13797bdc3dd03c6fb4ae2dcd2fde7dffc37233924/Mako-1.0.14.tar.gz#sha256=f5a642d8c5699269ab62a68b296ff990767eb120f51e2e8f3d6afb16bdb57f4b (from https://pypi.org/simple/mako/) (requires-python:>=2.6), version: 1.0.14
  Found link https://files.pythonhosted.org/packages/b0/3c/8dcd6883d009f7cae0f3157fb53e9afb05a0d3d33b3db1268ec2e6f4a56b/Mako-1.1.0.tar.gz#sha256=a36919599a9b7dc5d86a7a8988f23a9a3a3d083070023bab23d64f7f1d1e0a4b (from https://pypi.org/simple/mako/) (requires-python:>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*), version: 1.1.0
  Found link https://files.pythonhosted.org/packages/28/03/329b21f00243fc2d3815399413845dbbfb0745cff38a29d3597e97f8be58/Mako-1.1.1.tar.gz#sha256=2984a6733e1d472796ceef37ad48c26f4a984bb18119bb2dbc37a44d8f6e75a4 (from https://pypi.org/simple/mako/) (requires-python:>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*), version: 1.1.1
  Found link https://files.pythonhosted.org/packages/50/78/f6ade1e18aebda570eed33b7c534378d9659351cadce2fcbc7b31be5f615/Mako-1.1.2-py2.py3-none-any.whl#sha256=8e8b53c71c7e59f3de716b6832c4e401d903af574f6962edbbbf6ecc2a5fe6c9 (from https://pypi.org/simple/mako/) (requires-python:>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*), version: 1.1.2
  Found link https://files.pythonhosted.org/packages/42/64/fc7c506d14d8b6ed363e7798ffec2dfe4ba21e14dda4cfab99f4430cba3a/Mako-1.1.2.tar.gz#sha256=3139c5d64aa5d175dbafb95027057128b5fbd05a40c53999f3905ceb53366d9d (from https://pypi.org/simple/mako/) (requires-python:>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*), version: 1.1.2
  Found link https://files.pythonhosted.org/packages/a6/37/0e706200d22172eb8fa17d68a7ae22dec7631a0a92266634fb518a88a5b2/Mako-1.1.3-py2.py3-none-any.whl#sha256=93729a258e4ff0747c876bd9e20df1b9758028946e976324ccd2d68245c7b6a9 (from https://pypi.org/simple/mako/) (requires-python:>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*), version: 1.1.3
  Found link https://files.pythonhosted.org/packages/72/89/402d2b4589e120ca76a6aed8fee906a0f5ae204b50e455edd36eda6e778d/Mako-1.1.3.tar.gz#sha256=8195c8c1400ceb53496064314c6736719c6f25e7479cd24c77be3d9361cddc27 (from https://pypi.org/simple/mako/) (requires-python:>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*), version: 1.1.3
  Found link https://files.pythonhosted.org/packages/5c/db/2d2d88b924aa4674a080aae83b59ea19d593250bfe5ed789947c21736785/Mako-1.1.4.tar.gz#sha256=17831f0b7087c313c0ffae2bcbbd3c1d5ba9eeac9c38f2eb7b50e8c99fe9d5ab (from https://pypi.org/simple/mako/) (requires-python:>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*), version: 1.1.4
Given no hashes to check 61 links for project 'mako': discarding no candidates
Using version 1.1.4 (newest of versions: 0.1.0, 0.1.1, 0.1.2, 0.1.3, 0.1.4, 0.1.5, 0.1.6, 0.1.7, 0.1.8, 0.1.9, 0.1.10, 0.2.0, 0.2.1, 0.2.2, 0.2.3, 0.2.4, 0.2.5, 0.3.0, 0.3.1, 0.3.2, 0.3.3, 0.3.4, 0.3.5, 0.3.6, 0.4.0, 0.4.1, 0.4.2, 0.5.0, 0.6.0, 0.6.1, 0.6.2, 0.7.0, 0.7.1, 0.7.2, 0.7.3, 0.8.0, 0.8.1, 0.9.0, 0.9.1, 1.0.0, 1.0.1, 1.0.2, 1.0.3, 1.0.4, 1.0.5, 1.0.6, 1.0.7, 1.0.8, 1.0.9, 1.0.10, 1.0.11, 1.0.12, 1.0.13, 1.0.14, 1.1.0, 1.1.1, 1.1.2, 1.1.3, 1.1.4)
Collecting mako
  Created temporary directory: /tmp/pip-unpack-x3f4xytc
  Getting credentials from keyring for files.pythonhosted.org
  https://files.pythonhosted.org:443 "GET /packages/5c/db/2d2d88b924aa4674a080aae83b59ea19d593250bfe5ed789947c21736785/Mako-1.1.4.tar.gz HTTP/1.1" 200 479823
  Downloading Mako-1.1.4.tar.gz (479 kB)
     |████████████████████████████████| 479 kB 13.2 MB/s 
  Added mako from https://files.pythonhosted.org/packages/5c/db/2d2d88b924aa4674a080aae83b59ea19d593250bfe5ed789947c21736785/Mako-1.1.4.tar.gz#sha256=17831f0b7087c313c0ffae2bcbbd3c1d5ba9eeac9c38f2eb7b50e8c99fe9d5ab (from pdoc3) to build tracker '/tmp/pip-req-tracker-xq_mui27'
    Running setup.py (path:/tmp/pip-install-b1uccvc_/mako/setup.py) egg_info for package mako
    Running command python setup.py egg_info
    running egg_info
    creating /tmp/pip-install-b1uccvc_/mako/pip-egg-info/Mako.egg-info
    writing /tmp/pip-install-b1uccvc_/mako/pip-egg-info/Mako.egg-info/PKG-INFO
    writing dependency_links to /tmp/pip-install-b1uccvc_/mako/pip-egg-info/Mako.egg-info/dependency_links.txt
    writing entry points to /tmp/pip-install-b1uccvc_/mako/pip-egg-info/Mako.egg-info/entry_points.txt
    writing requirements to /tmp/pip-install-b1uccvc_/mako/pip-egg-info/Mako.egg-info/requires.txt
    writing top-level names to /tmp/pip-install-b1uccvc_/mako/pip-egg-info/Mako.egg-info/top_level.txt
    writing manifest file '/tmp/pip-install-b1uccvc_/mako/pip-egg-info/Mako.egg-info/SOURCES.txt'
    reading manifest file '/tmp/pip-install-b1uccvc_/mako/pip-egg-info/Mako.egg-info/SOURCES.txt'
    reading manifest template 'MANIFEST.in'
    warning: no files found matching '*.mako' under directory 'doc'
    warning: no files found matching '*.xml' under directory 'examples'
    warning: no files found matching '*.mako' under directory 'examples'
    no previously-included directories found matching 'doc/build/output'
    writing manifest file '/tmp/pip-install-b1uccvc_/mako/pip-egg-info/Mako.egg-info/SOURCES.txt'
  Source in /tmp/pip-install-b1uccvc_/mako has version 1.1.4, which satisfies requirement mako from https://files.pythonhosted.org/packages/5c/db/2d2d88b924aa4674a080aae83b59ea19d593250bfe5ed789947c21736785/Mako-1.1.4.tar.gz#sha256=17831f0b7087c313c0ffae2bcbbd3c1d5ba9eeac9c38f2eb7b50e8c99fe9d5ab (from pdoc3)
  Removed mako from https://files.pythonhosted.org/packages/5c/db/2d2d88b924aa4674a080aae83b59ea19d593250bfe5ed789947c21736785/Mako-1.1.4.tar.gz#sha256=17831f0b7087c313c0ffae2bcbbd3c1d5ba9eeac9c38f2eb7b50e8c99fe9d5ab (from pdoc3) from build tracker '/tmp/pip-req-tracker-xq_mui27'
1 location(s) to search for versions of markdown:
* https://pypi.org/simple/markdown/
Fetching project page and analyzing links: https://pypi.org/simple/markdown/
Getting page https://pypi.org/simple/markdown/
Found index url https://pypi.org/simple
Getting credentials from keyring for https://pypi.org/simple
Getting credentials from keyring for pypi.org
https://pypi.org:443 "GET /simple/markdown/ HTTP/1.1" 200 7779
  Found link https://files.pythonhosted.org/packages/de/23/1d9c21c95d8aaf06a4a1b1fe265591a8d93cd32bc6e8e57c630a0b84c476/markdown-1.7.tar.gz#sha256=1d11859f79bcf502572ad9e582dbed827f8fca3b6379173a283bc3080a0578d8 (from https://pypi.org/simple/markdown/), version: 1.7
  Skipping link: unsupported archive format: .exe: https://files.pythonhosted.org/packages/ae/8b/096165ba719ad4e55ab1fe9fb643cd24836bb23c793899a34084ea8b1a12/markdown-1.7.win32.exe#sha256=1243a1958868af4a02b2da63ea714feb62f2c1342137a9c2a1ca68de75855c62 (from https://pypi.org/simple/markdown/)
  Found link https://files.pythonhosted.org/packages/c2/44/9b774c90d6ebf543f08c4c06bc60065d931f7f5b72ad7526d80a86bc0d7d/markdown-1.7.zip#sha256=9600c27dc1266e40f06a94212b0620f97b71195f8dff6521152ac0fcae4b04e9 (from https://pypi.org/simple/markdown/), version: 1.7
  Found link https://files.pythonhosted.org/packages/59/0d/ab8fce37cabe1bed8daf8c1bc18056900cd700bf3ef135e0756afbc9c2a2/Markdown-2.0.tar.gz#sha256=fd9b22b7d69ffb9e26a993de61c74ca173ed861f1f5bf30858a069e4047757c1 (from https://pypi.org/simple/markdown/), version: 2.0
  Skipping link: unsupported archive format: .exe: https://files.pythonhosted.org/packages/ce/c5/fdcc44de01e4ccc76c1284d25b9b5b650240069b22e602598da4f991a319/Markdown-2.0.win32.exe#sha256=f10f7ab957e25d9f6b3489784c31593363f597ea3904631398279b148b10997a (from https://pypi.org/simple/markdown/)
  Found link https://files.pythonhosted.org/packages/a0/8d/94868abb78a8f99ce9ac15a4db472a3384a0beca36bff7bf5ef9be02012f/Markdown-2.0.zip#sha256=6b336ad5c79b69b9361b6826069ed96665fce536e4aa098a99126a65b2d16992 (from https://pypi.org/simple/markdown/), version: 2.0
  Found link https://files.pythonhosted.org/packages/66/7b/00bd2ffa9a36cf6fe5b49f01eb886863968d2e30923dadf0139d78d3c961/Markdown-2.0.1.tar.gz#sha256=ac63daef3cf5fd12853e19002914dcb459ae465769981238da2839c2dcf41652 (from https://pypi.org/simple/markdown/), version: 2.0.1
  Skipping link: unsupported archive format: .exe: https://files.pythonhosted.org/packages/1a/42/578c96a429672b48a55841f0afc8a5a8fadbd5b0c7931a6adc76cdd28129/Markdown-2.0.1.win32.exe#sha256=8930bde283ca5e9fb4849f022fb335874a40a7d3fbbab0de30b7f85e37d24d79 (from https://pypi.org/simple/markdown/)
  Found link https://files.pythonhosted.org/packages/cd/7a/ee53d59417bc49f9594657813158e448bde092df7fdea236edae082291a3/Markdown-2.0.1.zip#sha256=351e5428cde10875f3841d75fd920894044e31559350056dc044e4ad3d46c3d5 (from https://pypi.org/simple/markdown/), version: 2.0.1
  Found link https://files.pythonhosted.org/packages/40/7c/077648ce4b7cf5d8b376bf85c2415a5e2f9afd7fbdff4c30a89250132dc9/Markdown-2.0.2.tar.gz#sha256=9070e33d2ac5397adf4cb83a7828e7bcc729dfc33a10e8851585b4d8f0baff4e (from https://pypi.org/simple/markdown/), version: 2.0.2
  Skipping link: unsupported archive format: .exe: https://files.pythonhosted.org/packages/6a/32/cfa3c49873ba5f68dff1c0e4b5897e5122c544ffdc8e2c57b55fa20b61ce/Markdown-2.0.2.win32.exe#sha256=4de77dcea22453dede8366d0acdecde4b34d03cfd183a8818dc3e7ee53853879 (from https://pypi.org/simple/markdown/)
  Found link https://files.pythonhosted.org/packages/8e/97/b5e29c302c815792ab50477c7c5b5c6ebe216704f05074c55da6b47b447c/Markdown-2.0.2.zip#sha256=3a97a0e84c7d354d5254acb6836a5f467f27f1baacd321fc34949f28e8a16a64 (from https://pypi.org/simple/markdown/), version: 2.0.2
  Found link https://files.pythonhosted.org/packages/80/cd/12d6ee56a24ecd3c6fc582d5e5016f40db4abdfb16e7affc49780184d1df/Markdown-2.0.3.tar.gz#sha256=fff5d887cbf82dca288e55c8c240c435ca6ca80fb11d0b3c9fc44464fdece740 (from https://pypi.org/simple/markdown/), version: 2.0.3
  Skipping link: unsupported archive format: .exe: https://files.pythonhosted.org/packages/c8/a2/8426d0d1852851b56c77abd6252f710718199354bd9f739d0a3de98ac39d/Markdown-2.0.3.win32.exe#sha256=c0c140763ccaba21ca0b37bc6a67bbc77d512bcf817c46800947331f12905393 (from https://pypi.org/simple/markdown/)
  Found link https://files.pythonhosted.org/packages/2f/09/c28c1b056e23a2a29e0203acc13d989ee04c22ee7c4744cb876a033e06f8/Markdown-2.0.3.zip#sha256=8eb459f8e8f1318fd03e4fe807b314feb7201f835feae746e652778eedcbaea3 (from https://pypi.org/simple/markdown/), version: 2.0.3
  Found link https://files.pythonhosted.org/packages/a6/5e/6f5a9753526a03839f044daeb20f8fd461395a48b80f335168dabd732d1f/Markdown-2.1.0.tar.gz#sha256=ab537478e98137c0fa1cb4149adae23ddc56490ca6e8bb1b6130d91ada81d964 (from https://pypi.org/simple/markdown/), version: 2.1.0
  Skipping link: unsupported archive format: .exe: https://files.pythonhosted.org/packages/ac/e3/18176a76dd6eea736451b33a9d04531882c64cdbeb781407f553144557a2/Markdown-2.1.0.win32.exe#sha256=47b77cac8a6221aba56a085dfb0e2360e9cf1cc7878870ed8d3422228e9b86a2 (from https://pypi.org/simple/markdown/)
  Found link https://files.pythonhosted.org/packages/0b/80/693dbc12e544fd1149af7e668220bab7ea517afc60dd8271f7345c0b7078/Markdown-2.1.0.zip#sha256=6e771ea72a0484843edaa89d228e6fe181e541697a0d680dd84e52f8f846bf10 (from https://pypi.org/simple/markdown/), version: 2.1.0
  Found link https://files.pythonhosted.org/packages/42/b7/53c55d79022ee536f95b016e174c555b796ff19d731f5ca182a89fd85e0d/Markdown-2.1.1.tar.gz#sha256=be6c8cc8163875062b60d759451fec1e55fd3426321b52a6a9077a3f95503864 (from https://pypi.org/simple/markdown/), version: 2.1.1
  Found link https://files.pythonhosted.org/packages/52/dd/98b64ec40957ef264d6ef8aca0da55ece25eb5ad1902fe521e24a2d18ced/Markdown-2.1.1.zip#sha256=30f838bf913dd1e99c4d28920c70d9e67270c640280968b0725f34dfa64736e0 (from https://pypi.org/simple/markdown/), version: 2.1.1
  Found link https://files.pythonhosted.org/packages/ac/99/288a81a38526a42c98b5b9832c6e339ca8d5dd38b19a53abfac7c8037c7f/Markdown-2.2.0.tar.gz#sha256=98e1b0a0b2f87b8310d2060a560f427c24ee16c96c83c98ea416f1f8ddc379b5 (from https://pypi.org/simple/markdown/), version: 2.2.0
  Found link https://files.pythonhosted.org/packages/f1/9b/abac7cce338f4d832b9301c978103fd280f7ead4de869f4eb247beeac32b/Markdown-2.2.0.zip#sha256=7e6497c915492ff3729c62f245acda9d23ad0616185aee927d61bd6dbb0abad3 (from https://pypi.org/simple/markdown/), version: 2.2.0
  Found link https://files.pythonhosted.org/packages/4b/f6/42742630b6baf96f3c12ab811daef49841aac0df4e74e738a5fabb58fa41/Markdown-2.2.1.tar.gz#sha256=f8b9a1efceab71afe9336a7c456fde36bfb0f505fb664ebb7f3dd44eddab44b6 (from https://pypi.org/simple/markdown/), version: 2.2.1
  Found link https://files.pythonhosted.org/packages/2a/05/5d7d994904f8ea5643a69c8b37312a9e49517a261ada880dbbea70de2e3e/Markdown-2.2.1.zip#sha256=4a402dadb4053f3a0c57e3400553872a1b4ad64f90a85102392417a1bece2e3b (from https://pypi.org/simple/markdown/), version: 2.2.1
  Found link https://files.pythonhosted.org/packages/cf/61/6fa953530db38d47e594b55065ff1bf58f52f267da9df08285894c9c0078/Markdown-2.3.tar.gz#sha256=b2175e573eedf4cff47f116f06a53ba50aeb0656ff58a9577e0547cd5b0be3ab (from https://pypi.org/simple/markdown/), version: 2.3
  Found link https://files.pythonhosted.org/packages/8a/5f/2e9f61e20f65bb93155b096e19f313f7b8d5a562e66c019c68fad2fc7df2/Markdown-2.3.zip#sha256=b460173f1a8e10000ec6b5f27517256a9f77390f0c3613e213e4a073239b3cb5 (from https://pypi.org/simple/markdown/), version: 2.3
  Found link https://files.pythonhosted.org/packages/78/e9/f433f3774d27ae6748a601ba8607e433eec23e8b3ddd4ea88338de8443bf/Markdown-2.3.1.tar.gz#sha256=ffebd9385717aba00ff4e95b705b7693ddf12a7d483483d441218b6d3f4cf290 (from https://pypi.org/simple/markdown/), version: 2.3.1
  Found link https://files.pythonhosted.org/packages/7f/49/44ecaf1afc7012ae96989493ec7cf5891fa8084d5fa4c1e740b37e50e558/Markdown-2.3.1.zip#sha256=0c9f37fc36f1fc3d5ec4170133f73314d3e361630bf4c3cf3a47bbf98810bdc0 (from https://pypi.org/simple/markdown/), version: 2.3.1
  Found link https://files.pythonhosted.org/packages/ce/5d/d259c3b20aaafade22b3fb220fcfeee03124562ace2c6ddba7a5474a76c5/Markdown-2.4.tar.gz#sha256=b8370fce4fbcd6b68b6b36c0fb0f4ec24d6ba37ea22988740f4701536611f1ae (from https://pypi.org/simple/markdown/), version: 2.4
  Skipping link: unsupported archive format: .exe: https://files.pythonhosted.org/packages/2c/12/820b5b425adc09552d7edd505d2a3e38b2e5101b8741804461a251ea159b/Markdown-2.4.win-amd64.exe#sha256=6f83e8368fa3ab13dc9d9ab7f6214e2cc7df7242024bdaa9f7a90e3e7281bdbf (from https://pypi.org/simple/markdown/)
  Found link https://files.pythonhosted.org/packages/99/61/d67ba7cbcd5369bb0c6dc4bcccbc3ada94263e0898ac14c767b83f963457/Markdown-2.4.zip#sha256=711e52a84eb3553a4640c3cd87e063067c160349965162dae835779b3ab586bb (from https://pypi.org/simple/markdown/), version: 2.4
  Found link https://files.pythonhosted.org/packages/1e/67/2c34338f6a94f4dbac6737915eb9a30082ce32109138f5b95ec687e8f737/Markdown-2.4.1.tar.gz#sha256=812ec5249f45edc31330b7fb06e52aaf6ab2d83aa27047df7cb6837ef2d269b6 (from https://pypi.org/simple/markdown/), version: 2.4.1
  Found link https://files.pythonhosted.org/packages/9a/cf/976e393c9e88401f3fee18abf09e9aa44d8fce3ea7a2262ad748a3de5459/Markdown-2.4.1.zip#sha256=866f5474c2361de7ccf806b438c0462380b4b90aacb9fdf59dfc4b166fb66389 (from https://pypi.org/simple/markdown/), version: 2.4.1
  Found link https://files.pythonhosted.org/packages/79/22/1f3c8cd9731873d63cef2a5bfaba2a198e703dd53d46f2ae7634a58a175b/Markdown-2.5.tar.gz#sha256=6ba74a1e7141c9603750d80711b639a7577bffb785708e6260090239ee5bc76d (from https://pypi.org/simple/markdown/), version: 2.5
  Found link https://files.pythonhosted.org/packages/16/7f/034572fbc66f76a626156c9500349f5b384ca1f38194318ddde32bc2fcb0/Markdown-2.5.zip#sha256=e16b754e986408c87f5dcdd79d5c4702cf105f175aa6ade4edfd7e469f8dbd96 (from https://pypi.org/simple/markdown/), version: 2.5
  Found link https://files.pythonhosted.org/packages/e6/fb/1ad3b8e4318ff4a9547fe435224f5db12ec2e7c5e1d6107c87b88fb19268/Markdown-2.5.1.tar.gz#sha256=8f81ed12c18608a502828acb7d318f362c42f4eca97d01e93cadfc52c1e40b73 (from https://pypi.org/simple/markdown/), version: 2.5.1
  Found link https://files.pythonhosted.org/packages/8b/5d/bd5f5f161d955c4f2389df7cf176af0dffc12cf976b6ac8639e9276a73e0/Markdown-2.5.1.zip#sha256=5ca06751230143520016f39ff8244329a20985f713817d8a93840a28b3ec2fc0 (from https://pypi.org/simple/markdown/), version: 2.5.1
  Found link https://files.pythonhosted.org/packages/f8/c2/29d4cdd2305c8ed3a86d0f5061856c8f37ab2ad25d970e6be4e37e4d5d90/Markdown-2.5.2.tar.gz#sha256=284e97e56db9ada03ede9c0ed2870ca6590ce7869f3119104d53510debf1533d (from https://pypi.org/simple/markdown/), version: 2.5.2
  Found link https://files.pythonhosted.org/packages/cd/57/59e27269ded841b189d218020447ea8de2bcbab293df285328091e299041/Markdown-2.5.2.zip#sha256=ec754ad77d3db9647e155caeb695e10b288ce012de581577496b3bc49393f086 (from https://pypi.org/simple/markdown/), version: 2.5.2
  Found link https://files.pythonhosted.org/packages/1e/d4/8720229d479bf30b0c42998c2a4331adfa1382527613f14b5fb60d034dfd/Markdown-2.6.tar.gz#sha256=e1c8a489bb7c7154bc5a8c14f0fd1fc356ee36c8b9988f9fd8febff22dd435da (from https://pypi.org/simple/markdown/), version: 2.6
  Found link https://files.pythonhosted.org/packages/33/b0/62482489865f85d7818f43b30c7924a19911348be75363b1fa87950d3a83/Markdown-2.6.zip#sha256=9d8658d81626c03ee9d9dfcbb516382dd9064e21eeb184dda19ab42b168c8633 (from https://pypi.org/simple/markdown/), version: 2.6
  Found link https://files.pythonhosted.org/packages/75/01/1e68a8d388d3f9fa741a098546379fb0c1684b9f5a07725e5c69638bd578/Markdown-2.6.1.tar.gz#sha256=b5879b87e8e5c125c92ab8c8f3babce78ad4e840446eed73c5b6e2984648d2b1 (from https://pypi.org/simple/markdown/), version: 2.6.1
  Found link https://files.pythonhosted.org/packages/14/f8/0e7e0fac449eeb71d3eca9e8d710b3049f9f214bb24e328e3e8ad46cb905/Markdown-2.6.1.zip#sha256=37ed4578d40ff2948f61083193143e01403e666b02bb30acdccc9058e6cb5ff5 (from https://pypi.org/simple/markdown/), version: 2.6.1
  Found link https://files.pythonhosted.org/packages/59/bf/6bce4d6d91d25eaa58d8e88d8994b2b603ed1b223b25a92f68c3fd0e8fd9/Markdown-2.6.2-py2.py3-none-any.whl#sha256=df3bbae578f29767571b5ce67a4702fe14ed6710b97bab59251a5113b6bec3a3 (from https://pypi.org/simple/markdown/), version: 2.6.2
  Found link https://files.pythonhosted.org/packages/62/8b/83658b5f6c220d5fcde9f9852d46ea54765d734cfbc5a9f4c05bfc36db4d/Markdown-2.6.2.tar.gz#sha256=ee17d0d7dc091e645dd48302a2e21301cc68f188505c2069d8635f94554170bf (from https://pypi.org/simple/markdown/), version: 2.6.2
  Found link https://files.pythonhosted.org/packages/62/e7/7201086fe0ca3fd50ff0454130dc12527764ef5756c65b0f67ae9d83d117/Markdown-2.6.2.zip#sha256=30ff37bf64245c5fe4c6fbb6967efacd03bef9abbd0fc1de3c888d26a9dbc85b (from https://pypi.org/simple/markdown/), version: 2.6.2
  Found link https://files.pythonhosted.org/packages/ab/7c/28c26521cf556bde687ba224e4408bd7a55f4d03f5b96f52deedb85291f5/Markdown-2.6.3.tar.gz#sha256=ad75fc03c45492eba3bc63645e1e6465f65523a05fff0abf36910f810465a9af (from https://pypi.org/simple/markdown/), version: 2.6.3
  Found link https://files.pythonhosted.org/packages/e8/51/169adeea210503b2c32e29653065763b27fd4f1eeaf415d263c72c6308f4/Markdown-2.6.3.zip#sha256=ac8bde88ae93f5191c486d1a447af18d60bb02f4853fa3157e4f73d303bf500a (from https://pypi.org/simple/markdown/), version: 2.6.3
  Found link https://files.pythonhosted.org/packages/bd/ce/e0cdacfce54c4b3e123985e262f2697ff15ed195710575abb93b8fb56110/Markdown-2.6.4.tar.gz#sha256=e436eee7aaf2a230ca3315034dd39e8a0fc27036708acaa3dd70625ec62a94ce (from https://pypi.org/simple/markdown/), version: 2.6.4
  Found link https://files.pythonhosted.org/packages/e4/e0/54c7f2e3e8c495a46b38842b01ee10179bee384f52b728594fce4fd431d7/Markdown-2.6.4.zip#sha256=16fbd4960fe59bc8cdd029f31dd29ecee40f21ec27ccd6a642d74a32d5d57d5c (from https://pypi.org/simple/markdown/), version: 2.6.4
  Found link https://files.pythonhosted.org/packages/e0/e6/e373d058113efc3fcede632de0c76ded309892c405f960c45acd0250060f/Markdown-2.6.5.tar.gz#sha256=8d94cf6273606f76753fcb1324623792b3738c7612c2b180c85cc5e88642e560 (from https://pypi.org/simple/markdown/), version: 2.6.5
  Found link https://files.pythonhosted.org/packages/bb/78/5f1f5280cf645f99c35392198b302e336ae477258d83d2b3e178831874f0/Markdown-2.6.5.zip#sha256=a59fdbcec28f79ad9842ea7f74cde5a02e14a3025836e0bc66c4fc48596ce2ca (from https://pypi.org/simple/markdown/), version: 2.6.5
  Found link https://files.pythonhosted.org/packages/9b/53/4492f2888408a2462fd7f364028b6c708f3ecaa52a028587d7dd729f40b4/Markdown-2.6.6.tar.gz#sha256=9a292bb40d6d29abac8024887bcfc1159d7a32dc1d6f1f6e8d6d8e293666c504 (from https://pypi.org/simple/markdown/), version: 2.6.6
  Found link https://files.pythonhosted.org/packages/14/eb/ae35c7d154eb9395c49950788e738effd0e2e8293544e8ee7558a369d7e8/Markdown-2.6.6.zip#sha256=022239550fb4a84bcc3b3b42dff9a41efc56d773ef17c4f28016dd8f265c82d0 (from https://pypi.org/simple/markdown/), version: 2.6.6
  Found link https://files.pythonhosted.org/packages/d4/32/642bd580c577af37b00a1eb59b0eaa996f2d11dfe394f3dd0c7a8a2de81a/Markdown-2.6.7.tar.gz#sha256=daebf24846efa7ff269cfde8c41a48bb2303920c7b2c7c5e04fa82e6282d05c0 (from https://pypi.org/simple/markdown/), version: 2.6.7
  Found link https://files.pythonhosted.org/packages/48/a4/fc6b002789c2239ac620ca963694c95b8f74e4747769cdf6021276939e74/Markdown-2.6.7.zip#sha256=61169c455b0e541ac8b6d0cac33c785f14d486b4b24f28a58d63faeec6f2d0a8 (from https://pypi.org/simple/markdown/), version: 2.6.7
  Found link https://files.pythonhosted.org/packages/1d/25/3f6d2cb31ec42ca5bd3bfbea99b63892b735d76e26f20dd2dcc34ffe4f0d/Markdown-2.6.8.tar.gz#sha256=0ac8a81e658167da95d063a9279c9c1b2699f37c7c4153256a458b3a43860e33 (from https://pypi.org/simple/markdown/), version: 2.6.8
  Found link https://files.pythonhosted.org/packages/29/82/dfe242bcfd9eec0e7bf93a80a8f8d8515a95b980c44f5c0b45606397a423/Markdown-2.6.9.tar.gz#sha256=73af797238b95768b3a9b6fe6270e250e5c09d988b8e5b223fd5efa4e06faf81 (from https://pypi.org/simple/markdown/), version: 2.6.9
  Found link https://files.pythonhosted.org/packages/f0/68/d7d5503adbd302fb8e44c8ece2b8afff467a888efb8a0a116c432cc4f4fe/Markdown-2.6.10.zip#sha256=cfa536d1ee8984007fcecc5a38a493ff05c174cb74cb2341dafd175e6bc30851 (from https://pypi.org/simple/markdown/), version: 2.6.10
  Found link https://files.pythonhosted.org/packages/6d/7d/488b90f470b96531a3f5788cf12a93332f543dbab13c423a5e7ce96a0493/Markdown-2.6.11-py2.py3-none-any.whl#sha256=9ba587db9daee7ec761cfc656272be6aabe2ed300fece21208e4aab2e457bc8f (from https://pypi.org/simple/markdown/), version: 2.6.11
  Found link https://files.pythonhosted.org/packages/b3/73/fc5c850f44af5889192dff783b7b0d8f3fe8d30b65c8e3f78f8f0265fecf/Markdown-2.6.11.tar.gz#sha256=a856869c7ff079ad84a3e19cd87a64998350c2b94e9e08e44270faef33400f81 (from https://pypi.org/simple/markdown/), version: 2.6.11
  Found link https://files.pythonhosted.org/packages/7a/fd/e22357c299e93c0bc11ec8ba54e79f98dd568e09adfe9b39d6852c744938/Markdown-3.0-py2.py3-none-any.whl#sha256=80f44d67c4f34db6ae8210a7194c7335923744181b6240e06d67479478eb7bb9 (from https://pypi.org/simple/markdown/) (requires-python:>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*), version: 3.0
  Found link https://files.pythonhosted.org/packages/35/c6/8144e57cf7053aa3c8a6c5523fe1aafd77f11b4b563049561c80d2d685c0/Markdown-3.0.tar.gz#sha256=b853a125f03db3f2fdbcbc96fb738f2a7f2cdabc3f1262a4d89121c6ce1bd7e3 (from https://pypi.org/simple/markdown/) (requires-python:>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*), version: 3.0
  Found link https://files.pythonhosted.org/packages/7a/6b/5600647404ba15545ec37d2f7f58844d690baf2f81f3a60b862e48f29287/Markdown-3.0.1-py2.py3-none-any.whl#sha256=c00429bd503a47ec88d5e30a751e147dcb4c6889663cd3e2ba0afe858e009baa (from https://pypi.org/simple/markdown/) (requires-python:>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*), version: 3.0.1
  Found link https://files.pythonhosted.org/packages/3c/52/7bae9e99a7a4be6af4a713fe9b692777e6468d28991c54c273dfb6ec9fb2/Markdown-3.0.1.tar.gz#sha256=d02e0f9b04c500cde6637c11ad7c72671f359b87b9fe924b2383649d8841db7c (from https://pypi.org/simple/markdown/) (requires-python:>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*), version: 3.0.1
  Found link https://files.pythonhosted.org/packages/f5/e4/d8c18f2555add57ff21bf25af36d827145896a07607486cc79a2aea641af/Markdown-3.1-py2.py3-none-any.whl#sha256=fe463ff51e679377e3624984c829022e2cfb3be5518726b06f608a07a3aad680 (from https://pypi.org/simple/markdown/) (requires-python:>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*), version: 3.1
  Found link https://files.pythonhosted.org/packages/51/3f/92f9d2f4a1d5da51e7808a469ab40c6cfdf3ba1013f56abb1f46677a655c/Markdown-3.1.tar.gz#sha256=fc4a6f69a656b8d858d7503bda633f4dd63c2d70cf80abdc6eafa64c4ae8c250 (from https://pypi.org/simple/markdown/) (requires-python:>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*), version: 3.1
  Found link https://files.pythonhosted.org/packages/c0/4e/fd492e91abdc2d2fcb70ef453064d980688762079397f779758e055f6575/Markdown-3.1.1-py2.py3-none-any.whl#sha256=56a46ac655704b91e5b7e6326ce43d5ef72411376588afa1dd90e881b83c7e8c (from https://pypi.org/simple/markdown/) (requires-python:>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*), version: 3.1.1
  Found link https://files.pythonhosted.org/packages/ac/df/0ae25a9fd5bb528fe3c65af7143708160aa3b47970d5272003a1ad5c03c6/Markdown-3.1.1.tar.gz#sha256=2e50876bcdd74517e7b71f3e7a76102050edec255b3983403f1a63e7c8a41e7a (from https://pypi.org/simple/markdown/) (requires-python:>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*), version: 3.1.1
  Found link https://files.pythonhosted.org/packages/d5/16/c5a68ef8c62406b3bbd8f49199bbae56feb390746a284c4cf036c687465f/Markdown-3.2-py2.py3-none-any.whl#sha256=9c71241ec237505535eabff7a38b1307250f16cea174bb1e505c3e032f108867 (from https://pypi.org/simple/markdown/) (requires-python:>=3.5), version: 3.2
  Found link https://files.pythonhosted.org/packages/3a/0b/6deec230d8c30f1ae569e4cfca5fd202d912dbf61f338d4d86b284a40812/Markdown-3.2.tar.gz#sha256=5ad7180c3ec16422a764568ad6409ec82460c40d1631591fa53d597033cc98bf (from https://pypi.org/simple/markdown/) (requires-python:>=3.5), version: 3.2
  Found link https://files.pythonhosted.org/packages/ab/c4/ba46d44855e6eb1770a12edace5a165a0c6de13349f592b9036257f3c3d3/Markdown-3.2.1-py2.py3-none-any.whl#sha256=e4795399163109457d4c5af2183fbe6b60326c17cfdf25ce6e7474c6624f725d (from https://pypi.org/simple/markdown/) (requires-python:>=3.5), version: 3.2.1
  Found link https://files.pythonhosted.org/packages/98/79/ce6984767cb9478e6818bd0994283db55c423d733cc62a88a3ffb8581e11/Markdown-3.2.1.tar.gz#sha256=90fee683eeabe1a92e149f7ba74e5ccdc81cd397bd6c516d93a8da0ef90b6902 (from https://pypi.org/simple/markdown/) (requires-python:>=3.5), version: 3.2.1
  Found link https://files.pythonhosted.org/packages/a4/63/eaec2bd025ab48c754b55e8819af0f6a69e2b1e187611dd40cbbe101ee7f/Markdown-3.2.2-py3-none-any.whl#sha256=c467cd6233885534bf0fe96e62e3cf46cfc1605112356c4f9981512b8174de59 (from https://pypi.org/simple/markdown/) (requires-python:>=3.5), version: 3.2.2
  Found link https://files.pythonhosted.org/packages/44/30/cb4555416609a8f75525e34cbacfc721aa5b0044809968b2cf553fd879c7/Markdown-3.2.2.tar.gz#sha256=1fafe3f1ecabfb514a5285fca634a53c1b32a81cb0feb154264d55bf2ff22c17 (from https://pypi.org/simple/markdown/) (requires-python:>=3.5), version: 3.2.2
  Found link https://files.pythonhosted.org/packages/0e/ee/173f66a1954046debff7f4199cc826fc29d9e8521e1ae7a1c9d2bf858ea1/Markdown-3.3-py3-none-any.whl#sha256=fbb1ba54ca41e8991dc5a561d9c6f752f5e4546f8750e56413ea50f2385761d3 (from https://pypi.org/simple/markdown/) (requires-python:>=3.6), version: 3.3
  Found link https://files.pythonhosted.org/packages/92/57/9fd44cf022281ac9af66ac86d309351320ada5ec177c7e59e8e7861e90c3/Markdown-3.3.tar.gz#sha256=4f4172a4e989b97f96860fa434b89895069c576e2b537c4b4eed265266a7affc (from https://pypi.org/simple/markdown/) (requires-python:>=3.6), version: 3.3
  Found link https://files.pythonhosted.org/packages/7a/2e/d769892bfb09144ad79ef525de0cb1765382e012cdd31aa117bef2ca7f66/Markdown-3.3.1-py3-none-any.whl#sha256=10db1204a6c4aff7c7cf3cf25cc02761703baea54b6fb5e2b9ce2c186d81116f (from https://pypi.org/simple/markdown/) (requires-python:>=3.6), version: 3.3.1
  Found link https://files.pythonhosted.org/packages/cf/76/688d96f8e1d5e2be2ccf66bb4b2e84e0f38b4748c13d5ff756ee0ae352fd/Markdown-3.3.1.tar.gz#sha256=c3ce9ebb035c078cac0f2036068d054e7dc34354eeecc49c173c33c96b124af6 (from https://pypi.org/simple/markdown/) (requires-python:>=3.6), version: 3.3.1
  Found link https://files.pythonhosted.org/packages/a0/34/4d6b7e3044044e89eaa25ed5395656cc351163c625fda0656d2729de399f/Markdown-3.3.2-py3-none-any.whl#sha256=77b7bff443b1f97b4814fa438c181fd5882e31edb01b422856b3feca91475f3e (from https://pypi.org/simple/markdown/) (requires-python:>=3.6), version: 3.3.2
  Found link https://files.pythonhosted.org/packages/a1/c4/baa09aa2da7281e3da5137b1073e6ebfd6acf52ac885a363b7b3b5556402/Markdown-3.3.2.tar.gz#sha256=4b71fbd2db30c1dfb400f22b25f41cb823fc1db0aa8b7b67d120644f92cc1011 (from https://pypi.org/simple/markdown/) (requires-python:>=3.6), version: 3.3.2
  Found link https://files.pythonhosted.org/packages/ac/ef/24a91ca96efa0d7802dffb83ccc7a3c677027bea19ec3c9ee80be740408e/Markdown-3.3.3-py3-none-any.whl#sha256=c109c15b7dc20a9ac454c9e6025927d44460b85bd039da028d85e2b6d0bcc328 (from https://pypi.org/simple/markdown/) (requires-python:>=3.6), version: 3.3.3
  Found link https://files.pythonhosted.org/packages/fd/d6/9eeda2f440ef798c8222b77d7355199345ce3477941d8a02a2024ccb9ed2/Markdown-3.3.3.tar.gz#sha256=5d9f2b5ca24bc4c7a390d22323ca4bad200368612b5aaa7796babf971d2b2f18 (from https://pypi.org/simple/markdown/) (requires-python:>=3.6), version: 3.3.3
Given no hashes to check 22 links for project 'markdown': discarding no candidates
Using version 3.3.3 (newest of versions: 3.0, 3.0.1, 3.1, 3.1.1, 3.2, 3.2.1, 3.2.2, 3.3, 3.3.1, 3.3.2, 3.3.3)
Collecting markdown>=3.0
  Created temporary directory: /tmp/pip-unpack-orpva6ue
  Getting credentials from keyring for files.pythonhosted.org
  https://files.pythonhosted.org:443 "GET /packages/ac/ef/24a91ca96efa0d7802dffb83ccc7a3c677027bea19ec3c9ee80be740408e/Markdown-3.3.3-py3-none-any.whl HTTP/1.1" 200 96264
  Downloading Markdown-3.3.3-py3-none-any.whl (96 kB)
     |████████████████████████████████| 96 kB 20.3 MB/s 
  Added markdown>=3.0 from https://files.pythonhosted.org/packages/ac/ef/24a91ca96efa0d7802dffb83ccc7a3c677027bea19ec3c9ee80be740408e/Markdown-3.3.3-py3-none-any.whl#sha256=c109c15b7dc20a9ac454c9e6025927d44460b85bd039da028d85e2b6d0bcc328 (from pdoc3) to build tracker '/tmp/pip-req-tracker-xq_mui27'
  Removed markdown>=3.0 from https://files.pythonhosted.org/packages/ac/ef/24a91ca96efa0d7802dffb83ccc7a3c677027bea19ec3c9ee80be740408e/Markdown-3.3.3-py3-none-any.whl#sha256=c109c15b7dc20a9ac454c9e6025927d44460b85bd039da028d85e2b6d0bcc328 (from pdoc3) from build tracker '/tmp/pip-req-tracker-xq_mui27'
Requirement already satisfied: MarkupSafe>=0.9.2 in /usr/lib/python3/dist-packages (from mako->pdoc3) (1.1.0)
Building wheels for collected packages: pdoc3, mako
  Created temporary directory: /tmp/pip-wheel-6jnntcjt
  Building wheel for pdoc3 (setup.py) ...   Destination directory: /tmp/pip-wheel-6jnntcjt
  Running command /usr/bin/python3 -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/tmp/pip-install-b1uccvc_/pdoc3/setup.py'"'"'; __file__='"'"'/tmp/pip-install-b1uccvc_/pdoc3/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' bdist_wheel -d /tmp/pip-wheel-6jnntcjt
  running bdist_wheel
  running build
  running build_py
  creating build
  creating build/lib
  creating build/lib/pdoc
  copying pdoc/__main__.py -> build/lib/pdoc
  copying pdoc/cli.py -> build/lib/pdoc
  copying pdoc/html_helpers.py -> build/lib/pdoc
  copying pdoc/_version.py -> build/lib/pdoc
  copying pdoc/__init__.py -> build/lib/pdoc
  creating build/lib/test_mod
  copying test_mod/a.py -> build/lib/test_mod
  copying test_mod/__init__.py -> build/lib/test_mod
  creating build/lib/pdoc/test
  copying pdoc/test/__main__.py -> build/lib/pdoc/test
  copying pdoc/test/__init__.py -> build/lib/pdoc/test
  creating build/lib/pdoc/test/example_pkg
  copying pdoc/test/example_pkg/module.py -> build/lib/pdoc/test/example_pkg
  copying pdoc/test/example_pkg/_imported_once.py -> build/lib/pdoc/test/example_pkg
  copying pdoc/test/example_pkg/__init__.py -> build/lib/pdoc/test/example_pkg
  copying pdoc/test/example_pkg/index.py -> build/lib/pdoc/test/example_pkg
  creating build/lib/pdoc/test/example_pkg/_private
  copying pdoc/test/example_pkg/_private/module.py -> build/lib/pdoc/test/example_pkg/_private
  copying pdoc/test/example_pkg/_private/_private.py -> build/lib/pdoc/test/example_pkg/_private
  copying pdoc/test/example_pkg/_private/__init__.py -> build/lib/pdoc/test/example_pkg/_private
  creating build/lib/pdoc/test/example_pkg/_test_linking
  copying pdoc/test/example_pkg/_test_linking/a.py -> build/lib/pdoc/test/example_pkg/_test_linking
  copying pdoc/test/example_pkg/_test_linking/__init__.py -> build/lib/pdoc/test/example_pkg/_test_linking
  creating build/lib/pdoc/test/example_pkg/_relative_import
  copying pdoc/test/example_pkg/_relative_import/foo.py -> build/lib/pdoc/test/example_pkg/_relative_import
  copying pdoc/test/example_pkg/_relative_import/__init__.py -> build/lib/pdoc/test/example_pkg/_relative_import
  creating build/lib/pdoc/test/example_pkg/subpkg
  copying pdoc/test/example_pkg/subpkg/_private.py -> build/lib/pdoc/test/example_pkg/subpkg
  copying pdoc/test/example_pkg/subpkg/__init__.py -> build/lib/pdoc/test/example_pkg/subpkg
  creating build/lib/pdoc/test/example_pkg/_exclude_dir
  copying pdoc/test/example_pkg/_exclude_dir/__init__.py -> build/lib/pdoc/test/example_pkg/_exclude_dir
  creating build/lib/pdoc/test/example_pkg/subpkg2
  copying pdoc/test/example_pkg/subpkg2/module.py -> build/lib/pdoc/test/example_pkg/subpkg2
  copying pdoc/test/example_pkg/subpkg2/_private.py -> build/lib/pdoc/test/example_pkg/subpkg2
  copying pdoc/test/example_pkg/subpkg2/__init__.py -> build/lib/pdoc/test/example_pkg/subpkg2
  creating build/lib/pdoc/test/example_pkg/_test_linking/b
  copying pdoc/test/example_pkg/_test_linking/b/__init__.py -> build/lib/pdoc/test/example_pkg/_test_linking/b
  copying pdoc/test/example_pkg/_test_linking/b/c.py -> build/lib/pdoc/test/example_pkg/_test_linking/b
  running egg_info
  writing pdoc3.egg-info/PKG-INFO
  writing dependency_links to pdoc3.egg-info/dependency_links.txt
  writing entry points to pdoc3.egg-info/entry_points.txt
  writing requirements to pdoc3.egg-info/requires.txt
  writing top-level names to pdoc3.egg-info/top_level.txt
  reading manifest file 'pdoc3.egg-info/SOURCES.txt'
  writing manifest file 'pdoc3.egg-info/SOURCES.txt'
  copying pdoc/documentation.md -> build/lib/pdoc
  creating build/lib/pdoc/templates
  copying pdoc/templates/_lunr_search.inc.mako -> build/lib/pdoc/templates
  copying pdoc/templates/config.mako -> build/lib/pdoc/templates
  copying pdoc/templates/credits.mako -> build/lib/pdoc/templates
  copying pdoc/templates/css.mako -> build/lib/pdoc/templates
  copying pdoc/templates/head.mako -> build/lib/pdoc/templates
  copying pdoc/templates/html.mako -> build/lib/pdoc/templates
  copying pdoc/templates/logo.mako -> build/lib/pdoc/templates
  copying pdoc/templates/pdf.mako -> build/lib/pdoc/templates
  copying pdoc/templates/search.mako -> build/lib/pdoc/templates
  copying pdoc/templates/text.mako -> build/lib/pdoc/templates
  copying pdoc/test/css.mako -> build/lib/pdoc/test
  copying pdoc/test/html.mako -> build/lib/pdoc/test
  creating build/lib/pdoc/test/example_pkg/_namespace
  creating build/lib/pdoc/test/example_pkg/_namespace/1
  creating build/lib/pdoc/test/example_pkg/_namespace/1/a
  creating build/lib/pdoc/test/example_pkg/_namespace/1/a/a
  copying pdoc/test/example_pkg/_namespace/1/a/a/util.py -> build/lib/pdoc/test/example_pkg/_namespace/1/a/a
  creating build/lib/pdoc/test/example_pkg/_namespace/1/b
  creating build/lib/pdoc/test/example_pkg/_namespace/1/b/a
  copying pdoc/test/example_pkg/_namespace/1/b/a/main.py -> build/lib/pdoc/test/example_pkg/_namespace/1/b/a
  creating build/lib/pdoc/test/example_pkg/_namespace/2
  creating build/lib/pdoc/test/example_pkg/_namespace/2/a
  creating build/lib/pdoc/test/example_pkg/_namespace/2/a/a
  copying pdoc/test/example_pkg/_namespace/2/a/a/__init__.py -> build/lib/pdoc/test/example_pkg/_namespace/2/a/a
  copying pdoc/test/example_pkg/_namespace/2/a/a/util.py -> build/lib/pdoc/test/example_pkg/_namespace/2/a/a
  creating build/lib/pdoc/test/example_pkg/_namespace/2/b
  creating build/lib/pdoc/test/example_pkg/_namespace/2/b/a
  copying pdoc/test/example_pkg/_namespace/2/b/a/__init__.py -> build/lib/pdoc/test/example_pkg/_namespace/2/b/a
  copying pdoc/test/example_pkg/_namespace/2/b/a/main.py -> build/lib/pdoc/test/example_pkg/_namespace/2/b/a
  creating build/lib/pdoc/test/example_pkg/_namespace/3
  creating build/lib/pdoc/test/example_pkg/_namespace/3/a
  creating build/lib/pdoc/test/example_pkg/_namespace/3/a/a
  copying pdoc/test/example_pkg/_namespace/3/a/a/__init__.py -> build/lib/pdoc/test/example_pkg/_namespace/3/a/a
  copying pdoc/test/example_pkg/_namespace/3/a/a/util.py -> build/lib/pdoc/test/example_pkg/_namespace/3/a/a
  creating build/lib/pdoc/test/example_pkg/_namespace/3/b
  creating build/lib/pdoc/test/example_pkg/_namespace/3/b/a
  copying pdoc/test/example_pkg/_namespace/3/b/a/__init__.py -> build/lib/pdoc/test/example_pkg/_namespace/3/b/a
  copying pdoc/test/example_pkg/_namespace/3/b/a/main.py -> build/lib/pdoc/test/example_pkg/_namespace/3/b/a
  creating build/lib/pdoc/test/example_pkg/_reST_include
  copying pdoc/test/example_pkg/_reST_include/_include_me.py -> build/lib/pdoc/test/example_pkg/_reST_include
  copying pdoc/test/example_pkg/_reST_include/test.py -> build/lib/pdoc/test/example_pkg/_reST_include
  creating build/lib/pdoc/test/example_pkg/_resolve_typing_forwardrefs
  copying pdoc/test/example_pkg/_resolve_typing_forwardrefs/evaluated.py -> build/lib/pdoc/test/example_pkg/_resolve_typing_forwardrefs
  copying pdoc/test/example_pkg/_resolve_typing_forwardrefs/postponed.py -> build/lib/pdoc/test/example_pkg/_resolve_typing_forwardrefs
  creating build/lib/pdoc/test/example_pkg/_skip_errors
  copying pdoc/test/example_pkg/_skip_errors/unimportable.py -> build/lib/pdoc/test/example_pkg/_skip_errors
  creating build/lib/pdoc/test/example_pkg/_exclude_dir/downloaded_modules
  copying pdoc/test/example_pkg/_exclude_dir/downloaded_modules/foo.py -> build/lib/pdoc/test/example_pkg/_exclude_dir/downloaded_modules
  installing to build/bdist.linux-x86_64/wheel
  running install
  running install_lib
  creating build/bdist.linux-x86_64
  creating build/bdist.linux-x86_64/wheel
  creating build/bdist.linux-x86_64/wheel/pdoc
  copying build/lib/pdoc/__main__.py -> build/bdist.linux-x86_64/wheel/pdoc
  creating build/bdist.linux-x86_64/wheel/pdoc/templates
  copying build/lib/pdoc/templates/css.mako -> build/bdist.linux-x86_64/wheel/pdoc/templates
  copying build/lib/pdoc/templates/head.mako -> build/bdist.linux-x86_64/wheel/pdoc/templates
  copying build/lib/pdoc/templates/credits.mako -> build/bdist.linux-x86_64/wheel/pdoc/templates
  copying build/lib/pdoc/templates/_lunr_search.inc.mako -> build/bdist.linux-x86_64/wheel/pdoc/templates
  copying build/lib/pdoc/templates/search.mako -> build/bdist.linux-x86_64/wheel/pdoc/templates
  copying build/lib/pdoc/templates/text.mako -> build/bdist.linux-x86_64/wheel/pdoc/templates
  copying build/lib/pdoc/templates/pdf.mako -> build/bdist.linux-x86_64/wheel/pdoc/templates
  copying build/lib/pdoc/templates/config.mako -> build/bdist.linux-x86_64/wheel/pdoc/templates
  copying build/lib/pdoc/templates/logo.mako -> build/bdist.linux-x86_64/wheel/pdoc/templates
  copying build/lib/pdoc/templates/html.mako -> build/bdist.linux-x86_64/wheel/pdoc/templates
  copying build/lib/pdoc/cli.py -> build/bdist.linux-x86_64/wheel/pdoc
  copying build/lib/pdoc/html_helpers.py -> build/bdist.linux-x86_64/wheel/pdoc
  copying build/lib/pdoc/documentation.md -> build/bdist.linux-x86_64/wheel/pdoc
  copying build/lib/pdoc/_version.py -> build/bdist.linux-x86_64/wheel/pdoc
  creating build/bdist.linux-x86_64/wheel/pdoc/test
  copying build/lib/pdoc/test/css.mako -> build/bdist.linux-x86_64/wheel/pdoc/test
  copying build/lib/pdoc/test/__main__.py -> build/bdist.linux-x86_64/wheel/pdoc/test
  creating build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg
  creating build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_private
  copying build/lib/pdoc/test/example_pkg/_private/module.py -> build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_private
  copying build/lib/pdoc/test/example_pkg/_private/_private.py -> build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_private
  copying build/lib/pdoc/test/example_pkg/_private/__init__.py -> build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_private
  copying build/lib/pdoc/test/example_pkg/module.py -> build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg
  copying build/lib/pdoc/test/example_pkg/_imported_once.py -> build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg
  creating build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_resolve_typing_forwardrefs
  copying build/lib/pdoc/test/example_pkg/_resolve_typing_forwardrefs/postponed.py -> build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_resolve_typing_forwardrefs
  copying build/lib/pdoc/test/example_pkg/_resolve_typing_forwardrefs/evaluated.py -> build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_resolve_typing_forwardrefs
  creating build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_test_linking
  copying build/lib/pdoc/test/example_pkg/_test_linking/a.py -> build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_test_linking
  creating build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_test_linking/b
  copying build/lib/pdoc/test/example_pkg/_test_linking/b/__init__.py -> build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_test_linking/b
  copying build/lib/pdoc/test/example_pkg/_test_linking/b/c.py -> build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_test_linking/b
  copying build/lib/pdoc/test/example_pkg/_test_linking/__init__.py -> build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_test_linking
  creating build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_reST_include
  copying build/lib/pdoc/test/example_pkg/_reST_include/test.py -> build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_reST_include
  copying build/lib/pdoc/test/example_pkg/_reST_include/_include_me.py -> build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_reST_include
  creating build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_namespace
  creating build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_namespace/2
  creating build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_namespace/2/a
  creating build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_namespace/2/a/a
  copying build/lib/pdoc/test/example_pkg/_namespace/2/a/a/util.py -> build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_namespace/2/a/a
  copying build/lib/pdoc/test/example_pkg/_namespace/2/a/a/__init__.py -> build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_namespace/2/a/a
  creating build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_namespace/2/b
  creating build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_namespace/2/b/a
  copying build/lib/pdoc/test/example_pkg/_namespace/2/b/a/main.py -> build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_namespace/2/b/a
  copying build/lib/pdoc/test/example_pkg/_namespace/2/b/a/__init__.py -> build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_namespace/2/b/a
  creating build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_namespace/1
  creating build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_namespace/1/a
  creating build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_namespace/1/a/a
  copying build/lib/pdoc/test/example_pkg/_namespace/1/a/a/util.py -> build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_namespace/1/a/a
  creating build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_namespace/1/b
  creating build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_namespace/1/b/a
  copying build/lib/pdoc/test/example_pkg/_namespace/1/b/a/main.py -> build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_namespace/1/b/a
  creating build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_namespace/3
  creating build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_namespace/3/a
  creating build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_namespace/3/a/a
  copying build/lib/pdoc/test/example_pkg/_namespace/3/a/a/util.py -> build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_namespace/3/a/a
  copying build/lib/pdoc/test/example_pkg/_namespace/3/a/a/__init__.py -> build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_namespace/3/a/a
  creating build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_namespace/3/b
  creating build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_namespace/3/b/a
  copying build/lib/pdoc/test/example_pkg/_namespace/3/b/a/main.py -> build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_namespace/3/b/a
  copying build/lib/pdoc/test/example_pkg/_namespace/3/b/a/__init__.py -> build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_namespace/3/b/a
  creating build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_relative_import
  copying build/lib/pdoc/test/example_pkg/_relative_import/foo.py -> build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_relative_import
  copying build/lib/pdoc/test/example_pkg/_relative_import/__init__.py -> build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_relative_import
  creating build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/subpkg
  copying build/lib/pdoc/test/example_pkg/subpkg/_private.py -> build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/subpkg
  copying build/lib/pdoc/test/example_pkg/subpkg/__init__.py -> build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/subpkg
  creating build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_skip_errors
  copying build/lib/pdoc/test/example_pkg/_skip_errors/unimportable.py -> build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_skip_errors
  creating build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_exclude_dir
  creating build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_exclude_dir/downloaded_modules
  copying build/lib/pdoc/test/example_pkg/_exclude_dir/downloaded_modules/foo.py -> build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_exclude_dir/downloaded_modules
  copying build/lib/pdoc/test/example_pkg/_exclude_dir/__init__.py -> build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/_exclude_dir
  copying build/lib/pdoc/test/example_pkg/__init__.py -> build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg
  copying build/lib/pdoc/test/example_pkg/index.py -> build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg
  creating build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/subpkg2
  copying build/lib/pdoc/test/example_pkg/subpkg2/module.py -> build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/subpkg2
  copying build/lib/pdoc/test/example_pkg/subpkg2/_private.py -> build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/subpkg2
  copying build/lib/pdoc/test/example_pkg/subpkg2/__init__.py -> build/bdist.linux-x86_64/wheel/pdoc/test/example_pkg/subpkg2
  copying build/lib/pdoc/test/__init__.py -> build/bdist.linux-x86_64/wheel/pdoc/test
  copying build/lib/pdoc/test/html.mako -> build/bdist.linux-x86_64/wheel/pdoc/test
  copying build/lib/pdoc/__init__.py -> build/bdist.linux-x86_64/wheel/pdoc
  creating build/bdist.linux-x86_64/wheel/test_mod
  copying build/lib/test_mod/a.py -> build/bdist.linux-x86_64/wheel/test_mod
  copying build/lib/test_mod/__init__.py -> build/bdist.linux-x86_64/wheel/test_mod
  running install_egg_info
  Copying pdoc3.egg-info to build/bdist.linux-x86_64/wheel/pdoc3-0.9.2.egg-info
  running install_scripts
  adding license file "LICENSE.txt" (matched pattern "LICEN[CS]E*")
  creating build/bdist.linux-x86_64/wheel/pdoc3-0.9.2.dist-info/WHEEL
  creating '/tmp/pip-wheel-6jnntcjt/pdoc3-0.9.2-py3-none-any.whl' and adding 'build/bdist.linux-x86_64/wheel' to it
  adding 'pdoc/__init__.py'
  adding 'pdoc/__main__.py'
  adding 'pdoc/_version.py'
  adding 'pdoc/cli.py'
  adding 'pdoc/documentation.md'
  adding 'pdoc/html_helpers.py'
  adding 'pdoc/templates/_lunr_search.inc.mako'
  adding 'pdoc/templates/config.mako'
  adding 'pdoc/templates/credits.mako'
  adding 'pdoc/templates/css.mako'
  adding 'pdoc/templates/head.mako'
  adding 'pdoc/templates/html.mako'
  adding 'pdoc/templates/logo.mako'
  adding 'pdoc/templates/pdf.mako'
  adding 'pdoc/templates/search.mako'
  adding 'pdoc/templates/text.mako'
  adding 'pdoc/test/__init__.py'
  adding 'pdoc/test/__main__.py'
  adding 'pdoc/test/css.mako'
  adding 'pdoc/test/html.mako'
  adding 'pdoc/test/example_pkg/__init__.py'
  adding 'pdoc/test/example_pkg/_imported_once.py'
  adding 'pdoc/test/example_pkg/index.py'
  adding 'pdoc/test/example_pkg/module.py'
  adding 'pdoc/test/example_pkg/_exclude_dir/__init__.py'
  adding 'pdoc/test/example_pkg/_exclude_dir/downloaded_modules/foo.py'
  adding 'pdoc/test/example_pkg/_namespace/1/a/a/util.py'
  adding 'pdoc/test/example_pkg/_namespace/1/b/a/main.py'
  adding 'pdoc/test/example_pkg/_namespace/2/a/a/__init__.py'
  adding 'pdoc/test/example_pkg/_namespace/2/a/a/util.py'
  adding 'pdoc/test/example_pkg/_namespace/2/b/a/__init__.py'
  adding 'pdoc/test/example_pkg/_namespace/2/b/a/main.py'
  adding 'pdoc/test/example_pkg/_namespace/3/a/a/__init__.py'
  adding 'pdoc/test/example_pkg/_namespace/3/a/a/util.py'
  adding 'pdoc/test/example_pkg/_namespace/3/b/a/__init__.py'
  adding 'pdoc/test/example_pkg/_namespace/3/b/a/main.py'
  adding 'pdoc/test/example_pkg/_private/__init__.py'
  adding 'pdoc/test/example_pkg/_private/_private.py'
  adding 'pdoc/test/example_pkg/_private/module.py'
  adding 'pdoc/test/example_pkg/_reST_include/_include_me.py'
  adding 'pdoc/test/example_pkg/_reST_include/test.py'
  adding 'pdoc/test/example_pkg/_relative_import/__init__.py'
  adding 'pdoc/test/example_pkg/_relative_import/foo.py'
  adding 'pdoc/test/example_pkg/_resolve_typing_forwardrefs/evaluated.py'
  adding 'pdoc/test/example_pkg/_resolve_typing_forwardrefs/postponed.py'
  adding 'pdoc/test/example_pkg/_skip_errors/unimportable.py'
  adding 'pdoc/test/example_pkg/_test_linking/__init__.py'
  adding 'pdoc/test/example_pkg/_test_linking/a.py'
  adding 'pdoc/test/example_pkg/_test_linking/b/__init__.py'
  adding 'pdoc/test/example_pkg/_test_linking/b/c.py'
  adding 'pdoc/test/example_pkg/subpkg/__init__.py'
  adding 'pdoc/test/example_pkg/subpkg/_private.py'
  adding 'pdoc/test/example_pkg/subpkg2/__init__.py'
  adding 'pdoc/test/example_pkg/subpkg2/_private.py'
  adding 'pdoc/test/example_pkg/subpkg2/module.py'
  adding 'test_mod/__init__.py'
  adding 'test_mod/a.py'
  adding 'pdoc3-0.9.2.dist-info/LICENSE.txt'
  adding 'pdoc3-0.9.2.dist-info/METADATA'
  adding 'pdoc3-0.9.2.dist-info/WHEEL'
  adding 'pdoc3-0.9.2.dist-info/entry_points.txt'
  adding 'pdoc3-0.9.2.dist-info/top_level.txt'
  adding 'pdoc3-0.9.2.dist-info/RECORD'
  removing build/bdist.linux-x86_64/wheel
done
  Created wheel for pdoc3: filename=pdoc3-0.9.2-py3-none-any.whl size=117470 sha256=090be8257d5236c1b227670d2839f13d5bff55f901587edd4c03ca1f9e1b37e3
  Stored in directory: /tmp/pip-ephem-wheel-cache-eoq2o_b3/wheels/05/b5/f5/b9ed25253e8561519df747837e12558248b34ba732f2cc05f9
  Created temporary directory: /tmp/pip-wheel-zn8nv_od
  Building wheel for mako (setup.py) ...   Destination directory: /tmp/pip-wheel-zn8nv_od
  Running command /usr/bin/python3 -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/tmp/pip-install-b1uccvc_/mako/setup.py'"'"'; __file__='"'"'/tmp/pip-install-b1uccvc_/mako/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' bdist_wheel -d /tmp/pip-wheel-zn8nv_od
  running bdist_wheel
  running build
  running build_py
  creating build
  creating build/lib
  creating build/lib/mako
  copying mako/template.py -> build/lib/mako
  copying mako/exceptions.py -> build/lib/mako
  copying mako/cache.py -> build/lib/mako
  copying mako/lexer.py -> build/lib/mako
  copying mako/codegen.py -> build/lib/mako
  copying mako/runtime.py -> build/lib/mako
  copying mako/ast.py -> build/lib/mako
  copying mako/lookup.py -> build/lib/mako
  copying mako/util.py -> build/lib/mako
  copying mako/pygen.py -> build/lib/mako
  copying mako/parsetree.py -> build/lib/mako
  copying mako/cmd.py -> build/lib/mako
  copying mako/_ast_util.py -> build/lib/mako
  copying mako/__init__.py -> build/lib/mako
  copying mako/compat.py -> build/lib/mako
  copying mako/pyparser.py -> build/lib/mako
  copying mako/filters.py -> build/lib/mako
  creating build/lib/mako/ext
  copying mako/ext/babelplugin.py -> build/lib/mako/ext
  copying mako/ext/extract.py -> build/lib/mako/ext
  copying mako/ext/turbogears.py -> build/lib/mako/ext
  copying mako/ext/pygmentplugin.py -> build/lib/mako/ext
  copying mako/ext/linguaplugin.py -> build/lib/mako/ext
  copying mako/ext/autohandler.py -> build/lib/mako/ext
  copying mako/ext/beaker_cache.py -> build/lib/mako/ext
  copying mako/ext/preprocessors.py -> build/lib/mako/ext
  copying mako/ext/__init__.py -> build/lib/mako/ext
  installing to build/bdist.linux-x86_64/wheel
  running install
  running install_lib
  creating build/bdist.linux-x86_64
  creating build/bdist.linux-x86_64/wheel
  creating build/bdist.linux-x86_64/wheel/mako
  creating build/bdist.linux-x86_64/wheel/mako/ext
  copying build/lib/mako/ext/babelplugin.py -> build/bdist.linux-x86_64/wheel/mako/ext
  copying build/lib/mako/ext/extract.py -> build/bdist.linux-x86_64/wheel/mako/ext
  copying build/lib/mako/ext/turbogears.py -> build/bdist.linux-x86_64/wheel/mako/ext
  copying build/lib/mako/ext/pygmentplugin.py -> build/bdist.linux-x86_64/wheel/mako/ext
  copying build/lib/mako/ext/linguaplugin.py -> build/bdist.linux-x86_64/wheel/mako/ext
  copying build/lib/mako/ext/autohandler.py -> build/bdist.linux-x86_64/wheel/mako/ext
  copying build/lib/mako/ext/beaker_cache.py -> build/bdist.linux-x86_64/wheel/mako/ext
  copying build/lib/mako/ext/preprocessors.py -> build/bdist.linux-x86_64/wheel/mako/ext
  copying build/lib/mako/ext/__init__.py -> build/bdist.linux-x86_64/wheel/mako/ext
  copying build/lib/mako/template.py -> build/bdist.linux-x86_64/wheel/mako
  copying build/lib/mako/exceptions.py -> build/bdist.linux-x86_64/wheel/mako
  copying build/lib/mako/cache.py -> build/bdist.linux-x86_64/wheel/mako
  copying build/lib/mako/lexer.py -> build/bdist.linux-x86_64/wheel/mako
  copying build/lib/mako/codegen.py -> build/bdist.linux-x86_64/wheel/mako
  copying build/lib/mako/runtime.py -> build/bdist.linux-x86_64/wheel/mako
  copying build/lib/mako/ast.py -> build/bdist.linux-x86_64/wheel/mako
  copying build/lib/mako/lookup.py -> build/bdist.linux-x86_64/wheel/mako
  copying build/lib/mako/util.py -> build/bdist.linux-x86_64/wheel/mako
  copying build/lib/mako/pygen.py -> build/bdist.linux-x86_64/wheel/mako
  copying build/lib/mako/parsetree.py -> build/bdist.linux-x86_64/wheel/mako
  copying build/lib/mako/cmd.py -> build/bdist.linux-x86_64/wheel/mako
  copying build/lib/mako/_ast_util.py -> build/bdist.linux-x86_64/wheel/mako
  copying build/lib/mako/__init__.py -> build/bdist.linux-x86_64/wheel/mako
  copying build/lib/mako/compat.py -> build/bdist.linux-x86_64/wheel/mako
  copying build/lib/mako/pyparser.py -> build/bdist.linux-x86_64/wheel/mako
  copying build/lib/mako/filters.py -> build/bdist.linux-x86_64/wheel/mako
  running install_egg_info
  running egg_info
  writing Mako.egg-info/PKG-INFO
  writing dependency_links to Mako.egg-info/dependency_links.txt
  writing entry points to Mako.egg-info/entry_points.txt
  writing requirements to Mako.egg-info/requires.txt
  writing top-level names to Mako.egg-info/top_level.txt
  reading manifest file 'Mako.egg-info/SOURCES.txt'
  reading manifest template 'MANIFEST.in'
  warning: no files found matching '*.mako' under directory 'doc'
  warning: no files found matching '*.xml' under directory 'examples'
  warning: no files found matching '*.mako' under directory 'examples'
  no previously-included directories found matching 'doc/build/output'
  writing manifest file 'Mako.egg-info/SOURCES.txt'
  Copying Mako.egg-info to build/bdist.linux-x86_64/wheel/Mako-1.1.4.egg-info
  running install_scripts
  adding license file "LICENSE" (matched pattern "LICEN[CS]E*")
  adding license file "AUTHORS" (matched pattern "AUTHORS*")
  creating build/bdist.linux-x86_64/wheel/Mako-1.1.4.dist-info/WHEEL
  creating '/tmp/pip-wheel-zn8nv_od/Mako-1.1.4-py2.py3-none-any.whl' and adding 'build/bdist.linux-x86_64/wheel' to it
  adding 'mako/__init__.py'
  adding 'mako/_ast_util.py'
  adding 'mako/ast.py'
  adding 'mako/cache.py'
  adding 'mako/cmd.py'
  adding 'mako/codegen.py'
  adding 'mako/compat.py'
  adding 'mako/exceptions.py'
  adding 'mako/filters.py'
  adding 'mako/lexer.py'
  adding 'mako/lookup.py'
  adding 'mako/parsetree.py'
  adding 'mako/pygen.py'
  adding 'mako/pyparser.py'
  adding 'mako/runtime.py'
  adding 'mako/template.py'
  adding 'mako/util.py'
  adding 'mako/ext/__init__.py'
  adding 'mako/ext/autohandler.py'
  adding 'mako/ext/babelplugin.py'
  adding 'mako/ext/beaker_cache.py'
  adding 'mako/ext/extract.py'
  adding 'mako/ext/linguaplugin.py'
  adding 'mako/ext/preprocessors.py'
  adding 'mako/ext/pygmentplugin.py'
  adding 'mako/ext/turbogears.py'
  adding 'Mako-1.1.4.dist-info/AUTHORS'
  adding 'Mako-1.1.4.dist-info/LICENSE'
  adding 'Mako-1.1.4.dist-info/METADATA'
  adding 'Mako-1.1.4.dist-info/WHEEL'
  adding 'Mako-1.1.4.dist-info/entry_points.txt'
  adding 'Mako-1.1.4.dist-info/top_level.txt'
  adding 'Mako-1.1.4.dist-info/RECORD'
  removing build/bdist.linux-x86_64/wheel
done
  Created wheel for mako: filename=Mako-1.1.4-py2.py3-none-any.whl size=75675 sha256=99136cb05a5361b9064e7cdecdf642ae3939bd29fd74930fdfe162cbbc2f4c7d
  Stored in directory: /tmp/pip-ephem-wheel-cache-eoq2o_b3/wheels/17/bc/50/621fe4100d907a7296cc00c21371402b068b648820f6ff5812
Successfully built pdoc3 mako
Installing collected packages: mako, markdown, pdoc3
  Created temporary directory: /tmp/pip-unpacked-wheel-1ipbj_l2

  changing mode of /home/kvogel/.local/bin/mako-render to 755
  WARNING: The script mako-render is installed in '/home/kvogel/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  Created temporary directory: /tmp/pip-unpacked-wheel-5ft9shp1

  changing mode of /home/kvogel/.local/bin/markdown_py to 755
  WARNING: The script markdown_py is installed in '/home/kvogel/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  Created temporary directory: /tmp/pip-unpacked-wheel-scxo8vve

  changing mode of /home/kvogel/.local/bin/pdoc to 755
  changing mode of /home/kvogel/.local/bin/pdoc3 to 755
  WARNING: The scripts pdoc and pdoc3 are installed in '/home/kvogel/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed mako-1.1.4 markdown-3.3.3 pdoc3-0.9.2
Cleaning up...
  Removing source in /tmp/pip-install-b1uccvc_/pdoc3
  Removing source in /tmp/pip-install-b1uccvc_/mako
Removed build tracker: '/tmp/pip-req-tracker-xq_mui27'
21/02/1 14:27:46 kvogel-elitebook:~/projects/primrose ±(master) ✗ 
❯ 
```
