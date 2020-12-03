import matplotlib.pyplot as plt

for ip in hit_counter:

    hit = hit_counter[ip]

    ips = ip

    hits = hit

    if hit >= hit_count:

        print('{:20} {}'.format(ip,hit))

        plt.bar(ips, hits)

