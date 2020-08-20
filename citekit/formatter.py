def format_harvard(data):
    result = []

    for d in data:
        if " " in d["author"]:
            citation = f"{d['author'].split()[1]}, {d['author']}.split()[0]"
        else:
            citation = d["author"]

        citation += "{published}, {title} [online] {domain} Available at: <{url}> [Accessed 20 Aug 2020]".format(
            **d
        )

        result.append(citation)

    result.sort()

    return result
