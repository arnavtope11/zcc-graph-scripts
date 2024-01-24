import json

# Open the file
json_fd = open('client.json', 'r')
dataset = json.load(json_fd)
new_dataset = {}
print(dataset[1].keys())

for thread_ in dataset[1].keys():
    for time_slice in dataset[1][thread_]['latency_bucketed'].keys():
        if time_slice not in new_dataset.keys():
            new_dataset[time_slice] = []
        new_dataset[time_slice].append(dataset[1][thread_]['latency_bucketed'][time_slice])
print(new_dataset)
# for thread_ in dataset[1].keys():
#     for 
#     if time_slice not in new_dataset.keys():
#         new_dataset[time_slice] = []
#     new_dataset[time_slice]['latency_bucketed'].append(dataset[1]['latency_bucketed'][time_slice])
# print(new_dataset)