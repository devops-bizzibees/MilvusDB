import json
import numpy as np

# Generate sample embeddings
sample_data = {
    "ids": [i for i in range(100)],  # IDs for the vectors
    "embeddings": [np.random.rand(128).tolist() for _ in range(100)]  # 128-dimensional vectors
}

# Save to JSON file
with open("sample_embeddings.json", "w") as file:
    json.dump(sample_data, file)

print("Sample embeddings generated and saved to sample_embeddings.json")
