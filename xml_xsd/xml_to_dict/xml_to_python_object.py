import untangle

obj = untangle.parse('data.xml')

# también funciona con un string directamente: 
# obj = untangle.parse("""
#    <employees>
# 	    <employee>
#  		    <name>Dave</name>
#            <role>Sale Assistant</role>
#            <age>34</age>
#        </employee>
#    </employees>
# """)

#Access the name
print(obj.employees.employee.name.cdata)