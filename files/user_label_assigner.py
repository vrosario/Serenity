from shell import Shell

sh = Shell()
sh.run('oc get groups')
for file in sh.output():
    print(file)