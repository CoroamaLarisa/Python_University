def dp(l):
    f = []
    f.append(l[0])
    maxi = max(l[0], l[1])
    f.append(maxi)
    for i in range(2, len(l)):
        f.append(max(f[i - 1], f[i - 2] + l[i]))

    return f[len(l) - 1]


def sum_el(the_list, i):
    if i == 0:
        return the_list[0]
    elif i == 1:
        return max(the_list[0], the_list[1])
    else:
        return max(sum_el(the_list, i - 1), sum_el(the_list, i - 2) + the_list[i])


the_list = [4,2,1,3]

print(sum_el(the_list, len(the_list) - 1))

print(dp([4,2,1,3]))

