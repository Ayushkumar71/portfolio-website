import requests

import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_timeline import timeline
import streamlit.components.v1 as components
from PIL import Image


from constant import *



# Set page configuration
st.set_page_config(page_title='Template', layout="wide", page_icon='🙋🏻‍♂️')

# Set up a chatbot later


# -----------------  loading assets  ----------------- #
#     
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")

# loading assets
lottie_gif = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_x17ybolp.json")
python_lottie = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_2znxgjyt.json")
tensorflow_lottie = load_lottieurl("https://lottie.host/9f24235b-b198-42f0-a593-a1d09748f242/8Eig3YpEbM.json")
my_sql_lottie = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_w11f2rwn.json")
git_lottie = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_03cuemhb.json")
github_lottie = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_6HFXXE.json")
tableau_lottie = load_lottieurl("https://lottie.host/549bfc80-eaad-4644-9f78-df70d51d9ba4/Z7KANCNBQT.json")
figma_lottie = load_lottieurl("https://lottie.host/5b6292ef-a82f-4367-a66a-2f130beb5ee8/03Xm3bsVnM.json")
js_lottie = load_lottieurl("https://lottie.host/fc1ad1cd-012a-4da2-8a11-0f00da670fb9/GqPujskDlr.json")



# ----------------- info ----------------- #
def gradient(color1, color2, color3, content1, content2):
    st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:60px;border-radius:2%;">'
                f'<span style="color:{color3};">{content1}</span><br>'
                f'<span style="color:white;font-size:17px;">{content2}</span></h1>', 
                unsafe_allow_html=True)

with st.container():
    col1,col2 = st.columns([8,3])

full_name = info['Full_Name']
with col1:
    gradient('#FFD4DD','#000395','e0fbfc',f"Hi, I'm {full_name}👋", info["Intro"])
    st.write("")
    st.write(info['About'])
    
    
with col2:
    st_lottie(lottie_gif, height=280, key="data")
        

# ----------------- skillset ----------------- #
with st.container():
    st.subheader('⚒️ Skills')
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        st_lottie(python_lottie, height=70,width=70, key="python", speed=2.5)
    with col2:
        st_lottie(tensorflow_lottie, height=70,width=70, key="tensorflow", speed=4)
    with col3:
        st_lottie(my_sql_lottie,height=70,width=70, key="mysql", speed=2.5)
    with col4:
        st_lottie(tableau_lottie,height=70,width=70, key="docker", speed=2.5)
    with col1:
        st_lottie(github_lottie,height=50,width=50, key="github", speed=2.5)
    with col2:
        st_lottie(git_lottie,height=70,width=70, key="git", speed=2.5)
    with col3:
        st_lottie(figma_lottie,height=50,width=50, key="figma", speed=2.5)
    with col4:
        st_lottie(js_lottie,height=50,width=50, key="js", speed=1)
    
    
# # -----------------  tableau  -----------------  #
# with st.container():
#     st.markdown("""""")
#     st.subheader("📊 Tableau")
#     col1,col2 = st.columns([0.95, 0.05])
#     with col1:
#         with st.expander('See the work'):
#             components.html(
#                 """
#                 <!DOCTYPE html>
#                 <html>  
#                     <title>Basic HTML</title>  
#                     <body style="width:130%">  
#                         <div class='tableauPlaceholder' id='viz1684205791200' style='position: static'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Su&#47;SunnybrookTeam&#47;Overview&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='SunnybrookTeam&#47;Overview' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Su&#47;SunnybrookTeam&#47;Overview&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1684205791200');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='1350px';vizElement.style.maxWidth='100%';vizElement.style.minHeight='1550px';vizElement.style.maxHeight=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='1350px';vizElement.style.maxWidth='100%';vizElement.style.minHeight='1550px';vizElement.style.maxHeight=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.minHeight='5750px';vizElement.style.maxHeight=(divElement.offsetWidth*1.77)+'px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
#                     </body>  
#                 </HTML>
#                 """
#             , height=400, scrolling=True
#             )
#     st.markdown(""" <a href={}> <em>🔗 access to the link </a>""".format(info['Tableau']), unsafe_allow_html=True)




# ----------------- timeline ----------------- #


with st.container():
    st.markdown("""""")
    st.subheader('📌 Career Snapshot')

    # load data
    with open('example.json', "r") as f:
        data = f.read()

    # render timeline
    timeline(data, height=400)




# ------------------- Projects -------------------- # 

st.title("Projects")

# Iterate through projects
for project in projects:
    st.markdown(f"## {project['title']}")  # Display project title
    project_image = Image.open(project["image_path"])  # Open the image
    st.image(project_image, use_column_width=True)  # Display the image
    st.markdown(project["description"])  # Display the description
    st.markdown("---")  # Separator between projects

# -----------------  Testimonials  ----------------- #

with st.container():
    # Divide the container into three columns
    col1,col2,col3 = st.columns([0.475, 0.475, 0.05])
    # In the first column (col1)        
    with col1:
        # Add a subheader to introduce the Testimonials slideshow
        st.subheader("Testimonials")
        # Embed an HTML component to display the slideshow
        components.html(
        f"""
        <!DOCTYPE html>
        <html>
        <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <!-- Styles for the slideshow -->
        <style>
            * {{box-sizing: border-box;}}
            .mySlides {{display: none;}}
            img {{vertical-align: middle;}}

            /* Slideshow container */
            .slideshow-container {{
            position: relative;
            margin: auto;
            width: 100%;
            }}

            /* The dots/bullets/indicators */
            .dot {{
            height: 15px;
            width: 15px;
            margin: 0 2px;
            background-color: #eaeaea;
            border-radius: 50%;
            display: inline-block;
            transition: background-color 0.6s ease;
            }}

            .active {{
            background-color: #6F6F6F;
            }}

            /* Fading animation */
            .fade {{
            animation-name: fade;
            animation-duration: 1s;
            }}

            @keyframes fade {{
            from {{opacity: .4}} 
            to {{opacity: 1}}
            }}

            /* On smaller screens, decrease text size */
            @media only screen and (max-width: 300px) {{
            .text {{font-size: 11px}}
            }}
            </style>
        </head>
        <body>
            <!-- Slideshow container -->
            <div class="slideshow-container">
                <div class="mySlides fade">
                <img src={testimonials["img1"]} style="width:100%">
                </div>

                <div class="mySlides fade">
                <img src={testimonials["img2"]} style="width:100%">
                </div>

                <div class="mySlides fade">
                <img src={testimonials["img3"]} style="width:100%">
                </div>

            </div>
            <br>
            <!-- Navigation dots -->
            <div style="text-align:center">
                <span class="dot"></span> 
                <span class="dot"></span> 
                <span class="dot"></span> 
            </div>

            <script>
            let slideIndex = 0;
            showSlides();

            function showSlides() {{
            let i;
            let slides = document.getElementsByClassName("mySlides");
            let dots = document.getElementsByClassName("dot");
            for (i = 0; i < slides.length; i++) {{
                slides[i].style.display = "none";  
            }}
            slideIndex++;
            if (slideIndex > slides.length) {{slideIndex = 1}}    
            for (i = 0; i < dots.length; i++) {{
                dots[i].className = dots[i].className.replace("active", "");
            }}
            slides[slideIndex-1].style.display = "block";  
            dots[slideIndex-1].className += " active";
            }}

            var interval = setInterval(showSlides, 2500); // Change image every 2.5 seconds

            function pauseSlides(event)
            {{
                clearInterval(interval); // Clear the interval we set earlier
            }}
            function resumeSlides(event)
            {{
                interval = setInterval(showSlides, 2500);
            }}
            // Set up event listeners for the mySlides
            var mySlides = document.getElementsByClassName("mySlides");
            for (i = 0; i < mySlides.length; i++) {{
            mySlides[i].onmouseover = pauseSlides;
            mySlides[i].onmouseout = resumeSlides;
            }}
            </script>

            </body>
            </html> 

            """,
                height=270,
    )  

# -----------------  contact  ----------------- #
    with col2:
        st.subheader("📨 Contact Me")
        contact_form = f"""
        <form action="https://formsubmit.co/{info["Email"]}" method="POST">
            <input type="hidden" name="_captcha value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)
