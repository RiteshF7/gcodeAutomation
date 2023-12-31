
import jsonproccesor,codeprocessor

repeat = jsonproccesor.config['copies']
babystep= jsonproccesor.config['babystep']
precode = codeprocessor.preCode
mainobj = codeprocessor.objcode
postcode = codeprocessor.postcode
endCode = codeprocessor.endCode

f= open("gcodes/main.gcode","w+")
for index in range(repeat):
    f.write(str(precode))
    f.write(str("M290 Z"+babystep +"\n"+mainobj))
    f.write(str(postcode))

f.write(str(endCode))
f.close
   



