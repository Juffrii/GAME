def new_dir(direc, dop_dir):
    return((direc + "\ ").split()[0] + dop_dir) 

def write_to_log(message):   
    log = open('logs.txt', 'w')
    log.write(message)
    log.close()

write_to_log('initialization started')
    
fulsc = True
directory = ""
dr = open('directory.txt','r')

for i in dr: 
    for j in i:  
        directory += str(j)

dr.close()

items = []
it = open(new_dir(new_dir(new_dir(directory, 'resourses'), 'files'), 'items.txt'), 'r')
for i in it:
    items.append(i.split("-")[0])
it.close()

textures_dir = new_dir(new_dir(directory, 'resourses'), 'textures')

write_to_log('initialization ended sucsesfully')