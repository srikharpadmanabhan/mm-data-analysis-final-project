# march-madness-data-analysis
I would like to analyze the dataset about “March Madness”, found here: https://www.kaggle.com/datasets/nishaanamin/march-madness-data/data . There are lots of files and the data is public and available. I have not had a chance to open each file, but I plan on doing a few general things. First, I hope to get summary statistics about every team. Because there are so many files, and so many categories, there are almost infinite possibilities for which statistics to measure. I can look at things such as which teams consistently outperform expectations, and which teams come short. I can look at how offensive performance varies by seeding. Because these files have data from 2008 - 2024, I can see how certain statistics have changed over time. Additionally, because the data is split between regular season (and even here, conference games and non-conference games) and postseason, I can look at how the data for certain teams changes in each situation, and how that predicts the results in the postseason.

With all of these numbers, I want to construct charts and other visuals that could guide me to seeing which statistics matter the most and then hopefully create a relatively simple, supervised learning neural network that takes those stats for 2 teams and predicts a winner, and hopefully has good results.


Execution plan:
* By the end of week 4, I will have explored the dataset and create dictionaries that store some abasic ggregated statistics in a pickled file
* By the end of week 5, I will have created python classes for things like Teams, Games, Conferences, Coaches, Players, and then write member functions for each, which will make the process of accumulating all the data from these files easier
* By the end of week 6, I will create many charts showing the historic performances of teams amd conferences in March Madness
* By the end of week 7, I will have run regressions on things like seed, power rating, conference stats, etc with the result of games (in this case probably the final score) to see what single metric predicts wins the best
* By the end of week 8, I will have created a basic neural network that will take in at least 8 of these stats I handpick based on the results above, and attempts to predict the final score.

Finally, I will use this model to predict new games for this upcoming season. Essentially I will run the model twice, once for each time and then see which team had the higher score predicted. I will also use this on a holdout set to validate that the network performs better than random.
