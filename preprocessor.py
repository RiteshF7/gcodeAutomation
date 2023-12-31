from string import Template
import jsonproccesor

config = jsonproccesor.config


pre = Template(
"""


;preprocessor



G92 E0 ; Reset Extruder
G28 ; Home all axes
M190 S$bedTemp ; Heat bed back up to temp (change 65 to your bed temp)
M109 S$nozzelTemp ; set temperature and wait for it to be reached
G1 Z2.0 F3000 ; Move Z Axis up little to prevent scratching of Heat Bed
; this is to draw starting line and get filament flowing - use a skirt/brim if you would prefer no starting line
G1 X0.1 Y20 Z0.3 F5000.0 ; Move to start position
G1 X$fline Y200.0 Z$lineheight F1500.0 E15 ; Draw the first line
G1 X$sline Y200.0 Z$lineheight F5000.0 ; Move to side a little
G1 X$sline Y20 Z$lineheight F1500.0 E30 ; Draw the second line
G92 E0 ; Reset Extruder
G1 Z2.0 F3000 ; Move Z Axis up little to prevent scratching of Heat Bed
G1 X5 Y20 Z0.3 F5000.0 ; Move over to prevent blob squish


;pre_end



""")

preCode = pre.substitute(config)


print(preCode)
