with open('app/src/main/java/com/example/presentation/screens/AddLaborScreen.kt', 'r') as f:
    content = f.read()

content = content.replace('if (!isLast)', 'if (index < contacts.size - 1)')

with open('app/src/main/java/com/example/presentation/screens/AddLaborScreen.kt', 'w') as f:
    f.write(content)
