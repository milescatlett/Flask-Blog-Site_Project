
title = "Hi I am a man"
slug = title.lower()
slug = slug.replace(" ", "-")
page = None
# page = "hi-i-am-a-man-5"
if page:
    last = page.split("-")[-1]
    if last.isdigit():
        slug = slug + "-" + str(int(last) + 1)
    else:
        slug = slug + "-1"

print(slug)


