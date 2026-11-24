import os

TEXT = "4/5 stars: I visited Earth and found one species that queues politely to be scanned, eats tiny pretzels mid-flight, then applauds itself for surviving its own transportation."


def render_text():
    text = TEXT.strip()
    if not text:
        raise ValueError("entry text must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry text must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry text must be between 1 and 200 characters")
    text.encode("utf-8")
    return text


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    payload = (render_text() + "\n").encode("utf-8")
    with open(output_path, "wb") as f:
        f.write(payload)
    with open(output_path, "rb") as f:
        if f.read() != payload:
            raise IOError("written entry did not verify byte-for-byte")


if __name__ == "__main__":
    main()
