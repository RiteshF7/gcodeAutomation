"
G90 ;Absolute positionning ; Un-comment these out on the final copy-paste set of Gcode

G1 X0 Y{machine_depth} ;Present print
G28 ; Home all axes

;M106 S0 ;Turn-off fan ; Un-comment these out on the final copy-paste set of Gcode
;M104 S0 ;Turn-off hotend ; Un-comment these out on the final copy-paste set of Gcode
;M140 S0 ;Turn-off bed ; Un-comment these out on the final copy-paste set of Gcode

;M84 X Y E ;Disable all steppers but Z ; Un-comment these out on the final copy-paste set of Gcode
