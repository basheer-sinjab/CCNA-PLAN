import os

index_path = os.path.join(os.path.dirname(__file__), 'index.html')
inline_path = os.path.join(os.path.dirname(__file__), 'render_inline.html')

with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace body background with transparent for seamless thread blending
content = content.replace('class="bg-slate-950 text-slate-100 min-h-screen', 'class="text-slate-100 min-h-screen" style="background: transparent;')

with open(inline_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'Done! Created {inline_path}')
