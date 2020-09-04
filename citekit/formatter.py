from datetime import datetime

from dateparser import parse


def format_harvard(data):
    result = []

    for d in data:
        if d["author"] is not None:
            if " " in d["author"]:
                citation = f"{d['author'].split()[1]}, {d['author'].split()[0]}, "
            else:
                citation = d["author"]
        else:
            citation = ""

        accessed = parse(d["accessed"])
        # print(d["url"], accessed)
        d["accessed"] = accessed.strftime("%d %B %Y")
        citation += f"{d['published']}, " if d['published'] else ''

        citation += "{title} [online] {domain} Available at: <{url}> [Accessed {accessed}]".format(
            **d
        )

        result.append(citation)

    result.sort()

    return result
