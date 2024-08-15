def fishweighing():
    name= input("What is the species of your fish?")
    Length= input("How long is your fish in inches?")
    Girth= input("What is the girth of your fish?")
    name2= input("What is the species of your second fish?")
    Length2= input("How long is your second fish in inches?")
    Girth2= input("What is the girth of your fish?")
    if '.' in Length:
        Length= float(Length)
    else:
        Length= int(Length)
    if '.' in Girth:
        Girth= float(Girth)
    else:
        Girth= int(Girth)
    if '.' in Length2:
        Length2= float(Length2)
    else:
        Length2= int(Length2)
    if '.' in Girth2:
        Girth2= float(Girth2)
    else:
        Girth2= int(Girth2)
    Weight =((Girth*Girth*Length)/800)
    Weight2 =((Girth2*Girth2*Length2)/800)
    print("Your "+name+f" weighes {Weight:.2f} pounds")
    print("Your "+name2+f" weighes {Weight2:.2f} pounds")
    fish_list=[name,name2]
    weight_list=[Weight,Weight2]
    if 0<Weight<=41:
        print("Your "+name+" is a Small fish")
    elif 42<Weight<=99:
        print("Your "+name+" is a medium fish")
    elif 100<Weight<=174:
        print("Your "+name+" is a big fish")
    else:
        print("Your "+name+" is a giant fish")
    if 0<Weight2<=41:
        print("Your "+name2+" is a Small fish")
    elif 42<Weight2<=99:
        print("Your "+name2+" is a medium fish")
    elif 100<Weight2<=174:
        print("Your "+name2+" is a big fish")
    else:
        print("Your "+name2+" is a giant fish")
fishweighing()


