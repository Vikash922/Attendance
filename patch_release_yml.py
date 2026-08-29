with open('.github/workflows/release.yml', 'r') as f:
    content = f.read()

release_step = """
      - name: Rename APK for Release
        run: mv app/build/outputs/apk/release/app-release.apk app/build/outputs/apk/release/Attendance-v${{ github.run_number }}.apk

      - name: Create GitHub Release
        uses: softprops/action-gh-release@v2
        if: github.ref == 'refs/heads/main'
        with:
          tag_name: v${{ github.run_number }}
          name: Laborbook Update v${{ github.run_number }}
          files: app/build/outputs/apk/release/Attendance-v${{ github.run_number }}.apk
"""

# wait, I need the apk file name to match the json!
# The json expects `app-release.apk`
release_step = """
      - name: Create GitHub Release
        uses: softprops/action-gh-release@v2
        if: github.ref == 'refs/heads/main'
        with:
          tag_name: v${{ github.run_number }}
          name: Laborbook Update v${{ github.run_number }}
          files: app/build/outputs/apk/release/app-release.apk
"""

content = content + release_step

with open('.github/workflows/release.yml', 'w') as f:
    f.write(content)
