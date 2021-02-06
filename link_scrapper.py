# Example usage of Scraper class for link recollection

from scraper import Scraper


def run():
    scraper = Scraper()
    url = "https://ciudadseva.com/autor/leonora-carrington/cuentos/"
    text = scraper.get_links(url=url)
    author = "carrington"
    with open("links_"+author+".txt", "w") as f:
        for link in text:
            f.write(link + "\n")
    print("Written links to ",f)
    scraper.close()
    return text


run()
