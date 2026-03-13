# GitLab API Operations Reference

Default instance: `https://gitlabs.inet.vn`
API base: `{instance}/api/v4`

## Reading Credentials

```bash
# Try common .env file patterns at project root
cat .env.staging 2>/dev/null || \
cat .env.development 2>/dev/null || \
cat .env.production 2>/dev/null || \
cat .env 2>/dev/null
```

Extract `GITLAB*_ACCESS_TOKEN` or `GITLAB_PRIVATE_TOKEN`. Mask in output (last 4 chars).

## Common Operations

```bash
# Project info (get project ID)
curl -s --header "PRIVATE-TOKEN: $TOKEN" \
  "$API/projects?search=project-name"

# List pipelines
curl -s --header "PRIVATE-TOKEN: $TOKEN" \
  "$API/projects/$PID/pipelines"

# Pipeline jobs
curl -s --header "PRIVATE-TOKEN: $TOKEN" \
  "$API/projects/$PID/pipelines/$PLID/jobs"

# Job log (trace)
curl -s --header "PRIVATE-TOKEN: $TOKEN" \
  "$API/projects/$PID/jobs/$JID/trace"

# Trigger pipeline
curl -s -X POST --header "PRIVATE-TOKEN: $TOKEN" \
  "$API/projects/$PID/pipeline?ref=main"

# List branches
curl -s --header "PRIVATE-TOKEN: $TOKEN" \
  "$API/projects/$PID/repository/branches"

# Open merge requests
curl -s --header "PRIVATE-TOKEN: $TOKEN" \
  "$API/projects/$PID/merge_requests?state=opened"

# Search issues (for KPI linkage)
curl -s --header "PRIVATE-TOKEN: $TOKEN" \
  "$API/projects/$PID/issues?search=keyword"

# List project members
curl -s --header "PRIVATE-TOKEN: $TOKEN" \
  "$API/projects/$PID/members"
```

## Token Types

| Type | Scope | Usage |
|------|-------|-------|
| Project Access Token | project-scoped | CI/CD, repo operations |
| Private Token | user-scoped (read_api) | Cross-project queries, issue search |

All tokens configured at: GitLab → Settings → Access Tokens.
CI/CD uses project-level endpoints: `/api/v4/projects/:id/...`
