def IDValid(ID):
    IDInteger = False
    stringID = str(ID)
    panjangID = len(ID)
    if panjangID == 1:
        IDInteger = False
        print("gagal")
        return False
    else:
        if ID[0] == "C" or ID[0] == "G":
            kodeID = stringID[1:panjangID]
            for i in kodeID:
                if i not in "1234567890":
                    IDInteger = False
                else:
                    IDInteger = True
            if IDInteger:
                return True
            else:
                return False
        else:
            IDInteger = False
            return False

def IDditemukan(ID, data):
        found = False
        i = 1
        while i < len(data) and not found:
            if data[i]["id"] == ID:
                found = True
            else:
                i += 1
        if found:
            return True
        else:
            return False