# Python Selenium Demo

A Python Selenium automation practice repository organized around **pytest** tests and page objects.

> Portfolio status: this is a learning/demo project. Automated CI execution and test stability have not yet been verified.

## Structure

| Directory | Purpose |
| --- | --- |
| `Tests/` | pytest test cases and fixtures |
| `pageObjects/` | reusable Selenium page interactions |
| `TestData/` | test input files |
| `Utilities/` | shared utilities |
| `assets/` | supporting assets |

## Getting started

1. Clone this repository and open it in your Python environment.
2. Create and activate a virtual environment.
3. Install Selenium and pytest: `python -m pip install selenium pytest`.
4. Ensure a supported browser and compatible driver are installed and accessible.
5. Review the target URL and browser configuration in the tests before running them.
6. Run `python -m pytest Tests -v`.

The repository does not currently include a verified dependency lockfile; dependency setup may require additional packages. Review the code before running against any non-demo site.

## Improvements planned

- Add pinned dependencies and documented browser setup.
- Remove generated HTML reports from source control.
- Make browser setup configurable and ensure teardown is reliable.
- Add CI smoke tests and verify execution.
- Add representative test screenshots only after verification.

## Related work

For my current Playwright + Behave framework, see [playwright-bdd-framework](https://github.com/sicvinay/playwright-bdd-framework).

**Maintainer:** Vinay B S
