with open('.github/workflows/release.yml', 'r') as f:
    content = f.read()

# Replace the build command back
content = content.replace(
    'gradle assembleRelease bundleRelease --no-daemon',
    'gradle assembleRelease --no-daemon'
)

# Remove the AAB step
aab_step = """
      - name: Upload Release AAB Artifact
        uses: actions/upload-artifact@v4
        with:
          name: Laborbook-Release-AAB
          path: app/build/outputs/bundle/release/*.aab
          retention-days: 90
"""
content = content.replace(aab_step, "")

with open('.github/workflows/release.yml', 'w') as f:
    f.write(content)
