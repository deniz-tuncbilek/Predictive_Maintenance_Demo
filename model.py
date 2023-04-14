import pickle
import joblib

# load saved model
model = joblib.load('RUL_SVR.sav')

# pickle and load the model
pickle.dump(model, open('model.pkl', 'wb'))

model = pickle.load(open('model.pkl','rb'))
print(model.predict([[641.82, 1589.70, 1400.60, 554.36, 2388.06, 9046.19, 47.47, 521.66, 2388.02, 8138.62, 8.4195, 392, 39.06, 23.4190]]))