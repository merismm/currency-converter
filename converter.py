import requests
import json
import sys
from pprint import pprint

url = "http://data.fixer.io/api/latest?access_key=89aae4bb97079f6e159730ad3f000538"
data = requests.get(url).text
data2 = json.loads(data)
fx = data2["rates"]
currencies = [
    "AED : United Arab Emirates Dirham",
    "AFN : Afghan Afghani",
    "ALL : Albanian Lek",
    "AMD : Armenian Dram",
    "ANG : Netherlands Antilles Guilder",
    "AOA : Angolan Kwanza",
    "ARS : Argentine Peso",
    "AUD : Australian Dollar",
    "AWG : Aruban Florin",
    "AZN : Azerbaijan Manat",
    "BAM : Bosnia-Herzegovina Convertible Mark",
    "BBD : Barbadian Dollar",
    "BDT : Bangladeshi Taka",
    "BGN : Bulgarian Lev",
    "BHD : Bahraini Dinar",
    "BIF : Burundian Franc",
    "BMD : Bermudian Dollar",
    "BND : Bruneian Dollar",
    "BOB : Bolivian Bol&#237;viano",
    "BRL : Brazilian Real",
    "BSD : Bahamian Dollar",
    "BTC : Bitcoin",
    "BTN : Bhutanese Ngultrum",
    "BWP : Botswana Pula",
    "BYN : New Belarusian Ruble",
    "BYR : Belarusian Ruble",
    "BZD : Belize Dollar",
    "CAD : Canadian Dollar",
    "CDF : Congolese Franc",
    "CHF : Swiss Franc",
    "CLF : Chilean Unit of Account",
    "CLP : Chilean Peso,",
    "CNY : Chinese Yuan",
    "COP : Colombian Peso",
    "CRC : Costa Rican Colon",
    "CUC : Cuban Convertible Peso,",
    "CUP : Cuban Peso",
    "CVE : Cape Verdean Escudo",
    "CZK : Czech Republic Koruna",
    "DJF : Djiboutian Franc",
    "DKK : Danish Krone",
    "DOP : Dominican Peso",
    "DZD : Algerian Dinar",
    "EGP : Egyptian Pound",
    "ERN : Eritrean Nakfa",
    "ETB : Ethiopian Birr",
    "EUR : Euro",
    "FJD : Fijian Dollar",
    "FKP : Falkland Island Pound",
    "GBP : British Pound Sterling",
    "GEL : Georgian Lari",
    "GGP : Guernsey Pound",
    "GHS : Ghanaian Cedi",
    "GIP : Gibraltar Pound",
    "GMD : Gambian Dalasi",
    "GNF : Guinean Franc",
    "GTQ : Guatemalan Quetzal",
    "GYD : Guyanese Dollar",
    "HKD : Hong Kong Dollar",
    "HNL : Honduran Lempira",
    "HRK : Croatian Kuna",
    "HTG : Haitian Gourde",
    "HUF : Hungarian Forint",
    "IDR : Indonesian Rupiah",
    "ILS : Israeli Shekel",
    "IMP : Isle of Man Pound",
    "INR : Indian Rupee",
    "IQD : Iraqi Dinar",
    "IRR : Iranian Rial",
    "ISK : Icelandic Krona",
    "JEP : Jersey Pound",
    "JMD : Jamaican Dollar",
    "JOD : Jordanian Dinar",
    "JPY : Japanese Yen",
    "KES : Kenyan Shilling",
    "KGS : Kyrgyzstani Som",
    "KHR : Cambodian Riel",
    "KMF : Comorian Franc",
    "KPW : North Korean Won",
    "KRW : South Korean Won",
    "KWD : Kuwaiti Dinar",
    "KYD : Caymanian Dollar",
    "KZT : Kazakhstani Tenge",
    "LAK : Lao Kip",
    "LBP : Lebanese Pound",
    "LKR : Sri Lankan Rupee",
    "LRD : Liberian Dollar",
    "LSL : Basotho Loti",
    "LTL : Lithuanian litas",
    "LVL : Latvia Lats",
    "LYD : Libyan Dinar",
    "MAD : Moroccan Dirham",
    "MDL : Moldovan Leu",
    "MGA : Malagasy Ariary",
    "MKD : Macedonian Denar",
    "MMK : Burmese Kyat,",
    "MNT : Mongolian Tughrik",
    "MOP : Macau Pataca",
    "MRU : Mauritanian Ouguiya",
    "MUR : Mauritian Rupee",
    "MVR : Maldivian Rufiyaa",
    "MWK : Malawian Kwacha",
    "MXN : Mexican Peso",
    "MYR : Malaysian Ringgit",
    "MZN : Mozambican Metical",
    "NAD : Namibian Dollar",
    "NGN : Nigerian Naira",
    "NIO : Nicaraguan Cordoba",
    "NOK : Norwegian Krone",
    "NPR : Nepalese Rupee",
    "NZD : New Zealand Dollar",
    "OMR : Omani Rial",
    "PAB : Panamanian Balboa",
    "PEN : Peruvian Sol",
    "PGK : Papua New Guinean Kina",
    "PHP : Philippine Peso",
    "PKR : Pakistani Rupee",
    "PLN : Polish Zloty",
    "PYG : Paraguayan Guarani",
    "QAR : Qatari Riyal",
    "RON : Romanian Leu",
    "RSD : Serbian Dinar",
    "RUB : Russian Ruble",
    "RWF : Rwandan Franc",
    "SAR : Saudi Arabian Riyal",
    "SBD : Solomon Islander Dollar",
    "SCR : Seychellois Rupee",
    "SDG : Sudanese Pound",
    "SEK : Swedish Krona",
    "SGD : Singapore Dollar",
    "SHP : Saint Helenian Pound",
    "SLL : Sierra Leonean Leone",
    "SOS : Somali Shilling",
    "SRD : Surinamese Dollar",
    "STN : Sao Tomean Dobra",
    "SVC : Salvadoran Colon",
    "SYP : Syrian Pound",
    "SZL : Swazi Lilangeni",
    "THB : Thai Baht",
    "TJS : Tajikistani Somoni",
    "TMT : Turkmenistani Manat",
    "TND : Tunisian Dinar",
    "TOP : Tongan Pa&#039;anga",
    "TRY : Turkish Lira",
    "TTD : Trinidadian Dollar",
    "TWD : Taiwan New Dollar",
    "TZS : Tanzanian Shilling",
    "UAH : Ukrainian Hryvnia",
    "UGX : Ugandan Shilling",
    "USD : United States Dollar",
    "UYU : Uruguayan Peso",
    "UZS : Uzbekistani Som",
    "VEF : Venezuelan Bol&#237;var",
    "VND : Vietnamese Dong",
    "VUV : Ni-Vanuatu Vatu",
    "WST : Samoan Tala",
    "XAF : Central African CFA Franc BEAC",
    "XAG : Silver Ounce",
    "XAU : Gold Ounce",
    "XCD : East Caribbean Dollar",
    "XDR : IMF Special Drawing Rights",
    "XOF : CFA Franc",
    "XPF : CFP Franc",
    "YER : Yemeni Rial",
    "ZAR : South African Rand",
    "ZMK : Zambian Kwacha",
    "ZMW : Zambian Kwacha",
    "ZWL : Zimbabwean Dollar",
]


def displays_storage():
    file2 = open("conversion storage.txt", "r+")
    print(file2.read())
    file2.close()


def function1():
    query = input(
        "Please specify the amount of currency to convert, from currency, to currency (with space in between).\nPress "
        "SHOW to see list of currencies available. \n press DISPLAY to see previous transactions"
        "\nPress Q to quit. \n "
    )
    if query == "Q":
        sys.exit()
    elif query == "SHOW":
        pprint(currencies)
        function1()
    elif query == "DISPLAY":
        displays_storage()
        function1()

    else:
        qty, fromC, toC = query.split(" ")
        fromC = fromC.upper()
        toC = toC.upper()
        qty = float(round(int(qty), 2))
        amount = round(qty * fx[toC] / fx[fromC], 2)

        file1 = open("conversion storage.txt", "a")

        file1.write(
            f"{qty} of currency {fromC} amounts to {amount} of currency {toC} today\n"
        )

        file1.close()
        print(f"{qty} of currency {fromC} amounts to {amount} of currency {toC} today")


try:
    function1()
except KeyError:
    print("You seem to have inputted wrongly, retry!")
    function1()
