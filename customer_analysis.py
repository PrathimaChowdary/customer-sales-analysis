# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("customer_sales_data.csv")

# Preview data
print(df.head())

# Add Total Price column
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

# Sales by Region
sales_by_region = df.groupby("Region")["TotalPrice"].sum().reset_index()

# Plot sales by region
plt.figure(figsize=(8,5))
sns.barplot(data=sales_by_region, x="Region", y="TotalPrice", palette="Blues_d")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales ($)")
plt.tight_layout()
plt.savefig("sales_by_region.png")
plt.show()

# Top selling products
top_products = df.groupby("Product")["Quantity"].sum().sort_values(ascending=False)
print("Top selling products:\n", top_products)