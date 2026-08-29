import re

with open('app/src/main/java/com/example/presentation/viewmodel/LaborViewModel.kt', 'r') as f:
    content = f.read()

# Fix addLaborFromForm
old_validation = 'if (name.isBlank() || phone.isBlank() || wage <= 0.0) return false'
new_validation = 'if (name.isBlank() || name.length > 50 || phone.isBlank() || phone.length > 20 || wage <= 0.0 || wage > 1000000.0) return false'
content = content.replace(old_validation, new_validation)

with open('app/src/main/java/com/example/presentation/viewmodel/LaborViewModel.kt', 'w') as f:
    f.write(content)
