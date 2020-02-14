from newstyle/grid import standardize
fn = 'sudoku17'

with open(fn,'r') as f:
    sdks = f.readlines()
for s in range(len(sdks)):
    sdks[s] = sdks[s].replace('\n','')

fullsdks = [[] for i in sdks]
for i in range(len(fullsdks)):
#    while len(fullsdks[i]) < 10:
#        fullsdks[i].append([])
     start = 0
     end = 9
     while end <= len(sdks[i]):

         fullsdks[i].append([])
         fullsdks[i][-1] = sdks[i][start:end]
         start=end
         end+=9

for s in range(len(fullsdks)):
    print(fullsdks[s])
    print(sdks[s])
    print(standardize(fullsdks[s]))
#for s in fullsdks:
#    print(s)
#print(fullsdks)
#print(sdks)
