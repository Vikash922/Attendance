import re

with open('app/src/main/java/com/example/presentation/screens/LaborDetailScreen.kt', 'r') as f:
    content = f.read()

# Fix Header Weights
content = content.replace('.weight(1.35f)', '.weight(1.15f)')
content = content.replace('.weight(0.95f)', '.weight(1.15f)')

# Move 3 dots in Row
old_3dots = """                    }
                }

                // 3 dots More Menu (Mark Attendance Sheet)
                Box(
                    modifier = Modifier
                        .size(36.dp)
                        .clip(CircleShape)
                        .clickable { onOpenAttendanceSheet(dayInfo.day, status) },
                    contentAlignment = Alignment.Center
                ) {
                    Icon(
                        imageVector = Icons.Default.MoreVert,
                        contentDescription = "Mark Attendance",
                        tint = Color(0xFF475569),
                        modifier = Modifier.size(20.dp)
                    )
                }
            }"""

new_3dots = """                    }
                    
                    // 3 dots More Menu (Mark Attendance Sheet) moved next to OT
                    Box(
                        modifier = Modifier
                            .size(36.dp)
                            .clip(CircleShape)
                            .clickable { onOpenAttendanceSheet(dayInfo.day, status) },
                        contentAlignment = Alignment.Center
                    ) {
                        Icon(
                            imageVector = Icons.Default.MoreVert,
                            contentDescription = "Mark Attendance",
                            tint = Color(0xFF475569),
                            modifier = Modifier.size(20.dp)
                        )
                    }
                }
            }"""

content = content.replace(old_3dots, new_3dots)

with open('app/src/main/java/com/example/presentation/screens/LaborDetailScreen.kt', 'w') as f:
    f.write(content)
