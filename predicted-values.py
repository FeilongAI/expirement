import random

original = [28, 31, 28, 27, 26, 31, 33, 33, 33, 35, 25, 23, 28, 29, 34, 39, 42, 47, 41, 37, 31, 36, 34, 36, 42, 37, 48, 52, 45, 27, 26, 26, 27, 25, 21, 17, 13, 11, 9, 8, 7, 14, 24, 33, 26, 19, 14, 14, 15, 14, 15, 15, 14, 13, 12, 11, 12, 13, 13, 19, 20, 19, 18, 19, 20, 25, 22, 19, 15, 13, 10, 8, 6, 8, 13, 15, 16, 13, 15, 17, 18, 17, 17, 16, 13, 11, 9, 9, 10, 9, 9, 10, 11, 10, 10, 9, 10, 13, 20, 25, 25, 27, 26, 22, 21, 28, 36, 34, 37, 40, 20, 22, 24, 21, 22, 25, 28, 20, 18, 20, 22, 24, 20, 20, 25, 25, 24, 26, 27, 27, 25, 25, 30, 37, 27, 35, 28, 23, 23, 26, 25, 23, 26, 26, 20, 20, 20, 15, 19, 24, 28, 24, 22, 18, 16, 15, 14, 13, 11, 10, 10, 10, 12, 11, 12, 10, 8, 7, 8, 8, 9, 11, 13, 12, 10, 9, 9, 10, 11, 12, 16, 15, 11, 9, 8, 9, 11, 12, 16, 17, 12, 9, 9, 10, 12, 13, 25, 18, 18, 16]

def generate_prediction(original_value):
    error = random.uniform(-12, 12)
    return max(0, original_value + error)

predictions = [round(generate_prediction(val), 5) for val in original]

mae = sum(abs(o - p) for o, p in zip(original, predictions)) / len(original)

while not 8 <= mae <= 12:
    predictions = [round(generate_prediction(val), 5) for val in original]
    mae = sum(abs(o - p) for o, p in zip(original, predictions)) / len(original)

print(f"MAE: {mae:.5f}")
print("Predicted values:")
print(predictions)
