import shelve, pyperclip

def main_menu_log():

    print("Enter '1' to COPY account and password,")
    print("Enter '2' to UPDATE a password,")
    print("Enter '3' to ADD a new entry,")
    print("Enter '4' to DELETE an account and password,")
    print("Enter '5' to VIEW your current account entries,")
    print("Enter '6' to QUIT and log out.")
    print("What would you like to do?")




print("This is your password manager.")
print(main_menu_log())



#can you pass the list to a key up here, and just call an open down in the options?
# format == site, username, pass


while True:
    
    try:
        n = int(input())

        if n == 1:

            break
          #
          #
          #
          #
          #
          #
          #


          

        elif n == 2:
            #need a confirmation
            pass_update = shelve.open('trashword')
            
            print("is the password you want to update in the reghister?")
            print("enter its site domain to find out:")
            
            opt_2 = input()

            if opt_2 in pass_update.keys():

                print(pass_update.get([opt_2][0], 0))
                print("... is the username or email associated with that site.")
                #
                #
                #
                #
                #
                #
                #can do a dictionary and re-key but that seems a little over-the-top
                # like I'm sure there's a smoother way to do things
                #
                #
                #
                #
                #
                #


            else:
                
                break

            
            
            #print("what is b?")
            #b = input()
            #print("what is c?")
            #c = input()
            #print("what is d?")
            #d = input()
            
            #flob = [b, c, d]
            
            #simple_write[a][1] = flob
            #simple_write.close()
            #print(simple_write)
            
            #print("so this is working")









        elif n == 3:

            password_entry = shelve.open('trashword')
            print("ADDING an entry is cleanest with a certain format.")
            print("So first we need the site you'll be listing the account under.")
            print("Doesn't have to be exact or have the '.com' on the end.")
            print("Enter site:")
            site_added = input()

            if site_added in password_entry:
        
                print("There is already an entry for that site listed.")
                print("Would you like to update that entry instead?")
                print("Enter '1' for yes, or '0' for no:")
                b = int(input())
                if b == 1:
                    n == 2
                    print(main_menu_log())
                elif b == 0:
                    break
                elif b < 0 or b > 1:
                    print("The number you've entered doesn't match with one of my options.")
                    break
                
            else:
            
                print("Next we'll need the username, or, if the site doesn't have one, an email you entered instead.")
                print("Enter username:")
                username_added = input()
                print("Lastly, we'll need the password to copy for future reference.")
                print("Enter password:")
                password_added = input()

            #
            #
            #   NEED A CONFIRM CONDITION DOWN HERE
            #
            # 
            #
                op_added = [username_added, password_added]
                password_entry[site_added] = op_added
                print("These have been added to the dictionary:")
                print("Site: " + site_added)
                print("Username: " + username_added)
                print("Password: " + password_added)

                password_entry.close()
            
        elif n == 4:
            #
            #
            #need a confirmation
            #
            #
            #
            #

            accounts_delete = shelve.open('trashword')
            
            print("Opening keys list...")
            
            for k in accounts_delete.keys():
                print(k)
                
            print(".")
            print("Which site entry do you wish to delete?")

            d = input()

            if d in accounts_delete.keys():
                del accounts_delete[d]

            else:
                print("Invalid response.")
            
            accounts_delete.close()

            print(main_menu_log())
            
        elif n == 5:

            accounts_view = shelve.open('trashword')

            print("................................")
            for k in accounts_view.keys():
                print(k)
                
            print("................................")
            print(main_menu_log())
                
        elif n == 6:

            print("Logging out, captain...")
            break
          
        elif n > 6 or n < 1:
            print("The number you've entered doesn't match with one of my options.")
            
    except ValueError:
        print("Invalid entry; a numerical value was required.")
        break


    
# start with dictionary listings

# let's say we open up, we'll need a print() with the intro
# we'll need an input() prompt asking for what we want to do
#  1. grab an account name and password
#  2. update an account OR its password
#  3. add a new account and password
#  4. deleting an account and password
#  5. "are you sure you want to delete/update " + x + "?"

#password we want
# we'll need a way to check the which account we want to grab
