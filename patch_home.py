import re

with open('app/src/main/java/com/example/presentation/screens/LaborHomeScreen.kt', 'r') as f:
    content = f.read()

# Add imports
if 'import com.example.core.util.AppUpdater' not in content:
    content = content.replace('import com.example.core.util.AppStrings', 'import com.example.core.util.AppStrings\nimport com.example.core.util.AppUpdater\nimport com.example.core.util.UpdateInfo\nimport androidx.compose.runtime.LaunchedEffect\nimport androidx.compose.runtime.mutableStateOf\nimport androidx.compose.runtime.setValue\nimport androidx.compose.material3.AlertDialog\nimport androidx.compose.material3.TextButton')

# Find the start of Scaffold
old_scaffold = '    Scaffold('

new_scaffold = """    var updateInfo by androidx.compose.runtime.remember { mutableStateOf<UpdateInfo?>(null) }
    
    LaunchedEffect(Unit) {
        val info = AppUpdater.checkForUpdate()
        if (info != null && info.hasUpdate) {
            updateInfo = info
        }
    }

    if (updateInfo != null) {
        AlertDialog(
            onDismissRequest = { updateInfo = null },
            title = { Text("Update Available", fontWeight = FontWeight.Bold, color = Color(0xFF0F172A)) },
            text = {
                Column {
                    Text("Version ${updateInfo!!.latestVersionName} is available.", fontSize = 14.sp, color = Color(0xFF334155))
                    Spacer(modifier = Modifier.height(8.dp))
                    Text(updateInfo!!.releaseNotes, fontSize = 13.sp, color = Color(0xFF64748B))
                }
            },
            confirmButton = {
                androidx.compose.material3.Button(
                    onClick = {
                        AppUpdater.downloadAndInstallUpdate(context, updateInfo!!.apkUrl, updateInfo!!.latestVersionName)
                        updateInfo = null
                    },
                    colors = androidx.compose.material3.ButtonDefaults.buttonColors(containerColor = com.example.presentation.theme.LaborBlue)
                ) {
                    Text("Update Now", color = Color.White)
                }
            },
            dismissButton = {
                TextButton(onClick = { updateInfo = null }) {
                    Text("Later", color = Color(0xFF64748B))
                }
            },
            containerColor = Color.White,
            shape = RoundedCornerShape(16.dp)
        )
    }

    Scaffold("""

if old_scaffold in content:
    content = content.replace(old_scaffold, new_scaffold)

with open('app/src/main/java/com/example/presentation/screens/LaborHomeScreen.kt', 'w') as f:
    f.write(content)
