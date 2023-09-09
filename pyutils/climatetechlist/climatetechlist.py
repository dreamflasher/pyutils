import asyncio
import time

from flask import Flask, render_template, request
from playwright.sync_api import sync_playwright

app = Flask(
    __name__,
)

async def get_response(page):
    response = await page.waitForResponse(lambda response : response.url == "https://www.climatetechlist.com/api/jobs" and response.status == 200 )
    return response.text()
    
@app.route("/clmttchlst", methods=["GET"])
def fetch() -> str:
    """
    Endpoint to fetch ui.

    Returns:
        Processed html string
    """

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto(request.args["url"])
        print(request.args["url"])
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        response = loop.run_until_complete(get_response(page))
        print(response)
        return response


if __name__ == "__main__":
    port = 8884
    app.run(host="127.0.0.1", port=port, debug=False)  # noqa:S104,S201