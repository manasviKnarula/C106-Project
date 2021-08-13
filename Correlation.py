import csv 
import plotly.express as px
import numpy as np

def get_data_source(data_path):
    marksInPercentage = []
    daysPresent = []


    with open (data_path) as csv_file:
        df = csv.DictReader(csv_file)
        for row in df:
            marksInPercentage.append(float(row["Marks In Percentage"]))
            daysPresent.append(float(row["Days Present"]))
        
    
    return {"x":marksInPercentage,"y":daysPresent}

def find_correlation(data_source):
    correlation=np.corrcoef(data_source["x"],data_source["y"])
    print("correlation between marks in percentage and days present: ",correlation[0,1])

def setup ():
    data_path = "/Users/manasvinarula/Downloads/C106 project/present.csv"
    data_source = get_data_source(data_path)
    find_correlation(data_source)

def plot_figure ():
    fig = px.scatter(df,x="Marks In Percentage",y="Days Present")
    fig.show()


setup()