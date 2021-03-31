from reader import Log_reader as lr
from reader import Filename as fn
U1 =[
[213, 345, 456, 233, 355, 426],
[764, 555, 434, 734, 515, 474],
[213, 345, 456, 253, 315, 436] ]

# u2 = [[0]* 6] * 3
ar_LO  = [0 for i in range(6)]
ar_LOO = [0 for i in range(6)]
ar_SOC = [0 for i in range(6)]
ar_SOH = [0 for i in range(6)]
u2 = [[0 for i in range(6)] for j in range(3)]
# print("Unit 1")
# for r in U1:
#     # print("//")
#     # print(U1[U1.index(r)])
#     for e in U1[U1.index(r)]:
#         # print(U1[U1.index(r)].index(e))
#         if (U1[U1.index(r)].index(e)) > 4 :
#             print(str(e))
#         else:
#             print(str(e) , end= " " )
# u2[0][0] = 2
# print(u2[0][0])
# print(u2)
arr_battery = [[0 for i in range(2)] for j in range(6)]
for r in range(1):
    for element in range(2):
        battery_serial = str(input("Serial of Unit 2 " + "Battery No: " + str((r*6) + (element + 1)) +" - "))
        # print(battery_serial)
        # lr.read_text(battery_serial)
        u2[r][element] = battery_serial

for r2 in range(1):
    for c in range(2):
        LO, LOO, soc, soh = lr.read_text(u2[r2][c])
        # ar_LO[c - 1] = LO
        # ar_LOO[c - 1] = LOO
        # ar_SOC[c - 1] = soc
        # ar_SOH[c - 1] = soh
        arr_battery[r2][c] = u2[r2][c]
        # arr_battery[r2][c] = soc

        # print(u2[r2][c])
        # print(arr_battery[r2][c])
        print(arr_battery)
        # print("     Unit" + str(r2))
        # print("------------------------------")
        # # print(LO)
        # # print(LOO)
        # print(u2[r2][c])
        # print(soc)
        # print(soh)
# for unit in range(1):
#     print("Unit: " + str(unit))
#     print("------------------------------")
#     print("|" + str(arr_battery[1][1]) + "|" + "|" +str(arr_battery[1][2]) + "|" )
#     print("|" + str(arr_battery[2][1]) + "|" + "|" +str(arr_battery[2][2]) + "|" )


    # for p in range(6)

print(u2)
