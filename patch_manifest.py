import re

with open('app/src/main/AndroidManifest.xml', 'r') as f:
    content = f.read()

# Disable allowBackup to prevent ADB data extraction
content = content.replace('android:allowBackup="true"', 'android:allowBackup="false"')

# Ensure networkSecurityConfig is used (optional, but good)
# Wait, let's just do allowBackup="false" and check exported="true"

# Let's fix exported="true" for Receiver. Since it listens to BOOT_COMPLETED,
# on newer Androids it MUST be exported="true". But we can add a permission requirement
# so ONLY system can broadcast to it? No, protected broadcasts cannot be sent by apps anyway.
# But what about android.intent.action.MY_PACKAGE_REPLACED? That's also protected.

with open('app/src/main/AndroidManifest.xml', 'w') as f:
    f.write(content)
