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
st.header('Research Question: Does age help the popularity of artists?')
fig, axs = plt.subplots(1, 2, figsize=(10, 6))
plt.subplot(1,2,1)
sns.regplot(data=artists, 
                         x='age (since 1st album)', y='listeners')
plt.ylabel('Listeners (millions)')
plt.subplot(1,2,2)
sns.regplot(data=artists, x='age (since 1st album)', y = 'playcount')
plt.ylabel('Play count (billions)')
st.pyplot(fig)
st.caption('Interestingly, age correlates with increased'
           ' listeners, while having no correlation at all'
           ' with play count')
st.subheader('What if we partition the time frames differently?')

