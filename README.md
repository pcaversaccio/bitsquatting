# Bitsquatting the Ethereum Name Service (ENS) Domain Names
The helper script [`bitsquatting.py`](https://github.com/pcaversaccio/bitsquatting/blob/main/bitsquatting.py) generates (lowercase) permutations of an ENS domain that differ by 1-bit from the original domain.

## What Is Bitsquatting
> I borrowed this explanation from [here](https://github.com/benjaminpetrin-zz/bitsquatting).

Bitsquatting is _DNS Hijacking without exploitation_. A term coined by [Artem Dinaburg](https://web.archive.org/web/20180713212603/http://media.blackhat.com/bh-us-11/Dinaburg/BH_US_11_Dinaburg_Bitsquatting_WP.pdf) to refer to the act of registering domains that are 1-bit off from some other legitimate domain in order to capture traffic that was destined for the legitimate domain but became corrupted and ended up on the alternate domain.

Bitsquatting is due to an error on the part of the connecting client machine and not anything the operator of a domain can explicitly protect against except by purchasing additional domains. The more popular a website is, the more likely a connecting client may accidentally connect to some other domain on accident.

This is due to corruption in memory (or potentially transmission) and it is distinct from a typo made by a user (and therefor different from the more well-known practice of typosquatting). A good candidate domain name for bitsquatting is one that is both popular and not one visited by a user explicitly (that is, a domain that is not commonly navigated to in a web browser by a user). For example, `facebook.com` would not be a good candidate but `fbcdn.net` would be as it is the domain Facebook uses to host static resources that are embedded on `facebook.com`.

## Example `wagmi.eth`
*Original ENS Name:* `wagmi.eth`

*1-Bit Permutations:*
- 7agmi.eth
- wagmi.eth
- gagmi.eth
- agmi.eth
- sagmi.eth
- uagmi.eth
- vagmi.eth
- w!gmi.eth
- wagmi.eth
- wqgmi.eth
- wigmi.eth
- wegmi.eth
- wcgmi.eth
- w`gmi.eth
- wa'mi.eth
- wagmi.eth
- wawmi.eth
- waomi.eth
- wacmi.eth
- waemi.eth
- wafmi.eth
- wag-i.eth
- wagmi.eth
- wag}i.eth
- wagei.eth
- wagii.eth
- wagoi.eth
- wagli.eth
- wagm).eth
- wagmi.eth
- wagmy.eth
- wagma.eth
- wagmm.eth
- wagmk.eth
- wagmh.eth

## Potential Attack Vector
The attacker could bitsquat popular `ens` domains, register them, and could receive a very small portion of the transactions meant for someone else.

## Reference
- https://web.archive.org/web/20180713212603/http://media.blackhat.com/bh-us-11/Dinaburg/BH_US_11_Dinaburg_Bitsquatting_WP.pdf
- https://github.com/benjaminpetrin-zz/bitsquatting
