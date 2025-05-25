import numpy as np
sample_student = np.array([18, 70, 1, 2, 1, 1, 1, 1, 1, 2, 17, 0, 1, 0, 2]).reshape(1, -1)

# Predict
predicted_score = model.predict(sample_student)
print("🎯 Predicted JAMB Score:", round(predicted_score[0], 2))
