import re


def extract_links(page: str) -> list[str]:
    """Extract internal links from a wikicode string.
    
    ```
    >>> extract_links("UPN est une [[Université]] située en [[Ile de France]].")
    ['[[Université]]', '[[Ile de France]]']
    """
    links = re.findall(r"\[\[.*?\]\]", page)
    return links


if __name__ == "__main__":
# pour que ça ne s'exécute pas quand on l'importe dans cli.py etc
    res = extract_links("UPN est une [[Université]] située en [[Ile de France]].")
    print(res)
