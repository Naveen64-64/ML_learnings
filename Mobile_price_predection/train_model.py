import pandas as pd
import matplotlib.pyplot as plt
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
data = pd.read_csv("data/mobile_price_dataset.csv")
print("Dataset loaded successfully!")
print("\nFirst 5 rows:")
print(data.head())
X = data[
    [
        "ram",
        "storage",
        "battery",
        "camera",
        "screen_size",
        "processor_speed"
    ]
]
y = data["price"]
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
print("\nTraining rows:", len(X_train))
print("Testing rows:", len(X_test))
model = LinearRegression()
model.fit(X_train, y_train)
print("\nModel trained successfully!")
print("\nModel Coefficients:")
for feature, coefficient in zip(X.columns, model.coef_):
    print(feature, ":", coefficient)
print("\nIntercept:", model.intercept_)
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)
print("\n==============================")
print("MODEL EVALUATION")
print("==============================")
print("MAE :", round(mae, 2))
print("MSE :", round(mse, 2))
print("RMSE:", round(rmse, 2))
print("R2 Score:", round(r2, 4))
comparison = pd.DataFrame({
    "Actual Price": y_test.values,
    "Predicted Price": y_pred
})
print("\nActual vs Predicted:")
print(comparison)
plt.figure(figsize=(8, 5))
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual Price vs Predicted Price")
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()]
)
plt.tight_layout()
plt.savefig("actual_vs_predicted.png")
plt.show()
plt.figure(figsize=(8, 5))
plt.scatter(data["ram"], data["price"])
plt.xlabel("RAM (GB)")
plt.ylabel("Price (₹)")
plt.title("RAM vs Mobile Price")
plt.tight_layout()
plt.savefig("ram_vs_price.png")
plt.show()
joblib.dump(model, "model/model.pkl")

print("\nModel saved successfully!")
print("Location: model/model.pkl")