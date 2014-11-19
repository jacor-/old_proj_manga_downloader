from os import system


parallell_instances = 20;
first = 300
last = 700
down = range(first,last)

current = first

step = int((last-first+1)/parallell_instances)
if step*parallell_instances != last-first+1:
    step = step + 1

while current < parallell_instances:
    system("python download_scriptFromTo.py " + str(current*step+1) + " " + str((current+1)*step+1) + " &")
    print "running process " + str(current)
    current = current+1

