from math import ceil


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / 4))

    def add_photo(self, label: str) -> str:
        for i, page in enumerate(self.photos):
            i += 1
            if len(page) < 4:
                page.append(label)
                return f"{label} photo added successfully on page {i} slot {len(page)}"
        return f"No more free slots"

    def display(self) -> str:
        result = []
        separator = "-" * 11
        result.append(separator)
        for page in self.photos:
            result.append(" ".join("[]" for _ in page))
            result.append(separator)

        return "\n".join(result)


# test code
album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
