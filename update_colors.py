import re

with open('index.html', 'r') as f:
    content = f.read()

# Replace colors for light green elegant branding
content = content.replace('cyan-', 'lime-')
content = content.replace('emerald-', 'green-')
content = content.replace('blue-', 'emerald-')
content = content.replace('pink-', 'teal-')

# Make the background a bit more "nature" focused dark mode
content = content.replace('slate-900', 'zinc-900')
content = content.replace('slate-800', 'zinc-800')
content = content.replace('slate-700', 'zinc-700')
content = content.replace('slate-400', 'zinc-400')
content = content.replace('slate-300', 'zinc-300')
content = content.replace('slate-200', 'zinc-200')

with open('index.html', 'w') as f:
    f.write(content)
