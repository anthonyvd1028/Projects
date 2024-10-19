# Mind Your Surroundings

> Anthony DiTaranto | 10/18/2024

## Description

There’s a flag that has eluded us on deephax’s machine. We’ve looked through various files but can’t seem to locate it. See if you can characterize the machine and find the flag.

## Additional Info 

**From Landing Zone**
Connection Info:
Host: deephax@deephax.deadface.io
Username: deephax
Password: D34df4c32024$

## Solution

This challenge involves having access to Deephax's machine, which we accessed through ssh. More details about how I entered [here](https://github.com/anthonyvd1028/Projects/blob/main/CTF/Deadface_2024/Forensics/Mind_Your_Surroundings/README.md).

From the description, it seems that the flag won't be found in a file, whether it is hidden or not. Now where else can information be stored if it isn't a file? The answer is environment variables, which plays off the title as it mentions surroundings.

To view these environment variables, you can enter the command `printenv` or `export`. Both show the variable `flag3=flag{hostbusters3_ff07d6fb5ee992f6}`.

## Flag

`flag{hostbusters3_ff07d6fb5ee992f6}`
