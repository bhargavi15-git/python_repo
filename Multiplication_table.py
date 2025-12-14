int1=int(input("Enter the starting table number:"))
int2=int(input("Enter the ending table number:"))
int3=int(input("Enter number of rows in each table:"))
int4=list(map(int, input("Enter tables you would like to skip separated by space: ").split()))


def multiplication_table(start_num:int,end_num:int,rows:int,rows_omit:list):
    """This program calculates the multiplication table. The maximum number of table you can print is 20"""
    while start_num<=end_num:
        if rows <= 200 and (end_num-start_num)<=20:
            for i in range(rows):
                if start_num not in rows_omit:
                    print(f"{start_num}*{i}={start_num*i}")
        else:
            print("Maximum number of rows can be only 200" if rows> 200 else "The maximum number of table you can print is 20")
            break
        start_num+=1
    else:
        print("The starting table number should be less than the ending table number")

multiplication_table(int1,int2,int3,int4)
