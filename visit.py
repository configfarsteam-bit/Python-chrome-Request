import os, random, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

URL = os.getenv("TARGET_URL", "https://example.com")
WINDOW_MIN = 30
VISITS = 3

def visit():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=opts)
    try:
        driver.get(URL)
        time.sleep(5)  # مدت ماندن در صفحه
        print(f"[{time.strftime('%H:%M:%S')}] visited: {driver.title}")
    except Exception as e:
        print("error:", e)
    finally:
        driver.quit()

while True:
    minutes = sorted(random.sample(range(1, WINDOW_MIN + 1), VISITS))
    print("chosen minutes:", minutes)
    start = time.time()
    for m in minutes:
        wait = start + m * 60 - time.time()
        if wait > 0:
            time.sleep(wait)
        visit()
    # صبر تا پایان بازهٔ ۳۰ دقیقه‌ای، بعد انتخاب جدید
    rest = start + WINDOW_MIN * 60 - time.time()
    if rest > 0:
        time.sleep(rest)
