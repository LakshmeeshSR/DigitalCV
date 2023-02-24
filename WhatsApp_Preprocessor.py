import re
import pandas as pd
import datetime



def preprocess(data):

    # data = data.read().encode('ascii', 'ignore').decode()

    pattern = r'^(\d{1,2}/\d{1,2}/\d{2,4},? ?\d{1,2}:\d{2} ?(?:am|pm)?)(?: -|,) ([^:]+): (.*)$'

    matches = re.findall(pattern, data, flags=re.MULTILINE | re.IGNORECASE)

    # Create a Pandas DataFrame to store the extracted data
    df = pd.DataFrame(matches, columns=['date', 'user', 'message'])

    df['date'] = df['date'].astype(str)
    df['date'] = df['date'].str.strip()
    df['date'] = df['date'].apply(lambda x: pd.to_datetime(x).strftime('%Y-%m-%d, %H:%M:%S'))
    df = df[~df['user'].str.startswith('You added')]
    df['date'] = pd.to_datetime(df['date'])

    
    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    period = []
    for hour in df[['day_name', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period

    return df










    #replacement
    data = data.replace('\u202f', ' ')   
    data = data.replace('\u200e', '') 

        
    # pattern = r'^(\d{2}/\d{2}/\d{2}, \d{1,2}:\d{2} [apAP][mM]) - (.*?): (.*)$'



    # # Use the re.findall() function to extract all occurrences of the pattern in the text file
    # matches = re.findall(pattern, data, flags=re.MULTILINE)

    # # Create a Pandas DataFrame to store the extracted data
    # df = pd.DataFrame(matches, columns=['date', 'user', 'message'])
    

    # df['date'] = df['date'].astype(str)
    # df['date'] = df['date'].str.strip()
    # df['date'] = df['date'].apply(lambda x: pd.to_datetime(x).strftime('%Y-%m-%d, %H:%M:%S'))
    # df = df[~df['user'].str.startswith('You added')]
    # df['date'] = pd.to_datetime(df['date'])

    
    # df['only_date'] = df['date'].dt.date
    # df['year'] = df['date'].dt.year
    # df['month_num'] = df['date'].dt.month
    # df['month'] = df['date'].dt.month_name()
    # df['day'] = df['date'].dt.day
    # df['day_name'] = df['date'].dt.day_name()
    # df['hour'] = df['date'].dt.hour
    # df['minute'] = df['date'].dt.minute

    # period = []
    # for hour in df[['day_name', 'hour']]['hour']:
    #     if hour == 23:
    #         period.append(str(hour) + "-" + str('00'))
    #     elif hour == 0:
    #         period.append(str('00') + "-" + str(hour + 1))
    #     else:
    #         period.append(str(hour) + "-" + str(hour + 1))

    # df['period'] = period

    # return df


def preprocessIOS(data):


    # data = data.read().encode('ascii', 'ignore').decode()

    pattern = r'^\[(\d{2}\/\d{2}\/\d{2}, \d{2}:\d{2}:\d{2} [apAP][mM])\] (.+?): (.*)$'

    matches = re.findall(pattern, data, flags=re.MULTILINE | re.IGNORECASE)

    # Create a Pandas DataFrame to store the extracted data
    df = pd.DataFrame(matches, columns=['date', 'user', 'message'])

    if df.empty:
    
        pattern = r'^\[(\d{2}/\d{2}/\d{2}), (\d{2}:\d{2}:\d{2})\] (.+?): (.*)$'

        matches = re.findall(pattern, data, flags=re.MULTILINE)

        # Create a Pandas DataFrame to store the extracted data
        df = pd.DataFrame(matches, columns=['date', 'time', 'user', 'message'])

        # Remove the leading and trailing spaces from the columns
        df['date'] = df['date'].str.strip()
        df['time'] = df['time'].str.strip()
        df['user'] = df['user'].str.strip()
        df['message'] = df['message'].str.strip()

        # Combine the date and time columns into a single column
        df['datetime'] = df['date'] + ' ' + df['time']

        # Drop the date and time columns
        df = df.drop(['date', 'time'], axis=1)

        # Reorder the columns
        df = df[['datetime', 'user', 'message']]

        df.rename(columns={'datetime': 'date'}, inplace=True)
        

    df['message'] = df['message'].astype(str)
        
    df['message'] = df['message'].str.strip()



    df['date'] = df['date'].astype(str)
    df['date'] = df['date'].str.strip()
    df['date'] = df['date'].apply(lambda x: pd.to_datetime(x).strftime('%Y-%m-%d, %H:%M:%S'))
    #df['message'] = df['message'].replace(['GIF omitted', 'image omitted', 'sticker omitted', 'video omitted', 'audio omitted'],'<Media omitted>')
    df.loc[df['message'].str.contains('omitted'), 'message'] = '<Media omitted>'
    df = df[~df['user'].str.startswith('You added')]
    df['date'] = pd.to_datetime(df['date'])

        
    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    period = []
    for hour in df[['day_name', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period

    return df














