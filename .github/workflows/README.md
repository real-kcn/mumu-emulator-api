# GitHub Actions Workflows

This directory contains GitHub Actions workflows for automated testing, building, and publishing.

## Workflows

### 1. Test Workflow (`test.yml`)

**Triggers:**
- Push to `master`, `main`, or `develop` branches
- Pull requests to `master` or `main` branches  
- Manual dispatch

**Jobs:**
- **test**: Runs tests across Python 3.7-3.12
  - Lints code with flake8
  - Tests package imports
  - Runs basic tests (continues on error due to MuMuManager dependency)
  
- **build-test**: Tests package building
  - Builds source and wheel distributions
  - Validates package with twine
  - Tests wheel installation

### 2. Publish Workflow (`publish.yml`)

**Triggers:**
- Tags starting with `v*` (e.g., `v1.0.0`)
- GitHub releases
- Manual dispatch

**Jobs:**
1. **build**: Creates distribution packages
2. **test-install**: Tests installation across Python versions
3. **publish-testpypi**: Publishes to TestPyPI (on tags or manual)
4. **publish-pypi**: Publishes to PyPI (on releases only)

## Setup Requirements

### Repository Secrets

Add these secrets to your GitHub repository:

1. **`PYPI_API_TOKEN`**: Your PyPI API token
   - Go to https://pypi.org/manage/account/token/
   - Create a new token with "Entire account" scope
   - Add to GitHub repo secrets

2. **`TEST_PYPI_API_TOKEN`**: Your TestPyPI API token  
   - Go to https://test.pypi.org/manage/account/token/
   - Create a new token with "Entire account" scope
   - Add to GitHub repo secrets

### Release Process

#### Automatic Release
1. Create and push a version tag:
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```
2. The workflow will automatically publish to TestPyPI

#### GitHub Release
1. Go to your repository's releases page
2. Click "Create a new release"
3. Choose your tag (e.g., `v1.0.0`)
4. Fill in release notes
5. Click "Publish release"
6. The workflow will publish to both TestPyPI and PyPI

#### Manual Testing
1. Go to repository Actions tab
2. Select "Publish to PyPI" workflow
3. Click "Run workflow"
4. This will publish to TestPyPI only

## Workflow Features

- **Multi-version testing**: Tests on Python 3.7-3.12
- **Build validation**: Checks package integrity with twine
- **Staged publishing**: TestPyPI first, then PyPI
- **Artifact storage**: Saves build artifacts between jobs
- **Error handling**: Continues on non-critical failures
- **Skip existing**: Won't fail if version already exists on TestPyPI