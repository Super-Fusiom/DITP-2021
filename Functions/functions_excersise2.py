def cal_area():
    length = float(input("What is the length of the rectangle in cm?: "))
    width = float(input("What is the width of the rectangle in cm?: "))

    area = width * length

    print("The area is {}cm2".format(area))

cal_area()