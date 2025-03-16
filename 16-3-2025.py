import time as t
import pandas as pd
import streamlit as sl
from datetime import time
# # ------------------------- markdown
# sl.title('Home')
# sl.markdown("""
# #### Hello, wellcome to my dashboard
# > I'm danger


# Here's a sentence with a footnote. [^1]
# [^1]: This is the footnote.
# """)


# sl.code("""
# print("hello world")
# """)

# sl.write('## H@')
# sl.metric(label='wind speed', value='120ms', delta='-3ms')
# # ------------------------------ dataframe

# df = pd.DataFrame({
#     'col1': [1, 2, 3, 4],
#     'col2': [1, 4, 9, 16]
# })

# sl.table(df)
# sl.dataframe(df)

# #----------------------- media widget 
# sl.image('Dodge-Challenger.jpg', caption='first image', width=320)
# sl.audio('hayedeh-masti-128.mp3')
# # sl.video()


# # --------------------- intractive widget
# def change():
#     print(sl.session_state.first)
# x = sl.checkbox('hi', on_change=change, key='first')
# if x:
#     sl.write("hi how can i help you?")

# z = sl.radio('how are you', options=['ali', 'reza'])
# print(z)

# def click():
#     sl.write('I\'m clicked')
# y = sl.button("click me", on_click=click)
# sl.selectbox('select', options=['1', '2'])
# m = sl.multiselect('select', options=['1', '2'])
# sl.write(m)

## --------------------- file uploader
# files = sl.file_uploader(label='Upload your image', type=['jpg', 'png'], accept_multiple_files=True )
# if files is not None:
#     for file in files:
#         print(file)
#         sl.image(file)

## ---------------------intractive widgets
# s = sl.slider('slider', min_value=1, max_value=20)
# print(s)
# t = sl.text_input("write your name", 'name', max_chars=20  )
# t = sl.text_area("write your name", 'name', max_chars=20  )
# d = sl.date_input('birthday')
# time = sl.time_input('time', )
# sl.write(d)
# print(d)

## timer app with progress bar
time_val = sl.time_input("Set time", value=time(0, 0, 0))
print(time_val)
if str(time_val) is not None:
    h, m, s = str(time_val).split(':')
    seconds = int(h)*3600 + int(m)*60 + int(s)
    progress = seconds / 86400 * 100
    bar = sl.progress(0)
    bar.progress(0)
    for i in range(1, int(progress)):
        t.sleep(0.1)
        bar.progress(i)