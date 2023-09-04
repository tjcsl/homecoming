import bleach


def bleach_clean(text: str) -> str:
    return bleach.clean(
        text,
        tags=[
            "a",
            "b",
            "div",
            "iframe",
            "strong",
            "img",
            "table",
            "thead",
            "tbody",
            "th",
            "tr",
            "td",
            "hr",
            "br",
            "b",
            "i",
            "u",
            "s",
            "sup",
            "sub",
            "p",
            "ul",
            "ol",
            "li",
            "em",
            "blockquote",
        ],
        attributes={
            "*": ["title", "style"],
            "a": ["href"],
            "img": ["src", "alt"],
            "div": ["data-oembed-url"],
            "iframe": [
                "allowfullscreen",
                "mozallowfullscreen",
                "frameborder",
                "src",
                "tabindex",
                "webkitallowfullscreen",
            ],
        },
    )
