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

		if init == 'Normal':
			y = self.layer.in_features
			self.layer.weight.data.normal_(0.0,1/np.sqrt(y))
			self.layer.bias.data.fill_(0)
		elif init == 'Uniform':
			nn.init.uniform_(self.layer.weight)

	def forward(self, snt):
		x = self.layer(snt)
		# x = self.network(snt)
		# log_softmax = F.log_softmax(x, dim=1)
		probs = F.softmax(x, dim=1)
		# return [log_softmax, probs, x]
		return [x, probs]

labels = {"Statement": 0, "Answer": 1, "Opinion": 2, "Praphrase": 3}
model = MLP()

# loss_function = nn.NLLLoss()
loss_function = nn.CrossEntropyLoss()
# optimizer = optim.RMSprop(model.parameters(), lr=0.00001)
optimizer = optim.SGD(model.parameters(), lr=0.000008)
# optimizer = optim.Adam(model.parameters(), lr=0.000001)
batch_size = 12
epochs = 20

# This is a dictionary of sentence vectors and corresponding labels
# with open('train_vector_dict_480.json', 'r') as f:
# 	train_examples = json.load(f)

with open('data/newtrain_vector_dict_480.json', 'r') as f:
	train_examples = json.load(f)

with open('data/test_vector_dict_30.json', 'r') as f:
	test_examples = json.load(f)

print("Loaded Examples")

ids = []
low_effort_ex = []
mid_effort_ex = []
high_effort_ex = []
for i in range(len(train_examples)):
	idx = str(i+1)
	# ids.append(idx)
	if train_examples[idx][2] == 0:
		low_effort_ex.append(idx)
	elif train_examples[idx][2] == 1:
		mid_effort_ex.append(idx)
	else:
		high_effort_ex.append(idx)

print(len(low_effort_ex))
print(len(mid_effort_ex))
print(len(high_effort_ex))

random.shuffle(low_effort_ex)
random.shuffle(mid_effort_ex)
random.shuffle(high_effort_ex)

ids = low_effort_ex + mid_effort_ex + high_effort_ex

acc_list = []
ex_count = 0
example_seen_list = []
iterations = len(train_examples) // batch_size
print(iterations)

for e in range(iterations):

	for idn in ids[e*batch_size: batch_size + e*batch_size]:
		example_seen_list.append(idn)

	# Train for all examples seen so far
	print(idn)
	for epoch in range(epochs):
		random.shuffle(example_seen_list)
		for inst in example_seen_list:
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

	acc = correct_count*100 / len(test_examples)
	acc_list.append(acc)
	print("Current Test Accuracy: {}".format(acc))

	effort = 0
	for ele in example_seen_list:
		effort += train_examples[ele][3] 
	effort = effort / len(example_seen_list)
	print("Average Effort: {}, Examples seen: {}".format(effort, len(example_seen_list)))

plt.plot(acc_list)
plt.show()
			







