import sys
import string

size = 3; #default
count = 0;
dictionary = {};
worklist = [];

if (len(sys.argv) == 3):
    file_name = str(sys.argv[2])
    length = sys.argv[1].split("[]-l");
    if(len(length) == 0):
        size = 3;
    else:
        size = int(length[0:]);
else:
    file_name = str(sys.argv[1]);
    
for line in open(file_name, "r"):
    rule = line.split();
    prod = rule[2:];
    prodstring = '';
    key = rule[0];

    if(key not in dictionary.keys()):
        for item in prod:
            prodstring = prodstring + item + ' ';
        dictionary[key] = [prodstring];
    else:
        for item in prod:
            prodstring = prodstring + item + ' ';
        dictionary[key].append(prodstring);

startsym = open(file_name, 'r').readline().split(' ')[0];
worklist.append(startsym);
print("");

#while the worklist is not empty
while (len(worklist)!=0):
    lnt, index = '', 0;
    #get and delete one item from the beginning of the worklist
    s = worklist.pop(0).split();
    
    #if |s|>N, go to next iteration of while
    if len(s) > size:
        continue;
    
    for item in s:
        if item in dictionary.keys():
            lnt = item;
            index = s.index(item);
            break;
    
    if (lnt == ''):
        for item in s:
            print(item, end = ' ');
        count += 1;
        print();
        continue;
    
    for value in dictionary[item]:
        store = [];
        for item in s:
            store.append(item);
        store.remove(lnt);
        #replace NT is s with rhs and store in tmp
        store.insert(index, value);
        finalstring = '';
        
        for item in store:
            finalstring = finalstring + item + ' ';
        worklist.append(finalstring);

print("");
print("Total generated strings: {} ".format(count));