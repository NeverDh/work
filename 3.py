from datetime import date, datetime





def init():

    n = 0
    while True:
        while True:
            d1 = input("Digite a primeira data com o formato dd/mm/aaaa: ")
            if d1[0:2] == "0" or d2[0:1] == "0":
                exit()
                
            d2 = input("Digite a segunda data com o formato dd/mm/aaaa: ")
            if d1[0:2] == "0" or d2[0:2] == "0":
                exit()
            
        
            dat1 = datetime(int(d1[6:11]), int(d1[3:5]), int(d1[0:2]))
                
            dat2 = datetime(int(d2[6:11]), int(d2[3:5]), int(d2[0:2]))
                
                
            print(numDias(dat1, dat2))
    
        
        

def numDias(data1, data2):
    a = (data1-data2).days
    if str(a)[0] == "-":
        a = a * -1

    return a

init()


     
# date1 = date(2018, 12, 13)
# date2 = date(2019, 2, 25)
# print(numOfDays(date1, date2), "days")



# def bi(a):
#     first = int(a)%4
#     second = int(a)%100
#     third = int(a)%400

#     b = 0

#     if first == 0:
#         b = 1
#     if second == 0:
#         b = -1
#     if third == 0:
#         if b == 1:
#             None
#         else:
#             b = 1

#     return b
    





# def mes(m, a):
#     if m == "01":
#         m = 31
#     if m == "02":
#         m = 28
#     if m == "03":
#         m = 31
#     if m == "04":
#         m = 30
#     if m == "05":
#         m = 31
#     if m == "06":
#         m = 30
#     if m == "07":
#         m = 31
#     if m == "08":
#         m = 31
#     if m == "09":
#         m = 30
#     if m == "10":
#         m = 31
#     if m == "11":
#         m = 30
#     if m == "12":
#         m = 31

#     return m