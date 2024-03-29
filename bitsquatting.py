domain = "wagmi"
tld = ".eth"

bin_repr = bin(int.from_bytes(domain.encode(), 'big')) #Big-endianness
bin_repr = bin_repr[2:]

for index, bit in enumerate(bin_repr):
    bit = '0' if bit == '1' else '1'
    new_bin_repr = bin_repr[:index] + bit + bin_repr[index + 1:]
    new_bin_repr = f'0b{new_bin_repr}'

    n = int(new_bin_repr, 2)
    try:
        new_domain = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
        print(new_domain.lower() + tld)
    except:
        pass
