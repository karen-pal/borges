# Example usage of Scraper class for link recollection

from scraper import Scraper


def run():
    scraper = Scraper()
    url = "https://ciudadseva.com/autor/mario-benedetti/cuentos/"
    text = scraper.get_links(url=url)

    with open("links_benedetti.txt", "w") as f:
        for link in text:
            f.write(link + "\n")
    print("Written links to ",f)
    return text


run()
