# Phase One

> Anthony DiTaranto | 9/21/2024

## Description

We had one of our agents infiltrate an adversary's lab and photograph a gateway device that can get us access to their network. We need to develop an exploit as soon as possible. Attached is a picture of the device. Get us intel on what MCU the device is utilizing so we can continue with our research.

## target_product.jpg

![target_product.jpg](/Images/target_product.jpg)

## Solution

To find the flag, you need to wrap pctf{} around the MCU of the given gateway device. 

My next step was to do a boolean search to find all results with "MCU" and "DSL-6300v".

I google searched `"DSL-6300v" AND "MCU"`

After searching through the results, I found a [wiki page](https://deviwiki.com/wiki/D-Link_DSL-6300V) for the D-Link Modem which also included the CPU1, which was Ikanos



## Flag
`pctf{Ikanos}`
