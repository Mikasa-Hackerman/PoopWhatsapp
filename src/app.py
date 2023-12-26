"""Interfaz gráfica"""
import time
import pandas as pd
import src.whatsapp_parser as wpp
import streamlit as st
import plotly.express as px
from stqdm import stqdm

def run():
    """Función principal de la aplicación Streamlit"""
    st.set_page_config(page_title="Subir Archivo de Texto", page_icon="📄")

    st.markdown("---")
    st.markdown("<center><h1> 💩 Analizador de Cacas 💩", unsafe_allow_html=True)
    st.markdown("---")
    
    st.markdown('''
        <style>
            .rotate-and-scale {
                display: inline-block;
                animation: rotateAndScale 4s infinite linear;
            }
            @keyframes rotateAndScale {
                0%, 100% { 
                    transform: scale(0.1);
                }
                50% {
                    transform: scale(1.5);
                }
            }
        </style>
        <p style="text-align:center;">
            <img class="rotate-and-scale" src="https://media.giphy.com/media/2uxqZNcoAxujRtJ0ET/giphy.gif" alt="poop emoji">
        </p>
    ''', unsafe_allow_html=True)
    
    archivo = st.file_uploader("Seleccione su archivo lleno de caca (.txt)", type=["txt"])

    if archivo is not None:
        
        # with st.spinner("ULTRA PROCESANDO SU CHAT CACAL 🤢💩🤮💩🤮 .. . . . AGUARDE !!"):
        #     time.sleep(2)
        
        # st.markdown('<p style="text-align:center;"><img src="https://media.giphy.com/media/2uxqZNcoAxujRtJ0ET/giphy.gif" alt="poop emoji"></p>', unsafe_allow_html=True)

        # Centrar la imagen y hacerla girar utilizando HTML y CSS
        st.markdown('''
            <style>
                .rotate {
                    display: inline-block;
                    animation: rotate 2s infinite linear;
                }
                @keyframes rotate {
                    0% { transform: rotate(0deg); }
                    100% { transform: rotate(360deg); }
                }
            </style>
            <p style="text-align:center;">
                <img class="rotate" src="https://media.giphy.com/media/2uxqZNcoAxujRtJ0ET/giphy.gif" alt="poop emoji">
            </p>
        ''', unsafe_allow_html=True)

        
        for x in stqdm(range(1, 101), "DECODIFICANDO CACA 🤢"):
            time.sleep(1/x**1.03)
        
        for x in stqdm(range(1, 101), "ANAL-IZANDO ESPECTROS CACALES DE ALTO ORDEN 🤮"):
            time.sleep(1/x**1.03)
            
        st.error("EXCESO DE CACA EN EL CHATT DETECTADO!!!  🤮🤮🤮🤮🤮!!!!!")
        st.balloons()
        st.markdown('''
            <style>
                .rotate {
                    display: inline-block;
                    animation: rotate 20s infinite linear;
                }
                @keyframes rotate {
                    0% { transform: rotate(0deg); }
                    100% { transform: rotate(360deg); }
                }
            </style>
        ''', unsafe_allow_html=True)

        contenido = archivo.readlines()
        contenido = [cont.decode("utf-8") for cont in contenido]
        
        contenido_filtrado = list(filter(wpp.es_mensaje_caca, contenido)) # filtramos
        datos = list(map(wpp.android_parser, contenido_filtrado)) # mapeamos
        
        df = pd.DataFrame(datos, columns=["Fecha", "Hora", "Nombre"])
        
        caca_df = pd.DataFrame(df)
        caca_df["Fecha"] = pd.to_datetime(caca_df["Fecha"], format="%d/%m/%Y")

        caca_df["Dia"] = caca_df["Fecha"].dt.day_name()

        recuento_dia = caca_df.groupby(["Dia", "Nombre"]).size().reset_index().rename(columns={0: "Recuento día"})
        
        fig = px.bar(recuento_dia, x='Dia', y='Recuento día', color='Nombre',
             labels={'Recuento día': 'Recuento de cacas', 'Dia': 'Día de la semana'},
             title="Suma de cacas por día de semana y persona",
             barmode='group')

        # Mostrar la figura en Streamlit
        st.plotly_chart(fig)
        

    else:
        st.info("Por favor, carga un archivo de texto.")