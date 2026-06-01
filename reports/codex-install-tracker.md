# Codex Install Tracker — first safe batch (15 plugins)

**Update:** 14 installed successfully; `mermaid` failed during install due to an entry/manifest name mismatch — **fixed** (entry renamed to `mermaid-js-for-agents`). Test prompts in `post-install-test-checklist.md` / `codex-copy-paste-test-prompts.md`. Full record: `codex-install-tracker.csv`.

| # | Plugin | Category | Account/API | Risk | Installed? | Tested? | Result | Issue found | Next action |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `writers-loop` | Writing | No | Low | Yes | No | Pending | - | Run test prompt |
| 2 | `unslop` | Writing | No | Low | Yes | No | Pending | - | Run test prompt |
| 3 | `claude-mem` | Memory & Context | No | Low | Yes | No | Pending | - | Run test prompt |
| 4 | `pm-skills` | Project Management | No | Low | Yes | No | Pending | - | Run test prompt |
| 5 | `agentops` | Agent Orchestration | No | Low | Yes | No | Pending | - | Run test prompt |
| 6 | `session-orchestrator` | Agent Orchestration | No | Low | Yes | No | Pending | - | Run test prompt |
| 7 | `microsoft-docs` | Documentation | No | Low | Yes | No | Pending | - | Run test prompt |
| 8 | `citecheck` | Research & Fact-Checking | No | Low | Yes | No | Pending | - | Run test prompt |
| 9 | `github-librarian` | Research | No | Low | Yes | No | Pending | - | Run test prompt |
| 10 | `codebase-recon` | Coding | No | Low | Yes | No | Pending | - | Run test prompt |
| 11 | `brooks-lint` | Code Review | No | Low | Yes | No | Pending | - | Run test prompt |
| 12 | `commit-narrator` | Coding | No | Low | Yes | No | Pending | - | Run test prompt |
| 13 | `secret-guard` | Security | No | Low | Yes | No | Pending | - | Run test prompt |
| 14 | `env-lint` | Testing & QA | No | Low | Yes | No | Pending | - | Run test prompt |
| 15 | `mermaid-js-for-agents` | Diagrams | No | Low | Failed (entry renamed -> retry) | No | Fail (install) | entry/manifest name mismatch | Refresh Codex; retry install as 'mermaid-js-for-agents' |

**Note:** after refreshing Codex, retry the failed one under its corrected name `mermaid-js-for-agents`. See `mermaid-plugin-failure-report.md`.
