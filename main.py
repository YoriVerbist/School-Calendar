from bs4 import BeautifulSoup
import requests


def main():
    req = requests.get(
        "https://onderwijsaanbod.kuleuven.be/opleidingen/e/SC_51016883.htm"
        # "https://onderwijsaanbod.kuleuven.be/opleidingen/n/SC_50527959.htm"
    )

    soup = BeautifulSoup(req.text, "html.parser")
    soup = soup.find_all("div", {"class": "programma__content"})[0]

    main_section_titles = find_h_element(soup, "h3", {"class", "mandatory"})

    tables = soup.find_all("table")

    for table in tables:
        rows = table.find_all("tr")
        print(rows)
        input()


def find_h_element(soup, h_element: str, args: dict):
    """
    This function searches for specific <h> tags in the soup and returns their values as a list.
    """

    section_titles = []

    mandatory_elements = soup.find_all(h_element, args)
    for mandatory in mandatory_elements:
        for child in mandatory.children:
            child = child.get_text(strip=True)
            if child != "":
                section_titles.append(child)
    return section_titles


if __name__ == "__main__":
    main()
