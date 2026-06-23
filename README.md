# UITAP — Page Object Model Practice Project

Selenium + pytest POM structure for [UI Test Automation Playground](http://uitestingplayground.com/).

---

## Setup in PyCharm

1. **Open the project** — File → Open → select the `uitap_pom` folder
2. **Create a virtual environment** — PyCharm usually prompts you; or manually:
   ```
   python -m venv venv
   ```
3. **Activate it** (in the PyCharm terminal):
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
4. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```
5. **Run all tests**:
   ```
   pytest
   ```
6. **Run a specific test file**:
   ```
   pytest tests/test_sample_app.py -v
   ```
7. **Run with visible output** (print statements):
   ```
   pytest -s
   ```

---

## Project Structure

```
uitap_pom/
│
├── pages/                    # Page Object classes
│   ├── base_page.py          # Parent class — shared helpers (wait, click, type)
│   ├── home_page.py
│   ├── sample_app_page.py    # Login/logout demo
│   ├── dynamic_id_page.py    # Stable selectors practice
│   ├── ajax_page.py          # Async wait practice
│   ├── text_input_page.py    # Reliable text entry
│   └── progress_bar_page.py  # Polling & timing practice
│
├── tests/                    # pytest test files
│   ├── test_home_page.py
│   ├── test_sample_app.py
│   ├── test_dynamic_id.py
│   ├── test_ajax.py
│   ├── test_text_input.py
│   └── test_progress_bar.py
│
├── conftest.py               # Shared pytest fixtures (WebDriver setup/teardown)
├── pytest.ini                # pytest config
└── requirements.txt
```

---

## Key Concepts Practised

| Page | Skill |
|---|---|
| Dynamic ID | Never rely on auto-generated IDs; use stable CSS/text |
| AJAX Data | WebDriverWait for content that loads asynchronously |
| Sample App | Login flows, dynamic attribute handling |
| Text Input | Reliable `clear()` + `send_keys()` patterns |
| Progress Bar | Polling loops, stopping at the right moment |

---

## Adding More Pages

1. Create `pages/new_page.py` inheriting from `BasePage`
2. Add locators as class-level tuples: `BUTTON = (By.CSS_SELECTOR, "#myBtn")`
3. Add action methods that use `self.click()`, `self.type_text()`, etc.
4. Create `tests/test_new_page.py` and inject `driver` via the fixture

The site has many more pages to explore — each is a new automation challenge!
