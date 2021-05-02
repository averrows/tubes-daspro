import os
import sys
import time
def animation(durasi, teks):
    # String to be displayed when the application is loading
    ls_len = len(teks)

    currentTime = time.time()
    # String for creating the rotating line
    animation = "|/-\\"
    anicount = 0

    i = 0
    while time.time() < currentTime + durasi:
        time.sleep(0.025) 
                            
        # convert string ke dalam list
        teks_list = list(teks) 
        
        # dapatkan ordinal
        x = ord(teks_list[i])
        
        # y untuk nyimpan ordinal perubahan
        y = 0                             


        if x != 32 and x != 46:             
            if x>90:
                y = x-32
            else:
                y = x + 32
            teks_list[i]= chr(y)
        
        res =''             
        for j in range(ls_len):
            res = res + teks_list[j]
            
        sys.stdout.write("\r"+res + animation[anicount])

        teks = res

        
        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len
    else:
        sys.stdout.write("\r"+ teks + animation[anicount])

def animasiDoraemon(teks,durasi):
    # String to be displayed when the application is loading
    
    ls_len = len(teks)
    print(ls_len)
    currentTime = time.time()
    # String for creating the rotating line
    animation = "$^-/\\-^"
    anicount = 0

    while time.time() < currentTime + durasi:
        time.sleep(0.025)
        teksPerLine = teks.splitlines()
        print(teksPerLine)
        # sys.stdout.write("\r"+teks.replace('$',animation[anicount]))
        sys.stdout.flush()
        anicount = (anicount + 1)% 6

def animationLoad(durasi,teks):
    currentTime = time.time()
    animation = ["",".","..","...","....","....."]
    anicount = 0
    akhir = ""
    while time.time() < currentTime + durasi:
        time.sleep(0.5)         
        sys.stdout.write("\r"+ teks + akhir.replace(akhir,animation[anicount]))
        sys.stdout.flush()
        akhir = animation[anicount]
        anicount = (anicount + 1)% 6
