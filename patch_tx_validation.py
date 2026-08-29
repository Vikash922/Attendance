with open('app/src/main/java/com/example/presentation/viewmodel/LaborViewModel.kt', 'r') as f:
    content = f.read()

old_tx = """        if (amount <= 0.0) {
            closeTransactionSheet()
            return
        }"""
new_tx = """        if (amount <= 0.0 || amount > 10000000.0 || notes.length > 500) {
            closeTransactionSheet()
            return
        }"""
content = content.replace(old_tx, new_tx)

with open('app/src/main/java/com/example/presentation/viewmodel/LaborViewModel.kt', 'w') as f:
    f.write(content)
