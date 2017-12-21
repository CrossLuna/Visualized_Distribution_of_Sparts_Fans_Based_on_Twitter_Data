#load file
import os
import json
#output_path = './out2'
output_path = './out3'
#dirs = os.listdir('./out')
dirs = os.listdir(output_path)
outlist = []
for d in dirs:
    if d.startswith('test_out'):
        files = os.listdir( output_path + '/' + d)
        #print (files)
        for file in files:
            if file.startswith('part'):
                with open('./' + output_path + '/' + d + '/' + file) as f:
                    #content = f.readlines()
                    lines = f.readlines()
                    for l in lines:
                        left, right = l.split(',')
                        left = left[1:]
                        right = right[1:-2]
                        outlist.append((int(float(left)), int(right)))
                        #outlist.append(l[:-1])
                        
                    #if content:
                    #    outlist.append(content)
#print(arr)
#print(outlist)

#ftwit_name = 'all_tweets_list.json'
#ftwit_name = 'all_tweets_list11.json'
ftwit_name = 'all_json_big.json'
#ftwit_name = 'all_tweets_list_.json'
#ftwit = open(ftwit_name, 'r')
#lines = ftwit.readlines()

#f_visual_out = open('visual_out.txt', 'w')
#f_visual_out = open('visual_out_test.txt', 'w')
f_visual_out = open('visual_out_big.txt', 'w')
data = json.load(open(ftwit_name))
for o in outlist:
    coordinates = data[o[0]]['coordinates']

    #print(coordinates)
    #print(coordinates = data[o[0]]['coordinates'])
    #if coordinate is not Null:
    #if coordinate :
    if coordinates is not None:
        idx = o[0]
        label = o[1]
        print("index: " + str(o[0]))
        print("class: " + str(o[1]))
        #print("coordinates" + str(coordinates))
        lon = float(coordinates['coordinates'][0])
        lat = float(coordinates['coordinates'][1])
        print("long: " + str(lon))
        print("lat: " + str(lat))
        f_visual_out.write(str(idx) + ' ')
        f_visual_out.write(str(lon) + ' ')
        f_visual_out.write(str(lat) + ' ')
        #f_visual_out.write(str(label) + '\n')
        f_visual_out.write(str(label) + ' *-+!2312$ ')
        f_visual_out.write(data[o[0]]['text'])
        f_visual_out.write('*&*&*&\n');
        #f_visual_out.write('\n')
    #print("index: " + str(o[0]))
    #print("class: " + str(o[1]))
    #print(data[o[0]]['text'])
    #print(data[o[0]]['entities']['hashtags'])
    hashtags = data[o[0]]['entities']['hashtags']
    
    hashtexts = []
    for h in hashtags:
        if h:
            #print(h['text'])
            hashtexts.append(h['text'])
    
    # if len(data[o[0]]['entities']['hashtags']) != 0:
        #print(data[o[0]]['entities']['hashtags']['text'])
        #hashtags = data[o[0]]['entities']['hashtags']['text']
        #for htag in hashtags:
        #    print(htag)
    #print(data[o[0]]['entities']['hashtags']['text'])
#for i in range(len(data)):
#    print(d[i]['hashtag'])
#for d in data:
#    print(d['text'])

#for line in lines:
    

#for line in outlist:
#    print(line)
