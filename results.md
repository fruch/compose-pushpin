Running for 25min with 10000 longpoll clients, that reconnect every 1m:

     Name                                                          # reqs      # fails     Avg     Min     Max  |  Median   req/s
    --------------------------------------------------------------------------------------------------------------------------------------------
     GET /hello/test                                               237109 107745(31.24%)   62493   59613   72720  |   62000  105.90
    --------------------------------------------------------------------------------------------------------------------------------------------
     Total                                                         237109 107745(45.44%)                                     105.90

    Error report
     # occurences       Error
    --------------------------------------------------------------------------------------------------------------------------------------------
     106802             GET /hello/test: "HTTPError(u'500 Server Error: Internal Server Error for url: http://127.0.0.1:33667/hello/test',)"
     900                GET /hello/test: "HTTPError(u'502 Server Error: Bad Gateway for url: http://127.0.0.1:33667/hello/test',)"
     43                 GET /hello/test: 'ConnectionError(ProtocolError(\'Connection aborted.\', BadStatusLine("\'\'",)),)'
    --------------------------------------------------------------------------------------------------------------------------------------------

