# SauceDemo UI Automation (Selenium + pytest + POM)

Otomasi pengujian https://www.saucedemo.com/ memakai Page Object Model.

## Struktur
- `pages/` : Page Objects (`BasePage`, `LoginPage`, `InventoryPage`)
- `tests/` : Skrip uji (`test_login.py`, `test_inventory.py`)
- `conftest.py` : fixture browser
- `pytest.ini` : konfigurasi pytest

## Menjalankan
```bash
python -m venv venv
source venv/bin/activate      
pip install -r requirements.txt
pytest -v
```


