# Grade Point Calculator

# Create a console-based program that will take a letter grade, such as B+ or C, and convert it to its 
# corresponding numeric value. It will use two prompts, one for the letter grade and a second for the
# modifier, if any (+ or -), and calculate, then output the proper number grade.

# •	Possible letter grades are A, B, C, D, and F
# •	Possible numeric values are 4, 3, 2, 1, and 0, respective to the letters listed above.
# •	Possible modifiers are a plus (+), a minus (–) or nothing. 
# •	There is no F+ or F–. 
# •	Using the + sign increases the numeric value by 0.3, using the – sign decreases it by 0.3. However, an A+ has 
#       still has a value of only 4.0. 
# •	A valid letter grade can be either uppercase or lowercase.
# •	If an invalid value is entered, display a warning message.


#Jenille Cheney
#W0198745

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    #welcome message
    print("Grade Point Calculator")
    print("")

    print("Valid letter grades that can be entered: A, B, C, D, F.")
    print("Valid grade modifiers are +, - or nothing.")
    print("All letter grades except F can include a + or - symbol.")
    print("Calculated grade point value cannot exceed 4.0")
    print("")
    #inputs
    grade = input("Please Enter a letter grade: ") .upper()
    mod = input("Please enter a modifier (+, - or nothing): ")
    # if else statements 
    #grade
    if grade == "A":
        numberValue = 4.0
        if mod == "-":
            modValue=-0.3
        else:
            modValue=0.0
    elif grade == "B":
        numberValue= 3.0
        if mod == "+":
            modValue = + 0.3
        elif mod== "-":
            modValue = - 0.3
        else:
            modValue= 0.0
    elif grade == "C":
        numberValue= 2.0
        if mod == "+":
            modValue = + 0.3
        elif mod == "-":
            modValue = - 0.3
        else:
            modValue = 0.0
    elif grade == "D":
        numberValue = 1.0
        if mod == "+":
            modValue=+0.3
        elif mod=="-":
            modValue= -0.3
        else:
            modValue=0.0
    elif grade == "F":
        numberValue = 0.0 
        if mod == "+" or mod == "-":
            modValue= 0.0
        else:
            modValue= 0.0
    else:
        numberValue=0.0
        modValue= 0.0
        print("you entered an invalid letter grade")

    totalGradeValue = numberValue+modValue
    
    print("The Numeric value is: {0:.1f}".format(totalGradeValue))

    #modifier









    # YOUR CODE ENDS HERE

main()
