# Big Fish

> Anthony DiTaranto | 10/18/2024

## Description

TGRI employee Garry Sartoris fell for a phishing attack recently. It’s hard to say what DEADFACE was after, but Turbo Tactical needs your help looking through the attack artifacts. Take a look at this PCAP and submit the attacker’s IP address.

## Solution

From the description, I see that Garry Sartoris fell for a phishing attack, and we need to figure out the IP address of the attacker. I downloaded the .pcap file and opened it with wireshark. Phishing mainly happens through a victim receiving an email and clicking the link or downloading the attachment. Once this is done, the attacker may carry out their plan, whether it be downloading malware or other attacking techniques.

Therefore, I used a filter in wireshark to only show HTTP traffic. I was left with 4 packets, starting with packet number 13,000. I looked at packet number 13,000 because the info shows it is a POST request, which means that Garry is sending some sort of data.

Once I clicked on the packet, I expanded the Hypertext Transfer Protocol tab, which shows it was a POST request to `http://techg1obalresearch.com/notice.html`. I expanded the HTML Form tab and saw `username = "garry.sartoris@techglobalresearch.com"` and `password = S4rt0RIS19&&`.

Now I see that Garry sent what looks like his login information for techglobalresearch to a website that is typosquatting the legitimate website. That means the IP address of the attacker is the IP address under the destination column.

## Flag

`flag{45.55.201.188}`
