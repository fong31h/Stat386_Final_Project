import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

artists = pd.read_csv('artists.csv', index_col=None)
st.title('Musical Artists')
st.table(artists.head(7))

with st.expander("View full table"):
    st.table(artists)
st.header('Which factors affect the popularity of artists?')
st.subheader('Factor 1: Age')
fig, axs = plt.subplots(1, 2, figsize=(11,5))
plt.subplot(1,2,1)
plt.title('Age since first album against listeners and playcount,' 
          ' respectively')
sns.regplot(data=artists, 
                         x='age (since 1st album)', y='listeners',
                         color = '#17205e')
plt.ylabel('Listeners (millions)')
plt.subplot(1,2,2)
sns.regplot(data=artists, x='age (since 1st album)', y = 'playcount',
            color = '#1f420d')
plt.ylabel('Play count (billions)')
st.pyplot(fig)
st.caption('Interestingly, age correlates with increased'
           ' listeners, while having no correlation at all'
           ' with play count')
st.subheader('What if we partition the time frames differently?')
st.markdown('I split the years into three periods with a similar'
            ' amount of artists')
fig, axs = plt.subplots(3, 2, figsize=(6,9))
plt.subplot(3,2,1)
plt.title('2016-2023, n=108')
sns.regplot(data=artists[artists['age (since 1st album)'] < 8], 
                x='age (since 1st album)', y='listeners',
                color='#278ad6')
plt.ylabel('listeners (millions)')
plt.subplot(3,2,2)
sns.regplot(data=artists[artists['age (since 1st album)'] < 8], 
                x='age (since 1st album)', y='playcount',color='#278ad6')
plt.ylabel('playcount (hundreds of millions)')
plt.subplot(3,2,3)
plt.title('2002-2015, n=121')
sns.regplot(data=artists[(artists['age (since 1st album)'] >= 8) & 
                        (artists['age (since 1st album)'] <= 21)], 
                x='age (since 1st album)', y='listeners',color='#aa27d6')
plt.ylabel('listeners (millions)')
plt.subplot(3,2,4)
sns.regplot(data=artists[(artists['age (since 1st album)'] >= 8) & 
                        (artists['age (since 1st album)'] <= 21)], 
                x='age (since 1st album)', y='playcount',color='#aa27d6')
plt.ylabel('playcount (billions)')
plt.subplot(3,2,5)
plt.title('1946-2001, n=114')
sns.regplot(data=artists[artists['age (since 1st album)'] > 21], 
                x='age (since 1st album)', y='listeners')
plt.ylabel('listeners (millions)')
plt.subplot(3,2,6)
sns.regplot(data=artists[artists['age (since 1st album)'] > 21], 
                x='age (since 1st album)', y='playcount')
plt.ylabel('playcount (hundreds of millions)')
plt.tight_layout()
st.pyplot(fig)
st.caption('These plots mostly confirm our idea that age correlates with'
           ' increased listeners but not increased playcount.'
           ' However, based on the fifth plot, it seems that after a certain'
           ' upper limit, age no longer correlates with increased listeners' 
           ' either.')
st.markdown('Based on our plots, it appears that with some limits,' 
            ' age is a moderately accurate predictor for one aspect'
            ' of popularity.')
selected_year = st.select_slider('Year', np.sort(artists['age (since 1st album)'].unique())
                        , value=20)
st.markdown('We can also examine years individually with a slider.'
            ' unfortunately, streamlit runs too slow to be able to '
            ' quickly run the slider through and get a feel for the '
            ' trend, but with some patience we can see the trend '
            'of listeners increasing with time.')
fig, axs = plt.subplots(1,2,figsize=(10,5))
plt.subplot(1,2,1)
plt.ylim(0, 7500000)
sns.barplot(data=artists[artists['age (since 1st album)'] == selected_year], 
                x='age (since 1st album)', y='listeners',color='#d6274a')
plt.subplot(1,2,2)
plt.ylim(0,2000000000)
sns.barplot(data=artists[artists['age (since 1st album)'] == selected_year], 
                x='age (since 1st album)', y='playcount',color='#d6274a')
st.pyplot(fig)
st.subheader('Factor 2: Sex')
st.markdown('I labeled the artists as male, female, male band,'
            ' female band, or male/female band.')
palette = sns.set_palette('Set2')
fig, axs = plt.subplots(1, 2, figsize=(11,5))
plt.subplot(1,2,1)
plt.title('Boxplot of sex vs listeners and playcount respectively')
sns.boxplot(data=artists, 
                         x='sex', y='listeners',palette=palette)
plt.ylabel('Listeners (millions)')
plt.subplot(1,2,2)
sns.boxplot(data=artists, x='sex', y = 'playcount',palette=palette)
plt.ylabel('Play count (billions)')
st.pyplot(fig)
st.caption("From these two boxplots, it seems that male bands seem to have"
           " both the highest listeners and playcount, although the playcount"
           " plot is a little hard to read because of the outliers and "
           " the variance appears to be much smaller.")
st.markdown('If sex was not a factor in popularity, we would expect there'
            ' to be little to no difference in the means. Because we'
            ' do see variance, it implies that sex is a factor in some'
            ' way. That being said, it is possible that sex is simply'
            ' correlated with some other factor that is actually causal.')
st.subheader('Factor 3: Genre')
st.markdown('Genre was difficult to work with because there are so'
            ' many unique genres. To deal with that, I chose the 10'
            ' most popular genres.')
genres_total = artists['genre1'].value_counts() + (
    artists['genre2'].value_counts()) + (
    artists['genre3'].value_counts())
genres_total = genres_total.dropna()
top_10_genres = pd.DataFrame(genres_total[genres_total > 24].sort_values())
top_10_genres = top_10_genres.rename(columns={0:'count'}).reset_index()
fig, axs = plt.subplots(1,1, figsize=(10, 5))
sns.barplot(data=top_10_genres, x='index', y='count',palette=palette)
plt.xticks(rotation=45, ha="right")
plt.xlabel('Genre')
plt.ylabel('# of Artists')
st.pyplot(fig)
st.markdown('To explore genre, we can select one of the ten genres at a'
            ' to see the playcount and listeners averages')
indiv_genres = []
for genre in top_10_genres['index']:
    indiv_genres.append(artists[(artists['genre1'] == genre) | 
                                (artists['genre2'] == genre) | (
    artists['genre3'] == genre)])
for i in range(len(indiv_genres)):
    indiv_genres[i]['main_genre'] = top_10_genres['index'].loc[i]
top_10_full = pd.concat(indiv_genres)
selected_genre = st.selectbox('Select a genre', top_10_genres['index'])

listeners = top_10_full[top_10_full['main_genre'] == selected_genre]['listeners'].mean()
playcount = top_10_full[top_10_full['main_genre'] == selected_genre]['playcount'].mean()
df = pd.DataFrame({'listeners':[round(listeners)], 'playcount':[round(playcount)]})
st.markdown('Average listeners and playcount')
st.dataframe(df)
fig, axs = plt.subplots(1,2,figsize=(13, 4))
plt.subplot(1,2,1)
sns.boxplot(data=top_10_full, x='main_genre', y='listeners',palette=palette)
plt.ylabel('listeners (millions)')
plt.xticks(rotation=45, ha="right")
plt.subplot(1,2,2)
sns.boxplot(data=top_10_full, x='main_genre', y='playcount',palette=palette)
plt.ylabel('Play count (billions)')
plt.xticks(rotation=45, ha="right")
st.pyplot(fig)
st.caption('Genre too appears to be a factor in the popularity of '
           ' artists. Once again though, playcount appears to be much'
           ' less variable than listeners.')
st.subheader('Conclusion')

st.markdown('In conclusion, although EDA is not meant to draw '
            'definitive conclusions from data, a few ideas that one '
            'explore further with this data are which factors most influence'
            ' listeners total, and what factors, if any,'
            ' affect playcount total. While we found three factors that'
            ' seem to clearly affect listeners, none of the three seemed'
            ' to provide a strong explanation for playcount.')