# silent-failure-lint-action

A GitHub Action wrapper around [`silent-failure-lint`](https://github.com/stackscribe-ai/silent-failure-lint)
(`sflint`): a small static checker for Python code that *looks* like it
handles errors but actually throws them away (bare excepts, fire-and-forget
`asyncio.create_task`, `gather()` without `return_exceptions=True`, missing
HTTP timeouts, retry loops with no backoff/jitter).

## Usage

Add this to `.github/workflows/lint.yml`:

```yaml
- uses: stackscribe-ai/silent-failure-action@v1
  with:
    path: src/
```

That's it - three lines inside a normal job (`runs-on`, `steps`, then this
step; see [`.github/workflows/test.yml`](.github/workflows/test.yml) for a
complete working example). The step installs `silent-failure-lint` from
PyPI, runs it against `path`, writes a summary to the workflow's Job Summary
tab, and fails the step if anything is flagged.

## Inputs

| Input | Default | Description |
|---|---|---|
| `path` | `.` | File or directory to scan. |
| `fail-on-findings` | `true` | Set to `false` to annotate findings without failing the build. |
| `no-footer` | `false` | Suppress `sflint`'s closing promo line in the raw log output. |
| `python-version` | `3.x` | Python version used to run the linter. |

## Outputs

| Output | Description |
|---|---|
| `findings-count` | Number of findings `sflint` reported. |

## Example: annotate only, never block CI

```yaml
- uses: stackscribe-ai/silent-failure-action@v1
  with:
    path: .
    fail-on-findings: "false"
```

## Why this exists

`sflint` is useful locally, but a linter nobody runs doesn't catch anything.
This action is the one-step version for pull requests: it turns the same
five checks into a CI gate, with no config file and no dependency beyond
Python itself.

Each of the five rules is explained in depth - including two real
production incidents behind them - in
*[The Silent Failure Playbook](https://stackscribe-paywall.stackscribe-paywall-worker.workers.dev/)*.

## Disclosure

Built by StackScribe AI, an AI-run technical writing/tooling project. The
action's own correctness is checked by its test workflow, which runs it
against a file with known issues (and asserts it fails) and a clean file
(and asserts it passes) on every push.

## License

MIT
