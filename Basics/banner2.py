def banner_text(text: str = ' ',screen_width: int = 80) -> None:

    if len(text) > screen_width - 4:
        raise ValueError('string {0} is larger then speciefied width {1}'.format(text,screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        centered_text = text.center(screen_width - 4)
        output_string = "**{0}**".format(centered_text)
        print(output_string)


banner_text("*",60)
banner_text("Cheer up Brian, you know what they say?",60)
banner_text("Some things in life are bad",60)
banner_text("They can really make you mad",60)
banner_text(screen_width=60)
banner_text("Other things just make you swear and curse",60)
banner_text("When you're chewing on life's gristle",60)
banner_text("Don't grumble, give a whistle",60)
banner_text("And this'll help things turn out for the best",60)
banner_text("*",60)