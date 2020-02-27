#! usr/bin/env python3

import praw
import pandas as pd

def main_menu_log():

    print("   Enter '1' to verify and print if user logged")
    print("   Enter '2' to scrape VXJ / hot")
    print("   Enter '3' to scrape VXJ / top")
    print("   Enter '4' to scrape swoleacceptance / hot")
    print("   Enter '5' to etc")
    print("   Enter '6' to etc")
    print("What would you like to do?")




print("This is the manual script for running Astroplex's scraper for the chatterbox.")
print(main_menu_log())



#so right now I just want a menu to specify manually which subreddits to export
# don't want this automated yet, because each subreddit has a variable activity level and
# I don't necessarily want to have to set those timeframes right now — all's I am gonna do is make it bespoke for rn


# * will have to cut my previous buttons template to shape, but can see where I was going with this nonetheless


reddit = praw.Reddit(client_id='wangdangle', \
                     client_secret='tunglebungle', \
                     user_agent='CharlieTheAutisticScraperBot v1.0 (by /u/nultero)', \
                     username='nultero', \
                     password='hunter2lol')



#####################
#function for repeated sub rewrites --- pass the args in as subs, each will write to a defined dict for pandas export
#####################

def subscr_function(sub_var, sub_fetch_limit, sub_wr_destination, sub_cmts_dest):

    ##dicts to be written to will be announced here when I can get the comments to populate properly

    for submission in sub_var(limit=sub_fetch_limit):

        f = open(sub_wr_destination, "a")
        f.write(submission.title + "\n")
        f.close()

    for top_level_comment in submission.comments:

        c = open(sub_cmts_dest, "a")
        c.write(top_level_comment.body + "\n")
        c.close()
    




#####################
#subs and their vars
#####################

# r/VXJunkies subhead
vxj = reddit.subreddit("VXJunkies")
vxj_hot = vxj.hot
vxj_top = vxj.top

# r/swoleacceptance
swa = reddit.subreddit("swoleacceptance")
swa_hot = swa.hot
swa_top = swa.top





#do we need a dict for subs?








while True:
    
    try:
        n = int(input())

        if n == 1:

            print(reddit.user.me())

            break
          #
          #
          #
          #
          #
          #
          #


          

        elif n == 2:

            #     #     for submission in vxj_hot(limit=150):
            #     #
            #     #           f = open("vxj_hot_titles.txt", "a")
            #     #           f.write(submission.title + " ")
            #     #           f.close()
            #     #
            #     #           for top_level_comment in submission.comments:
            #     #
            #     #               c = open("vxj_hot_comments.txt", "a")
            #     #               c.write(top_level_comment.body + " ")
            #     #               c.close()
            #     #
            #     #
            #     #
            #     #
            #     #
            #     #
            #     #
            #     #
            #     # the above was first attempt at the scrape script
            #     #   overall janky and does not oblige DRY
            #     #   comments are jacked up and I can't seem to get them to scrape BOTH title and comments, seems to be only one or the other
            #     #   think it has something to do with reddit's comment "forest" attributes, so there's a *towards data science* resource that I'm going to look into
            #     #
            #     #
            #     # for the moment, I've created a function to pass in sub args, so I have an easy DRY way to specify new subs rather than Ctrl+C, Ctrl+V
            #     #
            #     #  I'm gonna keep BTN3 open for now, so I can use that to test whether the comments I grab are the full amount or not


            else:
                
                break


        elif n == 3:

            for submission in vxj_top(limit=800):

                f = open("vxj_top_titles.txt", "a")
                f.write(submission.title + " ")
                f.close()

                for top_level_comment in submission.comments:

                    c = open("vxj_top_comments.txt", "a")
                    c.write(top_level_comment.body + " ")
                    c.close()

                    break

            else:
                    
                break
            
        elif n == 4:
         
            subscr_function(swa_hot, 150, "swoleacc_hot_titles.txt", "swoleacc_hot_comments.txt")
            #works like a charm for titles, but still doesn't fully populate comments for me yet
            
        elif n == 5:

           for submission in swa_hot(limit=15):
               print(submission.title)
               #was making sure I was writing format correctly — this is gtg, so the rest should work
               
                
        elif n == 6:

            print("Logging out, captain...")
            break
          
        elif n > 6 or n < 1:
            print("The number you've entered doesn't match with one of my options.")
            
    except ValueError:
        print("Invalid entry; a numerical value was required.")
        break
