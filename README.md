# Valdbjorn Ranking

My Wife and I love ranking almost everything we do in our life

This little bot servers the nice simply task to Scan our messages in Discord and store them in a DB.

**How to Use the App:**

To submit a review, use the following format:
```
!review <Media Type>: "<Title>" <Score> ⬆️/⬇️ <Review>
```

Example:
```
!review Movie: "Home Alone" 4 ⬆️ Den var virkelig hyggelig
```

Replace `<Media Type>` with the type of media you're reviewing (e.g., Movie, Book, Game).
Replace `<Title>` with the title of the media enclosed in double quotes.
Replace `<Score>` with your rating score.
Use ⬆️ for positive reviews and ⬇️ for negative reviews.
Write your review after the score and icon.

**Supported types**
- Movies
- Books
- TV-Shows
- Board games
- Other
    - These are simply a bucket for stuff that can not be checked up against anything. If more types are added later, than this should be expanded

## How to run:

The tool uses [pdm](https://pdm-project.org/en/latest/) for package managing, and pyenv for the specific python version

In order to run it with your own agent: 
1) Create an agent at [https://discord.com/developers](https://discord.com/developers) 
2) Create a `.env` file and paste the bots token in format as below:
```
DISCORD_TOKEN=<INSERT TOKEN>
```