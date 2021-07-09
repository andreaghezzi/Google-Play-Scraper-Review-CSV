# Google-Play-Scraper-Review-CSV
<b>Python script </b> that allows you to download the reviews of applications from the google play store and save them in a .csv file.
In my case, I download reviews for multiple applications, in different languages.
Each application review in a language is saved in a different .csv file that will have the name: applicationName_language.csv.
In the case of Whatsapp, I downloaded 6'198'508 reviews and saved them in the whatsapp_en.csv file with a weight of 890Mb, I have saved only the ID of the review, UserName of who wrote the review, Score and content of the review. I am also making this dataset available.
The structure of the reviews that will be downloaded is as follows:
<ul>
<li>["UserName"] = "Andrea Ghezzi"</li>
<li>["userImage"] = "https://lh3.googleusercontent.com/-cVEHKr*******"</li>
<li>["ContentReview"] = "This is literally the best idle game I have ever played. The penguins waddle around and live their best lives in the cutest little outfits."</li>
<li>["Score"] = 5 </li>
<li>["thumbsUpCount"] = 54</li>
<li>["reviewCreatedVersion"] = "1.16"</li>
<li>["at"] = datetime.datetime(2020, 2, 24, 17, 19, 34) </li>
<li>["replyContent"] = "Hello, We will gradually improve the various systems in the game to enhance the player's game experience."</li>
<li>["repliedAt"] = datetime.datetime(2020, 2, 24, 18, 30, 42)</li>
<li>["reviewId"] = "gp:AOqpTOE0Iy5S9Je1 ****** " </li>
</ul>
