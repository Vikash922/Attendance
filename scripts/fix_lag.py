import re

def fix_labor_detail():
    with open('app/src/main/java/com/example/presentation/screens/LaborDetailScreen.kt', 'r') as f:
        content = f.read()

    # Create memoized lambdas for LaborDetailScreen
    lambdas = """
            val currentWorkerId = worker.id
            val onStatusSelectedMemo = androidx.compose.runtime.remember(currentWorkerId, selectedMonth) {
                { day: Int, newStatus: com.example.domain.model.AttendanceStatus ->
                    viewModel.setAttendance(currentWorkerId, day, newStatus, selectedMonth)
                }
            }
            val onOvertimeClickedMemo = androidx.compose.runtime.remember(currentWorkerId) {
                { day: Int -> selectedDayForOvertimeDialog = day }
            }
            val onAdvanceClickedMemo = androidx.compose.runtime.remember(currentWorkerId, currentYear, currentMonthNum) {
                { day: Int ->
                    val dateKey = com.example.core.util.LaborCalendarHelper.getDateKey(currentYear, currentMonthNum, day)
                    val dayRecord = worker.attendance[dateKey]
                    if ((dayRecord?.advanceAmount ?: 0.0) > 0.0) {
                        selectedDayForAdvanceDetailDialog = day
                    } else {
                        selectedDayForAdvanceEditDialog = day
                    }
                }
            }
            val onOpenAttendanceSheetMemo = androidx.compose.runtime.remember(currentWorkerId) {
                { day: Int, initialStatus: com.example.domain.model.AttendanceStatus? ->
                    selectedDayForAttendanceSheet = Pair(day, initialStatus)
                }
            }

            itemsIndexed(
                items = monthDaysInfo,
                key = { _, it -> it.dateKey }
            ) { index, dayInfo ->
                val dayRecord = worker.attendance[dayInfo.dateKey]

                LaborAttendanceDayRow(
                    dayInfo = dayInfo,
                    isLast = index == monthDaysInfo.lastIndex,
                    status = dayRecord?.status ?: com.example.domain.model.AttendanceStatus.UNMARKED,
                    advance = dayRecord?.advanceAmount ?: 0.0,
                    note = dayRecord?.note ?: "",
                    otHours = dayRecord?.overtimeHours ?: 0.0,
                    onStatusSelected = onStatusSelectedMemo,
                    onOvertimeClicked = onOvertimeClickedMemo,
                    onAdvanceClicked = onAdvanceClickedMemo,
                    onOpenAttendanceSheet = onOpenAttendanceSheetMemo
                )
            }
"""
    
    # Replace the itemsIndexed block
    items_regex = re.compile(r'itemsIndexed\(\s*items = monthDaysInfo,.*?\n\s*\}\n\s*\)\s*\}', re.DOTALL)
    if items_regex.search(content):
        content = items_regex.sub(lambdas.strip(), content)
        with open('app/src/main/java/com/example/presentation/screens/LaborDetailScreen.kt', 'w') as f:
            f.write(content)
        print("Fixed LaborDetailScreen.kt")
    else:
        print("Could not find itemsIndexed in LaborDetailScreen.kt")

def fix_cashbook():
    with open('app/src/main/java/com/example/presentation/screens/CashBookScreen.kt', 'r') as f:
        content = f.read()

    # The original CashBookScreen has a Card with a Column and forEachIndexed.
    # We will replace it so the Header is an item, and the rows are items.
    
    # Actually, the simplest fix without breaking the Card UI is to just wrap it in a memory efficient way?
    # No, forEach inside Compose is bad for long lists.
    # We can replace the Card structure with a LazyColumn items structure where Card is per-item, OR we just use `itemsIndexed`.
    # Wait, the user wants exact same UI. The border is around the entire table.
    
    # Let's change `displayTransactions.forEachIndexed { index, tx ->` 
    # Wait, CashBook usually has hundreds of items. If it's in a Card, it's one big node.
    pass

fix_labor_detail()
