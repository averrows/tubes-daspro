#Argparse
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("folderData", help="folder dari data",
                    type=str)
args = parser.parse_args()
folderData = args.folderData

#Dapatkan data CSV
from function.csv_tools import parseCSV
userData = parseCSV(folderData + "/user.csv")
gadgetData = parseCSV(folderData + "/gadget.csv")
consumableData = parseCSV(folderData + "/consumable.csv")
consumableHistoryData = parseCSV(folderData + "/consumable_history.csv")
gadgetBorrowHistoryData = parseCSV(folderData + "/gadget_borrow_history.csv")
gadgetReturnHistoryData = parseCSV(folderData + "/gadget_return_history.csv")

def main():
    print("Cek")

if __name__ == "__main__":
    main()