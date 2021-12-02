import yfinance as yf
import streamlit as st
import pandas as pd
from io import StringIO  
[theme]
primaryColor="#F63366"
backgroundColor="#CCCCFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif"
st.write("""
# Simple Stonk Price App
Shown are the stonk closing price and volume of Google!
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'GOOGL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
uploaded_file = st.file_uploader("Choose a file")
'''
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)
agree = st.checkbox('I agree')
if agree:
   st.write('Great!')
genre = st.radio(
  "What's your favorite movie genre",
     ('Comedy', 'Drama', 'Documentary'))
if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn't select comedy.")
option = st.selectbox(
     'How would you like to be contacted?',
 ('Email', 'Home phone', 'Mobile phone'))
st.write('You selected:', option)
'''
if uploaded_file is not None:
    st.image(uploaded_file)
    st.balloons()