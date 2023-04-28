
# cd Users/"Lakshmeesh S Reddy"/Desktop/Dinku/JOB/Whatsapp_Chat_Analyse
def run():
             
    import streamlit as st
    import WhatsApp_Preprocessor, helper
    import matplotlib.pyplot as plt
    import seaborn as sns
    import requests
    import os
    import zipfile
    
    # from ipywidgets import interactive

    


    def create_zip_archive(folder_path, output_path):
        try:
            with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        zipf.write(os.path.join(root, file), arcname=os.path.join(os.path.relpath(root, folder_path), file))
        except Exception as e:
            st.write(f"Error creating zip archive: {e}")

 

    button_label = "Dont have the chat file? Download a sample here"
    url = "https://raw.githubusercontent.com/LakshmeeshSR/DigitalCV/main/assets/Download_txt_file.zip"
    response = requests.get(url)

    st.sidebar.download_button(label=button_label, data=response.content, file_name="chat_txt_file.zip", mime="application/zip")

# https://cdn.wallpapersafari.com/54/0/HluF7g.jpg

    page_bg_img = f"""
    <style>
     [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/jpeg;base64,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");
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


    # st.markdown("<h1 style='color: green;'>Whatsapp Chat Analyzer</h1>", unsafe_allow_html=True)

    text = "Whatsapp Chat Analyzer"

    st.write(
        """
        <div style="position: relative; height: 40px; width: 100%;">
            <h1 style="position: relative; top: -65px; left: 15%; color:#3F4944; font-size:36px; font-family: Algerian">{}</h1>
        </div>
        """.format(text),
        unsafe_allow_html=True
    )

    uploaded_file_Android = st.sidebar.file_uploader("Upload Android WhatsApp chat txt file")
    
    uploaded_file_IOS = st.sidebar.file_uploader("Upload IOS WhatsApp chat txt file")

    if uploaded_file_Android is None and uploaded_file_IOS is None:

        default_file_url = "https://raw.githubusercontent.com/LakshmeeshSR/DigitalCV/main/Dummy_chat.txt"
        default_file_path = "default_chat.txt"
        response = requests.get(default_file_url)
        if response.status_code == 200:
            with open(default_file_path, "wb") as f:
                f.write(response.content)
            with open(default_file_path, "r", encoding="utf-8") as f:
                data = f.read()
                data = data.encode('ascii', 'ignore').decode()  # replace unicode characters
                df = WhatsApp_Preprocessor.preprocess(data)

        
        # fetch unique users
        user_list = df['user'].unique().tolist()
        #user_list.remove('group_notification')
        user_list.sort()
        user_list.insert(0,"Overall")

        selected_user = st.selectbox("Analysis according to users",user_list)

        

        # if st.button("Show Analysis"):

        num_messages,words, num_media_messages, num_links = helper.fetch_stats(selected_user, df)
        # st.title("Top Statistics")


        col1, col2, col3, col4 = st.columns(4)

        with col1:            
            st.header('Total messages')
            st.title(num_messages)

        with col2:            
            st.header('Total words')
            st.title(words)

        with col3:
            st.header("Media Shared")
            st.title(num_media_messages)

        with col4:
            st.header("Total links")
            st.write("#")
            st.title(num_links)

        # monthly timeline
        # st.title("Monthly Timeline")
        st.markdown("<h1 style='color: green;'>Monthly Timeline</h1>", unsafe_allow_html=True)
        timeline = helper.monthly_timeline(selected_user,df)
        fig,ax = plt.subplots(figsize=(5, 3))
        ax.plot(timeline['time'],timeline['message'], color='green')

        ax.set_xlim(timeline['time'].min(), timeline['time'].max())
        ax.xaxis.set_major_locator(plt.MaxNLocator(20))
        ax.set_xlabel('Months')
        ax.set_ylabel('Messages')
        plt.xticks(rotation='vertical')
        fig.set_size_inches(8, 4)
        st.pyplot(fig)

        # daily timeline
        # st.title("Daily Timeline")
        st.markdown("<h1 style='color: green;'>Daily Timeline</h1>", unsafe_allow_html=True)
        daily_timeline = helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='skyblue')
        fig.set_size_inches(8, 4)
        plt.xticks(rotation='vertical')
        # Set x-axis limits to include full range of dates
        ax.set_xlim(daily_timeline['only_date'].min(), daily_timeline['only_date'].max())
        ax.set_xlabel('Dates')
        ax.set_ylabel('Messages')
        st.pyplot(fig)

        # activity map
        # st.title('Activity Map')
        st.markdown("<h1 style='color: green;'>Activity Map</h1>", unsafe_allow_html=True)
        col1,col2 = st.columns(2)

        with col1:
            st.header("Most busy day")
            busy_day = helper.week_activity_map(selected_user,df)
            fig,ax = plt.subplots()
            ax.bar(busy_day.index,busy_day.values,color='purple')
            #ax.set_xlabel('Dates')
            ax.set_ylabel('Messages')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        with col2:
            st.header("Most busy month")
            busy_month = helper.month_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values,color='orange')
            ax.set_ylabel('Messages')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        # st.title("Weekly Activity Map")
        st.markdown("<h1 style='color: green;'>Weekly Activity Map</h1>", unsafe_allow_html=True)
        user_heatmap = helper.activity_heatmap(selected_user,df)
        fig,ax = plt.subplots()
        ax = sns.heatmap(user_heatmap, cmap="coolwarm")
        ax.set_xlabel("Hours of Day")
        ax.set_ylabel("WeekDay")
        st.pyplot(fig)
        
        
        col1, col2 = st.columns(2)

        # finding the busiest users in the group(Group level)
        if selected_user == 'Overall':
            # st.title('Most Busy Users')
            st.markdown("<h1 style='color: green;'>Most Busy Users</h1>", unsafe_allow_html=True)
            x,new_df = helper.most_busy_users(df)
            fig, ax = plt.subplots()

            col1, col2 = st.columns(2)

            with col1:
                ax.bar(x.index, x.values,color='red')
                ax.set_ylabel("Messages")
                plt.xticks(rotation='vertical')
                st.pyplot(fig)

            with col2:
                st.dataframe(new_df)


        # Most common words
        most_common_df = helper.most_common_words(selected_user,df)

        fig, ax = plt.subplots()

        ax.barh(most_common_df[0],most_common_df[1], color='Grey')
        ax.set_ylabel("Words")
        ax.set_xlabel("Frequency of usage")
        plt.xticks(rotation='vertical')

        # st.title('Most common words')
        st.markdown("<h1 style='color: green;'>Most common words</h1>", unsafe_allow_html=True)
        st.pyplot(fig)
##################################################################################################################################################

    if uploaded_file_Android is not None:

        data = uploaded_file_Android.read().decode("utf-8")
        data = data.encode('ascii', 'ignore').decode()  # replace unicode characters
        df = WhatsApp_Preprocessor.preprocess(data)

        # bytes_data = uploaded_file_IOS.getvalue()
        # data = bytes_data.decode("utf-8")
        
        # df = WhatsApp_Preprocessor.preprocessIOS(data)
        
        
        # fetch unique users
        user_list = df['user'].unique().tolist()
        #user_list.remove('group_notification')
        user_list.sort()
        user_list.insert(0,"Overall")

        selected_user = st.selectbox("Analysis according to users",user_list)



        # if st.button("Show Analysis"):

        num_messages,words, num_media_messages, num_links = helper.fetch_stats(selected_user, df)
        # st.title("Top Statistics")


        col1, col2, col3, col4 = st.columns(4)

        with col1:            
            st.header('Total messages')
            st.title(num_messages)

        with col2:            
            st.header('Total words')
            st.title(words)

        with col3:
            st.header("Media Shared")
            st.title(num_media_messages)

        with col4:
            st.header("Total links")
            st.title(num_links)

        # monthly timeline
        # st.title("Monthly Timeline")
        st.markdown("<h1 style='color: green;'>Monthly Timeline</h1>", unsafe_allow_html=True)
        timeline = helper.monthly_timeline(selected_user,df)
        fig,ax = plt.subplots(figsize=(5, 3))
        ax.plot(timeline['time'],timeline['message'], color='green')

        ax.set_xlim(timeline['time'].min(), timeline['time'].max())
        ax.xaxis.set_major_locator(plt.MaxNLocator(20))
        ax.set_xlabel('Months')
        ax.set_ylabel('Messages')
        plt.xticks(rotation='vertical')
        fig.set_size_inches(8, 4)
        st.pyplot(fig)

        # daily timeline
        # st.title("Daily Timeline")
        st.markdown("<h1 style='color: green;'>Daily Timeline</h1>", unsafe_allow_html=True)
        daily_timeline = helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='skyblue')
        fig.set_size_inches(8, 4)
        plt.xticks(rotation='vertical')
        # Set x-axis limits to include full range of dates
        ax.set_xlim(daily_timeline['only_date'].min(), daily_timeline['only_date'].max())
        ax.set_xlabel('Dates')
        ax.set_ylabel('Messages')
        st.pyplot(fig)

        # activity map
        # st.title('Activity Map')
        st.markdown("<h1 style='color: green;'>Activity Map</h1>", unsafe_allow_html=True)
        col1,col2 = st.columns(2)

        with col1:
            st.header("Most busy day")
            busy_day = helper.week_activity_map(selected_user,df)
            fig,ax = plt.subplots()
            ax.bar(busy_day.index,busy_day.values,color='purple')
            #ax.set_xlabel('Dates')
            ax.set_ylabel('Messages')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        with col2:
            st.header("Most busy month")
            busy_month = helper.month_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values,color='orange')
            ax.set_ylabel('Messages')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        # st.title("Weekly Activity Map")
        st.markdown("<h1 style='color: green;'>Weekly Activity Map</h1>", unsafe_allow_html=True)
        user_heatmap = helper.activity_heatmap(selected_user,df)
        fig,ax = plt.subplots()
        ax = sns.heatmap(user_heatmap, cmap="coolwarm")
        ax.set_xlabel("Hours of Day")
        ax.set_ylabel("WeekDay")
        st.pyplot(fig)
        
        
        col1, col2 = st.columns(2)

        # finding the busiest users in the group(Group level)
        if selected_user == 'Overall':
            # st.title('Most Busy Users')
            st.markdown("<h1 style='color: green;'>Most Busy Users</h1>", unsafe_allow_html=True)
            x,new_df = helper.most_busy_users(df)
            fig, ax = plt.subplots()

            col1, col2 = st.columns(2)

            with col1:
                ax.bar(x.index, x.values,color='red')
                ax.set_ylabel("Messages")
                plt.xticks(rotation='vertical')
                st.pyplot(fig)

            with col2:
                st.dataframe(new_df)


        most_common_df = helper.most_common_words(selected_user,df)

        fig, ax = plt.subplots()

        ax.barh(most_common_df[0],most_common_df[1], color='Grey')
        ax.set_ylabel("Words")
        ax.set_xlabel("Frequency of usage")
        plt.xticks(rotation='vertical')

        # st.title('Most common words')
        st.markdown("<h1 style='color: green;'>Most common words</h1>", unsafe_allow_html=True)
        st.pyplot(fig)

     
    ##############################################################################################################################################

    if uploaded_file_IOS is not None:

        data = uploaded_file_IOS.read().decode("utf-8")
        data = data.encode('ascii', 'ignore').decode()  # replace unicode characters
        df = WhatsApp_Preprocessor.preprocessIOS(data)

        # bytes_data = uploaded_file_IOS.getvalue()
        # data = bytes_data.decode("utf-8")
        
        # df = WhatsApp_Preprocessor.preprocessIOS(data)
        
        
        # fetch unique users
        user_list = df['user'].unique().tolist()
        #user_list.remove('group_notification')
        user_list.sort()
        user_list.insert(0,"Overall")

        selected_user = st.selectbox("Analysis according to users",user_list)



        # if st.button("Show Analysis"):

        num_messages,words, num_media_messages, num_links = helper.fetch_stats(selected_user, df)
        # st.title("Top Statistics")


        col1, col2, col3, col4 = st.columns(4)

        with col1:            
            st.header('Total messages')
            st.title(num_messages)

        with col2:            
            st.header('Total words')
            st.title(words)

        with col3:
            st.header("Media Shared")
            st.title(num_media_messages)

        with col4:
            st.header("Total links")
            st.title(num_links)

        # monthly timeline
        # st.title("Monthly Timeline")
        st.markdown("<h1 style='color: green;'>Monthly Timeline</h1>", unsafe_allow_html=True)
        timeline = helper.monthly_timeline(selected_user,df)
        fig,ax = plt.subplots(figsize=(5, 3))
        ax.plot(timeline['time'],timeline['message'], color='green')

        ax.set_xlim(timeline['time'].min(), timeline['time'].max())
        ax.xaxis.set_major_locator(plt.MaxNLocator(20))
        ax.set_xlabel('Months')
        ax.set_ylabel('Messages')
        plt.xticks(rotation='vertical')
        fig.set_size_inches(8, 4)
        st.pyplot(fig)

        # daily timeline
        # st.title("Daily Timeline")
        st.markdown("<h1 style='color: green;'>Daily Timeline</h1>", unsafe_allow_html=True)
        daily_timeline = helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='skyblue')
        fig.set_size_inches(8, 4)
        plt.xticks(rotation='vertical')
        # Set x-axis limits to include full range of dates
        ax.set_xlim(daily_timeline['only_date'].min(), daily_timeline['only_date'].max())
        ax.set_xlabel('Dates')
        ax.set_ylabel('Messages')
        st.pyplot(fig)

        # activity map
        # st.title('Activity Map')
        st.markdown("<h1 style='color: green;'>Activity Map</h1>", unsafe_allow_html=True)
        col1,col2 = st.columns(2)

        with col1:
            st.header("Most busy day")
            busy_day = helper.week_activity_map(selected_user,df)
            fig,ax = plt.subplots()
            ax.bar(busy_day.index,busy_day.values,color='purple')
            #ax.set_xlabel('Dates')
            ax.set_ylabel('Messages')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        with col2:
            st.header("Most busy month")
            busy_month = helper.month_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values,color='orange')
            ax.set_ylabel('Messages')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        # st.title("Weekly Activity Map")
        st.markdown("<h1 style='color: green;'>Weekly Activity Map</h1>", unsafe_allow_html=True)
        user_heatmap = helper.activity_heatmap(selected_user,df)
        fig,ax = plt.subplots()
        ax = sns.heatmap(user_heatmap, cmap="coolwarm")
        ax.set_xlabel("Hours of Day")
        ax.set_ylabel("WeekDay")
        st.pyplot(fig)
        
        
        col1, col2 = st.columns(2)

        # finding the busiest users in the group(Group level)
        if selected_user == 'Overall':
            # st.title('Most Busy Users')
            st.markdown("<h1 style='color: green;'>Most Busy Users</h1>", unsafe_allow_html=True)
            x,new_df = helper.most_busy_users(df)
            fig, ax = plt.subplots()

            col1, col2 = st.columns(2)

            with col1:
                ax.bar(x.index, x.values,color='red')
                ax.set_ylabel("Messages")
                plt.xticks(rotation='vertical')
                st.pyplot(fig)

            with col2:
                st.dataframe(new_df)


        most_common_df = helper.most_common_words(selected_user,df)

        fig, ax = plt.subplots()

        ax.barh(most_common_df[0],most_common_df[1], color='Grey')
        ax.set_ylabel("Words")
        ax.set_xlabel("Frequency of usage")
        plt.xticks(rotation='vertical')

        # st.title('Most common words')
        st.markdown("<h1 style='color: green;'>Most common words</h1>", unsafe_allow_html=True)
        st.pyplot(fig)

        



