import pandas as pd
import plotly.express as px
# Path to the JSON file

def read_data(path,data_name):
    file_path = path+"//"+data_name+".csv"
    try:
        df = pd.read_csv(file_path)
        return df
    except:
        print(f"exception in read_data")
        return None
def read_data_parse_dates(path,data_name,date_col):
    file_path = path+"//"+data_name+".csv"
    try:
        df = pd.read_csv(file_path,parse_dates=date_col)
        return df
    except:
        print(f"exception in read_data")
        return None

def clean_patient_data(df):
    df_cleaned = df.dropna(subset=['Id', 'SSN', 'GENDER'])
    df_cleaned.rename({"Id": "PATIENT_ID"}, axis=1, inplace=True)  # to be consistant
    duplicates = df_cleaned[df_cleaned['PATIENT_ID'].duplicated(keep=False)]  # keep=False shows all duplicates
    print("number of duplicates-->", duplicates.shape[0])
    if (duplicates.shape[0] > 0):
        df_cleaned = df_cleaned.drop_duplicates(subset=['PATIENT_ID'], keep='first')
    return df_cleaned

def transform_patient_data(df):
    df['BIRTHDATE'] = pd.to_datetime(df['BIRTHDATE'])
    today = pd.Timestamp.now() ## todays date
    df["GENDER"] = df["GENDER"].astype("string")
    df["ETHNICITY"] = df["ETHNICITY"].astype("string")
    df["RACE"] = df["RACE"].astype("string")
    df['age'] = ((today - df['BIRTHDATE']).dt.days/365).round()  #Calculate age in years
    bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, float('inf')]  # Add infinity for 90+
    labels = [f"{bins[i]}-{bins[i + 1] - 1}" for i in range(len(bins) - 2)] + [f"{bins[-2]}+"]
    df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels, right=False)
    return df

def clean_transform_condition_data(df):
    df.rename({"PATIENT": "PATIENT_ID"}, axis=1, inplace=True)
    duplicates = df[df.duplicated(subset=['PATIENT_ID', 'ENCOUNTER','CODE'], keep=False)]## chekcing if id encounter and code is same in any row
    print("number of duplicates on encounter-->",duplicates.shape[0])
    df['START'] = pd.to_datetime(df['START'])
    df['STOP'] = pd.to_datetime(df['STOP'])
    #df['STOP'] =  df['STOP'].fillna(df['START'])
    df.rename({"PATIENT": "PATIENT_ID","START":"START_DIAG","STOP":"STOP_DIAG"}, axis=1, inplace=True)
    return df

def delete_from_data(df,column,values):
    df = df[~df[column].isin(values)]
    return df

def clean_transform_medication_data(df):
    df['START'] = pd.to_datetime(df['START']) ## converted start date to datetpes
    df['STOP'] = pd.to_datetime(df['STOP'])
    df['STOP'] = df['STOP'].fillna(df['START'])
    df['Year'] = df['START'].dt.year
    df['Month'] = df['START'].dt.month
    df.rename({"PATIENT": "PATIENT_ID", "START": "START_MED", "STOP": "STOP_MED"}, axis=1, inplace=True)
    return df

def clean_transform_procedure_data(df):
    df['START'] = pd.to_datetime(df['START']) ## converted start date to datetpes
    df['STOP'] = pd.to_datetime(df['STOP'])
    df['Year'] = df['START'].dt.year
    df['Month'] = df['START'].dt.month
    df.rename({"PATIENT": "PATIENT_ID", "START": "START_PROC", "STOP": "STOP_PROC"}, axis=1, inplace=True)
    return df

def clean_transform_encounters_data(df):
    df['START'] = pd.to_datetime(df['START']) ## converted start date to datetpes
    df['STOP'] = pd.to_datetime(df['STOP'])
    df["LENGTH_OF_STAY"] = (df['STOP'] - df['START']).dt.total_seconds() / (24 * 60 * 60)
    df["LENGTH_OF_STAY"] = df["LENGTH_OF_STAY"].round(2)
    df['Year'] = df['START'].dt.year
    df['Month'] = df['START'].dt.month
    df.rename({"PATIENT": "PATIENT_ID", "START": "START_ENC", "STOP": "STOP_ENC"}, axis=1, inplace=True)
    return df

#def get_demographic_plot(df,x,y,title):
 ##  fig = px.bar(
   # temp_data,
    #x='DESCRIPTION',
    #y='Count',
    #color=x,
    #barmode='group',
    #title=title,
    #labels={'diagnosis_id': 'Diagnosis ID', 'Count': 'Frequency'}
#)
 #   return fig

def get_demographic_plot(df, x, y, title):
    # Group data and calculate counts
    temp_data = df.groupby([x, y]).size().reset_index(name='Count')
    
    # Calculate total counts for filtering top 10
    top_10_groups = (
        temp_data.groupby(y)["Count"]
        .sum()
        .nlargest(10)
        .index
    )
    
    # Filter data for only top 10
    temp_data = temp_data[temp_data[y].isin(top_10_groups)]
    
    # Create the bar chart
    fig = px.bar(
        temp_data,
        x=y,
        y='Count',
        color=x,
        barmode='group',
        title=title,
        labels={y: y.title(), 'Count': 'Frequency'}
    )
    
    return fig
