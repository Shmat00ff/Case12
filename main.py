"""" Developers: Anya Bayanova, Shmatov Denis """
class Nomer():

     def __init__(self):
         pass

     def sravnenie(self):

         '''Тут он должен подбирать номер '''
         resereved = {}
         for i in range(0,25):
             resereved.update({i:"free !"})

         nom = ""
         myfile = open('booking.txt', mode='r', encoding='utf-8')
         for line in myfile:
             dat = int(line.split()[-3].split('.')[0]) + int(line.split()[-2])
             dt = int(line.split()[0].split('.')[0])
             for i in range(1,25):
                if resereved.get(i).split()[1] == str(dt):
                    resereved.update({i:"free !"})
             if resereved.get(nom) == "free !":
                 resereved.update({nom: "занято {}".format(dat)})


             k = 0
             nom = ""
             eat = ""
             myfile1 = open('fund1.txt', "r", encoding='utf-8')
             price = 0
             for line1 in myfile1:
                 if resereved.get(int(line1.split()[0])) == "free !":
                    if line.split()[4] < line1.split()[2]:
                        price = float(line1.split()[-1]) * 0.7
                        if float(line.split()[-1]) >= price and price >= k:
                            k = price
                            nom = int(line1.split()[0])
                            eat = line1.split()[-2]


                    elif line.split()[4] == line1.split()[2]:
                        price = float(line1.split()[-1])
                        if float(line.split()[-1]) >= price and price >= k:
                            k = price
                            nom = int(line1.split()[0])
                            eat = line1.split()[-2]
                 if resereved.get(nom) != "free !":
                     nom = ""
                     k = 0
                     eat = ""

# первую дату сравнить с датой отъезда

             print(line, nom, k, eat)
         print(resereved)

     def data(self):
         myfile = open('booking.txt', mode='r', encoding='utf-8')
         for line in myfile:
             dat = int(line.split()[-3].split('.')[0]) + int(line.split()[-2])




     def sort(self):
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
                             if line.split()[-1] == "standard":
                                 s *= 1
                             elif line.split()[-1] == "improved_standard":
                                 s *= 1.2
                             elif line.split()[-1] == "apartment":
                                 s *= 1.5
                         elif line.split()[1] == "double_room":
                             s += 2300
                             if line.split()[-1] == "standard":
                                 s *= 1
                             elif line.split()[-1] == "improved_standard":
                                 s *= 1.2
                             elif line.split()[-1] == "apartment":
                                 s *= 1.5
                         elif line.split()[1] == "junior_suite":
                             s += 3200
                             if line.split()[-1] == "standard":
                                 s *= 1
                             elif line.split()[-1] == "improved_standard":
                                 s *= 1.2
                             elif line.split()[-1] == "apartment":
                                 s *= 1.5
                         elif line.split()[1] == "luxury":
                             s += 4100
                             if line.split()[-1] == "standard":
                                 s *= 1
                             elif line.split()[-1] == "improved_standard":
                                 s *= 1.2
                             elif line.split()[-1] == "apartment":
                                 s *= 1.5

                         out.write("{} {} {} {} {} {}\n".format(line.split()[0], line.split()[1], line.split()[2],
                                                            line.split()[3], k, str(s)))
         pass

def main():

    nom1 = Nomer()
    nom1.sort()
    nom1.sravnenie()
    nom1.data()


if __name__=='__main__':
    main()