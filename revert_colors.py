import re

with open('index.html', 'r') as f:
    content = f.read()

# Revert colors 
content = content.replace('lime-', 'cyan-')
# Wait, I had changed 'emerald-' to 'green-'.
content = content.replace('green-', 'emerald-')
# I had changed 'blue-' to 'emerald-'. 
# This means some original blue- became emerald- and were NOT changed to green- because they were changed to emerald-.
# Wait, my previous script:
# content = content.replace('cyan-', 'lime-')
# content = content.replace('emerald-', 'green-')
# content = content.replace('blue-', 'emerald-')
# content = content.replace('pink-', 'teal-')

# To reverse:
content = content.replace('teal-', 'pink-')
# emerald- in the current file was originally blue-. So emerald- -> blue-.
content = content.replace('emerald-', 'blue-')
# green- in the current file was originally emerald-. So green- -> emerald-.
content = content.replace('green-', 'emerald-')

# zinc- -> slate-
content = content.replace('zinc-900', 'slate-900')
content = content.replace('zinc-800', 'slate-800')
content = content.replace('zinc-700', 'slate-700')
content = content.replace('zinc-400', 'slate-400')
content = content.replace('zinc-300', 'slate-300')
content = content.replace('zinc-200', 'slate-200')

with open('index.html', 'w') as f:
    f.write(content)
