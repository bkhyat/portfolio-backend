import json
from vocab.models import VocabSource, Page, Word


def load_vocab(json_path: str):
    json_data = json.load(open(json_path))
    for data in json_data:
        vocab_source, _ = VocabSource.objects.get_or_create(source=data["source"], sheet=data["section"])
        for line in data["words"].split("\n"):
            print(line)
            page_no, words = line.split(".", maxsplit=1)
            page, _ = Page.objects.get_or_create(page=page_no, vocab_source=vocab_source)
            for word in words.split(","):
                Word.objects.get_or_create(word=word.strip(), page=page)

        # write to db
