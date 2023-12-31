from string import Template
import jsonproccesor

config = jsonproccesor.config


pre = Template(
""""



;post processor



M190 R$coolbedtemp
M109 S$coolnozzzeltemp

G0 X117 Y210 F3000 ; Edit this command based on your print
G0 X117 Y210 Z50 F3000 ; Edit this command based on your print
G0 X117 Y210 Z0.3 F3000 ; Edit this command based on your print
G0 X117 Y0 Z0.3 F3000 ; Edit this command based on your print
G0 X117 Y210 Z0.3 F3000 ; Edit this command based on your print
G0 X117 Y0 Z0.3 F3000 ; Edit this command based on your print



;post_end

""")

postcode = pre.substitute(config)


print(postcode)



