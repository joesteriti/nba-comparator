#pip install plotly
import plotly.graph_objects as go

#pip install requests to make HTTP requests
import requests
from dotenv import load_dotenv
import os

BASE_URL = "https://api-nba-v1.p.rapidapi.com/"

endpoint = ""

headers = {
    "x-rapidapi-host": "api-nba-v1.p.rapidapi.com",
    "x-rapidapi-key": "41c4debfe3mshb19c98476ad3e39p1b9b6bjsnf1057326c1b0" #os.getenv("API_KEY")
}

def configure():
    load_dotenv()

def search_player(name):
    url = f"{BASE_URL}players?search={name}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("Request was successful!")
        # Optionally, print the response content (e.g., the JSON data)
        print(response.json())
    else:
        print(f"Request failed with status code {response.status_code}")
    #return response.json()

player_name = "james"
'''
# Define the data for the radar chart
categories = ['A', 'B', 'C', 'D', 'E']
values = [3, 4, 2, 5, 4]

# Create a radar chart
radar = go.Figure(go.Scatterpolar(
    r=values,
    theta=categories,
    fill='toself',  # Fills the area inside the radar chart
))

# Update layout for better aesthetics
radar.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 5]
        ),
    ),
    showlegend=False
)

# Example data
x_values = [1, 2, 3, 4, 5]
y_values = [10, 11, 12, 13, 14]


# Create a scatter plot
scatter = go.Figure(data=go.Scatter(
    x=x_values,
    y=y_values,
    mode='markers',  # 'markers' for scatter plot
    marker=dict(color='blue', size=10)  # Custom marker style
))

# Update layout for better aesthetics
scatter.update_layout(
    title="Scatter Plot Example",
    xaxis_title="X Axis",
    yaxis_title="Y Axis"
)

labels = ['Category A', 'Category B', 'Category C', 'Category D']
values = [10, 20, 30, 40]

# Create the pie chart
pie = go.Figure(data=go.Pie(
    labels=labels,   # Labels for the sections
    values=values,   # Values for each section
    hole=0.3,        # Adds a hole in the middle to create a donut chart (optional)
    textinfo='percent+label',  # Display both percentage and label
    marker=dict(colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'])  # Custom colors
))

# Update layout for better aesthetics
pie.update_layout(
    title="Pie Chart Example"
)

# Show the plot
radar.show()

# Show the chart
scatter.show()
'''
def main():
    configure()
    search_player(player_name)

main()