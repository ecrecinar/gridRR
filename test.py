l = []

l.append([("A", i) for i in range(15)])
l.append([("B", i) for i in range(15, 20)])
l.append([("C", i) for i in range(20, 25)])

log = []
for item in l:
    for p in item:
        log.append(p)

condensed_log = []

current_item = log[0][0]
start_time = log[0][1]
end_time = start_time
for i in range(len(log)):
    if i == len(log) - 1:
        condensed_log.append((current_item, start_time, end_time))

    if log[i][0] == current_item:
        end_time = log[i][1]
    else:
        condensed_log.append((current_item, start_time, end_time))
        current_item = log[i][0]
        start_time = log[i][1]
        end_time = start_time

for item in log:
    print(item)

for item in condensed_log:
    print(item)
