def IDValid(ID):
    IDInteger = False
    stringID = str(ID)
    panjangID = len(ID)
    if panjangID == 1:
        IDInteger = False
        return False
    else:
        if ID[0] == "C" or ID[0] == "G":
            i = 1
            while i < panjangID and not IDInteger:
                if ID[i] not in "1234567890":
                    IDInteger = True
                else:
                    i += 1
            if IDInteger:
                return False
            else:
                return True
        else:
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