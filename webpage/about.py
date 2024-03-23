import streamlit as st

def about_page():
    phonepe_deatils= """ The Phonepe Data Visualization project is a Python-based solution that extracts data from the Phonepe Pulse Github repository, transforms them, and displays it through an interactive dashboard using Streamlit, Plotly and few other visualization and data manipulation libraries."""
    st.subheader(phonepe_deatils)
    st.markdown("## :violet[About PhonePe Pulse:] ")

    detail_col, video_col = st.columns([3,4])
    with detail_col:
        phonepe_pulse_deatil1= "The Indian digital payments story has truly captured the world's imagination. From the largest towns to the remotest villages, there is a payments revolution being driven by the penetration of mobile phones, mobile internet and state-of-the-art payments infrastructure built as Public Goods championed by the central bank and the government. Founded in December 2015, PhonePe has been a strong beneficiary of the API driven digitisation of payments in India. When we started, we were constantly looking for granular and definitive data sources on digital payments in India. PhonePe Pulse is our way of giving back to the digital payments ecosystem. "
        phonepe_pulse_deatil2 = "The PhonePe Pulse website showcases more than 2000+ Crore transactions by consumers on an interactive map of India. With over 45% market share, PhonePe's data is representative of the country's digital payment habits. The insights on the website and in the report have been drawn from two key sources - the entirety of PhonePe's transaction data combined with merchant and customer interviews. The report is available as a free download on the PhonePe Pulse website and GitHub."
        st.markdown(f"<h4>{phonepe_pulse_deatil1}</h4>", unsafe_allow_html=True)
        st.markdown(f"<h4>{phonepe_pulse_deatil2}</h4>", unsafe_allow_html=True)
    with video_col:
        video1 = open("src/videos/PhonePe-Pulse.mp4", "rb")
        video1 = video1.read()
        st.video(video1)        
    st.markdown("## :violet[About PhonePe:] ")

    video_col, detail_col = st.columns([4,4])
    with detail_col:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        phonepe_deatil1= "PhonePe is an Indian digital payments and financial technology company headquartered in Bengaluru, Karnataka, India. PhonePe was founded in December 2015, by Sameer Nigam, Rahul Chari and Burzin Engineer. The PhonePe app, based on the Unified Payments Interface (UPI), went live in August 2016. It is owned by Flipkart, a subsidiary of Walmart."
        st.markdown(f"<h3>{phonepe_deatil1}</h3>", unsafe_allow_html=True)
        st.write("")
        st.write("")
        st.download_button("DOWNLOAD THE APP NOW", "https://www.phonepe.com/app-download/")
        st.write("")
        st.write("")
        st.markdown("## :violet[Contact:] ")
        
        contact_col, img_col, social_col = st.columns([15,1,10])
        with contact_col:
            st.markdown("<h2> Saravana Perumal K </h2><h3> An Enthusiastic Data Science Engineer</h3>", unsafe_allow_html=True)

    with video_col:
        video2 = open("src/videos/Phonepe.mp4", "rb")
        video2 = video2.read()
        st.video(video2)
    with img_col:
        st.write("")
        st.image("src/images/gmail.png")
        st.image("src/images/github.jpeg")
        st.image("src/images/linkedin.png")
    with social_col:
        st.write("")
        st.write("smartsaravana002@gmail.com")
        st.write("https://github.com/Saravana-kr22")
        st.write("www.linkedin.com/in/saravana-perumal-k-07233b1b4")

    return None
    