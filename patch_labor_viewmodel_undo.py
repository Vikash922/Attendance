import re

with open('app/src/main/java/com/example/presentation/viewmodel/LaborViewModel.kt', 'r') as f:
    content = f.read()

# Change the sync message
content = content.replace('_syncMessage.value = "$name deleted. Tap to UNDO."', '_syncMessage.value = "$name deleted."')

# Remove lastDeletedWorker StateFlow
last_deleted_pattern = r'val lastDeletedWorker: StateFlow<LaborWorker\?> = repository.lastDeletedWorker\s*.*\s*'
content = re.sub(last_deleted_pattern, '', content)

# Remove undoDeleteWorker function
undo_func_pattern = r'    fun undoDeleteWorker\(\) \{.*?\n    \}\n'
content = re.sub(undo_func_pattern, '', content, flags=re.DOTALL)

with open('app/src/main/java/com/example/presentation/viewmodel/LaborViewModel.kt', 'w') as f:
    f.write(content)
