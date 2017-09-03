from flask import Flask, render_template
import config
import feedparser

rss_feed_links = config.rss_feed
results_dict = {}


app = Flask(__name__)


@app.route('/')
def rss_reader():
    for feed_link in rss_feed_links:
        d = feedparser.parse(feed_link)
        print("Total entries: ", len(d.entries))
        print("--------------------------------")
        for entry in d.entries:
            print("--------------------------------")
            print("Title :", entry.title)
            print("Link :", entry.link)
            results_dict[entry.title] = entry.link

    return render_template('index.html', results=results_dict)


if __name__ == '__main__':
    app.run()
