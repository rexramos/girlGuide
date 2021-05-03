def main():
    

    def in_n():
        while 1:
            try: 
                input_n = int (input("Enter the number of guides selling cookies:"))
                break
            except ValueError:
                print ("Enter an integer...")
                continue
        return (input_n)

    def in_guide():
        x = 1
        while x == 1:
            input_guide = input (f"\nEnter the name of Guide #{counter}: ").capitalize()
            checker = input_guide.isnumeric()
            if checker is True:
                print ("Enter alphabet names only...")
            else:
                x = (x+1)
        return (input_guide)

    def in_box_sold():
        while 1:
            try: 
                input_box = int (input(f"Enter the number of boxes sold by {guide[counter-1]}:"))
                break
            except ValueError:
                print ("Enter only a whole integer number...")
                continue
        return (input_box)

    #Program Starts Here

    n = "" # determine number of guides
    guide = [] #list for names of guides
    box_sold = [] #list of box sold

    n = in_n()
    counter = 1
    while (counter <= n):
        input_guide = in_guide()
        guide.append(input_guide)
        input_box = in_box_sold()
        box_sold.append(input_box)
        counter +=1

    aveBox = (sum(box_sold)/n)
    maxBox = max(box_sold)
    print (f"\nThe average number of boxes sold by each guide was {aveBox:.1f}\n")
    print ("Guide\t\t\t\tPrizes Won:")
    print ("-" *80)
    
    for i,j in enumerate(guide):
        if box_sold[i] == maxBox:
            prize1 = ("Trip to Girl Jamboree in Aruba!")
            print (f"{j}\t\t\t\t-{prize1}")
        elif box_sold[i] > aveBox:
            prize2 = ("Super Seller Badge")
            print (f"{j}\t\t\t\t-{prize2}")
        elif (box_sold[i] <= aveBox) and (box_sold[i] != 0):
            prize3 = ("Left over cookies")
            print (f"{j}\t\t\t\t-{prize3}")
        elif box_sold[i] == 0:
            prize4 = " "
            print (f"{j}\t\t\t\t-{prize4}")
            

if __name__ == "__main__":
    main ()