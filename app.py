import streamlit as st 
import pandas as pd
from PIL import Image


st.title('La mia App in python')
# st.markdown('Streamlit is **_really_ cool**.')#Display string formatted as Markdown.
# st.markdown("This text is :red[colored red], and this is **:blue[colored]** and bold.")
# st.markdown(":green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:")
st.subheader('Caricare i dati')

x = st.file_uploader('Upload a CSV')#upload 
df = pd.read_csv(x)#leggo

# y = st.file_uploader('Upload an Excel')#upload
# df2 = pd.read_excel(y)#leggo

if st.button('Carica csv'):#se clicco
    st.dataframe(df)#casto il df
# if st.button('Carica excel'):#se clicco
#     st.dataframe(df2)#casto il df
st.subheader('Caricare uno slice del df iniziale con pandas')
df1 = df.tail(5)#prime 5 righe
dfgroupby = df.groupby('company')['price']
st.dataframe(dfgroupby)
dfgroupby2 = df.groupby('company')['price'].max()
st.dataframe(dfgroupby2)

# misto = pd.concat([df,dfgroupby2])
# st.dataframe(misto)

 



# st.button('Click me')

# st.radio('Pick one', ['cats', 'dogs'])

# st.multiselect('Buy', ['milk', 'apples', 'potatoes'])

# st.slider('Pick a number', 0, 100)

# st.select_slider('Pick a size', ['S', 'M', 'L'])

# st.number_input('Pick a number', 0, 10)


# st.download_button('Download file', data= x)

# imageprova = Image.open('prova.bmp')
# st.image(imageprova)