# Kia ora.  
# This calculator was intended for recording 
# and playing back off-speed audio with QTake HD
# in combination with either a Lexicon MX200 or an
# EHX Pitch Fork +. Please run with python3.  
# eg python3 PATH/TimeWarp.py
#
# Questions and comments to
# Rohan Satyanand 
# rohansatyanand@gmail.com
# +64212625347

print("\nWelcome to TimeWarp! \nType q to quit\n")
import math

inFPS = input("Project FPS:  ")
if inFPS == "q":
    pass
else:
    fps = eval(inFPS)
    
    while True:
            
        inrec = input("Record speed:   ")
        if inrec == "q":
            break
            
        # for percentages
        elif inrec[-1] == "%":
            rec = float(inrec[:-1]) / 100
            
        # for fractions and decimals
        else: 
            rec = eval(inrec)
            
        inpb = input("Playback speed: ")
        if inpb == "q":
            break
            
        # for percentages
        elif inpb[-1] == "%":
                pb = float(inpb[:-1]) / 100
            
        # for fractions and decimals
        else:
            pb = eval(inpb)

        
        # the following is the central equation for converting
        # linear time into logarithmic scale for pitch
        # semitone = 12*log2(1/|speed|)
        recsemitones = round(12 * math.log(1 / abs(rec), 2))
        pbsemitones = round(12 * math.log(1 / abs(pb), 2))

        
        # this dictionary assigns semitones to guitar
        # intervals, in the notation used by the 
        # EHX Pitch Fork + guitar pedal
        intervals = {
            -36 : "-3OC",
            -31 : "-P19",
            -29 : "-P18",
            -28 : "-M17",
            -27 : "-m17",
            -24 : "-2OC",
            -23 : "-M14",
            -22 : "-m14",
            -21 : "-M13",
            -20 : "-m13",
            -19 : "-P12",
            -18 : "-b12",
            -17 : "-P11",
            -16 : "-M10",
            -15 : "-m10",
            -14 : "-M9",
            -13 : "-m9",
            -12 : "-1OC",
            -11 : "-M7",
            -10 : "-m7",
            -9 : "-M6",
            -8 : "-m6",
            -7 : "-P5",
            -6 : "-b5",
            -5 : "-P4",
            -4 : "-M3",
            -3 : "-m3",
            -2 : "-M2",
            -1 : "-m2",
            1 : "m2",
            2 : "M2",
            3 : "m3",
            4 : "M3",
            5 : "P4",
            6 : "b5",
            7 : "P5",
            8 : "m6",
            9 : "M6",
            10 : "m7",
            11 : "M7",
            12 : "1OCT",
            13 : "m9",
            14 : "M9",
            15 : "m10",
            16 : "M10",
            17 : "P11",
            18 : "b12",
            19 : "P12",
            20 : "m13",
            21 : "M13",
            22 : "m14",
            23 : "M14",
            24 : "2OCT",
            27 : "m17",
            28 : "M17",
            29 : "P18",
            31 : "P19",
            36 : "3OCT"
            }

        # prints the Play Speed and Cam Speed setting to
        # use in QTakeHD (or other playout software)
        print("\nPlay Speed %:  ", round(100 * pb / rec, 2),"%")
        print("Cam Speed:     ", round(fps * rec / pb, 3),"fps\n")

        
        print("Record shift: ")
        if recsemitones == 0:
            print("0\nBypass\n")
        elif recsemitones > 0:
            # prints total number of semitones for the Lexicon MX200
            print("Up", recsemitones, "semitones")
            
            # for octaves + semitones notation
            print("Up", math.floor(recsemitones / 12) , "octaves," , int(recsemitones) % 12 , "semitones")
            
            # if more than one pitch correcting device is needed
            if recsemitones not in intervals:
                print("Compound\n")
                
            else:
                # for EHX Pitch Fork + notation
                print(intervals[recsemitones],"\n")
                
        else:
            # prints total number of semitones for the Lexicon MX200
            print("Down", abs(recsemitones), "semitones")

            # for octaves + semitones notation
            print("Down", math.floor(abs(recsemitones) / 12) , "octaves," , int(abs(recsemitones) % 12) , "semitones")

            # if more than one pitch correcting device is needed
            if recsemitones not in intervals:
                print("Compound\n")
                
            else:
                # for EHX Pitch Fork + notation
                print(intervals[recsemitones],"\n")

        
        print("Playback shift: ")
        if pbsemitones == 0:
            print("0\nBypass\n")
        elif pbsemitones > 0:
            # prints total number of semitones for the Lexicon MX200
            print("Up", pbsemitones, "semitones")

            # for octaves + semitones notation
            print("Up", math.floor(pbsemitones / 12) , "octaves," , int(pbsemitones) % 12 , "semitones")

            # if more than one pitch correcting device is needed
            if pbsemitones not in intervals:
                print("Compound\n")
                
            else:
                # for EHX Pitch Fork + notation
                print(intervals[pbsemitones],"\n")
        else:
            # prints total number of semitones for the Lexicon MX200
            print("Down", abs(pbsemitones), "semitones")

            # for octaves + semitones notation
            print("Down", math.floor(abs(pbsemitones) / 12) , "octaves," , int(abs(pbsemitones) % 12) , "semitones")

            # if more than one pitch correcting device is needed
            if pbsemitones not in intervals:
                print("Compound\n")
                
            else:
                # for EHX Pitch Fork + notation
                print(intervals[pbsemitones],"\n")
            
        print("-----------------------\n")

print("\nNgā mihi\n")
