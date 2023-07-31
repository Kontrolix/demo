import subprocess
import time
import random

pr_title = ["feat: A new feature", "fix: a fix", "chore: typo"]

try:
    for i in range(55):
        branch = f"{int(time.time())}_{i}"

        title = random.choice(pr_title)

        subprocess.check_call(["git", "checkout", "-b", branch])

        with open(f"dummy_files/{branch}.txt", "w") as f:
            f.write("foo")

        subprocess.check_call(["git", "add", "--all"])
        subprocess.check_call(["git", "commit", "-a", "-m", title])

        subprocess.call(["git", "push", "--set-upstream", "origin", branch])

        subprocess.check_call(
            [
                "gh",
                "pr",
                "create",
                "--title",
                title,
                "--body",
                title,
                "--base",
                "main",
            ]
        )
finally:
    subprocess.check_call(["git", "checkout", "main"])
