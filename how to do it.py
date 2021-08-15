Challenge:
You work for a telecom company and have clients for several different services, including the main ones: internet and telephone.

The problem is that, looking at the customer history of the last few years, you've noticed that the company has Churn of more than 26% of the customers.

This represents a loss of millions for the company.

What does the company need to do to resolve this?

Data base: https://drive.google.com/drive/folders/blablablabla
Original Kaggle Link: https://www.kaggle.com/radmirzosimov/telecom-users-dataset

# Step 1: Import database into Python
import pandas as pd

chart = pd.read_csv('telecom_users.csv')
display(chart)

# Step 2: View the database
# Understand what information you have available
# Find the wrong things in the database
chart = chart.drop('Unnamed: 0', axis=1) # 0 is row and 1 is column
display(chart)

# Step 3: Database treatment
# Values that are numbers but Python thinks are texts
chart ['TotalCharges'] = pd.to_numeric(chart['TotalCharges'], errors='coerce')
# Values that are empty
# empty columns

# all is when you want to delete COMPLETELY empty columns
# any is when you want to exclude columns that have AT LEAST 1 empty value
chart = chart.dropna(how="all", axis=1) 

# empty lines
chart = chart.dropna(how="any", axis=0) 
print(chart.info())

# Step 4: Exploratory Analysis -> General Analysis -> See how the cancellations are doing.
display(chart["Churn"].value_counts())
display(chart["Churn"].value_counts(normalize=True).map("{:.1%}".format))

# Step 5: Looking at columns in our database -> identify why customers cancel
import plotly.express as px

for column in chart.columns:
    print(column)
    chart = px.histogram(chart, x=column, color='Churn')
    chart.show()

Write your conclusions here:

- Customers with larger families (married and with dependents) tend to cancel less

Isn't it worth it for us to give a free number to the client's child, to the client's husband/wife?

- Low Customer Months have MUCH, but MUCH more chance to cancel:

Maybe the first customer experience is being bad
Maybe we're bringing unqualified customers
Idea: it might be interesting for us to create a customer incentive program in the first months

- Fiber customers have a very high cancellation fee:

We have to check the fiber service, we have a problem there

- The more services the customer has, the less chance he or she will cancel:

Gigantic Opportunity: Create an Incentive Program for Other Services

- Almost all company cancellations are in the monthly contract:

Incentive plan for the annual or 2-year contract -> let's give a discount to the annual contract guy

- Avoid Electronic Billing

Encourage customers to switch to credit or debit card
