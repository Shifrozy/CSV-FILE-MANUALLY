# Writing CSV manually
data = [
    ["Date", "Action", "Price"],
    ["2025-09-01", "BUY", 210.5],
    ["2025-09-02", "SELL", 215.8],
]

with open("trades.csv", "w") as file:
    for row in data:
        line = ",".join(map(str, row))  # convert list to comma-separated string
        file.write(line + "\n")

print("CSV file created successfully!")
