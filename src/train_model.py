from sklearn.model_selection import train_test_split

# Features and target
X = encoded_df.drop(columns=['JAMB_Score'])    
y = encoded_df['JAMB_Score']

# Split into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#train model

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
