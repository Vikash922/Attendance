with open('app/build.gradle.kts', 'r') as f:
    content = f.read()

new_signing_config = """  signingConfigs {
    create("release") {
      storeFile = file("release.keystore")
      storePassword = "attendance123"
      keyAlias = "attendance_alias"
      keyPassword = "attendance123"
    }
    create("debugConfig") {
      storeFile = file("release.keystore")
      storePassword = "attendance123"
      keyAlias = "attendance_alias"
      keyPassword = "attendance123"
    }
  }"""

import re
content = re.sub(r'  signingConfigs \{.*?\n  \}', new_signing_config, content, flags=re.DOTALL)

with open('app/build.gradle.kts', 'w') as f:
    f.write(content)
