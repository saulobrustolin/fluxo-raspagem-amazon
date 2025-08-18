def detect_span(span_list):
    param = "Comparar";

    for span in span_list:
        if span.find(param) != -1:
            return span 