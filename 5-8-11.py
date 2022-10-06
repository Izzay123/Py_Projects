#Hello Admin + No users
#users = []
#if users:
#    for x in users:
#        if x == "Admin":
#            print("Hello Admin, would you like to see a status report?")
#        elif x != "Admin":
#            print(f"Hello, {x}, thank you for logging in again.")
#else:
#    print('We need some users!')

#Checking Usernames
#current_users = ['Tom','Tim','Tame','Tome','Tum']
#new_users = ['Shane', 'Sheen', 'Shine', 'Shone', 'Tom']

#current_users = [x.lower() for x in current_users]
#new_users = [x.lower() for x in new_users]
#for x in new_users:
#    if x in current_users:
#        print(f"{x}, you need a different username.")
#    else:
#        print('That username is available.')
    
#Ordinal Numbers

a_lis = list(range(1,10))
for x in a_lis:
    if x == 1:
        print("1st")
    elif x == 2:
        print("2nd")
    elif x == 3:
        print("3rd")
    else:
        print(f"{x}th")    
        