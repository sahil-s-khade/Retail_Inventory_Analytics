import pandas as pd

df = pd.read_csv("data/processed/final_featured_data.csv")

sample_df = df.sample(20000, random_state=42)

sample_df.to_csv(
    "data/processed/final_featured_data_sample.csv",
    index=False
)

print("Sample file created")
print(sample_df.shape)