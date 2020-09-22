import psutil
import time
import json
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-i", help="Interval between snapshots", type=int, default=30)
parser.add_argument("-t", help="Output file type", default="txt")
args = parser.parse_args()


class monitor:
    def __init__(self, t):
        self.t = t

    def txt(self):
        outputfile = "monitor.txt"
        count = 0
        while True:
            myfile2 = open(outputfile, mode='a', encoding='latin_1')
            count = count + 1
            list1 = psutil.getloadavg()
            list2 = psutil.disk_usage('/')
            list3 = psutil.virtual_memory()
            myfile2.write("SNAPSHOT " + str(count))
            myfile2.write(" Date: " + time.asctime())
            myfile2.write(" Overall CPU load: " + str(list1[2]) + "%")
            myfile2.write(" Overall memory usage: " + str(list2[1] // 1048576) + "mb")
            myfile2.write(" Overall virtual memory usage: " + str(list3[3] // 1048576) + "mb\n")
            myfile2.close()
            time.sleep(int(self.t))

    def json(self):
        outputfile = 'monitor.json'
        count = 0
        while True:
            myfile = open(outputfile, mode='a', encoding='latin-1')
            count = count + 1
            list1 = psutil.getloadavg()
            list2 = psutil.disk_usage('/')
            list3 = psutil.virtual_memory()
            snapshot = {
                'SNAPSHOT': count,
                'Date': time.asctime(),
                'Overall CPU load': str(list1[2]) + "%",
                'Overall memory usage': str(list2[1] // 1048576) + "mb",
                'Overall virtual memory usage': str(list3[3] // 1048576) + "mb"
            }
            json.dump(snapshot, myfile, indent=2)
            time.sleep(int(self.t))


def main():
    if args.t == "txt":
        mon1 = monitor(args.i)
        mon1.txt()

    if args.t == "json":
        mon2 = monitor(args.i)
        mon2.json()


main()
