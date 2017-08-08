Excavate -- Dig to understand disk usage over time
==================================================

Use::

    pip3 install --user excavate

to install. Executable is placed in ~/.local/bin.


Synopsis
--------

*Excavate* is a very simple command line utility used to understand how disk 
usage in a particular part of the file system has changed over time. It lists 
out the all of the files contained in a particular directory and its 
subdirectories while sorting them according to when they last changed, from 
youngest to oldest.  When listing the files it also gives their size and the 
accumulated disk space need to hold the file and all younger files.
Files in the top three deciles in size are colored red, pink, and yellow 
respectively.

  | Usage: excavate [options] [<path>...]
  |
  | Options:
  |     -d, --date  give modification date rather than description of age
  |     -s, --size  sort by size rather than by age
  |     -w, --warn  warn of inaccessible files


Normally the output would be piped into more (or less). For example::

    > excavate /etc | less
    MODIFIED             SIZE     ACCUM    FILE
    just now             0 B      0 B      /etc/mtab
    6 hours ago          76.3 kB  76.3 kB  /etc/ld.so.cache
    6 hours ago          106 B    76.4 kB  /etc/selinux/targeted/seusers
    6 hours ago          3.7 MB   3.78 MB  /etc/selinux/targeted/policy/policy.30
    6 hours ago          13.2 kB  3.79 MB  /etc/selinux/targeted/contexts/files/file_contexts.homedirs
    6 hours ago          44.7 kB  3.84 MB  /etc/selinux/targeted/contexts/files/file_contexts.homedirs.bin
    6 hours ago          1.39 MB  5.23 MB  /etc/selinux/targeted/contexts/files/file_contexts.bin
    6 hours ago          379 kB   5.61 MB  /etc/selinux/targeted/contexts/files/file_contexts
    2 days ago           9 B      5.61 MB  /etc/tuned/active_profile
    2 days ago           656 B    5.61 MB  /etc/vmware/config
    3 days ago           15.3 kB  5.63 MB  /etc/cron.daily/google-chrome-beta
    3 days ago           2.25 kB  5.63 MB  /etc/alternatives/google-chrome
    3 days ago           33 B     5.63 MB  /etc/vmware/usbarb.rules
    4 days ago           2.82 kB  5.63 MB  /etc/localtime
    4 days ago           129 B    5.63 MB  /etc/selinux/targeted/.policy.sha512
    4 days ago           607 B    5.63 MB  /etc/selinux/targeted/setrans.conf
    4 days ago           2.62 kB  5.64 MB  /etc/selinux/targeted/booleans.subs_dist
    4 days ago           74 B     5.64 MB  /etc/selinux/targeted/contexts/securetty_types
    4 days ago           245 B    5.64 MB  /etc/selinux/targeted/contexts/customizable_types
    4 days ago           422 B    5.64 MB  /etc/selinux/targeted/contexts/files/file_contexts.subs_dist
    4 days ago           0 B      5.64 MB  /etc/selinux/targeted/contexts/files/file_contexts.subs
    4 days ago           0 B      5.64 MB  /etc/selinux/targeted/semanage.trans.LOCK
    4 days ago           0 B      5.64 MB  /etc/selinux/targeted/semanage.read.LOCK
    4 days ago           30 B     5.64 MB  /etc/selinux/targeted/contexts/initrc_context
    4 days ago           254 B    5.64 MB  /etc/selinux/targeted/contexts/default_contexts
    ...
