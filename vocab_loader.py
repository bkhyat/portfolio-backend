import json
import django


def load_vocab(json_path: str):
    from vocab.models import VocabSource, Page, Word, Category, VocabWord
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


def load_vocab_new(json_path: str):
    from vocab.models import VocabSource, Page, Word, Category, VocabWord
    json_data = json.load(open(json_path))
    for data in json_data:
        category, _ = Category.objects.get_or_create(category_name=data["source"])
        sub_category, _ = Category.objects.get_or_create(category_name=data["section"], parent_category=category)
        for line in data["words"].split("\n"):
            page_no, words = line.split(".", maxsplit=1)
            page,_ = Category.objects.get_or_create(category_name=f"Page {page_no}", parent_category=sub_category)
            for word in words.split(","):
                VocabWord.objects.get_or_create(word=word.strip(), category=page)


if __name__ == "__main__":
    django.setup()
    load_vocab_new("vocab.json")
