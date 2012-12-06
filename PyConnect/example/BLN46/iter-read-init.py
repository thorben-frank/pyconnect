levels = 12
minima_index = {} 
i = 1
minima_index['Index'] = {}
for line in open('min.data', 'r'):
    minima_data = line.split()
            
    minima_index['Index'][i] =  dict(Energy = float(minima_data[0]))
            
    i += 1
        
temp_dict = {}
        
for i in range(1,levels + 1):
    temp_dict[i] = None

    for indice in minima_index['Index']:
        minima_index['Index'][indice]['Degree'] = 0
        minima_index['Index'][indice]['Colour'] = \
                {'RGB':(0.0,0.0,0.0)}
#{'r': 0.0,
# 'g': 0.0,
                # 'b': 0.0}
            
        minima_index['Index'][indice]['Metric'] = {'x': None,'y': None,'trval': None}
        minima_index['Index'][indice]['Identify'] = False
        minima_index['Index'][indice]['TS'] = []
        minima_index['Index'][indice]['Basin'] = {}
        minima_index['Index'][indice]['Basin']['Level']={}
        for i in range(1,levels + 1):
                
            minima_index['Index'][indice]['Basin']['Level'][i] = None
                
        #FindGM()
        
#        if idmin['Min']:
#            IdentifyMin()
        
        #if not connectmin:
         #   connectmin = minima_index['GM']