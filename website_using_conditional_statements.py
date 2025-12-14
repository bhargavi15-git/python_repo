name=(input('Enter your name: ')).capitalize()
x=input(f"Hey! {name}, which would you like to check \n 1. Upcoming Batches \n 2. Ask Anything \n")
if x=="Upcoming Batches":
    print("We have the following upcoming courses \n 1.AI Multi cloud Data Engineering \n 2.Azure Cloud and AI Data engineer \n 3.Fasttrack 3 months GenAI")
    y=input("Please enter your preference \n")
    def course(str1:str):
         duration_dict={"AI Multi cloud Data Engineering": '7 months',
                        "Azure Cloud and AI Data engineer": '4 months',
                        "Fasttrack 3 months GenAI": '120 hrs'
                        }
         starts_from_dict={"AI Multi cloud Data Engineering": '14 September, 2025',
                        "Azure Cloud and AI Data engineer": '2 July, 2025',
                        "Fasttrack 3 months GenAI": '19 July, 2025'
                           }
         batch_time_dict={"AI Multi cloud Data Engineering": '7 AM to 9 AM IST(Weekday Batch)',
                        "Azure Cloud and AI Data engineer": '9 AM - 1 PM IST(Weekend Batch)',
                        "Fasttrack 3 months GenAI": '8.30AM to 12.30PM IST(Weekday Batch)'
                           }
         print(f"The Duration of this course is {duration_dict[str1]} and it starts from {starts_from_dict[str1]}")
         z=input("Would you like to know the timings?Yes or No\n")
         if z=="Yes" or z=="yes":
                print(f"Batch Timing(s) {batch_time_dict[str1]}")
         elif z=="No" or z=="no":
                pass
         else:
                print("Invalid input")
         a=input("Would you like to enquire more about the course?Yes or No\n")
         if a=="Yes" or a=="yes":
                print("Please contact Helpline:08042757266 or email us atinfo@inceptez.com")
         elif a=="No" or a=="no":
                pass
         else:
                print("Invalid input")
    course(y)
elif x=="Ask Anything":
    question=input("Enter what you would like to ask \n")
    email=input("Enter your email so that we could respond \n")
    print(f"Thank you {name},We will contact you soon!")
else:

    print("Please enter an valid preference 1. Upcoming Batches 2. Ask Anything")
