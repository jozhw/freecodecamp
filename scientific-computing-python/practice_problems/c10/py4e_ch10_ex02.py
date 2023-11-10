f_name = input('File name: ')
try:
    open_name = open(f_name)
except:
    print('File: ', f_name, ' does not exist.')
    exit()

times = {}

for line in open_name:
    line = line.capitalize()
    words = line.split()
    for word in words:
        if len(words) == 0 or words[0] != 'From':
            #print('no email sent')
            continue
        else:
            #print(words[:6])
                #remember that [:6] is the beginning to the 7th, but not
                #including the 7th
            #print(words[5])
            hours = words[5].split(':')
            spechours = hours[0]
            times[spechours] = times.get(spechours, 0) + 1

print(times)

time_order = []

for k,v in times.items():
    new_order = (v,k)
    time_order.append(new_order)

print(sorted(time_order, reverse=True))
