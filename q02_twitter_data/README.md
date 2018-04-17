## Extract tweets 

In this assignment we will be creating a Utility function with the help of previous function to get the desired dataframe.

## Write a function `q02_twitter_data` that :
- Calls previous function and extracts the tweets of `NarendraModi` using tweepy's `user_timeline` method.
- Creates a Dataframe consisting of the following information(as features) extracted from the tweets
  - Lenght of the tweets.
  - ID of the tweets.
  - Date the tweet has been posted.
  - Source of the tweets.
  - Likes per tweet recorded.
  - No. of retweets on a particular tweet recorded.


### Parameters:

This function takes in no argument.

### Returns:

| Return | dtype | description |
| --- | --- | --- | 
| data | pandas.core.frame.DataFrame | dataframe containg the follwing information mentioned above |
