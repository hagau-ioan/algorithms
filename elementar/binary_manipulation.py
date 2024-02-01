import time


def is_even_nr(nr: int) -> bool:
    return (nr & 1) == 0


# 1000 (8 in binary)
# & 0111 (7 in binary)
# ------
#   0000 -> 8 is a power of 2
def is_power_of_two(nr: int) -> bool:
    return (nr & (nr - 1)) == 0


# Swapping Variable Values Without Using A Temporary Variable
def switch(a: int, b: int):
    # XOR operation example: 0101 and 0011 --> 0110 [0and0=0, 0and1=1, 1and1=0, 1and0=1]
    a = a ^ b
    print(a, b)
    b = a ^ b
    print(a, b)
    a = a ^ b
    print("Switched: ", a, b)


# https://levelup.gitconnected.com/6-mind-blowing-uses-of-bitwise-operations-that-you-probably-never-knew-existed-9e0359cfeaaf
if __name__ == '__main__':
    start_time = time.time()
    value = 64  # 4 (2 ^ 2), 8 (2 ^ 3), 16 (2 ^ 4), 32 (2 ^ 5), 64 (2 ^ 6), 128  (2 ^ 7)
    print("1. {} is par: {}".format(value, is_even_nr(value)))
    print("2. {} is_power_of_two: {}".format(value, is_power_of_two(value)))
    print("\t2.1 {} vs {}".format(bin(value).replace("0b", ""), bin(value - 1).replace("0b", "")))
    print("3. XOR operation switch no temp: 5, 3")
    switch(5, 3)  # a = a + b; b = a - b; a  = a - b

    print(bin(value))
    # original --> 1000000
    value >>= 1  # move to the left one bit (sub one bit) --> 100000
    print(bin(value))
    value <<= 1  # move to the right one bit (add one bit)--> 10000000
    print(bin(value))

    # a << b --> a * pow(2, b)
    # a >> b --> a / pow(2, b)
    x = 2 << 5  # convert "3" into binary (11) then extend it with 5 "00000" -> (1000000)
    print(x)
    print(bin(x))

    end_time = time.time()
    print("Execution time: {} seconds".format((end_time - start_time)))
