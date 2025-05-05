# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution.
# Student ID: 2052118
# Date: 13/12/2023

import sys

from graphics import*

def main():
    """"Prompt user to enter role and returns user role"""
    
    #Declare and initalizing variables
    user=0
    
    #Print the menu
    print("\n\t\t\t\t\t\t\tStudent's progression outcome for the academic year\n\n")
    print("This predicts the progression outcome of students for an individual student or staff member,")
    print("\n\t1 - Student\n\t2 - Staff Member\n")
    #If user entered a wrong role
    while user!=1 and user!=2:
        try:
            user=int(input("Enter 1 or 2 according to your role: "))
            if user!=1 and user!=2:
                raise Exception
        except ValueError:
            print("\n  Integer required...\n\n")
        except Exception:
            print("\n  You have entered an invalid integer...\n\n")
    print("\n\n")
    
    return user
    
def progression_outcome():
    """ Allow students or staff members to predict progression outcome for a individual student or multiple students at the end of each academic year """
    
    #Declare and initialize variables
    enter_again="y"
    data_list=[]
    student_total=0
    progress_total=0
    trailer_total=0
    excluded_total=0
    retriever_total=0
    progression_total_list=[]

    #List of acceptable credits
    range_list=[0,20,40,60,80,100,120]

    #If user wants to enter credits again
    while enter_again=="y":
        try:
            #Take credits
            pass_credit=int(input("Enter your total PASS credits: "))
            if pass_credit not in range_list:
                raise Exception
            defer_credit=int(input("Enter your total DEFER credits: "))
            if defer_credit not in range_list:
                raise Exception
            fail_credit=int(input("Enter your total FAIL credits: "))
            if fail_credit not in range_list:
                raise Exception

            #Total credits of a student
            total_credit=pass_credit + defer_credit + fail_credit
            print()
            
            #Output the progression outcome
            if total_credit==120:

                if pass_credit==120:
                    progression="Progress"
                    print("  Progression - ",progression)
                    progress_total=progress_total+1            

                elif pass_credit==100 and (defer_credit==20 or fail_credit==20):
                    progression = "Progress (module trailer)"
                    print("  Progression - ", progression)
                    trailer_total=trailer_total+1

                elif pass_credit<=40 and defer_credit<=40 and 80<=fail_credit<=120:
                    progression="Exclude"
                    print("  Progression - ",progression)
                    excluded_total=excluded_total+1

                else:
                    progression="Module retriever"
                    print("  Progression - ",progression)
                    retriever_total=retriever_total+1
                
                print("\n")
                
                #Exit the from program after the first attempt of a student
                if user==1:
                    sys.exit()
                else:
                    #Asking user to enter another set of data or not
                    print("Would you like to enter another set of data?")
                    enter_again = input("Enter 'y' for yes or 'q' to quit and view results: ")
    
                    while (enter_again!="y" and enter_again!="q"):
                        print("\n  You have entered a invalid letter...\n")
                        enter_again=input("Enter 'y' for yes or 'q' to quit and view results: ")

                    student_total=student_total+1  #Total number of students
                    
                    #Create a list with progression data
                    data_list.append(progression)
                    data_list.append(pass_credit)
                    data_list.append(defer_credit)
                    data_list.append(fail_credit)
          
                    if enter_again=="q":
                        break
            
            else:
                print("  Total incorrect...")

        except ValueError:
            print("\n  Integer required...")

        except Exception:
            print("\n  Out of range...")
    
        print("\n")

    print("\n\n")
    #Create a list with number of students for progressions
    progression_total_list.append(progress_total)
    progression_total_list.append(trailer_total)
    progression_total_list.append(excluded_total)
    progression_total_list.append(retriever_total)

    return (data_list,progression_total_list,student_total)

def graphics():
    """ Produce a 'histogram' representing the number of students who achieved a progress outcome in each category """

    #Declare and initalize variables
    progressions_list=["Progress","Trailer","Excluded","Retriever"]
    colour_list=["red","blue","green","yellow"]
    n=1
    
    #Open the window
    win=GraphWin("Histogram",700,600)
    win.setBackground("mint cream")
    #Display the topic
    topic=Text(Point(170,20),"Histogram Results")
    topic.setTextColor("grey")
    topic.setStyle("bold")
    topic.setSize(18)
    topic.draw(win)
   
    for x in range(4):
        #Create bars
        progression_bar=Rectangle(Point(75+78*2*x,540),Point(75+78*n,540-progression_total_list[x]*25))
        progression_bar.setFill(colour_list[x])
        progression_bar.setOutline("blue")
        progression_bar.draw(win)
        n=n+2
        #Display bar title below the bar
        progression=Text(Point(75+78*2*x+43,555),progressions_list[x])
        progression.setStyle("bold")
        progression.draw(win)
        #Display student count value at the top of the bar
        progression_count=Text(Point(75+78*2*x+40,540-progression_total_list[x]*25-10),progression_total_list[x])
        progression_count.setStyle("bold")
        progression_count.draw(win)
        #Display total number of students at the bottom of the window
        outcome_no=Text(Point(350,583),str(student_total)+" outcomes in total")
        outcome_no.setSize(14)
        outcome_no.setTextColor("brown")
        outcome_no.setStyle("bold")
        outcome_no.draw(win)
    #X-axis
    Line(Point(50,540),Point(650,540)).draw(win)
    
def list_output():
    """ Saves the input progression data to a list and print the data and save to a text file access from the list """
    
    #Declare and initalize variables
    nested_data_list=[]
    
    #Create a nested list with each student's progression data
    for x in range(0,len(data_list),4):
        nested_data_list.append(data_list[x:x+4])
    #Open a text file with write only mode    
    file=open("Progression_data.txt","w")
    file.write("Your progression data are...")
    file.write("\n\n")

    print(" ","Your progression data are...\n")
    #Print the progression data     
    for i in range(len(nested_data_list)):
       progression_data=str(nested_data_list[i][0])+" - "+str(nested_data_list[i][1])+", "+str(nested_data_list[i][2])+", "+str(nested_data_list[i][3])
       print("  ",progression_data)
       #Write progression data to a text file
       file.write("    "+(str(progression_data)))
       file.write("\n")
    file.close()

#------------------------------------------------------------------Main program-----------------------------------------------------------------------------

#Calling the "main" function
user = main()
#Calling the "progression_outcome" function
data_list,progression_total_list,student_total = progression_outcome()
#Calling the "graphics" function
graphics()
#Calling the "list_output" function
list_output()
    
