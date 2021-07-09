from google_play_scraper import Sort, reviews_all
import os
import sys
import csv

#key dictionary = application name, value = application id on google play store (https://play.google.com/store/apps/details?id=com.facebook.lite&hl=it&gl=US in this case the ID is com.facebook.lite)
app_id = {'telegram':'org.telegram.messenger', 'messanger':'com.facebook.orca'}
#app_id = {'Everbridge':'com.everbridge.mobile.iv.recipient','whatsapp':'com.whatsapp', 'telegram':'org.telegram.messenger', 'messanger':'com.facebook.orca','hangsout':'com.google.android.talk', 'discord':'com.discord', 'WeChat':'com.tencent.mm','GTL':'air.com.renovo.vismobile'}
languages = ['en','it','fr','ru','es'] #lista per scegleire poi le lingue, nel mio caso mi occorrono solo queste
for app in app_id:
    print("Download the reviews related to " + app)
    for lan in languages:
        dictionaries = reviews_all(
            app_id[app], # id of application
            sleep_milliseconds = 0,
            lang = lan, # default en
            count = 200 #default 100 (number of request)
        )

        #I remove all information redundant to me, leaving only username, rating, comment and the ID of the review with DEL
        cnt = 0
        for i in dictionaries:
            cnt += 1
            del i["userImage"]
            del i["thumbsUpCount"]
            del i["reviewCreatedVersion"]
            del i["at"]
            del i["replyContent"]
            del i["repliedAt"]
        print("Dataset " + app + "_" + lan + ": " + str(cnt) + " occurences")

        if(cnt == 0): # if there are no reviews in the desired language, I continue otherwise it freezes
            continue

            keys = dictionaries[0].keys()

            #I create a csv file for each application present in app_id
            a_file = open(app+"_"+lan+".csv", "w")
            dict_writer = csv.DictWriter(a_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(dictionaries)
