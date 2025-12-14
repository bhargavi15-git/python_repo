sum=0.0
choice=input("What do you like to explore? \n 1.Restaurants \n 2.Offers \n")
am_dict = {
        "chicken_briyani": 150,
        "chicken_65": 130,
        "fish_fry": 130,
        "pepper_chicken": 160,
        "payasam": 100,
        "gulab_jamun": 70
}

# --- Thalapakkati ---
thalapakkati_dict = {
    "chicken_briyani": 210,
    "mutton_briyani": 250,
    "egg_briyani": 180,
    "rasmalai": 170,
    "pepper_chicken": 170,
    "gulab_jamun": 80
}

# --- Saravana Bhavan ---
sb_dict = {
    "regular_meal": 100,
    "mini_meal": 80,
    "gobi_65": 90,
    "ice_cream": 70,
    "idli": 40,
    "vada": 40,
    "dosa": 70,
    "masala_dosa": 90
}


# --- A2B (Adyar Ananda Bhavan) ---
a2b_dict = {
    "regular_meal": 100,
    "mini_meal": 80,
    "gobi_65": 90,
    "ice_cream": 70,
    "paneer_tikka": 130,
    "veg_manchurian": 120,
    "baby_corn_fry": 100,
}

def print_dict_items(data_dict):
    for i, (key, value) in enumerate(data_dict.items(), start=1):
        print(f"{i}. {key}: {value}")

if choice=="Restaurants":
    restaurant = input("Choose restaurant of your choice: \n 1.AM Briyani \n 2.Thalapakkati \n 3.Saravana Bhavan \n 4.A2B \n")
    if restaurant == "AM Briyani":
        print(f"Currently AM Briyani serves:")
        print_dict_items(am_dict)
        print("Enter your choice here.After entering all your choices please enter 'done'")
        while True:
            food=input("")
            if food in am_dict.keys():

                sum+=am_dict[food]
            elif "Done" or "DONE" or "done":
                print("Thank you for choosing\n")
                break
            else:
                print("Try a valid choice")
        print("The total amount is {sum}.\n".format(sum=sum))
    elif restaurant == "Thalapakkati":
        print("Currently Thalapakkati serves:")
        print_dict_items(thalapakkati_dict)
        print("Enter your choice here.. once done please enter done")
        while True:
            food = input("")
            if food in thalapakkati_dict.keys():

                sum += thalapakkati_dict[food]
            elif "Done" or "DONE" or "done":
                print("Thank you for choosing\n")
                break
            else:
                print("Try a valid choice")
        print("The total amount is {sum}.\n".format(sum=sum))
    elif restaurant == "Saravana Bhavan":
        print("Currently Saravana Bhavan serves:")
        print_dict_items(sb_dict)
        print("Enter your choice here.. once done please enter done")
        while True:
            food = input("")
            if food in sb_dict.keys():

                sum += sb_dict[food]
            elif "Done" or "DONE" or "done":
                print("Thank you for choosing\n")
                break
            else:
                print("Try a valid choice")
        print("The total amount is {sum}.\n".format(sum=sum))
    elif restaurant == "A2B":
        print("Currently A2B serves:")
        print_dict_items(a2b_dict)
        print("Enter your choice here.. once done please enter done")
        while True:
            food = input("")
            if food in a2b_dict.keys():

                sum += a2b_dict[food]
            elif "Done" or "DONE" or "done":
                print("Thank you for choosing\n")
                break
            else:
                print("Try a valid choice")
        print("The total amount is {sum}.".format(sum=sum))


    def offer_cal(sum1: int):
        if sum > 499:
            offered_sum = sum - 100
            print(
                "Hurray! We offer Maximum discount up to ₹100 on all order above 499.\n\nYour total sum after discount is {offered_sum}".format(
                    offered_sum=offered_sum))
        else:
            offered_sum = sum
        print("Please proceed to pay\n")
        coupon = input("Do you have a valid Coupon? Yes or No \n")
        if coupon == 'Yes' or coupon == 'yes':
            coupon_offered1 = offered_sum - 100
            coupon_offered2 = offered_sum - offered_sum/10
            if coupon_offered1 > coupon_offered2:
                print("Hurray! You saved Rs.100 with coupon\n")
                return coupon_offered2

            else:
                print(f"Hurray! You saved Rs.{offered_sum / 10} with coupon\n")
                return coupon_offered1


        elif coupon == 'No' or coupon == 'no':

            bob_cc = input("Do you use a Bank of Baroda Credit card? Yes or No \n")
            if bob_cc == 'Yes' or bob_cc =='yes':
                bob_offered = offered_sum - offered_sum / 10
                print(f"Hurray! You saved Rs.{offered_sum / 10} with BOB credit card\n")
                return bob_offered
            elif coupon == 'No' or coupon == 'no':
                return offered_sum
            else:
                print("Chose a valid input")
        else:
            print("Chose a valid input")
    print(f"Your Total bill amount is Rs.{offer_cal(sum)}")
elif choice=="Offers":
    print("1.Maximum discount up to ₹100 on orders above ₹499")
    print("2.Coupon max discount of 100 or 10% which ever is lesser")
    print("3.Get 10% discount using Bank of Baroda Debit Cards.This is valid only when you dont have a coupon")

else:
    print("Chose a valid input")



