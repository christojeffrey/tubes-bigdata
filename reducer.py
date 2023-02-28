# myxl    2022-02-11      1
# myxl    2022-02-11      1
# myxl    2022-02-11      1
# myxl    2022-02-11      1
# count all in the same date
# read from stdin
import sys

counter = {}
for line in sys.stdin:
    line = line.strip()
    socialMedia, time, count = line.split("\t")

    if socialMedia not in counter:
        counter[socialMedia] = {}
    if time not in counter[socialMedia]:
        counter[socialMedia][time] = 0

    counter[socialMedia][time] += int(count)

# print
for socialMedia in counter:
    for time in counter[socialMedia]:
        print(socialMedia + "\t" + time + "\t" + str(counter[socialMedia][time]))

# output as csv
csv = open('output.csv', 'w')
csvString = 'socialMedia,time,count'
for socialMedia in counter:
    for time in counter[socialMedia]:
        csvString += socialMedia + "," + time + "," + str(counter[socialMedia][time]) + "\n"

csv.write(csvString)

