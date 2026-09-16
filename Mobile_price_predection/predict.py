
import pandas as pd
import joblib


# ==========================================
# 1. LOAD TRAINED MODEL
# ==========================================

model = joblib.load("model/model.pkl")


print("\n===================================")
print("       MOBILE PRICE PREDICTION")
print("===================================\n")


# ==========================================
# 2. GET USER INPUT
# ==========================================

ram = float(input("Enter RAM (GB): "))

storage = float(input("Enter Storage (GB): "))

battery = float(input("Enter Battery (mAh): "))

camera = float(input("Enter Camera (MP): "))

screen_size = float(input("Enter Screen Size (inches): "))

processor_speed = float(
    input("Enter Processor Speed (GHz): ")
)


# ==========================================
# 3. CREATE INPUT DATA
# ==========================================

new_mobile = pd.DataFrame({
    "ram": [ram],
    "storage": [storage],
    "battery": [battery],
    "camera": [camera],
    "screen_size": [screen_size],
    "processor_speed": [processor_speed]
})


# ==========================================
# 4. PREDICT PRICE
# ==========================================

predicted_price = model.predict(new_mobile)


# ==========================================
# 5. DISPLAY RESULT
# ==========================================

print("\n===================================")

print(
    "Predicted Mobile Price: ₹",
    round(predicted_price[0], 2)
)

print("===================================\n")
