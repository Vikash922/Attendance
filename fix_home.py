with open('app/src/main/java/com/example/presentation/screens/LaborHomeScreen.kt', 'r') as f:
    lines = f.readlines()

new_lines = []
skip = False
for line in lines:
    if '// Quick Undo Banner' in line:
        skip = True
    if skip and '// Labor Worker Cards List' in line:
        skip = False
    
    if not skip:
        new_lines.append(line)

with open('app/src/main/java/com/example/presentation/screens/LaborHomeScreen.kt', 'w') as f:
    f.writelines(new_lines)
