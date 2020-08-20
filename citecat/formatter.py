def format_harvard(data):
    result = []
    
    for d in data:
        citation = "{published}, {title} [online] Available at: <{url}> [Accessed 20 Aug 2020]".format(**d)
        
        result.append(citation)
    
    return result