# Import pandas
import pandas as pd
# Import matplotlib for plotting
import matplotlib.pyplot as plt

# Read a CSV file into a DataFrame
df = pd.read_csv('Financial_Data.csv')

# Extracting the needed columns for phone banking
df_target_phone = df[["txn_description", "gender", "age", "customer_id"]]

# Filtering out to see which Gender used the most phone banking
df_target_phone_gender = df_target_phone[df_target_phone["txn_description"] == "PHONE BANK"]
df_target_phone_gender = df_target_phone_gender[["gender", "txn_description"]]
df_target_phone_gender = df_target_phone_gender.groupby("gender").count()
df_target_phone_gender.rename(columns={"txn_description": "Count"}, inplace=True)
df_target_phone_gender = df_target_phone_gender.reset_index()

# Plotting the distribution of phone banking by Gender
plt.figure(figsize=(6, 4))
plt.bar(df_target_phone_gender["gender"], df_target_phone_gender["Count"])
plt.title("Phone Banking Transactions by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Transactions")
plt.show()
plt.clf()

# Filtering out to see which age used the most phone banking
df_target_phone_age = df_target_phone[df_target_phone["txn_description"] == "PHONE BANK"]
df_target_phone_age = df_target_phone_age[["age", "txn_description"]]
df_target_phone_age = df_target_phone_age.groupby("age").count()
df_target_phone_age.rename(columns={"txn_description": "Count"}, inplace=True)
df_target_phone_age = df_target_phone_age.reset_index()

# Plotting the distribution of phone banking by Age
plt.figure(figsize=(10, 5))
plt.bar(df_target_phone_age["age"], df_target_phone_age["Count"])
plt.title("Phone Banking Transactions by Age")
plt.xlabel("Age")
plt.ylabel("Number of Transactions")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.clf()

# Extracting the needed columns for transaction amount analysis
df_target = df[["gender", "age", "amount", "customer_id", "movement"]]

# Grouping by customer_id, movement, gender and age, and summing the amount
df_target_amount = df_target.groupby(["customer_id", "age", "gender","movement"])["amount"].sum().unstack(fill_value=0)
df_target_amount["net_income"] = df_target_amount["credit"] - df_target_amount["debit"]
df_target_amount = df_target_amount.reset_index()

# Filter to see which gender has the highest net income
df_target_amount_gender = df_target_amount[["gender", "net_income"]]
df_target_amount_gender = df_target_amount.groupby("gender")[["net_income"]].sum().reset_index()
df_target_amount_gender = df_target_amount_gender[["gender", "net_income"]]
df_target_amount_gender = df_target_amount_gender.reset_index()

# Plotting the distribution of net credit by Gender
plt.figure(figsize=(6, 4))
plt.bar(df_target_amount_gender["gender"], df_target_amount_gender["net_income"], color=['skyblue', 'salmon'])
plt.title("Net Income by Gender")
plt.xlabel("Gender")
plt.ylabel("Total Net Income")
plt.tight_layout()
plt.show()

# Filter to see which Age has the highest net income
df_target_amount_age = df_target_amount[["age", "net_income"]]
df_target_amount_age = df_target_amount.groupby("age")[["net_income"]].mean().reset_index()
df_target_amount_age = df_target_amount_age[["age", "net_income"]]
df_target_amount_age = df_target_amount_age.reset_index()

# Plotting the distribution of net credit by Age
plt.figure(figsize=(10, 6))
plt.bar(df_target_amount_age["age"], df_target_amount_age["net_income"], color='mediumseagreen')
plt.title("Net Income by Age")
plt.xlabel("Age")
plt.ylabel("Total Net Income")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
