import database as db
import ascii_boards as ab
import os
import time
from datetime import datetime
from Max_Error import Write_error as ME

now = datetime.now()

if __name__ == '__main__':
    db.get_serial()
    db.printer_ins()
    os.system("cls")
    ab.battery_sort()
    v = input("Press any key to continue..")

    while(1):
        print("1. Show Current Arrangment.")
        print("2. Show Current Arrangment and Sorted Arrangments")
        print("3. Exit Programe")
        ans = int(input("Please Select one of the above: "))
        print("Selected: "+ str(ans))

        if (ans == 1):
            os.system("cls")
            ab.battery_sort()
            db.current_arrangement_print()
            print("")
            print("DONE.")
            print("")
            print("")
            inserted_batteries_sorted = db.sorted_arrangement_print(0)
            db.sorted_arrangement_print(0)
            while(1):
                ans3 = str(input("Show Range selection? (Y/N): "))
                if (ans3 == "y" or ans3 == "Y" or ans3 == "yes" or ans3 == "YES"):
                    os.system("cls")
                    ab.battery_sort()
                    up_lim = int(input("Please enter Upper Limit of SOC: "))
                    down_lim = int(input("Please enter Lower Limit of SOC: "))
                    db.range_print(up_lim, down_lim)
                elif (ans3 == "n" or ans3 == "N" or ans3 == "no" or ans3 == "NO"):
                    print("")
                    break
                else:
                    print("Invalid selection..")

        elif (ans == 2):
            os.system("cls")
            ab.battery_sort()
            db.current_arrangement_print()
            print("")
            print("")
            print("")
            inserted_batteries_sorted = db.sorted_arrangement_print(1)
            print("")
            db.total_batteries(inserted_batteries_sorted)
            print("")
            print("DONE.")
            print("")
            print("")
            v = input("Press any key when sorting completed..")
            while(1):
                ans2 = str(input("Make Excel Files? (Y/N): "))
                if (ans2 == "y" or ans2 == "Y" or ans2 == "yes" or ans2 == "YES"):
                    os.system("cls")
                    ab.battery_sort()
                    inserted_batteries_sorted = db.sorted_arrangement_print(1)
                    db.position_print(inserted_batteries_sorted)
                    print("")
                    print("Created Excel File:- Positions..")
                    data = db.search()
                    date_time = now.strftime("%Y%m%d-%H.%M.%S")
                    ME.write_text_file(date_time, data)
                    print("Created Excel File:- Outputs..")
                    print("\n")
                    print("\n")
                    break
                elif (ans2 == "n" or ans2 == "N" or ans2 == "no" or ans2 == "NO"):
                    print("")
                    break
                else:
                    print("Invalid selection..")
        elif (ans == 3):
            print("Exiting Application")
            time.sleep(2)
            exit()
        else:
            print("Invalid Selection..")
            print("")
            print("")



    # db.current_arrangement_print()
