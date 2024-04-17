import cv2
import streamlit as st
from datetime import datetime

st.title("CCTV Camera")
start = st.button("Start Camera")

if start:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(1)

    while True:
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        now = datetime.now()
        dayOf = now.strftime("%A")
        currentTime = now.strftime("%H:%M:%S")

        frame = cv2.putText(img=frame, text=dayOf, org=(50,50), 
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, 
                    color=(0, 102, 105), thickness=2, lineType=cv2.LINE_AA)
        
        frame = cv2.putText(img=frame, text=currentTime, org=(50,90), 
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, 
                    color=(0, 102, 105), thickness=2, lineType=cv2.LINE_AA)

        streamlit_image.image(frame)