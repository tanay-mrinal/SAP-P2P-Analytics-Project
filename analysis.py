import pandas as pd
import matplotlib.pyplot as plt

# Read Excel (adjust header if needed)
data = pd.read_excel("p2p_data(2305742).xlsx", header=2)

# Clean column names
data.columns = data.columns.str.strip()

# 🔥 Find correct column names dynamically
vendor_col = [col for col in data.columns if "Vendor" in col][0]
total_col = [col for col in data.columns if "Total" in col][0]

# Group by Vendor
vendor_total = data.groupby(vendor_col)[total_col].sum()

print("Vendor-wise Procurement:\n")
print(vendor_total.to_string().encode('ascii', 'ignore').decode())

# Plot
vendor_total.plot(kind='bar')

plt.title("Vendor-wise Procurement (₹)")
plt.xlabel("Vendor")
plt.ylabel("Total Amount (₹)")

plt.savefig("python_chart.png")
plt.show()