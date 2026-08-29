with open('.github/workflows/release.yml', 'r') as f:
    content = f.read()

content = content.replace('jobs:\n  build:', 'permissions:\n  contents: write\n\njobs:\n  build:')

with open('.github/workflows/release.yml', 'w') as f:
    f.write(content)
