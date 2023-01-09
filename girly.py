import sys
import string

size = 3;
dictionary = {};
worklist = [];
count = 0;

#checks size. if not inserted, default length of 3 is given!
if(len(sys.argv) == 3):
    file_name = str(sys.argv[2]);
    string = sys.argv[1];
    string = string.strip('[]-l');
    if(len(string) == 0):
        size = 3;
    else:
        size = int(string[0:]);
else:
    file_name = str(sys.argv[1]);
    
#grammar rule instructions
for line in open(file_name, 'r'):
    rule = line.split();
    key = rule[0];
    output = rule[2:];
    outputstring = '';
    
    if(key not in dictionary.keys()): #if key not already a rule, add it.
        for i in output:
            outputstring = outputstring + i + ' ';        
        dictionary[key] = [outputstring];
        
    else:
        for i in output:
            outputstring = outputstring + i + ' ';
        dictionary[key].append(outputstring);
    
#get the start symbol and add it to the worklist
startsymbol = open(file_name, 'r').readline().split(' ')[0];
worklist.append(startsymbol);
print("");

#string generation algorithm
while (len(worklist) != 0):
    lnt = ''; #leftmost non terminal
    lntindex = 0; #index of leftmost non terminal
    s = worklist.pop().split(); #get and delete item containing the potential sentence s from the beginning of the worklist
    
    if len(s) > size: #go to next iteration of while if the length of the sentence is larger than the length of the command line argument
        continue;
    
    for i in s: 
        if i in dictionary.keys():
            lnt = i;
            lntindex = s.index(i);
            break;
    
    #if sentence has no nonterminals
    if(lnt == ''):
        #if the sentence is as big as the size
        if len(s) == int(size):
            for i in s:
                print(i, end = " ");
            #keep count of the addition to the set
            count+=1;
            print();
        continue;
    
    #all productions NT->rhs
    for p in dictionary[i]:
        tmp = [];
        # replace NT with rhs
        for i in s:
            #store in tmp
            tmp.append(i);
        tmp.remove(lnt);
        tmp.insert(lntindex, p);
        storage = '';
        #turn to string
        for i in tmp:
            storage = storage + i + ' ';
        worklist.append(storage);

print("");
print("Total generated strings: {} ".format(count));
