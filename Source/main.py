#import sys
import read_files
import clean_dataset

if __name__ == "__main__":

    dfGFA = read_files.loadGFA()
    dfElements = read_files.loadTablaPeriodica()
    clean_dataset.cleanDataset(dfGFA,dfElements)

#    if len(sys.argv) == 1:
#        simulator.restart()
#    else:
#        simulator.restart(sys.argv[1])