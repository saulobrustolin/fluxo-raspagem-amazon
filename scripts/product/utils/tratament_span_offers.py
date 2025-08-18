def tratament_span_offers(span):
    param = "Comparar outras ";

    ind = span.find(param);

    start = ind + len(param);
    end = span.find(" ", start + 1);

    return span[start:end];