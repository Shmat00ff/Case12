"""" Developers: Anya Bayanova 50%, Shmatov Denis 90% """
class Nomer():

     def __init__(self):
         pass
     def sort_booking(self):
         x = open("booking.txt", "r", encoding="utf-8")
         y = open("booking1.txt", "w", encoding="utf-8")
         list1 = []
         for line in x:
             if line.split()[0] != line.split()[-3]:
                 ll = line.split()[-3]
                 for i in range(1,8):
                    ll += " " + line.split()[i]
                 ll += "\n"
                 list1.append(ll)
             else:
                 list1.append(line)
         print(list1)
         for i in sorted(list1):
             y.writelines(i)




     def sravnenie(self):

         '''Тут он должен подбирать номер '''
         resereved = {}
         for i in range(0,25):
             resereved.update({i:"free !"})
         qq = 0
         qq1 = 0
         nom = ""
         date1 = "01.03.2018"
         myfile = open('booking1.txt', mode='r', encoding='utf-8')
         for line in myfile:
             dat = int(line.split()[-3].split('.')[0]) + int(line.split()[-2])
             dt = int(line.split()[0].split('.')[0])
             date = line.split()[0]

             for i in range(1,25):
                if resereved.get(i).split()[1] == str(dt):
                    resereved.update({i:"free !"})
             if resereved.get(nom) == "free !":
                 resereved.update({nom: "занято {}".format(dat)})
             k = 0
             nom = ""
             eat = ""
             spa = 0
             ppls = 0
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
                            spa = line1.split()[2]
                            ppls = line.split()[4]
                    elif line.split()[4] == line1.split()[2]:
                        price = float(line1.split()[-1])
                        if float(line.split()[-1]) >= price and price >= k:
                            k = price
                            nom = int(line1.split()[0])
                            eat = line1.split()[-2]
                            spa = line1.split()[2]
                            ppls = line.split()[4]
                 qq1 += price
                 if resereved.get(nom) != "free !":
                     qq += price
                     nom = ""
                     k = 0
                     spa = 0
                     eat = ""
                     ppls = 0

             if date1 == date:
                 print("------------------------------------------------------------------------------------")
                 print("Поступила заявка на бронирование:")
                 print()
                 print(line)
                 if nom != "":
                     print("Найдено:")
                     print()
                     print("номер " + str(nom) + " рассчитан на "+ str(spa) + " чел. фактически " + str(ppls) + " чел. стоимость "+ str(k) )
                     print()
                     print("------------------------------------------------------------------------------------")

                 else:
                     print("Предложений по данному запросу нет. В бронировании отказано.")
                     print()
                     print("------------------------------------------------------------------------------------")
             else:
                 print("Итог за " +date1+ " :" )
                 c = 0
                 cn1 = 0
                 cn2 = 0
                 cn3 = 0
                 cn4 = 0
                 for i in resereved:
                        if resereved[i] != "free !":
                            c += 1


                 print("Количество занятых номеров: " +str(c))
                 print("Количество свободных номеров: " +str(24-int(c)))
                 print("Загруженность номеров: " +str(int(round(c)/24*100)))
                 for i in range(1,24):
                     if i == 1 or i == 5 or i == 6 or i == 7 or i == 10 or i == 11 or i == 18 or i ==21 or i ==22:
                         if resereved[i] != "free !":
                             cn1 += 1
                     if i == 2 or i == 8 or i == 9 or i == 12 or i == 19 or i == 20:
                         if resereved[i] != "free !":
                             cn2 +=1
                     if i == 4 or i == 16 or i == 17 or i == 23 or i == 24:
                         if resereved[i] != "free !":
                             cn3 +=1
                     if i == 3 or i == 13 or i == 14 or i == 15:
                         if resereved[i] != "free !":
                             cn4 +=1
                 print("Одноместных номеров занято: " + str(cn1))
                 print("Двухместных номеров занято: " + str(cn2))
                 print("Полулюкс номеров занято: " + str(cn3))
                 print("Люкс номеров занято: " + str(cn4))

             date1 = date


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
    nom1.sort_booking()
    nom1.sravnenie()


if __name__=='__main__':
    main()