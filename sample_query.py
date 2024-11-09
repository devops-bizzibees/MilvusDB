from pymilvus import Collection, FieldSchema, CollectionSchema, DataType, connections
import json

# Step 1: Connect to Milvus
connections.connect("default", host="127.0.0.1", port="19530")

# Step 2: Define and Create Collection Schema
field1 = FieldSchema(name="id", dtype=DataType.INT64, is_primary=True)
field2 = FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=128)
schema = CollectionSchema(fields=[field1, field2], description="sample collection")
collection = Collection(name="sample_collection", schema=schema)

# Step 3: Load Sample Data
with open("data/sample_embeddings.json", "r") as file:
    data = json.load(file)

# Insert sample data into Milvus
collection.insert([data["ids"], data["embeddings"]])

# Step 4: Perform a Similarity Search
query_vector = np.random.rand(128).tolist()
search_params = {"metric_type": "L2", "params": {"nprobe": 10}}
results = collection.search([query_vector], "embedding", param=search_params, limit=5)

# Display Results
for result in results[0]:
    print(f"ID: {result.id}, Distance: {result.distance}")
