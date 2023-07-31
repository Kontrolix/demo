import subprocess
import time
import random

pr_title = ["feat: A new feature", "fix: a fix", "chore: typo"]

for i in range(3):
    branch = f"{time.time()}_{i}"

    title = random.choice(pr_title)

    subprocess.check_call(f"git checkout -b {branch}")

    with open(f"dummy_files/{branch}.txt", "w") as f:
        f.write("foo")

    subprocess.check_call(f"!git add --all && git commit -a -m {title}")

    subprocess.check_call(f"git --set-upstream origin {branch}")

    subprocess.check_call(f"gh pr create --title {title} --body '{title}' --base main")
