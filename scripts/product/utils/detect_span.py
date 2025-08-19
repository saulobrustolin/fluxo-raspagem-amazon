def detect_span(span_list):
    param = "Comparar outras "
    element_span = None

    for span in span_list:
        try:
            span = str(span.getText())
            if param in span:
                element_span = span
                print("Encontrado:", element_span)
                break
        except Exception as e:
            print("Erro:", e)
            continue
    
    if element_span is None:
        return None
    print('[offers] element_span não é None')

    # tratar o span encontrado
    print("span:", element_span)
    len_param = len(param)
    end = element_span.find(" ", len_param)
    if end == -1:
        # se não encontrar espaço, pega até o final da string
        end = len(element_span)

    return element_span[len_param:end]
