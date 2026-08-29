import re

with open('app/src/main/java/com/example/presentation/screens/LaborHomeScreen.kt', 'r') as f:
    content = f.read()

# Remove Quick Undo Banner
undo_banner_pattern = r'            // Quick Undo Banner\s*if \(lastDeletedWorker != null\) \{.*?\s*\}\s*\}\s*\}\s*// Labor Worker Cards List'
content = re.sub(undo_banner_pattern, '            // Labor Worker Cards List', content, flags=re.DOTALL)

# Remove undo stuff from EmptyLaborStateCard call
old_empty_call = """                        onAddLaborClick = { viewModel.navigateTo(Screen.AddLabor) },
                        onRestoreClick = {
                            viewModel.restoreFromSafetyBackup()
                        },
                        lastDeletedWorkerName = lastDeletedWorker?.name,
                        onUndoClick = { viewModel.undoDeleteWorker() },
                        lang = lang"""
new_empty_call = """                        onAddLaborClick = { viewModel.navigateTo(Screen.AddLabor) },
                        onRestoreClick = {
                            viewModel.restoreFromSafetyBackup()
                        },
                        lang = lang"""
content = content.replace(old_empty_call, new_empty_call)

# Remove undo stuff from EmptyLaborStateCard declaration
old_empty_decl = """fun EmptyLaborStateCard(
    onAddLaborClick: () -> Unit,
    onRestoreClick: () -> Unit,
    lastDeletedWorkerName: String?,
    onUndoClick: () -> Unit,
    lang: String
)"""
new_empty_decl = """fun EmptyLaborStateCard(
    onAddLaborClick: () -> Unit,
    onRestoreClick: () -> Unit,
    lang: String
)"""
content = content.replace(old_empty_decl, new_empty_decl)

# Remove undo button from EmptyLaborStateCard UI
old_undo_ui = """                if (lastDeletedWorkerName != null) {
                    androidx.compose.material3.OutlinedButton(
                        onClick = onUndoClick,
                        shape = RoundedCornerShape(20.dp),
                        border = androidx.compose.foundation.BorderStroke(1.dp, Color(0xFFF59E0B)),
                        colors = androidx.compose.material3.ButtonDefaults.outlinedButtonColors(contentColor = Color(0xFFD97706))
                    ) {
                        Text(
                            text = "Undo Delete ($lastDeletedWorkerName)",
                            fontWeight = FontWeight.Bold,
                            fontSize = 13.sp
                        )
                    }
                }"""
content = content.replace(old_undo_ui, '')

with open('app/src/main/java/com/example/presentation/screens/LaborHomeScreen.kt', 'w') as f:
    f.write(content)
