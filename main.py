"""" Developers: Anya Bayanova, Shmatov Denis """

def comfort(x,s):
    if x == "standard":
        s *= 1
    elif x == "improved_standard":
        s *= 1.2
    elif x == "apartment":
        s *= 1.5
    return s

with open("fund.txt") as n:
    with open("fund1.txt", "w") as out:
        for line in n:

            for g in range(0, 3):
                s = 0
                if g == 0:
                    k = "without_eat"
                elif g == 1:
                    s += 280
                    k = "breakfast"
                elif g == 2:
                    s += 1000
                    k = "half_board"

                if line.split()[1] == "single":
                    s += 2900
                    s = comfort(line.split()[3],s)
                elif line.split()[1] == "double_room":
                    s += 2300
                    s = comfort(line.split()[3], s)
                elif line.split()[1] == "junior_suite":
                    s += 3200
                    s = comfort(line.split()[3], s)
                elif line.split()[1] == "luxury":
                    s += 4100
                    s = comfort(line.split()[3], s)

                out.write("{} {} {} {} {} {} \n".format(line.split()[0], line.split()[1], line.split()[2],
                                                        line.split()[3], k, str(s)))
