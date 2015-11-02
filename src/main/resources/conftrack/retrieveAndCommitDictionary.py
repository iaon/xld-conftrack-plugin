import commands
import os
dir = env.WorkingDirectory + "/" + env.getName() + "/dict/"
if not os.path.exists(dir):
    os.makedirs(dir)
for dict in dicts:
    fileName = dict.name.rpartition('/')[2]
    fileName = fileName + '.conf'
    file = open( dir + fileName, 'w')
    for entry in dict.entries:
        file.write(entry + '=' + dict.entries[entry] + '\n')
    file.close()
os.chdir(dir + "..")
commands.getoutput('svn add *')
commands.getoutput('svn commit -m "Commit dictionary fom env:"' + env.getName())
