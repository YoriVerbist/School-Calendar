from bs4 import BeautifulSoup
import requests


def main():
    req = requests.get(
        "https://onderwijsaanbod.kuleuven.be/opleidingen/e/SC_51016883.htm"
        # "https://onderwijsaanbod.kuleuven.be/opleidingen/n/SC_50527959.htm"
    )

    soup = BeautifulSoup(req.text, "html.parser")
    soup = soup.find_all("div", {"class": "programma__content"})[0]

    main_section_titles = find_element(soup, "h3", {"class", "mandatory"})

    lis_level2 = soup.find_all("li", {"class", "lilevel_2"})
    titles_level2 = []
    for li in lis_level2:
        title_mandatory = find_element(li, "h4", {"class", "mandatory"})
        if title_mandatory:
            titles_level2.append(title_mandatory)
        title_optional = find_element(li, "h4", {"class", "optional"})
        if title_optional:
            titles_level2.append(title_optional)
    print(titles_level2)

    lis_level3 = soup.find_all("li", {"class", "lilevel_3"})
    titles_level3 = []
    for li in lis_level3:
        course_name = find_element(li, "td", {"class", "opleidingsonderdeel"})
        if course_name:
            titles_level3.append(course_name)
    print(titles_level3)


def find_element(soup, h_element: str, args: dict):
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
