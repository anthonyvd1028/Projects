# How to set up the Downloads folder cleaner on Windows

> Anthony DiTaranto | 9/19/2024

## Description

This Bash script removes all files older than two weeks in the Downloads folder

## Script

[DownloadCleaner.sh](https://github.com/anthonyvd1028/Projects/blob/main/Projects/DownloadCleaner/DownloadCleaner.sh)

## Instructions
1. Press the Windows button 
2. Open Task Scheduler
3. Select the "Action" menu and then select "Create Basic Task"
4. Give the task a name
5. Give the task a description(Optional)
6. Select Next
7. Select daily
8. Select the day and time you want it to start and hit next
9. Leave it on "start a program" and hit next
10. In "Program/script:" enter the path your Bash executable
11. In "Add arguments(optional):" enter the path to your Bash script
12. Hit next
13. Hit finish