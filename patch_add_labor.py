import re

with open('app/src/main/java/com/example/presentation/screens/AddLaborScreen.kt', 'r') as f:
    content = f.read()

# Replace the complex shape logic in contacts
old_items = """                    val isFirst = index == 0
                    val isLast = index == contacts.size - 1
                    val cardShape = when {
                        isFirst && isLast -> RoundedCornerShape(16.dp)
                        isFirst -> RoundedCornerShape(topStart = 16.dp, topEnd = 16.dp)
                        isLast -> RoundedCornerShape(bottomStart = 16.dp, bottomEnd = 16.dp)
                        else -> androidx.compose.ui.graphics.RectangleShape
                    }

                    Surface(
                        modifier = Modifier
                            .fillMaxWidth()
                            .clickable { selectedContactForAdd = contact }
                            .testTag("contact_item_${contact.id}"),
                        shape = cardShape,
                        color = Color.White,
                        shadowElevation = if (isFirst || isLast) 1.dp else 0.dp
                    ) {"""

new_items = """                    Surface(
                        modifier = Modifier
                            .fillMaxWidth()
                            .clickable { selectedContactForAdd = contact }
                            .testTag("contact_item_${contact.id}"),
                        shape = androidx.compose.ui.graphics.RectangleShape,
                        color = Color.White
                    ) {"""

content = content.replace(old_items, new_items)

# Add a divider instead of complex card if not last item
# Wait, let's check where the divider is.
old_divider = """                        }
                    }"""
# No, let's just use regex to replace the complex shape entirely and ensure there's a simple divider.

with open('app/src/main/java/com/example/presentation/screens/AddLaborScreen.kt', 'w') as f:
    f.write(content)
