## What's this project about?
In a nutshell, this project provides an end-to-end data pipeline that scrapes blog posts from Linköping University (LiU) student blog, performs unsupervised topic modeling using BERTopic to discover core themes, and automatically categorizes the live posts using the WordPress REST API.
One will need the access as Web admin to run the exact same script but if you're thinking about automate classifying your posts on WordPress, check out the `tagger` folder ✨


### Project architecture
[ 1. Web Scraper ] ──> ( Raw Data / CSV ) ──> [ 2. Topic Modeling ] ──> ( Classified CSV ) ──> [ 3. WordPress REST API Tagger ]

### Directory structure
├── data/
│   ├── blog_posts.csv          # Scraped data from the website
│   ├── cmp_tagged_posts.csv  # Final output with mapped categories
│   ├── tagged_posts        # Tagged posts using BERTopic
│   └── tb_tagged.xlsx      # Posts that need to be tagged manually since they're not labelled by the topic model
├── crawler/
│   └── crawler.py             # Crawler functions
├── tagger/
│   ├── main.py             # Automated WordPress REST API tagging script
│   └── tag_functions.py    # Tagger functions
│
├── crawler_main.py         # Script to extract blog posts
├── requirements.txt           # Python dependencies
└── README.md


## How to run the tag automator 
At the root directory, run:
    `python -m tagger.main`

## Results of topic modeling
The model extracts a total of 7 topics from all the 611 posts. The 10 most common terms for each topic is shown below. 
![](./topic_terms.png)