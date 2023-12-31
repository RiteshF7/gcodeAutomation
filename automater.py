
import jsonproccesor,codeprocessor

repeat = jsonproccesor.config['copies']
babystep= jsonproccesor.config['babystep']
zlineHeight = float(jsonproccesor.config['lineheight'])+0.5
precode = codeprocessor.preCode
mainobj = codeprocessor.objcode
postcode = codeprocessor.postcode
endCode = codeprocessor.endCode



def repeat_gcode(mainobj):
    f= open("gcodes/main.gcode","w+")
    for index in range(repeat):
        f.write(str(precode.replace(";lineheight;",str(zlineHeight+index))))
        f.write(str("\nM290 Z"+babystep +"\n"+mainobj))
        f.write(str(postcode))
    
    f.write(str(endCode))
    f.close

repeat_gcode( mainobj)


    


   



