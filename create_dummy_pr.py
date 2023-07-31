import subprocess
import time
import random

pr_title = ["feat: A new feature", "fix: a fix", "chore: typo"]

graphql_query_template = 'i{}: createPullRequest(input: {{ baseRefName: "main", headRefName: "{}", repositoryId: $repo_id, title: "{}" }}){{pullRequest{{ url }} }}'
graphql_query = []
try:
    for i in range(50):
        branch = f"{int(time.time())}_{i}"

        title = random.choice(pr_title)

        subprocess.check_call(["git", "checkout", "-b", branch])

        with open(f"dummy_files/{branch}.txt", "w") as f:
            f.write("foo")

        subprocess.check_call(["git", "add", "--all"])
        subprocess.check_call(["git", "commit", "-a", "-m", title])

        subprocess.call(["git", "push", "--set-upstream", "origin", branch])

        graphql_query.append(graphql_query_template.format(i, branch, title))

    with open("too-quickly.graphql", "w") as f:
        f.write(f"mutation($repo_id: ID!) {{{','.join(graphql_query)}}}")

    # NOTE: correspond à: gh repo view Kontrolix/demo --json id -q .id
    repo_id = "R_kgDOKBn23Q"
    subprocess.call(
        [
            "gh",
            "api",
            "graphql",
            "-F",
            "query=@too-quickly.graphql",
            "-f",
            f"repo_id={repo_id}",
        ]
    )
finally:
    subprocess.check_call(["git", "checkout", "main"])
