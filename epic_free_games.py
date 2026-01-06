from playwright.sync_api import sync_playwright, TimeoutError
import time

FREE_GAMES_URL = "https://store.epicgames.com/en-US/free-games"
MAX_GAMES = 5
DELAY = 6


def wait(sec=DELAY):
    time.sleep(sec)


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        print("🌐 Opening Epic Games Store (Free Games page)...")
        page.goto(FREE_GAMES_URL, timeout=60000)

        print("\n🔐 LOGIN MANUALLY (NO TIME LIMIT)")
        print("👉 After login & verification is DONE, come back here")
        input("👉 Press ENTER to continue...")

        # ---- wait until free games are actually visible ----
        try:
            page.wait_for_selector("a[href*='/p/']", timeout=60000)
        except TimeoutError:
            print("❌ Free games still not visible.")
            print("ℹ Make sure you are logged in and on the Free Games page.")
            print("ℹ Script will now stop safely.")
            input("Press ENTER to close browser...")
            browser.close()
            return

        games = page.query_selector_all("a[href*='/p/']")
        print(f"\n🎮 Found {len(games)} free game links")

        claimed = 0

        for game in games:
            if claimed >= MAX_GAMES:
                print("🛑 Safety limit reached")
                break

            link = game.get_attribute("href")
            if not link:
                continue

            page.goto("https://store.epicgames.com" + link)
            wait()

            if page.locator("text=In Library").count() > 0:
                print("✔ Already in library — skipped")
                continue

            if page.locator("text=Get").count() == 0:
                print("⚠ GET button not found — skipped")
                continue

            choice = input("👉 Claim this game? (y/n): ").lower()
            if choice != "y":
                print("⏭ Skipped")
                continue

            try:
                page.click("text=Get", timeout=10000)
                print("🟢 GET clicked")
            except TimeoutError:
                print("❌ Failed to click GET")
                continue

            wait()

            try:
                checkbox = page.locator("input[type='checkbox']")
                if checkbox.count() > 0:
                    checkbox.first.check()
                    print("☑ Checkbox selected")
                    wait()
            except Exception:
                pass

            try:
                if page.locator("text=Place Order").count() > 0:
                    page.click("text=Place Order", timeout=10000)
                    print("✅ Game claimed")
                    claimed += 1
            except TimeoutError:
                print("❌ Failed final confirmation")

            wait()

        print("\n🎉 Finished safely!")
        print(f"✅ Games claimed: {claimed}")
        input("Press ENTER to close browser...")
        browser.close()


if __name__ == "__main__":
    main()
