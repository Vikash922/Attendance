import re

with open('app/src/main/java/com/example/data/repository/LaborRepository.kt', 'r') as f:
    content = f.read()

import_str = """
import androidx.security.crypto.EncryptedSharedPreferences
import androidx.security.crypto.MasterKey
"""

content = content.replace('import android.content.SharedPreferences', 'import android.content.SharedPreferences' + import_str)

old_prefs = 'private val prefs: SharedPreferences? = context?.getSharedPreferences("laborbook_prefs", Context.MODE_PRIVATE)'

new_prefs = """private val prefs: SharedPreferences? = try {
        if (context != null) {
            val masterKey = MasterKey.Builder(context)
                .setKeyScheme(MasterKey.KeyScheme.AES256_GCM)
                .build()
            EncryptedSharedPreferences.create(
                context,
                "laborbook_secure_prefs",
                masterKey,
                EncryptedSharedPreferences.PrefKeyEncryptionScheme.AES256_SIV,
                EncryptedSharedPreferences.PrefValueEncryptionScheme.AES256_GCM
            )
        } else null
    } catch (e: Exception) {
        null
    }"""

content = content.replace(old_prefs, new_prefs)

with open('app/src/main/java/com/example/data/repository/LaborRepository.kt', 'w') as f:
    f.write(content)
