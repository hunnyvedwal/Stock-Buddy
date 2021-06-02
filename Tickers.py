from tkinter import ttk


def func(frame, name):
    if name == "Apple":
        wiki = ttk.Label(frame,
                         text='Apple Inc. is an American multinational technology company headquartered in '
                              'Cupertino, California, that designs, develops, and sells consumer '
                              'electronics, computer software, and online services. It is considered one of '
                              'the Big Five companies in the U.S. information technology industry, '
                              'along with Amazon, Google, Microsoft, and Facebook. It is one of '
                              'the most popular smartphone and tablet companies in the world.',
                         wraplength=240)

        wiki.place(x=0, y=0)
        ticker = "AAPL"

    if name == "Amazon":
        wiki = ttk.Label(frame, text='Amazon.com, Inc., is an American multinational '
                                     'technology company based in Seattle, Washington, which focuses on '
                                     'e-commerce, cloud computing, digital streaming, and artificial intelligence. '
                                     'It is one of the Big Five companies in the U.S. information technology '
                                     'industry, along with Google, Apple, Microsoft, and Facebook. '
                                     'The company has been referred to as "one of the most influential economic '
                                     'and cultural forces in the world", as well as the world\'s most valuable '
                                     'brand.', wraplength=240)
        wiki.place(x=0, y=0)
        ticker = "AMZN"

    if name == "Google":
        wiki = ttk.Label(frame, text='Google LLC is an American multinational technology company that specializes in '
                                     'Internet-related services and products, which include online advertising '
                                     'technologies, a search engine, cloud computing, software, and hardware. It is '
                                     'considered one of the five Big Tech companies along with Amazon, Facebook, '
                                     'Apple, '
                                     'and Microsoft. ', wraplength=240)
        wiki.place(x=0, y=0)
        ticker = 'GOOGL'

    if name == "Microsoft":
        wiki = ttk.Label(frame, text='Microsoft Corporation is an American multinational technology company with '
                                     'headquarters in Redmond, Washington. It develops, manufactures, licenses, '
                                     'supports, and sells computer software, consumer electronics, '
                                     'personal computers, and related services. Its best known software products '
                                     'are the Microsoft Windows line of operating systems, the Microsoft Office '
                                     'suite, and the Internet Explorer and Edge web browsers. ', wraplength=240)
        wiki.place(x=0, y=0)
        ticker = 'MSFT'

    if name == "Facebook":
        wiki = ttk.Label(frame, text='Facebook, Inc., is an American technology conglomerate based in Menlo Park, '
                                     'California. It was founded by Mark Zuckerberg, along with his fellow '
                                     'roommates and students at Harvard College, who were Eduardo Saverin, '
                                     'Andrew McCollum, Dustin Moskovitz and Chris Hughes, originally as '
                                     'TheFacebook.com—today\'s Facebook, a popular global social networking '
                                     'service. It is one of the world\'s most valuable companies. ', wraplength=240)
        wiki.place(x=0, y=0)

    if name == "IBM":
        wiki = ttk.Label(frame, text='International Business Machines Corporation (IBM) is an American multinational '
                                     'technology company headquartered in Armonk, New York, with operations in over '
                                     '170 countries. The company began in 1911, founded in Endicott, New York, '
                                     'as the Computing-Tabulating-Recording Company (CTR) and was renamed '
                                     '"International Business Machines" in 1924. IBM is incorporated in New York. ',
                         wraplength=240)
        wiki.place(x=0, y=0)
