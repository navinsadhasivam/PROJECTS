import re
x = "asdf#$&^#@!"
new = re.sub('[\w]+' ,'', x)
