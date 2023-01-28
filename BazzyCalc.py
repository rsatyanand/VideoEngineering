# This calculator was intended for use
# with BazzyBro. Please run with python3
# eg python3 PATH/BazzyCalc.py
#
# Questions and comments to
# Rohan Satyanand
# rohansatyanand@gmail.com
# +64212625347

print("\nKia ora, welcome to BazzyCalc!  \nType q to quit\n")

infps = input("Project FPS: ")
if infps == "q":
    pass

else:
    frame = 1000000 / eval(infps)
    
    option = input("Please choose an option: \n  -Angular (deg) = a \n  -Fractional (sec) = f \n  -Microseconds = m\n\n")
    
    if option == "a":
        while True:
            inshut = input("\nShutter angle:  ")
            if inshut == "q":
                break
            else:
                shut = float(inshut) / 360
                exp = frame * shut
                if exp > frame:
                    print("\nINVALID\nMaximum = 360")
                    print("\n-----------------------")
                else:
                    trig = abs(frame - (exp / 2)) + 1000
                    print("Exposure time: ", int(exp))
                    print("Trigger delay: ", int(trig))
                    print("\n-----------------------")
                
    elif option == "m":
        while True:
            inshut = input("\nExposure time:  ")
            if inshut == "q":
                break
            else:
                exp = float(inshut)
                if exp > frame:
                    print("\nINVALID\nMaximum =",int(frame))
                    print("\n-----------------------")
                else:
                    trig = abs(frame - (exp / 2)) + 1000
                    print("Trigger delay: ", int(trig))
                    print("\n-----------------------")
                      
    elif option == "f":
        while True:
            inshut = input("\nShutter speed:  1/")
            if inshut == "q":
                break
            else:
                shut = 1 / (float(inshut) / eval(infps))
                exp = frame * shut
                if exp > frame:
                    print("\nINVALID\nMaximum = 1/",infps)
                    print("\n-----------------------")
                else:
                    trig = abs(frame - (exp / 2)) + 1000
                    print("Exposure time: ", int(exp))
                    print("Trigger delay: ", int(trig))
                    print("\n-----------------------")
                      
    else:
        pass
    
print("\n\nNgaa mihi\n")
        
        
