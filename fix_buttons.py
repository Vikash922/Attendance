with open('app/src/main/java/com/example/presentation/screens/CashBookScreen.kt', 'r') as f:
    content = f.read()

content = content.replace('"+ ${AppStrings.get("cash_in", lang).uppercase()}"', 'AppStrings.get("cash_in", lang).uppercase()')
content = content.replace('"- ${AppStrings.get("cash_out", lang).uppercase()}"', 'AppStrings.get("cash_out", lang).uppercase()')

with open('app/src/main/java/com/example/presentation/screens/CashBookScreen.kt', 'w') as f:
    f.write(content)
