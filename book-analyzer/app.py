import logging

from chalice import Chalice

from chalicelib.analyze import analyze_book

# Your public bucket from Lab 06
BUCKET = "public-fcc6wd"

app = Chalice(app_name="book-analyzer")

# Show the logger.info lines in CloudWatch
logging.getLogger().setLevel(logging.INFO)


@app.on_s3_event(
    bucket=BUCKET,
    events=["s3:ObjectCreated:*"],
    suffix=".txt"
)
def analyze_new_book(event):
    """Analyze a book when it is uploaded to BUCKET."""
    # TODO: call analyze_book() with the arguments it expects
    analyze_book(event.bucket, event.key)

