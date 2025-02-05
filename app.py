import streamlit as st
import numpy as np


st.title("Juegos")

with open(f"games.txt", 'w') as f:
      for i in range(1, 6):
        a = np.random.randint(0, 5, size=(2, 2, 2))
        b = np.random.randint(0, 5, size=(2, 2, 2))
        c = np.random.randint(0, 5, size=(2, 2, 2))

        f.write(f"""
     L      R  \t\t     L      R  \t\t     L      R
   ----- ----- \t\t   ----- ----- \t\t   ----- -----
U | {a[0, 0][0]},{a[0, 0][1]} | {a[0, 1][0]},{a[0, 1][1]} |\t\tU | {b[0, 0][0]},{b[0, 0][1]} | {b[0, 1][0]},{b[0, 1][1]} |\t\tU | {c[0, 0][0]},{c[0, 0][1]} | {c[0, 1][0]},{c[0, 1][1]} |
   ----- ----- \t\t   ----- ----- \t\t   ----- -----
D | {a[1, 0][0]},{a[1, 0][1]} | {a[1, 1][0]},{a[1, 1][1]} |\t\tD | {b[1, 0][0]},{b[1, 0][1]} | {b[1, 1][0]},{b[1, 1][1]} |\t\tD | {c[1, 0][0]},{c[1, 0][1]} | {c[1, 1][0]},{c[1, 1][1]} |
   ----- ----- \t\t   ----- ----- \t\t   ----- -----
  \n
        """)
        if i %5 ==0:
          f.write("\n\n\n\n\n")


      f.close()
      
st.download_button(label="Descargar juegos estáticos", data=open("games.txt", "rb").read(), file_name="games.txt")