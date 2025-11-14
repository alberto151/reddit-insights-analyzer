thondef summarize_discussion(posts, comments):
    # Summarizes the filtered posts and comments into a short analysis.
    # A more advanced version could use NLP to summarize discussions.
summary = "Discussion Summary:\n"
summary += "\n".join([f"Post: {post}" for post in posts])
summary += "\n" + "\n".join([f"Comment: {comment}" for comment in comments])
return summary