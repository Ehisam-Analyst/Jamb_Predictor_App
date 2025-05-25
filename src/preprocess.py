import pandas as pd


# Drop duplicates
encoded_df.drop_duplicates(inplace=True)

# Drop rows where target column (e.g., JAMB_Score) is missing
encoded_df = encoded_df[encoded_df['JAMB_Score'].notna()]

# Drop rows with missing values in any column
encoded_df.dropna(inplace=True)

# Remove rows with invalid numeric data (e.g., negative scores or ages)
if 'JAMB_Score' in encoded_df.columns:
    encoded_df = encoded_df[encoded_df['JAMB_Score'] >= 0]

# Optional: Remove rows with unrealistic values (e.g., Age < 10 or > 100)
if 'Age' in encoded_df.columns:
    encoded_df = encoded_df[(encoded_df['Age'] >= 10) & (encoded_df['Age'] <= 100)]
    
# encoded_df = encoded_df.drop(['Student_ID'], axis=1)

# Reset index after cleaning
encoded_df.reset_index(drop=True, inplace=True)




