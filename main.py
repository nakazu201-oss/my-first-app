import streamlit as st

# アプリのタイトル
st.title("はじめての自作ツール")

# 入力欄を作る
name = st.text_input("あなたの名前を教えてください")

# ボタンを作る
if st.button("挨拶する"):
    if name:
        st.balloons() # お祝いの風船を飛ばす演出
        st.success(f"こんにちは、{name}さん！これはあなたが作った世界に一つだけのツールです。")
    else:
        st.warning("名前を入力してください！")
