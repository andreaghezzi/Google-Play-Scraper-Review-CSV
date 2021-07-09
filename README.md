# Google-Play-Scraper-Review-CSV
<p> <b>Python script </b> that allows you to download the reviews of applications from the google play store and save them in a .csv file. </p>
<p> In my case, I download reviews for multiple applications, in different languages.
 Each application review in a language is saved in a different .csv file that will have the name: applicationName_language.csv. </p>
<p> In the case of Everbridge application, I downloaded 701 reviews and saved them in the Everbridge_en.csv file with a weight of 150Kb, I have saved only the ID of the review, UserName of who wrote the review, Score and content of the review. I am also making this dataset available. </p>

<h3> The structure of the reviews that will be downloaded is as follows: </h3>
<ul>
<li> <b>["UserName"] </b> = "Andrea Ghezzi"</li>
<li> <b>["userImage"] </b> = "https://lh3.googleusercontent.com/-cVEHKr*******"</li>
<li> <b>["ContentReview"] </b> = "This is literally the best idle game I have ever played. The penguins waddle around and live their best lives in the cutest little outfits."</li>
<li> <b>["Score"] </b> = 5 </li>
<li> <b>["thumbsUpCount"] </b> = 54</li>
<li> <b>["reviewCreatedVersion"] </b> = "1.16"</li>
<li> <b>["at"] </b> = datetime.datetime(2020, 2, 24, 17, 19, 34) </li>
<li> <b>["replyContent"] </b> = "Hello, We will gradually improve the various systems in the game to enhance the player's game experience."</li>
<li> <b>["repliedAt"] </b> = datetime.datetime(2020, 2, 24, 18, 30, 42)</li>
<li> <b>["reviewId"] </b> = "gp:AOqpTOE0Iy5S9Je1 ****** " </li>
</ul>
