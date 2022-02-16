from modulos import saludo, mascotas
from camelcase import CamelCase


print (mascotas)
saludo("Antonio")

c = CamelCase()
s = "esta oración necesita CamelCase"
camelcased  = c.hump(s)
print(camelcased)
