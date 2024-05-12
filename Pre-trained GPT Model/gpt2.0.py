import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from torch.utils.data import Dataset, DataLoader
from torch.nn.utils.rnn import pad_sequence

# Define hyperparameters
MAX_LENGTH = 128
BATCH_SIZE = 8
LEARNING_RATE = 1e-4
NUM_EPOCHS = 3

# Load pre-trained GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Example conversation dataset
conversations = [
    "User: Hello! How are you?\nBot: I'm fine, thank you. How about you?",
    "User: What's your favorite book?\nBot: I don't have a favorite book, but I enjoy reading.",
    # Add more conversational data here
]

# Define dataset class
class ConversationDataset(Dataset):
    def __init__(self, conversations, tokenizer, max_length):
        self.conversations = conversations
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.conversations)

    def __getitem__(self, idx):
        conversation = self.conversations[idx]
        inputs = self.tokenizer.encode(conversation, add_special_tokens=False, return_tensors="pt").squeeze()
        if len(inputs) > self.max_length:
            inputs = inputs[:self.max_length]
        return inputs

# Pad sequences to ensure equal length in batches
def collate_fn(batch):
    return pad_sequence(batch, batch_first=True, padding_value=tokenizer.pad_token_id)

# Create dataset and dataloader
dataset = ConversationDataset(conversations, tokenizer, MAX_LENGTH)
dataloader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True, collate_fn=collate_fn)

# Set device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Define optimizer and loss function
optimizer = torch.optim.AdamW(model.parameters(), lr=LEARNING_RATE)
loss_fn = torch.nn.CrossEntropyLoss(ignore_index=tokenizer.pad_token_id)

# Training loop
for epoch in range(NUM_EPOCHS):
    model.train()
    total_loss = 0
    for batch in dataloader:
        inputs = batch.to(device)
        labels = inputs.clone()
        optimizer.zero_grad()
        outputs = model(inputs, labels=labels)
        loss = loss_fn(outputs.logits.view(-1, outputs.logits.size(-1)), labels.view(-1))
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    avg_loss = total_loss / len(dataloader)
    print(f"Epoch {epoch + 1}/{NUM_EPOCHS}, Average Loss: {avg_loss}")

# Save the fine-tuned model
model.save_pretrained("fine_tuned_chatgpt_model")
