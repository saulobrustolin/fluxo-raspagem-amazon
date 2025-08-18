def detect_span(span_list):
    try:
        param = "Comparar outras ";

        for span in span_list:
            if span.find(param) != -1:
                return span
    except:
        return