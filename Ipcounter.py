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
