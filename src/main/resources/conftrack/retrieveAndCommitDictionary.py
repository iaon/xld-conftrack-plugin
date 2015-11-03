import commands
import os
dir = env.WorkingDirectory + "/" + env.getName() + "/dict/"
if not os.path.exists(dir):
    os.makedirs(dir)
for dic in dicts:
    fileName = str(dic).rpartition('/')[2]
    fileName = fileName + '.conf'
    file = open( dir + fileName, 'w')
    for entry in dic.getEntries():
         file.write(str(entry) + '=' + str(dic.getValue(entry)) + '\n')
    file.close()
os.chdir(dir + "..")
( status , out) = commands.getstatusoutput('svn up')
print out
if status != 0:
   exit(status)
( status , out) = commands.getstatusoutput('svn add dict')
print out
if status != 0:
   exit(status)
(status, out) =  commands.getstatusoutput('svn commit -m "Commit dictionary for env:' + env.getName() +'" dict' )
print out
if status != 0:
   exit(status)
