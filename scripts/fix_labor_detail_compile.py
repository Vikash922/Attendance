import re

with open('app/src/main/java/com/example/presentation/screens/LaborDetailScreen.kt', 'r') as f:
    content = f.read()

# Extract the block
block_start = "            val currentWorkerId = worker.id"
block_end = """            val onOpenAttendanceSheetMemo = androidx.compose.runtime.remember(currentWorkerId) {
                { day: Int, initialStatus: com.example.domain.model.AttendanceStatus? ->
                    selectedDayForAttendanceSheet = Pair(day, initialStatus)
                }
            }"""

start_idx = content.find(block_start)
end_idx = content.find(block_end) + len(block_end)

if start_idx != -1 and end_idx != -1:
    extracted_block = content[start_idx:end_idx]
    
    # Remove it from the original place
    content = content[:start_idx] + content[end_idx:]
    
    # Insert it before LazyColumn
    lazy_col_idx = content.find("        LazyColumn(")
    if lazy_col_idx != -1:
        content = content[:lazy_col_idx] + extracted_block + "\n" + content[lazy_col_idx:]
        
        with open('app/src/main/java/com/example/presentation/screens/LaborDetailScreen.kt', 'w') as f:
            f.write(content)
        print("Moved successfully")
    else:
        print("LazyColumn not found")
else:
    print("Block not found")
