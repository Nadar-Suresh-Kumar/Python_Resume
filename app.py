from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"
back = current_dir / "assets" / "download.jpeg"
#https://www.bing.com/ck/a?!&&p=a3817258bb68a956JmltdHM9MTY5NjExODQwMCZpZ3VpZD0yYjVlNDhmMy1kZjM4LTZlZDItMTI5NS01Yjg4ZGVlYjZmNTAmaW5zaWQ9NTczNA&ptn=3&hsh=3&fclid=2b5e48f3-df38-6ed2-1295-5b88deeb6f50&u=a1L2ltYWdlcy9zZWFyY2g_cT1uYXZ5IGJsdWUgY29sb3ImRk9STT1JUUZSQkEmaWQ9NTlCMjJGMTcwQjdCNDg4MUJFOUJCNEIzQ0FENDIzQjdDRjI3NTM3OQ&ntb=1


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Suresh"
PAGE_ICON = ":wave:"
NAME = "Suresh Kumar"
DESCRIPTION = """
I am felexible person seeking employment which will allow , growth and make use of my existing skills.
I always seek to achieve a high standard in whatever work I undertake. 
"""
EMAIL = "sureshkumarnadar1701@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/suresh-kumar-n-1933a2255?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app",
    "GitHub": "https://github.com",
    
}
PROJECTS = {
    "🏆 Programming language ": "https://github.com/Nadar-Suresh-Kumar/Icon-journey-of-python",
    "🏆 Valentine Week : Mini projects": "https://github.com/Nadar-Suresh-Kumar/valentine",
  
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
-    South Indian's Welfare Society College  ( B.Sc.IT )
- ✔️ CGPA of Second Semester is 9.3
- ✔️ CGPA of First Semester is 8.5
-    Sies College Of Arts , Science & Commerce ( HSC )
- ✔️ Percentage : 58%
-    Kamarajar Memorial English High School and Junior College
- ✔️ Percentage : 85% 
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python , Go , C# , C++ , C , 
- 🌐 Full Stack : HTML , CSS , Javascript , PHP , JSON 
- 🗄️ Databases:  MySQL , PLSQL 
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write('\n')
st.write("🚧", "**Library Assistant | S.I.W.S College**")
st.write("Sep/23 to Current ")
st.write(
    """
- ► Used excel and e-library managemnt softwares
"""
)

# --- JOB 2
st.write("🚧", "**Data Entry | Jetking **")
st.write("36 Hrs")
st.write(
    """
- ► Used Excel 
- ► Increasing the traffic in websites by creating inorganic subscribers
"""
)

# --- JOB 3

st.write('\n')
st.write("🚧", "**Tutor | Jaya Classes**")
st.write("9 Months")



# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")


# --- LANGUAGES ---
st.write('\n')
st.subheader("Languages known")
st.write(
    """
- English , Tamil , Hindi , Marathi
""")