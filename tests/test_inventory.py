from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


class TestInventory:
    """Kasus uji alur inventori dan keranjang belanja."""

    def test_add_to_cart_flow(self, driver):
        """TC-04: Badge keranjang harus menampilkan '1' setelah menambah Backpack."""
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        inventory_page.add_backpack_to_cart()

        actual_count = inventory_page.get_cart_badge_count()
        assert actual_count == "1", (
            f"Badge keranjang tidak sesuai. Diharapkan: '1', Diterima: '{actual_count}'"
        )

    def test_logout_flow(self, driver):
        """TC-05: Logout mengalihkan ke halaman login dan tombol login tampil."""
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        inventory_page.logout()

        # Tunggu halaman login benar-benar tampil (Explicit Wait di BasePage)
        assert login_page.is_login_button_displayed() is True, (
            "Tombol login tidak tampil setelah logout!"
        )

        expected_url = "https://www.saucedemo.com/"
        actual_url = inventory_page.get_current_url()
        assert actual_url == expected_url, (
            f"URL setelah logout salah. Diharapkan: '{expected_url}', Diterima: '{actual_url}'"
        )