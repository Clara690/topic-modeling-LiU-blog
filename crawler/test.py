from crawler import fetch_blog_title, fetch_blog_content

results = fetch_blog_title(1)

# try and see if the fetch_blog_content function works by fetching the content of the first blog post
first_blog_url = list(results.values())[0]
print(first_blog_url)
print(fetch_blog_content(first_blog_url))