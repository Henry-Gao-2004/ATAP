import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
from torch.nn.utils.rnn import pad_sequence
from collections import defaultdict

# Sample data
texts = [
    "I love this product", "This is terrible", "Absolutely wonderful", 
    "Horrible experience", "Best thing ever", "Not good", 
    "Fantastic", "Worst I've had", "Really good", "So bad"
]
labels = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

# TODO: add tokenizer
# Tokenize
def tokenize(text):
    return text.lower().split()

# Build vocab
word2idx = defaultdict(lambda: len(word2idx))
PAD_IDX = 0
word2idx["<PAD>"] = PAD_IDX

tokenized_texts = [tokenize(t) for t in texts]
indexed_texts = [[word2idx[token] for token in tokens] for tokens in tokenized_texts]

# Pad
tensor_texts = [torch.tensor(seq, dtype=torch.long) for seq in indexed_texts]
padded_texts = pad_sequence(tensor_texts, batch_first=True, padding_value=PAD_IDX)
labels = torch.tensor(labels, dtype=torch.float32).unsqueeze(1)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(padded_texts, labels, test_size=0.2, random_state=42)

# Model with attention
class AttentionLogisticRegression(nn.Module):
    def __init__(self, vocab_size, embedding_dim):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim, padding_idx=PAD_IDX)
        self.attention = nn.Linear(embedding_dim, 1) # TODO: attention, not linear
        self.classifier = nn.Linear(embedding_dim, 1)

    def forward(self, x):
        emb = self.embedding(x)  # (batch, seq_len, embed_dim)
        scores = self.attention(emb).squeeze(-1)  # (batch, seq_len)

        # Mask padding
        mask = (x != PAD_IDX)
        scores = scores.masked_fill(~mask, float('-inf'))

        # Softmax over valid tokens
        attn_weights = torch.softmax(scores, dim=1).unsqueeze(-1)  # (batch, seq_len, 1)

        # Weighted sum of embeddings
        context = torch.sum(emb * attn_weights, dim=1)  # (batch, embed_dim)

        # Final classification
        output = self.classifier(context)
        return torch.sigmoid(output)

# Init model
vocab_size = len(word2idx)
embedding_dim = 50
model = AttentionLogisticRegression(vocab_size, embedding_dim)
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# Train
epochs = 30
for epoch in range(epochs):
    model.train()
    optimizer.zero_grad()
    outputs = model(X_train)
    loss = criterion(outputs, y_train)
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 5 == 0:
        print(f"Epoch {epoch+1}/{epochs}, Loss: {loss.item():.4f}")

# Eval
model.eval()
with torch.no_grad():
    preds = model(X_test)
    pred_classes = (preds > 0.5).float()
    accuracy = (pred_classes == y_test).float().mean()
    print(f"Test Accuracy: {accuracy:.4f}")
