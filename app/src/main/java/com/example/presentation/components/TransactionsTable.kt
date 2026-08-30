package com.example.presentation.components

import androidx.compose.material.icons.filled.ChevronRight
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.itemsIndexed
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Text
import androidx.compose.material3.Icon
import androidx.compose.material.icons.Icons
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.example.domain.model.CashTransaction
import com.example.domain.model.PaymentMethod
import com.example.domain.model.TransactionType
import java.text.SimpleDateFormat
import java.util.Locale

data class ParsedTransactionDate(
    val day: String,
    val dayOfWeek: String
)

fun parseTxDate(dateStr: String?): ParsedTransactionDate {
    if (dateStr.isNullOrBlank()) return ParsedTransactionDate("-", "-")
    
    // Check if it's already in "15 Sat" format (dateDisplay)
    val parts = dateStr.trim().split(" ")
    if (parts.size >= 2 && parts[0].all { it.isDigit() }) {
        return ParsedTransactionDate(parts[0], parts[1].take(3))
    }
    
    // Check if it's "yyyy-MM-dd" format (fullDate)
    try {
        val sdf = SimpleDateFormat("yyyy-MM-dd", Locale.getDefault())
        val date = sdf.parse(dateStr)
        if (date != null) {
            val dayFormat = SimpleDateFormat("d", Locale.getDefault())
            val dowFormat = SimpleDateFormat("EEE", Locale.getDefault())
            return ParsedTransactionDate(dayFormat.format(date), dowFormat.format(date))
        }
    } catch (e: Exception) {
        // ignore
    }
    
    return ParsedTransactionDate(dateStr, "")
}

@Composable
fun TransactionsTable(
    transactions: List<CashTransaction>,
    modifier: Modifier = Modifier
) {
    val borderColor = Color(0xFFE5E7EB)

    Column(
        modifier = modifier
            .fillMaxWidth()
            .padding(top = 4.dp)
    ) {
        // Table Header
        Row(
            modifier = Modifier
                .fillMaxWidth()
                .background(Color.White)
                .border(width = 1.dp, color = borderColor)
                .height(IntrinsicSize.Min),
            verticalAlignment = Alignment.CenterVertically
        ) {
            // Date Column Header (19%)
            Box(
                modifier = Modifier
                    .weight(0.19f)
                    .fillMaxHeight(),
                contentAlignment = Alignment.Center
            ) {
                Text(
                    text = "Date",
                    fontSize = 15.sp,
                    fontWeight = FontWeight.Bold,
                    color = Color.Black,
                    modifier = Modifier.padding(vertical = 8.dp)
                )
            }
            
            // Vertical Separator
            Box(modifier = Modifier.width(1.dp).fillMaxHeight().background(borderColor))

            // Notes Column Header (45%)
            Box(
                modifier = Modifier
                    .weight(0.45f)
                    .fillMaxHeight()
                    .padding(horizontal = 12.dp),
                contentAlignment = Alignment.CenterStart
            ) {
                Text(
                    text = "Notes",
                    fontSize = 15.sp,
                    fontWeight = FontWeight.Bold,
                    color = Color.Black
                )
            }

            // Vertical Separator
            Box(modifier = Modifier.width(1.dp).fillMaxHeight().background(borderColor))

            // Amount Column Header (36%)
            Box(
                modifier = Modifier
                    .weight(0.36f)
                    .fillMaxHeight()
                    .padding(start = 12.dp),
                contentAlignment = Alignment.CenterStart
            ) {
                Text(
                    text = "₹ Amount",
                    fontSize = 15.sp,
                    fontWeight = FontWeight.Bold,
                    color = Color.Black
                )
            }
        }

        // Table Rows
        if (transactions.isEmpty()) {
            Box(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(horizontal = 16.dp, vertical = 8.dp)
                    .background(Color.White, shape = RoundedCornerShape(12.dp))
                    .border(1.dp, Color(0xFFF1F5F9), RoundedCornerShape(12.dp))
                    .padding(32.dp),
                contentAlignment = Alignment.Center
            ) {
                Text(
                    text = "No transactions found for this date range.",
                    fontSize = 12.sp,
                    fontWeight = FontWeight.Medium,
                    color = Color(0xFF94A3B8),
                    textAlign = TextAlign.Center
                )
            }
        } else {
            LazyColumn(
                contentPadding = PaddingValues(bottom = 20.dp),
                modifier = Modifier
                    .fillMaxWidth()
                    .background(Color.White)
                    .border(width = 1.dp, color = borderColor)
            ) {
                itemsIndexed(transactions, key = { _, tx -> tx.id }) { index, tx ->
                    val isCashIn = tx.type == TransactionType.CASH_IN
                    val parsedDate = parseTxDate(tx.fullDate.takeIf { it.isNotBlank() } ?: tx.dateDisplay)
                    val isLast = index == transactions.size - 1

                    Row(
                        modifier = Modifier
                            .fillMaxWidth()
                            .height(IntrinsicSize.Min),
                        verticalAlignment = Alignment.CenterVertically
                    ) {
                        // Date Column (19%)
                        Column(
                            modifier = Modifier
                                .weight(0.19f)
                                .fillMaxHeight()
                                .padding(vertical = 6.dp),
                            horizontalAlignment = Alignment.CenterHorizontally,
                            verticalArrangement = Arrangement.Center
                        ) {
                            Text(
                                text = parsedDate.day,
                                fontSize = 16.sp,
                                fontWeight = FontWeight.Bold,
                                color = Color.Black,
                                lineHeight = 16.sp
                            )
                            Spacer(modifier = Modifier.height(2.dp))
                            Text(
                                text = parsedDate.dayOfWeek,
                                fontSize = 13.sp,
                                color = Color.Gray,
                                lineHeight = 13.sp
                            )
                        }

                        // Vertical Separator
                        Box(modifier = Modifier.width(1.dp).fillMaxHeight().background(borderColor))

                        // Notes Column (45%)
                        Column(
                            modifier = Modifier
                                .weight(0.45f)
                                .fillMaxHeight()
                                .padding(horizontal = 12.dp, vertical = 6.dp),
                            verticalArrangement = Arrangement.Center
                        ) {
                            Text(
                                text = tx.notes.takeIf { it.isNotBlank() } ?: if (isCashIn) "Cash In" else "Expense",
                                fontSize = 15.sp,
                                fontWeight = FontWeight.Normal,
                                color = Color.Black,
                                maxLines = 1,
                                overflow = TextOverflow.Ellipsis,
                                lineHeight = 15.sp
                            )
                            Spacer(modifier = Modifier.height(4.dp))
                            Text(
                                text = if (tx.paymentMethod == PaymentMethod.ONLINE) "UPI" else "CASH",
                                fontSize = 11.sp,
                                color = Color.Gray,
                                letterSpacing = 0.5.sp,
                                lineHeight = 11.sp
                            )
                        }

                        // Vertical Separator
                        Box(modifier = Modifier.width(1.dp).fillMaxHeight().background(borderColor))

                        // Amount Column (36%)
                        Row(
                            modifier = Modifier
                                .weight(0.36f)
                                .fillMaxHeight()
                                .padding(horizontal = 12.dp),
                            verticalAlignment = Alignment.CenterVertically,
                            horizontalArrangement = Arrangement.SpaceBetween
                        ) {
                            Text(
                                text = "₹${tx.amount.toInt()}",
                                fontSize = 15.sp,
                                fontWeight = FontWeight.Bold,
                                color = if (isCashIn) Color(0xFF28A745) else Color(0xFFDC3545)
                            )
                            Icon(
                                imageVector = androidx.compose.material.icons.Icons.Default.ChevronRight,
                                contentDescription = "View Details",
                                tint = Color(0xFFCBD5E1),
                                modifier = Modifier.size(18.dp)
                            )
                        }
                    }

                    // Bottom Border between rows
                    if (!isLast) {
                        Box(
                            modifier = Modifier
                                .fillMaxWidth()
                                .height(1.dp)
                                .background(borderColor)
                        )
                    }
                }
            }
        }
    }
}
