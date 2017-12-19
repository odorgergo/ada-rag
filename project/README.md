# For the project's 3rd milestone

Please visit https://odorgergo.github.io/ada-rag/ to view our visualisation of monthly tweet counts, and http://nbviewer.jupyter.org/github/odorgergo/ada-rag/blob/master/project/dist_of_tweets_new.ipynb to view our notebook. The notebook itself is at project/dist_of_tweets.ipynb . Additionally, our final report may be found at https://github.com/odorgergo/ada-rag/blob/master/paper/main.pdf .

# Abstract

Twitter is a tremendously popular social network (also notorious if you count Donald Trump's account), based on 140 character pieces of text called "tweets". Twitter has not only been used in a more personal capacity, but also in the direction of political agendas and activism.

The Swiss tweets dataset offers many intriguing questions, especially given the fact that it has geolocation tags. First of all, the locations allow us to understand how Swiss tweeters are distributed throughout the country. Secondly, given Switzerland's relatively rare status as a country with multiple official languages, tweets by Swiss users offer a unique opportunity to gain insight into the relationship between the languages, contents, and locations of tweets. In addition, an analysis of Swiss political activity on Twitter allows us to find out how much Switzerland has embraced this social media platform.
In this project we have striven to find answers for, or gain insights into, the following research questions:

# Research questions

- Does the density of the location of tweets correspond to population densities? Or are the tweets significantly more concentrated in cities?
- Can we reconstruct the Röstigraben only based on the language of tweets?
- Are there any spikes in activity and do they correspond to particular events (e.g. referendums) 
- How involved are swiss people in politics on twitter? Which areas are most involved?

# Dataset

We have used the Swisscom swiss tweets dataset. We have also used population density data from https://www.admin.ch/ .

# What we have done

- We have visualised the number of tweets written in each month and the total number of tweets in each municipality.
- We have reconstructed the Röstigraben by creating a map with each municipality's dominant tweeting language among the three official languages being shown.
- We have shown that, contrary to our intuition, the dataset indicates that Swiss urban areas are under-represented in Twitter: the number of distinct users in a municipality divided by municipality population is negatively correlated with population density of the municipality.
- We have shown that the dataset seems to indicate that French-speaking Switzerland is more active than German-speaking Switzerland, and also that tweeting in English is very commonplace.
- We have proposed, and implemented, a bootstrapping method for the retrieval of political tweets. A visualisation of the distribution of tweets collected using our method over time allows us to detect significant political events based on spikes in Twitter political activity. Our results indicate that this method is superior to a purely supervised method using tweets made by known politician accounts.
