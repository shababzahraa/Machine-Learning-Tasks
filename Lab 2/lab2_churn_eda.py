print("\n")

import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
df = pd.read_csv("TelcoCustomerChurn.csv")


print("Total Customers : ", df.shape[0])
print("Total features : ", df.shape[1])
print("Numerical Features: ",df.describe(include="number").columns)
print("Categorical Features : ",df.describe(include='object').columns)

print(df.dtypes)

print("Missing Values :\n",df.isnull().sum())
print("Missing Value Percentage per column:\n",df.isnull().mean()*100)


print("Duplicate Rows: ",df.duplicated().sum())
print("Duplicate CustomerID: ",df['customerID'].duplicated().sum())



# temp['TotalCharges']=pd.to_numeric(df['TotalCharges'], errors='coerce')
# print(temp.isna().sum())

# drop_customerID = df.drop(columns=['customerID'])
# temp.dropna(subset=['TotalCharges'])

# print("TotalCharges data type:", df['TotalCharges'].dtype)
# print("Missing total charges: ", temp['TotalCharges'].isna().sum())



# print("Missing TotalCharges:", df_clean['TotalCharges'].isna().sum())
# df['tenure'].plot(kind='hist', bins=20)
# plt.show()


for col in ['Contract', 'InternetService', 'PaymentMethod']:
    print("\n", col)
    print(df[col].unique())


# Convert TotalCharges to numeric
df['TotalCharges'] = pd.to_numeric(
    df['TotalCharges'],
    errors='coerce'
)
df['TotalCharges'] = df['TotalCharges'].fillna(df['TotalCharges'].mean())


plt.figure(figsize=(8,5))
plt.hist(df['tenure'], bins=20)
plt.title("Distribution of customer Tenure")
plt.xlabel('Tenure(Months)')
plt.ylabel('Number of Customers')
plt.show()


plt.figure(figsize=(8,5))
plt.hist(df['MonthlyCharges'], bins=20)
plt.title("Distribution of Monthly Charges")
plt.xlabel('Monthly Charges')
plt.ylabel('Number of customers')
plt.show()

plt.figure(figsize=(8,5))
count = df['Contract'].value_counts()
plt.bar(count.index, count.values)
plt.title("Distribution of Contract type")
plt.xlabel('Contract')
plt.ylabel('Number of customers')
plt.show()


plt.figure(figsize=(10,6))
df['PaymentMethod'].value_counts().plot(kind="bar")
plt.title("Distribution Payment Method")
plt.xlabel('PaymentMethod')
plt.ylabel('Number of customers')
plt.tight_layout()
plt.show()

print("Number of churned vs non churned: ", df['Churn'].value_counts())
print("Percentage of churned vs non churned: ", df['Churn'].value_counts(normalize=True) * 100)


churn_by_contract = (pd.crosstab(df['Contract'], df['Churn'],normalize='index')*100).round(2)
print(churn_by_contract)
churn_by_contract.plot(kind='bar')
plt.tight_layout()
churn_by_internet=(pd.crosstab(df['InternetService'],df['Churn'],normalize='index')*100).round(2)
print(churn_by_internet)
churn_by_internet.plot(kind='bar')
plt.tight_layout()
plt.show()

plt.figure(figsize=(7,5))
sns.boxplot(x='Churn', y='tenure', data=df)
plt.title("Tenure Distribution by Churn status")
plt.xlabel('churn')
plt.ylabel('tenure')
plt.tight_layout()
plt.show()

plt.figure(figsize=(7,5))
sns.boxplot(x='Churn', y='MonthlyCharges', data=df)
plt.title("Monthly Charges Distribution by Churn status")
plt.xlabel('churn')
plt.ylabel('Monthly Charges')
plt.tight_layout()
plt.show()



corr_matrix = df.corr(numeric_only=True)
print(corr_matrix)
sns.heatmap(corr_matrix, annot=True)
plt.figure(figsize=(8,6))
plt.title('Correlation Matrix')
plt.tight_layout
plt.show()


df_clean = df.copy()

print(df_clean.info())
df_clean = df.drop(columns=['customerID'])
df_clean['TotalCharges'] = pd.to_numeric(df_clean['TotalCharges'],errors='coerce')
df_clean = df_clean.dropna(subset=['TotalCharges'])
print("customerID present:", 'customerID' in df_clean.columns)
print("TotalCharges data type:", df_clean['TotalCharges'].dtype)
df_clean.to_csv('Clean_churn.csv', index=False)