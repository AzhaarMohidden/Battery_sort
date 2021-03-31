
import random

# arr_temp = [[0 for i in range(2)] for j in range(18)]
# arr_rec = [["000" for i in range(8)] for j in range(125)]
# arr_temp = [["   " for i in range(8)] for j in range(127)]

def fill_slots(arr_rec):
    arr_temp = [["   " for i in range(8)] for j in range(127)]
    for i in range(len(arr_rec)):
        num = i
        if (arr_rec[num][0] != 0):
            # print(arr_rec[num])
            # print("****************")
            # print(arr_rec[num][5])
            # print(arr_rec[num][6])
            # print((int(arr_rec[num][5])-1)*18 + int(arr_rec[num][6]))
            # print("****************")
            arr_temp[(int(arr_rec[num][5])-1)*18 + int(arr_rec[num][6])] = arr_rec[num]
            arr_temp[(int(arr_rec[num][5])-1)*18 + int(arr_rec[num][6])][0]= arr_temp[(int(arr_rec[num][5])-1)*18 + int(arr_rec[num][6])][0].replace("009", '')
            arr_temp[(int(arr_rec[num][5])-1)*18 + int(arr_rec[num][6])][2]= arr_temp[(int(arr_rec[num][5])-1)*18 + int(arr_rec[num][6])][2].replace("%", '')
            if (arr_temp[(int(arr_rec[num][5])-1)*18 + int(arr_rec[num][6])][2] == ''):
                arr_temp[(int(arr_rec[num][5])-1)*18 + int(arr_rec[num][6])][2] = '0'
            arr_temp[(int(arr_rec[num][5])-1)*18 + int(arr_rec[num][6])][2]= int(arr_temp[(int(arr_rec[num][5])-1)*18 + int(arr_rec[num][6])][2])
            if (arr_temp[(int(arr_rec[num][5])-1)*18 + int(arr_rec[num][6])][2] > 99):
                arr_temp[(int(arr_rec[num][5])-1)*18 + int(arr_rec[num][6])][2] = str(arr_temp[(int(arr_rec[num][5])-1)*18 + int(arr_rec[num][6])][2])
            elif (arr_temp[(int(arr_rec[num][5])-1)*18 + int(arr_rec[num][6])][2] > 9) :
                arr_temp[(int(arr_rec[num][5])-1)*18 + int(arr_rec[num][6])][2] = str(arr_temp[(int(arr_rec[num][5])-1)*18 + int(arr_rec[num][6])][2]) + "%"
            elif (arr_temp[(int(arr_rec[num][5])-1)*18 + int(arr_rec[num][6])][2]<= 9 ):
                arr_temp[(int(arr_rec[num][5])-1)*18 + int(arr_rec[num][6])][2] = str(arr_temp[(int(arr_rec[num][5])-1)*18 + int(arr_rec[num][6])][2]) + "% "


    # for l in range(len(arr_temp)):
    #     print(l, end ="")
    #     print(arr_temp[l])
    Output_multiple(1, arr_temp)





    # for i in range(len(arr_rec)):
    #     if (arr_rec[i][0] != 0):
    #         arr_temp[i] = arr_rec[(int(arr_rec[i][5])*0) + int(arr_rec[i][6])]
    #         print("*****************")
    #         print(arr_temp[i])
    #         print("*****************")
    #         print(i)


    # print(arr_rec)





def fill():
    for batteries in range(len(arr_temp)):


        for n in range(2):
            arr_temp[batteries][0] = str(random.randint(100, 900))
            soc_t = random.randint(0, 100)
            if (soc_t < 100 and soc_t > 9):
                arr_temp[batteries][1] = str(soc_t) + "%"
            elif soc_t < 10:
                arr_temp[batteries][1] = " " + str(soc_t) + "%"
            else:
                arr_temp[batteries][1] = str(soc_t)

            # arr_temp[batteries][1] = str(random.randint(145, 199))
            # arr_temp[batteries][0] = batteries
            # arr_temp[batteries][1] = batteries  + 1

# Current_battery[f][0], temp_data[0][0], Current_battery[f][1], Current_battery[f][4], Current_battery[f][2], Current_battery[f][3], Current_battery[f][5],Current_battery[f][6], Current_battery[f][7] = lg_r.read_text(extracted_serial_new,"Batterieverzeichnis_new")
# Current_battery = [[Serial, lastChargeDate, SOC, SOH, MAX_Error, LastChargeUnit, LastChargePosition, FileLength]]

def Output_single(unit, arr_temp):
        print("                     Unit: " + str(unit) )
        print("        | ------------------------------ |")
        print("        " + "|   1    2    3    4    5    6   |")
        print("        " + "|  ___  ___  ___  ___  ___  ___  |")
        print("Serial: " + "| |" + str(arr_temp[0][0]) + "|" + "|" + str(arr_temp[1][0]) + "|" + "|" + str(arr_temp[2][0]) + "|" + "|" + str(arr_temp[3][0]) + "|" + "|" + str(arr_temp[4][0]) + "|" + "|" + str(arr_temp[5][0]) + "|" + " |")
        print("SOC:    " + "| |" + str(arr_temp[0][1]) + "|" + "|" + str(arr_temp[1][1]) + "|" + "|" + str(arr_temp[2][1]) + "|" + "|" + str(arr_temp[3][1]) + "|" + "|" + str(arr_temp[4][1]) + "|" + "|" + str(arr_temp[5][1]) + "|" + " |")
        print("        " + "| |___||___||___||___||___||___| | ")
        print("        " + "|                                | ")
        print("        " + "|   7    8    9   10   11   12   |")
        print("        " + "|  ___  ___  ___  ___  ___  ___  |")
        print("Serial: " + "| |" + str(arr_temp[6][0]) + "|" + "|" + str(arr_temp[7][0]) + "|" + "|" + str(arr_temp[8][0]) + "|" + "|" + str(arr_temp[9][0]) + "|" + "|" + str(arr_temp[10][0]) + "|" + "|" + str(arr_temp[11][0]) + "|" + " |")
        print("SOC:    " + "| |" + str(arr_temp[6][1]) + "|" + "|" + str(arr_temp[7][1]) + "|" + "|" + str(arr_temp[8][1]) + "|" + "|" + str(arr_temp[9][1]) + "|" + "|" + str(arr_temp[10][1]) + "|" + "|" + str(arr_temp[11][1]) + "|"+ " |")
        print("        " + "| |___||___||___||___||___||___| |")
        print("        " + "|                                | ")
        print("        " + "|  13   14   15   16   17   18   |")
        print("        " + "|  ___  ___  ___  ___  ___  ___  |")
        print("Serial: " + "| |" + str(arr_temp[12][0]) + "|" + "|" + str(arr_temp[13][0]) + "|" + "|" + str(arr_temp[14][0]) + "|" + "|" + str(arr_temp[15][0]) + "|" + "|" + str(arr_temp[16][0]) + "|" + "|" + str(arr_temp[17][0]) + "|"+ " |" )
        print("SOC:    " + "| |" + str(arr_temp[12][1]) + "|" + "|" + str(arr_temp[13][1]) + "|" + "|" + str(arr_temp[14][1]) + "|" + "|" + str(arr_temp[15][1]) + "|" + "|" + str(arr_temp[16][1]) + "|" + "|" + str(arr_temp[17][1]) + "|" + " |")
        print("        " + "| |___||___||___||___||___||___| |")
        print("")
        # print("|" + str(arr_battery[1][1]) + "|" + "|" +str(arr_battery[1][2]) + "|" )
        # print("|" + str(arr_battery[2][1]) + "|" + "|" +str(arr_battery[2][2]) + "|" )

def Output_multiple(unit, arr_temp):
        print("                     Unit: " + str(unit) , end = "")
        print("                                   Unit: " + str(unit +1) , end = "")
        print("                                   Unit: " + str(unit +2) , end = "")
        print("                                   Unit: " + str(unit + 3) , end = "")
        print("                                    Unit: " + str(unit + 4) )
        print("        | ------------------------------ |", end = "")
        print("        | ------------------------------ |", end = "")
        print("        | ------------------------------ |", end = "")
        print("        | ------------------------------ |", end = "")
        print("        | ------------------------------ |")
        print("        " + "|   1    2    3    4    5    6   |", end = "")
        print("        " + "|   1    2    3    4    5    6   |", end = "")
        print("        " + "|   1    2    3    4    5    6   |", end = "")
        print("        " + "|   1    2    3    4    5    6   |", end = "")
        print("        " + "|   1    2    3    4    5    6   |")
        print("        " + "|  ___  ___  ___  ___  ___  ___  |", end = "")
        print("        " + "|  ___  ___  ___  ___  ___  ___  |", end = "")
        print("        " + "|  ___  ___  ___  ___  ___  ___  |", end = "")
        print("        " + "|  ___  ___  ___  ___  ___  ___  |", end = "")
        print("        " + "|  ___  ___  ___  ___  ___  ___  |")
        print("Serial: " + "| |" + str(arr_temp[1][0]) + "|" + "|" + str(arr_temp[2][0]) + "|" + "|" + str(arr_temp[3][0]) + "|" + "|" + str(arr_temp[4][0]) + "|" + "|" + str(arr_temp[5][0]) + "|" + "|" + str(arr_temp[6][0]) + "|" + " |" , end = "")
        print("        " + "| |" + str(arr_temp[19][0]) + "|" + "|" + str(arr_temp[20][0]) + "|" + "|" + str(arr_temp[21][0]) + "|" + "|" + str(arr_temp[22][0]) + "|" + "|" + str(arr_temp[23][0]) + "|" + "|" + str(arr_temp[24][0]) + "|" + " |" , end = "")
        print("        " + "| |" + str(arr_temp[37][0]) + "|" + "|" + str(arr_temp[38][0]) + "|" + "|" + str(arr_temp[39][0]) + "|" + "|" + str(arr_temp[40][0]) + "|" + "|" + str(arr_temp[41][0]) + "|" + "|" + str(arr_temp[42][0]) + "|" + " |" , end = "")
        print("        " + "| |" + str(arr_temp[55][0]) + "|" + "|" + str(arr_temp[56][0]) + "|" + "|" + str(arr_temp[57][0]) + "|" + "|" + str(arr_temp[58][0]) + "|" + "|" + str(arr_temp[59][0]) + "|" + "|" + str(arr_temp[60][0]) + "|" + " |" , end = "")
        print("        " + "| |" + str(arr_temp[73][0]) + "|" + "|" + str(arr_temp[74][0]) + "|" + "|" + str(arr_temp[75][0]) + "|" + "|" + str(arr_temp[76][0]) + "|" + "|" + str(arr_temp[77][0]) + "|" + "|" + str(arr_temp[78][0]) + "|" + " |" )
        print("SOC:    " + "| |" + str(arr_temp[1][2]) + "|" + "|" + str(arr_temp[2][2]) + "|" + "|" + str(arr_temp[3][2]) + "|" + "|" + str(arr_temp[4][2]) + "|" + "|" + str(arr_temp[5][2]) + "|" + "|" + str(arr_temp[6][2]) + "|" + " |", end = "")
        print("        " + "| |" + str(arr_temp[19][2]) + "|" + "|" + str(arr_temp[20][2]) + "|" + "|" + str(arr_temp[21][2]) + "|" + "|" + str(arr_temp[22][2]) + "|" + "|" + str(arr_temp[23][2]) + "|" + "|" + str(arr_temp[24][2]) + "|" + " |" , end = "")
        print("        " + "| |" + str(arr_temp[37][2]) + "|" + "|" + str(arr_temp[38][2]) + "|" + "|" + str(arr_temp[39][2]) + "|" + "|" + str(arr_temp[40][2]) + "|" + "|" + str(arr_temp[41][2]) + "|" + "|" + str(arr_temp[42][2]) + "|" + " |" , end = "")
        print("        " + "| |" + str(arr_temp[55][2]) + "|" + "|" + str(arr_temp[56][2]) + "|" + "|" + str(arr_temp[57][2]) + "|" + "|" + str(arr_temp[58][2]) + "|" + "|" + str(arr_temp[59][2]) + "|" + "|" + str(arr_temp[60][2]) + "|" + " |" , end = "")
        print("        " + "| |" + str(arr_temp[73][2]) + "|" + "|" + str(arr_temp[74][2]) + "|" + "|" + str(arr_temp[75][2]) + "|" + "|" + str(arr_temp[76][2]) + "|" + "|" + str(arr_temp[77][2]) + "|" + "|" + str(arr_temp[78][2]) + "|" + " |" )
        print("        " + "| |___||___||___||___||___||___| | ", end = "")
        print("       " + "| |___||___||___||___||___||___| | ", end = "")
        print("       " + "| |___||___||___||___||___||___| | ", end = "")
        print("       " + "| |___||___||___||___||___||___| | ", end = "")
        print("       " + "| |___||___||___||___||___||___| |")
        print("       " + " |                                |", end = "")
        print("       " + " |                                |", end = "")
        print("       " + " |                                |", end = "")
        print("       " + " |                                |", end = "")
        print("       " + " |                                |")
        print("        " + "|   7    8    9   10   11   12   |", end = "")
        print("        " + "|   7    8    9   10   11   12   |", end = "")
        print("        " + "|   7    8    9   10   11   12   |", end = "")
        print("        " + "|   7    8    9   10   11   12   |", end = "")
        print("        " + "|   7    8    9   10   11   12   |")
        print("        " + "|  ___  ___  ___  ___  ___  ___  |", end = "")
        print("        " + "|  ___  ___  ___  ___  ___  ___  |", end = "")
        print("        " + "|  ___  ___  ___  ___  ___  ___  |", end = "")
        print("        " + "|  ___  ___  ___  ___  ___  ___  |", end = "")
        print("        " + "|  ___  ___  ___  ___  ___  ___  |")
        print("Serial: " + "| |" + str(arr_temp[7][0]) + "|" + "|" + str(arr_temp[8][0]) + "|" + "|" + str(arr_temp[9][0]) + "|" + "|" + str(arr_temp[10][0]) + "|" + "|" + str(arr_temp[11][0]) + "|" + "|" + str(arr_temp[12][0]) + "|" + " |", end = "")
        print("        " + "| |" + str(arr_temp[25][0]) + "|" + "|" + str(arr_temp[26][0]) + "|" + "|" + str(arr_temp[27][0]) + "|" + "|" + str(arr_temp[28][0]) + "|" + "|" + str(arr_temp[29][0]) + "|" + "|" + str(arr_temp[30][0]) + "|" + " |", end = "")
        print("        " + "| |" + str(arr_temp[43][0]) + "|" + "|" + str(arr_temp[44][0]) + "|" + "|" + str(arr_temp[45][0]) + "|" + "|" + str(arr_temp[46][0]) + "|" + "|" + str(arr_temp[47][0]) + "|" + "|" + str(arr_temp[48][0]) + "|" + " |", end = "")
        print("        " + "| |" + str(arr_temp[61][0]) + "|" + "|" + str(arr_temp[62][0]) + "|" + "|" + str(arr_temp[63][0]) + "|" + "|" + str(arr_temp[64][0]) + "|" + "|" + str(arr_temp[65][0]) + "|" + "|" + str(arr_temp[66][0]) + "|" + " |", end = "")
        print("        " + "| |" + str(arr_temp[79][0]) + "|" + "|" + str(arr_temp[80][0]) + "|" + "|" + str(arr_temp[81][0]) + "|" + "|" + str(arr_temp[82][0]) + "|" + "|" + str(arr_temp[83][0]) + "|" + "|" + str(arr_temp[84][0]) + "|" + " |")
        print("SOC:    " + "| |" + str(arr_temp[7][2]) + "|" + "|" + str(arr_temp[8][2]) + "|" + "|" + str(arr_temp[9][2]) + "|" + "|" + str(arr_temp[10][2]) + "|" + "|" + str(arr_temp[11][2]) + "|" + "|" + str(arr_temp[12][2]) + "|"+ " |", end = "")
        print("        " + "| |" + str(arr_temp[25][2]) + "|" + "|" + str(arr_temp[26][2]) + "|" + "|" + str(arr_temp[27][2]) + "|" + "|" + str(arr_temp[28][2]) + "|" + "|" + str(arr_temp[29][2]) + "|" + "|" + str(arr_temp[30][2]) + "|" + " |", end = "")
        print("        " + "| |" + str(arr_temp[43][2]) + "|" + "|" + str(arr_temp[44][2]) + "|" + "|" + str(arr_temp[45][2]) + "|" + "|" + str(arr_temp[46][2]) + "|" + "|" + str(arr_temp[47][2]) + "|" + "|" + str(arr_temp[48][2]) + "|" + " |", end = "")
        print("        " + "| |" + str(arr_temp[61][2]) + "|" + "|" + str(arr_temp[62][2]) + "|" + "|" + str(arr_temp[63][2]) + "|" + "|" + str(arr_temp[64][2]) + "|" + "|" + str(arr_temp[65][2]) + "|" + "|" + str(arr_temp[66][2]) + "|" + " |", end = "")
        print("        " + "| |" + str(arr_temp[79][2]) + "|" + "|" + str(arr_temp[80][2]) + "|" + "|" + str(arr_temp[81][2]) + "|" + "|" + str(arr_temp[82][2]) + "|" + "|" + str(arr_temp[83][2]) + "|" + "|" + str(arr_temp[84][2]) + "|" + " |")
        print("        " + "| |___||___||___||___||___||___| |", end = "")
        print("        " + "| |___||___||___||___||___||___| |", end = "")
        print("        " + "| |___||___||___||___||___||___| |", end = "")
        print("        " + "| |___||___||___||___||___||___| |", end = "")
        print("        " + "| |___||___||___||___||___||___| |")
        print("        " + "|                                | ", end = "")
        print("       " + "|                                | ", end = "")
        print("       " + "|                                | ", end = "")
        print("       " + "|                                | ", end = "")
        print("       " + "|                                |")
        print("        " + "|  13   14   15   16   17   18   |", end = "")
        print("        " + "|  13   14   15   16   17   18   |", end = "")
        print("        " + "|  13   14   15   16   17   18   |", end = "")
        print("        " + "|  13   14   15   16   17   18   |", end = "")
        print("        " + "|  13   14   15   16   17   18   |")
        print("        " + "|  ___  ___  ___  ___  ___  ___  |", end = "")
        print("        " + "|  ___  ___  ___  ___  ___  ___  |", end = "")
        print("        " + "|  ___  ___  ___  ___  ___  ___  |", end = "")
        print("        " + "|  ___  ___  ___  ___  ___  ___  |", end = "")
        print("        " + "|  ___  ___  ___  ___  ___  ___  |")
        print("Serial: " + "| |" + str(arr_temp[13][0]) + "|" + "|" + str(arr_temp[14][0]) + "|" + "|" + str(arr_temp[15][0]) + "|" + "|" + str(arr_temp[16][0]) + "|" + "|" + str(arr_temp[17][0]) + "|" + "|" + str(arr_temp[18][0]) + "|"+ " |" , end = "")
        print("        " + "| |" + str(arr_temp[31][0]) + "|" + "|" + str(arr_temp[32][0]) + "|" + "|" + str(arr_temp[33][0]) + "|" + "|" + str(arr_temp[34][0]) + "|" + "|" + str(arr_temp[35][0]) + "|" + "|" + str(arr_temp[36][0]) + "|"+ " |" , end = "")
        print("        " + "| |" + str(arr_temp[49][0]) + "|" + "|" + str(arr_temp[50][0]) + "|" + "|" + str(arr_temp[51][0]) + "|" + "|" + str(arr_temp[52][0]) + "|" + "|" + str(arr_temp[53][0]) + "|" + "|" + str(arr_temp[54][0]) + "|"+ " |" , end = "")
        print("        " + "| |" + str(arr_temp[67][0]) + "|" + "|" + str(arr_temp[68][0]) + "|" + "|" + str(arr_temp[69][0]) + "|" + "|" + str(arr_temp[70][0]) + "|" + "|" + str(arr_temp[71][0]) + "|" + "|" + str(arr_temp[72][0]) + "|"+ " |" , end = "")
        print("        " + "| |" + str(arr_temp[85][0]) + "|" + "|" + str(arr_temp[86][0]) + "|" + "|" + str(arr_temp[87][0]) + "|" + "|" + str(arr_temp[88][0]) + "|" + "|" + str(arr_temp[89][0]) + "|" + "|" + str(arr_temp[90][0]) + "|"+ " |" )
        print("SOC:    " + "| |" + str(arr_temp[13][2]) + "|" + "|" + str(arr_temp[14][2]) + "|" + "|" + str(arr_temp[15][2]) + "|" + "|" + str(arr_temp[16][2]) + "|" + "|" + str(arr_temp[17][2]) + "|" + "|" + str(arr_temp[18][2]) + "|" + " |", end = "")
        print("        " + "| |" + str(arr_temp[31][2]) + "|" + "|" + str(arr_temp[32][2]) + "|" + "|" + str(arr_temp[33][2]) + "|" + "|" + str(arr_temp[34][2]) + "|" + "|" + str(arr_temp[35][2]) + "|" + "|" + str(arr_temp[36][2]) + "|"+ " |" , end = "")
        print("        " + "| |" + str(arr_temp[49][2]) + "|" + "|" + str(arr_temp[50][2]) + "|" + "|" + str(arr_temp[51][2]) + "|" + "|" + str(arr_temp[52][2]) + "|" + "|" + str(arr_temp[53][2]) + "|" + "|" + str(arr_temp[54][2]) + "|"+ " |" , end = "")
        print("        " + "| |" + str(arr_temp[67][2]) + "|" + "|" + str(arr_temp[68][2]) + "|" + "|" + str(arr_temp[69][2]) + "|" + "|" + str(arr_temp[70][2]) + "|" + "|" + str(arr_temp[71][2]) + "|" + "|" + str(arr_temp[72][2]) + "|"+ " |" , end = "")
        print("        " + "| |" + str(arr_temp[85][2]) + "|" + "|" + str(arr_temp[86][2]) + "|" + "|" + str(arr_temp[87][2]) + "|" + "|" + str(arr_temp[88][2]) + "|" + "|" + str(arr_temp[89][2]) + "|" + "|" + str(arr_temp[90][2]) + "|"+ " |" )
        print("        " + "| |___||___||___||___||___||___| |", end = "")
        print("        " + "| |___||___||___||___||___||___| |", end = "")
        print("        " + "| |___||___||___||___||___||___| |", end = "")
        print("        " + "| |___||___||___||___||___||___| |", end = "")
        print("        " + "| |___||___||___||___||___||___| |")
        print("")
        print("                     Unit: " + str(unit + 5), end = "" )
        print("                                   Unit: " + str(unit + 6))
        print("        | ------------------------------ |", end = "")
        print("        | ------------------------------ |")
        print("        " + "|   1    2    3    4    5    6   |", end = "")
        print("        " + "|   1    2    3    4    5    6   |")
        print("        " + "|  ___  ___  ___  ___  ___  ___  |", end = "")
        print("        " + "|  ___  ___  ___  ___  ___  ___  |")
        print("Serial: " + "| |" + str(arr_temp[91][0]) + "|" + "|" + str(arr_temp[92][0]) + "|" + "|" + str(arr_temp[93][0]) + "|" + "|" + str(arr_temp[94][0]) + "|" + "|" + str(arr_temp[95][0]) + "|" + "|" + str(arr_temp[96][0]) + "|" + " |", end = "")
        print("        " + "| |" + str(arr_temp[109][0]) + "|" + "|" + str(arr_temp[110][0]) + "|" + "|" + str(arr_temp[111][0]) + "|" + "|" + str(arr_temp[112][0]) + "|" + "|" + str(arr_temp[113][0]) + "|" + "|" + str(arr_temp[114][0]) + "|" + " |")
        print("SOC:    " + "| |" + str(arr_temp[91][2]) + "|" + "|" + str(arr_temp[92][2]) + "|" + "|" + str(arr_temp[93][2]) + "|" + "|" + str(arr_temp[94][2]) + "|" + "|" + str(arr_temp[95][2]) + "|" + "|" + str(arr_temp[96][2]) + "|" + " |", end = "")
        print("        " + "| |" + str(arr_temp[109][2]) + "|" + "|" + str(arr_temp[110][2]) + "|" + "|" + str(arr_temp[111][2]) + "|" + "|" + str(arr_temp[112][2]) + "|" + "|" + str(arr_temp[113][2]) + "|" + "|" + str(arr_temp[114][2]) + "|" + " |")
        print("        " + "| |___||___||___||___||___||___| | ", end = "")
        print("       " + "| |___||___||___||___||___||___| | ")
        print("        " + "|                                | ", end = "")
        print("       " + "|                                | ")
        print("        " + "|   7    8    9   10   11   12   |", end = "")
        print("        " + "|   7    8    9   10   11   12   |")
        print("        " + "|  ___  ___  ___  ___  ___  ___  |", end = "")
        print("        " + "|  ___  ___  ___  ___  ___  ___  |")
        print("Serial: " + "| |" + str(arr_temp[97][0]) + "|" + "|" + str(arr_temp[98][0]) + "|" + "|" + str(arr_temp[99][0]) + "|" + "|" + str(arr_temp[100][0]) + "|" + "|" + str(arr_temp[101][0]) + "|" + "|" + str(arr_temp[102][0]) + "|" + " |", end = "")
        print("        " + "| |" + str(arr_temp[115][0]) + "|" + "|" + str(arr_temp[116][0]) + "|" + "|" + str(arr_temp[117][0]) + "|" + "|" + str(arr_temp[118][0]) + "|" + "|" + str(arr_temp[119][0]) + "|" + "|" + str(arr_temp[120][0]) + "|" + " |")
        print("SOC:    " + "| |" + str(arr_temp[97][2]) + "|" + "|" + str(arr_temp[98][2]) + "|" + "|" + str(arr_temp[99][2]) + "|" + "|" + str(arr_temp[100][2]) + "|" + "|" + str(arr_temp[101][2]) + "|" + "|" + str(arr_temp[102][2]) + "|"+ " |", end ="")
        print("        " + "| |" + str(arr_temp[115][2]) + "|" + "|" + str(arr_temp[116][2]) + "|" + "|" + str(arr_temp[117][2]) + "|" + "|" + str(arr_temp[118][2]) + "|" + "|" + str(arr_temp[119][2]) + "|" + "|" + str(arr_temp[120][2]) + "|" + " |")
        print("        " + "| |___||___||___||___||___||___| |", end = "")
        print("        " + "| |___||___||___||___||___||___| |")
        print("        " + "|                                | ", end = "")
        print("       " + "|                                | ")
        print("        " + "|  13   14   15   16   17   18   |", end = "")
        print("        " + "|  13   14   15   16   17   18   |")
        print("        " + "|  ___  ___  ___  ___  ___  ___  |", end = "")
        print("        " + "|  ___  ___  ___  ___  ___  ___  |")
        print("Serial: " + "| |" + str(arr_temp[103][0]) + "|" + "|" + str(arr_temp[104][0]) + "|" + "|" + str(arr_temp[105][0]) + "|" + "|" + str(arr_temp[106][0]) + "|" + "|" + str(arr_temp[107][0]) + "|" + "|" + str(arr_temp[108][0]) + "|"+ " |" , end = "")
        print("        " + "| |" + str(arr_temp[121][0]) + "|" + "|" + str(arr_temp[122][0]) + "|" + "|" + str(arr_temp[123][0]) + "|" + "|" + str(arr_temp[124][0]) + "|" + "|" + str(arr_temp[125][0]) + "|" + "|" + str(arr_temp[126][0]) + "|"+ " |")
        print("SOC:    " + "| |" + str(arr_temp[103][2]) + "|" + "|" + str(arr_temp[104][2]) + "|" + "|" + str(arr_temp[105][2]) + "|" + "|" + str(arr_temp[106][2]) + "|" + "|" + str(arr_temp[107][2]) + "|" + "|" + str(arr_temp[108][2]) + "|" + " |", end = "")
        print("        " + "| |" + str(arr_temp[121][2]) + "|" + "|" + str(arr_temp[122][2]) + "|" + "|" + str(arr_temp[123][2]) + "|" + "|" + str(arr_temp[124][2]) + "|" + "|" + str(arr_temp[125][2]) + "|" + "|" + str(arr_temp[126][2]) + "|"+ " |")
        # print("        " + "| |" + str(arr_temp[12][2]) + "|" + "|" + str(arr_temp[13][2]) + "|" + "|" + str(arr_temp[14][2]) + "|" + "|" + str(arr_temp[15][2]) + "|" + "|" + str(arr_temp[16][2]) + "|" + "|" + str(arr_temp[126][2]) + "|" + " |")
        print("        " + "| |___||___||___||___||___||___| |", end = "")
        print("        " + "| |___||___||___||___||___||___| |")
        print("")












if __name__ == '__main__':
    # print(arr_temp)
    # fill()
    # print(arr_temp)
    # Output_single(1, arr_temp)
    Output_multiple(1, arr_temp)
