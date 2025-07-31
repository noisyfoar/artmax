from playwright.async_api import Page, Browser, async_playwright
import asyncio

class ReviewsParcer:

    def __init__(self, url=str):
        self.url = url


    async def get_reviews_data(self, page: Page):
        await page.goto(self.url)
        retries = 10
        left = retries
        count_review = 0
        review_list = None
        while left > 0:
            await asyncio.sleep(1)
            await page.locator("._1vgcy7c > ._3zzdxk > ._1667t0u > ._1rkbbi0x").evaluate("element => element.scrollTo(0, element.scrollHeight)")
            review_list = await page.query_selector_all("div._1k5soqfl")
            temp = len(review_list)
            if temp == count_review:
                left -= 1
            else:
                left = retries
                count_review = temp

        reviews_data = []
        review = []
        
        
        # username, text, date containers
        divs = ["span._16s5yj36","a._1wlx08h", "div._a5f6uz"] 
        for review_elem in review_list:
            for div in divs:
                temp = await review_elem.query_selector(div) # temp - data from container
                review.append(await temp.inner_text() if temp else "")
                            
            div_rating = await review_elem.query_selector("div._1fkin5c") # rating
            review.append(len(await div_rating.query_selector_all("span")) if div_rating else 0)
            if review[1] == "":
                temp = await review_elem.query_selector("a._1msln3t")
                review[1] = await temp.inner_text() if temp else ""
            reviews_data.append(review)
            review=[]    
        return reviews_data
    
    async def get_session(self):

        async with async_playwright() as p:
            browser = await p.chromium.launch(
                headless=True,
                args=[
                    '--no-sandbox',
                    '--disable-blink-features=AutomationControlled',
                    '--disable-web-security',
                    '--disable-dev-shm-usage',
                    '--disable-gpu',
                    '--disable-features=VizDisplayCompositor',
                ]
            )
            context = await browser.new_context(
                viewport = {"width": 1920,"height": 1080},
                user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            )
            page = await context.new_page()
            
            page.set_default_timeout(30000)
            page.set_default_navigation_timeout(30000)

            return await self.get_reviews_data(page)


