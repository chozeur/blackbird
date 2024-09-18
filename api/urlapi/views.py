import asyncio
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import StreamingHttpResponse

# Async URL generator function
async def generate_urls_async():
    urls = [
        "https://example.com/page1",
        "https://example.com/page2",
        "https://example.com/page3",
    ]
    for url in urls:
        await asyncio.sleep(2)  # Simulate delay in URL generation
        yield url

# Synchronous wrapper around the async URL generator
def generate_urls_sync():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    async_gen = generate_urls_async()  # Get the async generator
    try:
        while True:
            url = loop.run_until_complete(async_gen.__anext__())  # Fetch the next async URL
            yield f"{url}\n"  # Yield the URL, formatted as plain text with newline
    except StopAsyncIteration:
        pass
    finally:
        loop.close()

# DRF API view that uses StreamingHttpResponse
class URLStreamView(APIView):
    def get(self, request, *args, **kwargs):
        # Use StreamingHttpResponse to stream the synchronous generator
        response = StreamingHttpResponse(generate_urls_sync(), content_type="text/plain")
        return response
