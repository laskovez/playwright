import re
from time import sleep

from playwright.sync_api import Page, expect

def navigate_to_playwright(page: Page):
    page.goto("https://playwright.dev/")
    sleep(1)

def test_has_title(page: Page):
    navigate_to_playwright(page)
    expect(page).to_have_title(re.compile("Playwright"))

def click_get_started(page: Page):
    page.get_by_role("link", name="Get started").click()

def test_get_started_link(page: Page):
    navigate_to_playwright(page)
    click_get_started(page)
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
