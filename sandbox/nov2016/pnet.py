##

pnet = ProceduralNetwork()

##

proc1 = Proc("Proc 1", 'a b c'.split())
proc2 = Proc("Proc 2", '1 2 3'.split())
proc3 = Proc("Proc 3", '& ( *'.split())
proc4 = Proc("Proc 4", 'A N P'.split())

##

pnet.link_procedures(proc1, proc2)
pnet.link_procedures(proc2, proc4)
pnet.link_procedures(proc4, proc3)

##

pnet.executeAll()

##

executeProcedures = pnet.prepareManualExecution()

##

proc = executeProcedures.next()
proc.execute()

##
