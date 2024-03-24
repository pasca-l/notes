# Amazon Linux Cheat Sheet <!-- omit in toc -->

## Table of Content <!-- omit in toc -->
- [Extending Linux file system after resizing volume](#extending-linux-file-system-after-resizing-volume)

## [Extending Linux file system after resizing volume](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/recognize-expanded-volume-linux.html)
After increasing the size of Amazon EBS (Elastic Block Store), the file system needs to be extended to use the volume.

1. Check disk space and block device list.
- `nvme0n1` is the root volume with 2 partitions, and `nvme1n1` is the added volume.
    > Partition names are that of a Nitro instance, which is build on the AWS Nitro System, a collection of hardware and software components built by AWS that enable high performance, availability and security.

```bash
$ df -hT
```
```
Filesystem      Type  Size  Used Avail Use% Mounted on
/dev/nvme0n1p1  xfs   8.0G  1.6G  6.5G  20% /
/dev/nvme1n1    xfs   8.0G   33M  8.0G   1% /data
...
```

```bash
$ sudo lsblk
```
```
NAME          MAJ:MIN RM SIZE RO TYPE MOUNTPOINT
nvme0n1       259:1    0  16G  0 disk
└─nvme0n1p1   259:2    0   8G  0 part /
└─nvme0n1p128 259:3    0   1M  0 part
nvme1n1       259:0    0  30G  0 disk /data
```

2. Extend the partition using `growpart` command.
```bash
# growpart DEVICE_NAME PARTITION_NUM
$ sudo growpart /dev/nvme0n1 1
```
```
$ sudo lsblk
NAME          MAJ:MIN RM SIZE RO TYPE MOUNTPOINT
nvme0n1       259:1    0  16G  0 disk
└─nvme0n1p1   259:2    0  16G  0 part /         <- expanded 
└─nvme0n1p128 259:3    0   1M  0 part
nvme1n1       259:0    0  30G  0 disk /data
```
