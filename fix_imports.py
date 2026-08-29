with open('app/src/main/java/com/example/presentation/screens/CashBookScreen.kt', 'r') as f:
    lines = f.readlines()

# The first line is the import, second is package
if 'import androidx.compose.foundation.layout.fillMaxHeight' in lines[0]:
    # Swap line 0 and line 1
    lines[0], lines[1] = lines[1], lines[0]

with open('app/src/main/java/com/example/presentation/screens/CashBookScreen.kt', 'w') as f:
    f.writelines(lines)
