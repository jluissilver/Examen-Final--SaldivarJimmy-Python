import re

texto = """@robot9! @robot4& I have a good feeling that the show isgoing to be amazing! @robot9$ @robot7%"""
patron="@robot+[0-9]+!"
 
coincidencias = re.findall(patron, texto)

for coincidencia in coincidencias:
    print("Las coincidencias son : ",coincidencia)