# SSBT

SSBT (Super Simple Backup Tool) is a CLI based script that helps you make automated local backups of some directories or files at a given interval.

## Requirement

You must have Python 3 installed on your system.

## Usage

```
python ssbt.py --src [paths to make a backup of] --dest [where to save your backups] --minutes [number of minutes]
```

## Arguments

- --src: specify the absolute paths of the directories or files to backup.
- --dest: specify the absolute path of the directory where the backups are going to be saved.
- --minutes: specify the interval of the backups in minutes. It has to be a positive integer.
- --seconds: specify the interval of the backups in seconds. It has to be a positive integer.

> Only --minutes or --seconds can be specified at the same time.
