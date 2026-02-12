import pandas as pd
import pickle
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

# Load cleaned dataset
df = pd.read_csv("data/processed/civic_eye_nlp_ready.csv")

# Load SBERT model (FAST & efficient)
model = SentenceTransformer("all-MiniLM-L6-v2")

# Convert text column to list
texts = df["final_text"].astype(str).tolist()

print("Generating SBERT embeddings...")
embeddings = model.encode(
    texts,
    batch_size=64,
    show_progress_bar=True,
    normalize_embeddings=True
)

# Save embeddings + labels
with open("data/processed/Sbert_embeddings.pkl", "wb") as f:
    pickle.dump(
        {
            "embeddings": embeddings,
            "labels": df["category"].tolist()
        },
        f
    )

print("✅ SBERT embeddings saved successfully!")
print("Embedding shape:", embeddings.shape)
