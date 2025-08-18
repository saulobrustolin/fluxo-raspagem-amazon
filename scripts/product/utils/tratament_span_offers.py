def tratament_span_offers(span):
    param = "Comparar";
    print("Span", span)

    ind = span.find(param);
    print("Ind:" , ind)

    start = ind + len(param);
    print("Start", start)
    end = span.find(" ", start);
    print("End", end)

    return span[start:end];