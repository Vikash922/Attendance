import re

with open('app/src/main/java/com/example/presentation/screens/CashBookScreen.kt', 'r') as f:
    content = f.read()

# Replace the entire Table Header and Table Content logic
old_table_start = '// Entire Structured Compact Table matching reference screenshot'
old_table_end = 'item { Spacer(modifier = Modifier.height(16.dp)) }'

# We'll use regex to replace the entire section.
import re
pattern = re.compile(r'// Entire Structured Compact Table matching reference screenshot.*?item { Spacer\(modifier = Modifier\.height\(16\.dp\)\) }', re.DOTALL)

new_table = """// Entire Structured Compact Table matching reference screenshot
                    item {
                        Column(
                            modifier = Modifier
                                .fillMaxWidth()
                                // No horizontal padding here so dividers go full width!
                        ) {
                            // Table Header Row
                            Row(
                                modifier = Modifier
                                    .fillMaxWidth()
                                    .background(Color(0xFFF9FAFB))
                                    .height(IntrinsicSize.Min),
                                verticalAlignment = Alignment.CenterVertically
                            ) {
                                Text(
                                    text = AppStrings.get("date", lang),
                                    fontSize = 13.5.sp,
                                    fontWeight = FontWeight.Bold,
                                    color = Color.Black,
                                    modifier = Modifier
                                        .weight(0.20f)
                                        .padding(start = 12.dp, top = 8.dp, bottom = 8.dp),
                                    textAlign = TextAlign.Start
                                )
                                // Divider 1
                                androidx.compose.foundation.layout.Box(modifier = Modifier.width(1.dp).fillMaxHeight().background(Color.Black))
                                
                                Text(
                                    text = AppStrings.get("notes", lang),
                                    fontSize = 13.5.sp,
                                    fontWeight = FontWeight.Bold,
                                    color = Color.Black,
                                    modifier = Modifier
                                        .weight(0.44f)
                                        .padding(horizontal = 8.dp, vertical = 8.dp),
                                    textAlign = TextAlign.Start
                                )
                                // Divider 2
                                androidx.compose.foundation.layout.Box(modifier = Modifier.width(1.dp).fillMaxHeight().background(Color.Black))

                                Text(
                                    text = "₹ " + AppStrings.get("amount", lang),
                                    fontSize = 13.5.sp,
                                    fontWeight = FontWeight.Bold,
                                    color = Color.Black,
                                    modifier = Modifier
                                        .weight(0.36f)
                                        .padding(end = 12.dp, start = 8.dp, top = 8.dp, bottom = 8.dp),
                                    textAlign = TextAlign.Start
                                )
                            }
                            HorizontalDivider(color = Color.Black, thickness = 1.dp)
                        }
                    }
                    
                    itemsIndexed(
                        items = displayTransactions,
                        key = { _, tx -> tx.id }
                    ) { index, tx ->
                        Column(modifier = Modifier.fillMaxWidth()) {
                            Row(
                                modifier = Modifier
                                    .fillMaxWidth()
                                    .clickable { viewModel.openTransactionDetail(tx) }
                                    .testTag("tx_row_${tx.id}")
                                    .height(IntrinsicSize.Min),
                                verticalAlignment = Alignment.CenterVertically
                            ) {
                                val (dayNum, dayName) = parseDayAndWeek(tx.fullDate, tx.dateDisplay, tx.timestamp)

                                // Date Column
                                Column(
                                    modifier = Modifier
                                        .weight(0.20f)
                                        .padding(start = 12.dp, top = 6.dp, bottom = 6.dp),
                                    horizontalAlignment = Alignment.Start,
                                    verticalArrangement = Arrangement.spacedBy(2.dp)
                                ) {
                                    Text(
                                        text = dayNum,
                                        fontSize = 14.5.sp,
                                        fontWeight = FontWeight.Bold,
                                        color = Color.Black
                                    )
                                    Text(
                                        text = dayName,
                                        fontSize = 11.sp,
                                        fontWeight = FontWeight.Normal,
                                        color = Color(0xFF6B7280)
                                    )
                                }

                                // Divider 1
                                androidx.compose.foundation.layout.Box(modifier = Modifier.width(1.dp).fillMaxHeight().background(Color.Black))

                                // Notes Column
                                Column(
                                    modifier = Modifier
                                        .weight(0.44f)
                                        .padding(horizontal = 8.dp, vertical = 6.dp),
                                    verticalArrangement = Arrangement.spacedBy(2.dp)
                                ) {
                                    Text(
                                        text = tx.notes.ifBlank { "-" },
                                        fontSize = 14.sp,
                                        fontWeight = FontWeight.SemiBold,
                                        color = Color.Black,
                                        maxLines = 1,
                                        overflow = TextOverflow.Ellipsis
                                    )
                                    Text(
                                        text = tx.paymentMethod.name.uppercase(),
                                        fontSize = 10.5.sp,
                                        fontWeight = FontWeight.Normal,
                                        color = Color(0xFF6B7280)
                                    )
                                }

                                // Divider 2
                                androidx.compose.foundation.layout.Box(modifier = Modifier.width(1.dp).fillMaxHeight().background(Color.Black))

                                // Amount Column
                                Row(
                                    modifier = Modifier
                                        .weight(0.36f)
                                        .padding(end = 12.dp, start = 8.dp, top = 6.dp, bottom = 6.dp),
                                    horizontalArrangement = Arrangement.SpaceBetween,
                                    verticalAlignment = Alignment.CenterVertically
                                ) {
                                    val formattedAmount = if (tx.amount % 1.0 == 0.0) {
                                        "${tx.amount.toInt()}"
                                    } else {
                                        "${tx.amount}"
                                    }
                                    Text(
                                        text = "₹$formattedAmount",
                                        fontSize = 14.sp,
                                        fontWeight = FontWeight.Bold,
                                        color = if (tx.type == TransactionType.CASH_IN) Color(0xFF16A34A) else Color(0xFFDC2626)
                                    )
                                    Icon(
                                        imageVector = Icons.Default.KeyboardArrowRight,
                                        contentDescription = null,
                                        tint = Color(0xFFD1D5DB),
                                        modifier = Modifier.size(16.dp)
                                    )
                                }
                            }
                            HorizontalDivider(color = Color.Black, thickness = 1.dp)
                        }
                    }
                    item { Spacer(modifier = Modifier.height(16.dp)) }"""

if pattern.search(content):
    content = pattern.sub(new_table, content)
else:
    print("Pattern not found!")

with open('app/src/main/java/com/example/presentation/screens/CashBookScreen.kt', 'w') as f:
    f.write(content)
