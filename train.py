import pandas as pd
import re
import torch
import torch.nn as nn

from collections import Counter
from sklearn.model_selection import train_test_split
from torch.utils.data import Dataset, DataLoader

from model import SentimentLSTM

CSV_PATH = "data/training.1600000.processed.noemoticon.csv"

MAX_LEN = 30
VOCAB_SIZE = 10000
BATCH_SIZE = 64
EPOCHS = 3

print("Loading dataset...")

df = pd.read_csv(
    CSV_PATH,
    encoding="latin-1",
    header=None
)

df = df[[0, 5]]

df.columns = ["sentiment", "text"]

df["sentiment"] = df["sentiment"].replace(
    {4: 1}
)

# Use only first 50k tweets
df = df.head(50000)

def clean_text(text):
    text = text.lower()

    text = re.sub(r"http\S+", "", text)

    text = re.sub(r"[^a-zA-Z ]", "", text)

    return text

df["text"] = df["text"].apply(clean_text)

print("Building vocabulary...")

all_words = []

for text in df["text"]:
    all_words.extend(text.split())

counter = Counter(all_words)

vocab = {
    word: idx + 1
    for idx, (word, _)
    in enumerate(counter.most_common(VOCAB_SIZE - 1))
}

def encode(text):
    tokens = []

    for word in text.split():
        tokens.append(vocab.get(word, 0))

    tokens = tokens[:MAX_LEN]

    tokens += [0] * (MAX_LEN - len(tokens))

    return tokens

df["encoded"] = df["text"].apply(encode)

X = list(df["encoded"])
y = list(df["sentiment"])

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

class TweetDataset(Dataset):
    def __init__(self, X, y):
        self.X = torch.tensor(X)
        self.y = torch.tensor(y, dtype=torch.float32)

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

train_loader = DataLoader(
    TweetDataset(X_train, y_train),
    batch_size=BATCH_SIZE,
    shuffle=True
)

test_loader = DataLoader(
    TweetDataset(X_test, y_test),
    batch_size=BATCH_SIZE
)

device = torch.device(
    "cuda" if torch.cuda.is_available()
    else "cpu"
)

model = SentimentLSTM(
    vocab_size=VOCAB_SIZE
).to(device)

criterion = nn.BCEWithLogitsLoss()

optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)

print("Training...")

for epoch in range(EPOCHS):

    model.train()

    total_loss = 0

    for inputs, labels in train_loader:

        inputs = inputs.to(device)
        labels = labels.to(device)

        optimizer.zero_grad()

        outputs = model(inputs)

        loss = criterion(
            outputs,
            labels
        )

        loss.backward()

        optimizer.step()

        total_loss += loss.item()

    print(
        f"Epoch {epoch+1}/{EPOCHS} "
        f"Loss: {total_loss:.4f}"
    )

print("Evaluating...")

model.eval()

correct = 0
total = 0

with torch.no_grad():

    for inputs, labels in test_loader:

        inputs = inputs.to(device)

        outputs = model(inputs)

        predictions = (
            torch.sigmoid(outputs) > 0.5
        ).int()

        correct += (
            predictions.cpu()
            == labels.int()
        ).sum().item()

        total += len(labels)

accuracy = correct / total * 100

print(
    f"Accuracy: {accuracy:.2f}%"
)

torch.save(
    {
        "model_state": model.state_dict(),
        "vocab": vocab
    },
    "sentiment_model.pth"
)

print("Model saved.")