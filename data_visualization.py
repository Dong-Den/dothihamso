import streamlit as st
import numpy as np
import math
import matplotlib.pyplot as plt  

import seaborn as sns

st.set_page_config(
   page_title= "Đồ thị hàm số") 

st.title("Úng dụng vẽ đồ thị hàm số")

bai_tap= st.sidebar.selectbox(
    "Chọn bài tập:",
    ["Bài 1: Vẽ đồ thị hàm số cơ bản",
     "Bài 2: So sánh 2 hàm số trên cùng một biểu đồ",
     "Bài 3: Vẽ đồ thị hàm bậc 3",
     "BÀi 4: Tương tác với slider để khảo sát đồ thị",
     "Bài 5: Vẽ headmap cho hàm z= x2+ y2"])


if bai_tap =="Bài 1: Vẽ đồ thị hàm số cơ bản":
    st.header("Bài 1: Vẽ đồ thị hàm số cơ bản")
    st.write("Chọn 1 trong các hàm số sin, cos, exp, log và vẽ biểu đồ trên đoạn [-10, 10].")
    ham_so = st.selectbox(
      "Chọn hàm số:",
      ["sin", "cos", "exp", "log"])
    x= np.linspace(-10,10,100)
    if ham_so =="sin":
      y=np.sin(x)
      ten_ham= "f(x) = sin(x)"
    elif ham_so=="cos":
      y=np.cos(x)
      ten_ham= "f(x) = cos(x)"
    elif ham_so =="exp":
       y=np.exp(x)
       ten_ham="f(x)= exp(x)"
    elif ham_so =="log":
       x_log=np.linspace(0.01, 10,1000)
       y=np.log(x_log)
       x=x_log
       ten_ham="f(x)= log(x)"
    fig,ax= plt.subplots(figsize=(10,6))
    ax.plot(x,y, 'b-', linewidth=2)
    ax.set_title(f"Đồ thị hàm số {ten_ham}")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.grid(True)


    ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    ax.axvline(x=0,color='k', linestyle = '-', alpha=0.3)
    st.pyplot(fig)

    
elif bai_tap == "Bài 2: So sánh 2 hàm số trên cùng một biểu đồ":
    st.header("Bài 2: So sánh 2 hàm số trên cùng một biểu đồ")
    st.write("Chọn hai hàm số bất kỳ trong số: sin, cos, exp, log và vẽ chúng")
    ham1 = st.selectbox("Chọn hàm số thứ nhất:", ["sin", "cos", "exp", "log"], key="ham1")
    ham2 = st.selectbox("Chọn hàm số thứ hai:", ["sin", "cos", "exp", "log"], key="ham2")
    x = np.linspace(-10, 10, 500)
    x_log = np.linspace(0.01, 10, 500)
    def tinh_ham(ten_ham, x_vals):
        if ten_ham == "sin":
            return np.sin(x_vals)
        elif ten_ham == "cos":
            return np.cos(x_vals)
        elif ten_ham == "exp":
            return np.exp(x_vals)
        elif ten_ham == "log":
            return np.log(x_vals)

    if ham1 == "log" or ham2 == "log":
        x = x_log

    y1 = tinh_ham(ham1, x)
    y2 = tinh_ham(ham2, x)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, y1, label=f"f1(x) = {ham1}(x)", color='blue')
    ax.plot(x, y2, label=f"f2(x) = {ham2}(x)", color='green')
    ax.set_title("So sánh hai hàm số")
    ax.set_xlabel("x")
    ax.set_ylabel("Giá trị hàm")
    ax.grid(True)
    ax.legend()
    ax.axhline(y=0, color='k', linestyle='--', linewidth=0.5)
    ax.axvline(x=0, color='k', linestyle='--', linewidth=0.5)
    st.pyplot(fig)

elif bai_tap == "Bài 3: Vẽ đồ thị hàm bậc 3":
    st.header("Bài 3: Vẽ đồ thị hàm bậc 3")
    st.write("Nhập hệ số a, b, c, d cho hàm số y = ax³ + bx² + cx + d")

    a = st.number_input("Hệ số a", value=1.0)
    b = st.number_input("Hệ số b", value=0.0)
    c = st.number_input("Hệ số c", value=0.0)
    d = st.number_input("Hệ số d", value=0.0)

    x = np.linspace(-10, 10, 500)
    y = a * x**3 + b * x**2 + c * x + d

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, y, color='purple', linewidth=2)
    ax.set_title(f"Đồ thị hàm số y = {a}x³ + {b}x² + {c}x + {d}")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True)
    ax.axhline(y=0, color='k', linestyle='--', linewidth=0.5)
    ax.axvline(x=0, color='k', linestyle='--', linewidth=0.5)
    st.pyplot(fig)

elif bai_tap == "BÀi 4: Tương tác với slider để khảo sát đồ thị":
    st.header("Bài 4: Khảo sát hàm số y = ax² + bx + c")
    st.write("Sử dụng các thanh trượt để thay đổi hệ số a, b, c")

    a = st.slider("Hệ số a", -5.0, 5.0, 1.0)
    b = st.slider("Hệ số b", -10.0, 10.0, 0.0)
    c = st.slider("Hệ số c", -10.0, 10.0, 0.0)

    x = np.linspace(-10, 10, 500)
    y = a * x**2 + b * x + c

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, y, color='orange', linewidth=2)
    ax.set_title(f"Đồ thị y = {a}x² + {b}x + {c}")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True)
    ax.axhline(y=0, color='k', linestyle='--', linewidth=0.5)
    ax.axvline(x=0, color='k', linestyle='--', linewidth=0.5)
    st.pyplot(fig)

elif bai_tap == "Bài 5: Vẽ headmap cho hàm z= x2+ y2":
    st.header("Bài 5: Biểu diễn hàm z = x² + y² dưới các dạng biểu đồ")
    st.write("Hiển thị heatmap, contour và 3D surface của hàm số z = x² + y²")

    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    Z = X**2 + Y**2

    # Heatmap
    fig1, ax1 = plt.subplots()
    sns.heatmap(Z, cmap='viridis', cbar=True, ax=ax1)
    ax1.set_title("Heatmap z = x² + y²")
    st.pyplot(fig1)

    # 3D Surface plot
    fig2 = plt.figure()
    ax2 = fig2.add_subplot(111, projection='3d')
    ax2.plot_surface(X, Y, Z, cmap=cm.viridis)
    ax2.set_title("Surface plot z = x² + y²")
    st.pyplot(fig2)

    # Contour plot
    fig3, ax3 = plt.subplots()
    contour = ax3.contour(X, Y, Z, cmap=cm.viridis)
    ax3.clabel(contour, inline=True)
    ax3.set_title("Contour plot z = x² + y²")
    st.pyplot(fig3)
