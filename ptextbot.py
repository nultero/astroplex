#! usr/bin/env python3


import praw # for Charlie the scraper, the reddit shovel to dig up dirt
import pandas as pd # Charlie's dumping ground, indexing
import numpy as np 
import tensorflow as tf
import os
import time
from time import sleep # works as a timer so you don't lock out reddit's request limiter
from os.path import isfile
import random # not 100% necessary, but since scraping takes awhile I use this as a spinny loader
import sqlite3
from sqlite3 import Error



#global db var for my bot homies to dump into
database = (r"/have_to_reset_db")


def main_menu_log():

    print("   Enter '1' to verify and print if user logged")
    print("   Enter '2' to scrape r/VXJunkies")
    print("   Enter '3' to scrape r/swoleacceptance")
    print("   Enter '4' to scrape r/neckbeardRPG")
    print("   Enter '5' to scrape r/FloridaMan")
    print("   Enter '6' to etc")
    print("What would you like to do?")

#this function doesn't do anything serious,
#I just like having visual feedback for running these
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
        print("There was only a 1 percent chance of printing this")



















class TextRunner:

    def __init__(self, sub):

        self.sub = sub
        print(f"Text Runner model has been initialized for r/{self.sub}")

    def vector_text(self):

        path = os.getcwd()
        text = open(path + f"/{self.sub}_practicefile.txt", "r").read()

        vocab = sorted(set(text))

        char2idx = {u:i for i, u in enumerate(vocab)}
        idx2char = np.array(vocab)
        text_as_int = np.array([char2idx[c] for c in text])

        seq_length = 60
        #####examples_per_epoch = len(text)//(seq_length+1)

        char_dataset = tf.data.Dataset.from_tensor_slices(text_as_int)

        sequences = char_dataset.batch(seq_length+1, drop_remainder=True)
        for item in sequences.take(5):
            print(repr(''.join(idx2char[item.numpy()])))

        

    



















class DatabaseJanitor:

    def __init__(self, sub):

        self.sub = sub
        print(f"Database Janitor (Mr. SQL) has been initialized for r/{self}")


    def create_connection(self, db_file):
        
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(sqlite3.version)
            return conn
        except Error as e:
            print(e)

        return conn

    def create_table(self, conn):

        create_table_sql = f""" CREATE TABLE IF NOT EXISTS {self.sub} (
                        id text PRIMARY KEY,
                        title text,
                        body text
                        );"""

        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        
        except Error as e:
            print(e)

    def insert_datum(self, conn, datum_1, datum_2, datum_3):

        sql = f""" INSERT INTO {self.sub} (Id, Title, Body)
                    VALUES('{datum_1}','{datum_2}','{datum_3}'); """

        datum = datum_1, datum_2, datum_3
        c = conn.cursor()
        c.execute(sql, datum)
        return c.lastrowid






















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
                        fetch_a_spin()
                
                    post.comments.replace_more(limit=0)
                    for comment in post.comments.list():
                        unique_comment_id = comment.id not in tuple(df.id) if csv_loaded else True

                        if unique_comment_id:
                            sub_dict['comments'].append(comment.body)
                            sub_dict['id'].append(comment.id)
                            print("@@")
            sleep(0.12)
            print("####")

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






















if __name__ == '__main__':

    reddit = praw.Reddit(client_id='porque no los dos', \
                     client_secret='thinkitmightbetoefungus', \
                     user_agent='CharlieTheAutisticScraperBot v1.0 (by /u/nultero)', \
                     username='nultero', \
                     password='crapplesnatch')

    print("This is the manual script for running Astroplex's scraper for the chatterbox.")
    print(main_menu_log())

    n = int(input())

    if n == 1:
            print(reddit.user.me())

    elif n == 2:
        SubredditScraper('VXJunkies', lim=1750, mode='w', sort='hot').get_posts()

    elif n == 3:
        SubredditScraper('swoleacceptance', lim=1750, mode='w', sort='hot').get_posts()

    elif n == 4:
        SubredditScraper('neckbeardRPG', lim=1750, mode='w', sort='hot').get_posts()
    
    elif n == 5:
        SubredditScraper('FloridaMan', lim=997, mode='w', sort='hot').get_posts()



    elif n == 6:

        sql_df = pd.DataFrame(pd.read_csv("VXJunkies_posts.csv")) 
        # print(sql_df)
        # col_ids_to_print = sql_df['id'].tolist()
        
        # print(col_ids_to_print)
        ###  alright, so this worked
        ###  need a way to check the IDs to iterate and only grab uniques
        vxj = DatabaseJanitor("VXJunkies")
        conn = vxj.create_connection(database)
        vxj.create_table(conn)


        datum_dt = [] #ids
        # datum_2 = [] titles??
        # datum_3 = [] #selftext and comments
        for index, row in sql_df.iterrows():
            
            #need to put a limiter in so you can test the sql db more easily

            if row["id"] and row["title"] and row["selftext"] and row["comments"] not in datum_dt:
                try:
                    d_1 = row["title"]
                    d_2 = row["selftext"]
                    t = open("pracfile.txt", "a")
                    t.write(f"{d_1}" + f"{d_2}" + "\n")
                    t.close()
                    
                    print(row["id"], row["title"])

                except UnicodeEncodeError:
                     continue
                
            else:
                print("One (1) row in the opened CSV has been skipped over.")
                continue
            
            

        print("Database file updated.")


    elif n == 7:
        
        vxj_t = TextRunner("VXJunkies")
        vxj_t.vector_text()




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