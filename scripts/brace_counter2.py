with open('app/src/main/java/com/example/presentation/screens/CashBookScreen.kt', 'r') as f:
    lines = f.readlines()

depth = 0
for i, line in enumerate(lines):
    for char in line:
        if char == '{':
            depth += 1
        elif char == '}':
            depth -= 1
            
    if "LazyColumn(" in line:
        print(f"LazyColumn starts at line {i+1}")
    if i+1 == 305:
        print(f"At line 305 (after LazyColumn brace), depth={depth}")
    if "itemsIndexed(" in line:
        print(f"itemsIndexed at line {i+1}, depth={depth}")
