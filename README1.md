## Sample Data and Query

This repository includes sample embeddings and query scripts for quick testing.

### Sample Data

The file `data/sample_embeddings.json` contains 100 sample embeddings with 128 dimensions, saved in JSON format.

### Usage Instructions

1. **Generate and Load Sample Data**:
   - Use `sample_query.py` to create and search for embeddings in Milvus.
   - Make sure Milvus is running on `localhost:19530` or adjust the script accordingly.

2. **Run the Query**:
   ```bash
   python sample_query.py
