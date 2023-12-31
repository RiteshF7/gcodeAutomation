import preprocessor,postprocessor,objcode, end,jsonproccesor

repeat = 3
babystep= jsonproccesor.config['babystep']
precode = preprocessor.preCode
mainobj = objcode.objcode
postcode = postprocessor.postcode
endCode = end.endCode

f= open("main.gcode","w+")
for index in range(repeat):
    f.write(str(precode))
    f.write(str("M290 Z"+babystep +"\n"+mainobj))
    f.write(str(postcode))

f.write(str(endCode))
f.close
   



