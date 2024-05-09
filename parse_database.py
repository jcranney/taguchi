import json

in_filename = "database.txt"
out_filename = "database.json"
with open(in_filename,"r") as f:
    lines = f.readlines()

batches = {}
for line in lines:
    if line[:3] == "###":
        n_params = int(line.split(" ")[1].split("=")[1])
        n_states = int(line.split(" ")[2].split("=")[1])
        this_batch = []
        continue
    if line[0] in " c":
        continue
    if line[0] == ">":
        data = [[int(x)-1 for x in d] for d in this_batch]
        batches[f'{n_params:d},{n_states:d}'] = data
        continue
    this_batch.append(line.split()[1:])

with open(out_filename,"w") as f:
    json.dump(batches,f)