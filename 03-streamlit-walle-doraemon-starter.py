import streamlit as st
import sys

# Python 版本检查
if sys.version_info >= (3, 13):
    st.error("⚠️ 当前 Python 版本为 3.13+，可能与 fastai 不兼容。建议使用 Python 3.11。")
    st.stop()

from fastai.vision.all import *
import pathlib

@st.cache_resource
def load_model():
    model_path = pathlib.Path(__file__).parent / "doraemon_walle_model.pkl"
    return learner.load(model_path)

model = load_model()

st.title("Doraemon vs Walle 分类器")
st.write("上传一张图片，让模型判断它是 Doraemon 还是 Walle！")
uploaded_file = st.file_uploader("选择一张图片...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = PILImage.create(uploaded_file)
    st.image(image, caption="上传的图片", use_column_width=True)
    pred, pred_idx, probs = model.predict(image)
    st.write(f"预测结果: {pred}")
    st.write(f"概率: {probs[pred_idx]:.04f}")
