import pandas as pd
from sklearn.preprocessing import StandardScaler

# ================= EXTRACT =================
df = pd.read_csv("students.csv")

# ================= TRANSFORM =================
# Handle missing values (correct way)
df["Age"] = df["Age"].fillna(df["Age"].mean())

for col in ["Maths", "Science", "English"]:
    df[col] = df[col].fillna(df[col].mean())

# Feature engineering
df["Total"] = df[["Maths", "Science", "English"]].sum(axis=1)
df["Average"] = df["Total"] / 3

# Scaling using scikit-learn
scaler = StandardScaler()
df[["Maths", "Science", "English"]] = scaler.fit_transform(
    df[["Maths", "Science", "English"]]
)

# ================= LOAD =================
df.to_csv("cleaned_students.csv", index=False)
