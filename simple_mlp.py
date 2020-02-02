import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import json
import matplotlib.pyplot as plt
import numpy as np
import random

# Batch will always be 1
# Input 1 x 4096
# Output 1 x 4

# Using mLSTM to tackle issues like outlier words
# Words in train set and test set differ


class MLP(nn.Module):
	def __init__(self, init = 'Normal'):
		super(MLP, self).__init__()
		# self.network = nn.Sequential(nn.Linear(4096, 128),
		# 							nn.Linear(128, 4))
		self.layer = nn.Linear(4096, 4, bias = True)

		# Uncomment if desire different network initializations
		# if init == 'Normal':
		# 	y = self.layer.in_features
		# 	self.layer.weight.data.normal_(0.0,1/np.sqrt(y))
		# 	self.layer.bias.data.fill_(0)
		# elif init == 'Uniform':
		# 	nn.init.uniform_(self.layer.weight)

	def forward(self, snt):
		x = self.layer(snt)
		# x = self.network(snt)
		probs = F.softmax(x, dim=1)
		return [x, probs]

labels = {"Statement": 0, "Answer": 1, "Opinion": 2, "Praphrase": 3}
model = MLP()

loss_function = nn.CrossEntropyLoss()
# optimizer = optim.RMSprop(model.parameters(), lr=0.0001)
optimizer = optim.SGD(model.parameters(), lr=0.000008)
# optimizer = optim.Adam(model.parameters(), lr=0.0001)
batch_size = 12
epochs = 20

# This is a dictionary of sentence vectors and corresponding labels
with open('data/train_vector_dict_480.json', 'r') as f:
	train_examples = json.load(f)

with open('data/test_vector_dict_30.json', 'r') as f:
	test_examples = json.load(f)

print("Loaded Examples")

acc_list = []
ex_count = 0
iterations = len(train_examples) // batch_size
example_seen_list_all = []

while ex_count < iterations:
	# Find low confidence example
	# Here we consider least confidence sampling
	with torch.no_grad():
		example_seen_list = []
		for j in range(batch_size):
			min_conf = 1.0
			max_ent = -10.0
			curr_idx = -1
			for i in range(len(train_examples)):
				idx = str(i+1)
				if idx not in example_seen_list_all:
					input_utt = torch.from_numpy(np.asarray(train_examples[idx][0])).float().unsqueeze(0)
					gt_label = torch.LongTensor([int(train_examples[idx][1])])
					probs = model(input_utt)[1]
					# Least Confidence Sampling
					# curr_conf = torch.max(probs).item()
					# if curr_conf <= min_conf:
					# 	min_conf = curr_conf
					# 	curr_idx = idx

					# Margin Sampling
					# probas_val = probs.data.numpy()
					# rev = np.sort(probas_val, axis=1)[:, ::-1]
					# curr_conf = rev[:, 0] - rev[:, 1]
					# if curr_conf <= min_conf:
					# 	min_conf = curr_conf
					# 	curr_idx = idx

					# Entropy Sampling
					probas_val = probs.data.numpy()
					e = (-probas_val * np.log2(probas_val)).sum()
					if e > max_ent:
						max_ent = e
						curr_idx = idx


			example_seen_list_all.append(curr_idx)
			example_seen_list.append(curr_idx)

	print(curr_idx)
	for epoch in range(epochs):
		random.shuffle(example_seen_list_all)
		for inst in example_seen_list_all:
			model.zero_grad()
			curr_utt = torch.from_numpy(np.asarray(train_examples[inst][0])).float().unsqueeze(0)
			curr_label = torch.LongTensor([int(train_examples[inst][1])])
			log_probs = model(curr_utt)[0]
			loss = loss_function(log_probs, curr_label)
			loss.backward()
			optimizer.step()	

	# Get train Accuracy
	correct_count = 0
	with torch.no_grad():
		for i in range(len(train_examples)):
			idx = str(i+1)
			input_utt = torch.from_numpy(np.asarray(train_examples[idx][0])).float().unsqueeze(0)
			gt_label = torch.LongTensor([int(train_examples[idx][1])])
			probs = model(input_utt)[1]
			conf, pred = torch.max(probs, 1)
			if pred == gt_label:
				correct_count += 1

	acc = correct_count*100 / len(train_examples)
	print("Current Train Accuracy: {}".format(acc))

	# Get test Accuracy
	correct_count = 0
	with torch.no_grad():
		for i in range(len(test_examples)):
			idx = str(i+1)
			input_utt = torch.from_numpy(np.asarray(test_examples[idx][0])).float().unsqueeze(0)
			gt_label = torch.LongTensor([int(test_examples[idx][1])])
			probs = model(input_utt)[1]
			conf, pred = torch.max(probs, 1)
			if pred == gt_label:
				correct_count += 1

	ex_count += 1

	acc = correct_count / len(test_examples)
	acc_list.append(acc)
	print("Current Test Accuracy: {}".format(acc))

plt.plot(acc_list)
plt.show()
			







