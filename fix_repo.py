import re

with open('app/src/main/java/com/example/data/repository/LaborRepository.kt', 'r') as f:
    content = f.read()

content = re.sub(r'    private val _lastDeletedWorker = MutableStateFlow<LaborWorker\?>\(null\)\n', '', content)
content = re.sub(r'    val lastDeletedWorker: StateFlow<LaborWorker\?> = _lastDeletedWorker\.asStateFlow\(\)\n', '', content)
content = re.sub(r'\s*_lastDeletedWorker\.value = workerToDelete\n', '\n', content)
content = re.sub(r'\s*_lastDeletedWorker\.value = null\n', '\n', content)

# Replace clearUndoCache
old_clear = """    fun clearUndoCache() {
        if (_lastDeletedWorker.value != null) {
            _lastDeletedWorker.value = null
            // Once the undo window expires, push the deletion to the cloud
            persistLocalData(syncToCloud = true)
        }
    }"""
new_clear = """    fun clearUndoCache() {
        // Obsolete
    }"""
content = content.replace(old_clear, new_clear)

with open('app/src/main/java/com/example/data/repository/LaborRepository.kt', 'w') as f:
    f.write(content)
