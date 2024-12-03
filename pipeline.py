import subprocess

# Define repository URL and branch
repo_url = 'https://github.com/vivek30490/Jenkins.git'
branch = 'main'

# Clone the repository
subprocess.run(['git', 'clone', '-b', branch, repo_url], check=True)

# Detect build tool and run build
if Path('pom.xml').exists():
    subprocess.run(['mvn', 'clean', 'package'], check=True)
elif Path('build.gradle').exists():
    subprocess.run(['./gradlew', 'clean', 'build'], check=True)
else:
    raise FileNotFoundError("No recognized build file found (pom.xml or build.gradle).")
