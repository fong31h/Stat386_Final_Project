## Introduction and Motivation

The topic of this project is music, specifically, mainstream musical artists of all different genres. In exploring this topic, I hoped to
understand better what makes musical artists popular.

## Methods

To find data that would allow me to explore this question, I spent time searching the web for websites or APIs that had relevant data. I found one API, last.fm, that contained such information as genre, listeners, and playcount, and concert status (whether or not they are on tour) Data on age and sex I was forced to find manually, unfortunately. Since last.fm has an API, there were no ethical concerns in gathering this data. Navigating the API itself took a little bit of practice, and the data itself was not particularly clean when it came in. I spent time learning the structure of the data so that I could turn it into a tidy data frame. One area where I was forced to make a subjective decision was in handling the genres category. Because each musician had a differing number of genres associated with their music, I was forced to simply select the top three from each musician.

## Results

In performing the EDA, the most significant result that I discovered is that the listeners total is quite variable, it responds to age, sex, and genre in quite significant ways. Listeners seemed to increase with age, and there were clear differences in the means of listeners depending on sex and genre. On the other hand, playcount was stubbornly non-variable. No matter which way the data was sliced, on average, playcounts did not differ from one another. In other words, if I compared all old male bands to all young female solo artists, there wasn't a noticeable difference in average playcounts. It seems that playcounts is either completely random, or there are other factors which my data did not capture that affect it.

## Conclusion

The data collection and EDA were both very relevant and helpful in answering my research question. Without the categorical data on sex, genre, and age, I would not have been able to explore the different factors that affect popularity. At the same time, the quantitative data on playcout and listeners was absolutely vital as a concrete method for measuring popularity.

Overall, I feel this project is significant for anyone who enjoys exploring music and culture. Popular music shapes our culture in very significant ways and what makes an artist popular or not is valuable information for understand trends.

## Dashboard Link

https://stat386finalproject-7tr6hrcyblxbmipa6cm5fd.streamlit.app/