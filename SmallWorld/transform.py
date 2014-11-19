with open("facebook_combined.txt") as f:
    content = map(lambda line: line.replace(" ", ";"), f.readlines())


with  open('facebook_converted.csv','w') as f:
    for line in content:
        f.write(line)

    f.close()