with open('app/src/main/java/com/example/presentation/screens/CashBookScreen.kt', 'r') as f:
    lines = f.readlines()

new_lines = []
skip_next = 0
for i, line in enumerate(lines):
    if skip_next > 0:
        skip_next -= 1
        continue
    
    if "if (index < displayTransactions.size - 1) {" in line:
        # keep this line, the divider, and the closing brace
        new_lines.append(line)
        new_lines.append(lines[i+1])
        new_lines.append(lines[i+2])
        new_lines.append("                                }\n")
        
        # Now we skip the next 4 closing braces
        # 606: } (closed by us)
        # 607: }
        # 608: }
        # 609: }
        # 610: }
        skip_next = 6
        continue
    
    new_lines.append(line)

with open('app/src/main/java/com/example/presentation/screens/CashBookScreen.kt', 'w') as f:
    f.writelines(new_lines)
