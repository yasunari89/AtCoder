A, B = map(int, input().split())

summary = A
for XORed in range(A+1, B+1):
    summary = summary ^ XORed

print(summary)

# def int2bin(x):
#     quotient = x
#     string_bin = ''
#     while(quotient != 1):
#         rest = quotient % 2
#         quotient = int((quotient - rest) / 2)
#         string_bin = str(rest) + string_bin
#     string_bin = '1' + string_bin
#     return int(string_bin)
#
# def bin2int(x):
#     power = int(len(str(x)) - 1)
#     integer = 0
#     i = 0
#     while(power >= 0):
#         integer += 2**power * int(str(x)[i])
#         i += 1
#         power -= 1
#     return integer


# divided_bin_str1 = str(int2bin(A))
# for divided in range(A+1, B+1):
#     added = ''
#     divided_bin_str2 = str(int2bin(divided))
#     if len(divided_bin_str1) < len(divided_bin_str2):
#         divided_bin_str1 = '0' + divided_bin_str1
#     else:
#         pass
#     # print(divided_bin_str1, divided_bin_str2)
#     for i in range(len(divided_bin_str1)):
#         ans = int(divided_bin_str1[i]) + int(divided_bin_str2[i])
#         if ans == 1:
#             added += '1'
#         else:
#             added += '0'
#     divided_bin_str1 = added
#
# added = int(added)
# ans = bin2int(added)
#
# print(ans)
