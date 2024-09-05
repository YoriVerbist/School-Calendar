from bs4 import BeautifulSoup
import requests, itertools


def main():
    req = requests.get(
        "https://onderwijsaanbod.kuleuven.be/opleidingen/e/SC_51016883.htm"
        # "https://onderwijsaanbod.kuleuven.be/opleidingen/n/SC_51016775.htm"
    )

    soup = BeautifulSoup(req.text, "html.parser")
    soup = soup.find_all("div", {"class": "programma__content"})[0]

    lis_level2 = soup.find_all("li", {"class", "lilevel_2"})
    courses_map = {}
    for li2 in lis_level2:
        lis_level3 = li2.find_all("li", {"class", "lilevel_3"})
        for li in lis_level3:
            title_mandatory = find_element(li, "h4", {"class", "mandatory"})
            title_optional = find_element(li, "h4", {"class", "optional"})
            course_name = find_element(li, "td", {"class", "opleidingsonderdeel"})
            # if course_name:
            if title_mandatory:
                courses_map[title_mandatory[0]] = course_name
            if title_optional:
                courses_map[title_optional[0]] = course_name


def get_timeslots(course_name: str):
    pass


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
