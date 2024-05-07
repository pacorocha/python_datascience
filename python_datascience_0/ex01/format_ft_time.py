from datetime import datetime as dt

now = dt.now()
seconds = "{:,.4f}".format(now.timestamp())
scientific_notation = "{:e}".format(now.timestamp())

print(
    "Seconds since January 1, 1970: ",
    seconds,
    "or",
    scientific_notation,
    "in scientific notation",
)
print(now.strftime("%b %d %Y"))
