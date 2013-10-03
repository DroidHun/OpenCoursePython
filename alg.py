import django;
import sys;

def getGenerator(source):
    dataSource = source;
    dataPreSource = source;
    while dataPreSource > 0:
        dataSource = dataSource + dataPreSource % 10;
        dataPreSource = dataPreSource / 10;
    return dataSource;

arr = range(5001);
for i in range(1, 5000):
	result = getGenerator(i);
	if result <= 5000 :
		arr[result] = 0; 

print(sum(arr));

