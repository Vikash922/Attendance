import re

with open('app/src/main/java/com/example/data/repository/LaborRepository.kt', 'r') as f:
    content = f.read()

# Replace clearUndoCache completely
clear_pattern = r'    fun clearUndoCache\(\) \{.*?\n    \}\n'
content = re.sub(clear_pattern, '    fun clearUndoCache() { }\n', content, flags=re.DOTALL)

with open('app/src/main/java/com/example/data/repository/LaborRepository.kt', 'w') as f:
    f.write(content)
