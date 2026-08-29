import re

with open('app/src/main/java/com/example/presentation/screens/LaborReportScreen.kt', 'r') as f:
    content = f.read()

start_idx = content.find('// Formatted Slip Preview Card')
if start_idx != -1:
    end_idx = content.find('            }\n        }\n    }\n}', start_idx)
    if end_idx != -1:
        content = content[:start_idx] + content[end_idx:]

with open('app/src/main/java/com/example/presentation/screens/LaborReportScreen.kt', 'w') as f:
    f.write(content)
