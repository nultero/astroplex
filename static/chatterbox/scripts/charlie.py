#! usr/bin/env python3


import praw # for Charlie the scraper, the reddit shovel to dig up dirt
import pandas as pd # Charlie's dumping ground, indexing
import numpy as np 
import tensorflow as tf
import os
import time
from time import sleep # works as a timer so you don't always lock out reddit's request limiter
from os.path import isfile
import random # not 100% necessary, but since scraping takes awhile I use this as a spinny loader
import json





















class TextRunner:

    def __init__(self, sub, mod_path):

        self.sub = sub
        self.mod_path = mod_path
        print("\n")
        print(f"Text Runner model has been initialized for r/{self.sub}")

    def lord_of_the_strings(self):
        while True:
            path = os.getcwd()
            text = open(path + f"/{self.sub}.txt", "r").read()
            vocab = sorted(set(text))
            char2int = {u:i for i, u in enumerate(vocab)}
            int2char = np.array(vocab)
            text_as_int = np.array([char2int[c] for c in text])
            char_dataset = tf.data.Dataset.from_tensor_slices(text_as_int)
            from keras.models import load_model

            model = tf.keras.models.load_model(f'{self.mod_path}', compile=False)


            def generate_text(model, start_string, temperature, length):

                num_generate = length

                input_eval = [char2int[s] for s in start_string]
                input_eval = tf.expand_dims(input_eval, 0)

                text_generated = []

                temperature = temperature

                model.reset_states()
                for i in range(num_generate):
                    predictions = model(input_eval)
                    predictions = tf.squeeze(predictions, 0)
                    predictions = predictions / temperature
                    predicted_id = tf.random.categorical(predictions, num_samples=1)[-1,0].numpy()
                    input_eval = tf.expand_dims([predicted_id], 0)
                    text_generated.append(int2char[predicted_id])

                return (start_string + ''.join(text_generated))

            def bilbo_draggins():
                print("\n")
                my_precious = generate_text(model, start_string, temperature, length)
                print(my_precious)
                return my_precious # this actually has to be here to return results for below lol

            print("\n")
            print(f"    Model loaded for r/{self.sub}")
            print(f"    What temperature would you like Charlie to bake your string at?")
            print(f"(   for best results, keep very low — like, below 2, ~ 1.5 seems max)")
            temperature = float(input())
            print(f"    How many characters should you like your strings to be?")
            length = int(input())


            # break spot for the strings
            while True:
                print(f"    Almost ready to go. We need a seed string:")
                print("\n")
                start_string = str(input())


                #append a json list with the vacuum list
                vacuum = bilbo_draggins()

                #sort json temps for web app later
                if temperature >= 1.4:
                    temperature_string = "high"

                elif temperature < 1.4 and temperature >= 1:
                    temperature_string = "medium_high"

                elif temperature < 1 and temperature >= 0.8:
                    temperature_string = "medium"

                elif temperature < 0.8 and temperature >= 0.5:
                    temperature_string = "low"

                elif temperature < 0.5:
                    temperature_string = "extremely_low"

                else:
                    print("Error: something has gone wrong.")

                


                print("\n")
                print(f"    Would you like to save current string to /{self.sub}_{temperature_string}.json ?")
                print("    (answer in y/n or q to escape to main menu)")

                ans_input = str(input())
                if ans_input == "y":
                    filepath = f"{self.sub}_{temperature_string}.json" 

                    def writes_to():
                        with open(filepath, 'r') as jason:
                            data = json.load(jason)                    
                            
                        key_num = 0
                        for key in data.keys():
                            key_num += 1
                        new_dict = {f"{key_num + 1}":vacuum}
                        data.update(new_dict)

                        with open(filepath, "w") as jason:
                            json.dump(data, jason, indent=4)
                        

                        print("Reuse current temperature settings?")
                        ans_input2 = str(input())
                        if ans_input2 == "y":
                            pass
                        elif ans_input2 == "q":
                            main_menu_log()
                        else:
                            pass

                    if os.path.exists(filepath) == False:
                        with open(filepath, 'a+') as jason:
                            json.dump({}, jason)
                            print("\n")
                            print("    You may have to redo the string function, Charlie's JSON initializers are sorta broken atm")
                            writes_to()
                    else:
                        writes_to()
                elif ans_input == "q": #recursive main menu is bad design but I am not gonna be using this app for hours at a time
                    main_menu_log()
                else:
                    break













def modelSubMenu():

    while True:

        from pathlib import Path
        print("Searching for predictive models...")
        sleep(0.5)
            
        paths = []
        for pth in Path.cwd().iterdir():
            if pth.suffix == '.h5':
                paths.append(pth)

        listicle_of_models = 0
        print("\n")
        print("{" * 60)
        for i in paths:
            #really annoying seeing whole path
            #going to slice last coupla indices with trailing ellipses
            pthstr = str(i)
            print(f"   Enter '{listicle_of_models + 1}' to use ...{pthstr[-20:-1]} as your model for prediction")
            listicle_of_models += 1
        
        print("}" * 60)
        print("\n")
        print("    What would you like _ C h @ r l i e _ to do?")

        mn = int(input()) - 1


        if mn < 0:
            sleep(2.5)
            print("Error:")
            sleep(2.5)
            print("User intelligence not found")
            sleep(2.5)
            print("Returning to main menu...")
            sleep(1.5)
            break

        elif mn <= len(paths):
            #need a pattern match function for my other models here, TBD later, once I get the web app working
            while True:
                TextRunner("VXJunkies", paths[mn]).lord_of_the_strings()











        sleep(20)
        break
































class SubredditScraper:

    def __init__(self, sub, sort='new', lim=900, mode='w'):
        self.sub = sub
        self.sort = sort
        self.lim = lim
        self.mode = mode

        print(
            f'SubredditScraper instance created with values '
            f'sub = {sub}, sort = {sort}, lim = {lim}, mode = {mode}')

    def set_sort(self):
        if self.sort == 'new':
            return self.sort, reddit.subreddit(self.sub).new(limit=self.lim)
        elif self.sort == 'top':
            return self.sort, reddit.subreddit(self.sub).top(limit=self.lim)
        elif self.sort == 'hot':
            return self.sort, reddit.subreddit(self.sub).hot(limit=self.lim)
        else:
            self.sort = 'hot'
            print('Sort method was not recognized, defaulting to hot.')
            return self.sort, reddit.subreddit(self.sub).hot(limit=self.lim)

    def get_posts(self):
        """Get unique posts from a specified subreddit."""

        posts_fetched = 0
        comms_fetched = 0

        def fetch_a_spin():
            o = random.randrange(0,101)

            if o <= 20:
                print("/")
            elif 20 < o <= 40:
                print("\\")
            elif 40 < o <= 60:
                print("*")
            elif 60 < o <= 80:
                print("|")
            elif 80 < o <= 94:
                print("+")
            elif 94 < o <= 97:
                print("<.>")
            elif 97 < o <= 99:
                print(";")
            else:
                print(".....................")
                print(f"C H Λ R L I E has fetched {posts_fetched} posts so far...")
                print(".....................")
                print(f"... and that works out to {comms_fetched} comments so far.")
                print(".....................")
                print(f"This is {100 / (self.lim / (posts_fetched + 1))}% of your quota (margin of error +1)")
                print(".....................")

        sub_dict = {
            'selftext': [], 'title': [], 'id': [], 'comments': []}

        csv = f'{self.sub}_posts.csv'

        sort, subreddit = self.set_sort()

        df, csv_loaded = (pd.read_csv(csv), 1) if isfile(csv) else ('', 0)

        print(f'csv = {csv}')
        print(f'After set_sort(), sort = {sort} and sub = {self.sub}')
        print(f'csv_loaded = {csv_loaded}')

        print(f'Collecting information from r/{self.sub}.')



        for post in subreddit:
            unique_id = post.id not in tuple(df.id) if csv_loaded else True

            if unique_id:
                sub_dict['selftext'].append(post.selftext)
                sub_dict['title'].append(post.title)
                sub_dict['id'].append(post.id)

            # kept getting duplicates like before for the comment forest

                from praw.models import MoreComments

                for top_level_comment in post.comments:
                    unique_top_comment_id = top_level_comment.id not in tuple(df.id) if csv_loaded else True

                    if isinstance(top_level_comment, MoreComments):
                        continue
                    if unique_top_comment_id:
                        sub_dict['comments'].append(top_level_comment.body)
                        sub_dict['id'].append(top_level_comment.id)
                        comms_fetched += 1
                        fetch_a_spin()
                
                    post.comments.replace_more(limit=0)
                    for comment in post.comments.list():
                        unique_comment_id = comment.id not in tuple(df.id) if csv_loaded else True

                        if unique_comment_id:
                            sub_dict['comments'].append(comment.body)
                            sub_dict['id'].append(comment.id)
                            comms_fetched += 1
                            fetch_a_spin()
            posts_fetched += 1
            sleep(0.12)
            fetch_a_spin()

        # new_df = pd.DataFrame(sub_dict)
        new_df = pd.DataFrame({ key:pd.Series(value) for key, value in sub_dict.items() })

        if 'DataFrame' in str(type(df)) and self.mode == 'w':
            pd.concat([df, new_df], axis=0, sort=0).to_csv(csv, index=False)
            print(
                f'{len(new_df)} new posts collected and added to {csv}')
        elif self.mode == 'w':
            new_df.to_csv(csv, index=False)
            print(f'{len(new_df)} posts collected and saved to {csv}')
        else:
            print(
                f'{len(new_df)} posts were collected but they were not '
                f'added to {csv} because mode was set to "{self.mode}"')






















def main_menu_log():

    while True:


        ## all you gotta do to add a whole sub to scrape is to put it in the ""subWriteList"" below
        ## Charlie will populate its options from here and even create the Object scraper from scratch
        ## NOTE :: you do not need to put reddit's r/ in the sub name -- the scraper does that for ya
        subWriteList = ["VXJunkies", "swoleacceptance", "neckbeardRPG", "pathofexile", "CrusaderKings", "worldbuilding", "DiWHY", "wallstreetbets"]
        i = 0

        print("|" * 60)
        while i < len(subWriteList):
            print(f"   Enter '{i + 1}' to scrape r/{subWriteList[i]}")
            i += 1
        print("   ..........")
        print(f"   Enter '{i + 1}' to show predictive model TextRunner menu instead")
        print(f"   Enter '{i + 2}' to show regular expression menu instead")

        #end of options
        print("|" * 60)
        print("\n")
        print("What would you like _ C h Λ r l i e _ to do?")
        ##///////////////////////////////////////  INPUT begins
        n = int(input())


        if n < 0:
            sleep(2.5)
            print("Error:")
            sleep(2.5)
            print("User intelligence not found")
            sleep(2.5)
            print("Decommissioning Charlie instance...")
            sleep(2.5)
            break
        elif n == 0:
            print("Commencing division by zero operation:")
            sleep(2.5)
            print("This may take a while...")
            sleep(2.5)
            print("Gathering computational resources...")
            sleep(2.5)
            print("Contacting Russian mathematical professors...")
            sleep(2.5)
            print("Preparing to assume superintelligence...")
            sleep(2.5)
            print("Deriving space-flow time-constants from $deity_init_(__void__)...")
            sleep(5)
            try: 
                print(f"{1 / 0}")
            except ZeroDivisionError:
                print("Task failed successfully")
                sleep(2.5)
                print("Congratulating self")
                sleep(9999999)


        elif n <= len(subWriteList):
            SubredditScraper(f"{subWriteList[n - 1]}", lim=970, mode='w', sort='hot').get_posts()




        elif n == (len(subWriteList) + 1):

            modelSubMenu()



        #regex menu
        elif n == (len(subWriteList) + 2):
            
            i = 0
            while i < 10000:
                print(i)
                i += 1
                sleep(0.5)


        else:
            break


    # print("   Enter '6' to rewrap the database with regex (UNFINISHED)")




















def draws_C_H_A_R_L_I_E():

    sp = 13
    sl = 3
    done = 0
    teeth = 8

    print("\n")
    while sl < 9:
        print(" " * sp + "/" * sl)
        sp -= 1
        sl += 1
        sleep(0.4)
    print(" " * sp + "/" * 2 + "O" + "/" * 2 + "O" + 3 * "/")
    while sl < 11:
        print(" " * sp + "/" * sl)
        sp -= 1
        sl += 1
        sleep(0.4)
    print(" " * sp + "/" * 4 + "---" + "/" * 4)
    sleep(0.4)
    print(" " * (sp - 1) + "/" * 5 + "--" + "/" * 5)
    sp -= 1
    sl += 1
    sleep(0.4)
    print(" " * (sp - 1) + "/" * 6 + "-" + "/" * 7)
    sleep(0.4)
    print(" " * (sp - 1) + "/" * 7 + "/" * 8)
    sleep(0.4)
    while done < teeth:
        print(" " * (sp - 1) + "/" * 3 + "[" + "=" * teeth + "]" + "/" * 3)
        teeth -= 1
        sleep(0.4)
    sl = 7
    while sl > 2:
        print(" " * sp + "/" * sl)
        sl -= 1
        sleep(0.4)
    
    print("\n")
    sleep(0.4)





if __name__ == '__main__':

    print("Booting up...")
    print("This is the manual script for running Astroplex's scraper for the chatterbox.")
    sleep(1.5)
    print("Its name is Charlie.")
    sleep(1.5)
    draws_C_H_A_R_L_I_E()

    reddit = 0
    # reddit = praw.Reddit(client_id='sandwich', \
    #                  client_secret='robocopWasAdinosaur', \
    #                  user_agent='CharlieTheAutisticScraperBot v1.0 (by /u/nultero)', \
    #                  username='insert own name here', \
    #                  password='turtles')
    if reddit == 0:
        while True:
            print("\n")
            print("Charlie has detected that you have not set up a reddit dev account,")
            print("which you WOULD have set if you were looking through the sauce code and saw this")
            print("\n")
            print("Unfortunately, Charlie cannot scrape reddit, and ergo, function unless")
            print("you rewrite my code comment template to suit your own reddit dev credentials")
            print("\n")
            print("Till then, sayonara")
            break
    elif reddit != 0:
        main_menu_log()


    # # if n == 1:
    # #     SubredditScraper('VXJunkies', lim=970, mode='w', sort='hot').get_posts()
    # #     SubredditScraper('swoleacceptance', lim=970, mode='w', sort='hot').get_posts()
    # #     SubredditScraper('neckbeardRPG', lim=970, mode='w', sort='hot').get_posts()

    # # elif n == 2:
    # #     SubredditScraper('CrusaderKings', lim=970, mode='w', sort='hot').get_posts()
    # #     SubredditScraper('worldbuilding', lim=970, mode='w', sort='hot').get_posts()

    # # elif n == 3:
    # #     SubredditScraper('wallstreetbets', lim=970, mode='w', sort='hot').get_posts()

    # # elif n == 4:
    # #     SubredditScraper('redditsmuseumoffilth', lim=2000, mode='w', sort='hot').get_posts()

    # elif n == 5:
        
    #     vxj_t = TextRunner("VXJunkies")
    #     vxj_t.magic_bot()


    # elif n == 6:

    #     sql_df = pd.DataFrame(pd.read_csv("VXJunkies_posts.csv")) 
    #     # print(sql_df)
    #     # col_ids_to_print = sql_df['id'].tolist()
        
    #     # print(col_ids_to_print)
    #     ###  alright, so this worked
    #     ###  need a way to check the IDs to iterate and only grab uniques
    #     # vxj = DatabaseJanitor("VXJunkies")
    #     # conn = vxj.create_connection(database)
    #     # vxj.create_table(conn)


    #     datum_dt = [] #ids
    #     # datum_2 = [] titles??
    #     # datum_3 = [] #selftext and comments
    #     for index, row in sql_df.iterrows():
            
    #         #need to put a limiter in so you can test the sql db more easily

    #         if row["id"] and row["title"] and row["selftext"] and row["comments"] not in datum_dt:
    #             try:
    #                 d_1 = row["title"]
    #                 d_2 = row["selftext"]
    #                 d_3 = row["comments"]
    #                 #t = open(f"{self.sub}_pracfile.txt", "a")
    #                 t = open("VXJunkies_pracfile.txt", "a")
    #                 t.write(f"{d_1}" + "\n" + f"{d_2}" + "\n" + f"{d_3}" + "\n")
    #                 t.close()
                    
    #                 print(row["id"], row["title"])

    #             except UnicodeEncodeError:
    #                  continue
                
    #         else:
    #             print("One (1) row in the opened CSV has been skipped over.")
    #             continue
            
            

    #     print("Database file updated.")

    # elif n == 7:
    #     SubredditScraper('pathofexile', lim=970, mode='w', sort='hot').get_posts()


# print("This is the manual script for running Astroplex's scraper for the chatterbox.")
# print(main_menu_log())



#so right now I just want a menu to specify manually which subreddits to export
# don't want this automated yet, because each subreddit has a variable activity level and
# I don't necessarily want to have to set those timeframes right now — all's I am gonna do is make it bespoke for rn


# * will have to cut my previous buttons template to shape, but can see where I was going with this nonetheless



#####################
#function for repeated sub rewrites --- pass the args in as subs, each will write to a defined dict for pandas export
#####################

# def subscr_function(sub_var, sub_fetch_limit, sub_wr_destination, sub_cmts_dest):

#     ##dicts to be written to will be announced here when I can get the comments to populate properly

#     for submission in sub_var(limit=sub_fetch_limit):

#         f = open(sub_wr_destination, "a")
#         f.write(submission.title + "\n")
#         f.close()

#     for top_level_comment in submission.comments:

#         c = open(sub_cmts_dest, "a")
#         c.write(top_level_comment.body + "\n")
#         c.close()
    

#####################
#subs and their vars
#####################

# # r/VXJunkies subhead
# vxj = reddit.subreddit("VXJunkies")
# vxj_hot = vxj.hot
# vxj_top = vxj.top

# # r/swoleacceptance
# swa = reddit.subreddit("swoleacceptance")
# swa_hot = swa.hot
# swa_top = swa.top

# while True:
    
#     try:
#         n = int(input())

#         if n == 1:

#             print(reddit.user.me())

#             break

#         elif n == 2:

#             #     #     for submission in vxj_hot(limit=150):
#             #     #
#             #     #           f = open("vxj_hot_titles.txt", "a")
#             #     #           f.write(submission.title + " ")
#             #     #           f.close()
#             #     #
#             #     #           for top_level_comment in submission.comments:
#             #     #
#             #     #               c = open("vxj_hot_comments.txt", "a")
#             #     #               c.write(top_level_comment.body + " ")
#             #     #               c.close()
#             #     #
#             #     #
#             #     #
#             #     #
#             #     #
#             #     #
#             #     #
#             #     #
#             #     # the above was first attempt at the scrape script
#             #     #   overall janky and does not oblige DRY
#             #     #   comments are jacked up and I can't seem to get them to scrape BOTH title and comments, seems to be only one or the other
#             #     #   think it has something to do with reddit's comment "forest" attributes, so there's a *towards data science* resource that I'm going to look into
#             #     #
#             #     #
#             #     # for the moment, I've created a function to pass in sub args, so I have an easy DRY way to specify new subs rather than Ctrl+C, Ctrl+V
#             #     #
#             #     #  I'm gonna keep BTN3 open for now, so I can use that to test whether the comments I grab are the full amount or not


#             else:
                
#                 break


#         elif n == 3:

#             for submission in vxj_top(limit=800):

#                 f = open("vxj_top_titles.txt", "a")
#                 f.write(submission.title + " ")
#                 f.close()

#                 for top_level_comment in submission.comments:

#                     c = open("vxj_top_comments.txt", "a")
#                     c.write(top_level_comment.body + " ")
#                     c.close()

#                     break

#             else:
                    
#                 break
            
#         elif n == 4:
         
#             subscr_function(swa_hot, 150, "swoleacc_hot_titles.txt", "swoleacc_hot_comments.txt")
#             #works like a charm for titles, but still doesn't fully populate comments for me yet
            
#         elif n == 5:

#            for submission in swa_hot(limit=15):
#                print(submission.title)
#                #was making sure I was writing format correctly — this is gtg, so the rest should work
               
                
#         elif n == 6:

#             print("Logging out, captain...")
#             break
          
#         elif n > 6 or n < 1:
#             print("The number you've entered doesn't match with one of my options.")
            
#     except ValueError:
#         print("Invalid entry; a numerical value was required.")
#         break