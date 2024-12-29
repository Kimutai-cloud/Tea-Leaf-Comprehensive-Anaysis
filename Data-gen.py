import random
import pandas as pd

def generate_ml_training_data(num_samples=500):
    growth_stages = ["Young", "Mature"]
    
    data = {
        "N_level": [round(random.uniform(0, 250), 2) for _ in range(num_samples)],
        "P_level": [round(random.uniform(0, 50), 2) for _ in range(num_samples)],
        "K_level": [round(random.uniform(0, 250), 2) for _ in range(num_samples)],
        "pH": [round(random.uniform(4.0, 6.5), 2) for _ in range(num_samples)],
        "rainfall": [round(random.uniform(0, 300), 2) for _ in range(num_samples)],  # mm
        "temperature": [round(random.uniform(10, 35), 2) for _ in range(num_samples)],  # °C
        "growth_stage": [random.choice(growth_stages) for _ in range(num_samples)],
        "N_rec": [random.randint(50, 200) for _ in range(num_samples)],
        "P_rec": [random.randint(20, 50) for _ in range(num_samples)],
        "K_rec": [random.randint(50, 200) for _ in range(num_samples)],
        "pH_adj": [random.choice(["Apply Lime", "Use Ammonium Sulfate", "No Adjustment"]) for _ in range(num_samples)],
    }
    return pd.DataFrame(data)

ml_training_data = generate_ml_training_data()
ml_training_data.to_csv("ml_training_data.csv", index=False)
print("Training data saved to 'ml_training_data.csv'")
