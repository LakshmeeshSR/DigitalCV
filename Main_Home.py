import streamlit as st
import LinearReg
import SMS_Spam_Prediction_proj
import WhatsApp_app
import IPL_Youtube
import PowerBI
import requests
from io import BytesIO

# Define function for main page
#def show_main_page():
def show_main_page():

    import streamlit as st
    from PIL import Image
    import requests
    from io import BytesIO
# data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxISEhUTEhIVFRUXFxUXFRUVFRUVFRUVFRUXFxUVFRUYHSggGBolHRUVITEhJSkrLi4uFx8zODMtNygtLisBCgoKDg0OFRAQFy0dFR0tLS0tLS0tLS0tLS0tLSstLS0tLS0tNy0tLS0tLS0tLTctLS0tKy0tLS0tNy03LTctN//AABEIALcBEwMBIgACEQEDEQH/xAAYAAEBAQEBAAAAAAAAAAAAAAABAAIDB//EACEQAQEBAQADAAEFAQAAAAAAAAABEQISITHwA2FxgZFR/8QAGAEBAQEBAQAAAAAAAAAAAAAAAAECBQT/xAAXEQEBAQEAAAAAAAAAAAAAAAAAEQEx/9oADAMBAAIRAxEAPwD0zlqDla9rmnoSijCFb0xiVqUXDagQFFuNM9QNEjcZqgmN1iX6QKGlAIrWY1OTgQYYRoqxKoFahIqChQtEVBoXBU6BoFm1aMVk1nD2uQZsTdiCNc1dVnjpqRFNc+a6s3gxdHMbPMNSrmMVrmpmwCo1IJEGLG5BYlDYLDpkBmhqxkFatVVAxYcQKHQIghjTChqkFawRkrDgrFFaqxWWWdbxm8qg7v5/Sn09RmA3iGVA3OTG9c/Jlrg6ufG+a59Q89KjcUv/AFjqiSkWurOkXpFa5p5Z5p1BdM7WupUoOY1rEpgYdHJwcgji6o0CKloEQxAKz1W7HPvkxNa4pHMVFaZFqtEoOlnFRqK0aO4RR1RqxRWW4hhFavTOLkxlQJG5FFpFYpDqqKsYx0ipSMyNQZqoK1kVvmB1nDzGpFIgqzW6MBz+tSGcmLSC8rlKINVnRaLVhut+Tn1z8Sq4mlGUdxBnVTIlSERoYis2NWJVSMYy3KzYrKvaWkHSKxQ2stq0Vfn+ehegVMg6p0Gp0uumEFbitEOIrOHkWnmYqGoYcRUJ01YpAArQwGImsZsVENZOKi5rdjOHyNMMFFUQMixQgoNW+1gqtWiKKjPUMqqEBHtKOtSLDTPSxq/EEYhOM1QmiVmg6ShnWpAWBq0AYrTIEUabQKIadEGqLyEaxcwBYJG6pAZqwi0EFhzAWLDrIEYVQGCnRaILRSGkMQkQjroZ6q5ZjVaitFIolbxjnl000xhSGEBip1YijFKbVzBBpMVgrNNhkHVARSI0FaMVMEUNAFLBtYXGdblHVFFqlNrOqKwRa1rGHxBrWSOtBUGVVUEqZQVqxriNRcyJVzGsLCRo2jyY6q51YlbalYsUqQroIxrcoqsa5GpFOoWGQEy1IrAERowGaY1YzQWDGoAZqw4IqKwY1hwSOcbnKPRVjPUQtMogwdU2iriaFYpDFHPP3Td5IkbkEU6ZjLVbtF6ZrHd9LE3Xbn2sjH6Pxu1FzjNKioIqcoU2mRmLQbQFRWxglOgYr6AtBWqsxoRayKVGqzeStBcms2s6DUFFo56VKquRVFRLWhiCFrPXXttUY8k14oF5KUs9X2DYsU6FqK1zR5MynArXNWlYKdFo1uIvQsaFoJVk24DQs9qDEGtZViihkSakRXPGjaFQWrWOqosStYxXRnqGGs2ictcmiCKtc1n9Sb8BeSo8DgBGRUAklRWufVaGho8mZa3hqopTNZ1RFdeaZWIZUXGpGtYOIpqghop0YsNBSNMyrqopokEqtVDFoICgoGbPYrV+rpakXDPVNZ6gmnmGqDqAOOm9c+Y1QxdVSqKgNVrNvsxUVqN/lCslIQDpIRcfu0kDVi5SRoW1uBGmNYkkaNZ6oQmt6x1UjDVxGkjRDroINNqlCA6rQgSSUStSADySVkSrUgZpxIDUkD//2Q==
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("https://media.istockphoto.com/id/1005466206/photo/orange-creased-tissue-paper-background-texture.jpg?s=612x612&w=0&k=20&c=RMIK3NBPuC0X0Y6DkU-rt4uEELjJvQ0eFku3uOViChg=");
    background-size: cover;

    background-position: top left;
    background-repeat: no-repeat;
    opacity: 1;
    background-attachment: local;
    }}

    [data-testid="stSidebar"] > div:first-child {{
    background-image: url("data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxISEhUTEhIVFRUXFxUXFRUVFRUVFRUVFRUXFxUVFRUYHSggGBolHRUVITEhJSkrLi4uFx8zODMtNygtLisBCgoKDg0OFRAQFy0dFR0tLS0tLS0tLS0tLS0tLSstLS0tLS0tNy0tLS0tLS0tLTctLS0tKy0tLS0tNy03LTctN//AABEIALcBEwMBIgACEQEDEQH/xAAYAAEBAQEBAAAAAAAAAAAAAAABAAIDB//EACEQAQEBAQADAAEFAQAAAAAAAAABEQISITHwA2FxgZFR/8QAGAEBAQEBAQAAAAAAAAAAAAAAAAECBQT/xAAXEQEBAQEAAAAAAAAAAAAAAAAAEQEx/9oADAMBAAIRAxEAPwD0zlqDla9rmnoSijCFb0xiVqUXDagQFFuNM9QNEjcZqgmN1iX6QKGlAIrWY1OTgQYYRoqxKoFahIqChQtEVBoXBU6BoFm1aMVk1nD2uQZsTdiCNc1dVnjpqRFNc+a6s3gxdHMbPMNSrmMVrmpmwCo1IJEGLG5BYlDYLDpkBmhqxkFatVVAxYcQKHQIghjTChqkFawRkrDgrFFaqxWWWdbxm8qg7v5/Sn09RmA3iGVA3OTG9c/Jlrg6ufG+a59Q89KjcUv/AFjqiSkWurOkXpFa5p5Z5p1BdM7WupUoOY1rEpgYdHJwcgji6o0CKloEQxAKz1W7HPvkxNa4pHMVFaZFqtEoOlnFRqK0aO4RR1RqxRWW4hhFavTOLkxlQJG5FFpFYpDqqKsYx0ipSMyNQZqoK1kVvmB1nDzGpFIgqzW6MBz+tSGcmLSC8rlKINVnRaLVhut+Tn1z8Sq4mlGUdxBnVTIlSERoYis2NWJVSMYy3KzYrKvaWkHSKxQ2stq0Vfn+ehegVMg6p0Gp0uumEFbitEOIrOHkWnmYqGoYcRUJ01YpAArQwGImsZsVENZOKi5rdjOHyNMMFFUQMixQgoNW+1gqtWiKKjPUMqqEBHtKOtSLDTPSxq/EEYhOM1QmiVmg6ShnWpAWBq0AYrTIEUabQKIadEGqLyEaxcwBYJG6pAZqwi0EFhzAWLDrIEYVQGCnRaILRSGkMQkQjroZ6q5ZjVaitFIolbxjnl000xhSGEBip1YijFKbVzBBpMVgrNNhkHVARSI0FaMVMEUNAFLBtYXGdblHVFFqlNrOqKwRa1rGHxBrWSOtBUGVVUEqZQVqxriNRcyJVzGsLCRo2jyY6q51YlbalYsUqQroIxrcoqsa5GpFOoWGQEy1IrAERowGaY1YzQWDGoAZqw4IqKwY1hwSOcbnKPRVjPUQtMogwdU2iriaFYpDFHPP3Td5IkbkEU6ZjLVbtF6ZrHd9LE3Xbn2sjH6Pxu1FzjNKioIqcoU2mRmLQbQFRWxglOgYr6AtBWqsxoRayKVGqzeStBcms2s6DUFFo56VKquRVFRLWhiCFrPXXttUY8k14oF5KUs9X2DYsU6FqK1zR5MynArXNWlYKdFo1uIvQsaFoJVk24DQs9qDEGtZViihkSakRXPGjaFQWrWOqosStYxXRnqGGs2ictcmiCKtc1n9Sb8BeSo8DgBGRUAklRWufVaGho8mZa3hqopTNZ1RFdeaZWIZUXGpGtYOIpqghop0YsNBSNMyrqopokEqtVDFoICgoGbPYrV+rpakXDPVNZ6gmnmGqDqAOOm9c+Y1QxdVSqKgNVrNvsxUVqN/lCslIQDpIRcfu0kDVi5SRoW1uBGmNYkkaNZ6oQmt6x1UjDVxGkjRDroINNqlCA6rQgSSUStSADySVkSrUgZpxIDUkD//2Q==");
    background-size: cover;

    background-position: top left;
    background-repeat: no-repeat;
    opacity: 1;
    background-attachment: local;
    }}

    [data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
    }}
    [data-testid="stToolbar"] {{
    right: 2rem;
    }}
    </style>
    """

    st.markdown(page_bg_img, unsafe_allow_html=True)

    col1, col2 = st.columns(2,gap= 'small')


##  "C:\Users\Lakshmeesh s reddy\Desktop\Dinku\JOB\Pages\Pages\profile-picCLR.png"

    with col1:

        # image = Image.open(r"C:\Users\Lakshmeesh s reddy\Desktop\Dinku\JOB\Pages\Pages\profile-picCLR.png")  
        # st.image(image, width=230)

        url = "https://raw.githubusercontent.com/LakshmeeshSR/DigitalCV/main/profile-picCLR.png"
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        st.image(img, width=150)
        st.markdown("📳 +91 9739836908")
        st.markdown("📧 lakshmeeshsr@gmail.com")
        st.markdown("🔗[Lakshmeesh|LinkedIn](https://www.linkedin.com/in/lakshmeesh-s-reddy-6694ab208/)")

    with col2:

        st.write("<h1 style='text-align: left; color: #763E3E; font-size: 30px; font-family:Century Gothic;'>Lakshmeesh S Reddy</h1>", unsafe_allow_html=True)

        text = "A Data Storyteller with hands-on experience in various real-world projects.  Dedication, Positive thinking, creativity, and optimal utilisation of skills are my strengths. The goal is to make a mark in the society and to be a part of continuous growth."
        
        st.write("<p style='text-align: left; color: white; font-size: 20px; font-family: Calibri;'>{}</p>".format(text), unsafe_allow_html=True)

        # contacts = "📳 +91 9739836908&nbsp;&nbsp;&nbsp;;📧 <a href='mailto:lakshmeeshsr@gmail.com'>lakshmeeshsr@gmail.com</a>"

        # st.write("<p style='text-align: left; color: black; font-size: 15px; font-family: Calibri;'>{}</p>".format(contacts), unsafe_allow_html=True)


    # st.write("<h1 style='text-align: left; color: #763E3E; font-size: 26px; font-family:Century Gothic;'>Education 🎓</h1>", unsafe_allow_html=True)

    # text = [
    #     "• 🧑‍🎓 Mechanical Engineering (2021), <span style='font-size: 18px;'>7.87 CGPA</span>, <span style='font-size: 18px;'>Vemana IT, Bengaluru</span>",
    #     "• 🙋‍♂️ PUC (2017), <span style='font-size: 18px;'>76%</span>, <span style='font-size: 18px;'>Jain College, Bengaluru</span>",
    #     "• 🚴 S.S.L.C (2015), <span style='font-size: 18px;'>84.96%</span>, <span style='font-size: 18px;'>Sudarshan Vidya Mandir, Bengaluru</span>"
    # ]

    # for line in text:
    #     st.write(f'<p style="color: white; font-size: 20px; font-family: Arial;">{line}</p>', unsafe_allow_html=True)

    st.write("<h1 style='text-align: left; color: #763E3E; font-size: 26px; font-family:Century Gothic;'>Projects 📈</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='color: #763E3E;'>Real Estate – Price predictor</h4>", unsafe_allow_html=True)
    REP ="Helps numerous real estate property buyers/homeowner aspirants to assess the price of a real estate property and avoid paying premium costs on top of the property value. Using Linear regression, my solution will estimate the price of a property based on location, amenities, and growth potential. Customers who use my solution will end up paying no more than fair value."
    st.write("<p style='text-align: left; color: White; font-size: 20px; font-family: Calibri;'>{}</p>".format(REP), unsafe_allow_html=True)
    st.markdown("👈👈Click on side bar to view projects")


    st.markdown("<h4 style='color: #763E3E;'>IPL – YouTube analyser</h4>", unsafe_allow_html=True)
    IPL ="IPL (Indian Premier League) is a highly popular cricket tournament with millions of fans across the world. Digital media interactions are also a big part of the franchise. My solution helps to leverage the YouTube API to analyse the performance of all the IPL teams based on their uploads, views, and subscribers count by using YouTube API to extract the data. By using live data, my solution provides up-to-date insights into the performance of each team, helping fans and analysts to understand the trends and patterns in teams’ digital performance and hence assess online behaviour."
    st.write("<p style='text-align: left; color: White; font-size: 20px; font-family: Calibri;'>{}</p>".format(IPL), unsafe_allow_html=True)
    st.markdown("👈👈Click on side bar to view projects")

    st.markdown("<h4 style='color: #763E3E;'>SMS spam detector</h4>", unsafe_allow_html=True)
    SMSD ="Spam messages are a major problem in modern communication, with unwanted messages flooding people's inboxes and causing annoyance and frustration. My approach uses Logistic Regression to identify spam messages and block them from reaching the intended receivers, to address this issue. By accurately identifying spam messages and filtering them out, it helps to improve the quality of communication and reduce the negative impact of spam messages on people's daily lives."
    st.write("<p style='text-align: left; color: White; font-size: 20px; font-family: Calibri;'>{}</p>".format(SMSD), unsafe_allow_html=True)
    st.markdown("👈👈Click on side bar to view projects")

    st.markdown("<h4 style='color: #763E3E;'>WhatsApp chat analyser</h4>", unsafe_allow_html=True)
    WAA ="Understanding and analysing WhatsApp conversations can be a challenging task due to the large amount of data involved. Using Regular expression my chat analyser reads the text file and helps users to gain insights into their conversations by providing a comprehensive analysis of the number of messages, pictures, videos, and words in the chat. By using data visualization techniques, the tool makes it easier for users to interpret and analyse the conversation patterns, frequency, and timings. This will further enable users with a better understanding of their WhatsApp conversations, which can be used to improve communication, monitor performance, and make data-driven decisions."
    st.write("<p style='text-align: left; color: White; font-size: 20px; font-family: Calibri;'>{}</p>".format(WAA), unsafe_allow_html=True)
    st.markdown("👈👈Click on side bar to view projects")

    st.markdown("<h4 style='color: #763E3E;'>Operations and Finance Dashboard</h4>", unsafe_allow_html=True)
    OFD ="Managing and monitoring operations and financial performance is a critical aspect of business management. However, the complexity and volume of data involved can make this task challenging. My Power BI dashboards provide an easy-to-understand visual representation of operational and financial data. This enables business managers and stakeholders to make informed decisions and take proactive steps to optimize performance"
    st.write("<p style='text-align: left; color: White; font-size: 20px; font-family: Calibri;'>{}</p>".format(OFD), unsafe_allow_html=True)
    st.markdown("👈👈Click on side bar to view projects")




    st.write("#")

    st.write("<h1 style='text-align: left; color: #763E3E; font-size: 26px; font-family:Century Gothic;'>Skills 🛠️</h1>", unsafe_allow_html=True)

    st.write(
        """
        <div style='color: white; font-size: 20px; font-family: Arial; display: flex;'>
            <div style='margin-right: 10px;'>• 👩‍💻 Programming:</div>
            <div style='color: white; font-family: Arial;'>Python (Scikit-learn, Pandas, Matplotlib), Streamlit</div>
        </div>
        
        <div style='color: white; font-size: 20px; font-family: Arial; display: flex;'>
            <div style='margin-right: 10px;'>• 📊 Data Visualization:</div>
            <div style='color: white; font-family: Arial;'>PowerBi, MS Excel</div>
        </div>

        <div style='color: white; font-size: 20px; font-family: Arial; display: flex;'>
            <div style='margin-right: 10px;'>• 📈 Modeling:</div>
            <div style='color: white; font-family: Arial;'>Logistic regression, linear regression, NLP*</div>
        </div>

        <div style='color: white; font-size: 20px; font-family: Arial; display: flex;'>
            <div style='margin-right: 10px;'>• 🗄️ Databases:</div>
            <div style='color: white; font-family: Arial;'>MS SQL</div>
        </div>

        """, unsafe_allow_html=True
    )
    st.write("#")
    st.write("<h1 style='text-align: left; color: #763E3E; font-size: 26px; font-family:Century Gothic;'>Experience 🏢</h1>", unsafe_allow_html=True)

    # Set the font family, size, and color for the app
    st.markdown(
        """
        <style>
        .title {
            font-family: Arial;
            font-size: 22px;
            font-weight: bold;
            color: #763E3E;
        }
        .subtitle {
            font-family: Arial;
            font-size: 20px;
            font-style: italic;
            color: #906969;
        }
        .text {
            font-family: Arial;
            font-size: 18px;
            color: #906969;
        }

        .txt {
            font-family: Arial;
            font-size: 20px;
            color:White;
        }

        </style>
        """,
        unsafe_allow_html=True
    )




    st.markdown("<p class='title' style='margin-bottom: 0px;'>Jr Data Analyst,</p>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle' style='margin-top: 0; margin-bottom: 5px;'>Axcend Automation and software solution</p>", unsafe_allow_html=True)
    st.markdown("<p class='text' style='margin-top: 0;'>09/2021 – 08/2022 </p>", unsafe_allow_html=True)
    
    st.write(
        """
        <div style='color: white; font-size: 20px; font-family: Arial; display: flex; margin-bottom: 7px;'>
            <div style='margin-right: 10px;'>• Lead in data analysis, cleaning, and maintenance for multiple projects using SQL, and Excel.</div>
        </div>
        
        <div style='color: white; font-size: 20px; font-family: Arial; display: flex; margin-bottom: 7px;'>
            <div style='margin-right: 10px;'>• Created Visual dashboards to facilitate easy data interpretation using PowerBI.</div>
        </div>

        <div style='color: white; font-size: 20px; font-family: Arial; display: flex; margin-bottom: 7px;'>
            <div style='margin-right: 10px;'>• Digitized manufacturing processes by collecting and cleaning data, improving accuracy and efficiency</div>
        </div>

        <div style='color: white; font-size: 20px; font-family: Arial; display: flex; margin-bottom: 7px;'>
            <div style='margin-right: 10px;'>• Member of critical onsite inspections to correlate design and execution, ensuring project success.</div>
        </div>

        <div style='color: white; font-size: 20px; font-family: Arial; display: flex; margin-bottom: 7px;'>
        <div style='margin-right: 10px;'>• Demonstrated a keen attention to detail and accuracy, while working collaboratively in a team environment to contribute to overall project success.</div>
        </div>
        """, unsafe_allow_html=True
    )

    st.write("#")

    st.write("<h1 style='text-align: left; color: #763E3E; font-size: 26px; font-family:Century Gothic;'>Certificate Courses 📄</h1>", unsafe_allow_html=True)

    st.markdown("<p class='txt'>●	Google Data Analytics Professional Certificate, Coursera</p>", unsafe_allow_html=True)
    st.markdown("<p class='txt'>●	Python 101 for Data Science, Cognitiveclass.ai, Powered by IBM</p>", unsafe_allow_html=True)
    st.markdown("<p class='txt'>●	Data Science Methodology, Cognitiveclass.ai, Powered by IBM</p>", unsafe_allow_html=True)
    st.markdown("<p class='txt'>●	PowerBI workshop, Growth School</p>", unsafe_allow_html=True)


    txt = "👈👈👈PROJECTS" 
    st.write("#")
    st.write("#")
    st.write("<p style='text-align: left; black: white; font-size: 20px; font-family: Calibri;'>{}</p>".format(txt), unsafe_allow_html=True)


def select_project():
    st.sidebar.title("My projects")    
    # project01 = st.sidebar.radio("Home", ["Home"])
    project = st.sidebar.selectbox('select', ["Home","Real Estate – Price predictor", "IPL Analysis using Youtube API", "SMS spam detector", "WhatsApp Chat analyzer", "PowerBI"])
    return project


# Define function for "Back to Main Page" button
# def show_back_to_main_button():
#     st.sidebar.markdown("---")
#     if st.sidebar.button("Back to Main Page"):
#         return True


# Handle project selection
project = select_project()

if project == "Real Estate – Price predictor":
    LinearReg.run()
    # if show_back_to_main_button():
    #     project = None
    #     show_main_page()

elif project == "IPL Analysis using Youtube API":
    IPL_Youtube.run()
    # if show_back_to_main_button():
    #     project = None
    #     show_main_page()



elif project == "SMS spam detector":
    SMS_Spam_Prediction_proj.run()
    # if show_back_to_main_button():
    #     project = None
    #     show_main_page()


elif project == "WhatsApp Chat analyzer":
    WhatsApp_app.run()


elif project == "PowerBI":
    PowerBI.run()


else:
    show_main_page()



