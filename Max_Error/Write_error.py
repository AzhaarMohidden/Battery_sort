import pandas as pd
import xlsxwriter as xl


available_batteries = ['9508', '9509', '9510', '9511', '9512', '9513', '9514', '9515', '9516', '9517', '9532', '9534', '9535', '9536', '9537', '9544', '9545', '9546', '9547', '9548', '9549', '9550', '9551', '9556', '9557', '9558', '9564', '9568', '9569', '9570', '9571', '9572', '9573', '9574', '9575', '9576', '9577', '9578', '9579', '9580', '9581', '9582', '9583', '9584', '9585', '9586', '9587', '9588', '9589', '9590', '9591', '9592', '9593', '9594', '9595', '9596', '9597', '9598', '9599', '9600', '9601', '9602', '9603', '9610', '9611', '9612', '9613', '9615', '9646', '9647', '9649', '9650', '9651', '9652', '9653', '9654', '9655', '9656', '9657', '9658', '9659', '9660', '9661', '9662', '9663', '9666', '9670', '9671', '9672', '9673', '9674', '9675', '9677', '9682', '9683', '9684', '9685', '9686', '9687', '9688', '9689', '9690', '9691', '9700', '9701', '9702', '9703', '9704', '9705', '9706', '9707', '9708', '9709', '9710', '9711', '9712', '9713', '9714', '9715', '9716', '9717', '9718', '9719', '9720', '9721', '9722', '9723', '9724', '9725', '9726', '9727', '9728', '9729', '9730', '9731', '9732', '9733', '9734', '9735', '9736', '9737', '9738', '9739', '9740', '9741', '9742', '9743', '9744', '9745', '9746', '9747', '9748', '9749', '9750', '9751', '9752', '9753', '9754', '9755', '9756', '9757', '9758', '9759', '9760', '9761', '9762', '9763', '9764', '9765', '9766', '9767', '9768', '9769', '9770', '9771', '9772', '9773', '9774', '9775', '9776', '9777', '9778', '9779', '9780', '9781', '9782', '9783', '9784', '9785', '9786', '9787', '9788', '9789', '9790', '9791', '9792', '9793', '9794', '9795', '9796', '9797', '9798', '9799', '9800', '9801', '9802', '9803', '9804', '9805', '9806', '9807', '9808', '9809', '9810', '9811', '9813', '9820', '9821', '9822', '9823', '9824', '9825', '9826', '9827', '9828', '9829', '9830', '9831', '9832', '9833', '9834', '9835', '9836', '9837', '9838', '9839', '9840', '9841', '9842', '9843', '9844', '9845', '9848', '9849', '9850', '9851', '9852', '9853', '9854', '9855']

def write_text_file(filename, data):
    name = "C:\Azhaar_Data\Python\Logs"+ "\\" + str(filename) + ".txt"
    print(name)
    file1 = open(name, 'w+')
    for l in range(len(data)):
        for ll in range(len(data[l])):
            file1.writelines(data[l][ll])
            file1.writelines(" ")


        file1.writelines("\n")
    # file1.writelines(data)
    file1.close()

def Write_max_error(MAX_ERROR):
    workbook = xl.Workbook("Max_Error/Max_Error.xlsx")
    sheet = workbook.add_worksheet()
    sheet.write(0, 0, "Max_Error")
    for error in range(1, len(MAX_ERROR), 1):
        sheet.write(error, 0, int(MAX_ERROR[error]))
    workbook.close()

def variable_writer(name_colum, DATA):
    workbook = xl.Workbook("Output/Sample_output.xlsx")
    sheet = workbook.add_worksheet()
    for colum in range(len(name_colum)):
        sheet.write(0, colum, name_colum[colum])
        for rows in range(len(DATA[colum])):
            sheet.write(rows + 1,colum, DATA[colum][rows])
    workbook.close()


def Write_data(DATA, NAME, FILE):
    workbook = xl.Workbook(str(FILE) + "/" + str(FILE) + ".xlsx")
    sheet = workbook.add_worksheet()
    sheet.write(0, 0, "Serial")
    sheet.write(0, 1, NAME)
    for value in range(1, len(DATA) + 1, 1):
        sheet.write(value, 1, int(DATA[value - 1]))
        sheet.write(value, 0, int(available_batteries[value - 1]))
    workbook.close()

def Write_data_2row(DATA1, NAME1, DATA2, NAME2, FILE):
    workbook = xl.Workbook(str(FILE) + "/" + str(FILE) + ".xlsx")
    sheet = workbook.add_worksheet()
    sheet.write(0, 0, NAME1)
    sheet.write(0, 1, NAME2)
    for value in range(1, len(DATA1) + 1, 1):
        sheet.write(value, 0, DATA1[value - 1])
        sheet.write(value, 1, int(DATA2[value - 1]))
    workbook.close()

if __name__ == '__main__':
    print("Running as Main..")
    write_text_file("exe1", available_batteries )
