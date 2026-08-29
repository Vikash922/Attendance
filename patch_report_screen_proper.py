import re

with open('app/src/main/java/com/example/presentation/screens/LaborReportScreen.kt', 'r') as f:
    content = f.read()

# The block to remove is from "// Formatted Slip Preview Card" to "Spacer(modifier = Modifier.height(12.dp))\n            }"
pattern = re.compile(r'\s*// Formatted Slip Preview Card\s*item \{.*?Spacer\(modifier = Modifier\.height\(12\.dp\)\)\n            \}', re.DOTALL)
content = pattern.sub('', content)

with open('app/src/main/java/com/example/presentation/screens/LaborReportScreen.kt', 'w') as f:
    f.write(content)
