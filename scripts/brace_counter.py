with open('app/src/main/java/com/example/presentation/screens/CashBookScreen.kt', 'r') as f:
    lines = f.readlines()

depth = 0
lazy_col_started = False
lazy_col_depth = 0

for i, line in enumerate(lines):
    if "LazyColumn(" in line:
        pass
    if "{" in line and "LazyColumn" in lines[i-5:i+1][-1]: # approx
        pass # this is tricky
    
    for char in line:
        if char == '{':
            depth += 1
        elif char == '}':
            depth -= 1
            
    if "LazyColumn(" in line:
        print(f"LazyColumn at line {i+1}")
        
    if "itemsIndexed(" in line:
        print(f"itemsIndexed at line {i+1}, depth={depth}")
