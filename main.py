"""" Developers: Anya Bayanova, Shmatov Denis """
import re
class Nomer():

     def __init__(self):
         pass

     def budget(self):
         '''Узнаем бюджет клиента'''
         outputfile = "booking.txt"
         myfile1 = open(outputfile, mode='r', encoding='utf-8')
         for line in myfile1:
             parser_result = line[::-1]
             a = parser_result.find(' ')
             parser_result = parser_result[:a]
             print(parser_result[::-1])
         myfile1.close()

     def price(self):
         '''Узнаем цену номера'''
         outputfile = "fund1.txt"
         myfile1 = open(outputfile, mode='r', encoding='utf-8')
         for line in myfile1:
             parser_result = line[::-1]
             a = parser_result.find(' ')
             parser_result = parser_result[:a]
             print(parser_result[::-1])
         myfile1.close()

     def spl(self):
         '''Узнаем сколько клиентов'''
         outputfile = "fund1.txt"
         myfile1 = open(outputfile, mode='r', encoding='utf-8')
         for line in myfile1:
            result = re.split(r' ', line)
            print(result[2])
         myfile1.close()

     def nomspl(self):
         '''Узнаем сколько мест в номере'''
         outputfile = "booking.txt"
         myfile1 = open(outputfile, mode='r', encoding='utf-8')
         for line in myfile1:
             try:
                result = re.split(r' ', line)
                print(result[4])
             except IndexError:
                 pass
         myfile1.close()

     def sravnenie(self):
         '''Тут он должен подбирать номер '''
         myfile = open('booking.txt', mode='r', encoding='utf-8')


         for line in myfile:
             k = 0
             nom = ""
             myfile1 = open('fund1.txt', mode='r', encoding='utf-8')
             for line1 in myfile1:
                 if line.split()[4] <= line1.split()[2]:
                     if float(line.split()[-1]) >= float(line1.split()[-1]) and float(line1.split()[-1]) >= k:
                         k = float(line1.split()[-1])
                         nom = line1.split()[0] + " " + line1.split()[4]

             print(line, k, nom)



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

                out.write("{} {} {} {} {} {}\n".format(line.split()[0], line.split()[1], line.split()[2],
                                                        line.split()[3], k, str(s)))

def main():
    nom1 = Nomer()
    nom1.sravnenie()

if __name__=='__main__':
    main()