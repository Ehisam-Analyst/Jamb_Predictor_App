# Save the model for future use
import joblib
joblib.dump(model, "../models/jamb_score_predictor.pkl")

model = joblib.load("../models/jamb_score_predictor.pkl")