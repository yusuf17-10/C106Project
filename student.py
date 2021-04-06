import csv
import plotly.express as px
import numpy as np


def plot_figure(data_path):
    data=open(data_path)
    new_data=csv.DictReader(data)
    fig=px.scatter(new_data,x="Days Present",y="Marks In Percentage")
    fig.show()

def get_data_source(data_path):
    percentage=[]
    days=[]
    data=open(data_path)
    new_data=csv.DictReader(data)

    for row in new_data:
        percentage.append(float(row["Marks In Percentage"]))
        days.append(float(row["Days Present"]))

    return {"x":percentage,"y":days}

def find_correlation(data_source):
    correlation=np.corrcoef(data_source["x"],data_source["y"])
    print(correlation[0,1])



def setup():
    data_path="student.csv"
    plot_figure(data_path)
    data_source=get_data_source(data_path)
    find_correlation(data_source)


setup()