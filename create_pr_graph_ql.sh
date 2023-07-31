repo=Kontrolix/demo
repo_id="$(gh repo view "$repo" --json id -q .id)"
gh api graphql -F query=@too-quickly.graphql -f repo_id="$repo_id"