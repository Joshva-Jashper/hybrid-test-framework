<h1 align="center">🧪 Hybrid Test Framework</h1>
<p align="center">
  A production-ready hybrid automation framework combining <strong>UI</strong> and <strong>API</strong> testing,<br/>
  built with <strong>Playwright</strong> · <strong>pytest</strong> · <strong>Python</strong> · <strong>Allure</strong>
</p>
<p align="center">
  <a href="https://github.com/joshvajaspher6-dotcom/hybrid-test-framework/actions">
    <img src="https://github.com/joshvajaspher6-dotcom/hybrid-test-framework/actions/workflows/playwright-tests.yml/badge.svg" alt="CI Status"/>
  </a>
  <img src="https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white" alt="Python 3.11"/>
  <img src="https://img.shields.io/badge/Playwright-1.62.0-2EAD33?logo=playwright&logoColor=white" alt="Playwright"/>
  <img src="https://img.shields.io/badge/pytest-9.1.1-0A9EDC?logo=pytest&logoColor=white" alt="pytest"/>
  <img src="https://img.shields.io/badge/Allure-2.16.0-orange" alt="Allure"/>
  <img src="https://img.shields.io/badge/Docker-ready-2496ED?logo=docker&logoColor=white" alt="Docker"/>
</p>

---

## 📌 Overview

**Hybrid Test Framework** is a scalable, maintainable test automation suite targeting [automationexercise.com](https://automationexercise.com). It unifies **UI browser automation** (via Playwright) and **REST API testing** (via Playwright's `APIRequestContext`) under a single pytest-driven harness.

Key highlights:

- 🔀 **True hybrid tests** — `e2e` scenarios that mix API setup with UI verification (and vice versa)
- 🗂️ **Page Object Model** — clean separation of locators/actions from test logic
- 🔐 **Session-scoped authentication** — browser storage state persisted once per run, reused across all tests
- 📊 **Allure reporting** — rich HTML reports with screenshots, traces, and video attachments on failure
- 🐳 **Docker support** — run the full suite in an isolated container
- ♻️ **Auto-retry** — flaky tests automatically re-run up to 2 times

---

## 🏗️ Architecture

```
hybrid-test-framework/
├── .github/
│   └── workflows/
│       └── playwright-tests.yml   # CI/CD pipeline (GitHub Actions)
│
├── auth/
│   └── token.json                 # Persisted browser storage state (session auth)
│
├── pages/                         # Page Object Model layer
│   ├── ui/                        # UI page objects (Playwright Page)
│   │   ├── base_page.py           # Shared navigation actions
│   │   ├── login_signup_page.py   # Login & signup form interactions
│   │   ├── signup.py              # Full registration form
│   │   ├── cart.py                # Shopping cart actions
│   │   ├── products.py            # Product listing & search
│   │   ├── payment.py             # Checkout & payment flow
│   │   └── contact.py             # Contact Us page
│   └── api/                       # API client layer (Playwright APIRequestContext)
│       ├── user_client.py         # User CRUD endpoints
│       ├── product_client.py      # Product listing endpoints
│       ├── brands_client.py       # Brands endpoints
│       ├── user_login.py          # Login API client
│       └── update_client.py       # User update endpoint
│
├── tests/
│   ├── test_ui/                   # UI test suite
│   │   ├── conftest.py            # Fixtures: auth, browser context, page, tracing
│   │   ├── test_login.py          # Login / logout scenarios
│   │   ├── test_register.py       # User registration scenarios
│   │   ├── test_cart.py           # Cart & checkout scenarios
│   │   ├── test_product.py        # Product browsing & search
│   │   ├── test_contact_us.py     # Contact form submission
│   │   └── test_general.py        # General navigation checks
│   └── test_api/                  # API test suite
│       ├── conftest.py            # Fixtures: BaseApiClient, schema validator
│       ├── test_user.py           # User lifecycle (create, delete, get, edge cases)
│       ├── test_login_api.py      # Login API tests
│       ├── test_products_api.py   # Product & category API tests
│       ├── test_brand.py          # Brand API tests
│       ├── test_update_user.py    # User update tests
│       └── test_end_to_end.py     # Hybrid e2e flows (API <-> UI)
│
├── test_data/                     # Test data & JSON schemas
│   ├── api_schema.py              # JSON Schema definitions + Faker-generated payloads
│   ├── api_user.py                # Edge-case payloads (broken, missing fields)
│   ├── login.json                 # UI login data
│   ├── products.json              # Product test data
│   ├── category.json              # Category test data
│   └── add_to_cart.json           # Cart test data
│
├── utils/
│   └── read_file.py               # JSON file reader utility
│
├── pytest.ini                     # pytest configuration & default CLI options
├── requirements.txt               # Python dependencies
├── Dockerfile                     # Containerized test runner
└── .gitignore
```

---

## ✅ Test Coverage

### UI Tests (`@pytest.mark.ui`)

| Module | Scenarios Covered |
|---|---|
| `test_login.py` | Valid login, invalid credentials, logout |
| `test_register.py` | New user registration |
| `test_cart.py` | Add to cart, quantity update, checkout, payment |
| `test_product.py` | Product search, filter by category/brand |
| `test_contact_us.py` | Contact form submission |
| `test_general.py` | Navigation, homepage checks |

### API Tests (`@pytest.mark.api`)

| Module | Scenarios Covered |
|---|---|
| `test_user.py` | Create user, duplicate email, delete user, get by email, wrong data, missing fields |
| `test_login_api.py` | Successful login, invalid credentials |
| `test_products_api.py` | Get all products, search by name, category filter, schema validation |
| `test_brand.py` | Get all brands |
| `test_update_user.py` | Update user details via PUT |

### Hybrid E2E Tests (`@pytest.mark.e2e`)

| Test | Flow |
|---|---|
| `test_register_api_ui` | Create user via API → verify login via UI |
| `test_register_ui_api` | Register via UI → verify user exists via API |
| `test_delete_user_via_ui` | Create + delete user via API → verify login failure via UI |

### Smoke Tests (`@pytest.mark.smoke`)

Fast-running subset targeting critical paths — ideal for pre-deployment gates.

---

## 🚀 Getting Started

### Prerequisites

- Python **3.11+**
- `pip`
- `git`

### 1. Clone the Repository

```bash
git clone https://github.com/joshvajaspher6-dotcom/hybrid-test-framework.git
cd hybrid-test-framework
```

### 2. Create & Activate a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate        # macOS / Linux
.venv\Scripts\activate           # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright Browsers

```bash
playwright install --with-deps chromium
```

---

## ▶️ Running Tests

All options below use the defaults configured in `pytest.ini` (Chromium, screenshots/videos/traces retained on failure, Allure reporting).

### Run the Full Suite

```bash
pytest
```

### Run Only UI Tests

```bash
pytest -m ui
```

### Run Only API Tests

```bash
pytest -m api
```

### Run Only E2E Hybrid Tests

```bash
pytest -m e2e
```

### Run Smoke Tests

```bash
pytest -m smoke
```

### Target a Specific Test File

```bash
pytest tests/test_ui/test_cart.py
pytest tests/test_api/test_user.py
```

### Override Browser at Runtime

```bash
pytest --browser=firefox
pytest --browser=webkit
```

### Run Headed (Visible Browser Window)

```bash
pytest --headed
```

---

## 📊 Allure Reports

Allure results are generated automatically into `report/allure_result/`.

### Generate & Open the Report

```bash
# Install Allure CLI (once)
# macOS:       brew install allure
# Other OS:    https://allurereport.org/docs/install/

allure serve report/allure_result
```

On failure, the report automatically embeds:

- 📸 **Screenshots** — saved to `report/screenshot/`
- 🎬 **Videos** — saved to `report/videos/`
- 🔍 **Playwright Traces** — saved to `report/tracing/`, viewable at [trace.playwright.dev](https://trace.playwright.dev)

---

## 🐳 Running with Docker

Build and run the full test suite inside an isolated container:

```bash
# Build the image
docker build -t hybrid-test-framework .

# Run the suite
docker run --rm hybrid-test-framework
```

The `Dockerfile` installs all OS dependencies, Python packages, and Playwright browsers automatically — no local setup required.

---

## ⚙️ Configuration Reference

Key settings live in `pytest.ini`:

| Option | Default | Description |
|---|---|---|
| `--browser` | `chromium` | Browser engine (`chromium`, `firefox`, `webkit`) |
| `--base-url` | `https://automationexercise.com/` | Base URL for all UI tests |
| `--screenshot` | `only-on-failure` | When to capture screenshots |
| `--video` | `retain-on-failure` | When to record video |
| `--tracing` | `retain-on-failure` | When to save Playwright traces |
| `--alluredir` | `report/allure_result` | Allure results output directory |
| `--reruns` | `2` | Auto-retry count for flaky tests |
| `--reruns-delay` | `1` | Delay (seconds) between retries |

---

## 🔐 Authentication

UI tests use **session-scoped storage state** to avoid re-authenticating before every test:

1. A session-scoped fixture logs in once at the start of the run and saves the browser's cookies and localStorage to `auth/token.json`.
2. All subsequent browser contexts load this saved state — tests begin already authenticated.
3. Tests decorated with `@pytest.mark.no_auth` bypass this mechanism and start with a fresh, unauthenticated context (e.g., login page tests).

---

## 🔄 CI/CD

The project ships with a **GitHub Actions** workflow (`.github/workflows/playwright-tests.yml`) that triggers automatically on every push and pull request to `main` / `master`.

**Pipeline steps:**

| Step | Description |
|---|---|
| 1. Checkout | Clone the repository |
| 2. Python Setup | Configure Python 3.11 with pip cache |
| 3. Install Dependencies | `pip install -r requirements.txt` |
| 4. Install Playwright | Install Chromium + OS system deps |
| 5. Run Tests | Execute the full pytest suite |
| 6. Upload Artifacts | On failure: screenshots, traces & Allure results (retained 7 days) |

You can also trigger a run manually from the **Actions** tab via `workflow_dispatch`.

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|---|---|---|
| [Python](https://www.python.org/) | 3.11 | Core language |
| [Playwright](https://playwright.dev/python/) | 1.62.0 | Browser automation & API client |
| [pytest](https://docs.pytest.org/) | 9.1.1 | Test runner & fixture engine |
| [Allure pytest](https://allurereport.org/) | 2.16.0 | Rich HTML reporting |
| [Faker](https://faker.readthedocs.io/) | 40.36.0 | Dynamic test data generation |
| [jsonschema](https://python-jsonschema.readthedocs.io/) | 4.23.0 | API response schema validation |
| [pytest-rerunfailures](https://github.com/pytest-dev/pytest-rerunfailures) | 16.1.0 | Automatic flaky test retry |
| [pytest-base-url](https://github.com/pytest-dev/pytest-base-url) | 2.1.0 | Configurable base URL |
| [Docker](https://www.docker.com/) | — | Containerized test execution |

---

## 📁 Test Markers Reference

```ini
[pytest]
markers =
    ui:      UI browser automation tests
    api:     REST API tests
    e2e:     Hybrid end-to-end flows (API + UI combined)
    smoke:   Fast-running critical path tests
    no_auth: Tests requiring a fresh unauthenticated browser context
```

Combine markers for fine-grained filtering:

```bash
pytest -m "api and smoke"
pytest -m "not e2e"
pytest -m "ui or api"
```

---

## 🧬 Testing Strategy

This framework practices multiple layers of software testing to ensure comprehensive coverage:

| Testing Type | Description | Where Applied |
|---|---|---|
| **Functional Testing** | Validates that each feature works as expected against defined requirements | All UI & API test cases |
| **Smoke Testing** | A quick sanity check on the most critical paths to catch showstopper bugs fast | `@pytest.mark.smoke` tests |
| **API Testing** | Directly tests REST endpoints for correctness, status codes, response schemas, and edge cases | `tests/test_api/` |
| **UI / Browser Testing** | Automates real user interactions in a browser (clicks, form fills, navigation) | `tests/test_ui/` |
| **End-to-End (E2E) Testing** | Tests complete user journeys that span both API and UI layers in a single flow | `test_end_to_end.py` |
| **Hybrid Testing** | Combines API calls for test setup/teardown with UI assertions (and vice versa) for realistic, efficient test flows | `@pytest.mark.e2e` |
| **Negative Testing** | Verifies the system handles invalid inputs, duplicate data, and missing fields gracefully | `test_user.py`, `test_login_api.py` |
| **Schema Validation** | Ensures API responses conform to the expected JSON structure | `test_products_api.py`, `test_brand.py` |
| **Data-Driven Testing** | Runs the same test logic against multiple data sets from JSON files using `pytest.mark.parametrize` | Login, product, category, cart tests |
| **Regression Testing** | The full test suite acts as a regression safety net, automatically triggered on every push via CI | GitHub Actions pipeline |

---

<p align="center">Built with ❤️ using Playwright &amp; pytest &nbsp;·&nbsp; Crafted by Joshva Jaspher</p>
