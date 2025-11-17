import pandas as pd
import numpy as np

# Generate sample data for DVC demo
np.random.seed(42)

# Create a sample dataset
data = {
    'age': np.random.randint(18, 80, 100),
    'salary': np.random.randint(20000, 150000, 100),
    'experience': np.random.randint(0, 40, 100),
    'performance_score': np.random.uniform(1, 5, 100).round(2),
    'department': np.random.choice(['Sales', 'IT', 'HR', 'Finance'], 100)
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('sample_data.csv', index=False)

print("Sample data created and saved to sample_data.csv")
print(df.head(10))

print("Hello World" \
"")