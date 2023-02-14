import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("Streamlit 超入門")

st.write("プログレスバーの表示")

# プログレスバー(徐々に増えていくバー)
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i + 1)
    time.sleep(0.03)
"Done!!!"

left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラムです")

expander1 = st.expander("問い合わせ")
expander1.write("問い合わせ1への回答")
expander2 = st.expander("問い合わせ2")
expander2.write("問い合わせ2への回答")


# 　チェックボックス
# if st.checkbox("画像を表示"):
#     img = Image.open("スパイダーマン.png")
# st.image(img, caption="スパイダーマン", use_column_width=True)

# ウィジェット
# option = st.selectbox("あなたが好きな数字を教えてください、", list(range(1, 11)))
# "あなたが選んだ数字：", option
# text = st.text_input("あなたの趣味を教えてください、")
# "あなたの趣味：", text
# condition = st.slider("あなたの今の調子は？", 0, 100, 50)
# "あなたのコンディション：", condition

# 　サイドバーの作成
# text = st.sidebar.text_input("あなたの趣味を教えてください、")
# condition = st.sidebar.slider("あなたの今の調子は？", 0, 100, 50)
# "あなたの趣味：", text
# "あなたのコンディション：", condition

# df = pd.DataFrame(
#     np.random.rand(100, 2) / [50, 50] + [35.69, 139.70], columns=["lat", "lon"]
# )

# テーブルの作成
# st.dataframe(df.style.highlight_max(axis=0), width=300, height=300)  # 動的
# st.table(df.style.highlight_max(axis=0))  # 静的

# チャートの作成
# st.line_chart(df) #線形
# st.area_chart(df) #塗りつぶし
# st.bar_chart(df)  # 棒グラフ

# マッピング
# st.map(df) # 地図上にマッピング
