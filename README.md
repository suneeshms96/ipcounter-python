# ipcounter-python
A python program to count the IP connections and display it as graph


import matplotlib.pyplot as plt

logfile = 'access.log'
hit_count = 500

with open (logfile) as logobj:
    hit_counter = {}
    for line in logobj:
        ip = line.split()[0]
        if ip not in hit_counter:
            hit_counter[ip] = 1
        else:
            hit_counter[ip] = hit_counter[ip] + 1

for ip in hit_counter:
    hit = hit_counter[ip]
    ips = ip
    hits = hit
    if hit >= hit_count:
        print('{:20} {}'.format(ip,hit))
        plt.bar(ips, hits)

