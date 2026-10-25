# Publish AIPracticalKit to PyPI

This project is packaged as `ai-practical-kit`; the Python import name is `ai_practical_kit`.

## Recommended method: PyPI Trusted Publishing with GitHub Actions

This method avoids storing a long-lived PyPI API token in GitHub. It requires a GitHub repository and an internet connection during publication.

### 1. Create a GitHub repository

Create a repository, for example `AIPracticalKit`, under your own GitHub account. Upload the **contents** of this project folder to the repository root (so `pyproject.toml` is at the root). Include `.github/workflows/publish.yml`.

### 2. Create the GitHub environment

In the GitHub repository, open **Settings → Environments**, create an environment named exactly `pypi`. The workflow uses this environment name.

### 3. Register the pending publisher on PyPI

Open https://pypi.org/manage/account/publishing/ and select **GitHub**. Enter:

- **PyPI Project Name:** `ai-practical-kit`
- **Owner:** your exact GitHub username or organization (not automatically your PyPI username)
- **Repository name:** the exact repository name you created, e.g. `AIPracticalKit`
- **Workflow name:** `publish.yml`
- **Environment name:** `pypi`

Click **Add**. This is a pending publisher: it does not reserve the package name until the first successful publishing workflow runs.

### 4. Commit and push the workflow

Confirm `.github/workflows/publish.yml` is at the repository root under `.github/workflows/` and that `pyproject.toml` is also at the repository root.

### 5. Publish the first release

The current package version is `1.1.0`. After the files are pushed, create a GitHub Release with tag `v1.1.0` and publish the release. That triggers the workflow to build the wheel and source archive, check them, and upload them to PyPI using Trusted Publishing.

If the project name was claimed by someone else before the first upload, the workflow will fail. In that case, choose a new unique `project.name` in `pyproject.toml`, rebuild, and update the PyPI pending publisher to match before publishing.

### 6. Verify

After a successful workflow, check https://pypi.org/project/ai-practical-kit/ . Then, on a computer with internet, install it with:

```powershell
py -m pip install ai-practical-kit
```

Use it in Python with:

```python
from ai_practical_kit import solve_8_queens

result = solve_8_queens()
print(result["total_solutions"])
```

Expected total: `92`.

## Alternative: manual upload with an API token

You do not need to use the Trusted Publisher screen if you prefer to upload manually. Follow the current PyPI packaging guide: https://packaging.python.org/en/latest/tutorials/packaging-projects/

From the project root, build and check the distributions:

```powershell
py -m pip install --upgrade build twine
py -m build
py -m twine check dist/*
```

Then create a PyPI API token in **Account settings → API tokens** and upload:

```powershell
py -m twine upload dist/*
```

When Twine prompts for credentials, use username `__token__` and paste the API token (including its `pypi-` prefix) as the password. Never put the token in source code or send it in chat. If the package does not yet exist, an account-scoped token may be required for the first upload; after creating the project, consider a project-scoped token and revoke the broader token.

## Offline use

PyPI publication does not make installation possible without internet on a new machine. For offline systems, copy the `.whl` file from `dist/` to the machine and install it locally:

```powershell
py -m pip install --no-index --no-deps .\dist\ai_practical_kit-1.1.0-py3-none-any.whl
```

The package itself has no third-party runtime dependencies. Python must already be installed on the computer.
