with open('app/src/main/java/com/example/LaborApplication.kt', 'r') as f:
    content = f.read()

import_str = """import com.google.firebase.appcheck.FirebaseAppCheck
import com.google.firebase.appcheck.playintegrity.PlayIntegrityAppCheckProviderFactory
"""

content = content.replace('import com.google.firebase.FirebaseOptions', 'import com.google.firebase.FirebaseOptions\n' + import_str)

init_str = """
            if (FirebaseApp.getApps(this).isNotEmpty()) {
                try {
                    val firebaseAppCheck = FirebaseAppCheck.getInstance()
                    firebaseAppCheck.installAppCheckProviderFactory(
                        PlayIntegrityAppCheckProviderFactory.getInstance()
                    )
                    Log.i("LaborApplication", "Firebase AppCheck successfully initialized with PlayIntegrity.")
                } catch (e: Exception) {
                    Log.e("LaborApplication", "Failed to initialize Firebase AppCheck: ${e.message}")
                }
            }
"""

content = content.replace('Log.i("LaborApplication", "FirebaseApp successfully initialized with FirebaseOptions.")', 'Log.i("LaborApplication", "FirebaseApp successfully initialized with FirebaseOptions.")' + init_str)
content = content.replace('Log.i("LaborApplication", "FirebaseApp already initialized.")', 'Log.i("LaborApplication", "FirebaseApp already initialized.")' + init_str)

with open('app/src/main/java/com/example/LaborApplication.kt', 'w') as f:
    f.write(content)
