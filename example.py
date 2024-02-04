import streamlit as st
import pandas as pd
from PIL import Image
import time
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
import altair as alt

#STREAMLİT UYGULAMALARINI KİŞİSELLEŞTİRME

icon = Image.open("streamlit.png")
st.set_page_config(
    page_title="Data Application",
    page_icon=icon,
    layout="centered",
    initial_sidebar_state="auto",
)

#METİN GÖRÜNTÜLEME
 
st.text('Neptune AI Blog') #sabit genişlikte ve önceden biçimlendirilmiş metin görüntüler
st.markdown('# This is Heading 1 in Markdown')#markdown metnini gösteriyor
st.latex(r'''
...     a + ar + a r^2 + a r^3 + cdots + a r^{n-1} =
...     sum_{k=0}^{n-1} ar^k =
...     a left(frac{1-r^{n}}{1-r}right)
...     ''')#LaTex olarak biçimlendirilmiş matematiksel ifadeleri görüntüler
st.title('This is a title')#metni başlık biçiminde görüntüler
st.header('Header')#metni başlık biçimlendirmesinde görüntüler
st.code("st.latex()", language='python')#kodu görüntüler
st.code("st.write()", language='python')
st.write('Can display many things')

#VERİ GÖRÜNTÜLEME

df = pd.read_csv("netflix_india_shows_and_movies.csv")
st.dataframe(df)
st.table(df)
st.json(json_data) 

#MEDYA GÖRÜNTÜLEME

image = Image.open("streamlit.png")
st.image(image)
video_file = open("video.mp4", "rb")
video_bytes = video_file.read()
st.video(video_bytes)

#KOD GÖRÜNTÜLEME

with st.echo():  # Bu kod kodu gösterecek ve ardından veri çerçevesini görüntüleyecektir.
    df = pd.read_csv("netflix_india_shows_and_movies.csv")
    st.dataframe(df)
    

#İLERLEMEYİ VE DURUMU GÖRÜNTÜLEME
    

my_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1)
st.spinner()
with st.spinner(text='In progress'):
    time.sleep(5)
    st.success('Done')
st.balloons()
st.error('Error message')
st.warning('Warning message')
st.info('Info message')
st.success('Success message')
e = RuntimeError('This is an exception of type RuntimeError')
st.exception(e)


#st.progress(0): İlerleme çubuğunu başlatır ve başlangıç değeri olarak 0'ı kullanır.
#for percent_complete in range(100): ...: İlerleme çubuğunu yüzdeye göre güncellemek için bir döngü başlatır. Her adımda, ilerleme çubuğu bir sonraki yüzdeye güncellenir.
#time.sleep(0.1): İşlemi yavaşlatmak için 0.1 saniye bekler. Bu, ilerlemenin görsel olarak gösterilmesine yardımcı olur.
#my_bar.progress(percent_complete + 1): İlerleme çubuğunu belirli yüzdeye göre günceller.
#st.spinner(): Bir döner işareti gösterir.
#with st.spinner(text='In progress'): ...: İçindeki işlemleri bir döner işaretiyle birlikte yürütür. Bu, bir işlem devam ederken kullanıcıya ilerlemenin olduğunu göstermek için kullanılır.
#time.sleep(5): 5 saniye bekler.
#st.success('Done'): İşlem tamamlandığında bir başarı mesajı gösterir.
#st.balloons(): Kullanıcıya baloncuk animasyonu gösterir.
#st.error('Error message'): Bir hata mesajı gösterir.
#st.warning('Warning message'): Bir uyarı mesajı gösterir.
#st.info('Info message'): Bir bilgi mesajı gösterir.
#st.success('Success message'): Bir başarı mesajı gösterir.
#e = RuntimeError('This is an exception of type RuntimeError'): Bir RuntimeError istisnası oluşturur.
#st.exception(e): Oluşan istisnanın ayrıntılarını kullanıcıya gösterir.



#WİDGET'LAR

st.button('Click here')
st.checkbox('Check')
st.radio('Radio', [1,2,3])
st.selectbox('Select', [1,2,3])
st.multiselect('Multiple selection', [21,85,53])
st.slider('Slide', min_value=10, max_value=20)
st.select_slider('Slide to select', options=[1,2,3,4])
st.text_input('Enter some text')
st.number_input('Enter a number')
st.text_area('Text area')
st.date_input('Date input')
st.time_input('Time input')
st.file_uploader('File uploader')
st.color_picker('Color Picker')

#ÖNBELLEĞE ALMA

@st.cache_data
def fetch_data():
    df = pd.read_csv("netflix_india_shows_and_movies.csv")
    return df

data = fetch_data()

#Herhangi bir uygulamada, önbelleğe alma sunucuları, verilerin ve belirli işlevlerin isteğe bağlı olarak kullanıcı tarafından kullanılabilmesini sağlayarak kullanıcı deneyimini geliştirir. Örneğin, verileri getirmek için harcanan zamanı azaltmak için uygulamanızın verileri önbelleğe almasını sağlayabilirsiniz. Veri döndüren işlevlerin sonucunu da önbelleğe alabilirsiniz.
#'@st.cache_data' ile bir işlevi ilk kez çalıştırdığınızda, sonuç yerel bir önbellekte depolanır. İşlevin bir sonraki çağrılışında kod, giriş parametreleri ve işlevin adı değişmezse, Streamlit yürütmeyi atlar ve önbelleğin sonucunu okur.

#MATPLOTLİP KULLANIMI

# Streamlit başlığı
st.title('Matplotlib ile Grafik Çizme')

# Veri oluşturulur. Bu örnekte, 0 ile 10 arasında 100 adet noktayı içeren bir x dizisi oluşturulur ve bu x değerleri üzerindeki sinüs fonksiyonu hesaplanarak bir y dizisi elde edilir:
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Matplotlib kullanılarak bir figür ve eksen oluşturulur
fig, ax = plt.subplots()
ax.plot(x, y)
# Oluşturulan eksen üzerine sinüs grafiği çizilir ve eksen etiketleri ile başlık belirlenir
ax.set_xlabel('X ekseni')
ax.set_ylabel('Y ekseni')
ax.set_title('Sinüs Grafiği')

# Streamlit üzerinde gösterme
st.pyplot(fig)

#PLOTLY KULLANIMI

# Streamlit başlığı
st.title('Plotly ile Grafik Çizme')

# Veri oluşturma
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plotly figürü oluşturma
fig = go.Figure(data=go.Scatter(x=x, y=y))

# Streamlit üzerinde gösterme
st.plotly_chart(fig)

#VEGA-LİTE KULLANIMI

vega_lite_spec = {
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "description": "A simple bar chart with embedded data.",
  "data": {
    "values": [
      {"a": "A", "b": 28}, {"a": "B", "b": 55}, {"a": "C", "b": 43},
      {"a": "D", "b": 91}, {"a": "E", "b": 81}, {"a": "F", "b": 53},
      {"a": "G", "b": 19}, {"a": "H", "b": 87}, {"a": "I", "b": 52}
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "a", "type": "ordinal"},
    "y": {"field": "b", "type": "quantitative"}
  }
}

st.vega_lite_chart(vega_lite_spec, use_container_width=True)


#ALTAİR KULLANIMI

# Veri oluşturma
np.random.seed(0)
data = pd.DataFrame({
    'x': np.random.randn(100),
    'y': np.random.randn(100)
})

# Altair grafiği oluşturma
chart = alt.Chart(data).mark_point().encode(
    x='x',
    y='y'
).interactive()

# Streamlit üzerinde gösterme
st.altair_chart(chart, use_container_width=True)


