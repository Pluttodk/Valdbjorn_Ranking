import os, dotenv, discord
from dataclasses import dataclass

@dataclass
class MediaReview:
    media_type: str
    title: str
    score: int
    bonus_point: int
    review: str


class Ranking(discord.Client):
    SUPPORTED_MEDIA_TYPES = [
        "movie",
        "show",
        "book",
        "game",
        "boardgame",
        "other"
    ]

    def format_review(self, media_review: MediaReview) -> str:
        """
        Formats the review in a neat way
        """
        map_bonus_point = "⬆️" if media_review.bonus_point > 0 else "⬇️" if media_review.bonus_point < 0 else ""
        formatted_review = f"**{media_review.media_type} Review:**\n" \
                           f"**Title:** {media_review.title}\n" \
                           f"**Score:** {media_review.score} {map_bonus_point} / 5 \n" \
                           f"**Review:**\n{" ".join(media_review.review)}"
        return formatted_review
    
    def message_help(self):
        """
        A message to help identify how to use the app
        """
        return """
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
        """

    async def on_message(self, msg : discord.Message):
        """
        Checks the message that is receiver to check if it is a review
        
        The review should follow the format as below:
        !review MediaType: "Title of the content" <Score + Optional[Emoji]> <Text Review>
        """

        # Avoid infinite loop
        if msg.author == self.user:
            return
        
        if msg.content.startswith("!review"):
            # Parse the review
            try:
                review_content = msg.content.split(" ")

                if len(review_content) >= 5:
                    media_type = review_content[1][:-1]
                    if media_type.lower() not in self.SUPPORTED_MEDIA_TYPES:
                        raise ValueError("Unsupported media type")

                    # Extracting the title within quotes
                    title = msg.content[msg.content.find('"')+1:msg.content.rfind('"')]

                    post_title_content = msg.content.split('"')[-1].split(" ")[1:]
                    print(post_title_content)

                    supported_emojis = ("⬆️", "⬇️")
                    review_txt = ""
                    if post_title_content[1] in supported_emojis or post_title_content[0][1:] in supported_emojis:
                        if post_title_content[1] in supported_emojis:
                            review_txt = post_title_content[2:]
                            emoji = post_title_content[1]
                        else:
                            review_txt = post_title_content[1:]
                            emoji = post_title_content[0][1:]
                        bonus_point = -1 if emoji == "⬇️" else 1
                    else:
                        bonus_point = 0
                        review_txt = post_title_content[1:]

                    score = int(post_title_content[0][0])
                    
                    # Create MediaReview object
                    media_review = MediaReview(media_type, title, score, bonus_point=bonus_point, review=review_txt)
                    
                    # Now you can do whatever you want with media_review object
                    await msg.channel.send(self.format_review(media_review))
                    return
            except Exception as e:
                # Some misformed message. Send help!
                await msg.channel.send(self.message_help())
                print(e)
                raise e
                return
            await msg.channel.send(self.message_help())


if __name__ == "__main__":
    dotenv.load_dotenv()

    intents = discord.Intents.default()
    intents.message_content = True

    client = Ranking(intents=intents)
    client.run(os.getenv("DISCORD_TOKEN"))