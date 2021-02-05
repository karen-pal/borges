# Example usage of Scraper class for link recollection

from scraper import Scraper


def run():
    scraper = Scraper()
    text = scraper.get_links(url="https://ciudadseva.com/autor/silvina-ocampo/cuentos/")

    with open("links_silvina_ocampo.txt", "w") as f:
        for link in text:
            f.write(link + "\n")
    return text


run()
