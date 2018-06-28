import re
import color_util

text = 'at com.simba.framework.util.jdbc.Jdbc.query(Jdbc.java:133) ~[simba-database-2.1.0-SNAPSHOT.jar!/:2.1.0-SNAPSHOT]'
text = re.sub(r'\(([\w_]+\.java:\d+)\)', color_util.underline('\\1'), text)
print(text)