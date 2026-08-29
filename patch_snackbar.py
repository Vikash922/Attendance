import re

with open('app/src/main/java/com/example/MainActivity.kt', 'r') as f:
    content = f.read()

old_snackbar = """        snackbarHost = {
            SnackbarHost(snackbarHostState) { data ->
                Row(
                    modifier = Modifier
                        .padding(bottom = 24.dp, start = 16.dp, end = 16.dp)
                        .fillMaxWidth()
                        .shadow(12.dp, RoundedCornerShape(20.dp), ambientColor = com.example.presentation.theme.LaborBlue, spotColor = com.example.presentation.theme.LaborBlue)
                        .background(Color(0xFF1E293B), RoundedCornerShape(20.dp))
                        .padding(horizontal = 18.dp, vertical = 14.dp),
                    verticalAlignment = Alignment.CenterVertically
                ) {
                    Icon(
                        imageVector = Icons.Rounded.Info,
                        contentDescription = "Notification",
                        tint = com.example.presentation.theme.LaborWarning,
                        modifier = Modifier.size(22.dp)
                    )
                    Spacer(modifier = Modifier.width(14.dp))
                    Text(
                        text = data.visuals.message,
                        color = Color.White,
                        fontSize = 14.sp,
                        fontWeight = FontWeight.Medium
                    )
                }
            }
        },"""

new_snackbar = """        snackbarHost = {
            SnackbarHost(snackbarHostState) { data ->
                Box(
                    modifier = Modifier
                        .padding(bottom = if (isRootTabScreen) 90.dp else 32.dp, start = 24.dp, end = 24.dp)
                        .fillMaxWidth(),
                    contentAlignment = Alignment.Center
                ) {
                    Row(
                        modifier = Modifier
                            .shadow(4.dp, RoundedCornerShape(30.dp))
                            .background(Color(0xFF222222), RoundedCornerShape(30.dp))
                            .padding(horizontal = 20.dp, vertical = 12.dp),
                        verticalAlignment = Alignment.CenterVertically
                    ) {
                        val msg = data.visuals.message
                        val isSuccess = msg.contains("success", ignoreCase = true) || msg.contains("saved", ignoreCase = true) || msg.contains("added", ignoreCase = true)
                        
                        Icon(
                            imageVector = if (isSuccess) Icons.Rounded.CheckCircle else Icons.Rounded.Info,
                            contentDescription = "Notification",
                            tint = if (isSuccess) Color(0xFF4ADE80) else Color(0xFF60A5FA),
                            modifier = Modifier.size(20.dp)
                        )
                        Spacer(modifier = Modifier.width(12.dp))
                        Text(
                            text = msg,
                            color = Color.White,
                            fontSize = 13.sp,
                            fontWeight = FontWeight.Medium
                        )
                    }
                }
            }
        },"""

if old_snackbar in content:
    content = content.replace(old_snackbar, new_snackbar)

with open('app/src/main/java/com/example/MainActivity.kt', 'w') as f:
    f.write(content)
