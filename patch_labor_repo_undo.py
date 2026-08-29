import re

with open('app/src/main/java/com/example/data/repository/LaborRepository.kt', 'r') as f:
    content = f.read()

# Remove lastDeletedWorker variable
content = re.sub(r'    private val _lastDeletedWorker = MutableStateFlow<LaborWorker\?>(null)\n', '', content)
content = re.sub(r'    val lastDeletedWorker: StateFlow<LaborWorker\?> = _lastDeletedWorker.asStateFlow\(\)\n', '', content)

# Remove assigning to lastDeletedWorker in deleteWorker
content = re.sub(r'            _lastDeletedWorker.value = worker\n', '', content)

# Remove undoDeleteWorker function
undo_func_pattern = r'    fun undoDeleteWorker\(\): Boolean \{.*?\n    \}\n'
content = re.sub(undo_func_pattern, '', content, flags=re.DOTALL)

with open('app/src/main/java/com/example/data/repository/LaborRepository.kt', 'w') as f:
    f.write(content)
