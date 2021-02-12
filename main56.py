import re

string = '''Reliance Industries Limited
           NSE 1,961.95   (1.26%)
           
           BSE 1,962.60   (1.29%)
           
           Search
           The Reliance Story
           Our Company
           Our Businesses
           Sustainability
           Innovation & R&D
           Investor Relations
           Careers
           eB2B
           
           
           
           Media Releases
           04Jan
           RIL Media Statement
           
           31Dec
           IUC Regime for Domestic Voice Calls Comes to an End
           
           18Dec
           Reliance and BP Announce First Gas from Asia’s Deepest Project
           
           More...
           Subscribe to our news alerts
           Email Id
           Reliance Foundation
            
           
           Reliance Foundation works with some of the most vulnerable and marginalized communities across India...
           Quick Links
           Response to Covid-19
           Fraud Alert
           Jio
           Reliance Retail
           AJIO
           Reliance Petroleum
           Dhirubhai Ambani International School
           Mumbai Indians
           JioGenNext
           Contact Us
           © 2020 Reliance Industries Limited. All rights reserved.
           numbers 
           ,91465356-534
           ,91456465-562
           ,91465655-535
           ,91235455-465
           ,91989570-696
           
           Site best viewed in IExplorer 9+ | Chrome 40+ | Firefox'''

# pattern = re.compile(r'Jio')

# matches = pattern.finditer(string)
# for match in matches:
#     print(match)
# print(matches)
# print(string[992:995])
# print(string[1155:1158])

# pattern = re.compile(r'.tail')
# pattern = re.compile(r'^Reliance')
# pattern = re.compile(r'Firefox$')
# pattern = re.compile(r'ai*')
# pattern = re.compile(r'ai+')
# pattern = re.compile(r'(ai){1}')
# pattern = re.compile(r'ai{2}')
# pattern = re.compile(r'ai{1}|t')

# Special Sequences

# pattern = re.compile(r'\AReliance')
# pattern = re.compile(r'\bReliance')
# pattern = re.compile(r'Reliance\b')
# pattern = re.compile(r'\d{6}-\d{3}')
pattern = re.compile(r'\b,91')
matches = pattern.finditer(string)
for match in matches:
    print(match)
    # print(string[1017:1022])
