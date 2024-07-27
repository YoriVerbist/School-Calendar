from bs4 import BeautifulSoup
import requests


def main():
    req = requests.get(
        "https://onderwijsaanbod.kuleuven.be/opleidingen/e/SC_51016883.htm"
        # "https://onderwijsaanbod.kuleuven.be/opleidingen/n/SC_50527959.htm"
    )

    soup = BeautifulSoup(req.text, "html.parser")
    content = soup.find_all("div", {"class": "programma__content"})[0]
    mandatory_list = content.find_all("h3", {"class": "mandatory"})

    section_titles = []

    for mandatory in mandatory_list:
        for child in mandatory.children:
            child = child.get_text(strip=True)
            if child != "":
                section_titles.append(child)

    print(section_titles)


if __name__ == "__main__":
    main()
