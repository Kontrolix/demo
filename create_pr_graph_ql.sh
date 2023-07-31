repo=OWNER/MYREPO
repo_id=$(gh repo view "$repo" --json id -q .id)"
gh api graphql -F query=@too-quickly.graphql -f repo="$repo_id"