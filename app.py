import streamlit as st
from PIL import Image
import pytesseract
import io

# Tùy chỉnh đường dẫn nếu cần thiết
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Giao diện ứng dụng
st.title("Ứng dụng phân tích chữ viết tay")

# Cột giao diện
col1, col2 = st.columns([3, 1])

# hiển thị hình ảnh và kết quả
with col1:
    st.header("Hình ảnh đã tải lên")
    uploaded_image = st.file_uploader("Thêm hình ảnh chữ viết tay", type=["jpg", "png", "jpeg"])
    if uploaded_image is not None:
        # Hiển thị hình ảnh đã tải lên
        image = Image.open(uploaded_image)
        st.image(image, caption="Hình ảnh của bạn", use_column_width=True)

    st.header("Kết quả phân tích:")
    result_text = st.empty()  # Dùng để cập nhật kết quả phân tích

# Nút phân tích
with col2:
    st.header("Tác vụ")
    if uploaded_image:
        if st.button("Phân tích ảnh"):
            st.write("Đang phân tích...")
            with st.spinner("Phân tích ảnh..."):
                # Phân tích chữ viết tay bằng Tesseract
                extracted_text = pytesseract.image_to_string(image)
                result_text.write(extracted_text)
            st.success("Phân tích xong!")
