import re

with open('app/src/main/java/com/example/presentation/components/MonthYearSelectionBottomSheet.kt', 'r') as f:
    content = f.read()

# Replace the Month Picker Dialog with a beautiful grid layout
old_month_dialog = """    // Month Picker Dialog
    if (showMonthPicker) {
        AlertDialog(
            onDismissRequest = { showMonthPicker = false },
            containerColor = Color.White,
            shape = RoundedCornerShape(20.dp),
            title = {
                Text(
                    text = "Select Month",
                    fontSize = 18.sp,
                    fontWeight = FontWeight.Bold,
                    color = Color(0xFF111827)
                )
            },
            text = {
                LazyColumn(
                    modifier = Modifier
                        .fillMaxWidth()
                        .height(300.dp)
                ) {
                    items(LaborCalendarHelper.monthsFull.indices.toList()) { index ->
                        val mNum = index + 1
                        val mName = LaborCalendarHelper.monthsFull[index]
                        val isSelected = mNum == selectedMonthNum

                        Row(
                            modifier = Modifier
                                .fillMaxWidth()
                                .clip(RoundedCornerShape(8.dp))
                                .clickable {
                                    selectedMonthNum = mNum
                                    showMonthPicker = false
                                }
                                .padding(vertical = 10.dp, horizontal = 8.dp),
                            verticalAlignment = Alignment.CenterVertically
                        ) {
                            RadioButton(
                                selected = isSelected,
                                onClick = {
                                    selectedMonthNum = mNum
                                    showMonthPicker = false
                                },
                                colors = RadioButtonDefaults.colors(
                                    selectedColor = Color(0xFF1D61D2),
                                    unselectedColor = Color(0xFF9CA3AF)
                                )
                            )
                            Spacer(modifier = Modifier.width(10.dp))
                            Text(
                                text = mName,
                                fontSize = 15.sp,
                                fontWeight = if (isSelected) FontWeight.Bold else FontWeight.Normal,
                                color = if (isSelected) Color(0xFF1D61D2) else Color(0xFF1F2937)
                            )
                        }
                    }
                }
            },
            confirmButton = {},
            dismissButton = {
                TextButton(onClick = { showMonthPicker = false }) {
                    Text("Cancel", color = Color(0xFF1D61D2), fontWeight = FontWeight.Bold)
                }
            }
        )
    }"""

new_month_dialog = """    // Month Picker Dialog
    if (showMonthPicker) {
        AlertDialog(
            onDismissRequest = { showMonthPicker = false },
            containerColor = Color.White,
            shape = RoundedCornerShape(20.dp),
            title = {
                Text(
                    text = "Select Month",
                    fontSize = 18.sp,
                    fontWeight = FontWeight.Bold,
                    color = Color(0xFF111827)
                )
            },
            text = {
                Column(
                    modifier = Modifier.fillMaxWidth(),
                    verticalArrangement = Arrangement.spacedBy(12.dp)
                ) {
                    val months = LaborCalendarHelper.monthsFull
                    for (row in 0 until 4) {
                        Row(
                            modifier = Modifier.fillMaxWidth(),
                            horizontalArrangement = Arrangement.spacedBy(8.dp)
                        ) {
                            for (col in 0 until 3) {
                                val index = row * 3 + col
                                val mNum = index + 1
                                val mName = months[index].take(3)
                                val isSelected = mNum == selectedMonthNum
                                
                                Surface(
                                    modifier = Modifier
                                        .weight(1f)
                                        .height(48.dp)
                                        .clickable { 
                                            selectedMonthNum = mNum
                                            showMonthPicker = false
                                        },
                                    shape = RoundedCornerShape(12.dp),
                                    color = if (isSelected) Color(0xFF1D61D2) else Color(0xFFF3F4F6)
                                ) {
                                    androidx.compose.foundation.layout.Box(
                                        contentAlignment = Alignment.Center
                                    ) {
                                        Text(
                                            text = mName,
                                            fontSize = 15.sp,
                                            fontWeight = if (isSelected) FontWeight.Bold else FontWeight.Medium,
                                            color = if (isSelected) Color.White else Color(0xFF374151)
                                        )
                                    }
                                }
                            }
                        }
                    }
                }
            },
            confirmButton = {},
            dismissButton = {
                TextButton(onClick = { showMonthPicker = false }) {
                    Text("Cancel", color = Color(0xFF1D61D2), fontWeight = FontWeight.Bold)
                }
            }
        )
    }"""

content = content.replace(old_month_dialog, new_month_dialog)

with open('app/src/main/java/com/example/presentation/components/MonthYearSelectionBottomSheet.kt', 'w') as f:
    f.write(content)
